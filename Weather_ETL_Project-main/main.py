import subprocess

print("=" * 50)
print("🚀 WEATHER ETL PIPELINE")
print("=" * 50)

print("\n📥 Step 1: Extract")
subprocess.run(["python", "scripts/extract.py"])

print("\n🔄 Step 2: Transform")
subprocess.run(["python", "scripts/transform.py"])

print("\n📤 Step 3: Load")
subprocess.run(["python", "scripts/load.py"])

print("\n🎉 ETL Pipeline Completed Successfully!")