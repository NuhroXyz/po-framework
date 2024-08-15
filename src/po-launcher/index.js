#!/usr/bin/env node
const { execSync } = require('child_process');
const path = require('path');

// Get the command-line arguments
const args = process.argv.slice(2);

// Define the path to your Python script
const scriptPath = path.join(__dirname, 'po_init.py');

// Build the command to run the Python script
const command = `python3 ${scriptPath} ${args.join(' ')}`;

try {
  // Execute the Python script
  const result = execSync(command, { encoding: 'utf-8' });
  console.log(result);
} catch (error) {
  console.error(`Error executing Python script: ${error.message}`);
}
