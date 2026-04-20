# 📦 其他研究 | 2026年04月21日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 101. [Multi-objective Reinforcement Learning With Augmented States Requires Rewards After Deployment](https://arxiv.org/abs/2604.15757)

**<font color=#1a73e8>作者：</font>** Peter Vamplew, Cameron Foale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This research note identifies a previously overlooked distinction between multi-objective reinforcement learning (MORL), and more conventional single-objective reinforcement learning (RL). It has previously been noted that the optimal policy for an MORL agent with a non-linear utility function is required to be conditioned on both the current environmental state and on some measure of the previously accrued reward. This is generally implemented by concatenating the observed state of the environment with the discounted sum of previous rewards to create an augmented state. While augmented states have been widely-used in the MORL literature, one implication of their use has not previously been reported -- namely that they require the agent to have continued access to the reward signal (or a proxy thereof) after deployment, even if no further learning is required. This note explains why this is the case, and considers the practical repercussions of this requirement.

---


### 102. [KWBench: Measuring Unprompted Problem Recognition in Knowledge Work](https://arxiv.org/abs/2604.15760)

**<font color=#1a73e8>作者：</font>** Ankit Maloo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the first version of KWBench (Knowledge Work Bench), a benchmark for unprompted problem recognition in large language models: can an LLM identify a professional scenario before attempting to solve it. Existing frontier benchmarks have saturated, and most knowledge-work evaluations to date reduce to extraction or task completion against a specification. KWBench targets the step before that: recognizing the governing structure of the situation from raw inputs alone.
The benchmark contains 223 tasks sourced from practitioners across acquisitions, contract negotiations, clinical pharmacy, organizational politics, fraud analysis, and incentive design. Each task encodes a formal game-theoretic pattern (principal-agent conflict, signaling, mechanism design failure, strategic omission, coalitional dynamics, strategic interdependence) and carries structured ground truth recording the expert reading of the situation and the anticipated failure modes. Models receive raw data and a task prompt with no indication of problem type. Scoring is a three-tier rubric gated by a mandatory conjunctive check. Mandatory criteria encode the predicted wrong paths.
We evaluate 16 models. The best model passes on 27.9% of tasks. The top two models agree on only 31.7% of their passes. Among the top 8, 44 tasks are solved by exactly one model; routing across the top 8 covers 50.7% of the benchmark, nearly double the best single model. Conditional on passing, quality scores converge (approx 83% across models); unconditional scores do not. Same models articulate the relevant game-theoretic concept correctly when asked, then fail to apply it unprompted. We release KWBench to shift how frontier models are evaluated on knowledge work, scoring them on whether they recognize the right problem from the situation alone, not only on how well they execute once the problem has been framed for them.

---


### 103. [Zero-Shot Scalable Resilience in UAV Swarms: A Decentralized Imitation Learning Framework with Physics-Informed Graph Interactions](https://arxiv.org/abs/2604.15762)

**<font color=#1a73e8>作者：</font>** Huan Lin, Lianghui Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale Unmanned Aerial Vehicle (UAV) failures can split an unmanned aerial vehicle swarm network into disconnected sub-networks, making decentralized recovery both urgent and difficult. Centralized recovery methods depend on global topology information and become communication-heavy after severe fragmentation. Decentralized heuristics and multi-agent reinforcement learning methods are easier to deploy, but their performance often degrades when the swarm scale and damage severity vary. We present Physics-informed Graph Adversarial Imitation Learning algorithm (PhyGAIL) that adopts centralized training with decentralized execution. PhyGAIL builds bounded local interaction graphs from heterogeneous observations, and uses physics-informed graph neural network to encode directional local interactions as gated message passing with explicit attraction and repulsion. This gives the policy a physically grounded coordination bias while keeping local observations scale-invariant. It also uses scenario-adaptive imitation learning to improve training under fragmented topologies and variable-length recovery episodes. Our analysis establishes bounded local graph amplification, bounded interaction dynamics, and controlled variance of the terminal success signal. A policy trained on 20-UAV swarms transfers directly to swarms of up to 500 UAVs without fine-tuning, and achieves better performance across reconnection reliability, recovery speed, motion safety, and runtime efficiency than representative baselines.

---


### 104. [When Do Early-Exit Networks Generalize? A PAC-Bayesian Theory of Adaptive Depth](https://arxiv.org/abs/2604.15764)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early-exit neural networks enable adaptive computation by allowing confident predictions to exit at intermediate layers, achieving 2-8$\times$ inference speedup. Despite widespread deployment, their generalization properties lack theoretical understanding -- a gap explicitly identified in recent surveys. This paper establishes a unified PAC-Bayesian framework for adaptive-depth networks. (1) Novel Entropy-Based Bounds: We prove the first generalization bounds depending on exit-depth entropy $H(D)$ and expected depth $\mathbb{E}[D]$ rather than maximum depth $K$, with sample complexity $\mathcal{O}((\mathbb{E}[D] \cdot d + H(D))/\epsilon^2)$. (2) Explicit Constructive Constants: Our analysis yields the leading coefficient $\sqrt{2\ln 2} \approx 1.177$ with complete derivation. (3) Provable Early-Exit Advantages: We establish sufficient conditions under which adaptive-depth networks strictly outperform fixed-depth counterparts. (4) Extension to Approximate Label Independence: We relax the label-independence assumption to $\epsilon$-approximate policies, broadening applicability to learned routing. (5) Comprehensive Validation: Experiments across 6 architectures on 7 benchmarks demonstrate tightness ratios of 1.52-3.87$\times$ (all $p < 0.001$) versus $>$100$\times$ for classical bounds. Bound-guided threshold selection matches validation-tuned performance within 0.1-0.3%.

---


### 105. [Searching for European Alternatives: Digital Sovereignty, Digital Patriotism, and the Emerging Geopolitics of Software Adoption](https://arxiv.org/abs/2604.15767)

**<font color=#1a73e8>作者：</font>** Advait Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Software adoption has traditionally been understood through instrumental lenses, such as usability, cost, security, and interoperability. We argue that a new, ideological dimension is reshaping adoption decisions: one we term digital patriotism, the individual counterpart to the state ideology of digital sovereignty. Through two studies, we trace this phenomenon. First, a directed content analysis of decisions made by European government agencies to switch away from de facto technology standards reveals a shift around 2020: early switches cited costs and vendor lock-in, while later switches invoke sovereignty, geopolitical risk, and investment in local industry. Second, a qualitative analysis of over 700 online comments (over 51,000 words) surfaces how consumers and businesses articulate motivations for seeking European software alternatives. We find that digital patriotism entails a willingness to accept functional compromise in service of ideological goals. Our work extends software adoption theory by drawing attention to value rationality alongside instrumental rationality, and contributes an empirical account of how geopolitics is reshaping technology choice in the workplace.

---


### 106. [Closing the Theory-Practice Gap in Spiking Transformers via Effective Dimension](https://arxiv.org/abs/2604.15769)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking transformers achieve competitive accuracy with conventional transformers while offering $38$-$57\times$ energy efficiency on neuromorphic hardware, yet no theoretical framework guides their design. This paper establishes the first comprehensive expressivity theory for spiking self-attention. We prove that spiking attention with Leaky Integrate-and-Fire neurons is a universal approximator of continuous permutation-equivariant functions, providing explicit spike circuit constructions including a novel lateral inhibition network for softmax normalization with proven $O(1/\sqrt{T})$ convergence. We derive tight spike-count lower bounds via rate-distortion theory: $\varepsilon$-approximation requires $\Omega(L_f^2 nd/\varepsilon^2)$ spikes, with rigorous information-theoretic derivation. Our key insight is input-dependent bounds using measured effective dimensions ($d_{\text{eff}}=47$--$89$ for CIFAR/ImageNet), explaining why $T=4$ timesteps suffice despite worst-case $T \geq 10{,}000$ predictions. We provide concrete design rules with calibrated constants ($C=2.3$, 95\% CI: $[1.9, 2.7]$). Experiments on Spikformer, QKFormer, and SpikingResformer across vision and language benchmarks validate predictions with $R^2=0.97$ ($p<0.001$). Our framework provides the first principled foundation for neuromorphic transformer design.

---


### 107. [PLAF: Pixel-wise Language-Aligned Feature Extraction for Efficient 3D Scene Understanding](https://arxiv.org/abs/2604.15770)

