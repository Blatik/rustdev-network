use axum::{
    extract::Multipart,
    http::StatusCode,
    response::{IntoResponse, Response},
    body::Body,
};
use image::ImageReader;
use std::io::Cursor;
use image::ImageFormat;

pub async fn process_image(mut multipart: Multipart) -> impl IntoResponse {
    let mut image_data = None;
    let mut target_width = None;
    let mut target_height = None;
    let mut format = ImageFormat::Png; // Default

    while let Some(field) = multipart.next_field().await.unwrap() {
        let name = field.name().unwrap().to_string();
        
        if name == "image" {
            let data = field.bytes().await.unwrap();
            image_data = Some(data);
        } else if name == "width" {
            if let Ok(val) = field.text().await.unwrap().parse::<u32>() {
                target_width = Some(val);
            }
        } else if name == "height" {
            if let Ok(val) = field.text().await.unwrap().parse::<u32>() {
                target_height = Some(val);
            }
        } else if name == "format" {
            let val = field.text().await.unwrap();
            match val.as_str() {
                "jpeg" | "jpg" => format = ImageFormat::Jpeg,
                "webp" => format = ImageFormat::WebP,
                _ => {},
            }
        }
    }

    if let Some(data) = image_data {
        let img = match ImageReader::new(Cursor::new(data)).with_guessed_format() {
            Ok(reader) => match reader.decode() {
                Ok(img) => img,
                Err(_) => return (StatusCode::BAD_REQUEST, "Failed to decode image").into_response(),
            },
            Err(_) => return (StatusCode::BAD_REQUEST, "Failed to read image format").into_response(),
        };

        let processed = if let (Some(w), Some(h)) = (target_width, target_height) {
            img.resize_exact(w, h, image::imageops::FilterType::Lanczos3)
        } else {
            img
        };

        let mut buffer = Cursor::new(Vec::new());
        match processed.write_to(&mut buffer, format) {
            Ok(_) => {
                let body = Body::from(buffer.into_inner());
                let content_type = match format {
                    ImageFormat::Jpeg => "image/jpeg",
                    ImageFormat::WebP => "image/webp",
                    _ => "image/png",
                };
                
                Response::builder()
                    .header("Content-Type", content_type)
                    .body(body)
                    .unwrap()
            },
            Err(_) => (StatusCode::INTERNAL_SERVER_ERROR, "Failed to encode image").into_response(),
        }
    } else {
        (StatusCode::BAD_REQUEST, "Missing image field").into_response()
    }
}
