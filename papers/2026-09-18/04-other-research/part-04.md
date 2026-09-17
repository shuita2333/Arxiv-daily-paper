# 📦 其他研究 | 2026年09月18日

> 本类共 **223** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-223](./part-05.md)

---

### 151. [AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution](https://arxiv.org/abs/2609.18520)

**<font color=#1a73e8>作者：</font>** Jiabin Lou, Yirong Yang, Haopeng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective intelligence is a collaborative autonomy paradigm in which multiple agents pursue shared objectives through local perception, information exchange, and coordinated action. UAV swarms embody this paradigm by coordinating multiple vehicles in tasks such as search, inspection, and tracking. Recent advances in large language model (LLM) agents have strengthened natural-language task understanding and high-level planning, providing a flexible semantic interface between mission descriptions and collective behavior. While these advances expand semantic reasoning, applying LLM agents to UAV swarms raises challenges in grounding model decisions in executable capabilities, reconciling global task reasoning with distributed execution, and using mission-specific experience for continual adaptation. To address these challenges, we introduce AeroWeaver, an embodied-agent harness that weaves individual UAV skills into coordinated mission-level behavior. AeroWeaver connects semantic decisions to governed skills, organizes role-conditioned local agents for distributed coordination, and uses role-indexed state-action-reward experience to refine skill selection online. Experiments and runtime validation show that AeroWeaver maintains valid skill execution under tested conditions and supports body-local multi-UAV operation without a central agent generating joint actions from global context, while reward-guided online updates provide a training-free path for adaptive learning swarm agents from accumulated execution experience. Code: this https URL.

---


### 152. [TRIPROBE: Probing Task Separability Beyond Classification for XAI](https://arxiv.org/abs/2609.18525)

**<font color=#1a73e8>作者：</font>** Amirhossein Sadough, Freek Hens, Aleksa Bokšan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern evaluation of learning pipelines often reduces to downstream accuracy, leaving open the question of why tasks succeed or fail. TriProbe addresses this gap with a multi-level probing framework for explainable diagnosis of task separability. Rather than treating models as black boxes, TriProbe traces how separability evolves across inputs, learned features, and final classifiers. It decomposes multi-task problems into binary subtasks and applies three complementary probes: a Foundational Probe on input spaces, a Latent Probe on feature representations, and a Final Probe on classifier outputs. Using Maximum Fisher's Discriminant Ratio as a principled separability metric, TriProbe identifies bottlenecks and affected task pairs. Experiments on the Roshambo sEMG benchmark show how TriProbe reveals hidden breakdowns, guiding data collection, validation, and architecture design.

---


### 153. [Provable Guarantees for Spectral Structured Prediction](https://arxiv.org/abs/2609.18527)

**<font color=#1a73e8>作者：</font>** Violet Zheng, Jean Honorio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured prediction is the simultaneous prediction of multiple labels, and is widely used in various fields, such as natural language processing and computer vision. In this paper, we study binary node label recovery on signed graphs with edge-flip noise, a model introduced by (Globerson et al., 2015), via a simple spectral method that decodes node labels from the signs of the principal eigenvector of the noisy signed adjacency matrix. We develop graph structure-agnostic theoretical guarantees for approximate inference of node labels as well as guarantees for maximum angle deviation with respect to the ground truth node labels. By leveraging tools from matrix concentration theory and eigenvector perturbation analysis, we derive new concentration inequalities that explicitly quantify the effect of the spectral gap of the adjacency matrix, number of nodes, degree distribution, and noise level. As a corollary, we relate our general results to the Cheeger constant and provide results for different classes of graphs. We perform several synthetic experiments to validate our theory. To the best of our knowledge, we are the first to provide theoretical guarantees for the spectral-based approach. As a byproduct of our analysis, we derive technical results that might be of independent interest and useful for other machine learning problems.

---


### 154. [A Probe Shift Is Not a Fairness Fix: The Limits of Representation Steering in Speech Models](https://arxiv.org/abs/2609.18533)

**<font color=#1a73e8>作者：</font>** Nicolas Bourrel, Abderrahmane Issam, Gerasimos Spanakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems exhibit unequal error rates across speaker groups, motivating interventions on their internal representations. We ask whether speaker-linked attributes that are linearly readable from pretrained ASR encoders yield useful directions for reducing group word-error-rate (WER) gaps. Across Whisper-medium, HuBERT-large, and Wav2Vec2-large on Common Voice and the Speech Accent Archive, we probe every encoder layer for metadata-derived sex/gender, age, and native/accent labels; construct centroid and probe-derived directions; inject them at selected layers; and compare downstream probe trajectories with matched WER changes. Sex labels are highly decodable (best macro-F1 0.924--0.941), native/accent labels are also above chance (0.544--0.696), and age is weaker (0.354--0.397). Of 22 post-selected reruns, nine have 95% paired-bootstrap intervals entirely below zero, yet every absolute source-group WER reduction is below 0.7 percentage points. Conversely, a local target-class probe rate can rise from 8.09% to 99.87% while WER worsens. Linear readability is therefore neither evidence of causal use nor a reliable mitigation method. Our results motivate evaluating speech-bias interventions jointly at representation, propagation, and task levels.

---


### 155. [Provable Guarantees and Efficient Learning of Structural Equation Models with Latent Confounders](https://arxiv.org/abs/2609.18535)

**<font color=#1a73e8>作者：</font>** Weijian Yu, Jean Honorio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery aims to recover causal relationships from observed data. In various fields, exploring causal relationships among variables remains an important topic, but this task becomes challenging due to the existence of latent confounders. Ignoring such confounders can lead to false associations and incorrect edge directions. In this paper, we study the linear structural equation model with latent confounders. We propose an algorithm that iteratively identifies terminal (observed) nodes and reconstructs the directed acyclic graph of the observed variables. To do this, we recover the precision matrix of the observed variables as a sparse plus low-rank matrix: a sparse matrix captures the conditional dependencies among observed variables, while a low-rank matrix captures the combined influence of a few latent confounders. We establish that for $p$ observed variables, $r$ latent confounders and $s$ edges, our procedure correctly identifies the directed causal relationship among observed variables, for $n \gtrsim \max\{s\log p,\ r p\}$ samples. Experimental results validate our theoretical contributions.

---


### 156. [Accuracy- and Real-Time-Aware 4D Radar Preprocessing for Autonomous Driving Perception Systems](https://arxiv.org/abs/2609.18542)

**<font color=#1a73e8>作者：</font>** Woo-Jin Jung, Dong-Hee Paek, Jeong-Su Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D radar has emerged as a promising next-generation sensor for improving the robustness of autonomous driving perception systems because of its stable sensing capability under adverse weather conditions. However, deploying 4D radar in embedded environments with limited hardware resources requires radar-representation preprocessing that jointly considers perception accuracy, real-time performance, and computational complexity. This paper proposes a preprocessing framework for 4D-radar-based 3D object detection. First, Percentile-based 3D Shape Preservation (P3DP) extracts point clouds from radar tensors while preserving object-shape information and suppressing noise and false alarms. Second, Multi-frame-based Noise Point Discrimination using Kernel Density Estimation (MF-KDE) improves the density and reliability of sparse radar point clouds. Finally, Embedded \& NetScore (ENS) evaluates suitability for embedded deployment by jointly considering accuracy, real-time performance, adverse-weather robustness, and model complexity.

---


### 157. [Revisiting the Objective of Echo Chamber Detection](https://arxiv.org/abs/2609.18545)

**<font color=#1a73e8>作者：</font>** Abylaikhan Bexeit, Kushani Perera, Shanika Karunasekera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the detection of an echo chamber in a social network, i.e., the identification of a set of nodes that agree on a topic, while disagreeing with the rest of nodes. We argue that this problem is different from other social network analysis problems such as community detection, and from other graph problems such as maximum graph cut and maximum clique. To the best of our knowledge, we are the first to formalize the objective function of echo chamber detection, by using the theory of Fourier transforms of set functions (Stobbe and Krause, 2012). We propose scalable semidefinite relaxation, solved via an interior point method and sparse linear algebra. Experimentally, our algorithm recovers the ground truth echo chamber better than competing methods on small synthetic experiments. Our algorithm produces echo chambers with better network properties than competing methods on large real-world datasets. To independently validate our proposed objective function, we show that our algorithm finds echo chambers with more agreements with suspended users than competing methods on a small real-world dataset.

---


### 158. [STUNet-Fusion: Spatiotemporal Needle-Tip Localization in Ultrasound Video via Multi-Channel Motion Fusion](https://arxiv.org/abs/2609.18546)

