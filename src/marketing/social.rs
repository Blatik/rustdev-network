use async_trait::async_trait;

#[async_trait]
pub trait SocialBot {
    async fn post(&self, content: &str) -> Result<(), String>;
}

pub struct MastodonClient {
    pub instance_url: String,
    pub access_token: String,
    pub client: reqwest::Client,
}

impl MastodonClient {
    pub fn new(instance_url: String, access_token: String) -> Self {
        Self {
            instance_url,
            access_token,
            client: reqwest::Client::new(),
        }
    }
}

#[async_trait]
impl SocialBot for MastodonClient {
    async fn post(&self, content: &str) -> Result<(), String> {
        let url = format!("{}/api/v1/statuses", self.instance_url);
        
        let params = [("status", content)];

        let res = self.client.post(&url)
            .header("Authorization", format!("Bearer {}", self.access_token))
            .form(&params)
            .send()
            .await
            .map_err(|e| e.to_string())?;

        if res.status().is_success() {
            Ok(())
        } else {
            Err(format!("Failed to post: {}", res.status()))
        }
    }
}

// Mock client for testing/dry-run
pub struct MockSocialClient;

#[async_trait]
impl SocialBot for MockSocialClient {
    async fn post(&self, content: &str) -> Result<(), String> {
        println!("[MOCK SOCIAL] Posting: {}", content);
        Ok(())
    }
}
