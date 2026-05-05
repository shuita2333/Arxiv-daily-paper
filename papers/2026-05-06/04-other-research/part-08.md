# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 351. [DurableUn: Quantization-Induced Recovery Attacks in Machine Unlearning](https://arxiv.org/abs/2605.02196)

**<font color=#1a73e8>作者：</font>** Abdullah Ahmad Khan, Ferdous Sohel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove specified training data to satisfy privacy regulations such as GDPR. However, existing evaluations assume identical precision at unlearning and deployment, overlooking that production LLMs are deployed at low-bit precision. We show that INT4 quantization systematically restores forgotten content even when models pass compliance audits at bfloat16 (BF16), we term this the quantization recovery attack (QRA). We conduct the first systematic study of unlearning robustness under adapter-space INT4 quantization in the NF4+LoRA regime, evaluating seven methods on LLaMA-3-8B-Instruct across TOFU, MUSE-News, and WikiBio-WPU. INT8 is benign; INT4 induces recovery of up to 22x, worsening with dataset difficulty. We identify the FA-RA-Q-INT4 trilemma: no method simultaneously achieves strong forgetting, high utility, and quantization robustness. A dense Pareto sweep reveals a sharp phase transition once robustness is achieved, retaining accuracy collapses regardless of further tuning. To address this, we propose DURABLEUN-SAF (Sharpness-Aware Forgetting), a quantization-aware objective using Straight-Through Estimator gradients through INT4 rounding. DURABLEUN-SAF is the only method to achieve a stable empirical (0.047, {BF16, INT8, INT4})- durability certificate: Q-INT4= 0.043 +- 0.002, cert rate= 3/3, versus SalUn's cert rate= 1/3 at its own published hyperparameters. We call for Q-INT4 to be adopted as a standard evaluation metric alongside FA and RA.

---


### 352. [SlimDiffSR: Toward Lightweight and Efficient Remote Sensing Image Super-Resolution via Diffusion Model Distillation](https://arxiv.org/abs/2605.02198)

**<font color=#1a73e8>作者：</font>** Ce Wang, Zhenyu Hu, Wanjie Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently achieved remarkable performance in image super-resolution (SR), but their high computational cost limits practical deployment in remote sensing applications. To address this issue, we propose SlimDiffSR, a lightweight and efficient diffusion-based framework for real-world remote sensing image super-resolution. Unlike existing single-step diffusion methods that rely on fixed timesteps, we first introduce an uncertainty-guided timestep assignment strategy to construct a stronger single-step teacher model, where reconstruction difficulty is explicitly linked to diffusion timesteps, enabling adaptive generative strength. Building upon this teacher, we further present a structured pruning strategy tailored to remote sensing imagery, which systematically removes redundant semantic modules and replaces standard operations with lightweight designs, including frequency-separable convolution, direction-separable convolution, and a query-driven global aggregation module. These components explicitly exploit the unique characteristics of remote sensing data, such as sparse high-frequency details, strong directional patterns, and long-range spatial dependencies. To enhance knowledge transfer, we incorporate Maximum Mean Discrepancy (MMD) into the distillation process to align feature distributions between the teacher and student models. Extensive experiments on multiple remote sensing benchmarks demonstrate that SlimDiffSR achieves a favorable balance between efficiency and reconstruction quality. In particular, it attains up to $200\times$ inference acceleration and a $20\times$ reduction in model parameters compared with multi-step diffusion models, while achieving competitive perceptual quality and clearly outperforming existing lightweight diffusion baselines in efficiency. The code is available at: this https URL.

---


### 353. [ARGUS: Policy-Adaptive Ad Governance via Evolving Reinforcement with Adversarial Umpiring](https://arxiv.org/abs/2605.02200)

**<font color=#1a73e8>作者：</font>** Deyi Ji, Junyu Lu, Xuanyi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online advertising governance faces significant challenges due to the non-stationary nature of regulatory policies, where emerging mandates (e.g., restrictions on education or aesthetic anxiety) create severe label inconsistencies and reasoning ambiguities in historical datasets. In this paper, we propose ARGUS, a policy-adaptive governance system that enables evolving reinforcement through multi-agent adversarial umpiring. ARGUS addresses the sparsity of new policy data by employing a three-stage framework: (1) Policy Seeding for initial perception; (2) Adversarial Label Rectification, which utilizes a ``Prosecutor-Defender-Umpire'' architecture to resolve conflicts between stale labels and new mandates; and (3) Latent Knowledge Discovery, which employs a tripartite dialectical discussion to unearth sophisticated, ``gray-area'' violations. By leveraging RAG-enhanced policy knowledge and Chain-of-Thought synthesis as dynamic rewards for reinforcement learning, ARGUS synchronizes its reasoning pathways with evolving regulations. Extensive experiments on both industrial and public datasets demonstrate that ARGUS significantly outperforms traditional fine-tuning baselines, achieving superior policy-adaptive learning with minimal gold data.

---


### 354. [Super-resolution of airborne laser scanning point clouds for forest inventory](https://arxiv.org/abs/2605.02201)

**<font color=#1a73e8>作者：</font>** Jinyuan Shao, Sangyoong Park, Chunxi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Airborne Laser Scanning (ALS) can collect point clouds across large areas, enabling large-scale forest inventory. However, ALS point clouds are sparse and noisy, resulting in inaccurate individual-tree-level forest inventory, such as stem localization and tree size estimation. To overcome this problem, we propose a deep learning model, 3D Forest Super Resolution (3DFSR), to simultaneously improve point density and reduce noise for ALS forest point cloud. 3DFSR is a voxel-based CNN with a U-Net architecture. The proposed 3DFSR is evaluated on ALS point clouds collected in both temperate forests in the U.S. and boreal forests in Germany. Experimental results demonstrate that 3DFSR can generate finer point clouds of tree structure than other state-of-the-art point cloud super-resolution algorithms, achieving 0.249 m Chamfer Distance and 2.711 m Hausdorff Distance. Furthermore, to verify the effectiveness of 3DFSR point clouds in forest inventory, we conduct stem detection, DBH measurements, and stem reconstruction on both original ALS point clouds and 3DFSR enhanced point clouds. We find that stem detection and reconstruction algorithms developed for TLS/MLS point clouds can directly work on our 3DFSR point clouds, and DBH can be derived with circle-fitting method. F1 score of stem detection is improved from 0.71 on original ALS point clouds to 0.97 on 3DFSR point clouds; DBH estimation improves from 13.45 cm RMSE using allometric equations to 6.43 cm using circle fitting; comparing to stems reconstruction from MLS point clouds, stem reconstructed from 3DFSR point clouds has 0.170 m of Chamfer Distance and 0.377 m of Hausdorff Distance, and 0.95 R2 volume estimation. Finally, we find that the proposed 3DFSR is applicable to process point densities from 10 to 1700 points/m2; it also can be generalized across data collected from different LiDAR platforms without transfer learning.

---


### 355. [Submodular Benchmark Selection](https://arxiv.org/abs/2605.02209)

**<font color=#1a73e8>作者：</font>** Alexander Smola  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models across many benchmarks is expensive, yet many benchmarks are highly correlated. We formalize the selection of a small, informative subset as submodular maximization under a multivariate Gaussian model. Entropy (log-determinant covariance) and mutual information between selected and remaining benchmarks arise as natural objectives. Both are submodular; entropy selection coincides with pivoted Cholesky and has spectral residual bounds, while mutual information is non-monotone in general but empirically monotone for small subsets, so we optimize it greedily. Experiments on three matrices from ten public leaderboards show that mutual information selection outperforms entropy for imputation at small subsets.

---


### 356. [NTIRE 2026 Challenge on Efficient Low Light Image Enhancement: Methods and Results](https://arxiv.org/abs/2605.02212)

**<font color=#1a73e8>作者：</font>** Jiebin Yan, Chenyu Tu, Weixia Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive review of the NITRE 2026 Efficient Low Light Image Enhancement (E-LLIE) Challenge, highlighting the proposed solutions and final outcomes. This challenge focuses on mobile image enhancement under low-light conditions, aiming to design lightweight networks that improve enhancement quality while ensuring practical deployability under limited computational resources. A total of 207 participants registered, 27 teams submitted valid entries, and 17 teams ultimately provided valid factsheet. Based on these submissions, this paper provides a systematic evaluation of recent methods for E-LLIE, offering a comprehensive overview of state-of-the-art progress and demonstrating significant improvements in both performance and efficiency.

---