**<font color=#1a73e8>作者：</font>** Chia-Chi Hsu, Chia-Hsuan Hsu, Che-Chou Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Needle-tip localization in ultrasound remains challenging because the needle may appear weak, discontinuous, or partially invisible, while imaging artifacts and anatomical structures can produce similar responses. To address this problem, we propose STUNet-Fusion, a spatiotemporal framework for needle-tip localization in ultrasound videos. The proposed method formulates the input as a tri-channel spatio-temporal fusion tensor, comprising grayscale appearance, grid-based motion feature, and raw frame difference. A shared ResNet-34 encoder extracts spatial features, ConvLSTM integrates temporal dependencies, and a U-Net decoder reconstructs a dense probability heatmap. The final coordinates are extracted via a soft-argmax operation to achieve sub-pixel localization accuracy. Experimental results demonstrate that this spatiotemporal fusion strategy significantly improves localization robustness compared to conventional baselines.

---


### 159. [HAP: A Hand-Driven Active Perception Framework for Egocentric Head Motion Prediction](https://arxiv.org/abs/2609.18548)

**<font color=#1a73e8>作者：</font>** Yunji Feng, Junyi Ma, Guanzhong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric motion forecasting has primarily focused on hands and manipulated objects, leaving future human head motion comparatively underexplored. During manipulation, the head both redirects perception toward the target to acquire task-relevant evidence and coordinates with body and hand motion. We therefore formulate future six Degree of Freedom (6-DoF) head-motion prediction conditioned on observed hand motion and inferred target context, and propose HAP, a Hand-Driven Active Perception framework. HAP infers confidence for each target object from observed hand motion and object geometry. Then constructs a dynamic Predictive Target-Centric Amodal Occlusion Graph (P-TAOG) representing current and potential occlusion among candidate objects. Directed graph and causal temporal reasoning encode the evolving target conditioned perceptual state, which is fused with hand and head motion history. A horizon-wise gate then blends the learned trajectory with a constant velocity prior. We further introduce Bottle, an egocentric RGB-D dataset of object manipulation toward specified targets, with coordinated head and hand motion under changing target visibility. Experiments on the public dataset and Bottle show that HAP achieves lower head motion prediction errors than representative baselines, supporting the value of hand driven intention and dynamic occlusion reasoning for anticipating human head motion. Code will be released at this https URL.

---


### 160. [CARA: Collision-Aware Resolution Adaptation for Multiresolution Hash Encoding Based Image Fitting](https://arxiv.org/abs/2609.18554)

**<font color=#1a73e8>作者：</font>** Linfeng Ye, Zhixiang Chi, Shayan Mohajer Hamidi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiresolution hash encodings have recently enabled fast and high-fidelity implicit neural representations by storing multi-scale features in fixed-size hash tables along a geometric resolution schedule. However, the standard design is data-agnostic: different resolution levels receive identical hash-table capacity despite large differences in image frequency content. As a result, some levels experience severe hash collisions while others underutilize parameters, leading to inefficient capacity allocation. To address this issue, we propose Collision-Aware Resolution Adaptation (CARA), a method that assigns per-level resolutions by balancing the effective information load across hash levels. This adaptive allocation reduces capacity bottlenecks and improves parameter efficiency. In addition, we introduce an invertible pixel-shuffle transform that reduces hash load factors by redistributing spatial information, thereby mitigating collision-induced information loss without enlarging the hash tables. To support evaluation on extremely high-resolution data, we also curate, to the best of our knowledge, the first uncompressed whole-slide image dataset for academic research. Experiments on Kodak images, gigapixel natural images, and raw whole-slide images demonstrate that CARA consistently improves the fidelity-parameter trade-off. Our method matches state-of-the-art performance while using only $27.76%$ of the parameters, and achieves up to $6.11$ dB PSNR improvement at comparable parameter counts. Code is provided in the supplementary.

---


### 161. [Interpretable Patch-Based Deep Learning for Wildfire Spread Prediction from Ensemble Simulations](https://arxiv.org/abs/2609.18555)

**<font color=#1a73e8>作者：</font>** Marcin Lawenda, Aleksandra Krasicka, David Caballero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfire spread is traditionally predicted using physics-based simulators, which are physically interpretable but whose cost increases with each additional ensemble member. We ask how well deep learning surrogates can reproduce these simulations at a fraction of this cost, training them on 10,584 fire spread simulations at 2m resolution for the Rectoret region in Catalonia, Spain. Four architectures are compared: a patch-based U-Net, a transfer-learned ResNet-50, a physics-informed network constrained by the wind-driven advection equation and a Swin-Unet transformer. Among the terrain and vegetation variables, only surface fuel load predicts burn probability with any strength (r = 0.27) and including it lowers prediction error by 21%. The remaining variables correlate weakly and are highly duplicative. Next, an experiment with saliency, occlusion and rotation demonstrates the models' learning. Convolutional models rely primarily on distance from the current fire front, while Swin-Unet assigns more weight to fuel and terrain, a finding also noted in an unrelated wildfire dataset. When applied without retraining to the second region, Pedriza, all three convolutional models still predict fire spread, losing accuracy by a small but systematic margin.

---


### 162. [Accurate Trace Estimation with Fewer Random Bits via Recursive TensorSketch](https://arxiv.org/abs/2609.18577)

**<font color=#1a73e8>作者：</font>** Mohammad Azhar Khan, Rameshwar Pratap, Amit Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of estimating the trace of an implicit matrix $\mathbf{A} \in \mathbb{R}^{d^p\times d^p}$ that can only be accessed through matrix-vector products queries. The \textit{Hutchinson trace estimator}% ~\cite{Girard1987algorithme, article-hutchinson} is a classical sketching method for this problem. Their estimator, $H_{m}(\mathbf{A}) = \frac{1}{m} \sum_{i=1}^{m} {\mathbf{z}^{(i)}}^T \mathbf{A} \mathbf{z}^{(i)}, \quad \text{where } \ {\mathbf{z}^{(i)}}\in \mathbb{R}^{d^p}$, and $z^{(i)}_j \in {N}(0, 1), j\in [d^p]$, satisfies the following guarantees: (i) $\mathbb{E}[H_{m}(\mathbf{A})]=\operatorname{tr}(\mathbf{A})$, and (ii) $\mathrm{Var}[H_{m}(\mathbf{A})]=\frac{2}{m}||\mathbf{A}||_F^2$. Generating one query vector $\mathbf{z}^{(i)}$ requires $O(d^p)$ random bits; thus, $m$ queries require $O(md^p)$ random bits, which can be prohibitive in large-scale applications. Recent work by Meyer et al.~\cite{meyer2025hutchinsonsestimatorbadkroneckertraceestimation} proposes a variant of the Hutchinson trace estimator in which each query vector in $\mathbb{R}^{d^p}$ is constructed as the Kronecker product of $p$ random vectors in $\mathbb{R}^d$, requiring $O(mpd)$ random bits for $m$ query vectors. The estimator of~\cite{meyer2025hutchinsonsestimatorbadkroneckertraceestimation} is unbiased; however, its variance grows exponentially with $p$. In this work, we address this limitation by proposing a sketching-based estimator that requires $O\!\big(p (d + m)\log m\big)$ random bits, yields an unbiased estimate of the trace, and simultaneously achieves a variance bound that grows polynomially with $p$.

---


### 163. [Learning Where to Focus: Self-Supervised Multi-Scale ViTs for Histopathology](https://arxiv.org/abs/2609.18578)

**<font color=#1a73e8>作者：</font>** Anabel Stammer, Valay Bundele, Mehran Hosseinzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathologists diagnose diseases by first locating suspicious tissue and then examining it at higher magnification, whereas self-supervised vision transformers (ViTs) allocate the same spatial resolution to every image region despite diagnostic evidence being sparse and spanning multiple biological scales. Recent pathology foundation models have substantially improved representation quality by scaling training data and model capacity, but largely retain uniform tokenization. We instead investigate whether pathology representations can be improved by learning where to allocate spatial resolution during self-supervised learning. To this end, we propose CRAFT (Coarse-to-fine Region-Adaptive Feature Tokenization), a DINO-based framework that learns image-dependent mixed-scale representations by using self-supervised attention to selectively refine informative regions while preserving coarse context, together with a symmetric cross-scale regularization objective that encourages complementary coarse and fine representations. Across CAMELYON16, TCGA-Lung subtype classification, and TCGA-LUAD survival prediction, CRAFT consistently outperforms comparable-scale self-supervised methods while requiring lower inference computation. Despite using only a compact 22M parameter backbone trained on comparatively small pathology datasets, CRAFT remains competitive with, and often surpasses, substantially larger pathology foundation models.

---


### 164. [On-the-Fly Homographies Calibration for Multi-Camera Tracking](https://arxiv.org/abs/2609.18582)

