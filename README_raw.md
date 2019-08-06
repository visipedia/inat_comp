![Banner](https://rawgit.com/visipedia/inat_comp/master/assets/banner2019.gif)

# iNaturalist 2019 Competition
The 2019 competition is part of the [FGVC^6 workshop](https://sites.google.com/view/fgvc6/home) at [CVPR](http://cvpr2019.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Updates
August 6th, 2019: 
  * Un-obfuscated names are released. Simply replace the `categories` list in the dataset files with the list found in this [file](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/categories.json.tar.gz).

  * Thanks to everyone who attended and participated in the [FGVC5 workshop](https://sites.google.com/view/fgvc6/home)! Slides from the competition overview can be found [here](https://drive.google.com/file/d/1Ah5haDF6kFioQzy45-HKTsxZCqGwondf/view).

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here](https://www.kaggle.com/c/inaturalist-2019-fgvc6).

## Dates
|||
|------|---------------|
Data Released|March, 2019|
Submission Server Open |March, 2019|
Submission Deadline|June, 2019|
Winners Announced|June, 2019|

## Details
There are a total of 1,010 species in the dataset, spanning 72 genera, with a combined training and validation set of 268,243 images. The dataset was constructed such that each genera contains at least 10 species, making the dataset inherently fine-grained. 

![Train Val Distribution](https://rawgit.com/visipedia/inat_comp/master/assets/train_val_distribution.png)


## Evaluation
This competition employs average top-1 error. For each image $i$, an algorithm will produce 1 label $l_i$. Each image has one ground truth label $g_i$, and the error for that image is:
$$
e_i = d(l_i, g_i)
$$
Where
$$
d(x, y) =
\begin{cases}
    0       & \quad \text{if } x = y \\
    1  & \quad \text{otherwise}\\
\end{cases}
$$

The overall error score for an algorithm is the average error over all $N$ test images:
$$
\text{score} = \frac{1}{N} \sum_{i} e_{i}
$$

## Differences from iNaturalist 2018 Competition
The primary difference between the 2019 competition and the [2018 Competition](2018/README.md) is the way species were selected for the dataset. For the 2019 dataset, we filtered out all species that had insufficient observations. From this reduced set, we filtered out all species that were not members of genera with at least 10 species remaining. This produced a dataset of 72 genera, each with at least 10 species, for a total of 1010 species. Our aim was to produce a collection of fine-grained problems that are representative of the natural world. We made the evalue metric more strict in 2019, going to top-1 error as opposed to top-3. 





## Guidelines

Participants are welcome to use the [iNaturalist 2018](2018/README.md) and [iNaturalist 2017](2017/README.md) competition datasets as an additional data source. There is an overlap between the 2017 + 2018 species and the 2019 species, however we do not provide a mapping. Besides using the 2017 and 2018 datasetd, participants are restricted from collecting additional natural world data for the 2019 competition. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models, or iNaturalist 2017 pretrained models). Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images (with the exception of the allowed pretrained models) to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

Participants are allowed to collect additional annotations (e.g. bounding boxes, keypoints) on the provided training and validation sets. Teams should specify that they collected additional annotations when submitting results.

## Annotation Format
We follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download) and add additional fields. The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
```
{
  "info" : info,
  "images" : [image],
  "categories" : [category],
  "annotations" : [annotation],
  "licenses" : [license]
}

info{
  "year" : int,
  "version" : str,
  "description" : str,
  "contributor" : str,
  "url" : str,
  "date_created" : datetime,
}

image{
  "id" : int,
  "width" : int,
  "height" : int,
  "file_name" : str,
  "license" : int,
  "rights_holder" : str
}

category{
  "id" : int,
  "name" : str,
  "kingdom" : str,
  "phylum" : str,
  "class" : str,
  "order" : str,
  "family" : str,
  "genus" : str
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

## Submission Format

The submission format for the Kaggle competition is a csv file with the following format:
```
id,predicted
12345,0
67890,83
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to the predicted category ids. You should have one row for each test image.

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Download the dataset files here:
  * All training and validation images [120GB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/train_val2018.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/train_val2018.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/train_val2018.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/train_val2018.tar.gz). Warning this will be slow.
      * Running `md5sum train_val2018.tar.gz` should produce `b1c6952ce38f31868cc50ea72d066cc3`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val2018/super category/category/image.jpg`. This may take a while.
  * Training annotations [26MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/train2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/train2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/train2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/train2018.json.tar.gz)
      * Running `md5sum train2018.json.tar.gz` should produce `bfa29d89d629cbf04d826a720c0a68b0`
  * Validation annotations [26MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/val2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/val2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/val2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/val2018.json.tar.gz)
      * Running `md5sum val2018.json.tar.gz` should produce `f2ed8bfe3e9901cdefceb4e53cd3775d`
  * Test images [40GB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/test2018.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/test2018.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/test2018.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/test2018.tar.gz). Warning this will be slow.
      * Running `md5sum test2018.tar.gz` should produce `4b71d44d73e27475eefea68886c7d1b1`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `test2018/image.jpg`.
  * Test image info [6.3MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/test2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/test2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/test2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/test2018.json.tar.gz)
      * Running `md5sum test2018.json.tar.gz` should produce `fc717a7f53ac72ed8b250221a08a4502`

## Pretrained Models

A pretrained InceptionV3 model in PyTorch is available [here](https://github.com/macaodha/inat_comp_2018).

## Previous Competitions

* [2017 Competition](2017/README.md)
