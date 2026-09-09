# 📦 其他研究 | 2026年09月09日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

---

### 151. [Conformal Prediction for Offensive Security](https://arxiv.org/abs/2609.05165)

**<font color=#1a73e8>作者：</font>** Giovanni Cherubin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite its introduction more than a quarter century ago, Conformal Prediction (CP) has seen surprisingly few applications to the cyber security world thus far. In particular, we observe that, while CP has been employed as a defensive measure in many recent works, its use for carrying out attacks (i.e., for offensive security) is hard to trace in the literature. We explore this gap, by presenting initial findings in two key areas of offensive security: Privacy-Preserving Machine Learning, and network traffic analysis.

---


### 152. [WeAgent-MMGenEdit: A Full-Stack Recipe for Multimodal Agentic Image Generation and Editing](https://arxiv.org/abs/2609.05171)

**<font color=#1a73e8>作者：</font>** Hui Zhang, Zongkai Liu, Liqiang Niu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generation and editing models have advanced rapidly, yet remain unreliable when prompts require external world knowledge. Bounded and long-tail parametric knowledge prevents direct or reason-then-generate approaches from recovering the required facts and visual appearances. Existing agentic generation and editing methods mitigate this limitation with retrieval tools, yet remain constrained by insufficient visual verification, overloaded policy models, and weak integration of retrieved textual and visual evidence. To address these limitations, we present WeAgent-MMGenEdit, a full-stack recipe including a multimodal harness, a scalable data construction pipeline, a comprehensive benchmark, and post-training methods for the agent policy and image backend. We first introduce WeAgent-Harness, a multimodal runtime with persistent evidence management and dedicated verification and integration tools that organize retrieved multimodal evidence into a dense carrier. Upon this, we develop a scalable pipeline for prompt synthesis and agentic trajectory collection, yielding 23K supervised trajectories and 14.7K RL tasks with three-layer verifiable checklists. We further introduce WeBench-MMGenEdit, a bilingual benchmark covering both knowledge-intensive image generation and multi-image editing. Finally, a two-sided post-training recipe based on SFT and RL improves the agent policy and image backend. Together, WeAgent-MMGenEdit enables a 30B-total/3B-active policy to outperform similarly sized policy models and approach the performance of a 1T-parameter agent.

---


### 153. [SMILE: Self-Explainable Multimodal Information Bottleneck for Medical Diagnosis](https://arxiv.org/abs/2609.05174)

**<font color=#1a73e8>作者：</font>** Yuqing Yang, Alexander Schmatz, Zhaozhao Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainability is increasingly seen as a crucial requirement in AI-based medical diagnosis, particularly in safety-critical clinical decision-making. Most existing explainability methods in healthcare operate in a post-hoc manner and are predominantly designed for unimodal data, which limits their applicability in increasingly prevalent multimodal diagnostic settings. This paper addresses the problem of self-explainable multimodal diagnosis by formulating it within the information bottleneck (IB) framework. We propose a unified learning paradigm that jointly optimizes predictive performance and modality-specific explainability by identifying the most informative elements inside each modality that contribute to diagnostic decisions. To enable tractable and stable optimization, we employ a matrix-based Renyi's $\alpha$-order entropy functional under the assumption of sufficiently expressive encoders. Extensive experiments on representative medical datasets spanning heterogeneous modalities demonstrate that the proposed method consistently achieves strong diagnostic performance, including an absolute accuracy improvement of 9.1 percentage points on the iCTCF dataset. Moreover, the learned explanations provide transparent and modality-aware insights into feature relevance, thereby improving both the explainability and generalization.

---


### 154. [The Mirror Agent Model: a Bayesian Architecture for Interpretable Agent Behavior](https://arxiv.org/abs/2609.05190)

**<font color=#1a73e8>作者：</font>** Michele Persiani, Thomas Hellström  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper we illustrate a novel architecture generating interpretable behavior and explanations. We refer to this architecture as the Mirror Agent Model because it defines the observer model, that is the target of explicit and implicit communications, as a mirror of the agent's. With the goal of providing a general understanding of this work, we firstly show prior relevant results addressing the informative communication of agents intentions and the production of legible behavior. In the second part of the paper we furnish the architecture with novel capabilities for explanations through off-the-shelf saliency methods, followed by preliminary qualitative results.

---


### 155. [Phase Transition Frequency as a Training Time Predictor of Test Accuracy in ResNets](https://arxiv.org/abs/2609.05194)

**<font color=#1a73e8>作者：</font>** Arunan J  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The number of discrete class-separability jumps observed during ResNet finetuning is examined empirically as a predictor of final test accuracy. Across 75 experiments spanning four benchmarks (CIFAR-10, CIFAR-100, TinyImageNet, and CIFAR-10-C) and three architectures (ResNet-18, ResNet-50, and ResNet-101), with five to ten seeds per configuration, a strong within-dataset negative correlation is obtained on standard i.i.d. classification benchmarks: \(r = -0.84\) on CIFAR-10 (\(p < 10^{-8}\), \(n = 30\)) and \(r = -0.87\) on CIFAR-100 (\(p < 10^{-5}\), \(n = 15\)). Under distributional stress, the relationship attenuates: TinyImageNet yields \(r = -0.45\), and the CIFAR-10-C corruption benchmark yields \(r = -0.19\). Two additional analyses discipline the empirical claim. A partial correlation controlling for architecture depth, treated as a linear covariate, shows that on CIFAR-100 the transition count retains statistically significant predictive power (\(r_{\mathrm{partial}} = -0.69\), \(p = 0.007\)); the corresponding result under the stricter categorical conditioning is not established at \(n = 15\). A comparison against six alternative training-curve signals shows that transition count achieved the strongest correlation among the evaluated signals on CIFAR-100 and one of the strongest on CIFAR-10, but is dominated by other signals on the two stressed benchmarks. The comparison is restricted to training-curve-level signals; comparisons against effective rank, Hessian sharpness, Fisher information, margin, and neural-collapse measures, which are the strongest competitors in the current literature, are not part of the present study and remain open. The observation is presented as an in-distribution training-quality probe among a family of candidate probes, and an inexpensive detection procedure suitable for logging alongside a standard training loop is provided.

---


### 156. [BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors](https://arxiv.org/abs/2609.05210)