### 357. [InfiltrNet: Dual-Branch CNN-Transformer Architecture for Brain Tumor Infiltration Risk Prediction](https://arxiv.org/abs/2605.02230)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Shruti Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gliomas are aggressive brain tumors that infiltrate surrounding tissue beyond the visible tumor margins observed on Magnetic Resonance Imaging (MRI). Predicting the spatial extent of this infiltration is essential for surgical planning and radiation therapy, yet existing deep learning approaches focus on segmenting the visible tumor rather than estimating infiltration risk in the surrounding tissue. This paper presents InfiltrNet, a novel dual-branch architecture that combines a convolutional neural network (CNN) encoder with a Swin Transformer encoder through cross-attention fusion modules to predict three-zone infiltration risk maps from multimodal MRI. A label generation strategy based on distance transforms is proposed to derive reproducible infiltration risk zones from standard Brain Tumor Segmentation (BraTS) annotations. InfiltrNet is trained with a combined Dice-CrossEntropy and boundary-aware loss augmented by auxiliary supervision heads at intermediate decoder levels. Extensive experiments on BraTS 2020 and BraTS 2025 demonstrate that InfiltrNet outperforms five established baselines. Explainability analysis using GradCAM++ and Occlusion sensitivity confirms that the model attends to clinically relevant peritumoral regions.

---


### 358. [Bucketing the Good Apples: A Method for Diagnosing and Improving Causal Abstraction](https://arxiv.org/abs/2605.02234)

**<font color=#1a73e8>作者：</font>** Li Puyin, Jiyuan Tan, Ahmad Jabbar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a method for diagnosing interpretation in neural networks by identifying an input subspace where a proposed interpretation is highly faithful. Our method is particularly useful for causal-abstraction-style interpretability, where a high-level causal hypothesis is evaluated by interchange interventions. Rather than treating interchange intervention accuracy as a single global summary, we refine this framework by partitioning the input space into well-interpreted and under-interpreted regions according to pairwise interchange-intervention behavior. This turns causal abstraction from a purely global evaluation into a more diagnostic tool: it not only measures whether an interpretation works, but also reveals where it works, where it fails, and what distinguishes the two cases. This diagnostic view also provides practical heuristics for improving interpretations. By analyzing the structure of the well-interpreted and under-interpreted regions, we can identify missing distinctions in a high-level hypothesis, discover previously unmodeled intermediate variables, and combine complementary partial interpretations into a stronger one. We instantiate this idea as a simple four-step recipe and show that it yields informative error analyses across multiple causal abstraction settings. In a toy logic task, recursively applying the recipe recovers a high-level hypothesis from scratch. More broadly, our results suggest that partitioning the input space is a useful step toward more precise, constructive, and scalable mechanistic interpretability.

---


### 359. [Demographic-Aware Transfer Learning for Sleep Stage Classification in Clinical Polysomnography](https://arxiv.org/abs/2605.02245)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Shruti Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated sleep stage classification typically employs a single population-agnostic model, disregarding established demographic variations in sleep architecture. Sleep patterns, however, differ substantially across gender, age, and obstructive sleep apnea (OSA) severity, indicating that a onesize-fits all approach may be suboptimal for diverse clinical populations. In this paper, we propose a two stage training strategy based on demographic stratification and transfer learning framework. We first pretrains a convolutional recurrent model on the full population and then fine tunes it independently for demographic subgroups defined by gender, age, and Apnea-Hypopnea Index (AHI) severity according to the AASM clinical standard. Using the DREAMT dataset comprising 100 clinical subjects and 7 PSG channels, we evaluate 37 fine-tuned configurations across single-axis and two-way demographic combinations. Results demonstrate that 35 of the 37 fine-tuned models outperform the baseline, with Cohen's kappa improvements ranging from 0.9 to 12.9%. These findings indicate that stratified fine tuning tailored to specific patient demographics yields substantially more accurate sleep staging than a single generalized model, offering a practical and clinically grounded paradigm for personalized sleep assessment.

---


### 360. [A Study of Belief Revision Postulates in Multi-Agent Systems (Extended Version)](https://arxiv.org/abs/2605.02249)

**<font color=#1a73e8>作者：</font>** Michael Thielscher, Tran Cao Son  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate the belief revision problem in epistemic planning, i.e., what will be the beliefs of all agents in a multi-agent system after an agent gains the belief in some state property. Based on the standard representation in epistemic planning of agents' beliefs via a single multi-agent Kripke model, we generalize the classical AGM belief revision postulates to the multi-agent setting, with the aim to provide a formal framework for evaluating dynamic epistemic reasoning frameworks in which the beliefs of all agents as the result of actions are computed. As an example of a simple operator that satisfies all of the generalized AGM postulates, we present generalized full-meet multi-agent belief revision. We moreover define a generalization of the standard postulates for iterated revision, present a more sophisticated, event model based revision operator, and discuss the potential issues in defining an epistemic operator on Kripke models that can satisfy all of the generalized postulates for iterated multi-agent belief revision.

---


### 361. [An Information-theoretic Propagation Denoising and Fusion Framework for Fake News Detection](https://arxiv.org/abs/2605.02259)

**<font color=#1a73e8>作者：</font>** Mengyang Chen, Lingwei Wei, Wei Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Incomplete propagation data significantly hinders robust fake news detection. Recent approaches leverage large language models to simulate missing user interactions via role-playing, thereby enriching propagation with synthetic signals. However, such propagation data is intrinsically unreliable, and directly fusing it can lead to biased representations, leading to limited detection performance. In this paper, we alleviate the unreliability of synthetic propagation from the mutual information perspective and propose a novel information-theoretic propagation denoising and fusion (InfoPDF) framework to learn effective representations from both real and synthetic propagation. Specifically, we first generate attribute-specific synthetic propagation using large language models. Then we model each synthetic propagation graph as a probabilistic latent distribution to guide reliability-aware adaptive fusion with real propagation. During training, we design a mutual information-based objective to learn compressed and task-sufficient propagation representations. It jointly suppresses noisy signals across attribute-specific synthetic propagation, maintains consistency between real and synthetic propagation representations, and ensures task sufficiency for fake news detection and attribute prediction. Experiments on three real-world datasets show that InfoPDF consistently achieves superior performance across various fake news detection tasks. Further analysis demonstrates that InfoPDF can estimate attribute-level reliabilities and learn more discriminative propagation representations.

---


### 362. [WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization](https://arxiv.org/abs/2605.02262)

**<font color=#1a73e8>作者：</font>** Wei Tao, Xiaoyang Qu, Peiqiang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, video language models (VLMs) have been applied in various fields. However, the visual token sequence of the VLM is too long, which may cause intolerant inference latency and GPU memory usage. Existing methods propose mixed-precision quantization to the key-value (KV) cache in VLMs based on token granularity, which is time-consuming in the search process and hardware inefficient during computation. This paper introduces a novel approach called WindowQuant, which employs window-adaptive mixed-precision quantization to optimize the KV cache. WindowQuant consists of two modules: window-level quantization search and window-level KV cache computation. Window-level quantization search quickly determines the optimal bit-width configuration of the KV cache windows based on the similarity scores between the corresponding visual token windows and the text prompt, maintaining the model accuracy. Furthermore, window-level KV cache computation reorders the KV cache windows before quantization, avoiding the hardware inefficiency caused by mixed-precision quantization in inference computation. Extensive experiments demonstrate that WindowQuant outperforms state-of-the-art VLM models and KV cache quantization methods on various datasets.

---


### 363. [Reliability-Oriented Multilingual Orthopedic Diagnosis: A Domain-Adaptive Modeling and a Conceptual Validation Framework](https://arxiv.org/abs/2605.02266)

**<font color=#1a73e8>作者：</font>** Danish Ali, Li Xiaojian, Sundas Iqbal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly proposed for clinical decision support including multilingual diagnosis in low-resource settings. However, their reliability, calibration and safety characteristics remain insufficiently understood for structured, high-risk tasks. We present a system-level analysis of multilingual orthopedic diagnosis from free-text clinical notes in English, Hindi and Punjabi. We evaluate three modeling regimes: (i) task-aligned multilingual transformer encoders, (ii) a task-fine-tuned baseline (DistilBERT), and (iii) a domain-adaptive architecture tailored to orthopedic text (IndicBERT-HPA). These models are compared with zero-shot, instruction-tuned LLMs to assess suitability for structured diagnostic classification. Results indicate that while LLMs exhibit strong linguistic fluency, they show unstable calibration and reduced reliability under structured multilingual conditions, particularly in low-resource languages. These findings are specific to zero-shot evaluation and do not imply limitations of fine-tuned models. Domain-adaptive specialization substantially improves cross-lingual discrimination and confidence behavior. IndicBERT-HPA, with language-specific orthopedic adapter heads achieves consistently strong performance across six diagnostic categories and more predictable deployment characteristics than task-only adaptation. Building on these observations, we outline a conceptual deterministic agent-based validation framework for future implementation, formalizing evidence checks, language-sensitive validation and conservative human-in-the-loop gating. Reliable multilingual clinical decision support requires specialized architecture, explicit reliability analysis, and structured validation for safety-critical systems.

