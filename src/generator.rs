use csv::ReaderBuilder;
use serde::{Deserialize, Serialize};
use std::error::Error;
use std::fs;
use tera::{Context, Tera};

#[derive(Debug, Deserialize, Serialize, Clone)]
struct Niche {
    id: String,
    title: String,
    headline: String,
    description: String,
    keywords: String,
    domain_suggestion: String,
    #[serde(skip_deserializing, default)]
    slug: String,
}

// Convert title to SEO-friendly slug
fn slugify(text: &str) -> String {
    text.to_lowercase()
        .replace("&", "and")
        .replace(" ", "-")
        .chars()
        .filter(|c| c.is_alphanumeric() || *c == '-')
        .collect::<String>()
        .split('-')
        .filter(|s| !s.is_empty())
        .collect::<Vec<&str>>()
        .join("-")
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("🚀 Lead Gen Site Generator Starting...");

    // Load Tera templates
    let tera = Tera::new("templates/**/*.html")?;

    // Read niches from CSV
    let mut reader = ReaderBuilder::new()
        .has_headers(true)
        .from_path("niches.csv")?;

    let mut sites_generated = 0;

    // API URL - Updated for Rust API (Production Shuttle)
    const API_URL: &str = "https://lead-gen-api-fsoe.shuttle.app/leads";

    // Store sites for root index (with slugs)
    let mut sites_data = Vec::new();

    for result in reader.deserialize() {
        let mut niche: Niche = result?;
        
        // Generate SEO-friendly slug from title
        let slug = slugify(&niche.title);
        niche.slug = slug.clone();
        
        // Store niche with slug for index
        sites_data.push(niche.clone());

        println!("📄 Generating site for: {} ({})", niche.title, slug);

        // Create context for template
        let mut context = Context::new();
        context.insert("id", &niche.id);
        context.insert("title", &niche.title);
        context.insert("headline", &niche.headline);
        context.insert("description", &niche.description);
        context.insert("keywords", &niche.keywords);
        context.insert("api_url", API_URL);
        context.insert("slug", &slug);

        // Render template
        let html = tera.render("landing.html", &context)?;

        // Create output directory with SEO-friendly name
        let output_dir = format!("output/{}", slug);
        fs::create_dir_all(&output_dir)?;

        // Write HTML file
        let output_path = format!("{}/index.html", output_dir);
        fs::write(&output_path, html)?;

        println!("✅ Generated: {}", output_path);
        sites_generated += 1;
    }

    // Generate About Page
    println!("📄 Generating About Page...");
    let mut about_context = Context::new();
    about_context.insert("api_url", API_URL);
    let about_html = tera.render("about.html", &about_context)?;
    fs::write("output/about.html", about_html)?;
    println!("✅ Generated: output/about.html");

    // Generate Root Index Page
    println!("📄 Generating Root Index Page...");
    let mut index_context = Context::new();
    index_context.insert("sites", &sites_data);
    let index_html = tera.render("root_index.html", &index_context)?;
    fs::write("output/index.html", index_html)?;
    println!("✅ Generated: output/index.html");

    // Get current date
    let today = chrono::Utc::now().format("%Y-%m-%d").to_string();

    // Generate Sitemap
    println!("🗺️ Generating Sitemap...");
    let mut sitemap = String::from(r#"<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://blatik.github.io/rustdev-network/</loc>
    <lastmod>"#);
    sitemap.push_str(&today);
    sitemap.push_str(r#"</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://blatik.github.io/rustdev-network/about.html</loc>
    <lastmod>"#);
    sitemap.push_str(&today);
    sitemap.push_str(r#"</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://blatik.github.io/rustdev-network/thank-you.html</loc>
    <lastmod>"#);
    sitemap.push_str(&today);
    sitemap.push_str(r#"</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
"#);

    for site in &sites_data {
        sitemap.push_str(&format!(r#"  <url>
    <loc>https://blatik.github.io/rustdev-network/{}/</loc>
    <lastmod>{}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
"#, site.slug, today));
    }

    sitemap.push_str("</urlset>");
    fs::write("output/sitemap.xml", sitemap)?;
    println!("✅ Generated: output/sitemap.xml");

    println!("\n🎉 Successfully generated {} sites + Index + About + Sitemap!", sites_generated);
    println!("📂 Check the 'output' directory");

    Ok(())
}
