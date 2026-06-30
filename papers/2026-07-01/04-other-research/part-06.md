# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 251. [t-STEP: An interpretable model for Total Electron Content predictions and irregularities estimations](https://arxiv.org/abs/2606.29644)

**<font color=#1a73e8>作者：</font>** Stephen Tete, Carl Shneider, Maxime Cordy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earth system infrastructures relying on satellite-based technologies, such as Global Positioning System (GPS) communications, are affected by ionospheric Total Electron Content (TEC) gradients. Modeling these gradients under physical constraints remains challenging due to their dynamic and transient nature. While existing machine learning (ML) models can predict hourly TEC variations, it remains unclear whether their temporal resolution is sufficient to preserve small-scale TEC irregularities within predicted signals. To address this gap, we introduce an interpretable ML-based model, t-STEP, designed to predict TEC at a 30-second resolution and estimate irregularity signatures from the modeled signals. This high cadence enables the derivation of Rate of TEC changes (ROT) and the ROT Index (ROTI) as diagnostic indicators of ionospheric variability. The model is developed using GPS observations from solar cycle 24 at a station located at 5.49°S, 47.49°W. A multi-metric evaluation framework, including dynamic time warping, is used for robustness assessment, while SHAP (SHapley Additive exPlanations) provides insight into feature contributions. The 30-second TEC predictions achieve 91% accuracy with a mean absolute error (MAE) of 4.38 TECU during high solar activity (2015). Compared with the International Reference Ionosphere (IRI-2020), the hourly model improves accuracy by 35%, reduces absolute errors by 57%, and increases prediction skill by 54%. More importantly, the 30-second model captures TEC irregularity dynamics and morphologies during geomagnetic storms of different intensities, outperforming an attention-based Long Short-Term Memory model under the same experimental conditions. This study demonstrates the potential of a single TEC prediction framework for scalable irregularity monitoring without requiring separate models for individual transient events.

---


### 252. [Resolution Thresholds in VLM Detection of Harmful ASCII Art Across Construction Modes and Languages](https://arxiv.org/abs/2606.29649)

**<font color=#1a73e8>作者：</font>** Yikai Hua, Peter West  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (VLMs) are increasingly deployed as content moderation tools, yet they remain vulnerable to jailbreak attacks in which harmful text is visually encoded as ASCII art. This can allow inappropriate or harmful content to bypass moderation systems. To address this vulnerability, this paper investigates how image resolution affects VLM detection of harmful ASCII art across eight character construction modes (L1-L8), ranging from dense block characters to word-embedded designs. We evaluate eight state-of-the-art VLMs on English and Chinese corpora using a pipeline that generates ASCII art images at ten resolution scales, probing whether a consistent detection-failure threshold exists across models, modes, and languages. Results indicate that detection rates decline sharply above certain resolution thresholds, and that word-based modes are the most resistant to detection across the full resolution range. These findings reveal a systematic vulnerability in VLM-based content moderation systems and motivate resolution-aware evaluation standards.

---


### 253. [Safety from Honesty in a Disinterested AI Predictor](https://arxiv.org/abs/2606.29657)

**<font color=#1a73e8>作者：</font>** Yoshua Bengio, Oliver Richardson, Tomáš Gavenčiak 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems become more capable, training procedures that optimize for downstream outcomes risk introducing implicit agency: goal-directed behavior that designers never specified. We present a formal safety argument for the Scientist AI (SAI) Predictor, trained to approximate the Bayesian posterior conditioned on a dataset of "epistemically contextualized" natural-language statements. We argue that such a Predictor can honestly predict agents, actions, and their consequences without itself being an agent that selects outputs to achieve goals. This rests on data representation and on the training procedure. Epistemic contextualization of text distinguishes latent factual claims from communication acts, so expressions of goals are treated as evidence to be explained rather than drives the model adopts. With a posterior-seeking training objective, this is intended to drive the Predictor toward calibrated, cautious predictions. Training proceeds so downstream effects of deploying a prediction never serve as a reward signal; any agency the system needs is supplied by explicit scaffolding constrained by guardrails. We prove that, under assumptions on the training dynamics and on the argued sparsity of dangerous Predictors, the probability that training produces a Predictor whose guarded deployment carries residual harm above a specified threshold is small: a dangerous Predictor would have to underestimate harm in a coordinated way across many queries while such coordinated patterns are rare under the initialization distribution and receive no direct training signal. Safety and accuracy are jointly supported in this framework, since the constraints that secure accuracy are the same ones that make coordinated deception costly. These guarantees against misalignment and agency arising from within the Predictor itself do not preclude the use of the Predictor as part of an agentic system.

---


### 254. [Diversity is the Strength of the AI Crowd](https://arxiv.org/abs/2606.29661)

**<font color=#1a73e8>作者：</font>** Matthew Aitchison, Scott Jeen, Toby Shevlane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Top AI forecasting systems are approaching superforecaster-level accuracy on future world events, but still rely primarily on off-the-shelf LLMs combined with forecasting-specific context gathering and scaffolding. We study how to improve this recipe through ensembling: given a fixed number of samples, which off-the-shelf model forecasts should be combined to maximize accuracy? On binary questions from the Metaculus AI Benchmark, we find that individual accuracy is not enough: many frontier LLMs make highly correlated predictions, limiting the value of additional forecasts from the same or similar models. Instead, the strongest ensembles combine accurate but diverse forecasters, with models such as \model{Grok 4} contributing disproportionately because their predictions are less correlated with other frontier LLMs. These results suggest that the strength of the AI crowd comes not from sampling more forecasts indiscriminately, but from combining forecasts across models with complementary errors, motivating forecasting systems that explicitly optimize for both model quality and diversity.

---


### 255. [I-BBS: Coordinate-Free Inference of Latent Sub-Manifolds Using Random Distance Matrix Theory](https://arxiv.org/abs/2606.29675)

**<font color=#1a73e8>作者：</font>** Igor Halperin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bogomolny, Bohigas and Schmit (BBS) found that the spectrum of the pairwise distance matrix on N points sampled from a smooth d-dimensional manifold encodes a signature of the underlying geometry. We develop I-BBS (Inference-BBS), a coordinate-free method that identifies a low-dimensional latent sub-manifold embedded in a high-dimensional ambient distance matrix alone, without accessing an ambient high-dimensional vector space. It therefore applies even when that space is only partly observable or undefined. We model the ambient embedding by two classes of generative noise, model-based and model-free. The noise mixes the latent signal with off-manifold components, so the eigenvalues reorganise collectively and the latent geometry cannot be read off eigenvalue by eigenvalue. We recover it instead from two integer-stable signatures that survive the noise: the multiplicity of the top non-Perron multiplet, which fixes $d$, and a parameter-free law for how the multiplet positions shrink as the noise grows. On synthetic spheres $S^1$, $S^2$ and $S^3$ these integer signatures are far more stable under noise than the continuous spectral slope, and a blind test recovers both the manifold and the noise model from a single distance matrix. Applications to neural-network representations and to the dynamic training regime are developed in two companion papers.

---


### 256. [Learning as Observable Matrix Dynamics: Diffusive Relaxations versus Phase Transitions](https://arxiv.org/abs/2606.29679)

**<font color=#1a73e8>作者：</font>** Igor Halperin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Observable Matrix Dynamics (OMD) is a diagnostic framework that probes the dynamics of high-dimensional internal representations of inputs by a neural network via a fixed-size $N \times N$ distance matrix $M(t)$ on a held set of $N$ inputs. OMD uses methods of random matrix theory and particle dynamics to explore spectral reorganisations that are missed by scalar loss functions, but are informative of the training process. We read $M(t)$ against a perturbative ambient-versus-latent decomposition extending the Bogomolny--Bohigas--Schmit (BBS) theory of random distance matrices, with per-snapshot diagnostics for the top-of-spectrum band structure and ambient noise, trajectory-level observables linking snapshots, and a 3D MDS embedding (bottom-three eigenvectors) rendering training as a moving particle cloud. Across seven experiments, diffusive regimes lack stable top-of-spectrum band structure, while sharp endogenous or externally driven reorganisations produce stable fingerprints: consistent with smooth or product latent geometries in BBS-adjacent cases, and with finite-cluster or Fourier-soliton structures otherwise. OMD thus reads the geometric regime of a representation rather than reporting a single intrinsic dimension.

---


### 257. [Sample-Efficient Learning of Probabilistic Causes for Reachability in Markov Decision Processes with Probabilistic Guarantees](https://arxiv.org/abs/2606.29681)