**<font color=#1a73e8>作者：</font>** David Voihanski, Mor Sinai, Ben Zion Bobrovsky  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise multi-camera tracking traditionally relies on rigorous 3D site calibration, yet this requirement is often operationally impossible in large-scale deployments. Privacy regulations frequently prohibit recording video for offline calibration; limited bandwidth precludes synchronizing high-resolution streams from hundreds of cameras; and covering immense physical sites with calibration targets is logistically infeasible. We present a multi-camera homography calibration system designed to overcome these barriers through "on-the-fly" geometric refinement. Starting from coarse manual homographies, we introduce a centroid-based projection optimization (PO) that continuously aligns the ground-plane geometry using live detection streams. Because PO operates asynchronously on already-transmitted, lightweight metadata, it adds zero computational latency to the real-time tracker. This allows the system to adapt automatically to camera movements or environmental changes without human intervention. This optimized geometry feeds a multi-camera bird's-eye-view (BEV) tracker that fuses detections and unifies trajectories across zones. Crucially, by operating strictly on live anonymous metadata, our solution ensures a privacy-safe, zero-overhead, and resilient tracking pipeline that maintains global consistency in dynamic environments where static, recorded-video calibration is impossible.

---


### 165. [Label-free steering: Compressing test-time reinforcement learning into bias-only subspaces](https://arxiv.org/abs/2609.18587)

**<font color=#1a73e8>作者：</font>** Naveen Vakada, Mingyuan Li, Shaoxiong Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning (TTRL) enables models to improve their reasoning without relying on labeled training data, but existing approaches typically optimize a large fraction of the model parameters. This raises a natural question: can effective test-time adaptation emerge when both the reward signal and the optimization space are severely restricted? We answer this question with label-free bias-only TTRL, which uses majority-vote pseudo-labels as rewards and optimizes only approximately 100K bias parameters while keeping the pretrained backbone frozen. On MATH-500, our approach reaches 76.67% accuracy, slightly exceeding our own labeled bias-steering reproduction while optimizing 76,000x fewer parameters than full-parameter TTRL. The same training procedure improves performance across vision-language and audio reasoning tasks, including MathVista, AI2D, LogicVista, and MMAU. We further show that the learned steering vectors transfer to 4,500 held-out MATH problems, indicating that the adaptation is not limited to the problems used during test-time optimization. Finally, we analyze why this highly restricted adaptation can work, showing that majority-vote reliability improves with rollout consensus and that bias subspaces with greater accessible gradient energy exhibit stronger downstream trainability. These results demonstrate that substantial test-time adaptation can emerge from optimizing a tiny bias-only subspace using entirely label-free rewards.

---


### 166. [Peak-Aware Short-Term Load Forecasting Across Distribution Grid Aggregation Levels](https://arxiv.org/abs/2609.18588)

**<font color=#1a73e8>作者：</font>** Souhardya Chattopadhyay, Julian Oelhaf, Antonia Schoening 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For distribution system operators, short-term load forecasting (STLF) supports congestion management, voltage control, and asset protection. Most existing approaches focus on overall accuracy across all time steps and neglect performance during high-demand (HD) periods, where larger forecast errors can increase the risk of congestion and voltage violations. In this paper, we study peak-aware STLF across three operator-relevant distribution grid aggregation levels, area codes (AC), secondary substations (SUB), and low-voltage (LV) feeders, using open datasets from the United Kingdom and Switzerland. We compare statistical baselines, machine learning models (LightGBM and XGBoost), and recent time-series foundation models (Chronos Bolt and Chronos-2) under a peak-aware evaluation framework that reports both overall and HD forecasting performance using NMAE and MAPE. The results show that Chronos-2 achieves the best HD performance across all aggregation levels, with HD-NMAE and HD-MAPE of 0.039 and 4.53% at AC, 0.080 and 9.45% at SUB, and 0.138 and 16.14% at LV, while Chronos-Bolt consistently ranks second best. Compared with the gradient boosted ML models, Chronos-2 reduces mean HD-NMAE by about 20-51% across levels while remaining best or near-best on the overall metrics. A quantile analysis of the probabilistic Chronos outputs further identifies aggregation-specific operating points, and runtime measurements indicate that foundation model inference is fast enough for practical deployment. Overall, the findings highlight peak-aware evaluation and aggregation specific quantile selection as a practical pathway toward more operationally relevant STLF in distribution networks.

---


### 167. [ReDIL-GNN: Resynthesis Domain Incremental Learning for Circuit Graph Neural Networks](https://arxiv.org/abs/2609.18595)

**<font color=#1a73e8>作者：</font>** Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Logic resynthesis preserves circuit functionality while changing gate vocabulary, topology, and structural statistics, creating domain shift for circuit graph neural networks (GNNs) without changing task labels. To study this setting, we introduce ReDIL-GNN, a resynthesis domain-incremental learning framework that adapts a fixed prediction or representation head as new synthesis styles arrive and evaluates retention on all previously observed domains. Because not every shift should be adapted blindly, ReDIL-GNN further introduces the Resynthesis Adaptability Index (RAI), a pre-adaptation score that combines adaptation need, source-equivalence recoverability, structural coverage, and update compatibility. We evaluate supervised hardware-security tasks and representation-learning models using task-native metrics for classifiers and source-equivalence retrieval metrics for embedding models, comparing naive fine-tuning with LwF, Online EWC, MAS, ER, A-GEM, DER++, ER+LwF, and equivalence-guided replay. Across the studied pipelines, RAI separates unsupported shifts from promising updates, ranging from 0.001 for a structurally uncovered GNN-RE ABC-rewrite shift to 0.824 for the best original-only GNN-RE adaptation case. In practice, ReDIL-GNN turns resynthesis-aware circuit learning into a deployment control loop: RAI screens each new synthesis flow before update, guiding whether to reuse the current model, apply retention-aware adaptation, or defer adaptation until the shift is better supported.

---


### 168. [Online Robust Reinforcement Learning Through Monte-Carlo Planning](https://arxiv.org/abs/2609.18599)

**<font color=#1a73e8>作者：</font>** Tuan Dam, Kishan Panaganti, Brahim Driss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte Carlo Tree Search (MCTS) is a powerful framework for solving complex decision-making problems, yet it often relies on the assumption that the simulator and the real-world dynamics are identical. Although this assumption helps achieve the success of MCTS in games like Chess, Go, and Shogi, the real-world scenarios incur ambiguity due to their modeling mismatches in low-fidelity simulators. In this work, we present a new robust variant of MCTS that mitigates dynamical model ambiguities. Our algorithm addresses transition dynamics and reward distribution ambiguities to bridge the gap between simulation-based planning and real-world deployment. We incorporate a robust power mean backup operator and carefully designed exploration bonuses to ensure finite-sample convergence at every node in the search tree. We show that our algorithm achieves a convergence rate of $\mathcal{O}(n^{-1/2})$ for the value estimation at the root node, comparable to that of standard MCTS. Finally, we provide empirical evidence that our method achieves robust performance in planning problems even under significant ambiguity in the underlying reward distribution and transition dynamics.

---


### 169. [A Geometric Theory of Decision Boundaries in Structured Markov Decision Processes](https://arxiv.org/abs/2609.18610)

**<font color=#1a73e8>作者：</font>** Fredy Pokou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical dynamic programming represents optimal sequential decisions through value functions and policies. While this functional representation is natural for computing optimal decisions, it does not directly identify the mathematical object governing policy reconstruction, representation complexity, or oracle-query complexity once an optimal policy is fixed. This paper addresses this question by developing a geometric theory of structured optimal policies in which the decision-boundary geometry induced by the policy becomes the primary object of analysis. We show that, under suitable structural regularity conditions, this geometry provides the minimal representation required for policy reconstruction and determines the statistical and computational complexity of the reconstruction problem. Building upon this representation, we establish structural properties of policy-induced decision geometry, introduce intrinsic notions of boundary and decision complexity, derive information-theoretic measures of decision compression, and obtain statistical guarantees for boundary estimation and policy reconstruction from black-box policy queries. Collectively, these results demonstrate that, for the structured decision problems considered here, the complexity of policy reconstruction is governed by the geometry of the decision boundary rather than by the cardinality of the ambient state space. Controlled numerical experiments examine the principal theoretical predictions and provide empirical evidence consistent with the proposed framework.

---


### 170. [How Many Labels Does Model Choice Need? Certificates and Budgets for Selective Prediction](https://arxiv.org/abs/2609.18622)