**<font color=#1a73e8>作者：</font>** Vincent Leroy, Philippe Weinzaepfel, Lojze Zust 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively costly, especially considering time constraints inherent to online applications like Visual SLAM (VSLAM). In this paper, we introduce a regularized BA framework that leverages a fast multi-view matcher and monocular priors for initialization and regularization. In contrast to existing systems, our unified approach seamlessly supports both online VSLAM and offline reconstruction from unordered image collections within the same optimization framework and sharing common hyperparameters for all tasks. Extensive experiments across both domains demonstrate improved performance and speed tradeoffs over traditional, feed-forward, and hybrid baselines. Notably for VSLAM, our uncalibrated method outperforms all previous calibrated approaches.

---


### 157. [Dimension-Adaptive Batched Lipschitz Narrowing Without Knowing the Zooming Dimension](https://arxiv.org/abs/2609.05214)

**<font color=#1a73e8>作者：</font>** Yasong Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Appropriately Combined Edge-length (ACE) sequence in A-BLiN depends on the zooming dimension $d_z$. This note removes that dependence. The next edge length is selected from the number of cubes that survive the preceding elimination. The resulting Count-Adaptive BLiN algorithm does not use $d_z$ or the zooming constant $C_z$, yet it attains $\widetilde{\mathcal O}_d(T^{(d_z+1)/(d_z+2)})$ regret with $\mathcal O_d(\log\log T)$ batches. Together with the adaptive-grid lower bound in Theorem 10 of the original paper, the optimal batch complexity remains $\Theta_d(\log\log T)$ when $d_z$ is unknown.

---


### 158. [FedDRAW: Federated Dual Reputation Annealing Weighting for Heterogeneous Multi-Institutional Chest Radiograph Classification](https://arxiv.org/abs/2609.05223)

**<font color=#1a73e8>作者：</font>** Maryam Moradpour, Anne-Christin Hauschild  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence models are promising for medical diagnosis, but they require large numbers of unbiased data, which in medicine are distributed across hospitals and cannot be centralized to protect patient privacy. Federated Learning (FL) addresses this, since hospitals train one shared diagnostic model while patient data remain local. Training proceeds in communication rounds, in which each hospital trains the shared model locally and returns it to the server for merging by weighted average. This aggregation weight determines whose institutional knowledge shapes the result. Federated averaging (FedAvg) sets it in proportion to local sample count, so a small but informative hospital is permanently assigned a small influence, andl argest clients could dominate the global model even when they are less informative. We propose Federated Dual Reputation Annealing Weighting (FedDRAW), a server-side aggregation method that combines a data-size prior with the cosine similarity between client and global parameters under two coupled annealing schedules. An inner schedule shifts client reputation from the size prior towards similarity. An outer, deferred annealing schedule on the softmax inverse temperature keeps the weighting selective in the early and middle rounds and relaxes it to uniformity at convergence. We evaluate FedDRAW on 12 simulated client-partition scenarios of two chest radiograph datasets (CheXpert and ChestMNIST), against seven federated baselines under identical local training settings. FedDRAW achieved the highest average rank among all eight methods under both AUC and the geometric mean (GM) of sensitivity and specificity, which a Friedman test with Nemenyi post-hoc analysis confirmed to be a statistically significant difference between the methods. Scheduling two signals, rather than fixing the weights by sample count alone, could enable less biased diagnostic models.

---


### 159. [Hessian-based molecular conformation augmentation for a scalable and efficient strategy of machine learning interatomic potentials](https://arxiv.org/abs/2609.05233)

**<font color=#1a73e8>作者：</font>** Bumju Kwak, Jeonghee Jo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While machine-learning interatomic potentials (MLIPs) have successfully learned potential energy surfaces (PES) and atomic forces, many practical applications, such as vibrational analysis and transition state search, rely heavily on the PES Hessian. Yet, standard MLIPs tend to be trained on energy and forces alone, leaving Hessian information largely unexploited. Meanwhile, existing methods that explicitly incorporate the Hessian into training objectives require architectural modifications and introduce significant computational and memory overheads due to higher-order backpropagation. To address these limitations, we propose two Hessian-derived data augmentation schemes: isotropic Gaussian displacement (\textbf{UniAug}) and normal mode-weighted displacement (\textbf{ModeAug}). Both methods utilize simple Taylor expansions, achieving effective augmentation without altering training objectives or extending the autograd graph. This allows seamless, plug-and-play integration with existing architectures and training pipelines. Comprehensive evaluations across non-equilibrium and equilibrium datasets demonstrate that our approach enhances model accuracy while providing practical, task-specific guidelines.

---


### 160. [Measured Sliders: Learning Continuous Controls from Differentiable Image Measurements](https://arxiv.org/abs/2609.05234)

**<font color=#1a73e8>作者：</font>** Yijia Chen, Boyu Wei, Xuanhua Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous sliders are useful only when coefficient changes produce predictable image changes. Yet most diffusion sliders derive their axes from text or learned representations, leaving their scales disconnected from observable image properties. Consequently, we cannot tell in advance which attributes are learnable, compare control strengths directly, or anticipate interference when multiple controls are combined. We propose Measured Sliders, a framework that defines continuous controls through closed-form differentiable image measurements. A common measurement space unifies the pipeline. Before training, an observability test identifies usable supervision. During training, a measurement-guided objective learns target movement while suppressing non-target changes. After training, decoded calibration expresses controls in comparable units of realized image change. Multiple LoRA branches are stored in one checkpoint and composed without training on joint activations. Across SDXL and FLUX.1-dev, the resulting controls are ordered, selective, and composable. On 553 prompts, lighting direction reaches rho = 0.995 and 98.9% monotone sweeps. A five-attribute checkpoint achieves average selectivity 2.59, compared with 1.50 for the strongest baseline, and preserves every requested direction in 96.7% of pair and 86.1% of triple compositions. The observability test also separates every subsequently successful measurement from the failed candidate. Overall, image-space measurement provides a common basis for learning, diagnosing, calibrating, and composing continuous generative controls.

---


### 161. [Few-Shot Video Recognition via Hierarchical Metric Learning](https://arxiv.org/abs/2609.05242)