**<font color=#1a73e8>作者：</font>** Ryohei Oura, Georgios Fainekos, Hideki Okamoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic model checking for Markov decision processes (MDPs) provides quantitative guarantees, but often offers limited insight into why undesired outcomes occur. Probability-raising (PR) causality addresses this by identifying states whose visitation increases the probability of reaching designated states. Existing PR-cause identification methods, however, use MDP modifications not well-suited for learning: the gap between conditional and unconditional reachability probabilities can be hard to detect from transition samples, and construction requires reachability probabilities of the MDP, which are unavailable when transition probabilities are unknown. We study unknown MDPs and propose a learning approach with probabilistic guarantees for PR-cause identification. Our key ingredient is a restart-based MDP modification that reduces PR-cause checking to two conditional reachability queries without using reachability values of the original MDP. We prove correctness, establish sample-complexity bounds, and develop an anytime learning-and-checking algorithm based on two-sided value iteration that progressively classifies states as causal, non-causal, or undecided. Experiments on two benchmarks demonstrate reliable and fast identification of PR causes.

---


### 258. [PoseShield: Neural Collision Fields for Human Self-Collision Resolution](https://arxiv.org/abs/2606.29686)

**<font color=#1a73e8>作者：</font>** Zhengyuan Li, Zeyun Deng, Yifan Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-collision remains a persistent challenge in SMPL-based human pose estimation and motion generation. Under extreme articulations or stochastic motion synthesis, generated meshes frequently exhibit self-penetrations, leading to physically implausible results. We propose PoseShield, a neural collision constraint defined directly in SMPL pose space. We formulate collision correction as a constrained optimization problem and connect the learned constraint with the Eikonal equation. Enforcing Eikonal regularization ensures non-vanishing gradients near the collision boundary, improving numerical stability and robustness of the optimization process. Unlike prior methods that operate in the mesh space or rely on heuristic penalties, our approach operates directly in the low-dimensional space of human poses and is theoretically grounded. The same learned constraint extends to human motion sequences, providing a generator-agnostic post-hoc collision corrector without retraining the underlying motion model. Experiments on a newly constructed SMPL pose benchmark show that our method achieves a 95.8% success rate and outperforms state-of-the-art baselines.

---


### 259. [IG-Lens: Exact Additive Probability Attribution Across Transformer Layers via Telescoping Integrated Gradients](https://arxiv.org/abs/2606.29693)

**<font color=#1a73e8>作者：</font>** Duc Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask a simple question about decoder-only transformers: \emph{between which two layers is the probability of a predicted token actually produced?} Existing layer-wise readout tools answer only approximately. The logit lens and its trained variant report a per-layer \emph{level} of probability but give no additive decomposition; their estimates are biased and non-monotone across depth. Direct Logit Attribution and related residual-stream methods are additive, but only in \emph{logit} space -- the softmax nonlinearity breaks additivity in probability space, precisely the quantity one usually cares about. Layer Conductance integrates gradients per layer, but attributes each to its own baseline and so does not sum to the total change in prediction. We introduce \textbf{IG-Lens}, a telescoping application of Integrated Gradients along a single path through the hidden states from a baseline to the final layer. Crediting each segment to the layer it terminates at yields a layer-wise attribution whose sum is \emph{exactly} the change in target probability, with the softmax inside the integration path rather than linearized away. Our default estimator credits each integration step its \emph{observed} change in target probability -- a prediction-aware reweighting in the spirit of IDGI -- rather than its raw gradient. Because the readout is a one-dimensional probability, this collapses each segment to a telescoping sum of endpoint values, so completeness holds exactly (to floating point) at \emph{any} step count, removing Riemann discretization error while suppressing steps that show gradient sensitivity without a change in output. We give the telescoping identity and its proof, verify completeness to floating point, and describe a single-pass batched implementation computing the full token-by-layer map without any backward call. Code: this https URL.

---


### 260. [Progressive Self-Supervised Learning with Individualized Community Assignment for Brain Network Analysis](https://arxiv.org/abs/2606.29695)

**<font color=#1a73e8>作者：</font>** Hairui Chen, Yanwu Yang, Jianfeng Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain networks exhibit a modular community structure that varies across individuals and neurological conditions. However, existing self-supervised learning (SSL) methods often overlook this heterogeneity, relying on generic masking strategies that fail to capture subject-specific functional organization. We propose BrainPICM, a self-supervised framework for brain network analysis via progressive individualized community aware masking. BrainPICM formulates ROI-to-community mapping as a progressive unbalanced optimal transport process, yielding soft assignments and per-ROI confidence scores. Guided by these confidence estimates, a curriculum-style masking strategy gradually incorporates low-confidence, potentially pathological regions into training, enabling the model to learn both stable modular structures and individual variations. Additionally, a deviation-aware aggregation module quantifies functional reorganization by measuring mass redistribution relative to a population template, enhancing interpretability and downstream prediction. Experiments on three fMRI datasets (ABIDE-I, ADHD-200, ADNI) show that BrainPICM consistently outperforms state-of-the-art supervised and SSL methods in diagnostic accuracy, indicating that explicitly injecting modular community structure into masked modeling yields more functionally consistent and generalizable representations. The source code for this approach will be released at this https URL.

---


### 261. [MF-UAVPose6D: A Model-Free Monocular 6-DoF Pose Estimation Framework for Fixed-Wing UAVs](https://arxiv.org/abs/2606.29697)

**<font color=#1a73e8>作者：</font>** Juanqin Liu, Leonardo Plotegher, Eloy Roura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For uncrewed aerial vehicles (UAVs), estimating six-degree-of-freedom (6-DoF) poses is essential for airspace situational awareness, target tracking, and counter-UAV operations. However, non-cooperative targets usually lack computer-aided design (CAD) models and keypoint priors, making existing model-based or keypoint-matching methods difficult to apply reliably. To address these challenges, this paper proposes MF-UAVPose6D, a model-free monocular 6-DoF pose estimation framework for fixed-wing UAVs. During inference, the method takes only a single red-green-blue (RGB) image and camera intrinsics as input. It first obtains a stable target anchor through heatmap-guided center localization, introduces a Perspective-Aware Module (PAM) to model observation-ray priors, exploits Dynamic Topological Sampling (DTS) to complement weak structural cues from the wings, fuselage, and tail, and adopts a decoupled translation-rotation pose decoding mechanism to estimate the 6-DoF pose. In addition, we construct the FW-UAV6DPose synthetic dataset, which covers fixed-wing UAV observations across diverse distances, viewpoints, and poses. Experimental results show that MF-UAVPose6D achieves accurate and efficient monocular 6-DoF pose estimation without requiring CAD models, and demonstrates strong robustness in long-range rotation estimation, depth recovery, and joint pose evaluation.

---


### 262. [Early Warning Signals for OpenVLA Failure under Visual Distribution Shift](https://arxiv.org/abs/2606.29699)

**<font color=#1a73e8>作者：</font>** Dipesh Tharu Mahato, Rachel Ren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Action models combine perception, language grounding, and control in a single policy, but their failures are hard to diagnose once visual conditions shift. We test whether OpenVLA feedforward activations contain linearly decodable information about near term task failure in LIBERO manipulation rollouts. The policy is fixed throughout. We log internal activations during execution and fit lightweight monitors after the rollouts are collected. Occlusion is the main controlled stress test. It reduces OpenVLA success from $57\%$ to $17\%$ over $100$ episodes per condition. Under this shift, a logistic probe at layer 16 reaches AUROC $0.972$ and AUPRC $0.352$ for predicting failure within a $15$ step horizon. It outperforms both a mean difference direction and an action disagreement baseline. A sparse layer sweep finds uneven decodability across depth: layer 16 is strongest among the tested layers, layer 8 remains informative, and layer 10 is weaker. To check whether the monitor is just an occlusion detector, we also evaluate color shift and camera jitter without refitting. Color shift produces no failures in this setting, so it is a benign control rather than a failure benchmark. Camera jitter does induce failures, and the occlusion trained monitor remains above random. The result is deliberately limited: OpenVLA internal states contain failure relevant structure under controlled perceptual shift, but these experiments do not establish a causal mechanism, task held out generalization, or a deployable recovery system.

---


### 263. [SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution](https://arxiv.org/abs/2606.29713)