**<font color=#1a73e8>作者：</font>** Tetsuji Kuboyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifiers can make identical predictions yet require labels to compare their selective performance: confidence ranks weight the same errors differently. We quantify this requirement for the area under the generalized risk-coverage curve (AUGRC). A prelabel lower bound rules out insufficient budgets. With all labels known, a covering linear program bounds the minimum number of labels sufficient to fix the winner (the certificate size) within $K-1$ labels for $K$ candidates. For fixed $K$, independent uniform orders and identical predictions, the prelabel bound approaches one quarter of the pool. With iid Bernoulli errors independent of the orders, every exact acquisition policy reads almost all labels asymptotically, although a two-candidate certificate needs only half. Across 108 feature-panel comparisons on nine datasets, disagreement labels settle every accuracy choice but no AUGRC choice. A 20% budget is ruled out in 96 conditions; certificates need 56-57% on average. On ten conditions with pretrained image classifiers, confidence-score choice reads 68-91% of 10,000 labels for exact selection and 50-67% with AUGRC tolerance $5\times10^{-4}$. An exact stopping test works with any acquisition order. Together, these results link confidence ranks to label budgets and certified model comparison.

---


### 171. [GenStream: Semantic Streaming Framework for Generative Reconstruction of Human-centric Media](https://arxiv.org/abs/2609.18634)

**<font color=#1a73e8>作者：</font>** Emanuele Artioli, Daniele Lorenzi, Shivi Vats 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video streaming dominates global internet traffic, yet conventional pipelines remain inefficient for structured, human-centric content such as sports, performance, or interactive media. Standard codecs re-encode entire frames, foreground and background alike, treating all pixels uniformly and ignoring the semantic structure of the scene. This leads to significant bandwidth waste, particularly in scenarios where backgrounds are static and motion is constrained to a few salient actors. We introduce GenStream, a semantic streaming framework that replaces dense video frames with compact, structured metadata. Instead of transmitting pixels, GenStream encodes each scene as a combination of skeletal keypoints, camera viewpoint parameters, and a static 3D background model. These elements are transmitted to the client, where a generative model reconstructs photorealistic human figures and composites them into the 3D scene from the original viewpoint. This paradigm enables extreme compression, achieving over 99.9% bandwidth reduction compared to HEVC for the continuous data stream. We partially validate GenStream on Olympic figure skating footage and demonstrate potential for high perceptual fidelity under minimal data. While acknowledging the significant computational costs shifted to the client and challenges in generalization, GenStream opens new directions in volumetric avatar synthesis, canonical 3D actor fusion across views, and personalized viewing experiences, laying the groundwork for scalable, intelligent streaming in the post-codec era.

---


### 172. [CoRe-MARL: Cooperative Redistribution Under Unknown Dynamics Using Recurrent Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.18639)

**<font color=#1a73e8>作者：</font>** Naimur Rahman Chowdhury, Shatabdi Sen Prapti, Md. Salehin Seyam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergency management assistance programs, such as relief distribution, are essential for delivering necessary supplies to affected communities. However, these programs operate in a decentralized network of local centers that face uncertain local demand and supply dynamics, resulting in inconsistent avail- ability of local services. Redistribution of supplies among these local centers reduces these imbalances, but the centers often make decisions independently, with limited information and disrupted transportation. This study develops CoRe-MARL, a cooperative multi-agent reinforcement learning (MARL) framework, by formulating a decentralized partially observable Markov decision process (Dec-POMDP). We treat each center as an agent that learns a redistribution policy to improve the service in the worst-case region and reduce the service gap across regions while protecting network-wide service. We incorporate a recurrent network that captures evolving supply and demand dynamics without direct observation, while multi-agent proximal policy optimization (MAPPO) enables centralized training and decentralized execution (CTDE). We evaluate the framework in a simulated environment with diverse trajectories, where exact dynamics are not observed by actors and the MAPPO critic. We compare the recurrent MAPPO with the recurrent independent PPO (IPPO) and a local only heuristic, and find that MAPPO reduces the service gap across local centers and enhances service for the worst-served center while maintaining competitive network-wide service. The recurrent MAPPO also shows consistent performance across diverse trajectory patterns, demonstrating its ability to adapt to evolving dynamics. The findings demonstrate the capability of cooperative learning for decentralized redistribution and improving equitable service under uncertain and evolving dynamics.

---


### 173. [Learning to Program Adaptive Non-Local Observables for Machine Learning](https://arxiv.org/abs/2609.18655)

**<font color=#1a73e8>作者：</font>** Yu-Ting Lee, Samuel Yen-Chi Chen, Huan-Hsin Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum neural networks (QNNs) are typically built from variational quantum circuits (VQCs), which are limited by local measurements. Adaptive non-local observables (ANO) address this by jointly optimizing circuit parameters and multi-qubit measurements. However, existing ANO-based VQCs learn only a single static observable that remains invariant across all inputs. We propose QFWP-ANO, a novel architecture which employs a classical hypernetwork to dynamically program VQC parameters and/or non-local observables conditioned on each input. On multivariate time-series forecasting across four ETT datasets, QFWP-ANO achieves the lowest MSE in 16 of 20 settings and second-lowest in the remaining four, surpassing ANO-based and other strong baselines. On reinforcement learning tasks, QFWP-ANO consistently surpasses ANO-VQCs. Our results establish input-conditioned ANO as an effective approach for enhancing QNNs.

---


### 174. [Revisiting Distributed Sign-Based Variance Reduction](https://arxiv.org/abs/2609.18656)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Zechao Li, Lijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sign-based methods reduce communication costs in distributed environments, but aggregating local signs can introduce bias when data are heterogeneous. As a result, existing sign-based variance reduction methods fail to obtain the optimal convergence rates. In this paper, we solve this problem and obtain optimal rates for both nonconvex stochastic and finite-sum optimization. We first give a counterexample showing that majority voting can fail to approach stationary points even with exact local gradients. Motivated by this limitation, we propose tracking the global gradient at the server through unbiased compression of recursive gradient increments. As a result, we can obtain the convergence rates of $O(\sqrt{d/K}+\sqrt d (a/(nK))^{1/3})$ for the $\ell_1$-norm and $O(\sqrt{a/K}+\sqrt a/(nK)^{1/3})$ for the $\ell_2$-norm. Here, $K$ is the iteration number, $n$ is the number of workers, $d$ is the dimension, and $a=1+\omega$, with $\omega$ denoting the compressor's relative variance. For finite-sum problems with $M$ components, we combine periodic exact gradient refreshes with compressed component-gradient differences. The resulting total sample complexities are $O(M+d\sqrt{aM}\epsilon^{-2})$ and $O(M+a\sqrt M\ epsilon^{-2})$ for $\ell_1$ and $\ell_2$ gradient norms at most $\epsilon$, matching the corresponding bounds in centralized settings.

---


### 175. [A Security Risk Assessment Framework for AI-Powered Development Tools](https://arxiv.org/abs/2609.18658)

**<font color=#1a73e8>作者：</font>** Salem AlJanah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-powered development tools are now widely used to generate code and assist developers with routine programming tasks. Although existing work has identified vulnerabilities in AI-generated code, security-oriented work is often focused on vulnerability detection rather than risk assessment. To address this gap, this paper presents a Security Risk Assessment Framework (SRF) to evaluate the security risks of AI-generated code. SRF combines threat modeling, security analysis, and a quantitative risk evaluation approach based on vulnerability criticality. The framework is applied to a set of security-relevant programming tasks, where code generated by multiple AI-powered development tools is analyzed using Bandit and Semgrep. The results show that AI-generated code can introduce security vulnerabilities across all evaluated tools. They also show that risk levels vary by task type, as input processing and file handling tasks showed higher risk, while simpler tasks remained low-risk. Differences between tools exist but are smaller than differences across task categories. Overall, SRF enables reproducible evaluation of AI-generated code and provides a practical framework for assessing its security implications.

---


### 176. [Video-Based Markerless Motion Capture for Clinical and Rehabilitation Biomechanics: A PRISMA-ScR Scoping Review of Validated Architectures, Clinical Readiness, and Emerging Methods](https://arxiv.org/abs/2609.18667)

**<font color=#1a73e8>作者：</font>** Florian Delaplace, Elodie Piche, Frédéric Chorin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background.. Video-based markerless motion capture promises movement analysis without the cost, space and skin-marker constraints of optoelectronic systems, with particular potential for clinical and rehabilitation settings. Whether validated pipelines yet deliver clinically acceptable biomechanics, and how they relate to the underlying computer-vision research, remains unclear. Methods. We conducted a scoping review following the PRISMA extension for Scoping Reviews, with a registered protocol and searches of PubMed, Scopus and IEEE Xplore (January 2015 to February 2026; the computer-vision scan was updated to July 2026). A dual-tier design paired a primary corpus of validated biomechanical studies with a complementary, curated and deliberately non-exhaustive corpus of emerging computer-vision work, used qualitatively. We charted study characteristics, pipeline architecture, validation methods and joint-angle accuracy. Results. We included 117 studies, most published from 2024 onward and conducted on healthy adults walking in a laboratory. Pipelines formed five architectural families across monocular and multi-camera modalities; most reported raw joint angles without biomechanical refinement. Sagittal lower-limb agreement clustered around 5 to 6{\textdegree}, generally short of clinical acceptability, while out-of-plane kinematics, kinetics, and pathological or older populations were rarely validated. Emerging computer-vision building blocks (foundation-model mesh recovery, differentiable inverse kinematics, video-based kinetics) were almost absent from validated studies. Conclusions. Video-based markerless capture is not yet interchangeable with marker-based systems for clinical joint kinematics, and it remains barely validated where rehabilitation needs it most: older and pathological populations, out-of-plane kinematics, and kinetics. Mapping this evidence gap onto emerging computer-vision advances, we propose hypothesis-generating design guidelines, not a validated method, to steer the next generation of pipelines toward accessible, clinically meaningful movement analysis.