---


### 364. [A Systematic Benchmark of Machine Transliteration Models for the Tajik-Farsi Language Pair: A Comparative Study from Rule-Based to Transformer Architectures](https://arxiv.org/abs/2605.02270)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the first comprehensive comparative analysis of modern machine learning architectures for transliteration between Tajik (Cyrillic script) and Persian (Arabic script). A key contribution is the creation and validation of a unique parallel corpus aggregated from multiple heterogeneous sources, including crowdsourced projects, lexicographic pairs, parallel texts of "Shahnameh", diplomatic articles, texts of "Masnavi-i Ma'navi", official terminology lists, and transliterated correspondences. The initial dataset comprised 328,253 sentence pairs; a representative subset of 40,000 pairs was formed using stratified random sampling.
The experiment compared six classes of models: rule-based baseline, LSTM with attention, character-level Transformer, G2P Transformer (trained from scratch), pre-trained multilingual models (mBART, mT5 with LoRA), and byte-level ByT5. Results demonstrate the overwhelming superiority of ByT5 (chrF++ 87.4 for Tajik to Farsi, 80.1 for reverse). The G2P Transformer significantly outperformed mBART (72.3 vs. 62.2 chrF++) despite limited data. Models using subword tokenization (mT5) failed completely (chrF++ less than 18.5).
The findings demonstrate that for accurate transliteration of the Tajik-Farsi pair, architectures operating at the byte or character level are unequivocally more effective than traditional multilingual Seq2Seq models relying on subword tokenization.

---


### 365. [EdgeLPR: On the Deep Neural Network trade-off between Precision and Performance in LiDAR Place Recognition](https://arxiv.org/abs/2605.02275)

**<font color=#1a73e8>作者：</font>** Pierpaolo Serio, Hetian Wang, Zixiang Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Place recognition is essential for long-term autonomous navigation, enabling loop closure and consistent mapping. Although deep learning has improved performance, deploying such models on resource-constrained platforms remains challenging. This work explores efficient LiDAR-based place recognition for EdgeAI by leveraging Bird's Eye View representations to enable lightweight image-based networks. We benchmark representative architectures without aggregation heads using a unified descriptor scheme based on global pooling and linear projection, and evaluate performance under FP32, FP16, and INT8 quantization. Experiments reveal trade-offs between accuracy, robustness, and efficiency: FP16 matches FP32 with lower cost, while INT8 introduces architecture-dependent degradation. Overall, the presented results are a strong basis for future research on 'use-case'-aware quantisation of Neural Networks for Edge deployment.

---


### 366. [Post-Quantum Cryptography Migration in Australian Real-Time Payment Infrastructure: A Monte Carlo Simulation Study of the New Payments Platform](https://arxiv.org/abs/2605.02276)

**<font color=#1a73e8>作者：</font>** Nazmus Salehin Sammo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Australia's New Payments Platform (NPP) processes 5.2 million real-time transactions per day under a 2,000 ms SLA. With cryptographically relevant quantum computers projected by 2030-2035 and the Harvest Now, Decrypt Later (HNDL) threat active, this paper presents a Monte Carlo simulation study of NIST FIPS 204/205/206 signature standards (ML-DSA, SLH-DSA/SPHINCS+, Falcon) in Australian payment infrastructure, jointly modelling M/M/c queue saturation, GEV tail bounds, and HNDL actuarial exposure across 1,000 seasonally-mixed simulation days (80 million events). Cross-platform validation used liboqs 0.15.0 on a seven-node multi-cloud testbed spanning four microarchitectures (Intel Xeon Ice Lake/Cascade Lake, AMD EPYC Milan, ARM Graviton3).
ML-DSA and Falcon achieve 100% SLA compliance across all configurations; worst-case NPP p99 overhead is 1.57 ms (ML-DSA-87, 0.079% of SLA budget). We introduce the Crypto Dilution Index (CDI = delta-p99/p99_e2e), showing all non-SPHINCS+ algorithms achieve CDI < 0.04. GEV analysis yields p99.9 bounds below 154 ms (95% CI). Falcon-512 is the only NIST PQC signature fitting within the 2,048-byte SWIFT MT field limit (1,563 bytes combined).
SPHINCS+ saturates HSM queues at NPP volumes (rho=1.8855, c=2 servers), achieving 0% NPP SLA compliance, characterised as a DoS amplification surface in hybrid deployments (utilisation ratio ~9,428x ECDSA). An HNDL actuarial model estimates 9.56 billion NPP records at risk under CRQC-2030. Migration costs peak at USD 21.4M in 2026, declining to USD 1.5M/year by 2028.

---


### 367. [Compositional Multi-hop Factual Error Correction via Decomposition-and-Injection](https://arxiv.org/abs/2605.02277)

**<font color=#1a73e8>作者：</font>** Lei Zhu, Xiaobao Wang, Jianbiao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual Error Correction (FEC) aims to revise inaccurate text into statements that are factually consistent with external evidence. Although recent methods perform well on single-hop correction, they often treat claims as atomic units and struggle with multi-hop cases that require compositional reasoning across multiple evidence sources. This challenge is further amplified by limited paired data and difficulties in locating semantic errors within complex reasoning chains. We present CECoR (Compositional Error Correction via Reasoning-aware Synthesis), a reasoning-aware framework that introduces a Decomposition and Injection paradigm for compositional error correction. CECoR decomposes multi-hop claims into interpretable reasoning steps and injects controlled perturbations to synthesize high-quality training pairs. A two-stage learning strategy combining supervised fine-tuning and reinforcement learning improves factual accuracy and robustness. Comprehensive evaluations show that CECoR achieves strong performance on multi-hop benchmarks, outperforming both distantly supervised methods and few-shot LLM baselines. It also generalizes effectively to single-hop correction and remains stable under noisy evidence, demonstrating its versatility for real-world factual correction.

---


### 368. [HELIX: Hybrid Encoding with Learnable Identity and Cross-dimensional Synthesis for Time Series Imputation](https://arxiv.org/abs/2605.02278)

**<font color=#1a73e8>作者：</font>** Fengming Zhang, Wenjie Du, Huan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series imputation benefits from leveraging cross-feature correlations, yet existing attention-based methods re-discover feature relationships at each layer, lacking persistent anchors to maintain consistent representations. To address this, we propose HELIX, which assigns each feature a learnable feature identity, a persistent embedding that captures intrinsic semantic properties throughout the network. Unlike graph-based methods that rely on predefined topology and assume homogeneous spatial relationships, HELIX learns arbitrary feature dependencies end-to-end from temporal co-variation, naturally handling datasets where features mix spatial locations with semantic variables. Integrated with hybrid temporal-feature attention, HELIX achieves the state-of-the-art performance, surpassing all 16 baselines on 5 public datasets across 21 experimental settings in our evaluation. Furthermore, our mechanistic analysis reveals that HELIX aligns learned feature identities and dependencies with latent physical and semantic structure progressively across layers, demonstrating that it more effectively translates cross-feature structure into imputation accuracy.

---


### 369. [Variational Matrix-Learning Fourier Networks for Parametric Multiphysics Surrogates](https://arxiv.org/abs/2605.02280)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Jianhua Zhang, Liang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiphysics simulation is critical for system-technology co-optimization (STCO) in chiplet-based design, but repeated finite-element solutions of PDE-governed problems are computationally expensive in parametric design exploration. This paper proposes a variational matrix-learning Fourier network (VMLFN) for efficient parametric multiphysics surrogate modeling. VMLFN constructs a log-space sine neural representation with randomly sampled spectral frequencies, frequency-dependent decay regulation, and embedded Dirichlet boundary conditions. With fixed hidden-layer parameters, the output-layer weights are determined by reformulating the governing PDEs into variational weak forms and enforcing the stationarity condition of the resulting energy functional. This converts physics-informed training into a linear matrix-solving problem, requiring only first-order derivatives and avoiding both high-order automatic differentiation and penalty-coefficient tuning. A heuristic frequency-scanning algorithm is further introduced to select a problem-adaptive maximum frequency that covers the dominant spectral range of the target problem. The proposed method is validated on heat conduction, solid mechanics, and Helmholtz wave propagation problems. Results from five benchmark cases demonstrate that VMLFN delivers accurate full-field predictions with substantial speedup over conventional physics-informed neural networks and repeated finite-element simulations.