**<font color=#1a73e8>作者：</font>** Aojie Yuan, Yi Nian, Haiyue Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination is the reliability bottleneck for LLM-based agents, and fact attribution verifiers are the last line of defense -- yet today's verifiers emit only opaque binary labels, leaving agents unable to self-correct and operators unable to audit. We present SEVA, a structured verification agent that emits evidence alignments, step-by-step reasoning chains, calibrated confidence, and a six-category error diagnosis with actionable fixes. Training such an agent with RL is non-trivial: standard binary reward on multi-component output triggers advantage collapse -- within-group reward variance vanishes and the GRPO gradient disappears. We resolve this with a process reward that decomposes verification quality into five independent components weighted 70/30 toward process signals, restoring the gradient and inducing an implicit curriculum -- the agent first masters verification behavior (alignment 0.917 -> 0.997, format 72% -> 100%), then outcomes (F1 64.9 -> 69.0). Structured output further enables a Verify -> Reflect -> Probe -> Refine self-evolution loop, which over four rounds on a 7B model surfaces an unexpected structural finding: each round produces a benchmark-specialist, not a generalist (+15 pp on HaluEval, -10 to -14 pp on TruthfulQA in the same model, persistent at 4x data). On ClearFacts, SEVA-3B matches GPT-4o-mini (69.0 vs. 69.8 F1) while producing substantially richer, auditable output -- confirming a principle that should generalize: for any RL task with multi-component generation, reward granularity must match output granularity.

---


### 264. [UniVAD v2: Unified Visual Anomaly Detection via Support-Conditioned Boundary Construction](https://arxiv.org/abs/2606.29714)

**<font color=#1a73e8>作者：</font>** Zhaopeng Gu, Bingke Zhu, Zhaowen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified visual anomaly detection seeks to train a single detector that can be deployed across categories, domains, and application scenarios. In the few-shot transfer regime, the key challenge is to estimate an episode-specific boundary for an unseen target category from a small support set. Existing approaches mainly infer this boundary from normal-side evidence and provide limited abnormal-side evidence for deployment-specific tolerance. Within the normal side, they often struggle to jointly capture local correspondences and global support-query relations, making their boundaries less reliable for unseen anomalies. To address these issues, we propose UniVAD v2, a two-sided support-conditioned boundary construction framework for unified visual anomaly detection. Built on the component-patch divide-and-conquer framework of UniVAD, UniVAD v2 strengthens the normal side with an Optimal Transport-based Relational Modeling module (OTRM), which complements retrieval with support-query matching through transport-style allocation, and an Adaptive Coordination mechanism for Retrieval and Relational Modeling (ACRRM), which estimates episode-conditioned reliabilities to fuse the two sources of evidence. On the abnormal side, a Few-Shot Abnormal Reference module (FAR) converts optional abnormal references into rejection-side evidence for boundary adjustment. Experiments on six datasets spanning industrial, logical, and medical anomaly detection demonstrate strong cross-domain generalization. Under the 1N-shot protocol, UniVAD v2 improves the mean image-level AUC over UniVAD from 83.0\% to 84.5\%, and further reaches 85.7\% in the 1N+1A-shot setting. On the MVTec-AD Severity Split (MVTec-AD-SS), UniVAD v2 achieves 96.2\% image-level AUC and 96.9\% pixel-level AUC, showing that abnormal references enable controllable boundary customization without retraining.

---


### 265. [Accurate Recognition of Pneumonia and COVID-19 by Geometric Shape Normalization of Lung Region using Automatic Landmark Detection and Piecewise Affine Warping](https://arxiv.org/abs/2606.29715)

**<font color=#1a73e8>作者：</font>** Salvador E. Ayala-Raggi, Rafael Alejandro Cruz-Ovando, Lauro Reyes-Cocoletzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an automatic system for recognizing pulmonary diseases in chest X-rays using geometric normalization of the lung region. The method combines three modules: (1) a ResNet-18 landmark detector with coordinate attention that predicts 15 lung-contour landmarks, achieving a mean localization error of 3.61 pixels through an ensemble of four models with test-time augmentation; (2) a geometric normalizer based on Generalized Procrustes Analysis, Delaunay triangulation, and piecewise affine warping to map each lung region to a standardized shape; and (3) a ResNet-18 classifier with transfer learning and SAHS contrast enhancement to classify images as COVID-19, Viral Pneumonia, or Normal. On the COVID-19 Radiography Database, the normalized-image classifier achieved 98.60+/-0.26% accuracy and 98.00% F1-Macro using five-fold cross-validation. Although original images produced slightly higher raw accuracy, Grad-CAM and cropping experiments suggest that this advantage is partly influenced by acquisition artifacts. In contrast, geometrically normalized images outperformed artifact-masked/cropped unaligned images on both the COVID-19 Radiography Database (98.60% vs. 96.24%) and a balanced adult-pediatric mixed dataset including pediatric cases from the Kermany dataset (94.67% vs. 94.17%). These results suggest that anatomical alignment can provide a more controlled and artifact-resistant representation for pulmonary disease recognition.

---


### 266. [AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World](https://arxiv.org/abs/2606.29716)

**<font color=#1a73e8>作者：</font>** Zhongqiang Song, Guanying Chen, Yuqi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of monocular metric depth estimation in aerial UAV imagery. Although recent data-driven methods have achieved remarkable progress in ground-level scenarios, models trained primarily on street-view and indoor datasets exhibit significant domain gaps when applied to aerial viewpoints. To tackle these challenges, we introduce AerialMetric, a benchmark dataset designed to evaluate and facilitate the adaptation of monocular metric depth estimation under UAV aerial viewpoints. The dataset consists of four complementary subsets collected from different sources, jointly covering real-world photogrammetry data, controlled aerial acquisition settings, photorealistic synthetic scenes, and in-the-wild Internet imagery. Totally, AerialMetric provides 52K real-world and 16K synthetic image-depth pairs with reliable metric ground truth. Based on this dataset, we conduct systematic evaluations of existing state-of-the-art models under aerial settings and investigate the impact of viewpoint, altitude, and camera parameters on metric depth prediction. In addition, by fine-tuning representative metric depth model on our dataset, we establish a comprehensive aerial benchmark and achieve state-of-the-art performance across diverse aerial imagery. Our dataset, code, and model weight are publicly available at this https URL.

---


### 267. [The Hidden Cost of Resampling: How Imbalance Correction Degrades Probability Calibration in Tree Ensembles](https://arxiv.org/abs/2606.29720)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resampling methods such as SMOTE and random under/over-sampling are standard tools for class-imbalanced classification, almost always evaluated by minority-class accuracy or F1. Prior work has established that undersampling degrades probability calibration by distorting the training prior [1]. We extend this lens to synthetic oversampling (SMOTE) and provide a practical, evidence-based guide to when calibration damage matters and how to fix it. Across five public datasets (imbalance ratio 1.9-70) and two ensemble models (random forest, gradient boosting), with ten seeds and paired statistics, we find: (1) SMOTE's calibration cost is real but small (ECE +0.009; Cliff's delta = +0.27, small-to-moderate) across the studied imbalance range (IR 1.9-70) and its discrimination gains typically outweigh the calibration penalty; (2) random undersampling is the genuine danger -- its damage grows sharply with imbalance, inflating ECE from 0.008 to 0.395 on a dataset with ratio 70, largely because the resulting training sets are too small to estimate probabilities reliably; (3) a single post-hoc recalibration step (Platt or isotonic) eliminates the damage, reducing ECE by up to 66% at a negligible ranking-power cost (AUC -0.002, Cliff's delta = -0.07); and (4) the analytic prior-shift correction that repairs undersampling does not transfer to SMOTE, because SMOTE distorts the class-conditional density rather than only the prior -- so data-driven recalibration remains necessary. We recommend that imbalanced-learning studies report calibration alongside discrimination, and that practitioners recalibrate after resampling whenever predicted probabilities drive decisions.

---


### 268. [Redefining Maritime Anomaly Detection via Equation-Grounded Synthetic Anomalies](https://arxiv.org/abs/2606.29721)

**<font color=#1a73e8>作者：</font>** Youngseok Hwang, Sungho Bae, Dohun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maritime anomaly detection is essential for ensuring maritime safety, security, and efficient traffic management at sea, with Automatic Identification System (AIS) data serving as a primary data source. Despite its importance, most publicly available AIS datasets lack predefined anomaly labels, forcing prior studies to rely on either distribution-based rarity or domain rule/expert-assisted labeling. These approaches, however, face fundamental limitations: statistical rarity often fails to reflect practically critical events, while expert-based labeling is costly, subjective, and difficult to scale. Moreover, both paradigms tend to overlook interaction-driven hazards such as near-miss approaches between vessels. To address these challenges, we propose an equation-grounded anomaly taxonomy that is implementable under a limited AIS observation schema and extensible to other AIS datasets. Specifically, the taxonomy defines three anomaly types: unexpected AIS activity (A1), route deviation (A2), and close approach (A3), covering both single-vessel and inter-vessel anomalies. Building on this taxonomy, we introduce a unified score-synthesize-label pipeline that produces LLM-guided plausibility scores, uses them to synthesize anomalies, and assigns timestamp-level labels. To rigorously assess detection performance, we further design benchmark evaluation settings that account for variations in temporal-window length and anomaly-type composition, and evaluate a broad range of time-series models and anomaly detection models. Together, these contributions provide a systematic basis for evaluating maritime anomaly detection methods across different anomaly types. Our code is available at this https URL.