---


### 177. [Tracing individual knowledge trajectories in a changing field: the case of general relativity and gravitation](https://arxiv.org/abs/2609.18697)

**<font color=#1a73e8>作者：</font>** Raphael Schlattmann, Malte Vogl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historians have reconstructed the twentieth-century transformation of general relativity and gravitation (GRG) at the field level and through individual careers, but connecting these scales requires a way to compare researchers with the changing field over time. We develop such a comparison, setting a researcher's publications and references against GRG field literature from the same, earlier, and later two-year periods. Building on Own Vocabulary and Embedding Density Estimation from our earlier two-case study (arXiv:2501.00391), we extend the analysis to the fifty most-published authors in a NASA/ADS corpus of about 180,000 GRG records (1911 to 2000) and add two citation-based measures, Referenced Vocabulary and Citation Identity. The four measures compare an author's written language, cited literature, semantic neighbourhood, and cited-authority configuration with the surrounding field. The earlier cases suggested that closer field-vocabulary alignment accompanies a denser semantic neighbourhood. Across the fifty authors this holds only partially. Written and cited vocabularies tend to move together, usually resembling later GRG literature as the field turned towards astrophysical and cosmological research. Semantic neighbourhoods more often lie where the field's publications were concentrated in earlier periods, while co-citation patterns follow no single temporal direction, and the two citation measures frequently place the same researcher differently despite drawing on identical reference lists. Individual trajectories can thus combine vocabulary tied to later field states with older semantic or citation structures, and these divergent cases mark patterns for closer historical investigation. The approach transfers to other fields with defensible corpus boundaries and adequate coverage of texts, references, and disambiguated author identities.

---


### 178. [Mask IPL: Noise-Free Intrinsic Position Learning via Computation Graph Clipping for Event-Based Spike-Driven Tracking](https://arxiv.org/abs/2609.18716)

**<font color=#1a73e8>作者：</font>** Yimeng Shan, Malu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) match the event-driven nature of event cameras and naturally extract spatiotemporal features. These properties have motivated a series of recent studies on event-based tracking with SNNs. Intrinsic Position Learning (IPL) acquires strong position information without introducing additional parameters, making it a mainstream approach for position encoding in event-based spike-driven tracking. However, the mechanism behind its effectiveness lacks systematic theoretical analysis. Moreover, our analysis reveals that IPL introduces noise in both forward and backward propagation. The former increases inference error, while the latter prevents parameters from converging to better solutions. This paper presents a systematic analysis of IPL and demonstrates that its effectiveness stems from the synergy between IPL and multi-stage convolution. The zero blocks in the joint tensor act as zero padding for convolution, and the resulting boundary effect propagates layer by layer through multi-stage convolution. Every parameter update is therefore driven by a gradient that perceives the relative displacement between template and search frames. Positional encoding added after the convolutional stage cannot provide this information. We further propose a simple Computation Graph Clipping method that applies a validity mask determined by the layout to the operations of every layer, making invalid regions equivalent to zero padding in both forward and backward propagation. This eliminates the noise without introducing additional parameters and makes the actual gradient coincide with the ideal gradient. We name the improved method Mask IPL. Without increasing parameters or computational cost, Mask IPL improves the AUC of the Tiny-scale tracker on FE108, FELT, and VisEvent, and consistently improves the Base-scale tracker as well.

---


### 179. [LocQE: Principled Domain Adaptation for Localisation Quality Estimation by Leveraging Post-Edits](https://arxiv.org/abs/2609.18720)

**<font color=#1a73e8>作者：</font>** Kathy Hämmerl, Gabriel Bretschner, Joern Wuebker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learned quality estimation (QE) models such as COMETKiwi are widespread and work well for general machine translation evaluation. However, they are known to struggle on unseen domains, limiting their performance in a real-world localisation context. We show that they are insensitive to some important factors in localisation, such as whether numbers are translated accurately, or even whether the correct number of spaces and punctuation are preserved in a translation. Further, a key capability for optimisation of machine translation is the ability of QE models to accurately rank different translations of a single segment, which suffers significantly from the domain transfer. In the absence of large-scale direct assessment data, we propose principled fine-tuning approaches to reduce the domain gap with even small amounts of post-editing data. Using a multi-task fine-tuning approach and a simple tokeniser intervention, we create a QE model which proves markedly better at distinguishing preferred post-edits from rejected initial translations in a localisation context. We show that preferences and artificial continuous scores stabilise each other, and argue that to calibrate metrics both in terms of their absolute scores and comparisons between translation of the same source, both types of signal are needed.

---


### 180. [Calmables: Demonstrating Closed-Loop Infrared Earables for Thermal Biofeedback and Relaxation Support](https://arxiv.org/abs/2609.18726)

**<font color=#1a73e8>作者：</font>** Valeria Zitz, Michael Küttner, Jonas Hummel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present Calmables, a walk-up demo of a closed-loop infrared earable that uses smart-ring heart rate to create subtle, ear-localized warming cues. Building on work on thermal comfort and in-ear infrared stimulation, Calmables explores warmth at the ear as a biosignal-adaptive cue for brief recovery moments following acute activation. A smartphone first establishes an individual resting baseline and derives a personalized heart-rate threshold, while the earable controller independently enforces an over-temperature cut-off and communication fail-safes. During the guided demo flow, attendees complete a brief rapid-breathing activation phase until their heart rate reaches the personalized threshold. This triggers an ear-localized warming cue followed by a short relaxation phase, while physiological changes are displayed on a live dashboard. Attendees can also manually explore different infrared stimulation intensities. To contextualize the demo, we report preliminary placebo-controlled UX ratings from 18 participants: participants rated the active prototype higher on perceived relaxation and perceived recovery support than an identical-looking placebo. Together, the demo illustrates how infrared earables can make physiological feedback tangible through subtle, biosignal-adaptive thermal cues.

---


### 181. [Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737)

**<font color=#1a73e8>作者：</font>** Harvey Caldeira, Haoran Wang, Guoxi Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater 3D reconstruction supports applications ranging from marine ecosystem monitoring and subsea inspection to underwater archaeology, education, and immersive visualisation. 3D Gaussian Splatting has made real-time photorealistic novel-view rendering practical, while underwater variants incorporate physically based image-formation models to separate medium effects from scene radiance. Their reconstruction quality, however, remains fundamentally limited by the geometry used for initialisation.

---


### 182. [When Edit Flows are Edit Jumps: replicating Edit Flows and EvoFlows](https://arxiv.org/abs/2609.18745)

**<font color=#1a73e8>作者：</font>** Gabriel Bénédict, Melanie Buechler, Gerard Riera-Solà 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibody lead optimization calls for a small, bounded set of edits to an existing candidate: substitutions, but also insertions and deletions. Edit-based generative models are the only ones that allocate such an edit budget without fixing the edit positions, the edit count, or the output length in advance. However, the existing approaches Edit Flows and EvoFlows did not release code or complete training specifications. Here, we show that both methods follow the same underlying process -- edits firing one at a time, at learned rates, in continuous time -- the pure-jump case of generator matching over finite sequences. With EditJumps we introduce the first open implementation of this framework, with a single generalist antibody editor trained on 1.66M Observed Antibody Space homolog pairs to propose homolog-like variants of a seed sequence, editing unseen leads zero-shot, without the per-family retraining original approaches require. Replicating this system from scratch exposes why open code is essential for generative biology: reconciling published edit distributions required reverse-engineering an undocumented rate-scaling hyperparameter that dictates realized mutation counts. Moreover, we show that published evaluation metrics are highly sensitive to reference sample size, frequently flipping method rankings. We release our full codebase, automated test suite, and configurations at: this https URL

---


### 183. [Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks](https://arxiv.org/abs/2609.18751)