**<font color=#1a73e8>作者：</font>** Jiaxin Zhang, Haoran Gao, Xizhan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot action recognition (FSAR) aims to recognize unseen action categories with only a small number of annotated video samples. Recent works typically apply single-prototype supervision at the network output and fail to sufficiently exploit rich cross-frame global spatial information in videos. Even existing multi-level metric schemes only impose parallel prototype constraints on intermediate layers, without progressive supervision along the full feature pipeline, which results in limited generalization ability of the learned class prototypes. Inspired by this, we present a novel method, hierarchical metric learning for few-shot action recognition (HML-FSAR). First, a spatial-enhanced module is developed to capture cross-frame global spatial representations. Combined with temporal MHA, heterogeneous alignment, spatial-temporal feature fusion and dictionary learning modules, it constructs the complete feature processing pipeline. Second, a hierarchical metric learning (HML) strategy is embedded into HML-FSAR. Composed of center metric, alignment metric, contrastive metric, dictionary metric and prototype metric, HML imposes progressive multi-stage complementary constraints from frame-level representations to final class prototypes, so as to jointly optimize feature compactness, heterogeneous spatial-temporal alignment, inter-class discriminability and anti-noise robustness. The proposed HML-FSAR method is validated on five widely-used FSAR datasets, and experimental results fully demonstrate its effectiveness.

---


### 162. [A Unified Physics-Aware Quantum Machine Learning Framework across Power GaN HEMTs and Logic Nanowire FETs: Predicting Unseen Process Splits and Held-Out Geometry Combinations with Lower Error and Tighter Split-to-Split Variability](https://arxiv.org/abs/2609.05251)

**<font color=#1a73e8>作者：</font>** Rushat Rai, Yun-Yuan Wang, Autsada Kakaen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a unified reinforcement-learning (RL) framework that discovers compact parametrized quantum circuits (PQCs) for data-scarce device modeling. A graph neural network (GNN) policy optimized by proximal policy optimization (PPO) searches circuit architectures using leave-one-group-out cross-validation (LOGOCV) error on held-out process or geometry groups as the reward. The framework achieves the lowest mean absolute error (MAE) on all 11 targets versus six classical baselines, with 59% lower error (Ioff) and 81% tighter fold variability (VTH) for HEMTs and 84% lower error (VTH, SS, Ioff) and 82% tighter fold variability (Ioff) for NWFETs. These results demonstrate the potential of RL-selected, classically simulated PQCs as compact surrogates with low OOD error and improved physical consistency, despite imposing no explicit physical constraints, penalty terms, or device-specific equations, on the two evaluated device datasets.

---


### 163. [GLASS: Graph-Language Alignment with Spherical Scoring for Transferable Graph-Level Anomaly Detection](https://arxiv.org/abs/2609.05253)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Chris Ding, Tongxin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce GLASS, a framework for graph-level anomaly detection (GLAD) that achieves robust cross-domain transferability through graph-language alignment on the unit hypersphere. GLASS builds a unified representation space by aligning a structure-aware graph encoder with an instruction-aware text embedding via a multi-slice soft cosine objective. Our framework serializes local, global, and semantic graph properties into a compact Graph Descriptor Prompt (GraphDP), creating a text bridge that enables domain-agnostic anomaly scoring. By enforcing multi-scale consistency through Matryoshka representation slices, the model captures anomalous deviations at multiple levels of granularity. For scoring, we formulate anomaly detection as density estimation on the aligned hypersphere and introduce Spherical Multi-Modal Scoring (SMS), which instantiates von Mises-Fisher kernel density estimators in both graph and text embedding spaces. This probabilistic formulation recovers angular k-nearest-neighbor scoring as a high-concentration limiting case and provides a principled fusion of structural and semantic anomaly signals. The shared text embedding space further serves as a cross-domain bridge: by encoding a target domain's GraphDP without target-domain training data, GLASS performs zero-shot anomaly detection, and with only a handful of normal examples, few-shot adaptation via reference-set calibration. Across twelve benchmarks and three meta-domains, GLASS obtains the best average AUROC and rank compared with recent advanced GLAD baselines and enables effective cross-domain transfer.

---


### 164. [Compact Neural Appearance Models for Efficient Gaussian Splatting](https://arxiv.org/abs/2609.05255)

**<font color=#1a73e8>作者：</font>** Florian Hahlbohm, Jorge Condor, Linus Franke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explicit primitive-based radiance fields such as 3D Gaussian Splatting typically model view-dependent appearance using low-order spherical harmonics (SH). Although efficient to evaluate, SH coefficients dominate per-primitive storage and memory traffic, while their band-limited basis restricts angular detail. We present a thorough, end-to-end comparison of SH and recent spherical appearance models and introduce an implicit alternative that decodes compact per-primitive latent codes using a tiny shared MLP. We integrate all models into the same optimized pipeline, fusing their forward and backward passes into a differentiable CUDA rasterizer and provide a portable WebGL viewer for laptop and mobile GPUs. Our evaluation across reconstruction quality, memory use, and optimization and rendering performance shows that recent spherical models offer the strongest overall quality-efficiency trade-off. Our neural representation is the most compact model evaluated and, compared to third-degree SH, reduces the per-primitive appearance footprint from 192 to 28 bytes, accelerates optimization by 1.3$\times$, while improving reconstruction quality. We further analyze how appearance parametrization shapes optimization, identifying differences in recovered geometry and the tendency of expressive models to absorb non-static scene content. Together, our framework and analysis provide practical guidance for replacing SH beyond what image metrics alone can capture.

---


### 165. [Commonsense Reasoning in Computer Vision: Foundations, Recent Advancements, and Future Directions](https://arxiv.org/abs/2609.05257)

**<font color=#1a73e8>作者：</font>** Bahar Uddin Mahmud, Sumit Barua, Guan Yue Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Commonsense reasoning in computer vision encompasses integrating visual data and contextual knowledge, crucial for enhancing AI's understanding of everyday scenarios. This understanding not only improves machine learning models but also enhances their ability to interact meaningfully with humans and the environment. Unlike CNN-based conventional vision models, which are designed to identify objects within a specific image, incorporating commonsense knowledge enables models to interpret scenes in a more holistic manner, thereby improving their spatial ability to reason about relationships among objects and actions. This integration not only enhances object recognition but also facilitates a deeper understanding of the contextual factors, ultimately leading to more precise predictions and interactions in real-world applications. This paper presents a comprehensive survey of recent developments that integrate commonsense knowledge into computer vision tasks. We systematically review approaches based on knowledge graphs, scene graphs, neuro-symbolic models, and commonsense-augmented transformers. We also outline current limitations related to dataset bias, knowledge incompleteness, and integration challenges. Finally, we highlight prospective research trajectories in cross-modal reasoning, scalable commonsense knowledge injection, and neuro-symbolic hybrid architectures to develop truly intelligent visual systems.

---


### 166. [Self-Supervised Lexical Representation Learning for Fast, Large-Scale Phylogenetic Inference](https://arxiv.org/abs/2609.05262)