---


### 269. [ScaleAware-JEPA: Latent Representation for Discovery in Multiscale Physical Fields](https://arxiv.org/abs/2606.29723)

**<font color=#1a73e8>作者：</font>** Guang-Xing Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous physical fields represent a large fraction of data under scientific investigation. Their multiscale structures are central to discovery, yet useful coordinates are not known in advance. Standard self-supervised methods define context and targets in fixed image coordinates, posing a predictive task misaligned with fields organized across a continuous scale hierarchy. We introduce ScaleAware-JEPA, a framework that constructs dense, label-free latent coordinates for continuous scalar fields. Constrained Diffusion Decomposition (CDD) separates each field into pixel-registered scale components and provides the scale coordinates that define the masking geometry. The resulting JEPA objective predicts hidden structure with a context footprint tied to the diffusion scale of each component rather than to an arbitrary patch size. Across MHD turbulence, interstellar molecular gas and urban nighttime-light structure, the learned geometry maps back to coherent morphology, forming dense structural atlases without labels or predefined segmentation rules. By tying latent prediction to the scale hierarchy of a field, ScaleAware-JEPA constructs latent coordinates through which complex physical patterns can be inspected before their relevant structures have been prescribed. Code is available at this https URL.

---


### 270. [Simplifying Flow Matching Transformations with Low-Rank Mixture Models](https://arxiv.org/abs/2606.29724)

**<font color=#1a73e8>作者：</font>** Liam A. Kruse, Houjun Liu, Alexandros E. Tzikas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normalizing flows are powerful generative models that learn an invertible mapping between complex data distributions and simple latent distributions, typically a standard normal density. However, this choice of latent density can impose unnecessary complexity on the learned flow transformation due to the topological mismatch between the latent and data densities, leading to slower training and suboptimal performance. In this work, we propose using mixtures of probabilistic principal component analyzers (MPPCA) as the latent density for normalizing flows. We simplify the learned flow transformation by learning a latent distribution that more closely aligns with the data distribution in terms of KL divergence, thus enabling faster convergence and improved generative performance. Critically, MPPCA models can be fit quickly and cheaply using the expectation-maximization algorithm, making them a practical choice for initializing latent distributions even in high-dimensional generative tasks. We validate our method on both tabular and image datasets, demonstrating consistent gains in training efficiency and generation quality compared to baselines.

---


### 271. [From Trait to Behavior: A Cognitive-Affective Personality System (CAPS) Perspective on Multi-Homing Intention in AIGC Platforms](https://arxiv.org/abs/2606.29726)

**<font color=#1a73e8>作者：</font>** Xuchao Zhang, Jihye Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rapid development of Artificial Intelligence Generated Content (AIGC) platforms, users increasingly show cross-platform usage intentions. Existing research focuses on adoption and usage intentions in single-platform AIGC contexts. A theoretical gap still exists in studies on cross-platform usage. This paper constructs and verifies a three-stage multiple mediation model based on the personality trait-perception-behavioral response framework. The model integrates the optimum stimulation level (OSL) theory, complementarity theory, and perceived value theory, and it sets social influence and use experience as control variables to examine users' multi-homing intention. The results show that: (a) OSL significantly enhances users' perceived complementarity; (b) perceived complementarity positively affects perceived epistemic value; (c) perceived epistemic value significantly and positively predicts multi-homing intention; (d) OSL influences multi-homing intention through a chain mediation path of perceived complementarity and perceived epistemic value; and (e) social influence has a significant positive effect on multi-homing intention, while the effect of use experience is not significant.

---


### 272. [Fast Numbers, Slow Language: Bridging Quantitative and Qualitative Earnings Signals](https://arxiv.org/abs/2606.29734)

**<font color=#1a73e8>作者：</font>** Ding Yu, Zhuo Liu, Hao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Earnings announcements release two types of information sequentially: quantitative surprise (numeric earnings-per-share (EPS)/revenue versus analyst estimate) arrives first in press releases and financial news, processed by algorithmic traders within minutes; qualitative language (management tone, guidance, question-and-answer (Q&A) credibility) arrives 30-90 min later in the earnings conference call transcript (ECT), requiring human interpretation overnight. Financial economists have studied quantitative surprise for 50 years; natural language processing (NLP) researchers have studied qualitative ECT signals for a decade. Despite studying the same event, the two communities used incompatible frameworks: different targets (return vs. volatility), trading setups (long top-decile and short bottom-decile vs. trade-all), and metrics (return spread between top and bottom 20% (Q5-Q1) vs. mean squared error (MSE)), making direct comparison and connection challenging.
We bridge these communities with EarningsInOne, the first corpus aligning earnings news, ECTs, and intraday and next-day prices across SP 1500 (broad U.S. equity universe, 2022-2025). Applying unified trading and evaluation tools to both signal types, we confirm a clean speed separation, fast numbers, slow language: quantitative surprise peaks at announcement and is largely eliminated by the next market open; qualitative ECT sentiment peaks on the next trading day, real and tradeable, but hidden under prior transcript-based evaluation that optimised sign-agnostic volatility with pointwise MSE.

---


### 273. [HTC-SGA Former: A Hybrid Transformer-CNN Network with Self-Guided Attention and a New Boundary-Weighted Adaptive Loss for Coronary DSA Vessel Segmentation](https://arxiv.org/abs/2606.29744)

**<font color=#1a73e8>作者：</font>** Rayan Merghani Ahmed, Marwa Omer Mohammed Omer, Mohamed Elmanna 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate coronary Digital Subtraction Angiography (DSA) vessel segmentation is essential for computer-aided diagnosis and treatment planning of coronary artery disease (CAD). However, thin low-contrast vessels, background interference, and severe vessel-background class imbalance make reliable segmentation of weak distal branches and vessel boundaries challenging. Existing methods struggle to balance global contextual reasoning with preservation of weak vessels, vessel continuity, and fine boundaries. To address these limitations, we propose HTC-SGA Former, a lightweight hybrid Transformer-CNN framework for coronary DSA vessel segmentation. It employs a CNN encoder for local vessel morphology extraction and a Transformer decoder for contextual feature modeling. A Multi-Scale Global-Local Window Attention (MS-GLWA) block performs efficient global-local contextual modeling, while a Self-Guided Feature Attention (SGFA) module enhances weak-vessel responses. In addition, a Boundary-Weighted Adaptive Compound Loss (BWACL) emphasizes thin-vessel boundaries and adaptively balances vessel recovery and boundary refinement. Experiments on private right and left coronary artery DSA subsets show that HTC-SGA Former outperforms 14 state-of-the-art segmentation methods while maintaining a compact architecture with only 0.81M parameters. BWACL also improves performance over binary cross-entropy and Dice losses across four encoder-decoder architectures, demonstrating strong cross-backbone applicability. HTC-SGA Former improves thin-vessel recovery, vessel continuity, and boundary localization through complementary global-local contextual modeling, vessel-focused refinement, and adaptive optimization, supporting reliable and computationally efficient coronary vessel analysis for future computer-assisted cardiovascular interventions.

---


### 274. [ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit](https://arxiv.org/abs/2606.29745)

**<font color=#1a73e8>作者：</font>** Abhijnan Nath, Nikhil Krishnaswamy  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> What does it mean for a language agent to be adaptive? Effective multi-turn agents must decide what information to seek, how to use new evidence, and when they are certain enough to act. We introduce Epistemic Decision Processes (EDPs), a belief-state formulation of multi-turn information seeking in which actions produce external observations that update the agent's posterior over a latent task variable. EDPs make epistemic adaptivity explicit: good policies choose actions that are useful under the current belief, not merely those that correlate with eventual success. We prove that belief-agnostic policies can suffer errors that compound exponentially over the horizon, and that aggregate trajectory returns can fail to identify the per-turn Bayesian advantage needed for epistemic credit. We then introduce ECHO (Epistemic Credit for History-Conditioned Optimization), a practical clipped policy-gradient objective that assigns turn-level credit using posterior-sensitive rewards. In the Clue Selector Game, a novel controlled evidence-seeking benchmark, we show that ECHO substantially improves resolution, information gain, and efficiency over trajectory-level GRPO, and matches or exceeds frontier baselines on epistemic metrics such as grounding, recovery, and calibration while producing almost no visible reasoning text.

---


### 275. [Rethinking Generative Reconstruction Attacks against Graph Neural Network Models](https://arxiv.org/abs/2606.29748)