**<font color=#1a73e8>作者：</font>** Shi Tang, Zirui Chen, Yongjia Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> At EUROCRYPT 2025, Carlini et al. proposed a breakthrough in the cryptanalytic extraction on hard-label (S1) deep neural networks (DNNs), demonstrating polynomial-time signature and sign recovery. However, Carlini et al.'s sign-recovery method (which we call Future Toggle) suffers only a marginal advantage over random guessing, producing high-confidence wrong sign predictions in deeper layers. Such errors trigger expensive exponential-time enumeration.
This work presents Normal Alignment, a novel statistical sign-recovery approach for S1 DNNs. Drawing on the expected length difference between projected normals of adjacent decision facets at dual points, our method infers neuron signs via normal-signature alignment. It delivers higher voting accuracy and pushes erroneous predictions to low-confidence ranks, which further enables a more efficient combined method, eSOE + Alignment, by combining Normal Alignment with the hard-label SOE extension. This combined strategy removes heavy enumeration overhead and realizes exact polynomial-time full sign recovery.
Experiments demonstrate the effectiveness of our method, especially for deep layers. For example, with our method, the signs for CIFAR-10 (architecture 192-64$\times$8-10) and MNIST (architecture 64-96$\times$3-32-10) models can be fully recovered in polynomial time; in contrast, Carlini et al.'s sign-recovery method would require exponential-time enumerations involving $2^{52}$ or $2^{82}$ guesses of the signs, respectively.

---


### 184. [Toward Markerless Video-based Tremor Analysis: Objective Quantification of Pathological Tremor in Mouse Preclinical Models](https://arxiv.org/abs/2609.18753)

**<font color=#1a73e8>作者：</font>** Yota Koshimoto, Akihiro Tsukahara, Yasuhiro Moriwaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tremor is a movement disorder characterized by involuntary, rhythmic oscillations of body parts and is a hallmark of several neurological conditions, including Parkinson's disease and essential tremor. Elucidating its underlying mechanisms relies heavily on mouse models, which offer genetic manipulability and translational relevance to human neural circuitry. Accordingly, these models are indispensable for studying tremor pathophysiology. So far, electromyography and accelerometers have been used as methods to quantitatively observe tremors in mice. However, these methods have several drawbacks, such as high costs and complex setups. In particular, the invasive surgical implantation of devices causes significant stress to the animals. Although RGB-based methods offer non-invasive and cost-effective alternatives, they often lack the sensitivity required to detect subtle tremors. Therefore, this paper addresses these challenges by achieving mouse tremor severity estimation using conventional RGB cameras only. To address the challenging task of isolating tremor-related vibrations while the mouse itself is also in motion, our pipeline incorporates segmentation-based pre-processing to extract the mouse region and a Tremor Score Estimation Module that captures subtle tremors with high sensitivity. In the experiments, we assessed tremors in unrestrained mice using a non-invasive method with two standard cameras. The results demonstrated a strong correlation with accelerometer measurements and confirmed that the method accurately captured the intensity-dependent characteristics of tremors. The project page is available at this https URL.

---


### 185. [Version- and Scope-Aware Question Answering over Normative Documents: A Deployed System and an End-to-End Evaluation at Production Scale](https://arxiv.org/abs/2609.18769)

**<font color=#1a73e8>作者：</font>** Liuyin Wang, Shuaipeng Jin, Jiwei Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correctly answering a question grounded in normative documents often depends on information outside any single passage: whether the retrieved document is the version currently in force; whether it applies to the jurisdiction, subject (such as an institution or applicant), and date at issue; and whether each normative claim can be traced to its supporting source text. Hosted retrieval services have substantially lowered the engineering cost of building an initial system over such corpora, making "upload the documents and ask" a common default. We evaluate this default on approximately 73,000 candidate normative documents supplied to a production deployment. The evaluation uses a stratified sample of 200 questions from our published benchmark, with a gold source document for every question; the released sampling rule reads no system outputs or scores. We compare the hosted service with a governed system that resolves version and scope through explicit rules before generation. The governed system scored 97.7 overall, while the hosted service scored 88.1, a gap of 9.6 points computed from unrounded means. The question set, the answer text evaluated for both systems, the scores, and the scripts used to reproduce the reported benchmark statistics are public. The governed configuration has operated as a commercial product since January 2026 and serves 1,126 registered users; named customer organizations include Zhipu AI and Lecheng Health. By mid-April 2026, it had reached roughly 100,000 calls per workday.

---


### 186. [Zero-Shot Cross-Lingual Recognition of Sign Language Handshapes](https://arxiv.org/abs/2609.18772)

**<font color=#1a73e8>作者：</font>** Marcel Granero-Moya, Carolina del Corral Farrarós, Gloria Haro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language processing advances rapidly for high-resource languages such as American Sign Language (ASL), yet most of the world's sign languages lack the phonological annotations new methods require. We present the first zero-shot cross-lingual framework for handshape recognition, transferring from ASL to Catalan Sign Language (LSC). Our approach leverages the decomposition of handshapes into five phonological features -- selected fingers, flexion, spread, thumb position, and thumb contact -- shared across both languages, to decode LSC handshapes from predicted features via a composite phonological distance metric. We evaluate three architectures (MLP, SL-GCN, SHuBERT) trained on two ASL corpora (PopSign, Sem-Lex) against a 37-handshape, single-signer LSC benchmark. Zero-shot transfer proves viable once recording-format disparities are harmonized, reaching 80.0% phonological feature accuracy and 54.5% expected handshape accuracy. Phonological decomposition thus offers a bridge for extending sign language technologies to low-resource languages without any target-language video training labels.

---


### 187. [DISTA-Net++: Rethinking Infrared Small Target Unmixing Beyond Sub-Pixel Separation](https://arxiv.org/abs/2609.18773)

**<font color=#1a73e8>作者：</font>** Mengze Xu, Zhu Liu, Weidong Sheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range infrared imaging frequently confronts dense target clusters whose diffraction-limited signatures merge into a single indistinguishable blob, concealing the number, sub-pixel positions, and radiant intensities of the underlying sources. While deep learning has advanced general object detection, resolving such Closely-Spaced Infrared Small Targets (CSIST) remains largely unexplored, owing to a systemic infrastructure void and a fundamental paradigm mismatch. The dominant formulation, which reduces unmixing to a blind, discrete sub-pixel separation, is inherently insufficient: without semantic guidance, the ill-posed inverse problem admits ambiguous solutions plagued by false and missed detections, while grid-based discretization locks predictions onto fixed lattice centers, chaining precision to prohibitively expensive grid refinement. We argue that CSIST unmixing should instead be informed and continuous. To ground this paradigm shift, we establish the first comprehensive open-source ecosystem for the field, comprising the large-scale CSIST-100K benchmark, a tailored metric suite, and the GrokCSO toolkit. Upon this foundation, we propose DISTA-Net++, which anchors a dynamic deep unfolding backbone with two synergistic mechanisms: a Count-Guided Prior that injects the global target count as an explicit semantic constraint to regularize the solution space, and a Continuous Coordinate Rectification that regresses off-grid offsets to decouple localization accuracy from grid resolution. Extensive experiments validate our paradigm: even under the most economical 3x division, DISTA-Net++ surpasses 7x-division state-of-the-art methods by 16.15% in CSO-mAP and 62.96% in count accuracy at merely one-sixth of their computation, demonstrating that unmixing precision need not be purchased with finer discretization. The complete ecosystem is available at this https URL.

---


### 188. [A Convergence Framework for Deep $V$-Learning: Error Propagation and Sharp Action-Gap Bounds](https://arxiv.org/abs/2609.18782)

**<font color=#1a73e8>作者：</font>** Yury Kolomeytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish convergence bounds for deep $V$-learning with horizon $H$. The algorithm fits a scalar value function to targets from executed transitions and selects actions using a predictive model and the value function. For current observed-successor targets with fresh true-kernel outcomes, the conditional mean is $\mathcal{T}^\beta V$, which averages over behavior-policy actions. The Bellman optimality update is $\mathcal{T} V$. We decompose the update error into six residuals: fitting, transition reuse, target construction, replay, action selection, and exploration. Under $L^s$ concentrability, their $L^p$ norms ($p=s/(s-1)$) control expected $L^1$ policy loss. The bound explicitly weights residuals from only the last $H-1$ update blocks, plus an initialization term for shorter runs. We quantify the cost of a shared sampling distribution across horizon levels. For statistical error bounds of order $n^{-\nu}$, we derive optimal continuous allocations and an integer allocation whose objective is within a factor $2^\nu$ of the constrained optimum. A margin condition with exponent $\alpha$ gives action error of order $\Lambda^{1+\alpha/p}$, where $\Lambda$ combines network drift and score error; a one-step construction proves the exponent sharp. Bounds on the distance between frozen and optimal scores transfer an optimal-gap condition to frozen-iterate gap bounds while retaining the mass of optimal ties. Survival probabilities and coverage conditions at deployment yield bounds for policies selected with approximate scores. Separate spatial ReLU networks per horizon level give a conditional neural regression rate, and the finite-state case gives a log-free expected fit rate. These results give expected policy-loss consistency for the fixed-horizon generative-reset approximate-ERM procedure with exact action scores and provide an explicit residual-decay criterion for FIFO/interleaved SGD.

