import pandas as pd
import os

def generate_haunting_report(input_csv, output_dir="results/irr"):
    """
    Filters for 'Ironclad' results: Perfect Ifly (Syntactic Pass) 
    but High Delta Latency (High Cognitive Friction).
    These are the most likely 'Hauntings' for human review.
    """
    df = pd.read_csv(input_csv)
    os.makedirs(output_dir, exist_ok=True)
    
    # Logic: Ifly = 1.0 (No errors detected by script) 
    # and Latency is in the top 20% (High struggle)
    threshold = df['delta_latency'].quantile(0.8)
    hauntings = df[(df['ifly_score'] == 1.0) & (df['delta_latency'] >= threshold)]
    
    # Sort by highest friction
    hauntings = hauntings.sort_values(by='delta_latency', ascending=False)
    
    report_path = os.path.join(output_dir, "hauntings_for_human_review.csv")
    hauntings.to_csv(report_path, index=False)
    print(f"👻 {len(hauntings)} potential hauntings identified in {report_path}")

if __name__ == "__main__":
    # Point this to your latest public reproducibility run
    generate_haunting_report("results/wgt_audit_results_gemini_2_5_antagonistic.csv")