**<font color=#1a73e8>作者：</font>** Adebayo Keji, Sayanton Dibbo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The application of graph data in numerous disciplines raises the need for gathering and analyzing huge volumes of data, some of which is private and sensitive. The non-Euclidean nature of the graph data makes the analysis computationally challenging, leading to the use of Graph Neural Networks (GNNs) in the age of AI. GNNs may inadvertently leak sensitive data they are trained on, which raises serious data security issues, including the model inversion attack. In this study, we analyze GNNs' vulnerabilities by introducing two novel graph inversion (i.e., reconstruction) attacks: graph-label conditioned (GLC) attack and embedding-label conditioned (ELC) attack, utilizing targetmodel predictions and their intermediate representations, respectively. We perform a comprehensive analysis of our introduced privacy attacks and compare them with existing baselines across three benchmark graph datasets (i.e., NCI1, PROTEINS, and AIDS) and four graph distributional/structural metrics (i.e., FGD, EGD, MMD, and GKS). Our work demonstrates that an adversary can use the generator-discriminator technique to reconstruct high-quality graphs in real-world black-box attack scenarios against GNNs. Additionally, we present a variant of our attacks (Ours--) with 50% reduced queries, achieving good or comparable reconstruction attack performance. In addition, we show that GNNs are highly vulnerable to privacy attacks, varying Laplacian noise-scales.

---


### 276. [LEIQ-Assessor: Multi-dimensional Quality Assessment of Low-light Enhanced Images via Multi-task Learning](https://arxiv.org/abs/2606.29752)

**<font color=#1a73e8>作者：</font>** Wei Sun, Yanwei Jiang, Dandan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement algorithms (LIEAs) aim to improve the visibility of images captured under poor illumination. However, the enhancement process often introduces artifacts such as noise amplification, color shift, structural damage, and over-exposure, which degrade the perceptual quality of the enhanced images. Therefore, a reliable image quality assessment (IQA) metric for evaluating enhancement effects is of great importance for both the development of LIEAs and their practical applications. In this paper, we present \textbf{LEIQ-Assessor}, a multi-dimensional quality assessment model for low-light image enhancement based on multi-task learning, developed for the QoMEX 2026 Grand Challenge on Low-light Enhanced Image Quality Assessment. Specifically, our method leverages a pre-trained SigLIP2 Vision Transformer as the backbone and simultaneously predicts the overall Mean Opinion Score (MOS) together with six perceptual sub-attributes: lightness, color fidelity, noise level, exposure quality, naturalness, and content recovery. By jointly optimizing these correlated objectives via the PLCC loss, the shared representation captures richer quality-aware features than its single-task counterpart. Experiments on the MLE benchmark demonstrate that LEIQ-Assessor significantly outperforms existing no-reference IQA models and hand-crafted quality descriptors. Our method achieved second place in the QoMEX 2026 Grand Challenge on Low-light Enhanced Image Quality Assessment. The code is available at this https URL.

---


### 277. [GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures](https://arxiv.org/abs/2606.29759)

**<font color=#1a73e8>作者：</font>** Shixi Qin, Zhiyong Yang, Shilong Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper tackles the challenging problem of developing a proactive copyright protection mechanism that cuts off unauthorized use of diffusion bridge models. Existing studies largely fall into post-hoc attribution (e.g., watermarking and fingerprinting) or degradation-only defenses, which offer only indirect and limited preventive effects. We therefore propose GoodDiffusion, inspired by backdoor mechanisms, to enforce model-level use-time control by internalizing authorization into the generative process through a selectively permissive, otherwise closed behavior. Specifically, GoodDiffusion preserves high-quality generation for authorized queries carrying valid signatures, yet refuses to generate for unauthorized inputs. We further theoretically show that naive static-signature designs (like conventional backdoor injection) are fundamentally fragile, since a surrogate signature can be efficiently recovered via gradient-based optimization. To strengthen security, we introduce a Learnable Signature Network (LSN) that assigns sample-specific signatures conditioned on each input. This breaks the universality of signatures and prevents a surrogate from transferring across inputs. Extensive experiments validate that GoodDiffusion effectively blocks unauthorized use while maintaining strong generation quality for authorized users.

---


### 278. [MR-IQA: A Unified Margin View of Regression and Ranking for Blind Image Quality Assessment](https://arxiv.org/abs/2606.29760)

**<font color=#1a73e8>作者：</font>** Yuan Li, Youyuan Lin, Zitang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image quality assessment (BIQA) is commonly built on two basic learning paradigms: regression and ranking. Regression calibrates absolute scores, whereas ranking recovers quality structure from ordinal relations. Although joint regression-ranking supervision often improves BIQA, the relation between the two paradigms remains largely empirical and underexplored. In this work, we revisit what underlies regression and ranking and identify pairwise relational distance, termed quality margin, as their common bridge. Our derivation shows that, at the objective-optimization level, both paradigms fit quality margins: regression fits margins induced by score endpoints, while ranking fits transformed or sign-level margins through preference probabilities. Motivated by this insight, we propose MR-IQA, a direct quality-margin optimization framework for reinforcement learning (RL)-based BIQA. MR-IQA samples quality scores and optimizes pairwise margin errors as policy rewards, thereby modeling quality structure more explicitly. Experiments on six BIQA benchmarks show competitive general performance, and controlled comparisons demonstrate that MR-IQA achieves the strongest average PLCC/SRCC over regression- or ranking-based RL methods. Our findings provide a new insight into unifying regression and ranking, offering a theoretical basis for understanding quality-structure modeling in BIQA and beyond.

---


### 279. [UrbanCDNet: Appearance-Robust and Boundary-Aware Bitemporal Change Detection for Korean Urban Building Monitoring](https://arxiv.org/abs/2606.29781)

**<font color=#1a73e8>作者：</font>** Abdirashid Omar, Jonghyuk Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban building change detection from bi-temporal aerial imagery is important for redevelopment monitoring, infrastructure management, and unauthorized-construction screening, but Korean urban scenes remain difficult because changed regions are often sparse, appearance varies strongly between acquisition dates, and useful outputs must follow building footprints rather than coarse blobs. This paper presents UrbanCDNet, a task specific Siamese CNN that combines appearance-robust multi-cue comparison, alignment-aware middle-scale differencing, lightweight context refinement, scene calibration, and auxiliary boundary supervision. Experiments use a corrected AIHub-based Korean benchmark with 3,998 training, 503 validation, and 499 test pairs, and report changed-class precision, recall, F1, and IoU. On the locked test split, UrbanCDNet achieves 0.7335 precision, 0.7696 recall, 0.7511 F1, and 0.6014 IoU, outperforming a strong Siamese U-Net baseline (0.7108 F1, 0.5514 IoU) and the strongest external competitor, ChangeFormer-MIT-B0 (0.7107 F1, 0.5512 IoU). Additional diagnostic slicing shows that the gain is concentrated in the operating regimes that motivated the design: on the sparse-change subset with less than 5% changed area, F1 improves from 0.4765 to 0.6175, and on the high photometric-gap subset it improves from 0.6349 to 0.7285. Boundary F1 at 3-pixel tolerance rises from 0.3445 to 0.4447, while object F1 at IoU 0.3 rises from 0.0690 to 0.2258. These results indicate that, on this Korean benchmark, task-shaped temporal comparison and boundary-aware supervision matter more than generic model scale alone

---


### 280. [OP3DSG: Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Environments](https://arxiv.org/abs/2606.29786)

**<font color=#1a73e8>作者：</font>** Yirum Kim, Ue-Hwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graphs (3DSGs) provide a compact and structured abstraction of 3D environments. Although advances in foundation models have enabled open-vocabulary 3DSG generation, existing approaches remain object-centric and encode limited relational information -- restricting their applicability in real-world scenarios that require fine-grained understanding. We propose OP3DSG, an open-vocabulary part-aware 3DSG generation framework that constructs unified graphs that jointly model objects, interactive parts, spatial relations, functional relations, and affordances. OP3DSG integrates object-part knowledge-guided detection with part-aware 3D fusion to preserve small and interaction-relevant components, and employs a geometry-initialized prior graph with LLM-based refinement to reduce spurious relational predictions while enabling efficient graph construction. To systematically evaluate unified 3D scene graph construction, we introduce UniGraph3D, a benchmark designed for part-aware perception and multi-level relational reasoning. Experimental results show that OP3DSG achieves state-of-the-art performance and demonstrates its effectiveness as a perception backbone in diverse real-world robotics tasks.

---


### 281. [What Drives the Inlier-Memorization Effect? A Theory of Outlier Detection via Early Training Dynamics](https://arxiv.org/abs/2606.29791)

