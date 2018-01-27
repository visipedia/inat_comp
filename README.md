![Banner](https://rawgit.com/visipedia/inat_comp/master/assets/banner2018.jpg)

# iNaturalist Competition
Please open an issue if you have questions or problems with the dataset.

# 2018 Competition
The 2018 competition is part of the [FGVC^5 workshop](http://fgvc.org) at [CVPR](http://cvpr2018.thecvf.com/).

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here]().

## Dates
|||
|------|---------------|
Data Released|February, 2018|
Submission Server Open |February, 2018|
Submission Deadline|June, 2018|
Winners Announced|June, 2018|

## Details

There are a total of 8,142 species in the dataset, with 462,624 training and 76,381 validation images. The species are split into "head" and "tail" groups, with 2,189 species falling into the head group and 5,953 species in the tail group. Each species in the head group has at least 29 and at most 3,582 training images. Each species in the tail group has at least 2 and at most 28 training images.

| Super Category |	Category Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
Plantae|2,917|118,800|26,868|
Insecta|2,031|91,145|16,082|
Aves|1,258|161,736|17,729|
Actinopterygii|369|7,835|1,347|
Fungi|321|6,864|1,422|
Reptilia|284|24,724|4,530|
Mollusca|262|8,007|1,501|
Mammalia|234|21,506|2,794|
Animalia|178|5,966|1,196|
Amphibia|144|11,156|1,783|
Arachnida|114|4,037|887|
Chromista|25|621|174|
Protozoa|4|211|65|
Bacteria|1|16|3|
|||||
Total|8,142|462,624|76,381|

![Train Distribution](https://rawgit.com/visipedia/inat_comp/master/assets/train_distribution2018.png)

![Val Distribution](https://rawgit.com/visipedia/inat_comp/master/assets/val_distribution2018.png)

## Evaluation
Participants will only be evaluated on *tail species*. We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.642109pt height=21.60213pt/>, an algorithm will produce 5 labels <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/655bedbaf4a65f397b5041d0fdecde4c.svg?invert_in_darkmode" align=middle width=15.601905pt height=22.74591pt/>, <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/6d0aa77223bd2246e5cdd2a422d9e584.svg?invert_in_darkmode" align=middle width=82.4274pt height=21.60213pt/>. We allow 5 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/681a37b53b66acbc455e39ca3e6f1c41.svg?invert_in_darkmode" align=middle width=12.444795pt height=14.10255pt/>, and the error for that image is:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/7a42826f81c53c77e0fef3c827238d25.svg?invert_in_darkmode" align=middle width=123.403665pt height=24.865665pt/></p>
Where
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/7a45c501d5042bd031a267f008fa2ae6.svg?invert_in_darkmode" align=middle width=190.2021pt height=49.13139pt/></p>

The overall error score for an algorithm is the average error over all <img src="https://rawgit.com/visipedia/inat_comp/None/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.94405pt height=22.38192pt/> test images:
<p align="center"><img src="https://rawgit.com/visipedia/inat_comp/None/svgs/444adcac0c7cbb4a8419ee1484625349.svg?invert_in_darkmode" align=middle width=118.05123pt height=41.069655pt/></p>

## Differences from iNaturalist 2017 Competition
The 2018 competition differs from the [2017 Competition](README_2017.md) in several ways:

### Species Only
The 2017 dataset categories represented several taxonomic ranks. The 2018 categories are all species.

### Evaluation on Tail Species Only
For the 2017 competition, participants were evaluated on all 5k categories. For the 2018 competition we are only evaluating participants on species from the *tail*. Participants are encouraged to use the species from the head in novel ways to increase classification performance on species from the tail.

### Taxonomy Information & Obfuscation
The 2018 dataset contains kingdom, phylum, class, order, family, and genus taxonomic information for all species. However, we have obfuscated all taxonomic names to hinder participants from constructing web search terms to collect additional data.

## Guidelines

Participants are welcome to use the [iNaturalist 2017 Competition dataset](README_2017.md) as an additional data source. There is an overlap bewteen the 2017 categories and the 2018 *head species*, however we do not provide a mapping from the 2017 categories to the 2018 categories. Besides the 2017 dataset, participants are restricted from collecting additional natural world data for the 2018 competition. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models, or iNaturalist 2017 pretrained models). Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

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
  "rights_holder" : str,
  "tag" : "tail" or "head"
}

category{
  "id" : int,
  "name" : str,
  "supercategory" : str,
  "kingdom" : str,
  "phylum" : str,
  "class" : str,
  "order" : str,
  "family" : str,
  "genus" : str,
  "tag" : "tail" or "head"
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int,
  "tag" : "tail" or "head"
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

## Annotation Notes

We have added a field called `tag` to the `image`, `category` and `annotation` objects. This field will have the value `"tail"` or `"head"` and acts a convenient way to split the dataset into the head and tail groups.

Since participants will only be evaluated on species from the tail, we have ordered the categories such that the tail species are first. Therefore tail species have category ids in the range [0, 5952]. This means that a submission file created by a model trained *only* on the tail species will be valid for upload to Kaggle.

## Submission Format

The submission format for the Kaggle competition is a csv file with the following format:
```
id,predicted
12345,0 78 23 3 42
67890,83 13 42 0 21
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to 5 category ids, separated by spaces. You should have one row for each test image.

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Download the dataset files here:
  * [All training and validation images [186GB]]()
      * Alternate links for different parts of the world:
          * [North America [186GB]]()
          * [Asia [186GB]]()
          * [Europe [186GB]]()
      * Running `md5sum` on the tar.gz file should produce `blah`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val2018/super category/category/image.jpg`. This may take a while.
      * Image Subsets
          * [Head training and validation images]()
              * [North America [186GB]]()
              * [Asia [186GB]]()
              * [Europe [186GB]]()
              * Running `md5sum` on the tar.gz file should produce `blah`
          * [Tail training and validation images]()
              * [North America [186GB]]()
              * [Asia [186GB]]()
              * [Europe [186GB]]()
              * Running `md5sum` on the tar.gz file should produce `blah`
  * [Training and validation annotations [26MB]]()
      * Alternate links for different parts of the world:
          * [North America [26MB]]()
          * [Asia [26MB]]()
          * [Europe [26MB]]()
  * [Test images [53GB]]()
      * Alternative links for different parts of the world:
          * [North America [53GB]]()
          * [Asia [53GB]]()
          * [Europe [53GB]]()
      * Running `md5sum` on the tar.gz file should produce `blah`
      * Images have a max dimension of 800px and have been converted to JPEG format
  * [Test image info [6.3MB]]()
      * Alternative links for different parts of the world:
          * [North America [6.3MB]]()
          * [Asia [6.3MB]]()
          * [Europe [6.3MB]]()
