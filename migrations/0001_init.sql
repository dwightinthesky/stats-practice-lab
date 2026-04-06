CREATE TABLE IF NOT EXISTS sessions (
  session_id TEXT PRIMARY KEY,
  username TEXT NOT NULL,
  display_name TEXT NOT NULL,
  expires_at TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS sessions_expiry_idx
  ON sessions (expires_at);

CREATE TABLE IF NOT EXISTS question_progress (
  username TEXT NOT NULL,
  question_id INTEGER NOT NULL,
  status TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (username, question_id)
);

CREATE TABLE IF NOT EXISTS part_state (
  username TEXT NOT NULL,
  question_id INTEGER NOT NULL,
  part_id TEXT NOT NULL,
  selected_keys TEXT NOT NULL DEFAULT '[]',
  checked INTEGER NOT NULL DEFAULT 0,
  revealed INTEGER NOT NULL DEFAULT 0,
  is_correct INTEGER,
  attempts INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (username, question_id, part_id)
);

CREATE TABLE IF NOT EXISTS answer_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  question_id INTEGER NOT NULL,
  part_id TEXT NOT NULL,
  selected_keys TEXT NOT NULL DEFAULT '[]',
  checked INTEGER NOT NULL DEFAULT 0,
  revealed INTEGER NOT NULL DEFAULT 0,
  is_correct INTEGER,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS answer_records_user_created_idx
  ON answer_records (username, created_at DESC);