**<font color=#1a73e8>作者：</font>** Kunwoong Kim, Dongha Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outlier detection (OD) aims to identify anomalous instances by learning the underlying structure of normal data (inliers), and is particularly challenging in fully unsupervised settings where no information about anomalies is available during training. Recent advances have leveraged the inlier-memorization (IM) effect, a phenomenon in which deep models memorize inlier patterns earlier than those of outliers, as a powerful signal for distinguishing outliers. However, despite its empirical success, the theoretical understanding of the IM effect remains limited. In this work, we present a theoretical study of the IM effect. Focusing on a simple autoencoder, we show that, under mild assumptions, the model can successfully memorize inliers while failing to memorize outliers during certain stages of early training. In particular, we characterize not only the emergence of the IM effect, but also its strength and persistence, and analyze how these properties depend on the data distribution and parameter initialization. In addition, building on these insights, we derive simple yet practical guidelines for enhancing the IM effect, including data preprocessing and parameter initialization schemes, achieving state-of-the-art performance on the ADBench datasets. Our findings provide a theoretical foundation for the IM effect and offer actionable directions for improving IM-based outlier detection methods.

---


### 282. [Fund2Persona: A Framework for Building and Refining Financial Advisor Personas from Fund Disclosure Data](https://arxiv.org/abs/2606.29793)

**<font color=#1a73e8>作者：</font>** Suhwan Park, Hoyoung Lee, Zhangyang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Demand for personalized financial advising is growing, but consistent advisor expertise is difficult to obtain, scale, and encode in LLM systems. Simple persona prompts rarely specify how a financial advisor should reason and often drift toward generic recommendations. We propose Fund2Persona, a framework that grounds financial-advisor personas in fund disclosures, holdings transitions, market context, and manager commentary, then refines them through an agentic actor--scorer--patcher loop. We evaluate the resulting personas on held-out holdings-transition reconstruction and manager-commentary alignment, where they better recover portfolio decisions and grounded manager interpretation than generic baselines. We further study two downstream diagnostics: market-scenario generation, where persona retrieval broadens plausible investment views beyond repeated generic rollouts, and advisory dialogues grounded in investor profiles, where matched personas give more specific and useful advice than a generic advisor. These results suggest that fund-data-grounded financial-advisor personas can make manager-specific investment expertise portable rather than merely changing an LLM's surface style.

---


### 283. [UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras](https://arxiv.org/abs/2606.29794)

**<font color=#1a73e8>作者：</font>** Yipeng Zhu, Huajian Huang, Tristan Braud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D Gaussian Splatting (3DGS) frameworks rely on camera-specific rasterization, suffering from inconsistent solid-angle sampling and degraded performance across heterogeneous camera models (e.g., perspective, fisheye, omnidirectional). To address this limitation, we propose UniTriSplat, a unified 3DGS framework for universal cameras that reformulates Gaussian splatting on the unit sphere via HEALPix discretization. Leveraging the equal-area property of HEALPix, we construct a spherical sampling grid aligned with the angular resolution of input images. We derive the forward rendering and gradient propagation of Gaussians directly in the spherical radian domain, yielding uniform optimization behavior from narrow-FoV images to full 360-degree panoramas. To enhance perceptual reconstruction quality, we additionally introduce a HEALPix-aware SSIM loss that respects spherical neighborhood structure. Extensive experiments across diverse camera models demonstrate that UniTriSplat consistently improves cross-camera generalization while preserving geometric fidelity and rendering quality.

---


### 284. [Multi-Level Distributional Entropy for Explainable Network Intrusion Detection](https://arxiv.org/abs/2606.29797)

**<font color=#1a73e8>作者：</font>** Mohamed Aly Bouke, Md Shohel Sayeed, Swee-Huay Heng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning network intrusion detection systems (IDS) rely on aggregate flow statistics that discard distributional structure, while established entropy measures require raw packet sequences unavailable in pre-aggregated flow datasets. We propose Multi-Level Distributional Entropy (MDE), an analytical framework that derives interpretable entropy features directly from flow-level summary statistics at three levels: within-flow Gaussian differential entropy, cross-directional Jensen-Shannon divergence (JSD), and Transmission Control Protocol (TCP) flag-pattern Shannon entropy, without raw packet access or training data. Across four benchmarks (NSL-KDD, CICIDS-2017, CICIDS-2018, UNSW-NB15) under a leakage-free fold-local pipeline, entropy-only features achieve weighted F1 of 0.708-0.989, matching conventional features without degrading performance. Full operational metric reporting then exposes failure modes that aggregate F1 conceals. On CICIDS-2018, F1=0.74 hides a detection rate (DR) of 0.48, and on held-out attack families F1 exceeds 0.998 while DR falls to zero. Under temporal shift, a pseudo-live replay of 703K flows reveals a threshold-ranking divergence in which score ranking is preserved (AUC=0.87) but fixed thresholds collapse (DR=0.082) and recalibration offers no recovery. SHapley Additive exPlanations (SHAP) fold-stability analysis (Spearman rho=0.80-0.95) confirms that entropy attributions are reproducible and domain-coherent across heterogeneous environments.

---


### 285. [Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling](https://arxiv.org/abs/2606.29801)

**<font color=#1a73e8>作者：</font>** Yoonseok Choi, Chaeyoung Oh, Hyunjun Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models remain vulnerable to adversarial prompts that elicit disallowed content, motivating reliable inference-time controls. A popular approach is negative guidance, which subtracts a negative prompt direction with a fixed weight. However, it often forces a safety-fidelity trade-off, causing artifacts or prompt drift when over-applied and failing under attacks when under-applied. Dynamic variants reweight guidance using posterior-odds signals, which can be brittle for open-vocabulary compositional prompts, while lightweight similarity-based methods ignore the evolving image evidence along the denoising trajectory. We introduce Concept Removal Guidance (CRG), a training-free method that estimates unwanted-concept presence at each diffusion step from the model's noise predictions, and adaptively calibrates negative guidance via a closed-form constrained update enforcing a target presence threshold while minimally perturbing the conditional trajectory. Across red-teaming benchmarks, CRG reduces attack success rates while preserving benign fidelity, and extends to additional suppression targets such as artist style and violence without fine-tuning or external classifiers.

---


### 286. [Accelerating Q-learning through Efficient Value-Sharing across Actions](https://arxiv.org/abs/2606.29806)

**<font color=#1a73e8>作者：</font>** Prabhat Nagarajan, Brett Daley, Martha White 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Action-values are foundational to many control algorithms such as Q-learning. Therefore learning action-values efficiently is central to reinforcement learning (RL). However, learning them can be slow, requiring many updates to move values from their initialization, typically near zero, to their true values, which may be far from zero. Moreover, action-value learning algorithms typically update each state-action pair independently, without learning shared value structure across actions within a state. In this paper, we address these inefficiencies by introducing the mean-expansion layer, which accelerates action-value learning by sharing values across actions within a state and by changing the problem from directly learning potentially large action-values to learning a lower-norm representation of them. In deep RL, this layer can be applied as a parameter-free addition to Q-network architectures without altering the underlying algorithm. Applied to deep Q-networks and implicit quantile networks, it improves aggregate performance across 57 Atari games while increasing action gaps and dramatically reducing value overestimation.

---


### 287. [Rethinking Forgery Attacks on Semantic Watermarks in Black-Box Settings: A Geometric Distortion Perspective](https://arxiv.org/abs/2606.29807)

**<font color=#1a73e8>作者：</font>** Cheng-Yi Lee, Yichi Zhang, Yuchen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that semantic watermarks, which embed information into the initial noise of latent diffusion models (LDMs), are vulnerable to black-box forgery attacks. However, existing methods primarily rely on empirical evidence and lack a rigorous theoretical understanding of the conditions under which such attacks succeed or fail. To bridge this gap, we rethink the nature of such attacks through the lens of rate-distortion in the latent space. Our analysis identifies an irreducible distortion floor due to structural mismatches between proxy and target models, which fundamentally limits the fidelity of forged watermarks. We further characterize this distortion as structured geometric deviations on the latent manifold, in the form of global drift and local deformation rather than stochastic noise. Leveraging these insights, we propose a scheme-agnostic detection method that distinguishes forged samples before watermark verification. Extensive experiments demonstrate the effectiveness of our method across diverse black-box scenarios, while preserving robustness to common distortions.

---


### 288. [How Far Can You Get Without a GPU? A Systematic Benchmark of Lightweight Hallucination Detection Across Question Answering, Dialogue, and Summarisation](https://arxiv.org/abs/2606.29809)