**<font color=#1a73e8>作者：</font>** Junjie Wen, Junlin He, Fei Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate open-vocabulary 3D scene understanding requires semantic representations that are both language-aligned and spatially precise at the pixel level, while remaining scalable when lifted to 3D space. However, existing representations struggle to jointly satisfy these requirements, and densely propagating pixel-wise semantics to 3D often results in substantial redundancy, leading to inefficient storage and querying in large-scale scenes. To address these challenges, we present \emph{PLAF}, a Pixel-wise Language-Aligned Feature extraction framework that enables dense and accurate semantic alignment in 2D without sacrificing open-vocabulary expressiveness. Building upon this representation, we further design an efficient semantic storage and querying scheme that significantly reduces redundancy across both 2D and 3D domains. Experimental results show that \emph{PLAF} provides a strong semantic foundation for accurate and efficient open-vocabulary 3D scene understanding. The codes are publicly available at this https URL.

---


### 108. [Federated Learning with Quantum Enhanced LSTM for Applications in High Energy Physics](https://arxiv.org/abs/2604.15775)

**<font color=#1a73e8>作者：</font>** Abhishek Sawaika, Durga Pritam Suggisetti, Udaya Parampalli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with large-scale datasets and information-critical applications, such as in High Energy Physics (HEP), demands highly complex, large-scale models that are both robust and accurate. To tackle this issue and cater to the learning requirements, we envision using a federated learning framework with a quantum-enhanced model. Specifically, we design a hybrid quantum-classical long-shot-term-memory model (QLSTM) for local training at distributed nodes. It combines the representative power of quantum models in understanding complex relationships within the feature space, and an LSTM-based model to learn necessary correlations across data points. Given the computing limitations and unprecedented cost of current stand-alone noisy-intermediate quantum (NISQ) devices, we propose to use a federated learning setup, where the learning load can be distributed to local servers as per design and data availability. We demonstrate the benefits of such a design on a classification task for the Supersymmetry(SUSY) dataset, having 5M rows. Our experiments indicate that the performance of this design is not only better that some of the existing work using variational quantum circuit (VQC) based quantum machine learning (QML) techniques, but is also comparable ($\Delta \sim \pm 1\%$) to that of classical deep-learning benchmarks. An important observation from this study is that the designed framework has $<$300 parameters and only needs 20K data points to give a comparable performance. Which also turns out to be a 100$\times$ improvement than the compared baseline models. This shows an improved learning capability of the proposed framework with minimal data and resource requirements, due to the joint model with an LSTM based architecture and a quantum enhanced VQC.

---


### 109. [PIIBench: A Unified Multi-Source Benchmark Corpus for Personally Identifiable Information Detection](https://arxiv.org/abs/2604.15776)

**<font color=#1a73e8>作者：</font>** Pritesh Jha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present PIIBench, a unified benchmark corpus for Personally Identifiable Information (PII) detection in natural language text. Existing resources for PII detection are fragmented across domain-specific corpora with mutually incompatible annotation schemes, preventing systematic comparison of detection systems. We consolidate ten publicly available datasets spanning synthetic PII corpora, multilingual Named Entity Recognition (NER) benchmarks, and financial domain annotated text, yielding a corpus of 2,369,883 annotated sequences and 3.35 million entity mentions across 48 canonical PII entity types. We develop a principled normalization pipeline that maps 80+ source-specific label variants to a standardized BIO tagging scheme, applies frequency-based suppression of near absent entity types, and produces stratified 80/10/10 train/validation/test splits preserving source distribution. To establish baseline difficulty, we evaluate eight published systems spanning rule-based engines (Microsoft Presidio), general purpose NER models (spaCy, BERT-base NER, XLM-RoBERTa NER, SpanMarker mBERT, SpanMarker BERT), a PII-specific model (Piiranha DeBERTa), and a financial NER specialist (XtremeDistil FiNER). All systems achieve span-level F1 below 0.14, with the best system (Presidio, F1=0.1385) still producing zero recall on most entity types. These results directly quantify the domain-silo problem and demonstrate that PIIBench presents a substantially harder and more comprehensive evaluation challenge than any existing single source PII dataset. The dataset construction pipeline and benchmark evaluation code are publicly available at this https URL.

---


### 110. [SegMix:Shuffle-based Feedback Learning for Semantic Segmentation of Pathology Images](https://arxiv.org/abs/2604.15777)

**<font color=#1a73e8>作者：</font>** Zhiling Yan, Sicheng Chen, Tianyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation is a critical task in computational pathology, as it identifies areas affected by disease or abnormal growth and is essential for diagnosis and treatment. However, acquiring high-quality pixel-level supervised segmentation data requires significant workload demands from experienced pathologists, limiting the application of deep learning. To overcome this challenge, relaxing the label conditions to image-level classification labels allows for more data to be used and more scenarios to be enabled. One approach is to leverage Class Activation Map (CAM) to generate pseudo pixel-level annotations for semantic segmentation with only image-level labels. However, this method fails to thoroughly explore the essential characteristics of pathology images, thus identifying only small areas that are insufficient for pseudo masking. In this paper, we propose a novel shuffle-based feedback learning method inspired by curriculum learning to generate higher-quality pseudo-semantic segmentation masks. Specifically, we perform patch level shuffle of pathology images, with the model adaptively adjusting the shuffle strategy based on feedback from previous learning. Experimental results demonstrate that our proposed approach outperforms state-of-the-arts on three different datasets.

---


### 111. [Fusing Cellular Network Data and Tollbooth Counts for Urban Traffic Flow Estimation](https://arxiv.org/abs/2604.15782)

**<font color=#1a73e8>作者：</font>** Oluwaleke Yusuf, Shaira Tabassum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic simulations, essential for planning urban transit infrastructure interventions, require vehicle-category-specific origin-destination (OD) data. Existing data sources are imperfect: sparse tollbooth sensors provide accurate vehicle counts by category, while extensive mobility data from cellular network activity captures aggregated crowd movement, but lack modal disaggregation and have systematic biases. This study develops a machine learning framework to correct and disaggregate cellular network data using sparse tollbooth counts as ground truth. The model uses temporal and spatial features to learn the complex relationship between aggregated mobility data and vehicular data. The framework infers destinations from transit routes and implements routing logic to distribute corrected flows between OD pairs. This approach is applied to a bus depot expansion in Trondheim, Norway, generating hourly OD matrices by vehicle length category. The results show how limited but accurate sensor measurements can correct extensive but aggregated mobility data to produce grounded estimates of background vehicular traffic flows. These macro-scale estimates can be refined for micro-scale analysis at desired locations. The framework provides a generalisable approach for generating origin-destination data from cellular network data. This enables downstream tasks, like detailed traffic simulations for infrastructure planning in data-scarce contexts, supporting urban planners in making informed decisions.

---


### 112. [Similarity-Based Bike Station Expansion via Hybrid Denoising Autoencoders](https://arxiv.org/abs/2604.15783)

**<font color=#1a73e8>作者：</font>** Oluwaleke Yusuf, M. Tsaqif Wismadi, Adil Rasheed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban bike-sharing systems require strategic station expansion to meet growing demand. Traditional allocation approaches rely on explicit demand modelling that may not capture the urban characteristics distinguishing successful stations. This study addresses the need to exploit patterns from existing stations to inform expansion decisions, particularly in data-constrained environments. We present a data-driven framework leveraging existing stations deemed desirable by operational metrics. A hybrid denoising autoencoder (HDAE) learns compressed latent representations from multi-source grid-level features (socio-demographic, built environment, and transport network), with a supervised classification head regularising the embedding space structure. Expansion candidates are selected via greedy allocation with spatial constraints based on latent-space similarity to existing stations. Evaluation on Trondheim's bike-sharing network demonstrates that HDAE embeddings yield more spatially coherent clusters and allocation patterns than raw features. Sensitivity analyses across similarity methods and distance metrics confirm robustness. A consensus-based procedure across multiple parametrisations distils 32 high-confidence extension zones where all parametrisations agree. The results demonstrate how representation learning captures complex patterns that raw features miss, enabling evidence-based expansion planning without explicit demand modelling. The consensus procedure strengthens recommendations by requiring agreement across parametrisations, while framework configurability allows planners to incorporate operational knowledge. The methodology generalises to any location-allocation problem where existing desirable instances inform the selection of new candidates.