**<font color=#1a73e8>作者：</font>** Tim Wientzek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational phylogenetics has become an essential tool in historical linguistics, yet its application at a global scale remains constrained by two factors: the labor-intensive manual annotation of cognacy judgments required for character-based methods and the substantial computational cost of inference on large datasets. This paper introduces a fully self-supervised contrastive learning framework that learns lexical representations directly from raw IPA-transcribed wordlists, without requiring cognacy annotations, alignments, or additional expert input. The model employs a dual contrastive objective: a word-level loss that organizes phonetically similar forms into a coherent space, and an auxiliary language-level loss that encourages the lexical space to reflect broader phonological properties of languages. From the resulting word representations, pairwise language distances are derived and used to infer a global phylogenetic tree of 3,399 language varieties. The inferred tree achieves a generalized quartet distance (GQD) to the Glottolog reference tree competitive with multiple baselines, while requiring only minutes of computation on a standard notebook GPU. Furthermore, the same representations capture diachronic concept stability: variance in pairwise distances across languages yields stability rankings that correlate significantly with established rankings. Ablation studies confirm that both the language-level objective and the use of phonetic feature vectors improved the inferred trees topology with regards to GQD. The framework thus provides a computationally efficient and fully automatic alternative for large-scale phylogenetic inference and offers a unified representation supporting downstream analyses at both the language and concept level.

---


### 167. [AI for Computational Design Science: A Responsible Human-AI Framework and Case Study on Short-Form Video Safety Surveillance](https://arxiv.org/abs/2609.05270)

**<font color=#1a73e8>作者：</font>** Wenli Zhang, Jiaheng Xie, Zhihe Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is transforming not only what information systems researchers design, but also how design research is conducted. Yet existing literature offers limited guidance for computational design science (CDS) when AI actively participates in problem formulation, resource construction, design search, evaluation, and knowledge abstraction. We develop AI for Computational Design Science (AI4CDS), a five-phase methodological framework in which AI expands problem and design search while researchers retain responsibility for domain grounding, admissibility, verification, and scientific judgment. Collaboration is governed by graduated trust, reversibility, auditability, and differentiated reproducibility. We instantiate AI4CDS through ChildRiskGuard, an interpretable artifact for detecting short-form videos inappropriate for children, while documenting AI interactions, rejected alternatives, corrections, and audit trails. The case translates audience-dependent safety and explanation faithfulness into three technical challenges and develops an artifact that separates generic from child-specific risk, represents distinct developmental-risk mechanisms, and makes concept-level explanations part of the predictive computation. ChildRiskGuard achieves an F1 score of 0.769, substantially outperforming direct application of a general-purpose content-safety model while remaining competitive with strong benchmarks. The primary contribution is AI4CDS as a responsible framework for AI-enabled CDS; ChildRiskGuard provides process and artifact evidence of how AI-expanded, researcher-governed design can generate and evaluate novel computational design knowledge.

---


### 168. [Learning from VAE Errors to support ECG-based Differential Diagnosis of Myocardial Scar](https://arxiv.org/abs/2609.05294)

**<font color=#1a73e8>作者：</font>** Shayan Sharifi, Riccardo Treu, Ilaria Gandin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Late Gadolinium Enhancement (LGE) on cardiac magnetic resonance is a key marker of myocardial scar, but its limited accessibility motivates routine ECG-based screening. We evaluated whether $\beta$-variational autoencoder (VAE)-derived ECG representations can discriminate LGE+ from LGE- cardiomyopathic patients in a local cohort of 300 subjects. We compared 32-dimensional features from the foundation this http URL model with those from a shallower $\beta$-VAE trained on normal PTB-XL ECGs, evaluating downstream classification and Dynamic Time Warping (DTW)-based reconstruction errors. this http URL reached an area under ROC of 0.686 with Random Forest, while the proposed $\beta$-VAE reached 0.577 with sensitivity of 0.775 with Gradient Boosting. Notably, DTW-reconstruction errors significantly differed between classes in 10 out of 12 leads according to Mann-Whitney U test and help in classification, leading to an area under ROC of 0.643 with Logistic Regression, supporting their potential as markers of scar-related ECG alterations.

---


### 169. [LexFlip: A Dissociation Diagnostic for Legal Meaning Preservation Metrics](https://arxiv.org/abs/2609.05296)

**<font color=#1a73e8>作者：</font>** Gaurab Baral  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does a simplified legal clause still say what the original said? The checks in current use cannot establish that it does: requiring an identical pair to score highest and an unrelated pair lowest moves lexical overlap and legal force together, so any monotone function of token overlap satisfies both. Our remedy is a dissociation, an item holding surface form fixed while legal force moves. We release LexFlip, 373 minimal perturbations of Quebec statutory French that reverse legal force while preserving 0.93 of the tokens, with a harness scoring metrics, regressors and prompted judges alike. The seven embedding and BERTScore metrics we test spend only 0.022 to 0.039 of their identical-to-unrelated range on such an edit, against 0.670 for bidirectional NLI, the one family the identical-pair check would disqualify. On FrJudge, against a measured human ceiling of r=0.597, a bare length feature outscores every semantic metric and has the lowest margin we measure.

---


### 170. [Online Change-point Detection for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.05298)

**<font color=#1a73e8>作者：</font>** Fatemeh Saberi Khomami, Julita Vassileva  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning (MARL) systems rely on past experience for learning coordinated behaviour, but this experience may become unreliable if the environment or task objective changes during training. In such cases, agents first need a way to recognize that the situation has changed before deciding how to adapt. This paper studies online change-point detection for cooperative MARL using reward-derived signals. We propose \emph{Patterns of Past Rewards} (PPR), a lightweight algorithm-agnostic detector that smooths agents' return streams, highlights recent changes, and applies a statistical drift detector to flag significant shifts. We evaluate PPR in a custom Speaker-Listener environment based on the Multi-Agent Particle Environment under two controlled non-stationarity scenarios. Our results show a trade-off between detection speed and alarm stability. A smoothed-return baseline detects earlier but produces many repeated alarms. In contrast, applying the detector directly to raw returns often misses the shift. PPR offers a more balanced approach by limiting redundant detections while still identifying the controlled shifts. These findings highlight PPR as a lightweight, reward-based monitoring tool that enables cooperative MARL systems to reliably identify major changes during training.

---


### 171. [Learning Spatial-Spectral Refinement and Calibrating Complementary Observations for Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2609.05303)

