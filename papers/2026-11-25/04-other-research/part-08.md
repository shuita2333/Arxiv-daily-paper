# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 351. [When Should We Trust Medical Image Models? Evaluating Confidence Reliability under Cross-Dataset Shift](https://arxiv.org/abs/2611.29955)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Sarah Lam, Yuting Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for chest X-ray analysis often achieve strong performance on benchmark datasets, but their reliability under cross-dataset deployment remains unclear. In clinical practice, models trained in one hospital system may be applied to data from another, where distributional and labeling differences can affect both prediction accuracy and model confidence.
We conduct a controlled empirical study of model confidence under cross-dataset transfer. We train ResNet-50 and DenseNet-121 on CheXpert and evaluate them on MIMIC-CXR across five experimental settings, focusing on Pneumothorax and Pleural Effusion. We measure predictive performance using AUC and confidence reliability using Expected Calibration Error (ECE), Brier score, and average confidence on incorrect predictions, all reported with 95% bootstrap confidence intervals. We further evaluate post-hoc temperature scaling fit on the source validation set and use Grad-CAM to examine the mechanism behind cross-domain performance differences.
Cross-domain AUC drops 7-13 percentage points, and the best in-domain model is not the best cross-domain model. Source-domain temperature scaling produces marginal ECE changes but systematically increases confidence on incorrect predictions across all four model-pathology combinations. Grad-CAM reveals that DenseNet relies on a concentrated spatial prior that fails to transfer, while ResNet's more distributed attention generalizes better. These findings argue for cross-site validation and safety-specific calibration metrics in medical AI evaluation.

---


### 352. [Packing Stern into L2: GPU-Accelerated Primal-Shortened ISD for High-Codimension Binary Goppa Key Recovery](https://arxiv.org/abs/2611.29958)

