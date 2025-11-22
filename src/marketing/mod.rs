use serde::{Deserialize, Serialize};
use std::sync::Arc;
use tokio::sync::Mutex;

pub mod social;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AffiliateLink {
    pub id: String,
    pub name: String,
    pub url: String,
    pub category: String, // e.g., "hosting", "vpn"
    pub payout: String,   // e.g., "$50 CPA"
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Campaign {
    pub id: String,
    pub name: String,
    pub templates: Vec<String>, // e.g., "Check out {product} for fast hosting!"
    pub target_link_id: String,
}

pub struct MarketingEngine {
    links: Arc<Mutex<Vec<AffiliateLink>>>,
    campaigns: Arc<Mutex<Vec<Campaign>>>,
}

impl MarketingEngine {
    pub fn new() -> Self {
        Self {
            links: Arc::new(Mutex::new(Vec::new())),
            campaigns: Arc::new(Mutex::new(Vec::new())),
        }
    }

    pub async fn add_link(&self, link: AffiliateLink) {
        let mut links = self.links.lock().await;
        links.push(link);
    }

    pub async fn add_campaign(&self, campaign: Campaign) {
        let mut campaigns = self.campaigns.lock().await;
        campaigns.push(campaign);
    }

    pub async fn generate_post(&self) -> Option<String> {
        let campaigns = self.campaigns.lock().await;
        let links = self.links.lock().await;

        if campaigns.is_empty() || links.is_empty() {
            return None;
        }

        // Simple rotation logic for MVP: pick first campaign
        // In real app: random or weighted rotation
        let campaign = &campaigns[0];
        
        if let Some(link) = links.iter().find(|l| l.id == campaign.target_link_id) {
            // Pick first template
            let template = &campaign.templates[0];
            let post = template.replace("{product}", &link.name)
                               .replace("{url}", &link.url);
            Some(post)
        } else {
            None
        }
    }
}