---


### 113. [Filter Babel: The Challenge of Synthetic Media to Authenticity and Common Ground in AI-Mediated Communication](https://arxiv.org/abs/2604.15786)

**<font color=#1a73e8>作者：</font>** Advait Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Filter Babel is a thought experiment about a near future in which everything we read, watch, and even whom we "meet" is privately generated for each of us. If we each recede into a world of purely private experience, we may each develop a Wittgensteinian private language that remains intelligible to others only because an AI translator sits in the middle. This intermediation challenges the integrity of common ground and therefore of communication. On the other hand, private experience is an essential engine of identity and selfhood: as Lanier warns, one must be somebody before one can share oneself. This paper opens a discussion of the challenges and opportunities that Filter Babel might present to human communication and identity, and what constructive directions for research in AI-mediated communication might ensue.

---


### 114. [Convolutionally Low-Rank Models with Modified Quantile Regression for Interval Time Series Forecasting](https://arxiv.org/abs/2604.15791)

**<font color=#1a73e8>作者：</font>** Miaoxuan Zhu, Yi Yu, Yuyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quantification of uncertainty in prediction models is crucial for reliable decision-making, yet remains a significant challenge. Interval time series forecasting offers a principled solution to this problem by providing prediction intervals (PIs), which indicates the probability that the true value falls within the predicted range. We consider a recently established point forecasts (PFs) method termed Learning-Based Convolution Nuclear Norm Minimization (LbCNNM), which directly generates multi-step ahead forecasts by leveraging the convolutional low-rankness property derived from training data. While theoretically complete and empirically effective, LbCNNM lacks inherent uncertainty estimation capabilities, a limitation shared by many advanced forecasting methods. To resolve the issue, we modify the well-known Quantile Regression (QR) and integrate it into LbCNNM, resulting in a novel interval forecasting method termed LbCNNM with Modified Quantile Regression (LbCNNM-MQR). In addition, we devise interval calibration techniques to further improve the accuracy of PIs. Extensive experiments on over 100,000 real-world time series demonstrate the superior performance of LbCNNM-MQR.

---


### 115. [Fed3D: Federated 3D Object Detection](https://arxiv.org/abs/2604.15795)

**<font color=#1a73e8>作者：</font>** Suyan Dai, Chenxi Liu, Fazeng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object detection models trained in one server plays an important role in autonomous driving, robotics manipulation, and augmented reality scenarios. However, most existing methods face severe privacy concern when deployed on a multi-robot perception network to explore large-scale 3D scene. Meanwhile, it is highly challenging to employ conventional federated learning methods on 3D object detection scenes, due to the 3D data heterogeneity and limited communication bandwidth. In this paper, we take the first attempt to propose a novel Federated 3D object detection framework (i.e., Fed3D), to enable distributed learning for 3D object detection with privacy preservation. Specifically, considering the irregular input 3D object in local robot and various category distribution between robots could cause local heterogeneity and global heterogeneity, respectively. We then propose a local-global class-aware loss for the 3D data heterogeneity issue, which could balance gradient back-propagation rate of different 3D categories from local and global aspects. To reduce communication cost on each round, we develop a federated 3D prompt module, which could only learn and communicate the prompts with few learnable parameters. To the end, several extensive experiments on federated 3D object detection show that our Fed3D model significantly outperforms state-of-the-art algorithms with lower communication cost when providing the limited local training data.

---


### 116. [From Intention to Text: AI-Supported Goal Setting in Academic Writing](https://arxiv.org/abs/2604.15800)

**<font color=#1a73e8>作者：</font>** Yueling Fan, Richard Lee Davis, Olga Viberg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study presents WriteFlow, an AI voice-based writing assistant designed to support reflective academic writing through goal-oriented interaction. Academic writing involves iterative reflection and evolving goal regulation, yet prior research and a formative study with 17 participants show that writers often struggle to articulate and manage changing goals. While commonly used AI writing tools emphasize efficiency, they offer limited support for metacognition and writer agency. WriteFlow frames AI interaction as a dialogic space for ongoing goal articulation, monitoring, and negotiation grounded in writers' intentions. Findings from a Wizard-of-Oz study with 12 expert users show that WriteFlow scaffolds metacognitive regulation and reflection-in-action by supporting iterative goal refinement, maintaining goal-text alignment during drafting, and prompting evaluation of goal fulfillment. We discuss design implications for AI writing systems that prioritize reflective dialogue, flexible goal structures, and multi-perspective feedback to support intentional and agentic writing.

---


### 117. [Secure Authentication in Wireless IoT: Hamming Code Assisted SRAM PUF as Device Fingerprint](https://arxiv.org/abs/2604.15810)

**<font color=#1a73e8>作者：</font>** Florian Lehn, Pascal Ahr, Hans D. Schotten  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static Random Access Memory (SRAM) Physically Unclonable Functions (PUFs) make use of intrinsic manufacturing variations in memory cells to derive device-unique responses. Employing such hardware-rooted fingerprints for authentication, this work demonstrates a threshold-based authentication proof of concept for constrained Industrial Internet of Things (IIoT) devices. The proposed scheme can reliably cap the the post-authentication bit error rate (BER) below 1 %. Inherent SRAM PUF unreliability is addressed by a resource-efficient combination of Hamming code (HC) Error Correction (EC) and Temporal Majority Voting (TMV). Increasing HC redundancy or TMV count significantly reduces the BER, albeit with diminishing returns and increasingly prohibitive computational overhead. Furthermore, this work quantifies the threshold gap between strict reliability and security constraints. This gap is reframed as a design budget which enables the resource-aware calibration of the acceptance threshold, PUF response length, and stabilization technique, without violating designed-for error limits. Larger responses make reliability optimizations increasingly obsolete. This comparative analysis establishes a comprehensive design space for PUF EC, guiding future implementations in balancing EC quality against resource constraints such as computational demand, power consumption, and implementation complexity.

---


### 118. [Continual Hand-Eye Calibration for Open-world Robotic Manipulation](https://arxiv.org/abs/2604.15814)

**<font color=#1a73e8>作者：</font>** Fazeng Li, Gan Sun, Chenxi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand-eye calibration through visual localization is a critical capability for robotic manipulation in open-world environments. However, most deep learning-based calibration models suffer from catastrophic forgetting when adapting into unseen data amongst open-world scene changes, while simple rehearsal-based continual learning strategy cannot well mitigate this issue. To overcome this challenge, we propose a continual hand-eye calibration framework, enabling robots to adapt to sequentially encountered open-world manipulation scenes through spatially replay strategy and structure-preserving distillation. Specifically, a Spatial-Aware Replay Strategy (SARS) constructs a geometrically uniform replay buffer that ensures comprehensive coverage of each scene pose space, replacing redundant adjacent frames with maximally informative viewpoints. Meanwhile, a Structure-Preserving Dual Distillation (SPDD) is proposed to decompose localization knowledge into coarse scene layout and fine pose precision, and distills them separately to alleviate both types of forgetting during continual adaptation. As a new manipulation scene arrives, SARS provides geometrically representative replay samples from all prior scenes, and SPDD applies structured distillation on these samples to retain previously learned knowledge. After training on the new scene, SARS incorporates selected samples from the new scene into the replay buffer for future rehearsal, allowing the model to continuously accumulate multi-scene calibration capability. Experiments on multiple public datasets show significant anti scene forgetting performance, maintaining accuracy on past scenes while preserving adaptation to new scenes, confirming the effectiveness of the framework.

---


### 119. [ECG-Lens: Benchmarking ML & DL Models on PTB-XL Dataset](https://arxiv.org/abs/2604.15822)