**<font color=#1a73e8>作者：</font>** Raullen Chai, Xinxin Fan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Primal-Shortened Information-Set Decoding (ISD) with quadratic polar lifting recently pushed TII McEliece Track-2 key recovery to $mt=126$ (TII-228, $2{,}463$ CPU core-hours), with over $99\%$ of runtime spent harvesting weight-$(2t+1)$ codewords. Porting MiniMax's Mode-6 Stern sampler directly to one block per SM leaves $1.0\text{-}1.5\text{ GB}$ of hash tables active and stalls on global memory. For $mt \le 145$, we pack all $mt-17 \le 128$ remaining syndrome bits into one $16$-byte ulonglong2 without left-triple indices, share $G \in \{4, 8\}$ cooperative tables inside GPU L2 cache, batch $64G$ random systematic reductions per launch, and widen the shortening prefix $n'$ to cut modeled GPU-hours by $34\%\text{-}47\%$.
Across four Track-2 challenges ($mt = 108 \to 144$), every recovered private key passes both the official SageMath checker and a standalone pure-Python verifier. Eight Modal L40S GPUs solve TII-228 ($mt=126$) in $18.9\text{ min}$ ($2.15$ GPU-hours, $3.0\times$ faster in wall-clock than MiniMax's EPYC cluster). We further recover keys for the previously undocumented challenges TII-237 ($mt=135$, $22.1$ L4 GPU-hours) and TII-235 ($mt=144$, $4.30\text{ h}$ across ten L40S GPUs, $39.62$ GPU-hours, $17.97\text{ s}$ lift), using $127$ of $128$ packed bits. These results do not demonstrate practical recovery against Classic McEliece parameters ($mt \ge 768$).

---


### 353. [IDSMorph: Self-Adaptive Malicious Traffic Detection through Consistency-Guided Dynamic Decision Boundaries](https://arxiv.org/abs/2611.29964)

**<font color=#1a73e8>作者：</font>** Hao Fu, Degang Sun, Jinxia Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anomaly-based malicious traffic detection learns decision boundaries for normal behavior and identifies deviations as anomalies. However, normal behavior varies across networks and changes dynamically, limiting adaptability and increasing retraining costs. Despite this variability, our measurements show that clients accessing the same service exhibit consistent flow structures and interaction patterns, since each service provides specific functionality. We therefore construct service-specific decision boundaries. However, variations in personalized requests make it difficult to construct stable boundaries.
To address this challenge, we propose IDSMorph, a self-adaptive malicious traffic detection system that learns consistency-guided embeddings through two key designs: (1) a flow structure consistency builder, which constructs contrastive samples capturing consistent embeddings within services; and (2) a service interaction consistency builder, which captures local structural consistency among different clients and global behavioral consistency among clients accessing that service. IDSMorph constructs dynamic decision boundaries from the majority of similar embeddings within each service and dynamically updates them through a differencing algorithm that mitigates the transient traffic shifts within short observation windows. Experiments show that IDSMorph's detection F1 score decreases by no more than 0.12 points across network environments, compared with an average decrease of 55.43 points for prior methods. In real-world deployment with red-team operators independently choosing attack strategies and timing, IDSMorph achieves an F1 score 46.81 points higher than other methods.

---


### 354. [When Learned IDS Model Selection Collapses to a Static Choice: A Measurement Study at the Edge](https://arxiv.org/abs/2611.29968)

**<font color=#1a73e8>作者：</font>** Nuonan Ouyang, Bonan Zhang, Adrian Shatte 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime model selection trades detection quality against energy and latency. However, comparing a selector only with a more costly static detector conflates detector choice with the benefit of adaptation. We present a framework for analysis and physical measurement that combines a pairwise reward criterion, matched static controls, paired blocks, a fixed load-prevalence factorial design, and reporting of actions outside training support. On one Raspberry Pi 4B with four frozen TON-IoT detectors, tabular Q-learning and a deep Q-network (DQN) both select LightLR throughout. A retrospective audit using validation data only rules out preference reversals for MedRF versus LightLR and HeavyMLP versus LightLR. However, TinyDT has a higher reward than LightLR in seven of the 2,500 windows, so the audit does not establish global LightLR optimality. We also evaluate a causal DeadlineGuard rule under a fixed factorial design with three arrival rates (50, 100, and 4,000 rows/s) and three attack prevalences (0.10, 0.50, and 0.90). Compared with Static-MedRF, DeadlineGuard saves 43.7 J per 500-s run (2.98%; 95% paired CI 41.4--46.0 J) and eliminates all 512 deadline misses among 5,000 windows, at a cost of 1.373 percentage points in F1. Outside training support, Tabular-Q's deterministic tie-breaking rule selects TinyDT, resulting in a false-positive rate of 67.76%. These single-board results motivate joint audits of reward attainability, realized actions, attribution against matched static controls, service feasibility, and default actions outside training support.

---


### 355. [FASCIA: Seeing Beneath the Surface with Queryable, Personalized Anatomy in Any Pose](https://arxiv.org/abs/2611.29970)

**<font color=#1a73e8>作者：</font>** R. James Cotton, Tim Unger, Lucinda Williamson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FASCIA (*Functional Anatomical Structures and Composition via Implicit Atlas*), a Momentum Human Rig (MHR)-anchored framework that predicts and poses a person's internal anatomy from their external body shape and skeletal proportions. FASCIA maps a single 290-structure population template onto each individual through a smooth, invertible warp. As people with the same shape can differ internally, a body-dependent Gaussian prior predicts both average warp coordinates and their inter-subject variability. The warp deforms a learned base template into bones, muscles, organs, and fat depots. Extending MHR skinning into the interior enables direct supervision of this model across four automatically labeled CT cohorts and one whole-body MRI cohort. On 82 held-out CT scans, FASCIA reaches a mean volumetric Dice (volume agreement) of 0.48 on named bones and 0.63 on muscles, keeps the majority of bones and muscles in one piece, and yields calibrated voxel probabilities. On 33 held-out whole-body MRI subjects, FASCIA's pointwise field improves tissue overlap over HIT across all compartments, predicts between-person differences in whole-body adipose percentage ($R^2 = 0.88$ vs. $0.38$ in women and $0.54$ vs. $-0.01$ in men), and recovers segment centers of mass within 1.1 mm. Because it needs only an MHR fit, FASCIA can be driven from images, video, or any system that outputs MHR. This opens the door to fitting individualized calibrated musculoskeletal digital twins to video motion data.

---


### 356. [Verifying Declared AI Workloads from GPU Supply Current](https://arxiv.org/abs/2611.29982)

**<font color=#1a73e8>作者：</font>** Tom Kimpson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier AI governance agreements require compute verification techniques that allow an external observer to confirm that a hardware operator does not run prohibited workloads. Off-chip, analogue hardware signals, such as power draw, have been proposed as a potential information channel for compute verification. Such signals can be measured externally, without the operator's cooperation. We show that the supply current drawn by a GPU can be used to verify the work declared by the GPU operator, without requiring examples of prohibited workloads or evasion strategies. We record 23.4 h of GPU current with a Rogowski coil under idle, training and inference workloads. We consider five evasion strategies an operator might use to disguise prohibited training. We show that a one-class model fitted to the current draw of permitted, declared work (idle and inference) flags at least 99.9% of windows of prohibited training, including training hidden by the five evasion strategies. As a continuous monitor across successive windows, it detects all 188 episodes of prohibited training hidden by time-sharing with declared inference, with a median delay of 3.0 s, and raises one alarm in 8.8 h of declared work. Incomplete or corrupt recordings of the declared work can undermine verification. An incomplete recording fails loudly; with idle missing, the monitor is in alarm for 99.97% of declared idle. A corrupt recording can fail silently; if the operator runs training during the recording, the monitor can miss hidden training while raising no alarm on declared work. These results suggest that operator declarations together with external analogue sensing might offer a practical route to compute verification.

---


### 357. [Differential Proteomics to XAI Rules: A SHAP-FOL-ILP Modeling for Lung Adenocarcinoma](https://arxiv.org/abs/2611.29989)

**<font color=#1a73e8>作者：</font>** Surajit Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: We developed an interpretable workflow linking paired differential proteomics, sparse logistic regression, SHAP attribution, and first-order logic (FOL) rule learning in lung adenocarcinoma (LUAD).
Methods: We analysed 213 CPTAC-LUAD tissue samples (111 tumour, 102 adjacent-normal) from 111 patients, including 102 matched pairs. Protein effect estimation and testing used the same complete pairs, with Benjamini-Hochberg correction. Sparse logistic regression used five-fold stratified patient-grouped nested cross-validation. Preprocessing and model selection were confined to training data, with feature selection repeated within inner folds. A separate five-fold patient-grouped evaluation tested SHAP-guided inductive logic programming (FOL/ILP) using training-derived evidence and discretisation.
Results: Quality control retained 9,518 proteins. At FDR below 0.05 and an absolute mean paired log-ratio difference of at least 1, 378 were differentially abundant (40 increased, 338 decreased). The sparse classifier yielded ROC-AUC 0.9997, average precision 0.9998, accuracy 0.9906, and balanced accuracy 0.9906. FOL/ILP yielded held-out accuracy 0.9765, balanced accuracy 0.9767, precision 0.9818, recall 0.9730, and F1 0.9774. HSPA12B, PALM2-AKAP2, STARD13, and PPM1F had non-zero coefficients in all five classifier folds. The most frequent Horn clause occurred in two of five folds. All others occurred once.
Conclusions: The workflow connects proteomic classification, attribution, and symbolic rules. Performance reflects tumour-versus-adjacent-normal discrimination within one cohort. Biomarker and clinical claims require independent validation, repeated assessment of rule stability, and further biological annotation.

---


### 358. [One Size Doesn't Fit All: Input Adaptive Class Activation Mapping for Improved Visual Explanations](https://arxiv.org/abs/2611.29993)

**<font color=#1a73e8>作者：</font>** Ayesha Sahar, Tahir Mustafa Madni, Tehseen Zia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite their widespread use in tasks such as image classification, object detection and semantic segmentation, the limited interpretability of Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) can undermine trust and hinder adoption in safety-critical applications. Explainable artificial intelligence (XAI) methods seek to address this by providing human-understandable explanations for model predictions. Class Activation Maps (CAM) constitute one such widely used XAI technique for visualizing discriminative regions. However, existing CAM methods may exhibit limitations in channel weighting, localization, and adaptability across network architectures potentially resulting in noisy or imprecise explanations. To address these issues, we propose ADAPT-CAM, a gradient-based, parameter-adaptive CAM framework. The method combines first-order gradient energy with activation-weighted second-order curvature to derive channel contributions. It further incorporates adaptive local contrast normalization and knee-guided soft channel selection to refine the resulting explanations. Importantly, key parameters are estimated independently for each input, allowing the framework to adapt to variations in feature representations across network architectures. We validate ADAPT-CAM on ImageNet and Oxford 102 Flowers across CNN and ViT architectures. Quantitative results demonstrate competitive or superior performance against established CAM methods across multiple evaluation metrics. In parallel, qualitative comparisons illustrate its ability to highlight discriminative image regions. Further parameter analysis and ablation experiments examine the behaviour and contributions of the individual adaptive components. These findings demonstrate the applicability of ADAPT-CAM across different architectures and datasets.

---


### 359. [MindBridge: A Multilingual and Multimodal Tool for Interactive Cognitive Monitoring](https://arxiv.org/abs/2611.29996)

**<font color=#1a73e8>作者：</font>** Xiaojie Gu, Haoyu Zhang, Qian Niu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present MindBridge, a clinician-informed, multilingual, multimodal cognitive monitoring tool combining participant-controlled interviews with explainable reports. Reports link lexical diversity and pause patterns to speech or text evidence and disclose data quality and missingness. In a formative study of typed interaction with 10 adults (seven aged 18-59; three aged 60 or older), follow-ups prompted elaboration but sometimes introduced assumptions requiring correction. Nine participants ranked interpretation-first reports highest; all identified score-only reports as most likely to encourage fixation and overreaction. On a fixed DementiaBank manifest, the best configuration achieved 70.3% zero-shot accuracy on valid predictions versus a 56.0% majority-class baseline on the full manifest. Some configurations predicted only one category; tests with generated samples revealed different error patterns across input types and languages. MindBridge makes evidence collection, analysis, and interpretation inspectable, linking participant control to the scope and limits of monitoring results.

---


### 360. [Categorical Foundations of AI Agents](https://arxiv.org/abs/2611.29998)

**<font color=#1a73e8>作者：</font>** Yong Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We follow the idea of separating intelligence from execution and give the categorical foundations of AI agents: the transformers, the agents, and the orchestrations and choreographies of AI agents are categorized, and which also include their coalgebras and algebras.

---


### 361. [EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution](https://arxiv.org/abs/2611.30004)

**<font color=#1a73e8>作者：</font>** Zehao Liu, Huashuo Lei, Xi Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface. Prior attacks on embodied systems have used crafted instructions, adversarial visual inputs, and training-time policy modifications; we study environment-only object rearrangements with unchanged models and instructions. We reveal an attack surface in safety-critical spatial relations among existing objects. An adversary who rearranges objects, without modifying instructions or accessing models, can cause hazardous consequences. In this work, we propose EnvTrap, a diagnostic pipeline that constructs paired safe, trap, and null-trap (benign but misleading) embodied scenarios. We demonstrate that environment-only perturbations raise hazardous-action rates to an average of 83.4% across the five evaluated action policies, with similar vulnerability patterns confirmed in world models. On a consequence-prediction task, model accuracy remains near chance, while human evaluators achieve high accuracy. We further propose a consequence-aware defense that reduces trap trigger rates by an average of 76.3 percentage points across action policies in simulation and by 62.9 percentage points pooled across physical backends. Together, these findings link environment-only attacks to a broader deficit in physical reasoning: embodied models recognize task-relevant objects yet fail to anticipate how spatial relations change the consequences of acting on them. EnvTrap makes this gap directly testable and turns hazardous layouts into training scenarios for safer embodied action. Our code and data are available at this https URL.

---


### 362. [FlexGaze: Weakly Supervised Gaze Estimation at Scale](https://arxiv.org/abs/2611.30012)

**<font color=#1a73e8>作者：</font>** Zongjian Li, Mohammad Soleymani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most gaze estimation models are trained on data collected using specialized equipment. The limited diversity of subjects, scenes, and head poses in these datasets hinders generalization to new conditions. We present FlexGaze, a family of 3D gaze estimators pretrained with weak supervision from gaze labels (pseudo-labels) automatically generated from in-the-wild images. We use off-the-shelf models to predict 2D gaze targets and scene depth, then combine these predictions to generate 3D gaze labels for approximately 3.24 million head instances. At inference, FlexGaze predicts gaze from a head crop alone and can handle profile and rear views without requiring face detection or head pose estimation. We use data augmentation during training to improve robustness to variations in crop position and scale. Pretrained using only these generated gaze labels, FlexGaze generalizes to unseen benchmarks. After supervised fine-tuning on public gaze datasets, we evaluate FlexGaze on eight benchmarks under a unified evaluation protocol. Our models match or outperform publicly available gaze estimators with several times as many parameters on most benchmarks. We release our dataset of generated gaze labels, all trained models, and code via this https URL.

---


### 363. [ReplaySAM: Zero-Shot 3D Particle-Pack Segmentation with SAM 2](https://arxiv.org/abs/2611.30016)

**<font color=#1a73e8>作者：</font>** Bogong Wang, Yulai Zhang, Philipp D. Lösel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray computed tomography (XCT) provides non-destructive three-dimensional (3D) images of particle packs, making their internal structure accessible for quantitative analysis. Extracting particle-level measurements from these volumes first requires identifying and separating individual particles, a task that remains challenging in dense, irregular packs. Existing workflows often require manual correction or task-specific training, while promptable models need a strategy for automatically locating individual particles and recovering their instance masks. We present ReplaySAM, which adapts the pretrained Segment Anything Model 2 (SAM2) to three-dimensional particle-pack segmentation without additional training. It generates point prompts from foreground geometry and fuses SAM2 predictions across orthogonal slice sequences to recover particle instances. On XCT volumes of real quartz and iron-ore particle packs, ReplaySAM achieves higher mean instance Dice scores than expert-assisted watershed and nnInteractive under the evaluated protocols. ReplaySAM thus provides a training-free framework for 3D particle-pack instance segmentation, with geometry-based prompting that eliminates manual prompt placement.

---


### 364. [Automated Neural Network Auditing (ANNA) for Energy Market Settlements: A Machine and Reinforcement Learning-Based Approach](https://arxiv.org/abs/2611.30020)

**<font color=#1a73e8>作者：</font>** J. R. Rivadeneyra, I. Lee, F. Nugen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of segmented energy markets into Independent System Operators (ISOs) like CAISO and MISO has increased settlement complexity. Automated transaction processing creates challenges for evaluating accuracy, compliance, and financial integrity. Traditional rule-based manual auditing is inefficient, error-prone, and cannot handle the data volume from automated this http URL research proposes Automated Neural Network Auditing (ANNA), a machine and reinforcement learning framework for settlement auditing via anomaly prioritization. ANNA integrates statistical anomaly detection, K-Nearest Neighbors (KNN), clustering, and Deep Q-Network (DQN) reinforcement learning to flag potentially anomalous transactions from historical market data. The approach is evaluated as an analyst-support tool for prioritizing transactions needing further audit this http URL was tested against traditional statistical methods, clustering-based techniques, and supervised/reinforcement learning models. The study used three years of CAISO settlement data over 63 million source records across 32 charge codes and multiple counterparties. After preprocessing, approximately 2.9 million labeled transactions formed the working dataset, with model-specific subsets used for training and evaluation. Performance was assessed using precision, recall, computational efficiency, and false-negative this http URL outperforms traditional methods by identifying hidden relationships in settlement data, while standard deviation thresholds, K-Means, KNN, and Q-Learning performed poorly across key metrics. The result is a scalable solution integrating machine and reinforcement learning for automated auditing of energy market settlements, contributing computationally efficient anomaly prioritization to settlement-auditing workflows.

---


### 365. [MOVER: Planning Beyond Motion](https://arxiv.org/abs/2611.30022)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Yu Jiang, Tianyi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Residual world models forecast a driving scene through its temporal change, so feature components that stay constant over time vanish from the residual pathway. We ask whether evidence with weak temporal change, such as a waiting pedestrian or a stopped vehicle, can be used more effectively for planning, and introduce MOVER, a complementary event-routing mechanism. A training-time teacher measures how each spatially grounded event query responds when a past frame is removed from shared history and contrasts that sensitivity with the event's pooled temporal residual, prioritizing events that depend on history but receive weak residual evidence. A student predicts the resulting priorities from unperturbed history, so the teacher adds no inference cost. Under fixed total routing mass, one distribution scales a low-rank future bird's-eye-view update and biases trajectory-conditioned event reading. On nuScenes, MOVER reduces ResWorld's UniAD-style average L2 from 0.65 to 0.55 m and its collision rate from 0.23% to 0.12% without direct planner ego status (0.50 m and 0.09% with it), adding 4.1 ms per frame. Matched controls show that the complementary teacher outperforms either signal alone and that the allocation acts mainly during training. Adapted to BridgeDrive-LEAD, MOVER reaches a 96.52 +/- 0.65 driving score over three seeds on the 220-route Bench2Drive closed-loop benchmark, exceeding matched controls in each paired seed by a margin within seed variation.

---


### 366. [QSRadar: Query-Conditioned Sparse Radar-Camera Fusion for Efficient 3D Object Detection](https://arxiv.org/abs/2611.30023)

**<font color=#1a73e8>作者：</font>** Chenhao Yan, Hongyu Liu, Xiang Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable 3D object detection for autonomous trucks requires both the semantic detail provided by cameras and the geometric and motion cues measured by 4D radar. Existing radar-camera detectors commonly construct global radar bird's-eye-view (BEV) representations, whose computational and memory costs grow with the perception range. Sparse query-based detectors offer greater efficiency, but global feature construction can obscure point-level radar geometry and motion information. We present QSRadar, a query-conditioned sparse radar fusion framework for efficient long-range 3D detection. Built on a Sparse4Dv3-style visual-temporal detector, QSRadar retrieves a compact set of raw radar points around each evolving object hypothesis. The selected points are represented in an anchor-aligned coordinate frame, augmented with motion residuals, radar cross section, and sweep timing, and aggregated by a query-conditioned set encoder. Radar neighborhoods are retrieved again after each anchor refinement, coupling evidence selection with object estimation. Under the official MAN TruckScenes validation protocol, QSRadar achieves 38.09 mAP and 52.20 NDS, compared with 37.08 mAP and 50.78 NDS for our reproduced Sparse4D-Radar global Radar-BEV baseline. In matched tests on an RTX 4090 D, QSRadar reduces latency by 45%, peak memory usage by 49%, and GFLOPs by 43%.

---


### 367. [Damped Atomic Wave Integration Neurons (DAWIN): A Universal Primitive for Continuous-Time Spatiotemporal Learning](https://arxiv.org/abs/2611.30025)

**<font color=#1a73e8>作者：</font>** Byunggu Yu, Justin Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations. We introduce the Damped Atomic Wave Integration Neuron (DAWIN), a continuous-time primitive for replacing standard neural layers in MLPs, Transformers, and graph neural networks. DAWIN couples spatial projection with elapsed-time-dependent wave excitation and integrates it into a local complex state through closed-form damped evolution, avoiding numerical differential equation solvers. We show that DAWIN generalizes static sinusoidal and memoryless wave neurons on interval-augmented inputs, derive closed-form gradients, and establish bounded-input bounded-output stability for positive damping and sampling intervals bounded away from zero. An associative Triton prefix-scan implementation, DAWINLinear, uses FP32 accumulation and achieves O(log L) parallel depth for sequence length L. Across 11 parameter-matched tasks covering irregular oscillators, MuJoCo dynamics, pedestrian trajectories, and PhysioNet 2012 clinical sequences, DAWIN outperforms Neural CDE on 9 tasks and ReLU-MLP on 8. It achieves the lowest error on dense clinical dynamics (0.9531 NRMSE, winning across all 10 seeds) and ties for the best mortality prediction (0.9993 AUROC). Shuffling elapsed intervals increases error by 58.2%-77.4% on selected dynamics tasks, versus 0.06% on a time-irrelevant control, supporting reliance on physical timing. On NVIDIA B200 GPUs, parallel wave integration accelerates inference by up to 2,630 times over its serial implementation and reduces peak GPU memory by up to 97.6% relative to Mamba in the tested configurations.

---


### 368. [SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042)

**<font color=#1a73e8>作者：</font>** Jenna Kang, Bingxuan Li, Colin Groth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive world models generate virtual environments autoregressively from player actions and visual history. However, visual history alone cannot reliably capture the evolving states of independently acting non-player characters (NPCs) in real games, particularly when they are outside the camera view. Recent multi-agent world models address this challenge through joint multi-view generation or persistent shared state, but often rely on external observations, like maps or scene geometry, or predefined state transitions. We present SWAM, a State-aware World Action Model that separates agent-state evolution from autoregressive visual generation in interactive 3D environments. A lightweight state model propagates character dynamics from actions without consuming generated frames, combining motion priors with learned scene-dependent corrections. The predicted states then guide an autoregressive diffusion transformer alongside visual history through a novel conditioning scheme. Rather than requiring an explicit scene geometry map or visibility tests, the conditioning indicates where characters may appear, allowing the diffusion model to learn their appearance and occlusion. This design enables NPCs to evolve independently of visual generation while maintaining consistent observations across visibility changes, interactions, and respawns. Evaluations in a custom Godot-based first-person shooter game demonstrate improvements in visual fidelity, NPC consistency, and long-horizon stability over existing approaches.

---


### 369. [PsyDrift: Healthy-Reference Latent Diffusion for Anomaly Scoring in Autism Spectrum Disorder](https://arxiv.org/abs/2611.30050)

**<font color=#1a73e8>作者：</font>** Yasaman Mohammadpour, Pouya Shaeri, Ariane Middel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual heterogeneity and acquisition-site variability complicate neuroimaging-based characterization of autism spectrum disorder (ASD). We propose PsyDrift, combining ASD/healthy-control-supervised functional-connectivity representations with healthy-reference latent diffusion. An encoder produces 128-dimensional representations, and a denoising diffusion probabilistic model (DDPM) learns exclusively from healthy training latents. Distance from a diffusion-denoised reconstruction provides a continuous deviation score. We evaluate 1,102 subjects from all 20 ABIDE-I sites using five-seed leave-one-site-out cross-validation. The classifier and DDPM achieve mean-site AUROCs of $0.798 \pm 0.003$ and $0.718 \pm 0.013$, respectively; uncertainties denote seed standard deviations. Matched healthy-reference scorers on the same representation achieve 0.68-0.71; the statistical significance of diffusion's modest numerical advantage remains unestablished. Within ASD, scores show weak associations with ADOS Total (Spearman $\rho = 0.108$, $p = 0.038$) and full-scale IQ ($\rho = -0.138$, $p = 0.002$), without adjustment for age, sex, site, or head motion. Frozen evaluation without retraining or hyperparameter adaptation yields pooled AUROCs of 0.69 on ABIDE-II and 0.61 on ADHD-200, providing preliminary evidence of cross-cohort and cross-disorder transfer. These results demonstrate healthy-reference deviation scoring within an ASD-supervised representation; incremental predictive and clinical value remains unestablished.

---


### 370. [Bi-Refine: Semantic Verification-Guided Progressive Refinement for Moment Retrieval](https://arxiv.org/abs/2611.30055)

**<font color=#1a73e8>作者：</font>** Mengnan Liu, Sanping Zhou, Kun Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moment Retrieval (MR) aims to identify the temporal segment in an untrimmed video that corresponds to a natural language query. Existing approaches commonly refine temporal predictions within the localization pathway, without explicitly verifying candidate-level semantic consistency. Moreover, directly reusing semantic scores as feedback can cause over-correction when the verification signal is unreliable. To address these issues, we propose Bi-Refine, a semantic verification-guided progressive refinement framework that formulates MR as a closed-loop verification-and-refinement process. A Heuristic Localization Branch first generates candidate moments, while a Semantic Verification Branch evaluates their query consistency in a semantically enriched latent space. Query supervision further trains the verifier with the same candidate moment but different queries, encouraging it to distinguish the matched query from semantically similar mismatched queries. The resulting verification features are incorporated into a Progressive Refinement Loop that updates both query representations and multimodal features. To suppress potentially harmful updates, a lightweight reliability estimator gates query updates and reweights candidate contributions in feature feedback. A convergence-based adaptive stopping strategy additionally terminates unnecessary refinement during inference. Experiments on three standard MR benchmarks demonstrate the effectiveness and state-of-the-art performance of our method.

---


### 371. [FireDesmoke: Fire Smoke Removal via Real Smoke Transfer and Semantic Rectification](https://arxiv.org/abs/2611.30057)

**<font color=#1a73e8>作者：</font>** Chih-Chung Hsu, Rong-Lin Jian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fire smoke removal must restore dense and medium smoke regions while preserving the clear (smoke-free) content. Existing methods either leave the smoke or alter the visible content, and generative models may hallucinate people or remove flames. Real fire smoke is spatially local: the degradation and its corruption of semantic features are both concentrated in the smoke regions. We propose FireDesmoke, built on this locality: Real Smoke Transfer calibrates smoke fields on real-fire recordings and transfers their spatial layout onto clean images to synthesize training pairs, and Semantic Rectification uses pixel features to rectify the tokens of a frozen foundation encoder where smoke corrupts them. With matched training budgets, replacing the transferred pairs with SmokeBench pairs lowers dense-smoke PSNR by 0.74 dB, and removing Semantic Rectification leaves clear regions 1.31 dB below the input. On what is, to the best of our knowledge, the first paired dataset of real fire smoke for image restoration, with 1,500 test frames from a held-out viewpoint, FireDesmoke improves dense- and medium-smoke PSNR by 3.73 and 2.63 dB while keeping clear regions at the input level (+0.41 dB); no other compared method gains at least 1 dB in dense smoke without lowering clear-region PSNR, and no hallucinated person is found in its outputs. It achieves state-of-the-art overall results on this benchmark and, trained on SmokeBench, the highest PSNR with the second-best SSIM and LPIPS.

---


### 372. [EVD-Bench: A Comprehensive Benchmark for EEG-to-Image Decoding](https://arxiv.org/abs/2611.30061)

**<font color=#1a73e8>作者：</font>** Kieren Yu, Qian Zhang, Ziyang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EEG-to-image decoding recovers visual information from non-invasive brain recordings, providing a window into human perception. However, comparisons across systems are confounded by a variable that is rarely reported as such: which participants' data the system was allowed to use. The same Top-1 score on a 200-way gallery may come from a per-participant system, a pooled model over all participants, or a model that never saw the test participant---cases that differ by more than most architectural changes between the methods being compared. We present \bench, a benchmark on THINGS-EEG2 that standardizes the gallery and EEG input, matches training budgets across systems within each regime, and compares three participant-access regimes: within-subject, joint-subject, and strict leave-one-subject-out, with unlabeled target calibration reported separately. All three settings evaluate concept-level zero-shot retrieval: the 200 test concepts are disjoint from the 1,654 concepts used for EEG--image fitting and validation. We compare retrieval across access regimes and use zero-EEG and matched-wrong EEG controls to assess dependence on correct EEG--stimulus pairing. We vary trial averaging, gallery size and difficulty, and training data coverage, and compare target adaptation and visual feature targets. We also assess sensitivity to EEG window length and channel count, robustness to input perturbations, and confidence calibration. These results establish participant-access regime as a necessary reporting dimension alongside gallery, repetition, and visual target.

---


### 373. [LaTSEC: Lattice-Based Threshold Signatures with Native Non-Interactive Identifiable Abort and Compact Per-Party Storage](https://arxiv.org/abs/2611.30063)

**<font color=#1a73e8>作者：</font>** Muhammad Arzaki, Muhammed F. Esgin, Markku-Juhani O. Saarinen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present $\mathsf{LaTSEC}$, a three-round lattice-based threshold signature scheme with native non-interactive identifiable abort. Each party holds one small-norm signing share and is associated with one public abort key, against which its partial signature is verified directly, without zero-knowledge proofs or an additional interactive protocol. Prior lattice-based threshold signatures that identify misbehaving parties rely on one of three mechanisms: zero-knowledge proofs, an additional interactive protocol, or an everywhere-short secret sharing scheme in which each party holds multiple signing shares, each with its own public abort key. Compared with schemes that use the third mechanism, $\mathsf{LaTSEC}$ substantially reduces per-party storage. The construction uses $\mathsf{SEC}$, a recent ramp everywhere-short secret sharing scheme based on lossless expanders that gives each party a single short share. We prove correctness, identifiable-abort security, and threshold unforgeability under the standard $\mathsf{MLWE}$ and $\mathsf{MSIS}$ assumptions. The unforgeability proof introduces the Repeated-$\boldsymbol{A}$ Matrix Hint-MLWE problem, a new variant of $\mathsf{MLWE}$ with hints that captures the complete tuple of correlated public abort keys. We rigorously prove that this new variant admits a reduction from the standard $\mathsf{MLWE}$ problem. For 60 parties at 128-bit security, $\mathsf{LaTSEC}$ tolerates up to 6 corrupted parties, and, empirically, a randomly chosen set of at least 46 parties can sign with probability at least 0.99. Each party holds one signing share of about 14.3 KiB and is associated with one 24-KiB public abort key.

---


### 374. [How Latent Transition Geometry Matters for Planning in World Models](https://arxiv.org/abs/2611.30064)

**<font color=#1a73e8>作者：</font>** Xuanya Zhu, Da Li, Xiatian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models support planning by predicting how the environment evolves under candidate actions. However, one-step predictive accuracy alone does not characterize multi-step planning utility, which depends on distinguishing candidate futures. This raises a natural question: How does latent transition geometry shape planning? We investigate this through an action-conditioned transition-field view, using curvature regularization as a controlled intervention. Across four continuous-control tasks, appropriately tuned regularization improves planning, while excessive regularization can be detrimental. By decomposing the transition field into affine and non-affine components, we find that regularization reduces action sensitivity mainly through the non-affine component. To assess its role in planning, we directly manipulate the non-affine action response in frozen models and show that it affects candidate selection and closed-loop success. Further analysis shows that curvature generally brings predicted futures closer together, while preserving more of the differences along the goal direction. This helps explain why the planning effects vary across tasks. We observe broadly consistent planning trends across five sampling- and gradient-based solvers on LeWM and similar rollout-geometry trends on DINO-WM. Qualitative attention visualizations reveal accompanying shifts toward task-relevant visual structure. Together, these findings clarify how latent transition geometry influences multi-step planning.

---


### 375. [Regularizing Hard Examples Improves Adversarial Robustness](https://arxiv.org/abs/2611.30065)

**<font color=#1a73e8>作者：</font>** Hyungyu Lee, Saehyung Lee, Ho Bae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies have validated that pruning hard-to-learn examples from training improves the generalization performance of neural networks (NNs). In this study, we investigate this intriguing phenomenon -- the negative effect of hard examples on generalization -- in adversarial training. Particularly, we theoretically demonstrate that the increase in the difficulty of hard examples in adversarial training is significantly greater than the increase in the difficulty of easy examples. Furthermore, we verify that hard examples are only fitted through memorization of the label in adversarial training. We conduct both theoretical and empirical analyses of this memorization phenomenon, showing that pruning hard examples in adversarial training can enhance the model's robustness. However, the challenge remains in finding the optimal threshold for removing hard examples that degrade robustness performance. Based upon these observations, we propose a new approach, difficulty proportional label smoothing (DPLS), to adaptively mitigate the negative effect of hard examples, thereby improving the adversarial robustness of NNs. Notably, our experimental result indicates that our method can successfully leverage hard examples while circumventing the negative effect.

---


### 376. [Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability Evaluation for Foundation MLIPs in Materials Discovery](https://arxiv.org/abs/2611.30066)

**<font color=#1a73e8>作者：</font>** Harry Sevi, Joonatan E. M. Laulainen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In AI-guided materials discovery, machine-learning models increasingly decide which candidate materials should receive expensive first-principles or experimental evaluation. Standard reliability metrics such as uncertainty, calibration, novelty, and ranking accuracy evaluate properties of the predictions, but success on these metrics does not necessarily imply a better downstream screening decision. We study this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate three representative reliability interventions (novelty detection, sparse DFT calibration, and chemistry-level ranking audits) using a deployment objective that measures how much DFT can be avoided while maintaining a required recall of near-hull candidates. Across all three, a reliability signal can succeed on its immediate target without improving the final screening decision: novelty detects distribution shift but weakly ranks failure severity; calibration can improve pooled ranking metrics while leaving screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations with poor ranking reliability without yielding a robustly beneficial routing policy. A two-oracle analysis further shows that the source of failure depends on the screening decision itself: under formation-energy screening, even perfect knowledge of average ranking reliability can select the wrong model, whereas in the evaluated hull-aligned variant the oracle target becomes decision-aligned but finite-budget audits still fail to realize the value. Reliability should be evaluated relative to the decision it supports: the relevant question is not whether a model is uncertain or inaccurate, but whether acquiring and acting on additional information will improve the final discovery decision enough to justify its cost.

---


### 377. [FolioWeaver: A LayerGraph-Grounded Agent for Layered Image Generation and Editing](https://arxiv.org/abs/2611.30067)

**<font color=#1a73e8>作者：</font>** Wentao Lu, Shengzhe Cui, Xihao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layered image generation separates images into compositable layers, allowing users to manipulate individual elements independently. However, such asset-level editability does not enable the generation system to interpret successive feedback, perform targeted edits, and preserve unaffected content. We introduce FolioWeaver, a LayerGraph-grounded agent that unifies layered-image generation and iterative editing through a persistent Executable Scene State. FolioWeaver constructs a LayerGraph and generates independent visual assets conditioned on a shared scene reference. An Editing Agent performs feedback-driven modifications and self-repair through scoped actions, selective layer execution, and visual verification, enabling targeted updates while reusing unchanged assets. We also publicly release LayerFolio, a dataset of 100,377 human-reviewed layered scenes spanning six visual domains, together with two evaluation protocols: AtomicQA for measuring requirement satisfaction and CBLP for assessing layer organization. Experiments demonstrate that FolioWeaver achieves superior layer organization and composite fidelity compared with direct layered-generation methods. Analyses validate the contributions of component adaptation, execution-grounded repair, and cross-domain training. FolioWeaver advances layered-image generation toward persistent, controllable, and iterative visual creation. The dataset is available at this https URL.

---


### 378. [Stable but Hidden: Identifiability and Experimental Design under Missing Compositional Support](https://arxiv.org/abs/2611.30070)

**<font color=#1a73e8>作者：</font>** Harry Sevi, Joonatan E. M. Laulainen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-guided scientific discovery often uses inexpensive predictors to allocate scarce verification measurements. We study a structural failure when relevant components have been observed separately but never jointly: distinct admissible response functions can agree on all observed compositions while disagreeing on the missing combinations. Additional same-support data cannot resolve this ambiguity, and agreement among fitted models need not expose it.
We characterize the unresolved directions as an invisible subspace $\mathcal{N}_T(\mathcal{F}) = \ker \mathcal{R}_T$, whose geometry determines oracle zero-shot ambiguity and minimax risk under a symmetric, bounded ambiguity class. When the missing response lies in an $r$-dimensional, well-conditioned linear basis, optimally designed joint measurements achieve minimax integrated risk $\Theta(\sigma^2 r/m)$, with classical $I$-optimality the fixed-design criterion.
We validate on materials. In electrocatalysis, a six-dimensional support-derived structural basis (a prior on candidate directions, not an identified physical model) reduces held-out MSE against a dimension-matched generic basis (median paired ratio 0.75, improving 98% of 60 element pairs at $m = 15$), while $I$-optimal and same-basis posterior-variance acquisition show no detected difference. In Materials Project, removing joint property labels reduces $E_{\text{above hull}}$ ranking on 90% of 30 element pairs, more than matched data-removal controls, under a frozen pretrained representation. Pair difficulty is reproducible across learners but poorly predicted by zero-label ensemble disagreement; 20 joint measurements enable transferable pair-level rankings without reliable absolute calibration.
In practice, experiment selection should ask which relationships the observed support leaves unidentified before asking where a fitted model is least certain.

---


### 379. [SalivaryHSI-Seg: A New Challenging Benchmark for Ex Vivo Salivary Gland Hyperspectral Tissue Segmentation](https://arxiv.org/abs/2611.30071)

**<font color=#1a73e8>作者：</font>** Xiaoqi Guo, Xianran Wang, Xinquan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salivary gland tumors are common lesions in oral and maxillofacial practice, and accurate identification of tumor regions and surrounding salivary gland tissues is important for tissue assessment, pathological sampling, and clinical decision support. Hyperspectral imaging (HSI) records continuous spectral responses together with spatial imaging information, providing a promising way to capture fine-grained tissue-discriminative information. Nevertheless, the development of salivary gland HSI tissue segmentation remains limited due to the lack of standardized benchmarks with pixel-level annotations and unified evaluation protocols. To address this issue, we introduce SalivaryHSI-Seg, a hyperspectral tissue segmentation benchmark for ex vivo salivary gland specimens, containing 119 HSI samples from 31 patients with multi-class pixel-level annotations. We establish a patient-level five-fold cross-validation protocol and evaluate different input representations, model architectures, and challenging subsets with small tumor and complex boundary. Based on this benchmark, we further propose HyBSD, a hyperspectral boundary-guided spectral-difference network for full-HSI salivary gland tissue segmentation. HyBSD exploits boundary-guided spectral-difference cues to improve tissue delineation in ambiguous transition regions. Extensive experiments show that full-HSI input provides more discriminative information than sampled spectrums, and that HyBSD achieves 74.97% mDice and 87.76% Tumor Dice, with further advantages on the challenging subsets. Dataset and code will be released.

---


### 380. [SF-Flow: Spectral Flow Matching with High Structural Fidelity for Hallucination-Suppressed Scientific Image Generation](https://arxiv.org/abs/2611.30073)

**<font color=#1a73e8>作者：</font>** Zehua Wang, Patxi Fernandez-Zelaia, Mohamed Wahib 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific image generation focuses on reproducing experimental appearance while following a prescribed spatial layout. A key challenge is acute data sparsity, which requires operating with unpaired collections of materials (real images and prescribed layouts), where no direct supervision is feasible. Work on unpaired translation has shown that it is possible to reproduce the texture and intensity variations of real images, but it is extremely hard to retain the intended phase boundaries in the prescribed locations. This paper tackles this challenge and introduces SF-Flow, a flow-matching model trained only on real material images that imposes spectral constraints during generation, producing images that are high-fidelity and consistent with the prescribed layouts. Because layouts enter only at generation time, the approach extends to layout maps outside the distribution of any available training layouts. We evaluate the method on synchrotron tomography of concrete, lens-coupled laboratory microCT of powders, and industrial XCT of additively manufactured metal. Without instrument-specific modeling, we show that SF-Flow achieves substantially higher template agreement and joint fidelity--structure score than previous methods, including contrastive unpaired translation.

---


### 381. [RadarOSV: Unified 3D Scene and Motion Perception from mmWave Radars](https://arxiv.org/abs/2611.30078)

**<font color=#1a73e8>作者：</font>** Yuan Fang, Long Zhuang, Xijia Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave radar offers weather-resilient sensing for 3D occupancy prediction. Existing radar occupancy methods mainly model geometry, with limited joint modeling of semantics and motion. Cascaded imaging radar provides fine spatial detail but has a limited unambiguous velocity range, whereas single-chip radar offers a wider range but coarser spatial resolution. We propose RadarOSV, to our knowledge the first radar-only framework that jointly predicts occupancy, dynamic object semantics, and ground-relative velocity from raw radar data in unified voxels, by exploiting complementary measurements from both radars. Its Polar-to-Cartesian Geometry (PCG) backbone maps polar imaging-radar features into Cartesian voxels through fixed and deformable sampling, guiding cross-radar fusion for geometry and attribute prediction. Single-chip detection outputs provide class evidence, while raw Doppler spectra supply motion features and radial-velocity candidates. The velocity readout selects from these candidates using fused features to resolve aliasing, then combines the selected radial estimate with learned motion. Ego-motion compensation uses radar-estimated velocity, so inference requires no external odometry or other sensors. On K-Radar, single-frame PCG achieves 40.7% mIoU within 12.8 m, compared with RadarOcc's reported 34.3%. On the BRIDGE-Liv dataset, compared with a cascaded-radar baseline predicting the same outputs with external ego velocity, RadarOSV improves macro-averaged accuracy across four dynamic object classes within annotated object regions from 63.1% to 75.5% and reduces object radial-velocity MAE against manual Doppler annotations from 1.03 to 0.51 m/s, while maintaining geometric occupancy mIoU.

---


### 382. [The Growth Path Is the Missing Half of Neural Networks](https://arxiv.org/abs/2611.30081)

**<font color=#1a73e8>作者：</font>** Tingan Jin, Haosong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An artificial neuron computes and learns, but it does not live: the units of a network are fixed when it is designed, and every one of them is kept and paid for whether it is used or not. We give each neuron a second pathway. Beside its Task Path, the usual computation and gradient learning, a dual-pathway neuron has a Growth Path: a nutrient flows from the outputs back through the network, every layer receives the same fixed budget, and each unit is fed in proportion to how much the units above it use it. A well-fed unit divides and a starving unit dies. This allocation is not a separate analysis or pruning step: it runs throughout training and reads only activations and weights. The task is still learned from labels with the ordinary loss, and the training procedure gains no phase, no schedule and no target size. Because the budget is conserved, the competition is zero-sum and a single number sets the size of the network. Switched on in a pretrained network that is deployed on a narrower domain, the Growth Path shrinks the network while it keeps learning. With Adam the network ends 1.0 to 1.2 points more accurate on the domain than the same network trained ordinarily, at 24% to 60% of its compute, and at 12% of the compute it is still ahead; a random choice of the same number of units gives no gain. Letting starving pretrained units sleep instead of die keeps 1.2 to 4.6 points more of the rarely used content. Over 800 changing tasks a network with the Growth Path holds its accuracy while ordinary networks decline. With plain SGD the gains are smaller: at deployment the method trades compute against rarely used content, and on one of the two continual-learning streams it only ties networks of equal size. The experiments are small (three-layer perceptrons on MNIST-like data); what they show is that a conserved, loss-free second pathway can decide by itself which units a network needs.

---


### 383. [Correlated by Construction: Endpoint Choice and the Validation of Protein Screening](https://arxiv.org/abs/2611.30087)

**<font color=#1a73e8>作者：</font>** Eric LoPrete, Galen Loving, George Sabin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning for protein engineering depends on functional measurements collected at screening scale, but the designs those measurements rank are deployed in processes that run elsewhere. Whether a miniaturized assay remains informative under the conditions of use is usually assumed rather than demonstrated. We describe an automated production and screening platform and test the transfer of its solution-phase metal-affinity measurements to immobilized rare-earth separation. Primary pKd-derived separation factors tracked those measured on covalently immobilized protein across 82 protein-metal-pair measurements from 35 proteins, with pairwise Spearman correlations of 0.878 to 0.923 (pooled Pearson $r$ = 0.836; Spearman $\rho$ = 0.869). Separation factors at a fixed metal pair are insensitive to the ordering shared across the lanthanide series, so these coefficients report protein-specific correspondence directly; permutation of protein identity confirms it, giving a mean scrambled correlation of 0.003 and, for the 17 proteins measured on all three pairs, $r$ = 0.917 against 0.001 ($p \approx 0.001$). Profiles compared as profiles behave differently. An independent comparison against published LAMBS profiles for the same protein backbones (417 proteins, 5,212 paired measurements) reproduced normalized raw elution at $r$ = 0.870, but reassigning protein identity still reached 0.840. High profile-level agreement across assay formats is largely attributable to metal preferences shared across the series rather than to protein identity. Transfer can be demonstrated, but the endpoint decides whether a correlation shows it: a pairwise contrast removes the shared ordering; a normalized profile retains it, and needs a null that reassigns protein identity.

---


### 384. [When "A or B" Is Less Likely than A: Coherent Probabilities for Vision Decision Models](https://arxiv.org/abs/2611.30096)

**<font color=#1a73e8>作者：</font>** Seongrae Noh, SeongEun Hong, HyeongYeop Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision decision models answer a multiple-choice question about an image with one probability per option, and software uses them directly. We show that the probabilities depend on how the options are grouped: a merged option "A or B" receives on average 11.5 points less probability than the sum of A and B. This under-additivity appears at every model size from 0.85B to 26B and remains after fine-tuning on labels. We propose CORE, which asks each training question with its options regrouped and trains the answers to all these questions toward one target distribution over the original options, summed into each question's groups. On 1,050 items from seven benchmarks, CORE reduces the total variation distance between the answer to a regrouped question and the original answer summed into the same groups from 14.8 to 5.8 points on the 0.85B model, against 9.4 for the best baseline trained on the same questions. At all five model sizes, CORE reduces this distance without lowering accuracy.

---


### 385. [LMnOP: Pruning 3D Gaussian Splatting via Leave-Many-Out Importance](https://arxiv.org/abs/2611.30102)

**<font color=#1a73e8>作者：</font>** Sunjae Jeong, Jaeseung Kim, Hyoseok Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting renders photorealistic views in real time. However, a single scene often needs millions of Gaussians, so these models are costly to store and render. Pruning reduces this cost by keeping a subset of the Gaussians. A common score is the leave-one-out importance, which is the loss increase when a Gaussian alone is removed. At high pruning ratios, many Gaussians are removed together, so Gaussians that are redundant alone but essential together are lost. We present LMnOP (Leave-Many-Out Pruning), which estimates the importance of each Gaussian under the removal of the other Gaussians. This leave-many-out importance is the average loss increase when a Gaussian is removed while the others are also removed at random. We compute the exact mean and variance of each pixel's color under random removal in closed form, and approximate the importance from them without sampling removal patterns. We refine each Gaussian's probability of remaining with its importance and prune once at the end. Without fine-tuning, LMnOP achieves the best results in 16 of 18 metrics on three datasets at 90% and 99% removal. It improves SSIM and LPIPS over GaussianPOP in all 13 scenes.

---


### 386. [A Polynomial-Time Best-of-Both-Worlds Algorithm for Matroid Semi-Bandit Problems](https://arxiv.org/abs/2611.30104)

**<font color=#1a73e8>作者：</font>** Botao Chen, Junya Honda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Follow-the-Perturbed-Leader (FTPL) offers a computationally attractive framework for online learning, with recent advances establishing Best-of-Both-Worlds (BOBW) guarantees for various bandit settings. For matroid semi-bandits, existing methods offering such guarantees primarily rely on Follow-the-Regularized-Leader (FTRL), which requires solving an optimization problem at each round. We establish BOBW guarantees for FTPL with Fréchet and Pareto distributions with a certain parameter with geometric resampling in the matroid semi-bandit problem, showing that FTPL can simultaneously achieve the minimax-optimal $O(\sqrt{mdT})$ regret in adversarial setting and a logarithmic regret in stochastic setting. To the best of our knowledge, this is the first polynomial-time algorithm for matroid semi-bandits that achieves BOBW guarantees.

---


### 387. [Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones](https://arxiv.org/abs/2611.30106)

**<font color=#1a73e8>作者：</font>** Renzhi Hao, Shirui Cao, Yizhu Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-speech (TTS), voice conversion (VC), and AI-driven speech synthesis enable adversaries to convincingly impersonate trusted individuals during phone calls. Existing defenses often rely on offline analysis, degrade under telephony distortions, or remain vulnerable to adaptive attacks. To address these limitations, we present Ultrasound Watermark, a real-time, smartphone-native framework that protects live calls by binding speech to the caller's physical articulatory motion through acoustic watermarking. During a call, the smartphone emits ultrasonic signals and captures reflections from facial articulatory movements using only its built-in speaker and microphone. Ultrasound Watermark extracts motion features from these reflections and fuses them with outgoing speech to generate a dynamic watermark. Because the ultrasonic measurements are physically and temporally coupled with speech production, they are difficult to spoof without the underlying articulatory motion. A synchronized generator-detector architecture enforces cross-modal speech-motion consistency against replay, synthesized speech, and articulation-mimicking attacks. Ultrasound Watermark operates continuously with less than 200 ms latency overhead and requires no additional hardware. We implement Ultrasound Watermark on iOS and Android and evaluate it using over 2.5 hours of synchronized speech-ultrasound recordings from 22 speakers across eight smartphones and four real-world environments. Results demonstrate robustness to diverse attacks and telephony distortions while preserving perceptual audio quality.

---


### 388. [Quantum-Resilient, PUF-Based, and Anonymity-Preserving Authentication and Key Agreement Scheme for UAV Networks](https://arxiv.org/abs/2611.30107)

**<font color=#1a73e8>作者：</font>** Bhavik Yadav, Bhavya Dixit, Gaurav S. Kasbekar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We design a lightweight authentication and key agreement protocol for Internet of Drones (IoD) environments that simultaneously provides post-quantum security, hardware-rooted trust, and resistance against machine-learning-based Physical Unclonable Function (PUF) modeling attacks. Existing PUF-based authentication schemes for unmanned aerial vehicles (UAVs) offer protection against cloning and physical capture, but generally lack resistance against quantum adversaries. Conversely, recent post-quantum UAV authentication protocols provide quantum-resistant key establishment, yet do not incorporate hardware-bound authentication mechanisms and therefore remain vulnerable to device cloning and physical compromise. To address these limitations, we integrate CRYSTALS-Kyber, dynamic challenge scrambling (DCS), fuzzy extractors, and PUF-based identity binding into a unified framework. The resulting protocol enables anonymous authentication, forward secrecy, resistance to physical capture and replay attacks, and secure drone-to-drone communication, while maintaining suitability for resource-constrained UAV platforms. We provide a formal security analysis of the proposed scheme under the real-or-random model, a ProVerif-based formal verification, an informal analysis of its effectiveness against various attacks, and a performance evaluation of the proposed scheme through communication, computation, and storage cost analyses, which show its advantages over state-of-the-art architectures.

---


### 389. [FToken: Factors as Tokens for Dual-Axis Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.30112)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Yihan Wang, Sheng'en Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On a given trading day, a stock-factor panel describes both how stocks differ across factors and how each factor varies across stocks. Most stock Transformers model relationships among stocks or across time. We introduce FToken, which also models relationships among factors. Its factor branch encodes all stocks' values for one factor as a token, applies self-attention across factors, and maps the result back to one return forecast per stock. A second branch applies attention across stocks in the same panel. A gate combines their forecasts using trailing factor covariance and market volatility. We evaluate both branches on NASDAQ, NYSE, and S&P 500 with the benchmarks' five price features and with 158 factors computed from the same data. On the 158-factor NASDAQ panel, averaging the two forecasts yields an information coefficient (IC) of 0.0421, compared with 0.0392 for the strongest external baseline. The gate raises IC to 0.0443 and gives the highest annualized excess return after costs. The equal-weight ensemble has the higher portfolio information ratio. Both combinations also improve on the strongest external baseline in mean IC on the other two 158-factor panels. On the five-feature NYSE panel, the differences are within the variation across seeds. ```

---


### 390. [Thermal-Guided Low-Light UAV Image Enhancement: A Reliability-Aware Guidance Network and a Unified Benchmark](https://arxiv.org/abs/2611.30114)

**<font color=#1a73e8>作者：</font>** Zhicheng Zhao, Yu Wang, Jiangong Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal-guided low-light image enhancement (LLIE) is promising for nighttime unmanned aerial vehicle (UAV) perception because thermal imagery remains informative under severe visible degradation. However, the degraded visible image serves as both the alignment reference and the enhancement target, making thermal guidance uncertain in its spatial correspondence and local utility under low illumination, sensor differences, and UAV motion. Misaligned or unsuitable thermal cues may introduce artifacts, while spatially varying degradation requires region-specific restoration rather than uniform enhancement. To address these challenges, we propose a Reliability-Aware Multi-Strategy Guidance Network (RMGNet) for thermal-guided UAV LLIE under weak optical-thermal alignment. Its Reliability-Aware Guidance Calibration Module (RAGCM) performs coarse-to-fine displacement estimation and jointly evaluates the reliability of aligned thermal guidance and the usability of degraded visible evidence. Based on calibrated guidance, degradation, and reliability cues, the Multi-Strategy Enhancement Routing Module (MSERM) generates candidates for detail preservation, highlight-protected relighting, and thermal compensation, then spatially routes their contributions. We further construct the UAV weakly aligned Optical-Thermal dataset (UWOT), the largest UAV-oriented benchmark to date for weakly aligned optical-thermal low-light enhancement, containing 5,000 triplets. Extensive experiments show that RMGNet outperforms representative single-modal and multimodal state-of-the-art methods in enhancement quality while retaining competitive computational efficiency and greater robustness to practical cross-modal misalignment. The dataset and code will be publicly available at this https URL.

---


### 391. [Grokking as a Subspace Search: Computing the Destination Before Training](https://arxiv.org/abs/2611.30116)

**<font color=#1a73e8>作者：</font>** Sunjae Jeong, Jaeseung Kim, Hyoseok Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is the phenomenon in which a neural network generalizes long after it has memorized its training data. Many explanations have been proposed for the delay between memorization and generalization. However, none of them can say before training where the network is heading, so they cannot be tested against one another. We show that on group tasks this destination can be computed from the task itself before training begins. It is a low-dimensional subspace of the network's embeddings, which we call the right subspace, and we prove that it is essentially unique. Knowing the destination makes our hypothesis falsifiable: the delay is a search for the right subspace, and generalization begins when the network finds it. When we give the network the right subspace from the start, the delay disappears. When we take the right subspace away, accuracy stops at a ceiling that we compute before training, and on multiplication the network cannot generalize at all. When we train the network normally, its embeddings move toward the right subspace by themselves, long before test accuracy rises. Finally, interventions during training show that this search sets the length of the delay, and that noise in the optimization does not. On every group task that we tested, grokking is a search for the right subspace, and the delay is the time that this search takes.

---


### 392. [What Remains After Concept Erasure? Sparse Autoencoder Probes for Auditing Diffusion Models](https://arxiv.org/abs/2611.30117)

**<font color=#1a73e8>作者：</font>** Zhuan Shi, Lu Wei, Yuta Nakashima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to remove selected visual concepts from text-to-image diffusion models while preserving the generation of non-target concepts. Evaluation typically measures target suppression and non-target preservation in generated images, but a concept's absence from these outputs does not establish its removal from the model. We introduce SAE-Audit, a white-box audit using sparse autoencoder (SAE) probes to test whether activation interventions can restore target-concept generation without changing model weights or test prompts. After verifying target suppression, we compare the original and edited models using a shared SAE representation learned from original-model activations, identifying features whose target-related responses weaken after erasure. We inject sparse directions derived from the original-model responses into the edited model, keeping these directions fixed across test prompts, and evaluate recovery on held-out scene families. Experiments span six erasure methods and four domains: objects, artistic styles, copyrighted content, and nudity. Interventions using a few dozen selected SAE features yield higher average recovery rates than matched random-feature interventions, with recovery concentrated in objects and nudity following cross-attention edits. Most styles and copyrighted concepts show limited recovery under the tested intervention settings. These findings show that output suppression can coexist with responsiveness to sparse concept directions supplied from the original model.

---


### 393. [Small data machine learning: the trilemma of low-sample tabular regimes](https://arxiv.org/abs/2611.30118)

**<font color=#1a73e8>作者：</font>** Ilya Emelyanov, Dmitrii Dobrydin, Muhammad Hamza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small tabular datasets leave few observations for choosing a model and assessing its predictions. We examine these competing demands in controlled simulations and on six public datasets, using SmallGBM and SmallMLP as fixed-configuration case studies. Three results illustrate why the choice of evaluation matters. First, at n = 100, five-fold cross-validation overstated the gain from tuning XGBoost by 0.063 ROC-AUC on random labels, while tuning improved independent-test ROC-AUC by 0.0078 on a Gaussian mixture. Second, when 20% of binary training labels were flipped, the median within-trial ROC-AUC loss was 0.0210 for SmallGBM and 0.0778 for a fixed 200-tree XGBoost configuration. A separate regression experiment showed the sensitivity of squared-error training to heavy-tailed responses. Third, in a heteroscedastic regression experiment, locally weighted SmallMLP intervals covered about one percentage point more test responses than ordinary split conformal intervals at both tested dimensions. Their mean widths also increased. On a Gaussian classification task with linear log odds, logistic regression achieved the highest mean ROC-AUC at all seven training sizes. These experiments identify settings in which a small-data model helps and quantify the cost of its assumptions.

---


### 394. [AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events](https://arxiv.org/abs/2611.30120)

**<font color=#1a73e8>作者：</font>** Haiyu Xu, Yiyang Chen, Jiayi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge cases are not the long tail; they are the norm. An embodied system deployed across changing environments, bodies, objects, and tasks will routinely encounter combinations that were absent from its training data. General-purpose physical intelligence therefore requires world models that reuse prior knowledge, predict consequences, and adapt with little or no additional training. Yet current evaluations of conditional video generation emphasize visual quality, prompt alignment, or isolated physical plausibility, leaving systematic generalization difficult to measure. We introduce AxE Bench, a benchmark that organizes condition changes along eight factors of the acting agent and of its environment, and pairs every original condition with controlled variants that change one side or both. WBench-plus applies the same structure to an existing multi-turn benchmark, pairing each WBench scenario with variants on the environment side, through its world setting or camera behavior, or on the agent side, through its interaction instructions. Additionally, to score generated futures, we develop an evaluation harness that combines vision-language reasoning with targeted computer-vision evidence, converting each video into temporally localized events and comparing generated events with reference events in both time and semantics. We summarize each model with the AxE Score, event Fidelity weighted by its Stability across original-variant pairs. Across twenty models, generated events match reference events far more often in timing than in content: no model exceeds a Fidelity of 13.01, the highest Stability is 0.55, and the highest AxE Score is 7.10. Together, these components turn world-model generalization from an informal aspiration into a falsifiable evaluation program for real and simulated interactions. Our project website can be found at: this http URL

---


### 395. [iFeST: An Iterative Motion Correction Framework for Fetal Brain Diffusion MRI via Frequency-Spatial-Temporal Modeling](https://arxiv.org/abs/2611.30131)

**<font color=#1a73e8>作者：</font>** Haoan Xu, Ruike Chen, Jing Xia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fetal brain diffusion magnetic resonance imaging (dMRI) is a pivotal non-invasive tool for assessing the development of brain connectivity and microstructure. However, the prolonged acquisition times and complex sampling requirements render dMRI highly susceptible to unpredictable fetal motion. Existing motion correction methods typically process each dMRI volume independently and focus on inter-slice motion. Such strategies fail to utilize the coherent information between dMRI volumes along different diffusion directions and lack the ability to restore the intra-slice corruption. To address these limitations, we proposed iFeST, an iterative framework that combines frequency (k-space), spatial, and temporal (inter-slice) modeling for fetal brain dMRI motion correction. At each iteration, iFeST integrates information across diffusion directions into fiber orientation distributions (FODs). These distributions encode local fiber orientations within each voxel and serve as microstructural priors for intra-slice restoration and inter-slice alignment in the next iteration. To train the framework, we developed a fetal brain dMRI motion simulator that synthesizes compound motion artifacts from FODs. Evaluation on simulated datasets demonstrated that iFeST outperformed four inter-slice networks in motion estimation and three intra-slice networks in image restoration. Further validation on a real-world dataset confirmed significantly better volume reconstruction and FOD estimation than conventional pipelines. Overall, iFeST provides a learning-based framework for fetal dMRI motion correction, restoring motion-corrupted data and improving microstructural reconstruction for downstream diagnostic applications.

---


### 396. [LambdaLens: Auditing a Representation-Changing Hyperparameter in Graph Neighbor Embedding](https://arxiv.org/abs/2611.30140)

**<font color=#1a73e8>作者：</font>** Juntang Wang, Yihan Wang, Sheng'en Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Changing a graph embedding parameter can change what the layout represents. In SG-t-SNE-$\Pi$, the rescaling parameter $\lambda$ changes the probability assigned to each neighbor before optimization begins. We introduce LambdaLens to trace that change from individual edges to the resulting layout. For nodes with at least two neighbors, we derive a normalized power path. When the original weights are unequal, the number of neighbors determines where the weights become uniform and where their ordering reverses. Near $\lambda=1$, the rate of change in each edge probability depends on its surprisal relative to the neighborhood entropy. To measure the geometric effect, we vary $\lambda$ while holding the input graph, initialization, random seed, and optimizer settings fixed. Across six graphs, some layouts continue to move as $\lambda$ increases, others stabilize early, and others barely move. PubMed has the widest relative spread in node degree, yet its layout changes little. On four datasets with class labels, four probes recover 98.48-100% of the best label-fidelity score on a 16-value grid, using 75% fewer evaluations. In a six-dataset comparison, SG-t-SNE-$\Pi$ attains the highest observed primary score on four datasets and ranks among the top three on all six. On Citeseer, four probes come close to the dense-grid optimum, yet PHATE better preserves class structure, making a change of embedding pipeline worth considering on that graph. ```

---


### 397. [Separating Protocol Effects from Spatio-Temporal Evidence in Person Re-Identification Re-Ranking](https://arxiv.org/abs/2611.30142)

**<font color=#1a73e8>作者：</font>** Mochamad Rizal Fauzan, Doan Pham Thao Nhu, Jeslin Konthoujam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal priors re-rank person re-identification matches using the camera pair and the time gap, and are reported to add large gains on Market-1501. We ask how much of such a gain encodes the evaluation protocol rather than learned spatio-temporal evidence. Starting from a course-project re-ranker that adds log camera-transition and log time-gap terms to cosine similarity, we train a strong ResNet-50 baseline (Rank-1 94.3 %, mAP 86.2 % over three seeds), choose the fusion weights on an identity-disjoint validation split and evaluate on the official test set with control priors. The repository form adds 2.30 mAP points, but a one-parameter penalty on same-camera pairs alone adds 2.19: the protocol never places a true match in the query's camera, so the penalty removes distractors for free. The time term of that form is almost unused; a pair-level diagnostic traces this to its modelling the time gap given a match without dividing by the gap distribution of all candidate pairs. A likelihood-ratio prior adds 4.04 points without the penalty and 5.62 with it; shuffling the time stamps removes the extra gain, so about 3.43 points are tied to identity. The prior fixes the first-ranked match of 4.2 % of the queries and breaks it for 0.1 %. The gain shrinks as the visual baseline improves (11.9 to 5.62 points between a 70.5 % and a 86.2 % mAP model) and concentrates on queries whose true matches share the query's video sequence. The study covers one dataset, one backbone and three seeds.

---


### 398. [IADR: Interface-Augmented Neural Operator for Phase-Field Mean-Curvature Flow](https://arxiv.org/abs/2611.30153)

**<font color=#1a73e8>作者：</font>** Qinyi Zhang, Duanyu Feng, Yangshuai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Allen-Cahn equation is one of the standard phase-field models for mean-curvature flow (MCF), parameterised by the diffuse-interface width $\varepsilon$. Practical simulations span a range of $\varepsilon$, so a single model covering this range is needed. PDE-specific neural operators are accurate but must be retrained at every $\varepsilon$; general neural operators cover $\varepsilon$ in one model but lose the phase-field structure of the target. We introduce Interface-Augmented Diffusion-Reaction (IADR), a neural operator that addresses both shortcomings: a target network with a diffusion-and-reaction (DR) structure preserves the phase-field structure of the Allen-Cahn equation, while a hypernetwork that maps $\varepsilon$ to the weights of this target network amortises the dependence on $\varepsilon$ across the range. A single IADR matches the per-$\varepsilon$ specialists on in-distribution data within the prescribed range, retains their cross-shape generalisation under both $\varepsilon$- and geometry-out-of-distribution shifts, and retains their compact DR target structure with millisecond-scale inference. We further establish a conditional $K$-step rollout error bound under consistency and stability assumptions.

---


### 399. [Preserve to Compress: Beyond Low-Dimensional Latents in One-Step Diffusion Codec](https://arxiv.org/abs/2611.30154)

**<font color=#1a73e8>作者：</font>** Chuqin Zhou, Xiaoyue Ling, Yuhang Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained latent diffusion models bring powerful generative priors to ultra-low-bitrate image compression, but their latent spaces reflect a reconstruction--generation tradeoff. Low-dimensional latents reduce modeling cost but can discard image details, while higher-dimensional latents improve reconstruction yet make diffusion optimization harder under a fixed computational budget. Generative codecs that adopt these pretrained spaces also inherit this compromise, even though compression requires fidelity to a specific source image. In particular, low-dimensional latent interfaces can discard source details before coding and restrict how much decoded information reaches the image decoder. We propose Preserving Information for Compression and Synthesis (PICS), a one-step generative image compression framework that adapts these interfaces to preserve source information. Our Information-Preserving Adaptors (IPAs) expose richer features for coding and retain decoded information throughout reconstruction, while deferred decoder adaptation stabilizes training and helps the image decoder exploit the expanded representations. Experiments on Kodak, DIV2K, and CLIC 2020 show average BD-rate savings of 52.64% and 39.61% over StableCodec at matched LPIPS and DISTS, respectively.

---


### 400. [UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction](https://arxiv.org/abs/2611.30157)

**<font color=#1a73e8>作者：</font>** Ye Pan, Chenfei Liao, Bin Ren 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective real-time, full-duplex multimodal interaction requires systems to understand not only what users say, but also the communicative needs conveyed through prosody, facial expressions, gestures, and context, and to generate audiovisual responses that appropriately address those needs. Existing evaluations offer limited insight into whether systems translate an understanding of such unspoken needs into effective responses. We introduce UUBench, a benchmark for assessing how well multimodal interactive systems Understand the Unspoken intent and address users' implicit communicative needs. The inherent subjectivity of implicit intent inference poses a key challenge for evaluation. To address this, we introduce Process-Oriented Scoring, which grounds the assessment of intent fulfillment in observable auditory and visual cues, such as prosody and gestures. Rather than relying solely on a single overall score, it evaluates how well a response addresses the communicative needs conveyed by each applicable primitive dimension. We aggregate the dimension-level scores according to each dimension's relevance to the annotated evidence. Beyond intent fulfillment, Outcome-Oriented Scoring evaluates the naturalness, appropriateness, and human-likeness of the reply itself under audio-only, visual-only, and audiovisual conditions. To make these judgments traceable to observable evidence, we propose a Fact-Grounded Scoring JEV module, which uses structured, timestamped audiovisual observations of the user and the digital human's reply to assess one dimension or criterion at a time. UUBench provides a foundation for assessing whether multimodal interactive systems respond effectively to meaning beyond literal wording, supporting progress toward context-aware, real-time, full-duplex interaction.

---


> [!TIP]
> 当前位于：**351-400**（第 8/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
