# 📦 其他研究 | 2026年11月24日

> 本类共 **206** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-206**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-206**

---

### 201. [Ranking-Preserving Coreset Selection for Efficient Evolutionary Hyperparameter Optimization](https://arxiv.org/abs/2611.27959)

**<font color=#1a73e8>作者：</font>** Mamoona Tasadduq, Maryam Bashir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter optimization (HPO) is essential for high predictive performance, but its computational cost becomes prohibitive when candidate configurations require repeated training on large datasets. This paper proposes a ranking-preserving coreset (RPC) selection framework for accelerating evolutionary HPO. The method constructs a compact coreset that preserves the relative ranking of hyperparameter configurations observed on the full training data. Coreset selection is formulated as an evolutionary optimization problem that maximizes Spearman rank correlation between full-data and subset-based configuration rankings while penalizing subset size. The selected coreset is then used for HPO with three evolutionary algorithms: Genetic Algorithm (GA), Cross-generational elitist Selection, Heterogeneous Recombination and Cataclysmic Mutation (CHC), and Particle Swarm Optimization (PSO). Experiments on seven tabular, two text, and two image benchmark datasets show that RPC substantially reduces HPO time while maintaining test accuracy comparable to full-dataset HPO across decision tree, text classification, and image classification tasks. Across datasets and optimizers, HPO-stage speedups range from approximately 1.14x to 8.80x, while the one-time coreset construction cost is accounted for separately through end-to-end runtime and break-even analysis. On 20 held-out configurations excluded from coreset construction, RPC achieves higher ranking correlation than same-size random sampling on 8 of 11 datasets (dataset-level Wilcoxon signed-rank test, p = 0.014). These results show that ranking preservation extends beyond the configurations used during selection. The one-time construction cost can be amortized when the coreset is reused across HPO runs.

---


### 202. [Model Carving: Training Transformers That Optimize Their Own Topology](https://arxiv.org/abs/2611.27962)

**<font color=#1a73e8>作者：</font>** Kaden Zheng, Pratyusha Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has largely kept separate the choice of architecture and the process of training. A classic Transformer, for instance, trains a fixed set of attention and MLP sublayers at every layer, in the same order, and optimizes the weights within. This uniformity is a convention rather than a principled design choice, and it is likely suboptimal: the best architecture for a given task may be smaller, more efficient, and far from uniform. We believe that, ideally, training itself should shape the model's topology. To this end, we introduce Model Carving, which learns both a Transformer's weights and its architecture in a single run. By applying learnable, scalar gates to each sublayer, we allow the training loss to remove the model's own components during training -- freeing a smaller heterogeneous network inside. We evaluate Model Carving by pre-training standard Transformers from 140M to 2.7B parameters and looped Transformers from 140M to 1.3B. At equal training compute, carved models reach a lower validation loss than dense models trained with up to 1.7 times more compute. Furthermore, carved models also outperform size-matched models produced by pruning or distillation, suggesting that the best way to obtain small models for edge devices is to carve them during training, not to compress a large one afterwards. This advantage both grows with scale and carries over to downstream tasks such as few-shot evaluation and generation. Because the removed sublayers no longer run, carved models also cost up to 34% fewer FLOPs per token and decode up to 1.6 times faster without cost in quality. Our results show that architecture, like weights, should be learned and not fixed in advance, and that inside every large transformer is a smaller, faster, stronger one waiting to be carved out.

---


### 203. [Non-penetrating World Models](https://arxiv.org/abs/2611.27963)

**<font color=#1a73e8>作者：</font>** Yuhang Dai, Yinwei Wu, Ziyue Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict such violations. We find that the hidden states of diffusion transformers (DiTs) can predict whether a candidate action will penetrate an obstacle. Building on this, we introduce NoPeWorld, a lightweight framework that detects and prevents penetration. Specifically, we train a small prediction head on top of a frozen DiT's hidden states to read out if a candidate action is safe or not. Unsafe actions are then replaced with safe ones that best preserve the original intent. Despite its simplicity, NoPeWorld substantially reduces the physical violation rate, averaged over six video world models, from 74% to 16%. Remarkably, our method shows zero-shot generalization to open-domain imagery, third-person viewpoints, and moving obstacles. We publicly release our code, the NoPeBench benchmark, and model weights. Project Page: this https URL .

---


### 204. [Your Camera Can Hear You: Side-Channel Acoustic Eavesdropping via Android Camera2 Metadata](https://arxiv.org/abs/2611.27964)