**<font color=#1a73e8>作者：</font>** Saloni Garg, Ukant Jadia, Amit Sagtani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated classification of electrocardiogram (ECG) signals is a useful tool for diagnosing and monitoring cardiovascular diseases. This study compares three traditional machine learning algorithms (Decision Tree Classifier, Random Forest Classifier, and Logistic Regression) and three deep learning models (Simple Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM), and Complex CNN (ECGLens)) for the classification of ECG signals from the PTB-XL dataset, which contains 12-lead recordings from normal patients and patients with various cardiac conditions. The DL models were trained on raw ECG signals, allowing them to automatically extract discriminative features. Data augmentation using the Stationary Wavelet Transform (SWT) was applied to enhance model performance, increase the diversity of training samples, and preserve the essential characteristics of the ECG signals. The models were evaluated using multiple metrics, including accuracy, precision, recall, F1-score, and ROC-AUC. The ECG-Lens model achieved the highest performance, with 80% classification accuracy and a 90% ROC-AUC. These findings demonstrate that deep learning architectures, particularly complex CNNs substantially outperform traditional ML methods on raw 12-lead ECG data, and provide a practical benchmark for selecting automated ECG classification models and identifying directions for condition-specific model development.

---


### 120. [Watching Movies Like a Human: Egocentric Emotion Understanding for Embodied Companions](https://arxiv.org/abs/2604.15823)

**<font color=#1a73e8>作者：</font>** Ze Dong, Hao Shi, Zejia Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied robotic agents often perceive movies through an egocentric screen-view interface rather than native cinematic footage, introducing domain shifts such as viewpoint distortion, scale variation, illumination changes, and environmental interference. However, existing research on movie emotion understanding is almost exclusively conducted on cinematic footage, limiting cross-domain generalization to real-world viewing scenarios. To bridge this gap, we introduce EgoScreen-Emotion (ESE), the first benchmark dataset for egocentric screen-view movie emotion understanding. ESE contains 224 movie trailers captured under controlled egocentric screen-view conditions, producing 28,667 temporally aligned key-frames annotated by multiple raters with a confidence-aware multi-label protocol to address emotional ambiguity. We further build a multimodal long-context emotion reasoning framework that models temporal visual evidence, narrative summaries, compressed historical context, and audio cues. Cross-domain experiments reveal a severe domain gap: models trained on cinematic footage drop from 27.99 to 16.69 Macro-F1 when evaluated on realistic egocentric screen-view observations. Training on ESE substantially improves robustness under realistic viewing conditions. Our approach achieves competitive performance compared with strong closed-source multimodal models, highlighting the importance of domain-specific data and long-context multimodal reasoning.

---


### 121. [Beyond Text Prompts: Precise Concept Erasure through Text-Image Collaboration](https://arxiv.org/abs/2604.15829)

**<font color=#1a73e8>作者：</font>** Jun Li, Lizhi Xiong, Ziqiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generative models have achieved impressive fidelity and diversity, but can inadvertently produce unsafe or undesirable content due to implicit biases embedded in large-scale training datasets. Existing concept erasure methods, whether text-only or image-assisted, face trade-offs: textual approaches often fail to fully suppress concepts, while naive image-guided methods risk over-erasing unrelated content. We propose TICoE, a text-image Collaborative Erasing framework that achieves precise and faithful concept removal through a continuous convex concept manifold and hierarchical visual representation learning. TICoE precisely removes target concepts while preserving unrelated semantic and visual content. To objectively assess the quality of erasure, we further introduce a fidelity-oriented evaluation strategy that measures post-erasure usability. Experiments on multiple benchmarks show that TICoE surpasses prior methods in concept removal precision and content fidelity, enabling safer, more controllable text-to-image generation. Our code is available at this https URL

---


### 122. [Placing Puzzle Pieces Where They Matter: A Question Augmentation Framework for Reinforcement Learning](https://arxiv.org/abs/2604.15830)

**<font color=#1a73e8>作者：</font>** Yangyi Fang, Jiaye Lin, Xiaoliang Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a powerful approach for enhancing large language model reasoning, but faces a fundamental dilemma: training on easy problems can cause overfitting and pass@k degradation, while training on hard problems often results in sparse rewards. Recent question augmentation methods address this by prepending partial solutions as hints. However, uniform hint provision may introduce redundant information while missing critical reasoning bottlenecks, and excessive hints can reduce reasoning diversity, causing pass@k degradation. We propose \textbf{PieceHint}, a hint injection framework that strategically identifies and provides critical reasoning steps during training. By scoring the importance of different reasoning steps, selectively allocating hints based on problem difficulty, and progressively withdrawing scaffolding, PieceHint enables models to transition from guided learning to independent reasoning. Experiments on six mathematical reasoning benchmarks show that our 1.5B model achieves comparable average performance to 32B baselines while preserving pass@k diversity across all $k$ values.

---


### 123. [A Protocol-Agnostic Backscatter-Based Security Layer for Ultra-Low-Power SWIPT IoT Networks](https://arxiv.org/abs/2604.15831)

**<font color=#1a73e8>作者：</font>** Taki Eddine Djidjekh, Alexandru Takacs, Gaël Loubet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a lightweight, protocol-agnostic security enhancement for Simultaneous Wireless Information and Power Transfer (SWIPT) in Internet of Things (IoT) applications. Building on a backscatter-based identification mechanism, the proposed approach introduces a secure, energy-efficient layer that operates independently of communication protocols and with minimal hardware modification. A rectifier-driven backscattering scheme embedded in battery-free sensing nodes enables authentication without activating conventional RF transceivers, thereby reducing power consumption while ensuring secure device identification. To assess robustness, replay attacks are emulated on standard LoRaWAN Activation By Personalization (ABP) encryption, highlighting vulnerabilities and demonstrating the relevance of the proposed solution. The approach is experimentally validated in a real Wireless Sensor Network (WSN) using LoRaWAN-compatible, battery-free sensing nodes equipped with compact, low-profile antennas, confirming both practicality and scalability for space-constrained IoT deployments. Results show that the method achieves secure identification, reliable energy harvesting, and data transmission with negligible impact on node autonomy. The proposed approach offers a practical, energy-efficient, and scalable security framework for SWIPT-enabled IoT systems, strengthening device authentication without altering existing communication protocols or compromising power autonomy.

---


### 124. [Modern Structure-Aware Simplicial Spatiotemporal Neural Network](https://arxiv.org/abs/2604.15833)

**<font color=#1a73e8>作者：</font>** Zhaobo Hu, Vincent Gauthier, Mehdi Naima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal modeling has evolved beyond simple time series analysis to become fundamental in structural time series analysis. While current research extensively employs graph neural networks (GNNs) for spatial feature extraction with notable success, these networks are limited to capturing only pairwise relationships, despite real-world networks containing richer topological relationships. Additionally, GNN-based models face computational challenges that scale with graph complexity, limiting their applicability to large networks. To address these limitations, we present Modern Structure-Aware Simplicial SpatioTemporal neural network (ModernSASST), the first approach to leverage simplicial complex structures for spatiotemporal modeling. Our method employs spatiotemporal random walks on high-dimensional simplicial complexes and integrates parallelizable Temporal Convolutional Networks to capture high-order topological structures while maintaining computational efficiency. Our source code is publicly available on GitHub\footnote{Code is available at: this https URL.

---


### 125. [Stein Variational Black-Box Combinatorial Optimization](https://arxiv.org/abs/2604.15837)

**<font color=#1a73e8>作者：</font>** Thomas Landais, Olivier Goudet, Adrien Goëffon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combinatorial black-box optimization in high-dimensional settings demands a careful trade-off between exploiting promising regions of the search space and preserving sufficient exploration to identify multiple optima. Although Estimation-of-Distribution Algorithms (EDAs) provide a powerful model-based framework, they often concentrate on a single region of interest, which may result in premature convergence when facing complex or multimodal objective landscapes. In this work, we incorporate the Stein operator to introduce a repulsive mechanism among particles in the parameter space, thereby encouraging the population to disperse and jointly explore several modes of the fitness landscape. Empirical evaluations across diverse benchmark problems show that the proposed method achieves performance competitive with, and in several cases superior to, leading state-of-the-art approaches, particularly on large-scale instances. These findings highlight the potential of Stein variational gradient descent as a promising direction for addressing large, computationally expensive, discrete black-box optimization problems.

---


### 126. [Reversible Residual Normalization Alleviates Spatio-Temporal Distribution Shift](https://arxiv.org/abs/2604.15838)