**<font color=#1a73e8>作者：</font>** Liqian Yang, Xingchi Chen, Xinfeng Gui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral and multispectral image fusion (HMIF) aims to reconstruct a high-resolution hyperspectral image (HR-HSI) by combining the fine spatial details of a high-resolution multispectral image (HR-MSI) with the rich spectral information of a low-resolution hyperspectral image (LR-HSI). Recent advances in implicit neural representations (INRs) have enabled flexible coordinate-based modeling for HMIF; however, existing INR-based approaches may not fully capture fine-grained spatial structures and rich spectral dependencies. Moreover, the LR-HSI and HR-MSI are primarily incorporated through degradation-consistency constraints, leaving their complementary information underexploited. To address these limitations, we propose Two-Stage Reconstruction with Implicit Tensor Neural Representation (TSR-ITNR), a unified self-supervised framework integrating representation refinement and observation-guided calibration. In Stage 1, TSR-ITNR learns an implicit Tucker representation and refines its low-rank spatial coefficient tensor and spectral basis to better capture fine spatial structures and interband correlations. A fixed pretrained denoiser further provides a deep prior for the preliminary reconstruction. In Stage 2, parameter-free calibration derives complementary and noninterfering corrections from both observations to recover information insufficiently captured in Stage 1. Theoretical analysis establishes the geometry-preserving property of spectral refinement and the orthogonal complementarity of calibration. Extensive experiments on multiple benchmark datasets demonstrate strong quantitative, visual, and spectral reconstruction performance without ground-truth HR-HSI supervision. Beyond conventional reconstruction metrics, we further assess the effectiveness of TSR-ITNR using downstream semantic segmentation accuracy.

---


### 172. [Optimal Rates for Agentic Networked Information Aggregation](https://arxiv.org/abs/2609.05318)

**<font color=#1a73e8>作者：</font>** MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building on the pioneering paper of Kearns, Roth, and Ryu (SODA'26), we study information aggregation in a networked learning model. The model captures a central pattern in agentic AI: each agent sees only part of the data and passes on only its own conclusion. Their model considers a linear regression problem with the mean squared error (MSE) loss. Agents sit in a DAG and each sees only a subset of the features and its parents' predictions, fits a linear predictor, and passes only its prediction forward. The benchmark is the full-feature learner that sees all raw features. A path of depth $D$ is $M$-covered if every block of $M$ consecutive agents collectively sees all raw features. Kearns, Roth, and Ryu proved that the excess mean squared error of the last agent on such a path is $O(M/\sqrt D)$, and gave a cyclic instance with excess error $\Omega(M/D)$ for $D<M^2$.
We close this gap: the correct rate is constant up to depth $M^2$, and $\Theta(M^2/D)$ beyond it. We first give a sharper analysis of the cyclic instance and improve its lower bound to $\Omega(\sqrt{M/D})$ for $D<M^2$. We then construct, for every depth $D\ge M^2$, an $M$-covered path of depth $D$ with excess error $\Omega(M^2/D)$. The same instance gives the constant lower bound for all $D < M^2$. We also show that for any fixed distribution the excess error contracts geometrically along the path, ruling out any single instance that witnesses any polynomial lower bound at every depth.
Finally, we prove the same optimal rate for logistic classification in the logit-passing model of Bateni et al., which considers the binary cross-entropy (BCE) loss. The same improved upper bound of $O(M^2/D)$ holds, and we transfer all the regression lower bounds by showing that on those examples the logistic path follows the least-squares path up to rescaling.

---


### 173. [Adaptive Gated Deepfake Detection for Low-Resolution and Resource-Constrained Environments](https://arxiv.org/abs/2609.05320)

**<font color=#1a73e8>作者：</font>** Vaishnavi Sen, Cody Laurie, Rashida Hasan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection models often rely on high-quality inputs, fixed inference paths, and computationally expensive architectures, limiting their use in low-resolution and resource-constrained settings. This paper proposes AdaGate-DF, an adaptive gated deepfake detection framework that uses image-quality cues to route samples through a dual multi-exit system so high-quality images can exit earlier and save compute. We evaluated AdaGate-DF against MaD-CoRN, DefakeHop++, and ShuffleNetV2 on two benchmark datasets (Celeb-DF and FaceForensics++) under multiple configurations to test image resolution dependence and training and inference efficiency. On Celeb-DF, AdaGate-DF achieves an AUC of 0.9370, outperforming MaD-CoRN and DefakeHop++ while maintaining a low inference latency. Resolution-based testing shows consistent improvement as input resolution increases, reaching an AUC of 0.9708 at 384 by 384. The FaceForensics++ results highlight that AdaGate-DF remains effective under class imbalance, following competitive results with evaluated models. Overall, AdaGate-DF demonstrated a practical balance between detection performance, uncertainty-aware prediction, and computational efficiency for variable-quality deepfake detection.

---


### 174. [Scalable Detection of Fossil Palynomorphs in Multifocal Digital Microscopy Images](https://arxiv.org/abs/2609.05323)

**<font color=#1a73e8>作者：</font>** Abbas Shaikh, Praise Mayor, Patrick Ainlay-Vazquez 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Palynomorphs (microscopic, organic-walled fossils such as pollen, spores, and dinoflagellates) are important high-resolution records of past climates and are critical to the study of ancient ecosystems. Existing methods rely on manual analysis of high-resolution, multifocal digital microscopy images, which is slow and time-consuming and requires researchers to compromise on the scale of their investigations. To the best of our knowledge, our work proposes the first ever scalable end-to-end pipeline for automated palynomorph detection in whole slide images that addresses this bottleneck through: (1) efficient methods for decomposing and compressing digitized multifocal microscope slide images into tractable 2-dimensional tiles for analysis; (2) benchmarking modern object detection models, including RF-DETR, for the detection of palynomorphs, achieving an AP@50 of 0.879; (3) an efficient algorithm for the synthesis of detection outputs across large-scale, high-resolution images; and (4) an I/O optimization resulting in faster inference time. Our methods drastically reduce the time required for palynomorph detection in a single slide from often days of manual inspection to under one hour of automated analysis, enabling palynological research at a substantially greater scale.

---


### 175. [Embedded Graph Flows for Categorical Graph Generation](https://arxiv.org/abs/2609.05328)

