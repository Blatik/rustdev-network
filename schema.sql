-- Create leads table
CREATE TABLE IF NOT EXISTS leads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  niche TEXT NOT NULL,
  niche_name TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster queries
CREATE INDEX IF NOT EXISTS idx_created_at ON leads(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_email ON leads(email);