**<font color=#1a73e8>作者：</font>** Zhaobo Hu, Vincent Gauthier, Mehdi Naima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distribution shift severely degrades the performance of deep forecasting models. While this issue is well-studied for individual time series, it remains a significant challenge in the spatio-temporal domain. Effective solutions like instance normalization and its variants can mitigate temporal shifts by standardizing statistics. However, distribution shift on a graph is far more complex, involving not only the drift of individual node series but also heterogeneity across the spatial network where different nodes exhibit distinct statistical properties. To tackle this problem, we propose Reversible Residual Normalization (RRN), a novel framework that performs spatially-aware invertible transformations to address distribution shift in both spatial and temporal dimensions. Our approach integrates graph convolutional operations within invertible residual blocks, enabling adaptive normalization that respects the underlying graph structure while maintaining reversibility. By combining Center Normalization with spectral-constrained graph neural networks, our method captures and normalizes complex Spatio-Temporal relationships in a data-driven manner. The bidirectional nature of our framework allows models to learn in a normalized latent space and recover original distributional properties through inverse transformation, offering a robust and model-agnostic solution for forecasting on dynamic spatio-temporal systems.

---


### 127. [QUACK! Making the (Rubber) Ducky Talk: A Systematic Study of Keystroke Dynamics for HID Injection Detection](https://arxiv.org/abs/2604.15845)

**<font color=#1a73e8>作者：</font>** Alessandro Lotto, Francesco Marchiori, Mauro Conti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern computing systems inherently trust human input devices, creating an exploitable attack surface for adversarial automation. USB Human Interface Device (HID) emulation attacks, such as those enabled by the USB Rubber Ducky, exploit this assumption to inject arbitrary keystroke sequences while bypassing traditional defenses. Existing countermeasures rely on simple heuristics based on typing speed or timing regularity, which can be easily evaded through basic randomization. Keystroke dynamics analysis offers a more robust alternative by modeling temporal typing behavior. However, prior work frames this problem as behavioral authentication, verifying whether input originates from a specific user rather than detecting automated injection. An alternative approach is continuous monitoring via keylogging integrated with intrusion detection systems, but this requires access to input content, raising significant privacy concerns.
In this paper, we provide the first systematic characterization of keystroke dynamics for human-vs-machine discrimination, independent of user identity. Guided by five research questions, we show that robust, privacy-preserving detection is achievable using lightweight models operating solely on timing features, eliminating the need for content access or user profiling. Our analysis reveals that attacker sophistication does not monotonically translate into improved evasion. Instead, robustness depends on exposure to structurally diverse generation strategies rather than increased model complexity. Finally, we quantify the trade-off between detection timeliness and reliability across varying keystroke sequence lengths, identifying practical operating points for early and effective attack interception.

---


### 128. [Learning to Look before Learning to Like: Incorporating Human Visual Cognition into Aesthetic Quality Assessment](https://arxiv.org/abs/2604.15853)

**<font color=#1a73e8>作者：</font>** Liwen Yu, Chi Liu, Xiaotong Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated Aesthetic Quality Assessment (AQA) treats images primarily as static pixel vectors, aligning predictions with human-rating scores largely through semantic perception. However, this paradigm diverges from human aesthetic cognition, which arises from dynamic visual exploration shaped by scanning paths, processing fluency, and the interplay between bottom-up salience and top-down intention. We introduce AestheticNet, a novel cognitive-inspired AQA paradigm that integrates human-like visual cognition and semantic perception with a two-pathway architecture. The visual attention pathway, implemented as a gaze-aligned visual encoder (GAVE) pre-trained offline on eye-tracking data using resource-efficient contrast gaze alignment, models attention from human vision system. This pathway augments the semantic pathway, which uses a fixed semantic encoder such as CLIP, through cross-attention fusion. Visual attention provides a cognitive prior reflecting foreground/background structure, color cascade, brightness, and lighting, all of which are determinants of aesthetic perception beyond semantics. Experiments validated by hypothesis testing show a consistent improvement over the semantic-alone baselines, and demonstrate the gaze module as a model-agnostic corrector compatible with diverse AQA backbones, supporting the necessity and modularity of human-like visual cognition for AQA. Our code is available at this https URL.

---


### 129. [Robust Multispectral Semantic Segmentation under Missing or Full Modalities via Structured Latent Projection](https://arxiv.org/abs/2604.15856)

**<font color=#1a73e8>作者：</font>** Irem Ulku, Erdem Akagündüz, Ömer Özgür Tanrıöver  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal remote sensing data provide complementary information for semantic segmentation, but in real-world deployments, some modalities may be unavailable due to sensor failures, acquisition issues, or challenging atmospheric conditions. Existing multimodal segmentation models typically address missing modalities by learning a shared representation across inputs. However, this approach can introduce a trade-off by compromising modality-specific complementary information and reducing performance when all modalities are available. In this paper, we tackle this limitation with CBC-SLP, a multimodal semantic segmentation model designed to preserve both modality-invariant and modality-specific information. Inspired by the theoretical results on modality alignment, which state that perfectly aligned multimodal representations can lead to sub-optimal performance in downstream prediction tasks, we propose a novel structured latent projection approach as an architectural inductive bias. Rather than enforcing this strategy through a loss term, we incorporate it directly into the architecture. In particular, to use the complementary information effectively while maintaining robustness under random modality dropout, we structure the latent representations into shared and modality-specific components and adaptively transfer them to the decoder according to the random modality availability mask. Extensive experiments on three multimodal remote sensing image sets demonstrate that CBC-SLP consistently outperforms state-of-the-art multimodal models across full and missing modality scenarios. Besides, we empirically demonstrate that the proposed strategy can recover the complementary information that may not be preserved in a shared representation. The code is available at this https URL.

---


### 130. [AHS: Adaptive Head Synthesis via Synthetic Data Augmentations](https://arxiv.org/abs/2604.15857)

**<font color=#1a73e8>作者：</font>** Taewoong Kang, Hyojin Jang, Sohyun Jeong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent digital media advancements have created increasing demands for sophisticated portrait manipulation techniques, particularly head swapping, where one's head is seamlessly integrated with another's body. However, current approaches predominantly rely on face-centered cropped data with limited view angles, significantly restricting their real-world applicability. They struggle with diverse head expressions, varying hairstyles, and natural blending beyond facial regions. To address these limitations, we propose Adaptive Head Synthesis (AHS), which effectively handles full upper-body images with varied head poses and expressions. AHS incorporates a novel head reenacted synthetic data augmentation strategy to overcome self-supervised training constraints, enhancing generalization across diverse facial expressions and orientations without requiring paired training data. Comprehensive experiments demonstrate that AHS achieves superior performance in challenging real-world scenarios, producing visually coherent results that preserve identity and expression fidelity across various head orientations and hairstyles. Notably, AHS shows exceptional robustness in maintaining facial identity while drastic expression changes and faithfully preserving accessories while significant head pose variations.

---


### 131. [Module Lattice Security (Part I): Unconditional Verification of Weber's Conjecture for $k \le 12$](https://arxiv.org/abs/2604.15858)

**<font color=#1a73e8>作者：</font>** Ming-Xing Luo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Weber's conjecture (1886) governs three aspects of lattice-based cryptography: the solvability of the Principal Ideal Problem, the freeness of modules over rings of integers, and the tightness of worst-case-to-average-case reductions in Ring-LWE (R-LWE) and Module-LWE (MLWE). Existing verifications for $k \ge 9$ rely on Generalized Riemann Hypothesis (GRH). In this paper, we present the first unconditional proof for $k \le 12$. Our method combines the Fukuda-Komatsu computational sieve, inductive structure of the cyclotomic $\mathbb{Z}_2$-tower, and Herbrand's theorem.

---


### 132. [Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862)