**<font color=#1a73e8>作者：</font>** Ethan Ma, Zihan Wang, Chris Siu Yeung Chow 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating categorical graphs requires choosing node and edge types that form a coherent structure without depending on node order. Many graph generators encode categories as fixed one-hot vectors, which can impose an artificial geometry in which categories are equidistant. We propose Embedded Graph Flows (EGF), a generative model that learns continuous embeddings for node and unordered-edge categories and transports Gaussian noise towards these learnt endpoints using a permutation-equivariant graph transformer. A terminal readout maps the embeddings back to discrete graph categories. Across molecular benchmarks, EGF achieved competitive performance. On QM9, EGF gives the best result on all four reported metrics among the three methods, including a Fréchet ChemNet Distance (FCD) of 0.150, compared with 0.717 for the categorical-diffusion baseline DiGress and 0.812 for the bridge-based baseline GruM. When applied to larger molecules in ZINC250k, EGF retains the lowest maximum mean discrepancy (MMD) using the neighbourhood subgraph pairwise distance kernel (NSPDK), indicating close agreement with the local substructures of the reference molecules. Our code is available at this https URL.

---


### 176. [Machine Unlearning as Private Retroactive Algorithms](https://arxiv.org/abs/2609.05329)

**<font color=#1a73e8>作者：</font>** Haim Kaplan, Refael Kohen, Yishay Mansour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning typically aims to emulate retraining from scratch: upon a deletion request, the unlearning algorithm should produce an outcome that would have been obtained had the deleted point never been included. Recent work has shown that this emulation requirement carries no meaningful privacy semantics against an adversary who observes a sequence of releases. Machine unlearning is thus not a privacy question per se, but rather a data maintenance question, which is precisely the subject of retroactive algorithms. These are algorithms supporting modifications of past operations, guaranteeing that all subsequent answers reflect the revised history as if it had always been in force.
We put forward a definition of private retroactive algorithms, combining the retroactivity requirement with differential privacy under continual observation. We present constructions achieving both privacy and retroactivity at no asymptotic cost over privacy alone for linear statistics, clustering, and histograms, alongside impossibility results.

---


### 177. [Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions](https://arxiv.org/abs/2609.05334)

**<font color=#1a73e8>作者：</font>** Mahadev Sunil Kumar, Bhavika Gondi, Desaisetty Venkata Satya Sai Swapnith 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chilli (Capsicum annuum) is one of India's most economically significant crops, yet its productivity is persistently threatened by diseases that are difficult to identify without expert intervention. While Vision Transformers (ViTs) have achieved high classification accuracy, their large computational footprint makes deployment on resource constrained devices challenging. Existing compression approaches typically address pruning, quantization, and knowledge distillation in isolation, leaving the potential benefits and interactions of their combined application insufficiently explored. We propose a unified Vision Transformer compression framework that combines Hessian-Balanced Adaptive Block Pruning (H-BAC), guided by second-order sensitivity estimation, with quantization and attention-based knowledge distillation. To systematically identify the most effective configuration within each compression family, each technique is first evaluated independently through controlled ablation studies, after which the best-performing components are integrated into a sequential deployment pipeline tailored to real-world agricultural constraints. On a chilli 3-class village-split dataset with a genuine cross-village, cross-device out-of-distribution test split, the resulting compressed models match or exceed the 95.13% FP32 baseline's accuracy, alongside 74-98% model size reduction, and the fully integrated compression pipeline achieves a 54.5x size reduction (327.42 MB to 6.01 MB) at 95.13 +/- 2.32% accuracy across four tested configurations. A direct comparison further reveals that, on this dataset, a directly-trained student of the same final size, without pruning or distillation, reaches comparable accuracy of 94.87%, at the same 6.01 MB INT8 size, indicating where H-BAC and knowledge distillation are, and are not yet shown to be, worth their computational cost.

---


### 178. [Variational Continuation for Double Pendulum Periodic Orbits](https://arxiv.org/abs/2609.05337)

**<font color=#1a73e8>作者：</font>** Leo Yao, Ziming Liu, Max Tegmark  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a Hessian-based approach to numerically continue periodic orbits in dynamical systems. A loop (periodic orbit candidate) is parametrized as a Fourier series; a loss function is defined based on the deviation of the loop from the physical differential equations. Unlike previous work relying on hand-derived Jacobians, our method automates the process by leveraging automatic differentiation, a common machine learning technique. The continuation direction can be determined by the flat directions of the loss landscapes (directions with zero eigenvalues), making the search of periodic orbits efficient and guided. Our method is integrator-free, precisely initializes oscillations around unstable fixed points, and efficiently detects orbit family intersections and subharmonic bifurcations. As a demonstration, we present full continuations of periodic double pendulum oscillations from fixed points, showing bifurcations along orbit families and categorizing branches of periodic orbits. In particular, we find periodic orbits where both pendulum masses are never simultaneously at rest, which to our knowledge has been missing in the literature.

---


### 179. [Trust-Aware Adaptive Disclosure for Inference Privacy Preservation in Multi-Agent Networks](https://arxiv.org/abs/2609.05340)

**<font color=#1a73e8>作者：</font>** Puspanjali Ghoshal, Tobias J. Oechtering  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agent based systems are increasingly deployed in information critical systems including healthcare management systems, and smart grids. In this paper, we consider a multi-agent system where each agent has a latent goal that needs to be kept hidden from observing adversaries. More specifically, this paper studies privacy-preserving consensus in networked multi-agent systems under goal inference attacks. We propose a Trust-Aware Privacy Control framework that adapts message disclosure based on the dynamic trust relationships between agents. The proposed method controls information release using a trust-dependent stochastic policy. This enables a tradeoff between consensus performance and privacy preservation. Experiments demonstrate that the proposed method reduces adversarial goal inference accuracy compared to representative baselines, while maintaining competitive consensus utility, thereby highlighting the effectiveness of trust-aware mechanisms in privacy preservation of the agents in multi-agent systems.

---


### 180. [TherMosaic: Accelerating Perceived Thermal Transitions Through Spatiotemporal Thermal Feedback](https://arxiv.org/abs/2609.05347)

**<font color=#1a73e8>作者：</font>** Zining Zhang, Jiasheng Li, Myungin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Thermal feedback can enrich immersive interaction, but thermoelectric devices often change temperature too slowly to match interactive timing. We present TherMosaic, a spatiotemporal thermal feedback approach that accelerates perceived temperature transitions by leveraging two perceptual mechanisms: spatial summation and thermal adaptation. Focusing on the fingertip, we first investigate this approach using a custom 2*2 array of independently controlled Peltier modules. Across three controlled perceptual studies, we show that distributed thermal stimulation can preserve stable hot and cold percepts despite local deviations, that adaptation helps maintain these percepts during changing stimulation, and that combining these effects reduces perceived transition time by about 30%-40% for transitions originating from hot or cold states. We then translate the same design principles into a standalone wearable implementation of TherMosaic and evaluate it in virtual reality. Our results show that this approach reduces perceived thermal lag and improves temporal alignment between thermal and visual events in interactive use.