---


### 189. [s-MDM: Generative Virtualization of Multi-Device Hardware Variations for Portable DL-SCA](https://arxiv.org/abs/2609.18783)

**<font color=#1a73e8>作者：</font>** Niloufar Sayadi, Marten van Dijk, Chenglu Jin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep Learning-based Side-Channel Analysis (DL-SCA) frequently suffers from catastrophic performance degradation across unseen hardware due to printed circuit board routing differences, silicon process variations, and measurement noise shifts. This poster presents the Synthetic Multiple Device Model (s-MDM), a zero-target-trace generative framework designed to improve cross-device portability. s-MDM combines a structured cVAE generator, a Walsh-Hadamard leakage anchor, continuous style modulation, and decoupled leakage-style--domain critics to synthesize virtual source-device profiles offline. Benchmarked on 32-bit side-channel traces (AES_PTv2), s-MDM maps a precise operational boundary: while physical MDM remains superior on identical electrical clones (D4), s-MDM achieves consistently low key rank on the layout/acquisition-shifted Pinata target, where physical baselines are unstable or misaligned.

---


### 190. [Differential Trust: Dynamic Multi-Authority Anonymous Credentials with Epoch-Weighted Updates](https://arxiv.org/abs/2609.18811)

**<font color=#1a73e8>作者：</font>** Chen Li, Jianting Ning, Xiulong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anonymous credentials (ACs) are fundamental to privacy-preserving authentication, allowing users to prove possession of attributes without revealing their identities. State-of-the-art ACs distribute credential issuance across multiple authorities, typically employing techniques such as Shamir's secret sharing or aggregate signatures. While this approach enhances system robustness and eliminates a single point of failure, it treats all authorities equally in the credential issuance phase. This uniform treatment disregards the varying levels of trustworthiness or stake held by different authorities. Such a limitation has become particularly problematic in modern decentralized systems like Proof-of-Stake networks, where the inherent trust differentiation among nodes cannot be leveraged in the credential issuance process.
To address this limitation, we propose the notion of Multi-Authority Anonymous Credentials with Epoch-Based Weights (MA-ACEW), the first Multi-Authority Anonymous Credential (MA-AC) model that considers authorities' weight distribution in credential issuance. Crucially, MA-ACEW enables efficient credential updates when authority weight distributions change across epochs. The core of MA-ACEW is our novel Epoch-Bound Pointcheval-Sanders Signature (EB-PS) primitive, which binds signatures to specific time epochs. This temporal binding enables both weight-based credential issuance within epochs and efficient non-interactive credential updates across epochs. We formalize the EUF-eCMA unforgeability requirement for EB-PS and prove our construction satisfies it under a novel STB-GPS assumption. We then prove that our MA-ACEW construction achieves unforgeability, anonymity, and blindness. Finally, we present benchmarks demonstrating the efficiency of EB-PS and MA-ACEW. Remarkably, presenting a credential aggregated from 128 partial ones takes only 10.68 ms on average.

---


### 191. [Interpretable Multi-Instance Learning Enables Early Prediction of Key Molecular Alterations from Routine Flow Cytometry in Acute Myeloid Leukemia](https://arxiv.org/abs/2609.18825)

**<font color=#1a73e8>作者：</font>** Jonathan Legrand, Aguirre Mimoun, Baudouin Denis de Senneville 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Molecular testing for NPM1 and FLT3-ITD mutations guides critical early treatment decisions in acute myeloid leukemia (AML), but results can take weeks, long after these decisions must be made. Flow cytometry, already performed within hours of admission as part of routine care, may carry enough signal to predict these mutations directly, without added cost or delay. Methods: We developed an interpretable multi-instance learning classifier based on a decision tree, in which each patient sample is modeled as a collection of individual cells and mutation status is inferred from cell-level predictions. The model was benchmarked against a random forest trained on clinical variables and a deep convolutional neural network adapted for multitube flow cytometry data. Performance was assessed by cross-validation on a discovery cohort of 197 patients and tested on an independent cohort of 161 patients, using the area under the receiver operating characteristic curve (AUROC) and positive predictive value. Results: In cross-validation on the discovery cohort, the MIL model achieved mean AUROCs of 0.96 (SD=0.05) for NPM1 and 0.86 (SD=0.10) for FLT3-ITD, outperforming the clinical baseline and matching deep learning approaches. The model then successfully generalized to the independent test cohort of 161 patients, reaching AUROCs of 0.90 (NPM1) and 0.82 (FLT3-ITD), with positive predictive values of 0.87 and 0.68, respectively. Cell-level interpretation recovered established immunophenotypic signatures (CD33${}^{+}$ /CD34___ for NPM1-mutated cases, CD33${}^{+}$ /low side-scatter for FLT3-ITD), directly linking model predictions to known biology.  Conclusions: These results show that an interpretable model applied to data already collected in routine care can predict AML molecular status within hours, offering a practical route to earlier, biology-informed treatment decisions.

---


### 192. [Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration](https://arxiv.org/abs/2609.18836)

**<font color=#1a73e8>作者：</font>** Zhida Qu, Shengchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A surveillance system that detects an anomaly often has to repair the footage as well, yet the two tasks are studied in isolation: training-free anomaly detectors stop at a score or a label, while training-free video editing answers to a user prompt rather than to a detector. This paper proposes AVR (Anomaly-aware Video Restoration), which closes that gap with frozen pretrained models alone and generates content only where the clip offers no evidence to copy. Motion evidence first gates open-vocabulary proposals into spatio-temporal masks. A background prior computed from the clip then fills every pixel the anomaly ever uncovers, leaving diffusion to synthesize only what no frame showed, and a frozen verifier decides per clip whether to trust a classical, a prior-anchored, or a background-conditioned restorer. Extensive experiments on three surveillance datasets, under both full-reference anomaly injection and real anomalies, show that AVR leads full-frame fidelity under oracle masks, matches three trained video inpainters inside the edited region, and outperforms a detect-then-generate pipeline on the masks it produces itself, while suppressing both the residual anomaly and the flicker of free diffusion.

---


### 193. [Physics-based prediction, uncertainty quantification and decision-making for IN718 crystallographic texture intensity across LPBF defocus regimes](https://arxiv.org/abs/2609.18863)

**<font color=#1a73e8>作者：</font>** Yisheng Lu, John Riris, Jie Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable prediction of crystallographic texture in laser powder bed fusion is critical for linking process conditions with anisotropic response and for qualification. However, black-box models may fail under shift and cannot distinguish weak data support from loss of physical validity. This study develops a two-stage physics-based model for <001> || BD (build direction) texture in Inconel 718. Stage 1 maps process variables to melting mode and melt pool geometry. Stage 2 predicts texture by combining an empirical physics model with a random-forest residual model. A k-nearest-neighbor weight attenuates residual corrections for poorly supported queries, while a study-specific areal beam-power-density criterion withholds predictions outside the adopted conduction envelope. Conformal intervals are evaluated on the retained physics-valid set, and SHAP and Sobol analyses assess residual sensitivity. Under a controlled leave-one-defocus-out evaluation, the physics anchor achieved R^2 = 0.778, against -0.001 for the black-box model and 0.750 for the gated hybrid. Under leave-one-group-out cross-validation, the gated hybrid reached R^2 = 0.592 against 0.538 for the black-box model. Retained-set coverage was 92.9% at a mean full width of 3.65 multiples of a uniform distribution (MUD) under grouped cross-validation and 100% at a width of 3.21 MUD under transfer to a withheld +80 mm defocus regime. An illustrative mapping produced a retained BD elastic-modulus span of 127-187 GPa. On nine conditions from a separately built sample set, the framework withheld three, attenuated three, and matched the measured ordering for the rest. Separating data applicability, physics validity, and predictive uncertainty into distinct decisions lets the framework transfer where an unconstrained model does not, and withhold predictions where no model class performs adequately.

---


### 194. [Hamming Ideals and Grobner Bases for ISD-like Syndrome Decoding](https://arxiv.org/abs/2609.18866)

