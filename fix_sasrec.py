import os
import fileinput
import sys

def fix_sasrec_model():
    """Fix the SASRec model by changing how arguments are passed to the encoder."""
    
    # Get the path to the installed model.py file
    try:
        import recommenders
        model_path = os.path.join(os.path.dirname(recommenders.__file__), 
                                 "models", "sasrec", "model.py")
    except ImportError:
        print("Recommenders package not found.")
        return
        
    if not os.path.exists(model_path):
        print(f"SASRec model file not found at {model_path}")
        return
        
    # Make the fix
    fixed = False
    for line in fileinput.input(model_path, inplace=True):
        if "seq_attention = self.encoder(seq_attention, training, mask)" in line:
            fixed = True
            print(line.replace("seq_attention = self.encoder(seq_attention, training, mask)", 
                              "seq_attention = self.encoder(seq_attention, training=training, mask=mask)"), 
                  end="")
        else:
            print(line, end="")
            
    if fixed:
        print(f"Fixed SASRec model at {model_path}")
    else:
        print(f"No fixes needed or line not found in {model_path}")

if __name__ == "__main__":
    fix_sasrec_model()