---


### 181. [Propagation Model for SSC attacks: Why SBOM (tools) don't tell the whole truth](https://arxiv.org/abs/2609.05380)

**<font color=#1a73e8>作者：</font>** Ljubica Grgic, Lazar Maksimovic, Pavel Laskov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ensuring security of software supply chains (SSC) is indispensable in today's world of modern software practices. SBOM (tools) have been introduced as relevant building blocks to ensure the transparency of SSCs. However they have serious limitations in practices as their vulnerability detection and interpretation capacity is not sufficient to explain exploitability effects that can propagte through the whole chain. To address this gap, we propose a propagation-centred approach to SSC security and introduce a four-stage propagation model. We empirically evaluate four open-source SBOM tools against each stage using three projects and Log4j vulnerability as our test case. Our results show that current SBOM tools systematically support only Stage 1 (Structural Exposure) and Stage 2 (Vulnerability Class Presence) while Stage 3 (Code Reachability) and Stage 4 (Taint Path Analysis) require capabilities absent from the SBOM ecosystem. We argue that putting propagation effects at the centre of SSC security research is essential to prevent cyber risk evolving into systemic risks. Our research findings contribute to a future research and design of modern SSC security tools.

---


### 182. [Reflection-aware Generative Novel View Synthesis](https://arxiv.org/abs/2609.05382)

**<font color=#1a73e8>作者：</font>** GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Ref-GeNVS, a training-free, reflection-aware method for generative novel view synthesis (NVS) in mirror scenes. Existing multi-view diffusion models often fail to recognize the mirror in the scene and cannot exploit reflected content for scene generation. To fix this issue without additional training, our key idea is to treat a mirror image as two complementary views. From input images, we estimate the mirror plane and reflect camera poses to form virtual views. Based on this virtual view setup, we propose a two-stage generation method consisting of Mirror-gated attention and Reflection injection, which enables reflection-consistent NVS by explicitly leveraging reflection relationships in a multi-view diffusion model. Ref-GeNVS inherits the strong generalizability of the multi-view diffusion backbone, while it does not require finetuning. On synthetic and real scenes including mirrors, Ref-GeNVS outperforms recent generative NVS methods by generating reflection-consistent and contextually coherent novel views, revealing scene structure visible only through mirrors. Project page: this https URL

---


### 183. [A Deep Generative Model for Synthesizing Labeled Wireless Signals](https://arxiv.org/abs/2609.05396)

**<font color=#1a73e8>作者：</font>** Yuxiao Li, Keke Hu, Santiago Mazuelas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wireless signals with position-related labels are pivotal for both performance evaluation and model training in the realm of wireless sensing. However, acquiring real-world datasets is often challenged by significant measurement and labeling costs. Traditional methods for synthesizing labeled wireless signals typically rely on environmental models, leading to extensive hyper-parameter tuning and inadequate realism for comprehensive model training purposes. To address these limitations, we introduce a novel deep learning (DL)-based method, namely Inter-Instance Generative Adversarial Networks (IIns-GAN), to generate realistic labeled wireless signals. The generated signals are particularly adaptive to different environment scenarios and well-suited for various model training tasks, including distance estimation and environment identification. We have conducted extensive experiments on public Ultra-Wideband (UWB) datasets to evaluate the realism and utility of the generated signals. The results demonstrate that the signals generated by IIns-GAN mirror the physical characteristics of real-world measurements, and significantly contribute to the improvement of model training in diverse wireless sensing tasks.

---


### 184. [CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation](https://arxiv.org/abs/2609.05397)

**<font color=#1a73e8>作者：</font>** Samer Abualhanud, Max Mehltretter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable 3D understanding of the surrounding environment is a core requirement for autonomous driving. Multi-view surround camera rigs provide broad scene coverage, but the spatially adjacent images typically overlap only minimally. Consequently, the depth of most pixels must be inferred from monocular appearance cues. These cues can appear differently across images and may therefore be interpreted differently by the depth estimation model. We target two main sources of cross-image inconsistency: differences in camera intrinsics and the limited receptive field of each image. We address the former by conditioning the features on per-pixel camera-aware ray embeddings, enabling the network to account for camera-dependent variations in monocular cues. We address the latter by extending each pixel's context beyond its own image through cross-image attention constrained to geometrically plausible regions, derived from the calibrated rig setup. The model is trained in a fully self-supervised manner based on photometric consistency. Evaluations on DDAD and nuScenes show improved overall depth accuracy and cross-image depth consistency over state-of-the-art self-supervised methods under in-domain and cross-domain evaluation. Code is available at this https URL.

---


### 185. [From Interpretability Methods to Interpretable Models](https://arxiv.org/abs/2609.05399)

**<font color=#1a73e8>作者：</font>** Julien Colin, Nuria Oliver, Thomas Serre  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> More than a decade in, explainable AI (XAI) for computer vision has assembled a mature toolbox: attribution, feature visualization, concept-based, and circuit-based methods. Yet almost all of the field's effort has gone into building and comparing these methods, and little into the question they were meant to answer---how interpretable are our models, and are we making progress as they evolve? We argue for shifting the field's focus from methods to models, along two complementary lines. One is already within reach: existing tools let us characterize and compare what different models represent and compute. The other is harder, and largely neglected: whether a model can actually be understood by the humans who rely on it---the independent evaluators on whom trust and certification depend, not the experts confirming what they already expect. It can only be measured, not inferred. We review why the toolbox is mature enough to support both, survey the thin body of work comparing models, draw a parallel to systems neuroscience, and close with a model-centric XAI agenda.

---


### 186. [A Generalizable Feature Extractor for Alzheimer's-Related Brain MRI Tasks](https://arxiv.org/abs/2609.05400)

