#!/bin/bash
#SBATCH --job-name=TrackSampleRandom
#SBATCH --account=rl54
#SBATCH --time=05:00:00
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=Abigail.McGovern1@monash.edu
#SBATCH --mail-type=ALL

source /projects/rl54/Abi/miniconda/bin/activate
conda activate dl-env
python /projects/rl54/Abi/track-annotator/massive_sample_rdm.py