---


### 370. [Beyond Known Objects: A Novel Framework for Open-Set Object Detection using Negative-Aware Norm](https://arxiv.org/abs/2605.02284)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Yao Lu, Johannes Betz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Set Object Detection (OSOD) is crucial for autonomous driving, where perception systems must recognize and localize both known and previously unseen objects in complex, dynamic environments. While recent approaches deliver promising results, they often require retraining the detector extensively to learn objectness, which describes the likelihood that a bounding box tightly encloses a valid object, regardless of whether its category was learned during training. Deviating from existing work, we hypothesize that standard off-the-shelf detectors may already contain helpful cues for objectness, owing to their training on numerous and diverse known categories. Building on this idea, we propose NAN-SPOT, a training-light framework that does not require to retrain the base object detector and estimates objectness by leveraging a hidden layer metric called Negative-Aware Norm (NAN), requiring only minutes of training on just hundreds of images. To support comprehensive evaluation, we introduce COCO-Open, an expanded version of the existing COCO-Mixed dataset, increasing unknown object annotations from 433 to 1853, making it the most exhaustively labeled dataset for OSOD to the best of our knowledge. Experimental results demonstrate that NAN-SPOT achieves even better performance on unknown object detection than methods requiring heavy training, without compromising performance on known objects. This efficiency and robustness make NAN-SPOT a promising step towards open-world perception in autonomous driving.

---


### 371. [LabBuilder: Protocol-Grounded 3D Layout Generation for Interactable and Safe Laboratory](https://arxiv.org/abs/2605.02288)

**<font color=#1a73e8>作者：</font>** Jianbao Cao, Zhangrui Zhao, Bohan Feng 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated laboratories hold the promise of accelerating scientific discovery, yet their deployment is bottlenecked by the difficulty of designing safe and executable environments. While simulator-based design offers scalability, existing 3D scene generation methods are primarily tailored for household settings, optimizing for visual plausibility while neglecting the rigorous functional semantics and safety constraints essential for scientific experimentation. We present LabBuilder, an end-to-end system that generates and verifies 3D laboratory layouts from concise textual specifications. It operates through three tightly coupled components: LabForge first curates a meta-dataset of annotated assets and chemical knowledge, translating natural language specifications into structured protocols; building on these protocols, LabGen synthesizes laboratory layouts via an iterative, constraint-aware optimization strategy; finally, LabTouchstone evaluates the resulting layouts as a unified benchmark. Extensive experiments demonstrate that LabBuilder significantly outperforms existing state-of-the-art methods, producing laboratory environments that are not only realistic but also functionally valid and safe for complex experimental workflows.

---


### 372. [Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding](https://arxiv.org/abs/2605.02290)

**<font color=#1a73e8>作者：</font>** Taewon Yun, Jisu Shin, Jeonghwan Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling large reasoning models is essential for making Long-CoT reasoning practical, as full-scale inference remains computationally prohibitive. Existing curation-based approaches select complete reasoning traces post-hoc, overlooking collaboration among heterogeneous teachers and lacking dynamic exploration, which leads to redundant sampling and missed complementary reasoning. We introduce CoRD, a collaborative multi-teacher decoding framework that performs step-wise reasoning synthesis guided by predictive perplexity-based scoring and beam search. This enables heterogeneous LRMs to jointly construct coherent reasoning trajectories while efficiently preserving diverse, high-potential hypotheses. Experiments show that CoRD produces higher-quality reasoning data and achieves near teacher-level student performance with fewer, structured supervision signals, without substantial efficiency overhead. CoRD further generalizes well to out-of-domain and open-ended settings. The dataset and model are available at \href{this https URL}{this https URL}.

---


### 373. [A Hybrid Approach for Closing the Sim2real Appearance Gap in Game Engine Synthetic Datasets](https://arxiv.org/abs/2605.02291)

**<font color=#1a73e8>作者：</font>** Stefanos Pasios  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video game engines have been an important source for generating large volumes of visual synthetic datasets for training and evaluating computer vision algorithms that are to be deployed in the real world. While the visual fidelity of modern game engines has been significantly improved with technologies such as ray-tracing, a notable sim2real appearance gap between the synthetic and the real-world images still remains, which limits the utilization of synthetic datasets in real-world applications. In this letter, we investigate the ability of a state-of-the-art image generation and editing diffusion model (FLUX.2-4B Klein) to enhance the photorealism of synthetic datasets and compare its performance against a traditional image-to-image translation model (REGEN). Furthermore, we propose a hybrid approach that combines the strong geometry and material transformations of diffusion-based methods with the distribution-matching capabilities of image-to-image translation techniques. Through experiments, it is demonstrated that REGEN outperforms FLUX.2-4B Klein and that by combining both FLUX.2-4B Klein and REGEN models, better visual realism can be achieved compared to using each model individually, while maintaining semantic consistency. The code is available at: this https URL

---


### 374. [Momentum-Anchored Multi-Scale Fusion Model for Long-Tailed Chest X-Ray Classification](https://arxiv.org/abs/2605.02292)

**<font color=#1a73e8>作者：</font>** Duy Hoang Khuong, Duy Nguyen Huu, Ngu Huynh Cong Viet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray classification suffers from severe class imbalance where gradient updates bias toward majority classes, causing feature drift and poor performance on rare but critical pathologies. We propose a Momentum-Anchored Multi-Scale Fusion Network that uses exponential moving averages (EMA) as a temporal anchoring mechanism to stabilize feature representations under long-tailed distributions. Our approach applies selective momentum updates to the final expansion block of an EfficientNet backbone, creating a slowly-evolving reference branch that resists gradient-induced drift while preserving discriminative patterns for minority classes. Combined with multi-scale spatial fusion ($1\times 1$, $3 \times 3$, $5 \times 5$ convolutions), this anchoring strategy maintains representational stability throughout training. On ChestX-ray14, our method achieves 0.8682 average AUC, outperforming state-of-the-art approaches and showing particular improvements on rare pathologies like Hernia (0.9470) and Pneumonia (0.8165). The results demonstrate that momentum anchoring effectively counters feature instability in long-tailed medical image classification.

---


### 375. [Graph Federated Unlearning for Privacy Preservation](https://arxiv.org/abs/2605.02297)

**<font color=#1a73e8>作者：</font>** Ruotong Ma, Wentao Yu, Qizhou Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph federated learning (GFL) facilitates decentralized training on distributed graph data while keeping sensitive user information local, aligning with policies such as GDPR and CCPA that grant users the right to freely join or withdraw from learning systems. However, even decentralized, user information can persist after quitting, potentially propagating to central servers and then redistributing to malicious clients. This privacy leakage during user withdrawal, despite its importance, has received seldom attention in GFL. To fill the gap, we explore the potential of machine unlearning (MU) to thoroughly remove user information. However, classical MU methods are known to degrade overall performance, a problem that is exacerbated in GFL due to local message passing and global model collaboration. To this end, we make two adjustments to mitigate this challenge for GFL. First, we ensure unlearning updates that minimally affect overall performance, steering them in directions orthogonal to the gradients from learning other data. Second, we introduce virtual clients, maintained by the central server, to preserve graph topology and global embeddings without recovering information of removed entities. We conduct comprehensive experiments under a representative user-withdrawal scenario and propose a novel membership inference framework to rigorously evaluate and validate the reliability of our privacy preservation. The experimental results demonstrate the effectiveness of our approach, which also surpasses the performance of seven state-of-the-art baseline methods.

---


### 376. [A Meta Reinforcement Learning Approach to Goals-Based Wealth Management](https://arxiv.org/abs/2605.02300)

**<font color=#1a73e8>作者：</font>** Sanjiv R. Das, Harshad Khadilkar, Sukrit Mittal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying concepts related to zero-shot meta-learning and pre-training of foundation models, we develop a meta reinforcement learning approach (denoted MetaRL) that is pre-trained on thousands of goals-based wealth management (GBWM) problems. Each GBWM problem involves a multiple year scenario over which the investor looks to optimally choose an investment portfolio each year and choose to fulfill all, some, or none of the different financial goals that arise each year. These choices seek to maximize the expected total investor utility obtained from the fulfilled financial goals. By eliminating separate training and optimization for each new investor problem, the MetaRL model in inference mode produces near-optimal dynamic investment portfolio and goal-fulfilling strategies for a new GBWM problem within a few hundredths of a second. This delivers expected utilities that are, on average, 97.8% of the optimal expected utilities (determined via Dynamic Programming). These results are remarkably robust to capital market regime changes, even when training uses only one capital market regime. Further, the MetaRL approach can enable solving problems with larger state spaces where Dynamic Programming becomes computationally infeasible.