**<font color=#1a73e8>作者：</font>** Kriti Faujdar, Smit Kadvani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination detection has become a pressing requirement for trustworthy AI deployment at scale. The most accurate detection methods depend on GPU-intensive inference, proprietary API calls, or white-box access to the generating model. This puts them out of reach for resource-constrained researchers and practitioners. In this paper, we explore a practical alternative: how well can hallucination detection perform using only lightweight, CPU-feasible methods built on publicly available models? We systematically benchmark five such methods: ROUGE-L, semantic similarity, BERTScore, a Natural Language Inference (NLI) detector based on a FEVER-trained DeBERTa model, and a score-level ensemble of similarity and NLI. We evaluate them across all three tasks of the HaluEval benchmark: question answering (QA), dialogue, and summarisation. We calibrate each method on a held-out validation split and evaluate it on 2,000 test instances per task. We find that no single method dominates and performance is highly task-dependent. The ensemble performs best on QA (F1 = 0.792, AUC-ROC = 0.873), the NLI detector leads on dialogue (AUC-ROC = 0.713), and all five methods degrade to near-random performance on summarisation (AUC-ROC between 0.469 and 0.574). This task-dependence and the systematic failure on summarisation map the practical frontier of GPU-free hallucination detection. They give practical guidance for method selection under computational constraints. All experiments run on a standard laptop CPU using public models.

---


### 289. [Nemotron-Labs-Diffusion-Image: Advancing Masked Discrete Diffusion for High-Resolution Image Synthesis](https://arxiv.org/abs/2606.29814)

**<font color=#1a73e8>作者：</font>** Shufan Li, Greg Heinrich, Hanrong Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Nemotron-Labs-Diffusion-Image, a state-of-the-art masked discrete diffusion model (MDM) for high-resolution text-to-image synthesis. Compared with prior work on masked image generation, Nemotron-Labs-Diffusion-Image addresses two key challenges. First, unlike continuous diffusion models which progressively refine latent representations across the entire image, standard MDMs lack self-correcting capability because discrete tokens cannot be modified once they are unmasked. Second, although increasing the vocabulary size of discrete image tokenizers improves reconstruction fidelity, it introduces optimization difficulties for generative modeling as the per-token training signal becomes increasingly sparse. To address the first challenge, Nemotron-Labs-Diffusion-Image incorporates a token-editing mechanism that enables the model to dynamically revise already-unmasked tokens during inference, similar to how a sculptor iteratively refines their work. To tackle the second challenge, we propose a Grouped Cross-Entropy (GCE) objective that assigns positive learning signals to tokens neighboring the ground truth in embedding space, thereby alleviating signal sparsity. To further improve training efficiency, we implement a custom fused operator for GCE that significantly reduces VRAM usage in large-vocabulary settings. Experimental results demonstrate that these innovations substantially improve both training efficiency and image fidelity of masked discrete image generators, achieving a score of 0.90 on GenEval, 86.9 on DPG and 10.76 of HPSv3.

---


### 290. [Dual-Flow Reinforcement Learning with State-Aware Exploration](https://arxiv.org/abs/2606.29820)

**<font color=#1a73e8>作者：</font>** Qijun Li, Zheng Fu, Qi Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In complex continuous-control reinforcement learning tasks, multimodal optimal actions often coincide with uncertain, multimodal return distributions, making reliable value estimation and multimodal exploration challenging. Existing value estimation methods using unimodal Gaussians restrict expressiveness and yield biased estimates. Recent generative policies can represent multimodal actions but often collapse to a few modes and under-explore high-value areas of the action space. Motivated by these challenges, we propose Dual-Flow RL, a unified actor-critic framework that jointly models a continuous return distribution and a multimodal policy distribution using conditional flow matching (CFM). This design supports reliable value estimation and sustained multimodal exploration. To further enhance exploration, we introduce an Entropy-Covariance Exploration Regulator (ECER) that enables state-aware exploration regulation leveraging policy entropy and action-uncertainty covariance. Experiments on DeepMind Control Suite and Humanoid-Bench show that Dual-Flow RL achieves state-of-the-art performance on most tasks, significantly outperforming prior diffusion-based and flow-based methods.

---


### 291. [Learning Cross-view Correspondences for Geo-localization on Planetary Surfaces](https://arxiv.org/abs/2606.29821)

**<font color=#1a73e8>作者：</font>** Hong Minh Nguyen, Marcus Märtens, Tat-Jun Chin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining global position awareness is a fundamental challenge for planetary surface exploration, since satellite-based positioning systems are unavailable and onboard odometry drifts over time. Although orbital mapping products, such as overhead imagery and terrain-derived maps, provide global context, aligning them with surface observations is challenging due to large viewpoint differences, low texture, repetitive terrain, and drastic changes in appearance caused by varying illumination and topography. We introduce a new cross-view geo-localization benchmark built from physically rendered surface panoramas and overhead tiles derived from a high-resolution lunar terrain model. Our dataset contains 10438 ground views rendered as 360$^\circ$ surface panoramas with matching overhead images precisely centered at the same location. Additionally, a set of overlapping tiles is provided to study off-center localization with multiple plausible candidates per panorama. We study the performance of a state-of-the-art transformer-based geo-localization method on our data, by training it from scratch and reporting retrieval accuracy. Our results demonstrate that learning-based cross-view localization methods can be successfully applied to the domain of planetary surfaces, providing a vision-based alternative to global navigation satellite systems.

---


### 292. [Rethinking Collaborative Trust for Verifiably Decentralized Blockchain Systems](https://arxiv.org/abs/2606.29826)

**<font color=#1a73e8>作者：</font>** Yunqi Zhang, Shaileshh Bojja Venkatakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the promise of decentralization, measurement studies have identified a conspicuous lack of decentralization in blockchains. Centralization has been observed in almost all layers of the blockchain, in decentralized applications, and in decentralized autonomous organizations. In many cases, it is practically impossible to definitively determine the extent of centralization in the system. While multiple works have proposed methods to decrease centralization, by and large blockchains continue to be significantly centralized.
In this paper, we develop a general framework for building verifiably decentralized blockchain systems. Our framework is motivated by the core observation that the richness and diversity of collaborative interactions between users -- rather than resource uniformity -- captures the essence and extent of decentralization in a blockchain system. Existing blockchains do not have any incentive mechanisms to encourage inter-coalition collaboration, which directly contributes to centralization. We propose a novel reward design that incentivizes users to collaborate with other users without forming isolated coalitions. Technically, our method uses a Sybil-resistant asymmetric Shapley value for reward attribution within a collaboration group, and the theory of expander graphs for measuring and enforcing decentralization.
Our framework is general and can be adapted to alleviate centralization in any layer, application, or decentralized organization. It also has important implications beyond the topic of centralization. For example, we show that our solution can naturally address the blockchain scalability problem. We also identify a new class of decentralized collaborative applications that have hitherto been unexplored in blockchains.

---


### 293. [HomeDiffusion: Zero-Shot Object Customization with Multi-View Representation Learning for Indoor Scenes](https://arxiv.org/abs/2606.29828)

**<font color=#1a73e8>作者：</font>** Guoqiu Li, Jin Song, Yiyun Fei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, zero-shot object customization generation methods have rapidly developed and shown tremendous potential for applications. For instance, in the e-commerce domain, consumers can observe the visual effect of furniture placed within their personal living spaces or clothes worn on their own bodies. Many existing approaches perform object customization generation based on diffusion models and extracted reference object features. However, the generated object significantly diverges from the original reference object in details such as patterns and curves. Particularly for asymmetrical reference objects, the absence of comprehensive multi-viewpoint information prevents the generation of object poses that harmonize with the background scene. To address these shortcomings, we have constructed a novel dataset comprising multi-angle images of furniture and indoor scenes. Based on diffusion models, we introduce HomeDiffusion, which can leverage multi-viewpoint images of the same reference object to accurately generate visually harmonious object poses within specified areas of the background scene. During the diffusion process, we further extract high-fidelity details of the reference object and perform cross-attention with the noise latents in the latent space, thereby ensuring the preservation of details in the customized object generation. Extensive qualitative and quantitative experiments demonstrate that our method achieves superior performance over other existing zero-shot as well as few-shot object customization approaches.

---


### 294. [The Forgetting-Retention Dilemma: Certified Unlearning Theory in Continual Learning](https://arxiv.org/abs/2606.29832)

**<font color=#1a73e8>作者：</font>** Yiting Hu, Lingjie Duan, Qian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to eliminate the influence of specific data from trained models to safeguard privacy. However, this presents a significant challenge in the context of continual learning (CL), where models update sequentially on dynamic datasets. A major limitation is that current certified unlearning algorithms fail to account for the complex, cumulative model evolution inherent to CL framework. In this work, we establish the first theoretical foundation bridging CL and machine unlearning. We formulate the CL's unlearning objective as the minimization of post-unlearning excess risk, which decomposes into CL excess risk and unlearning loss, characterizing the fundamental trade-off between preserving historical knowledge and targeted forgetting. Under mild assumptions, we first establish an upper bound for the CL excess risk in non-convex models. We then adapt two certified unlearning approaches, gradient-based and Hessian-based, to the CL framework. Our analysis reveals that while the gradient-based approach is less effective than the Hessian-based method in minimizing unlearning loss, it offers the distinct advantage of nearly zero storage overhead for enabling unlearning. This insight motivates a hybrid strategy that reduces storage costs while maintaining post-unlearning performance. Experimental results further validate our theoretical findings.