**<font color=#1a73e8>作者：</font>** Yijia Guo, Wenkai Huang, Tong Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has recently redefined the paradigm of 3D reconstruction, striking an unprecedented balance between visual fidelity and computational efficiency. As its adoption proliferates, safeguarding the copyright of explicit 3DGS assets has become paramount. However, existing invisible message embedding frameworks struggle to reconcile secure and high-capacity data embedding with intrinsic asset utility, often disrupting the native rendering pipeline or exhibiting vulnerability to structural perturbations. In this work, we present \textbf{\textit{Splats in Splats++}}, a unified and pipeline-agnostic steganography framework that seamlessly embeds high-capacity 3D/4D content directly within the native 3DGS representation. Grounded in a principled analysis of the frequency distribution of Spherical Harmonics (SH), we propose an importance-graded SH coefficient encryption scheme that achieves imperceptible embedding without compromising the original expressive power. To fundamentally resolve the geometric ambiguities that lead to message leakage, we introduce a \textbf{Hash-Grid Guided Opacity Mapping} mechanism. Coupled with a novel \textbf{Gradient-Gated Opacity Consistency Loss}, our formulation enforces a stringent spatial-attribute coupling between the original and hidden scenes, effectively projecting the discrete attribute mapping into a continuous, attack-resilient latent manifold. Extensive experiments demonstrate that our method substantially outperforms existing approaches, achieving up to \textbf{6.28 db} higher message fidelity, \textbf{3$\times$} faster rendering, and exceptional robustness against aggressive 3D-targeted structural attacks (e.g., GSPure). Furthermore, our framework exhibits remarkable versatility, generalizing seamlessly to 2D image embedding, 4D dynamic scene steganography, and diverse downstream tasks.

---


### 133. [Low-Stack HAETAE for Memory-Constrained Microcontrollers](https://arxiv.org/abs/2604.15868)

**<font color=#1a73e8>作者：</font>** Gustavo Banegas, Kim Youngbeom, Seo Seog Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a low-stack implementation of the module-lattice signature scheme HAETAE, targeting microcontrollers with 8 kB-16 kB of available SRAM. On such devices, peak stack usage is often the binding constraint, and HAETAE's hyperball-based sampler, large transient polynomial vectors, and variable-length signature payloads (hint and high-bits arrays) pose a particular challenge. To address this we introduce (i) Rejection-aware pass decomposition, which isolates encoding to the post-acceptance path; (ii) Component-level early rejection, which short-circuits the response computation when a partial norm already exceeds the bound; and (iii) Reverse-order streaming entropy coding using range Asymmetric Numeral Systems (rANS), which eliminates full hint and high-bits staging buffers. Combined with streamed matrix generation, a two-pass hyperball sampler with streaming Gaussian backend, and row-streamed verification, these techniques bring Signing stack from 71 kB-141 kB in the reference implementation down to 5.8 kB-6.0 kB, key generation to 4.7 kB-5.7 kB, and verification to 4.7 kB-4.8 kB across all three security levels. Our pure C implementation covers all three security levels (HAETAE-2/3/5), whose optimization paths differ due to the public-key domain (d>0 vs. d=0) and rejection structure. We implement our optimization on a Nucleo-L4R5ZI and compare to the reference pqm4 (for HAETAE-2 and -3) and a recently published memory-optimized implementation (targeting HAETAE-5 only). We reduce HAETAE-2, -3, and -5 stack by respectively 75, 86 and 8 % for key generation, 92, 95 and 24 % for signature generation, and 85, 91 and 22 % for verification. Depending on the parameter set, this impacts performance by at most a factor 1.8 and 3.4 for key and signature generation respectively, while even offering a performance improvement up to 18 % for verification. Verification at all security levels fits within 8 kB of RAM (signature buffer + stack) and is 2.34-3.34x faster than ML-DSA m4fstack at each comparable security level. We additionally validate portability under RIOT-OS on ARM Cortex-M4 and RISC-V targets.

---


### 134. [CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875)

**<font color=#1a73e8>作者：</font>** Sadia Mubashshira, Nazanin Amini, Kevin Desai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Cloth-HUGS, a Gaussian Splatting based neural rendering framework for photorealistic clothed human reconstruction that explicitly disentangles body and clothing. Unlike prior methods that absorb clothing into a single body representation and struggle with loose garments and complex deformations, Cloth-HUGS represents the performer using separate Gaussian layers for body and cloth within a shared canonical space. The canonical volume jointly encodes body, cloth, and scene primitives and is deformed through SMPL-driven articulation with learned linear blend skinning weights. To improve cloth realism, we initialize cloth Gaussians from mesh topology and apply physics-inspired constraints, including simulation-consistency, ARAP regularization, and mask supervision. We further introduce a depth-aware multi-pass rendering strategy for robust body-cloth-scene compositing, enabling real-time rendering at over 60 FPS. Experiments on multiple benchmarks show that Cloth-HUGS improves perceptual quality and geometric fidelity over state-of-the-art baselines, reducing LPIPS by up to 28% while producing temporally coherent cloth dynamics.

---


### 135. [Towards Rigorous Explainability by Feature Attribution](https://arxiv.org/abs/2604.15898)

**<font color=#1a73e8>作者：</font>** Olivier Létoffé, Xuanxiang Huang, Joao Marques-Silva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For around a decade, non-symbolic methods have been the option of choice when explaining complex machine learning (ML) models. Unfortunately, such methods lack rigor and can mislead human decision-makers. In high-stakes uses of ML, the lack of rigor is especially problematic. One prime example of provable lack of rigor is the adoption of Shapley values in explainable artificial intelligence (XAI), with the tool SHAP being a ubiquitous example. This paper overviews the ongoing efforts towards using rigorous symbolic methods of XAI as an alternative to non-rigorous non-symbolic approaches, concretely for assigning relative feature importance.

---


### 136. [Shaping Plant-Like Shape-Changing Interfaces as Vertical Charts: Maximizing Readability, Aesthetics, and Naturalness](https://arxiv.org/abs/2604.15902)

**<font color=#1a73e8>作者：</font>** Elodie Bouzekri, Guillaume Riviere  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conveying environmental data has grown interest in encouraging the adoption of eco-friendly lifestyles through data-driven strategies. This scope appeals to data visualizations representing the environmental purpose. For example, previous work has already proposed nature-inspired counters, gauges, and bitmaps, but data series remains to be explored. Therefore, could we design and implement effective plant-like charts? This paper brings answers through a research-through-design approach that explores a design space to maximize readability and aesthetics. It then compares four prototypes of charts over modality and material dimensions by asking users about scenarios involving renewable energy forecasts. The results examine whether implementing physical charts is worth it instead of graphical charts and the advantages of using meaningful materials that evocate sustainability and enhance naturalness. The results also reexamine, with physical charts, the previous results on graphical infographics of slightly lower clarity and readability but higher aesthetics of embellishment. In addition, learnability is examined for encoding rates through folded shapes. This paper shows that physical plant-like charts are worthwhile because of promising performance and best-of-breed naturalness when materials allow low-tech aspects' perception and because being installable in public places without explanations if folded shapes encode rates ranging from 0 to a maximum value.

---


### 137. [AeroDeshadow: Physics-Guided Shadow Synthesis and Penumbra-Aware Deshadowing for Aerospace Imagery](https://arxiv.org/abs/2604.15903)

**<font color=#1a73e8>作者：</font>** Wei Lu, Zi-Yang Bo, Fei-Fei Sang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadows are prevalent in high-resolution aerospace imagery (ASI). They often cause spectral distortion and information loss, which degrade downstream interpretation tasks. While deep learning methods have advanced natural-image shadow removal, their direct application to ASI faces two primary challenges. First, strictly paired training data are severely lacking. Second, homogeneous shadow assumptions fail to handle the broad penumbra transition zones inherent in aerospace scenes. To address these issues, we propose AeroDeshadow, a unified two-stage framework integrating physics-guided shadow synthesis and penumbra-aware restoration. In the first stage, a Physics-aware Degradation Shadow Synthesis Network (PDSS-Net) explicitly models illumination decay and spatial attenuation. This process constructs AeroDS-Syn, a large-scale paired dataset featuring soft boundary transitions. Constrained by this physical formulation, a Penumbra-aware Cascaded DeShadowing Network (PCDS-Net) then decouples the input into umbra and penumbra components. By restoring these regions progressively, PCDS-Net alleviates boundary artifacts and over-correction. Trained solely on the synthetic AeroDS-Syn, the network generalizes to real-world ASI without requiring paired real annotations. Experimental results indicate that AeroDeshadow achieves state-of-the-art quantitative accuracy and visual fidelity across synthetic and real-world datasets. The datasets and code will be made publicly available at: this https URL.

---


### 138. [Efficient Video Diffusion Models: Advancements and Challenges](https://arxiv.org/abs/2604.15911)