---


### 377. [Structural Dilemmas and Developmental Pathways of Legal Argument Mining in the Era of Artificial Intelligence](https://arxiv.org/abs/2605.02308)

**<font color=#1a73e8>作者：</font>** Xianglei Liao, Chuanyi Li, Kun Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Against the backdrop of rapid advances in artificial intelligence, legal argument mining has emerged as an important research area linking legal texts with intelligent analysis, carrying significant theoretical and practical implications. Existing studies have primarily developed along three dimensions: data, technology, and theory. At the data level, raw legal texts and annotated corpora constitute the foundational resources. At the technological level, research paradigms have evolved from rule-based systems and traditional machine learning to large language models (LLMs). At the theoretical level, argumentation theory and legal dogmatics provide important references for modeling argumentation structures. However, despite ongoing progress, the overall development of legal argument mining remains relatively slow. Building on a systematic review of existing research, this study conducts an in-depth analysis and finds that this is due not only to data scarcity or technical limitations, but more fundamentally to the lack of a structured representational approach that reconciles theoretical expressiveness with computational feasibility. Specifically, this challenge manifests in dilemmas in data standardization, obstacles to effective modeling, and limitations in domain adaptation. In response, the study proposes several key directions for future research. It aims to provide a reframing of key problems and a pathway for future development in legal argument mining, while leaving specific models and implementation schemes for further investigation.

---


### 378. [Differentiable Kernel Ridge Regression for Deep Learning Pipelines](https://arxiv.org/abs/2605.02313)

**<font color=#1a73e8>作者：</font>** Jean-Marc Mercier, Gabriele Santin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks dominate modern machine learning, while alternative function approximators remain comparatively underexplored at scale. In this work, we revisit kernel methods as drop-in components for standard deep learning pipelines. We introduce \emph{Sparse Kernels} (SKs), a differentiable, localized, and lazy variant of kernel ridge regression (KRR) that defers training to inference time and reduces to the solution of small local systems. We integrate SKs into PyTorch as modular layers that preserve end-to-end trainability, and we show that they expose three distinct sets of parameters -- feature representations, target values, and evaluation points -- each of which can be fixed or learned. This decomposition broadens the design space available to practitioners, enabling, in particular, training-free transfer, nonlinear probing, and hybrid kernel-neural models. Across convolutional networks, vision transformers, and reinforcement learning, SK-based modules serve two complementary roles: in some settings, they match the performance of trained neural readouts with substantially less training; in others, they augment existing models and improve their performance when used as additional components. Our results suggest that kernel methods, once made scalable and differentiable, can be readily integrated with deep learning rather than treated as a separate paradigm.

---


### 379. [Open-access model for detecting openly dumped dispersed municipal solid waste from crowdsourced UAV imagery in Sub-Saharan Africa](https://arxiv.org/abs/2605.02316)

**<font color=#1a73e8>作者：</font>** Steffen Knoblauch, Ram Kumar Muthusamy, Luis M. A. Bettencourt 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Managing municipal solid waste in rapidly urbanizing Sub-Saharan Africa remains challenging due to dispersed informal dumping and limited high-resolution datasets for spatial monitoring. We present an open-access deep learning model for automated detection of openly dumped dispersed solid waste via crowdsourced UAV imagery, trained and evaluated across 29 regions in 10 countries, encompassing diverse environmental contexts. A deep learning model trained on manually annotated image tiles achieved excellent performance in detecting openly dumped dispersed solid waste across all study regions. Predicted distributions reveal heterogeneous accumulation patterns, ranging from localized hotspots - often along waterways, where waste can exacerbate flood and public health risks - to more dispersed litter across urban areas. Waste accumulation is most strongly associated with population density and indicators of lack of local infrastructure access, whereas its relationship with broader measures of regional development is weaker, highlighting the importance of fine-scale data for understanding localized waste dynamics. By releasing the model, this study provides a ready-to-use tool for UAV imagery collected by municipalities and local mapping communities, enabling openly dumped dispersed solid waste monitoring without extensive technical expertise. This approach empowers local practitioners to convert UAV imagery into actionable insights, supporting targeted interventions and improved municipal solid waste management across Sub-Saharan Africa.

---


### 380. [Anon: Extrapolating Optimizer Adaptivity Across the Real Spectrum](https://arxiv.org/abs/2605.02317)

**<font color=#1a73e8>作者：</font>** Yiheng Zhang, Kaiyan Zhao, Shaowu Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers such as Adam have achieved great success in training large-scale models like large language models and diffusion models. However, they often generalize worse than non-adaptive methods, such as SGD on classical architectures like CNNs. We identify a key cause of this performance gap: adaptivity in pre-conditioners, which limits the optimizer's ability to adapt to diverse optimization landscapes. To address this, we propose Anon (Adaptivity Non-restricted Optimizer with Novel convergence technique), a novel optimizer with continuously tunable adaptivity in R, allowing it to interpolate between SGD-like and Adam-like behaviors and even extrapolate beyond both. To ensure convergence across the entire adaptivity spectrum, we introduce incremental delay update (IDU), a novel mechanism that is more flexible than AMSGrad's hard max-tracking strategy and enhances robustness to gradient noise. We theoretically establish convergence guarantees under both convex and non-convex settings. Empirically, Anon consistently outperforms state-of-the-art optimizers on representative image classification, diffusion, and language modeling tasks. These results demonstrate that adaptivity can serve as a valuable tunable design principle, and Anon provides the first unified and reliable framework capable of bridging the gap between classical and modern optimizers and surpassing their advantageous properties.

---


### 381. [Can Causal Discovery Algorithms Help in Generating Legal Arguments?](https://arxiv.org/abs/2605.02318)

**<font color=#1a73e8>作者：</font>** Soham Wasmatkar, Subinay Adhikary, Rakshit Rohan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In 2011, Judea Pearl received the Turing Award, considered the Nobel Prize in Computing, for fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning. It includes pioneering the development of causal discovery algorithms. These computer algorithms can analyze large multivariate datasets and automatically discover the causal relationships among the constituent variables. They have been widely used in many critical fields such as medicine and economics to support decisions. However, to our knowledge, they have not been leveraged in law. This paper attempts to alleviate this gap by investigating whether causal discovery algorithms can be leveraged for automated generation of legal arguments. To that end, a novel legal dataset is prepared by identifying 17 legal concepts, such as physical assault and property dispute. A curated collection of 150 homicide cases are annotated with these concepts, e.g., a case is annotated with physical assault only if a physical assault had been reported in that case. Subsequently, a selected set of widely-used causal discovery algorithms is applied to the annotated dataset to discover the causal relationships between the legal concepts. Additionally, the degrees of belief associated with the discovered relationships are quantified in mathematical probabilities. It is shown that some of the causal relationships help generate viable legal arguments, e.g., if one could establish that a physical assault has not taken place during a homicide, it should be a sufficient condition (with probability 1) to establish that the homicide has not been committed due to a property-related dispute. Thus, this paper shows that causal discovery algorithms can be helpful in generating legal arguments, opening up avenues for promising future endeavors.

---


### 382. [Optimal Privacy-Utility Trade-Offs in LDP: Functional and Geometric Perspectives](https://arxiv.org/abs/2605.02319)

**<font color=#1a73e8>作者：</font>** Seung-Hyun Nam, Hyun-Young Park, Si-Hyeon Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Local differential privacy (LDP) has emerged as a gold-standard framework for privacy-preserving data analysis. However, characterizing the optimal privacy-utility trade-off (PUT) and the corresponding optimal LDP channels remains largely fragmented, relying on problem-specific, case-by-case analyses. In this work, we develop a unified theoretical framework that systematically characterizes the optimal PUT and optimal LDP channels for general privacy-preserving statistical decision-making problems. We first identify key functional properties of Bayesian and minimax risks as functions of the LDP channel, including the data processing inequality (DPI), direct-sum quasi-convexity (or additivity), concavity, and symmetry invariance. Leveraging these properties, we reduce the optimization domain required to compute the optimal PUT. Additionally, building on convex geometric insights, we establish a one-to-one correspondence between maximal LDP channels under the Blackwell order and a finite-dimensional polytope, yielding an exact geometric characterization. This result renders the optimal PUT computationally tractable via vertex enumeration or linear programming. Furthermore, when the underlying problem exhibits symmetries characterized by a transitive group action, we derive an exact analytic expression for the optimal PUT, leading to closed-form solutions without numerical optimization. Our framework applies broadly beyond risk minimization, encompassing the maximization of information-theoretic measures such as mutual information, $f$-divergences, and Fisher information over LDP channels. We demonstrate the efficacy of our theoretical framework by recovering or strengthening several known results, and deriving exact analytic expressions for the optimal PUTs in specific tasks that were previously unaddressed.