---


### 295. [A Sieve-Accelerated Quadrature Method for Exact Privacy Accounting in the 2020 U.S. Decennial Census](https://arxiv.org/abs/2606.29835)

**<font color=#1a73e8>作者：</font>** Buxin Su, Weijie Su, Chendi Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2020, the U.S. Census Bureau adopted differential privacy for the Decennial Census by injecting integer-valued Gaussian noise into published census tabulations. Exactly evaluating the privacy guarantees of these data releases would enable the Bureau to determine the absolute minimum noise required to satisfy a given privacy budget, preventing the injection of unnecessary excess noise and thereby substantially enhancing the statistical utility of the data for downstream applications such as federal funding allocation and political redistricting. In this paper, we introduce a computationally efficient and mathematically rigorous quadrature method to evaluate the exact privacy profile of practical, large-scale census releases under the composition of heterogeneous discrete Gaussian mechanisms. Mathematically, this problem reduces to evaluating the tail probabilities of high-dimensional convolutions of integer-valued random variables sampled from heterogeneous discrete Gaussian distributions under exceptionally stringent numerical error tolerances (e.g., $10^{-35}$). By recasting the exact privacy accounting as a numerical integration problem via the discrete Fourier transform, we explicitly exploit the exponential convergence of the trapezoidal rule for complex analytic, periodic characteristic functions. Furthermore, to overcome the computational bottleneck of evaluating highly oscillatory integrands in high dimensions, we develop a sieve algorithm that identifies and prunes negligible quadrature nodes, accelerating the computation by three orders of magnitude. Taken together, these numerical innovations enable the first exact, assumption-free privacy accounting for the 2020 Census Demographic and Housing Characteristics File, achieving a 1,824-fold speedup over prior methods while maintaining census-mandated error tolerances.

---


### 296. [Revealing the Technology Development of Natural Language Processing: A Scientific Entity-Centric Perspective](https://arxiv.org/abs/2606.29836)

**<font color=#1a73e8>作者：</font>** Heng Zhang, Chengzhi Zhang, Yuzhuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most studies on technology development have been conducted from a thematic perspective, but the topics are coarse-grained and insufficient to accurately represent technology. The development of automatic entity recognition techniques makes it possible to extract technology-related entities on a large scale. Thus, we perform a more accurate analysis of technology development from an entity-centric perspective. To begin with, we extract technology-related entities such as methods, datasets, metrics, and tools in articles on Natural Language Processing (NLP), and we apply a semi-automatic approach to normalize the entities. Subsequently, we calculate the z-scores of entities based on their co-occurrence networks to measure their impact. We then analyze the development trends of new technologies in the NLP domain since the beginning of the 21st century. The findings of this paper include three aspects: Firstly, the continued increase in the average number of entities per paper implies a growing burden on researchers to acquire relevant technical background knowledge. However, the emergence of pre-trained language models has injected new vitality into the technological innovation of the NLP domain. Secondly, Methods dominate among the 179 high-impact entities. An analysis of the z-score trend about the top 10 entities reveals that pre-trained language models, exemplified by BERT and Transformer, have become mainstream in recent years. Unlike the trend of the other eight method entities, the impact of Wikipedia dataset and BLEU metric has continued to rise in the long term. Thirdly, in recent years, there has been a remarkable surge in popularity for new high-impact technologies than ever before, and their acceptance by researchers has accelerated at an unprecedented speed. Our study provides a new perspective on analyzing technology development in a specific domain.

---


### 297. [Robust Trajectory Distillation: Hybrid Reweighting Meets Teacher-Inspired Targets](https://arxiv.org/abs/2606.29837)

**<font color=#1a73e8>作者：</font>** Kaifeng Chen, Lechao Cheng, Jiyang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) condenses large corpora into compact, information-rich subsets for efficient training and reuse. However, under noisy supervision, DD risks condensing corrupted associations together with useful signals, degrading robustness. Conventional noisy-label remedies (sample selection, loss weighting, label correction) tightly couple noise estimation with model optimization, often require clean anchors, and can amplify confirmation bias-assumptions that are misaligned with DD's goal of compact, plug-and-play supervision. We therefore propose a trajectory-based DD framework that jointly suppresses noise and preserves transferable knowledge without relabeling or clean subsets. It comprises two complementary components: Selective Guidance Reweighting (SGR), which fuses global forgetting patterns (second-split forgetting) with local neighborhood consistency into a progressive reweighting scheme that prioritizes clean supervision along the teacher trajectory; and Teacher-Inspired Auxiliary Targets (TIAT), which inject auxiliary residual guidance distilled from intermediate teacher dynamics to reinforce informative signals while remaining internally consistent. Together, SGR and TIAT produce distilled datasets with cleaner and richer representations under noisy supervision. The framework is robust, label-preserving, computationally lightweight, and broadly applicable, yielding consistent gains over state-of-the-art DD baselines across symmetric, asymmetric, and real-world noise.

---


### 298. [Theory of Continual Learning Against Data Poisoning Attacks](https://arxiv.org/abs/2606.29841)

**<font color=#1a73e8>作者：</font>** Yiting Hu, Lingjie Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL), where a model is trained on a sequence of data tasks, is increasingly being adopted across key fields such as large language models and image recognition, yet it remains highly vulnerable to data poisoning that triggers learning divergence or severe excess risk. Despite these threats, a principled theoretical foundation in CL for understanding attack and defense remains lacking. In this paper, we develop a theoretical framework to analyze strategic attacks and defenses in regularization-based CL, a cornerstone of recent CL theory. By framing the adversary-defender interaction as an online zero-sum game, we first establish a fundamental performance limit: no defense succeeds when an adversary poisons a linear proportion of tasks by injecting unbounded noise or pattern shifts in regularization-based CL. We then analyze two possibly defensible scenarios: infrequent attacks and bounded noise per attack. For the former regime, we propose a task-to-task verification mechanism to detect data poisoning and reduce cumulative bias for learning convergence. For the latter regime, we derive a robust defense that minimizes the model's sensitivity to poisoned features, provably accelerating the convergence rate. Extensive experiments on realistic tasks further validate our theoretical results.

---


### 299. [MATCH: Modulating Attention via In-Context Retrieval for Long-Context Transformers](https://arxiv.org/abs/2606.29844)

**<font color=#1a73e8>作者：</font>** Linrui Ma, Chun Hei Lo, Xinyu Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The quadratic computational cost of traditional attention mechanisms poses a major bottleneck to the scalability and practical deployment of large language models (LLMs), particularly in long-context scenarios. To improve efficiency, existing approaches often enforce rigid structural constraints such as local attention windows. However, these strategies typically lead to substantial performance degradation on tasks requiring precise long-range recall. In this work, we propose MATCH, a scalable and efficient framework that augments sparsified attention mechanisms with dynamically integrated in-context information through an efficient retrieval system. Empirical results show that MATCH significantly improves the performance of sparse-attention models on both synthetic and real-world natural-language tasks. These findings highlight the versatility of MATCH as a general approach for enhancing in-context retrieval capabilities while maintaining the efficiency benefits of sparse attention architectures.

---


### 300. [Bricker to BRACE: A Bracket Exposure RAW Dataset and Restoration Model for Flicker-Banding](https://arxiv.org/abs/2606.29845)

**<font color=#1a73e8>作者：</font>** Zihan Zhou, Libo Zhu, Jue Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flicker-banding (FB), arises from temporal aliasing between a camera's rolling shutter and a display's brightness modulation, degrading screen-captured image readability with color shifts and jagged patterns. Existing single-frame methods with simplified parametric stripe models cannot reliably distinguish these artifacts from genuine texture. To address this, we conduct a systematic analysis of complex FB morphologies and reveal their significant variation across exposure settings, motivating a multi-frame bracketed RAW restoration paradigm. We construct Bricker, a synthetic-real bracketed RAW dataset built via ray-tracing-based physical simulation and automated multi-exposure capture tool. We further propose BRACE: Bracketed RAW Flicker-Banding Removal, a multi-frame restoration model that utilizes frequency-aware banding prior and a multi-scale spatial cross-attention modulator (MSCAM) for cross-exposure spatial fusion. We also introduce the Stripe Frequency Consistency (SFC) metric to evaluate banding removal. Experiments demonstrate state-of-the-art performance on both synthetic and real benchmarks. Our dataset and code are available at: this https URL.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