**<font color=#1a73e8>作者：</font>** Shitong Shao, Lichen Bai, Pengfei Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have rapidly become the dominant paradigm for high-fidelity generative video synthesis, but their practical deployment remains constrained by severe inference costs. Compared with image generation, video synthesis compounds computation across spatial-temporal token growth and iterative denoising, making attention and memory traffic major bottlenecks in real-world settings. This survey provides a systematic and deployment-oriented review of efficient video diffusion models. We propose a unified categorization that organizes existing methods into four classes of main paradigms, including step distillation, efficient attention, model compression, and cache/trajectory optimization. Building on this categorization, we respectively analyze algorithmic trends of these four paradigms and examine how different design choices target two core objectives: reducing the number of function evaluations and minimizing per-step overhead. Finally, we discuss open challenges and future directions, including quality preservation under composite acceleration, hardware-software co-design, robust real-time long-horizon generation, and open infrastructure for standardized evaluation. To the best of our knowledge, our work is the first comprehensive survey on efficient video diffusion models, offering researchers and engineers a structured overview of the field and its emerging research directions.

---


### 139. [MUSCAT: MUltilingual, SCientific ConversATion Benchmark](https://arxiv.org/abs/2604.15929)

**<font color=#1a73e8>作者：</font>** Supriti Sinhamahapatra, Thai-Binh Nguyen, Yiğit Oğuz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The goal of multilingual speech technology is to facilitate seamless communication between individuals speaking different languages, creating the experience as though everyone were a multilingual speaker. To create this experience, speech technology needs to address several challenges: Handling mixed multilingual input, specific vocabulary, and code-switching. However, there is currently no dataset benchmarking this situation. We propose a new benchmark to evaluate current Automatic Speech Recognition (ASR) systems, whether they are able to handle these challenges. The benchmark consists of bilingual discussions on scientific papers between multiple speakers, each conversing in a different language. We provide a standard evaluation framework, beyond Word Error Rate (WER) enabling consistent comparison of ASR performance across languages. Experimental results demonstrate that the proposed dataset is still an open challenge for state-of-the-art ASR systems. The dataset is available in this https URL
\\ \newline \Keywords{multilingual, speech recognition, audio segmentation, speaker diarization}

---


### 140. [(Weighted) Adaptive Radius Near Neighbor Search: Evaluation for WiFi Fingerprint-based Positioning](https://arxiv.org/abs/2604.15940)

**<font color=#1a73e8>作者：</font>** Khang Le, Joaquín Torres-Sospedra, Philipp Müller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed Radius Near Neighbor (FRNN) search is an alternative to the widely used k Nearest Neighbors (kNN) search. Unlike kNN, FRNN determines a label or an estimate for a test sample based on all training samples within a predefined distance. While this approach is beneficial in certain scenarios, assuming a fixed maximum distance for all training samples can decrease the accuracy of the FRNN. Therefore, in this paper we propose the Adaptive Radius Near Neighbor (ARNN) and the Weighted ARNN (WARNN), which employ adaptive distances and in latter case weights. All three methods are compared to kNN and twelve of its variants for a regression problem, namely WiFi fingerprinting indoor positioning, using 22 different datasets to provide a comprehensive analysis. While the performances of the tested FRNN and ARNN versions were amongst the worse, three of the four best methods in the test were WARNN versions, indicating that using weights together with adaptive distances achieves performance comparable or even better than kNN variants.

---


### 141. [Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941)

**<font color=#1a73e8>作者：</font>** Haato Watanabe, Nobuyuki Umetani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the rapid emergence of 3D Gaussian splatting (3DGS) as a powerful approach for 3D reconstruction and novel view synthesis. Its explicit representation with Gaussian primitives enables fast training, real-time rendering, and convenient post-processing such as editing and surface reconstruction. However, 3DGS suffers from a critical drawback: the number of primitives grows drastically for scenes with high-frequency appearance details, since each primitive can represent only a single color, requiring multiple primitives for every sharp color transition. To overcome this limitation, we propose neural Gabor splatting, which augments each Gaussian primitive with a lightweight multi-layer perceptron that models a wide range of color variations within a single primitive. To further control primitive numbers, we introduce a frequency-aware densification strategy that selects mismatch primitives for pruning and cloning based on frequency energy. Our method achieves accurate reconstruction of challenging high-frequency surfaces. We demonstrate its effectiveness through extensive experiments on both standard benchmarks, such as Mip-NeRF360 and High-Frequency datasets (e.g., checkered patterns), supported by comprehensive ablation studies.

---


### 142. [SENSE: Stereo OpEN Vocabulary SEmantic Segmentation](https://arxiv.org/abs/2604.15946)

**<font color=#1a73e8>作者：</font>** Thomas Campagnolo, Ezio Malis, Philippe Martinet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation enables models to segment objects or image regions beyond fixed class sets, offering flexibility in dynamic environments. However, existing methods often rely on single-view images and struggle with spatial precision, especially under occlusions and near object boundaries. We propose SENSE, the first work on Stereo OpEN Vocabulary SEmantic Segmentation, which leverages stereo vision and vision-language models to enhance open-vocabulary semantic segmentation. By incorporating stereo image pairs, we introduce geometric cues that improve spatial reasoning and segmentation accuracy. Trained on the PhraseStereo dataset, our approach achieves strong performance in phrase-grounded tasks and demonstrates generalization in zero-shot settings. On PhraseStereo, we show a +2.9% improvement in Average Precision over the baseline method and +0.76% over the best competing method. SENSE also provides a relative improvement of +3.5% mIoU on Cityscapes and +18% on KITTI compared to the baseline work. By jointly reasoning over semantics and geometry, SENSE supports accurate scene understanding from natural language, essential for autonomous robots and Intelligent Transportation Systems.

---


### 143. [From Competition to Coopetition: Coopetitive Training-Free Image Editing Based on Text Guidance](https://arxiv.org/abs/2604.15948)

**<font color=#1a73e8>作者：</font>** Jinhao Shen, Haoqian Du, Xulu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing, a pivotal task in modern multimedia content creation, has seen remarkable progress with training-free methods that eliminate the need for additional optimization. Despite recent progress, existing methods are typically constrained by a competitive paradigm in which the editing and reconstruction branches are independently driven by their respective objectives to maximize alignment with target and source prompts. The adversarial strategy causes semantic conflicts and unpredictable outcomes due to the lack of coordination between branches. To overcome these issues, we propose Coopetitive Training-Free Image Editing (CoEdit), a novel zero-shot framework that transforms attention control from competition to coopetitive negotiation, achieving editing harmony across spatial and temporal dimensions. Spatially, CoEdit introduces Dual-Entropy Attention Manipulation, which quantifies directional entropic interactions between branches to reformulate attention control as a harmony-maximization problem, eventually improving the localization of editable and preservable regions. Temporally, we present Entropic Latent Refinement mechanism to dynamically adjust latent representations over time, minimizing accumulated editing errors and ensuring consistent semantic transitions throughout the denoising trajectory. Additionally, we propose the Fidelity-Constrained Editing Score, a composite metric that jointly evaluates semantic editing and background fidelity. Extensive experiments on standard benchmarks demonstrate that CoEdit achieves superior performance in both editing quality and structural preservation, enhancing multimedia information utilization by enabling more effective interaction between visual and textual modalities. The code will be available at this https URL.

---


### 144. [TwinTrack: Post-hoc Multi-Rater Calibration for Medical Image Segmentation](https://arxiv.org/abs/2604.15950)

**<font color=#1a73e8>作者：</font>** Tristan Kirscher, Alexandra Ertl, Klaus Maier-Hein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pancreatic ductal adenocarcinoma (PDAC) segmentation on contrast-enhanced CT is inherently ambiguous: inter-rater disagreement among experts reflects genuine uncertainty rather than annotation noise. Standard deep learning approaches assume a single ground truth, producing probabilistic outputs that can be poorly calibrated and difficult to interpret under such ambiguity. We present TwinTrack, a framework that addresses this gap through post-hoc calibration of ensemble segmentation probabilities to the empirical mean human response (MHR) -the fraction of expert annotators labeling a voxel as tumor. Calibrated probabilities are thus directly interpretable as the expected proportion of annotators assigning the tumor label, explicitly modeling inter-rater disagreement. The proposed post-hoc calibration procedure is simple and requires only a small multi-rater calibration set. It consistently improves calibration metrics over standard approaches when evaluated on the MICCAI 2025 CURVAS-PDACVI multi-rater benchmark.