---


### 383. [ANO: A Principled Approach to Robust Policy Optimization](https://arxiv.org/abs/2605.02320)

**<font color=#1a73e8>作者：</font>** Yiheng Zhang, Yiming Wang, Kaiyan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) dominates deep RL but faces a fundamental dilemma. Its "hard clipping" mechanism discards valuable gradient information from outliers, leading to sample inefficiency. Conversely, removing clipping (as in SPO) exposes optimization to unbounded gradients, causing significant instability and hyperparameter sensitivity. To resolve this, we establish a Unified Trust Region Framework that generalizes existing objectives. Within this framework, we derive Anchored Neighborhood Optimization (ANO) based on a set of design principles. We identify that the failure of standard policy gradients stems from a misapplication of gradient influence on outliers. We propose the Redescending Influence Principle, a paradigm shift from monotonic penalties (SPO) and hard-thresholding (PPO) to dynamic outlier suppression, and prove its necessity for stability in high-variance stochastic optimization. Theoretically, we prove ANO possesses the minimal structural complexity required for robust optimization. Empirically, ANO achieves state-of-the-art performance on MuJoCo benchmarks, significantly outperforming PPO and SPO. Notably, ANO demonstrates superior stability, preventing policy collapse even under aggressive hyperparameters (e.g., learning rates 3x larger than standard) where PPO fails completely.

---


### 384. [When Attention Collapses: Residual Evidence Modeling for Compositional Inference](https://arxiv.org/abs/2605.02323)

**<font color=#1a73e8>作者：</font>** Niklas Houba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional inference - the decomposition of observations into an unknown number of latent components - is central to perception and scientific data analysis. Attention-based models perform well when components are approximately separable, as in object-centric vision. Under additive superposition, however - where multiple components contribute to every observation - we identify a structural failure mode we term slot collapse: multiple slots converge to the same dominant component while weaker ones remain unrepresented. We trace this to a general limitation: attention is memoryless with respect to explained evidence. All slots repeatedly operate on the same input without accounting for what has already been explained, so gradients are dominated by the strongest component, inducing shared fixed points across slots. As a result, attention fails to enforce non-redundant allocation under additive superposition. We address this by introducing residual evidence modeling, instantiated via evidence depletion - a minimal modification combining multiplicative depletion with an attention bias. Controlled ablations show that parallel attention, sequential processing alone, and loss-based regularization fail to resolve collapse; evidence depletion, which adds residual state to sequential attention, consistently succeeds. Across synthetic benchmarks and real-world audio mixtures (FUSS), evidence depletion reduces slot collapse by up to an order of magnitude, generalizing beyond synthetic settings. On gravitational-wave source inference for the ESA/NASA LISA mission, under identical architectures, data, and losses, standard attention fails while evidence depletion prevents collapse and enables multi-source posterior estimation. These results show that under additive superposition, residual evidence tracking is the operative ingredient for preventing collapse and enabling compositional inference.

---


### 385. [Improving Imbalanced Multi-Label Chest X-Ray Diagnosis via CBAM-Enhanced CNN Backbones](https://arxiv.org/abs/2605.02328)

**<font color=#1a73e8>作者：</font>** Duy Nguyen Huu, Duy Hoang Khuong, Ngu Huynh Cong Viet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest radiography is a widely used imaging modality for thoracic disease diagnosis, yet its conventional interpretation remains time-consuming and heavily dependent on expert knowledge. While deep learning has improved diagnostic efficiency through automated feature extraction, challenges such as class imbalance and the localization of multiple co-existing pathologies remain unsolved. In this paper, inspired by the strength of Convolutional Block Attention Module (CBAM) in feature refinement and the capability of CNN blocks in feature extraction, we propose a strategy to integrate CBAM into traditional CNN blocks to enhance performance in multi-label classification tasks. Our method achieves a mean AUC of 0.8695 on ChestXray14 dataset, outperforming several state-of-the-art this http URL source code is available at: this https URL

---


### 386. [A Near-optimal SQ Lower Bound for Smoothed Agnostic Learning of Boolean Halfspaces](https://arxiv.org/abs/2605.02350)

**<font color=#1a73e8>作者：</font>** Tim Sinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the complexity of smoothed agnostic learning of halfspaces on $\{\pm 1\}^n$ under the uniform distribution in the model of \citet{KM25} where each input coordinate is independently flipped with probability $\sigma \in (0, {1}/{2})$. We show that $L^1$ polynomial regression achieves complexity $\tilde{O}(n^{O(\log(1/\varepsilon)/\sigma)})$, and prove a nearly matching Statistical Query complexity lower bound of $n^{\Omega(\log(1+\sigma/\varepsilon ^2)/\sigma)}$. This complements the recent work of \citet{DK26}, which established analogous bounds in the continuous setting under Gaussian marginals.

---


### 387. [ZNO: Stable Rational Neural Operators in the Z-Domain for Discrete-Time Dynamic](https://arxiv.org/abs/2605.02356)

**<font color=#1a73e8>作者：</font>** Xianli Zhu, Jia Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Z-Domain Neural Operator (ZNO), a causal neural operator whose layers are stable low-rank multiple-input multiple-output (MIMO) rational filters parameterized directly in the $z$-plane. ZNO addresses a limitation of existing operator learning methods, many of which are primarily tailored for continuous-time problems, while a large class of system-identification problems is intrinsically discrete-time. The $z$-domain form expresses stability as a unit-disk pole constraint and makes learned discrete-time poles directly readable. The model combines low-rank channel mixing, smooth stable pole reparameterization, causal recurrence, and an optional short finite impulse response (FIR) branch in a single $z$-domain rational recurrent layer. Across controlled discrete system-identification experiments, ZNO's advantage is most evident when the target dynamics are stable rational systems with lightly damped poles near the unit circle. Under matched parameter budgets, ZNO is not uniformly dominant; however, with validation-selected configurations, the same architecture can achieve the lowest mean error across the controlled tasks. A five-bin difficulty sweep over near-unit-circle / long-memory dynamics shows that ZNO has the lowest mean error across memory regimes, from short (approximately 10 steps) to long (approximately 100-200 steps). On five public nonlinear system-identification benchmarks, ZNO is competitive with neural operator and state-space baselines, achieving the lowest mean error on benchmarks whose dynamics align with stable rational discrete-time filters, while classical or state-space baselines remain preferable on some systems. These results position ZNO as a strong model for stable rational discrete-time dynamics, especially in near-unit-circle and long-memory regimes, but not as a universal replacement for specialized system-identification methods.

---


### 388. [Channel-Level Relation to Attentive Aggregation with Neighborhood-Homogeneity Constraint for Point Cloud Analysis](https://arxiv.org/abs/2605.02357)

**<font color=#1a73e8>作者：</font>** Jiaqi Shi, Jin Xiao, Xiaoguang Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In 3D point cloud understanding, the core challenge lies in accurately capturing discriminative features within complex neighborhoods, which directly affects the execution precision of downstream tasks such as embodied AI and autonomous driving. Existing methods explore feature correlation discrimination but are limited to point-level spatial distribution or channel responses, enabling only coarse-grained level evaluation. For modern multi-scale point cloud networks, such coarse-grained metrics inevitably incur significant information loss in deeper layers. To address this issue, we propose a novel network equipped with a channel-level metric-based enhancement mechanism, termed the PointCRA network. Our core idea is to introduce temporal trend variation as a new evaluation dimension to avoid the information loss caused by weight dimension collapse in existing spatial and channel attention mechanisms. On this basis, we construct a multi-level calibration framework guided by neighborhood homogeneity for weight calibration, and design a dedicated loss function to enhance channel discriminability. The module effectively leverages the intrinsic feature priors of deep networks to adaptively correct the feature aggregation process, offering strong interpretability with low parameter overhead. Furthermore, our proposed method exhibits strong transferability, interpretability, and parameter efficiency. We validate the proposed method effectiveness on diverse datasets and benchmark models, and further demonstrate its rationality through extensive analytical experiments. Our PointCRA achieves 77.5% mIoU on the S3DIS dataset, 90.4% OA on the ScanObjectNN dataset, and 87.4% instance mIoU on the ShapeNetPart dataset. The code and pretrained weights are publicly available on GitHub:

---


### 389. [Predicting Post Virality with Temporal Cross-Attention over Trend Signals](https://arxiv.org/abs/2605.02358)

**<font color=#1a73e8>作者：</font>** Sarvagya Somvanshi, Mohan Xu, Rakhi Chadalavada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current models for predicting social media virality rely heavily on static textual and structural features, effectively ignoring the highly dynamic nature of trend signals. We study whether real-world attention signals can improve the prediction of social-media virality beyond what post text alone reveals. We introduce \model{}, an architecture that predicts Reddit post virality by fusing internal platform representations with exogenous temporal signals derived from Wikipedia pageview spikes. We frame virality as a binary classification task that accounts for differences in subreddit scale, labeling posts as viral if they exceed the 90th percentile of per-subreddit engagement and a minimum absolute score threshold.
We introduce ViralityNET combines four post-level streams: title embeddings, body embeddings, structural metadata, and learned subreddit embeddings with a cross-attention block that queries a daily sliding-window trends matrix encoding the top-512 Wikipedia spike terms from the preceding seven days. Empirical results suggest that incorporating external attention signals yields consistent gains, outperforming text-only baselines by +0.015 AUC-PR and achieving an overall AUC-ROC of 0.836. Overall, we provide evidence that incorporating external attention signals yields measurable improvements over text-only baselines, highlighting the importance of real-world dynamics in shaping online virality.

---


### 390. [A Compound AI Agent for Conversational Grant Discovery](https://arxiv.org/abs/2605.02366)

**<font color=#1a73e8>作者：</font>** Zhisheng Tang, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research funding discovery remains fundamentally fragmented: researchers navigate disparate agency portals (e.g., in the United States, NSF, NIH, DARPA, this http URL, and many others) with heterogeneous interfaces, search capabilities, and data schemas. We present a compound AI system that unifies this landscape through two tightly coupled components: (1) an aggregation layer that autonomously collects, normalizes, and indexes almost 12,000 federal and nonprofit opportunities from fragmented sources via LLM-equipped browser agents, maintaining a biweekly-updated unified database; and (2) an agentic ReAct-based query processing layer that interprets research context (including from PDF documents) and employs hybrid search combining a structured index with selective web search to retrieve relevant opportunities - while avoiding LLM hallucination. The conversational interface supports iterative refinement through multi-turn interactions, allowing researchers to progressively apply constraints without reformulating their core research description. Results stream in real time with full transparency of intermediate reasoning, enabling appropriate calibration of user trust. Currently used by almost 3,000+ users, our approach demonstrates the feasibility of compound AI in reducing grant discovery time from 30--45 minutes (manual, fragmented portal searches) to under 10 minutes (unified, conversational search).

---


### 391. [Privacy Preserving Machine Learning Workflow: from Anonymization to Personalized Differential Privacy Budgets in Federated Learning](https://arxiv.org/abs/2605.02372)

**<font color=#1a73e8>作者：</font>** Judith Sáinz-Pardo Díaz, Álvaro López García  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing development of artificial intelligence based solutions, together with privacy legislation, has driven the rise of the so-called privacy preserving machine learning architectures, such as federated learning. While federated learning enables model training on decentralized data preventing their sharing and centralization, it still faces several challenges related to data integrity and privacy. This paper presents a comprehensive privacy preserving federated learning workflow for sensitive tabular data, including anonymization and differential privacy techniques. We also introduce a formal definition for the concept of client drift, together with ways of detecting it to mitigate poisoning attacks. Then, we detail a complete methodology for assigning personalized privacy budgets for global differential privacy to the different clients participating in the network, based on a re-identification risk metric. The proposed methodology is presented and tested on an openly available dataset of medical records. Within the experimental setup we show that the approach based on personalized budgets, compared to the architecture including global differential privacy with fixed privacy budget, achieves a better model performance in terms of two error metrics.

---


### 392. [Fight Poison with Poison: Enhancing Robustness in Few-shot Machine-Generated Text Detection with Adversarial Training](https://arxiv.org/abs/2605.02374)

**<font color=#1a73e8>作者：</font>** Wenjing Duan, Qi Zhou, Yuanfan Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-generated text (MGT) detection is critical for regulating online information ecosystems, yet existing detectors often underperform in few-shot settings and remain vulnerable to adversarial, humanizing attacks. To build accurate and robust detectors under limited supervision, we adopt a threat-modeling perspective and study detector vulnerabilities from an attacker's viewpoint under an output-only black-box setting. Motivated by this perspective, we propose RAG-GuidEd Attacker Strengthens ConTrastive Few-shot Detector (REACT), an adversarial training framework that improves both few-shot detection performance and robustness against attacks. REACT couples a humanization-oriented attacker with a target detector: the attacker leverages retrieval-augmented generation (RAG) to craft highly human-like adversarial examples to evade detection, while the detector learns from these adversaries with a contrastive objective to stabilize few-shot representation learning and enhance robustness. We alternately update the attacker and the detector to enable their co-evolution. Experiments on 4 datasets with 4 shot sizes and 3 random seeds show that REACT improves average detection F1 by 4.95 points over 8 state-of-the-art (SOTA) detectors and reduces the average attack success rate (ASR) under 4 strong attacks by 3.66 percentage points.

---


### 393. [Binary Rewards and Reinforcement Learning: Fundamental Challenges](https://arxiv.org/abs/2605.02375)

**<font color=#1a73e8>作者：</font>** Marc Dymetman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a standard approach for improving reasoning in language models, yet models trained with RLVR often suffer from diversity collapse: while single-sample accuracy improves, multi-sample coverage degrades, sometimes falling below the base model. We provide a structural account of this phenomenon grounded in the properties of binary rewards. Binary rewards create a fundamental degeneracy for policy gradient methods: the set of distributions maximizing expected reward is infinite, with no distinguished element. KL-control resolves this degeneracy by selecting, in the limit $\beta\to 0$, the filtered model $p_*:=a(\cdot\mid\mathcal{Y}_1)$ -- the base model conditioned on validity -- which is the unique fully valid distribution closest to the base model in KL divergence. This selection operates through a nontrivial asymmetry: the tilted distribution $p_{[\beta]}\propto a(y)\,e^{v(y)/\beta}$ converges to $p_*$ in forward KL as $\beta\to 0$, yet $p_*$ cannot serve as a direct optimization target because $\mathrm{KL}(q\,\|\,p_*)$ is infinite for any full-support policy $q$. We develop explicit formulas relating the hyperparameter $\beta$ to the more interpretable target validity rate $\mu$. Under model misspecification -- the typical practical regime -- the pressure to decrease $\beta$ drives the optimizer toward highly concentrated distributions over a small number of valid outputs, collapsing toward ever fewer as $\beta$ decreases, rather than toward the filtered model. We illustrate this mechanism on a toy autoregressive experiment and discuss how alternative divergences that target $p_*$ directly -- as pursued empirically by \citet{kruszewski_whatever_2026} -- avoid this failure mode by rewarding coverage of $p_*$'s support rather than concentration on high-validity outputs.

---


### 394. [Graph-Augmented Topological Internalization with Dual-Stream Classifiers for Medical Report Generation](https://arxiv.org/abs/2605.02376)

**<font color=#1a73e8>作者：</font>** Moyu Tang, Chupei Tang, Junxiao Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated medical report generation, MRG, holds substantial value for alleviating radiologist workload and enhancing diagnostic efficiency. However, mainstream approaches typically treat diverse chest abnormalities as isolated classification targets. This paradigm often overlooks inherent disease co-occurrences and struggles to translate medical topological structures into explicit data correlations, constraining the model's reasoning capacity on complex or subtle lesions. To address this, we propose a Graph-Augmented Dual-Stream Medical Report Generation with Topological Internalization, GDMRG. Our framework introduces a Topological Knowledge Internalization module, TKI, which leverages a Graph Convolutional Network, GCN, to generate an explicit parameterized weight matrix based on global disease co-occurrence priors. This facilitates efficient topological knowledge injection without relying on external retrieval mechanisms. Building upon this, we construct a dual-stream classification system: the main branch generates discrete diagnostic prompts under topological constraints, while the auxiliary branch employs an asymmetric optimization strategy to dynamically calibrate decision boundaries for highly imbalanced samples. Concurrently, to establish a logical closed loop between diagnosis and visual grounding, we design a diagnostic-driven Diagnosis-Guided Spatial Attention, DGSA, that utilizes high-dimensional clinical semantics to recalibrate the visual encoder, mitigating feature hallucinations. Comprehensive experiments on the MIMIC-CXR dataset demonstrate that GDMRG achieves competitive clinical efficacy, CE, while maintaining natural language fluency. Furthermore, our model exhibits robust zero-shot generalization on the IU X-Ray dataset. In summary, this work presents an integrated and interpretable paradigm for medical report generation.