**<font color=#1a73e8>作者：</font>** Guangyuan Ji, Wenjing Wang, Bingsheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To prevent motion sensors from acting as covert microphones, Android 12+ caps SensorManager gyroscope and accelerometer rates at 200 Hz by default, requires HIGH_SAMPLING_RATE_SENSORS for higher rates, and throttles sensors back to 200 Hz when the microphone toggle is off. We show that Android's Camera2 subsystem bypasses these defenses. During an active Camera2 session, Camera HAL stabilization pipelines record high-rate gyroscope measurements and export them via vendor CaptureResult metadata. Loudspeaker speech excites chassis vibrations that couple into this path. Across 50 smartphones (2020-2026) from 10 vendors, 37 expose gyroscope metadata via Camera2, and 26 exceed 200 Hz--including six flagship models at 800-1000 Hz, double SensorManager's 400-500 Hz ceiling. This channel requires neither RECORD_AUDIO nor HIGH_SAMPLING_RATE_SENSORS and defeats privacy switches: turning off the microphone toggle does not throttle metadata, and turning off the camera toggle blanks only video frames while 800-1000 Hz metadata keeps streaming.
To build a zero-profiling attack that generalizes to unseen phones, we introduce Source-to-Leakage Learning (S2L). Prior attacks train on real sensor traces, entangling speech with a specific phone's mechanical resonances and sampling rate. S2L decouples speech content from hardware acoustics using a physics-constrained forward simulator. Trained exclusively on simulated leakage without target-phone traces, our universal recognizer CamEar achieves 52.1% mean word accuracy (up to 61.8%) and 74.3% character accuracy (up to 80.7%) across the six 800-1000 Hz phones. In contrast, ISpyU models fine-tuned on real target-phone data drop to 25.9% word accuracy on unseen phones; CamEar improves cross-device accuracy by 101.4% and outperforms ISpyU's same-device models on every tested phone.

---


### 205. [On the Complete Feature Set for ADHD Classification in Children and Adolescents Based on EEG Signals](https://arxiv.org/abs/2611.27970)

**<font color=#1a73e8>作者：</font>** Javier Sanchis, Álvaro Navarro, Jorge García-Carrasco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention-deficit/hyperactivity disorder is a neurodevelopmental condition that can affect attention, activity and impulse control. Electroencephalography (EEG) records brain activity as children and adolescents perform cognitive tasks. However, comparing features derived from these recordings requires consistent signal preparation, shared analysis windows and documented quality decisions. We curated 669 existing BALLADEER recordings from 156 participants across five task conditions so that researchers can compare seven EEG feature families on the same time intervals for each participant and task. The dataset links continuous signals to precomputed measurements from 115 feature definitions or templates and records the quality decisions made for each recording. Analyses must still account for repeated measurements within participants, residual artefacts and differences between acquisition systems. Technical validation covered signal integrity, numerical checks on feature estimators and completeness of the released files. In every task, the median proportion of recording time retained after preprocessing was 100%. To illustrate reuse, we report saved participant-held-out evaluations comparing XGBoost using all seven families on eight-second windows with a predictor based only on recruitment-group prevalence in the training fold. Recruitment-group discrimination was stronger in Robots than in the three Slackline conditions. These descriptive results from overlapping cohorts do not establish diagnostic validity. The dataset, curation software and aggregate results for the predictive example are publicly available.

---


### 206. [A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning](https://arxiv.org/abs/2611.27978)

**<font color=#1a73e8>作者：</font>** Hari Sitaula, Joseph Opitz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features. We benchmark three model families, namely linear regression, vanilla recurrent neural networks (RNN), and long short-term memory networks (LSTM), within a unified preprocessing and chronological evaluation pipeline. A central contribution of this work is a methodological audit of common practices in the deep-learning-for-stock-prediction literature. We identify three sources of result inflation that frequently appear in published methodologies: wavelet-denoised evaluation targets, the absence of a naive persistence baseline, and best-of-N replicate reporting. We then re-evaluate all model families under a corrected protocol that controls for each. Performance is reported using root mean squared error, mean absolute percentage error, and the Pearson correlation coefficient, averaged across N = 30 independent replicates per configuration. We compare models on accuracy, stability across replicates, and architectural depth sensitivity, using the naive persistence forecast (predicting today's close as tomorrow's close) as a primary baseline against which all candidate models must demonstrate improvement.

---


> [!TIP]
> 当前位于：**201-206**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-206**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
