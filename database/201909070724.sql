ALTER TABLE biometrics ADD COLUMN activity INTEGER DEFAULT 1;
ALTER TABLE biometrics ALTER COLUMN datetime SET DEFAULT now();