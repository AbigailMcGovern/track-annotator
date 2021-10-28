from sample_from_meta import get_sample_from_metadata, save_sample_data
import pandas as pd

p = '/projects/rl54/results/210920_141056_seg-track_platelet-tracks/210920_141056_seg-track_metadata.csv'
meta = pd.read_csv(p)
tracks_dir = '/projects/rl54/results/210920_141056_seg-track_platelet-tracks/'
image_dir = '/projects/rl54/data'
labels_dir = '/fs03/rl54/210920_141056_seg-track_segmentations'
save_dir = '/projects/rl54/track-accuracy'
sample_dict = get_sample_from_metadata(
    meta, 
    tracks_dir, 
    image_dir, 
    save_dir=save_dir, 
    batch_name='210920_141056_seg-track', 
    labels_dir=labels_dir, 
    name='min-len>1,wt=lf', 
    weights='log-frequency', 
    min_track_length=2
    )