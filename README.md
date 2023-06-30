# TSDM
A RGB-D tracker base on CNN with using depth information.  
Download paper https://arxiv.org/abs/2005.04063  
The code is simple here.

### Required Libs
* Conda with Python 3.7.
* Nvidia GPU.
* PyTorch 1.0
* OpenCV

### Our models
* Res20.pth: retrained SiamRPN++ model (works with M-g)
* modelRes: not retrained SiamRPN++ model
* High-Low-two.pth: D-r model  
Pease put the three models into data_and_result/weight. Link as follow:  
BAIDU YUN:    https://pan.baidu.com/s/1Z2c9SymPIRTA_-4p5W1hHA     pin: faon  
Google Drive: https://drive.google.com/drive/folders/17EN9IU-GOhFQt7middHVaNQFwWj7U8MP?usp=sharing  

### Evaluation datasets
* VOT-RGBD2019: www.votchallenge.net/
* PTB dataset:  http://tracking.cs.princeton.edu/dataset.html  
Note that a subset of the offical EvaluationSet is the real evaluation dataset, which needs be extracted by offical matlab shell. Here, I offer the subset as follow, you could just test the subset directly and submit your result. ptb_evaluate_demo.py can assisit you to make your result in the correct form.
https://pan.baidu.com/s/1Ggak_KOlEDV6agOEnXPCIQ      pin:x5rf
  
* demo dataset: https://drive.google.com/drive/folders/19O6o8H_CblZehAJpNQ_KIFe2XGVMs_eY?usp=sharing  
Please put three datasets above into "data_and_result/test_data/". If you only run demo, you can only download demo dataset and put it into "data_and_result/test_data/"


### Test demo
If you wang to run the demo, please run "python3 test.py --sequence n". Here, n ranges {1,2,3}.

### Acknowlege
Thanks to SiamRPN++, it is the core of our model. Paper in https://arxiv.org/pdf/1812.11703.pdf


### Others
I am Pengyao Zhao, one of authors of this work.