---


### 145. [Multi-Objective Bayesian Optimization via Adaptive \varepsilon-Constraints Decomposition](https://arxiv.org/abs/2604.15959)

**<font color=#1a73e8>作者：</font>** Yaohong Yang, Sammie Katt, Samuel Kaski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimization (MOBO) provides a principled framework for optimizing expensive black-box functions with multiple objectives. However, existing MOBO methods often struggle with coverage, scalability with respect to the number of objectives, and integrating constraints and preferences. In this work, we propose \textit{STAGE-BO, Sequential Targeting Adaptive Gap-Filling $\varepsilon$-Constraint Bayesian Optimization}, that explicitly targets under-explored regions of the Pareto front. By analyzing the coverage of the approximate Pareto front, our method identifies the largest geometric gaps. These gaps are then used as constraints, which transforms the problem into a sequence of inequality-constrained subproblems, efficiently solved via constrained expected improvement acquisition. Our approach provides a uniform Pareto coverage without hypervolume computation and naturally applies to constrained and preference-based settings. Experiments on synthetic and real-world benchmarks demonstrate superior coverage and competitive hypervolume performance against state-of-the-art baselines.

---


### 146. [Evaluating quality in synthetic data generation for large tabular health datasets](https://arxiv.org/abs/2604.15961)

**<font color=#1a73e8>作者：</font>** Jean-Baptiste Escudié, Benjamin Barnes, Stefan Meisegeier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is no consensus in the field of synthetic data on concise metrics for quality evaluations or benchmarks on large health datasets, such as historical epidemiological data. This study presents an evaluation of seven recent models from major machine learning families. The models were evaluated using four different datasets, each with a distinct scale. To ensure a fair comparison, we systematically tuned the hyperparameters of each model for each dataset. We propose a methodology for evaluating the fidelity of synthesized joint distributions, aligning metrics with visualization on a single plot. This method is applicable to any dataset and is complemented by a domain-specific analysis of the German Cancer Registries' epidemiological dataset. The analysis reveals the challenges models face in strictly adhering to the medical domain. We hope this approach will serve as a foundational framework for guiding the selection of synthesizers and remain accessible to all stakeholders involved in releasing synthetic datasets.

---


### 147. [Stochastic wage suppression on gig platforms and how to organize against it](https://arxiv.org/abs/2604.15962)

**<font color=#1a73e8>作者：</font>** Ana-Andreea Stoica, Celestine Mendler-Duenner, Moritz Hardt  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital labor platforms are increasingly used to procure human input, ranging from annotating data and red-teaming AI models, to ride-sharing and food delivery. A central concern in such markets is the ability of platforms to suppress wages by exploiting the abundance of low-cost labor. To study this exploitation pattern, we introduce a novel posted-price procurement model with coverage objectives. A platform seeks to complete M tasks by posting prices to sequentially arriving workers, each of whom accepts a task if it exceeds their private cost. First, we show that under natural assumptions on the workers' estimated cost, there exists a simple pricing strategy for the platform to cover all M tasks with wait time O(M), while paying only a O(log(M)/M) fraction of the total cost of labor. This result highlights how platforms can exploit workers' uncertainty about the cost of labor to effectively suppress wages. Then, we study collective action as a lever to increase wages and promote welfare in digital labor markets. In particular, we show how a small coalition of targeted low-cost workers who commit to a price floor forces the platform's total spending from logarithmic to linear in M. In contrast, a randomly sampled coalition of equal size remains largely ineffective. We complement our theory with synthetic experiments, showcasing the benefits of collective action across different market regimes.

---


### 148. [TwoHamsters: Benchmarking Multi-Concept Compositional Unsafety in Text-to-Image Models](https://arxiv.org/abs/2604.15967)

**<font color=#1a73e8>作者：</font>** Chaoshuo Zhang, Yibo Liang, Mengke Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable synthesis capabilities of text-to-image (T2I) models, safeguarding them against content violations remains a persistent challenge. Existing safety alignments primarily focus on explicit malicious concepts, often overlooking the subtle yet critical risks of compositional semantics. To address this oversight, we identify and formalize a novel vulnerability: Multi-Concept Compositional Unsafety (MCCU), where unsafe semantics stem from the implicit associations of individually benign concepts. Based on this formulation, we introduce TwoHamsters, a comprehensive benchmark comprising 17.5k prompts curated to probe MCCU vulnerabilities. Through a rigorous evaluation of 10 state-of-the-art models and 16 defense mechanisms, our analysis yields 8 pivotal insights. In particular, we demonstrate that current T2I models and defense mechanisms face severe MCCU risks: on TwoHamsters, FLUX achieves an MCCU generation success rate of 99.52%, while LLaVA-Guard only attains a recall of 41.06%, highlighting a critical limitation of the current paradigm for managing hazardous compositional generation.

---


### 149. [Weak-Link Optimization for Multi-Agent Reasoning and Collaboration](https://arxiv.org/abs/2604.15972)

**<font color=#1a73e8>作者：</font>** Haoyu Bian, Chaoning Zhang, Jiaquan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven multi-agent frameworks address complex reasoning tasks through multi-role collaboration. However, existing approaches often suffer from reasoning instability, where individual agent errors are amplified through collaboration, undermining overall performance. Current research mainly focuses on enhancing high-capability agents or suppressing unreliable outputs to improve framework effectiveness, while systematic identification and reinforcement of performance-limiting agents receive less attention. To address this gap, we propose WORC, a \underline{w}eak-link \underline{o}ptimization framework for multi-agent \underline{r}easoning and \underline{c}ollaboration, grounded in the weak-link principle. WORC follows a two-stage workflow. In the weak agent localization stage, task features are constructed, and a meta-learning-based weight predictor trained on optimal configurations identified by swarm intelligence algorithms (SIAs) enables zero-shot mapping from these features to agent performance weights, where the agent with the lowest predicted weight is identified as the weak agent. In the weak-link optimization stage, an uncertainty-driven allocation strategy assigns additional reasoning budgets to weak agents, with lower predicted weights leading to larger repeated-sampling quotas to compensate for reliability deficiencies. Experimental results show that WORC achieves an average accuracy of 82.2\% on reasoning benchmarks while improving framework stability and cross-architecture generalization, suggesting that compensating for weak links, rather than reinforcing strengths alone, enhances the robustness of multi-agent systems.

---


### 150. [Impact of Nonlinear Power Amplifier on Massive MIMO: Machine Learning Prediction Under Realistic Radio Channel](https://arxiv.org/abs/2604.15977)

**<font color=#1a73e8>作者：</font>** Marcin Hoffmann, Paweł Kryszkiewicz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> M-MIMO is one of the crucial technologies for increasing spectral and energy efficiency of wireless networks. Most of the current works assume that M-MIMO arrays are equipped with a linear front end. However, ongoing efforts to make wireless networks more energy-efficient push the hardware to the limits, where its nonlinear behavior appears. This is especially a common problem for the multicarrier systems, e.g., OFDM used in 4G, 5G, and possibly also in 6G, which is characterized by a high Peak-to-Average Power Ratio. While the impact of a nonlinear Power Amplifier (PA) on an OFDM signal is well characterized, it is a relatively new topic for the M-MIMO OFDM systems. Most of the recent works either neglect nonlinear effects or utilize simplified models proper for Rayleigh or LoS radio channel models. In this paper, we first theoretically characterize the nonlinear distortion in the M-MIMO system under commonly used radio channel models. Then, utilizing 3D-Ray Tracing (3D-RT) software, we demonstrate that these models are not very accurate. Instead, we propose two models: a statistical one and an ML-based one using 3D-RT results. The proposed statistical model utilizes the Generalized Extreme Value (GEV) distribution to model Signal to Distortion Ratio (SDR) for victim users, receiving nonlinear distortion, e.g., as interference from neighboring cells. The proposed ML model aims to predict SDR for a scheduled user (receiving nonlinear distortion along with the desired signal), based on the spatial characteristics of the radio channel and the operation point of each PA feeding at the M-MIMO antenna array. The predicted SDR can then be used to perform PA-aware per-user power allocation. The results show about 12% median gain in user throughput achieved by the proposed ML-based power allocation scheme over the state-of-the-art, fixed operating point scheme.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