---


### 395. [UnGAP: Uncertainty-Guided Affine Prompting for Real-Time Crack Segmentation](https://arxiv.org/abs/2605.02380)

**<font color=#1a73e8>作者：</font>** Conghui Li, Huanyu He, Xin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time crack segmentation is vital for structural health monitoring but is plagued by aleatoric uncertainties arising from varying lighting, blur, and texture ambiguity. Current uncertainty-aware approaches typically treat uncertainty estimation as a passive endpoint for post-hoc analysis, failing to close the loop by feeding this information back to refine feature representations. We contend that independent pixel-wise heteroscedastic modeling is uniquely suited for crack segmentation, as cracks are defined by fine-grained local gradients rather than the global semantic coherence relied upon in general object segmentation. However, this approach suffers from a structural optimization pathology: high predicted variance attenuates loss gradients, effectively causing the model to ignore difficult samples and under-fit complex boundaries. To address these challenges, we propose UnGAP, a novel framework that establishes a closed-loop mechanism between uncertainty estimation and feature learning. Central to our approach is the Uncertainty-Prompted Feature Modulator (UPFM), which treats aleatoric uncertainty as an active visual prompt rather than a mere output. UPFM dynamically calibrates feature distributions through pixel-wise affine transformations. Crucially, this mechanism mitigates the heteroscedastic pathology by transforming high variance, which would otherwise indicate gradient suppression, into a constructive signal for stronger feature rectification in ambiguous regions. Additionally, a boundary-aware detection head is introduced to further constrain prediction precision. Extensive experiments demonstrate that UnGAP balances superior segmentation accuracy with real-time inference speed, effectively validating the benefit of transforming uncertainty from a passive metric into an active calibration tool.

---


### 396. [Design and Performance Evaluation of a BLE-Based IoT Authentication System](https://arxiv.org/abs/2605.02381)

**<font color=#1a73e8>作者：</font>** Nitesh Yadav, Vashisht Kumar, Sachin Kadam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bluetooth Low Energy (BLE) is widely used in modern IoT systems because it consumes very little power, saves energy, and allows for simple device connectivity; however, maintaining security and communication reliability remains a challenge. In this paper, an authentication system is designed using industry-grade BLE-enabled nodes (nRF5340 development kit) that include a peripheral node with a keypad for entering a PIN and a central node with an LCD display. The entered PIN is sent wirelessly from the peripheral node to the central node via BLE technology, where it is verified in real time and displayed as correct or incorrect. Next, only after successful authentication can the peripheral node send data to the central node. In addition to authentication, the peripheral node can measure temperature in real time using the temperature sensor interfaced to it and send it wirelessly to the central node, where it can be displayed on the LCD interface. Received Signal Strength Indicator (RSSI) values are collected during experiments under various scenarios to evaluate the system's performance. We see that the signal strength (measured in terms of RSSI values) is strong at close range but weak as distance increases, indicating a decaying logarithmic pattern. The system also has low latency, which allows for quick input and output, and it uses PIN-based authentication to ensure security and prevent misuse. The entire system seamlessly integrates communication, sensing, and security, making it suitable for smart access control and wireless monitoring systems, including home automation.

---


### 397. [Differentially Private Runtime Monitoring](https://arxiv.org/abs/2605.02391)

**<font color=#1a73e8>作者：</font>** Bernd Finkbeiner, Frederik Scheerer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern stream-based monitors collect detailed statistics of the runtime behavior of the system under observation. If the system runs in a privacy-sensitive context, this poses the risk of disclosing sensitive information. Differential privacy is the state-of-the-art approach for protecting sensitive information, however, integrating it into runtime monitoring is challenging: temporal operators can cause individual input values to influence multiple outputs over time, leading to repeated disclosure of private information. We propose an approach that automatically enforces differential privacy in stream-based monitoring specifications by analyzing temporal dependencies and injecting carefully calibrated noise into the specification. To preserve the utility of the outputs, we identify strategically chosen positions in the specification for noise injection and leverage tree-based mechanisms to mitigate the accuracy loss caused by noise injected into aggregation operators. We demonstrate the practicality and effectiveness of our approach in a case study on monitoring public transportation usage.

---


### 398. [Is It Novel and Why? Fine-Grained Patent Novelty Prediction Based on Passage Retrieval](https://arxiv.org/abs/2605.02392)

**<font color=#1a73e8>作者：</font>** Valentin Knappich, Anna Hätty, Simon Razniewski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Novelty assessment is a critical yet complex task in the examination process for patent acceptance, requiring examiners to determine whether an invention is disclosed in a prior art document. The process involves intricate matching between specific features of a patent claim and passages in the prior art. While prior work has approached novelty prediction primarily as a binary classification task at the claim level, we argue that this formulation is susceptible to spurious correlations and lacks the granularity required for practical application. In this work, we introduce FiNE-Patents (Fine-grained Novelty Examination of Patents), a novel dataset comprising 3,658 first patent claims annotated with fine-grained, feature-level prior art references extracted from European Search Opinion (ESOP) documents. We propose shifting the evaluation paradigm from simple binary classification to a joint retrieval and abstract reasoning task at the feature level, requiring models to identify specific passages from a prior art document that disclose individual claim features, and to identify which features of a claim make it novel. We implement and evaluate LLM-based workflows that decompose claims into features, analyze each feature against prior art, and finally derive a claim-level novelty prediction. Our experiments demonstrate that these workflows outperform embedding-based baselines on passage retrieval and novel feature identification. Furthermore, we show that unlike trained classifiers, LLMs are robust against spurious correlations present in the claim-level novelty classification task. We release the dataset and code to foster further research into transparent and granular patent analysis.

---


### 399. [FEAT: Fashion Editing and Try-On from Any Design](https://arxiv.org/abs/2605.02393)

**<font color=#1a73e8>作者：</font>** Soye Kwon, Keonyoung Lee, Dahuin Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion design aims to express a designer's creative intent and to depict how garments interact with the human body. Recent methods condition on multimodal inputs to support garment editing and virtual try-on. However, existing methods still (i) confine design to garment-related images, excluding creative design sources such as artwork, abstract imagery, and natural photographs, and (ii) cannot support complete outfits, including accessories. We present FEAT (Fashion Editing And Try-On from Any Design), a method that enables editing and try-on across garments and accessories using diverse design sources. To achieve this, we introduce Disentangled Dual Injection (DDI). It takes both apparel and non-apparel design sources and selectively injects design cues via content and style disentanglement. Furthermore, we propose Orthogonal-Guided Noise Fusion (OGNF), a training-free mechanism that removes residual garments via orthogonal projection and applies region-specific noise strategies to enable virtual try-on for both garments and accessories. Extensive experiments demonstrate that FEAT achieves state-of-the-art performance in design flexibility, prompt consistency, and visual realism.

---


### 400. [Controllable and Verifiable Process Data Synthesis for Process Reward Models](https://arxiv.org/abs/2605.02395)

**<font color=#1a73e8>作者：</font>** Yinghui Chi, Lucien Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) rely on high-quality process supervision data, yet existing construction methods often provide limited control over error location, error type, and trajectory consistency. We propose a controllable and verifiable framework for synthesizing process supervision data for PRMs. Our framework first constructs a correct symbolic reasoning chain, injects a template-aware error into an intermediate step, recomputes subsequent steps under the corrupted state, and verifies that the injected step is not derivable from its prefix. The resulting paired trajectories are prefix-invalid at the first error while remaining trajectory-consistent after symbolic recomputation, and are translated into aligned natural-language processes for PRM training and evaluation. Experiments show that the synthesized data improve Best-of-8 reranking on logical reasoning benchmarks and transfer to mathematical reasoning. Step-level evaluation further shows that first-error localization remains substantially more challenging than overall step classification, highlighting the need for fine-grained and verifiable process supervision.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