**<font color=#1a73e8>作者：</font>** Roberto La Scala, Marco Marchesin, Sharwan K. Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We investigate an algebraic approach to the Syndrome Decoding Problem, based on a reformulation of the Hamming weight constraint and its integration with the Information Set Decoding paradigm. We begin with a systematic analysis of the Hamming variety, deriving its defining equations in terms of elementary symmetric functions. Since these equations may have high degree, we exploit convolution identities for elementary symmetric functions, together with factorizations based on Lucas' identity, to derive an equivalent formulation with auxiliary variables and equations of bounded degree.
Building on this modeling, we generalize the ISD paradigm through an ISD-like decoding strategy, implemented by the GBDecode algorithm, in which only a subset of an information set is fixed. This approach reduces the size of the combinatorial search space at the cost of solving the associated multivariate nonlinear systems. To handle this algebraic component, we employ the MultiSolve algorithm, which replaces a single Grobner basis computation with a collection of computations on simpler systems, obtained by exhaustively assigning a varying number of indeterminates over the finite field. This provides a tunable balance between combinatorial search and algebraic solving.
We evaluate the resulting approach experimentally on instances of the Syndrome Decoding Problem for random binary linear codes, using parameters corresponding to the NIST Security Category 1 parameter set of the Classic McEliece cryptosystem. The experiments assess the feasibility of this combinatorial-algebraic approach and provide insights into the practical behavior of Grobner basis techniques within an ISD-like decoding framework.

---


### 195. [NeuroECG: ECGFounder-Based Deep ECG Representation for EEG-Free Neurological Prognostication After Cardiac Arrest](https://arxiv.org/abs/2609.18891)

**<font color=#1a73e8>作者：</font>** Jiaju Gao, Yi Zhao, Chenyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurological prognostication after cardiac arrest commonly relies on electroencephalography (EEG). However, EEG demands high clinical resources. Bedside electrocardiography (ECG) is standard and low-cost. Yet, its value for predicting neurological outcomes remains underexplored. In this study, we propose NeuroECG, an ECGFounder-based deep representation framework for EEG-free auxiliary prognostication. NeuroECG adapts a pretrained ECG foundation model via task-specific fine-tuning. We implement a gradual unfreezing strategy on single-channel bedside monitoring ECG. Multiple ECG segments per patient are encoded into segment-level deep features. These embeddings are aggregated via quantile pooling ($q = 0.24$) and compressed using principal component analysis (PCA). Experiments on 412 ECG-available patients from the multicenter I-CARE database show that the adapted ECGFounder backbone achieves the best performance among ECG-only backbone baselines, with a test AUROC of 0.7333. We further combine the learned deep ECG representation with static clinical covariates. The proposed NeuroECG model achieves a test AUROC of 0.8077 and an AUPRC of 0.8970. These results support deep bedside ECG representations as a useful source of auxiliary prognostic information. Their integration with static clinical covariates improves prediction in an EEG-free setting. The source code is available at this https URL

---


### 196. [NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898)

**<font color=#1a73e8>作者：</font>** Yihan Zang, Da Li, Dominik Engel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free weighted aggregation is widely used to lift 2D semantic features onto 3D Gaussians for open-vocabulary scene understanding, yet its theoretical role remains insufficiently understood. Existing analyses typically justify this operation from the rendering side, treating Gaussian features as linearly composable Euclidean variables for reconstructing 2D feature maps. However, this view does not match downstream 3D usage, where each Gaussian is often queried independently in a cosine-based embedding space. We revisit feature lifting from the 3D side and formulate per-Gaussian assignment as a cosine alignment problem on the CLIP unit sphere. Under this objective, the L2-normalized semantic back-projected feature emerges as the closed-form solution, providing a complementary interpretation of the standard lifting rule from the perspective of per-Gaussian semantic assignment. The same formulation further yields a norm decomposition into intra-view and inter-view consistency, suggesting that feature magnitude itself can serve as a semantic reliability signal. Calibrated by effective multi-view support, this reliability score guides a mode-voting refinement that preserves CLIP feature validity by avoiding linear averaging. Experiments on open-vocabulary 3D semantic segmentation show that NormLift is an efficient, training-free framework that achieves strong performance across evaluation protocols.

---


### 197. [Social Laws for Multi-agent Coordination in Stochastic Environments](https://arxiv.org/abs/2609.18929)

**<font color=#1a73e8>作者：</font>** Rolando Fernandez, Caleb Probine, Tyler Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-agent environments, coordinating agents to prevent interference and ensure robust individual performance is a critical challenge. Previous research on social laws for multi-agent systems has primarily focused on deterministic, goal-based settings. This paper extends the concept of social laws to stochastic, reward-based environments, proposing a formalism for defining and verifying their robustness under various conditions. We introduce the notion of $\alpha$-robustness, a measure of the guaranteed utility each agent retains while pursuing its optimal single agent policy, assuming all agents obey the social law. We then present an approach for robustness verification of social laws in stochastic settings, based on a reduction to solving a series of Markov decision processes. Empirical evaluations on toy environments illustrate the potential of our framework.

---


### 198. [Dose-Aware Cold Diffusion with Physics Consistency for Generalizable Low-Dose CT Reconstruction](https://arxiv.org/abs/2609.18943)

**<font color=#1a73e8>作者：</font>** Md Imam Ahasan, Guangchao Yang, A F M Abdun Noor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing radiation dose in computed tomography significantly degrades image quality and poses challenges for accurate and clinically reliable reconstruction. While recent approaches have shown promise for low-dose CT, they often struggle to generalize across continuous and previously unseen dose levels, leading to artifacts and loss of anatomical detail. To address these limitations, we propose Dose-Aware Cold Diffusion (DACD), a physics-consistent reconstruction framework that explicitly models radiation dose as a continuous latent factor within a cold diffusion process. The proposed DACD framework integrates image-based dose-aware perception, multi-scale structural prior extraction, and dose-calibrated step allocation to adaptively guide the denoising trajectory. In addition, an iterative forward-backprojection correction is incorporated into the reverse refinement process to enforce projection-domain data consistency. Extensive experiments on three public benchmarks, including Mayo-2020, Mayo-2016, and LoDoPaB-CT, demonstrate that DACD consistently outperforms state-of-the-art diffusion-based and physics-guided methods in both quantitative accuracy and visual fidelity, particularly under ultra-low-dose conditions. The results show that DACD achieves robust generalization across a continuous range of dose levels, including those unseen during training.

---


### 199. [Changepoint-Aware World Models: Detecting Dynamics Shifts and Recovering by Forgetting Stale Replay in Model-Based RL](https://arxiv.org/abs/2609.18950)

**<font color=#1a73e8>作者：</font>** Everest Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A robot's learned model of its own dynamics is only valid until those dynamics change: actuators wear, payloads shift, and joints stiffen. A model-based agent that keeps training as if nothing happened adapts slowly, dragged back by a replay buffer full of stale experience. We present Changepoint-Aware World Models (CAWM), a DreamerV3 agent that detects an abrupt dynamics shift from its own internal prediction error, using an online CUSUM test against a rolling baseline that fires only on abrupt change rather than on slow learning drift. It then forgets stale replay, keeping the learned representation while flushing obsolete data. On simulated locomotion under two robot-relevant shifts, doubled gravity and halved actuator gain, CAWM recovers substantially faster than passive retraining. It also beats a strong baseline that respawns a fresh dynamics model on detection, the deep-world-model analogue of model-bank methods. With the response triggered at the shift, CAWM gains +95 to +153 return in the first 30k post-shift frames over three seeds, while matching that respawn at asymptote. Running the detector in closed loop reproduces this gain on the gravity shift. The benefit holds across both shift types, and is largest when the shift is severe enough that old data is genuinely obsolete.

---


### 200. [Automated Dental Caries Segmentation in Panoramic Radiographs Using Dual-Stage Deep Learning](https://arxiv.org/abs/2609.18952)

**<font color=#1a73e8>作者：</font>** Jihun Kim, Kyeonghun Kim, Jong-yeol Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection of dental caries remains challenging due to limitations in traditional diagnostic methods, particularly for proximal lesions in posterior teeth. Deep learning models show promise for automated caries detection but face scalability constraints due to requirements for large volumes of expertly annotated training data. This study presents a dual-stage deep learning framework combining Faster R-CNN for tooth localization with U-Net for pixel-wise caries segmentation in panoramic radiographs. We developed a systematic transformation pipeline to convert large-scale polygon-annotated datasets into high-resolution binary segmentation masks, enabling pixel-wise supervised learning. The framework was trained using both expert-verified datasets and algorithmically processed labels from 3,000 panoramic images. Our approach achieved robust performance with an IoU of 0.9013, Dice coefficient of 0.9482, Recall of 0.9433, and Precision of 0.9774, demonstrating superior accuracy compared to existing methods while significantly reducing false-positive rates. The dual-stage framework effectively addresses data annotation bottlenecks in dental AI applications and demonstrates potential for scalable, automated caries detection systems that can improve diagnostic consistency and support clinical decision-making.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