**<font color=#1a73e8>作者：</font>** Reza Rajabli, D. Louis Collins  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When there is not enough labeled data to properly train deep learning models, transfer learning can help. We still do not fully understand how effective it is in neuroimaging, especially for Alzheimer's disease research. It is also not clear if these transferred models can work on new datasets without being retrained for each specific task. We evaluate whether a compact, supervised pretrained model can serve as a reusable foundation model for downstream neuroimaging tasks. We freeze the 7.18 million weights of a 3D CNN previously trained for brain-age prediction, and adapt it to each task using Low-Rank Adaptation (LoRA), requiring only ~1% additional trainable parameters. We evaluate generalizability in six experiments. Adapting the model to classify cognitively normal versus Dementia on ADNI gave an AUC of 0.964 on held-out folds (Experiment #1). Applying that adapted model unchanged to OASIS-3, with no retraining, gave an AUC of 0.871 (Experiment #2). Reusing its output logit together with age and a cognitive score distinguished stable from progressing MCI with an AUC of 0.828 (Experiment #3). Adapting the same backbone to predict amyloid positivity from structural MRI gave an AUC of 0.804 (Experiment #4). Finally, the same approach estimated ICV-normalized hippocampal and white matter hypointensity volumes directly from the T1w image, with R^2 of 0.80 and 0.91 respectively, tasks normally addressed with much larger U-Net networks (Experiments #5 and #6). A compact model supervised on brain age can therefore serve as a reusable backbone, adapting to each task with ~1% additional parameters and transferring to an unseen cohort without any training. Our findings suggest that a carefully trained brain age model can serve as an effective foundation model for Alzheimer's related tasks, even under strict data constraints.

---


### 187. [RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous Retail Environments](https://arxiv.org/abs/2609.05403)

**<font color=#1a73e8>作者：</font>** Quoc H. Nguyen, Ali Lafzi, Abhijeet Phatak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retail search systems serve diverse geographic regions with distinct query patterns, vocabularies, and product preferences, creating significant data heterogeneity that challenges both privacy-preserving training and model personalization. Federated learning offers a natural solution for privacy, but standard FL methods produce global models that sacrifice regional performance, while existing personalized FL approaches operate at the parameter level and catastrophically collapse on modern transformers (below 10\% accuracy on T5) due to tied embeddings and LayerNorm interactions. We introduce RegionFed, an \textit{architecture-robust} federated learning framework that sidesteps this failure by operating entirely at the gradient level. RegionFed uses the $\ell_2$ conflict between regional and global gradients as a unified signal that (i) diagnoses heterogeneity, (ii) routes each region to the cheapest sufficient personalization strategy, and (iii) adaptively controls personalization strength. Because it treats models as differentiable black boxes, RegionFed deploys on T5-Small, T5-3B, RoBERTa, and CNN with zero code changes, providing large gains on transformers (where parameter-level methods collapse) and consistent improvements on CNNs. Across three public datasets (Amazon ESCI, Amazon Reviews, LEAF-FEMNIST) and four architectures, RegionFed-Meta achieves 92.27\%, closing the gap to the privacy-violating centralized upper bound (Centralized + Regional Weighting: 92.04\%, $\Delta$=0.23pp, within 1$\sigma$) while providing $(\epsilon{\approx}0.60)$-differential privacy and $\mathcal{O}(1/\sqrt{T})$ convergence.

---


### 188. [Diffusion TV: Experiencing Diffusion Models through Tangible, Embodied Interaction](https://arxiv.org/abs/2609.05404)

**<font color=#1a73e8>作者：</font>** Sihwa Park  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Diffusion TV is an interactive AI art installation that offers a tangible and embodied experience of diffusion models through a modified CRT TV. By physically manipulating the TV's antenna, audiences control the clarity of AI-generated images and sounds, metaphorically enacting the denoising process that underlies diffusion-based generation. Using the tuning knob, participants switch between three channels featuring AI-generated animals from the Past (extinct species), Present (endangered species), and Future (speculative creatures), situating the interaction within a temporal and ecological narrative. Through continuous audiovisual feedback and physical interaction, Diffusion TV foregrounds the generative process over final outputs, allowing audiences to explore intermediate states as experiential material. Rather than providing explicit technical explanation, the work presents an alternative, embodied mode of explainable AI that invites exploratory engagement with and reflection on generative technologies.

---


### 189. [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415)

**<font color=#1a73e8>作者：</font>** Linzhan Mou, Jiahui Lei, Zhiyang Dou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in automatic rigging now deliver animation-ready 3D assets at scale, yet generating the motion to drive them remains a bottleneck. Existing learned animators are topology-constrained: they rely on category-specific templates or require per-skeleton fine-tuning and reference motions at inference. We present UniMate, a unified foundation model that synthesizes articulated motion for arbitrary skeletons from a rigged 3D asset and a text prompt, with no test-time optimization or per-skeleton retraining. UniMate introduces a topology-aware diffusion transformer, which integrates skeletal topology into attention via three mechanisms: (1) a graph-aware attention bias from pairwise joint relations and geodesic distances; (2) a spectral rotary position embedding generalizing RoPE to arbitrary kinematic trees via the graph Laplacian; and (3) a global topological conditioner attention-pooled from the rest-pose skeleton. We also curate UniML3D, 13,006 motion sequences spanning bipedal, quadrupedal, avian, marine, insectoid, serpentine, and articulated rigid objects with unified canonicalization and text pairing. Trained on this dataset, UniMate outperforms state-of-the-art baselines in quality, generalization, and efficiency, and supports zero-shot cross-topology transfer, in-betweening, expansion, and text-guided editing. Our project page is available at this https URL.

---


### 190. [WorldSculpt: Generating Compositional Worlds from Grounded Videos](https://arxiv.org/abs/2609.05416)

**<font color=#1a73e8>作者：</font>** Muyao Niu, Jixuan He, Ruihan Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics. This task is challenging in densely cluttered scenes, where objects heavily occlude one another and each view reveals only a fraction of their geometry. Geometry-based approaches typically reconstruct the scene as a single representation and leave incomplete geometry in occluded regions, while existing compositional methods with generative priors are largely limited to relatively simple scenes. We show that complex scenes with hundreds of objects can instead be generated compositionally by adapting a strong single-object 3D generative prior to multi-view observations. We instantiate this paradigm with Pixal3D, extending it with a multi-view conditioning pathway that grounds object generation in multiple posed observations. Although the model is finetuned entirely on single objects in canonical space, it generalizes to large scenes with severe occlusion without any scene-level training, demonstrating the feasibility and scalability of this paradigm. We further introduce UE-MeshyScene, a photorealistic benchmark of densely cluttered scenes with hundreds of objects, per-object annotations, and ground-truth meshes. Across single-object, controlled multi-object, and UE-MeshyScene evaluations, our method consistently outperforms prior approaches, with larger gains as scene complexity and occlusion increase. Finally, we demonstrate broader applicability by converting generated 3DGS worlds, such as Marble and HY-World 2.0, into compositional mesh scenes.

---


> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
