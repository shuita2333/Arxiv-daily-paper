# 📦 其他研究 | 2026年07月26日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

---

### 101. [The Geometry of Personality: Activation Steering with Jungian Cognitive Functions](https://arxiv.org/abs/2607.20803)

**<font color=#1a73e8>作者：</font>** Liu Zai, Yumeng Wang, Junchen Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering enables control and interpretation of LLMs, yet existing work primarily models personality through static trait frameworks such as the Big Five. We investigate whether personality can instead be represented and controlled as a set of cognitive processes using the eight Jungian Cognitive Functions. To this end, we introduce a framework comprising a Jungian evaluation protocol and a dataset of over 2,100 role-playing character narrations.
Activation steering vector extraction and evaluation experiments on Llama-3.1-8B demonstrate effective monotonic control over all eight cognitive functions through activation steering. Beyond controllability, our analysis reveals that: 1. personality information is concentrated in middle transformer layers; 2. steering vectors exhibit structured geometric relationships consistent with distinctions between rational and irrational functions; 3. effective multi-dimensional steering directions cannot be recovered as linear combinations of single-function directions. These findings provide new insights into the representation of personality in LLM activation space and establish a framework for studying interpretable, effective, and multi-dimensional personality control.

---


### 102. [New Complexity-Theoretic Frontiers of Tractability for Neural Network Training](https://arxiv.org/abs/2607.20811)

**<font color=#1a73e8>作者：</font>** Cornelius Brand, Robert Ganian, Mathis Rocton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In spite of the fundamental role of neural networks in contemporary machine learning research, our understanding of the computational complexity of optimally training neural networks remains incomplete even when dealing with the simplest kinds of activation functions. Indeed, while there has been a number of very recent results that establish ever-tighter lower bounds for the problem under linear and ReLU activation functions, less progress has been made towards the identification of novel polynomial-time tractable network architectures. In this article we obtain novel algorithmic upper bounds for training linear- and ReLU-activated neural networks to optimality which push the boundaries of tractability for these problems beyond the previous state of the art. In particular, for ReLU networks we establish the polynomial-time tractability of all architectures where hidden neurons have an out-degree of $1$, improving upon the previous algorithm of Arora, Basu, Mianjy and Mukherjee. On the other hand, for networks with linear activation functions we identify the first non-trivial polynomial-time solvable class of networks by obtaining an algorithm that can optimally train network architectures satisfying a novel data throughput condition.

---


### 103. [SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813)

**<font color=#1a73e8>作者：</font>** Jiun Lee, Jaekwang Kim, Sangmin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-aligned Gaussian splatting enables efficient and generalizable novel-view synthesis. However, high-resolution rendering faces a critical trade-off where increasing input resolution improves detail at the expense of quadratically rising network computational cost. Conversely, maintaining low-resolution inputs stabilizes this cost but results in insufficient Gaussian density and artifacts. To address this, we propose SubSplat, which introduces Sub-pixel Gaussian Reparameterizer(SPGR) to subdivide primary Gaussians into fine-grained primitives, restoring structural density directly from low-resolution features. We further enhance the reparameterization quality through feature aggregation, which effectively captures high-frequency details across multiple views. Experiments on RealEstate10K and ACID demonstrate that SubSplat achieves high-fidelity rendering with superior efficiency. Our results validate that the proposed framework successfully resolves the trade-off between reparameterization fidelity and network computational cost inherent in pixel-aligned Gaussian Splatting.

---


### 104. [Explainable graph attention network for stress recognition (StressGAT) via differential action units](https://arxiv.org/abs/2607.20819)

**<font color=#1a73e8>作者：</font>** Thomas Kassiotis, Stefanos Gkikas, Nikolaos Smyrnis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stress is a dynamic process characterized by significant individual variability in facial expression. Traditional architectures, such as Recurrent Neural Networks (RNNs) and Convolutional Neural Networks (CNNs), often overlook person-specific baselines or lack the representational capacity to model the non-linear temporal progression of distress due to sequential bottlenecks and rigid grid-based constraints. Furthermore, many deep learning models lack the interpretability required for clinical deployment. This study introduces StressGAT, a Graph Attention Network that leverages the relational inductive bias of graph modeling to capture complex facial dynamics that indicate acute stress. By using Differential Action Units, the framework normalizes individual responses relative to neutral baselines to achieve personalized recognition. The proposed model achieves 88.62\% accuracy on a diverse stress-induction cohort (58 participants) using a subject-independent, Leave-One-Subject-Out (LOSO) cross-validation protocol. Beyond predictive accuracy, the architecture integrates a Multiple Instance Learning (MIL) attention mechanism to identify peak stress intervals and reveal distinct expressivity phenotypes. By simultaneously optimizing for accuracy and interpretability, this framework provides a robust, explainable solution for personalized affective monitoring.

---


### 105. [Efficient and Interpretable Body-Based Emotion Recognition with Lightweight Temporal Convolutional Networks](https://arxiv.org/abs/2607.20820)

**<font color=#1a73e8>作者：</font>** Christian Arzate Cruz, Stefanos Gkikas, Houshyar Asadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Body-based emotion recognition is important for real-time affective systems, but graph-based skeleton models can be computationally expensive. This paper studies whether lightweight temporal convolutional networks (TCNs) can provide an efficient and interpretable alternative for body-based emotion classification. We evaluate a family of TCN models on DIEM-A and compare them with a graph-based time-series graph (G-TSG) baseline using accuracy, macro-F1, parameter count, and inference latency. Although G-TSG achieves the highest mean performance, TCN-Base remains within $1.58$ accuracy points and $1.25$ macro-F1 points while using $79.18\%$ fewer parameters and reducing classifier latency by approximately $12.5\times$. We also analyze body-region contributions using region-specific TCN models, zero-based occlusion, and G-TSG gradient saliency. The results show that upper-body motion provides the strongest standalone regional cue, that the usefulness of body regions varies across emotions, and that different interpretability methods capture distinct aspects of model behavior. These findings suggest that lightweight TCNs can support efficient body-based emotion recognition while also providing practical insight into how motion cues contribute to classification.

---


### 106. [Robust Asynchronous Q-Learning under Reward and State Corruption via Batching](https://arxiv.org/abs/2607.20822)

**<font color=#1a73e8>作者：</font>** Sreejeet Maity, Aritra Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by reinforcement learning in harsh environments, we consider the problem of learning an optimal policy subject to adversarially corrupted feedback. Specifically, at each time-step, an adversary can perturb both the reward and state observations of the learner following the Huber contamination model. To defend against such data corruption, we propose {\texttt{BR-Async-Q}}: a novel, epoch-based, robust \(Q\)-learning algorithm built upon two key ideas: (i) partitioning the online data stream into batches to reduce variance, and (ii) constructing robust estimates of the Bellman optimality operator using such batched data. We prove a high-probability $\ell_\infty$ error bound for {\texttt{BR-Async-Q}} that matches that for vanilla \(Q\)-learning, up to a small additive term that scales with the fraction of corrupted samples. To our knowledge, this provides the first robustness guarantee for asynchronous \(Q\)-learning subject to both reward and state corruption. Furthermore, when only rewards are corrupted, the dependence of our algorithm's bound on the corruption fraction is minimax optimal.

---


### 107. [Offline RL with Hierarchical Action Chunking](https://arxiv.org/abs/2607.20834)

**<font color=#1a73e8>作者：</font>** Ahad Jawaid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning (RL) holds the promise of learning general-purpose policies from static datasets. However, scaling these methods to long-horizon tasks remains a challenge due to the curse of horizon, where value estimation errors can compound through long chains of bootstrapped Bellman backups. Existing hierarchical approaches mitigate this by decomposing tasks into subgoals, yet they often rely on low-level controllers that suffer from myopic execution and biased value estimates. In this work, we propose Hierarchical Implicit Q-Chunking (HiQC), an offline goal-conditioned RL algorithm that combines high-level latent planning with low-level action chunking. By conditioning the low-level critic on temporally extended action sequences, HiQC enables unbiased k-step value backups, compressing the horizon at both the planning and execution levels. We theoretically demonstrate that this dual decomposition results in a tighter bound on value error under a bounded per-backup error model compared to standard hierarchy or flat chunking alone. Empirically, HiQC achieves the highest aggregate performance among the compared methods on the OGBench suite, with its largest gains on long-horizon navigation tasks such as humanoid-giant.

---


### 108. [Sonic Stage: Automatically Generating Interactive Spatial Soundscapes to Facilitate Dialogue Video Comprehension for Blind Viewers](https://arxiv.org/abs/2607.20835)

**<font color=#1a73e8>作者：</font>** Shuchang Xu, Xiaofu Jin, Gaurav Jain 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Audio description (AD) makes film and television accessible to blind and low-vision (BLV) audiences by narrating characters' actions. However, in scenes with lots of dialogue, AD often omits important actions because it is constrained not to overlap with speech. It is not yet known how to convey characters' actions during dialogue. We present Sonic Stage, a system that transforms dialogue videos into interactive spatial soundscapes, enabling BLV audiences to intuitively understand characters' actions and movements through immersive auditory cues. Sonic Stage conveys essential visual information during dialogue through three auditory techniques: (1) spatialized dialogue to represent spatial layout, (2) diegetic sound to convey character actions, and (3) interactive descriptions to provide context-specific visual details. Evaluation with 12 BLV viewers showed that Sonic Stage significantly improved video comprehension, spatial presence, and narrative engagement. We highlight opportunities for enhancing video accessibility across diverse genres through immersive, interactive audio representations.

---


### 109. [Code Monitor Red Teaming for Public-Test-Passing Code](https://arxiv.org/abs/2607.20852)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Jiawen Deng, Fuji Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visible tests are a common gate for LLM-generated code, but passing them does not certify specification correctness. We study a deployment-like monitoring problem: after code has passed public tests, can a weaker LLM verifier identify the residual hidden bugs? We introduce Code Monitor Red Teaming, a monitor-red-teaming protocol that fixes a public-check information boundary while varying generator pressure, verifier scaffolding, and weak-to-strong capability. We instantiate it as CodeMonitorBench, spanning function-level, data-science, and workflow code. Across 71,000 generated candidates, 43,677 pass public tests and 23,081 of those fail hidden tests. Weak verifiers improve with scaffolding and model family, but still miss most hidden bugs at 5% false-positive rate. As a robustness stress test, adversarial public-test-overfit pressure lowers verifier AUROC and raises low-FPR miss rates in most cells. A GLM-5.1 verifier recovers part of the gap under the same evidence boundary; an inferability audit shows that remaining misses mix verifier failures with M1 evidence limits.

---


### 110. [Multilevel Graph Wavelet Compressed Sensing with Scale-Aware Neural Recovery](https://arxiv.org/abs/2607.20857)

**<font color=#1a73e8>作者：</font>** Amirhossein Nouranizadeh, Sarang Rajendra Patil, Alan John Varghese 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning methods such as neural operators and physics-informed neural networks have advanced engineering applications and inverse problems, but their training typically requires large volumes of simulated data. This makes data preparation and model training expensive. We propose Graph Wavelet Compressed Sensing (GWCS), a learning-based framework for offline compression of graph signals by representing them as sparse, interpretable wavelet-domain representations using the spectral graph wavelet transform. The framework combines a nonparametric multilevel importance sampler, which retains high-energy wavelet coefficients within each scale for a given compression ratio, with a scale-aware graph neural network that reconstructs the signal from the sparse coefficients. We evaluate the proposed framework on synthetic approximately band-limited graph signals over random graphs and four PDE simulation datasets over meshes, which include Turbulent Radiative Layer, Viscoelastic Instability, Kolmogorov Flow, and Dynamic Stall. We compare against graph signal sampling methods and graph autoencoder baselines. Results demonstrate that the framework achieves high reconstruction fidelity and substantial data compression compared to existing benchmarks.

---


### 111. [CSPF: A Constrained Shared-Private Fusion Method for Non-Verifiable Preference Evaluation](https://arxiv.org/abs/2607.20862)

**<font color=#1a73e8>作者：</font>** Hehao Zhang, Danli Wang, Xinyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At present, reliable evaluation of non-verifiable tasks remains challenging. Existing approaches often fail to adequately capture the diverse evaluative criteria underlying human preferences in such tasks. To this end, we propose Constrained Shared-Private Fusion (CSPF), a fusion method that treats heterogeneous frozen reward models as complementary evaluators and learns to integrate their hidden-state representations under pairwise human-preference supervision. CSPF decomposes each expert signal into shared and expert-private representations, encouraging cross-expert alignment while preserving complementary viewpoints. Across experiments on LM-Arena target-domain adaptation and PPE out-of-distribution preference evaluation, CSPF achieves the best performance on the primary metrics among the evaluated single-expert reward-model, scalar-score multi-expert, and rubric-judge baselines. Overall, CSPF suggests that fusing hidden-state representations provides a more expressive basis for preference assessment, offering a practical route toward integrated evaluative signals for non-verifiable preference tasks.

---


### 112. [LegalCiteTrust: Benchmarking Citation Trustworthiness in Chinese Long-Form Legal Research Reports](https://arxiv.org/abs/2607.20872)

**<font color=#1a73e8>作者：</font>** Yunhan Li, Mingjie Xie, Zeyang Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form legal research reports increasingly rely on LLMs and agentic research systems, but their reliability depends not only on answering the task, but also on whether cited legal authorities are trustworthy. A citation can be risky even when it points to a real source: the report may omit limiting conditions, misdescribe the authority, or use it to support a stronger claim than the source allows. We introduce LegalCiteTrust, a benchmark for evaluating citation trustworthiness in Chinese long-form legal research reports. It contains 72 densely annotated report-level tasks and evaluates reports along three dimensions: Coverage, Support, and Citation Trustworthiness. Citation Trustworthiness is operationalized through citation-level Existence, Fidelity, and Applicability (E/F/A). Experiments on general-purpose LLMs, deep-research systems, and legal-specific systems show that task completion, evidence richness, citation density, and citation reliability expose different system behaviors. Retrieval tools can improve evidence support without reliably improving the Trust score, while E/F/A-based revision improves Trust and Final score more clearly than existence-only filtering. These results suggest that trustworthy legal research generation requires citation-aware evidence governance after retrieval: systems must not only retrieve legal authorities, but also select, describe, and apply them reliably.

---


### 113. [Webly Supervised Multi-Label Recognition: Evaluation Benchmark and Dual-Branch Multi-Label Contrastive Learning](https://arxiv.org/abs/2607.20874)

**<font color=#1a73e8>作者：</font>** Zhihua Xu, Zhijing Yang, Yufeng Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training deep learning models with freely available web images can reduce their dependence on costly manual annotations. Although webly supervised learning has been widely studied for single-label recognition, its multi-label counterpart remains underexplored, partly due to the lack of unified benchmarks and fair comparison protocols. To address this gap, we construct a benchmark for webly supervised multi-label recognition (WS-MLR), including Web-COCO and Web-Pascal, and re-implement representative baselines under a unified setting. The two datasets cover the same 80 and 20 categories as MS-COCO and Pascal VOC, respectively, and contain about 300 thousand images retrieved from the Internet using category-word combinations as search keywords. We further propose a Dual-Branch Multi-Label Contrastive Learning (DBMLCL) framework, which learns category-specific instance-level and category-level representations together with their similarities to identify and correct noisy labels. Extensive experiments on the benchmark demonstrate that DBMLCL achieves superior performance compared to representative baselines.

---


### 114. [WhereEdit: Mask-aware Local Latent Editing for One-Step Image Editing](https://arxiv.org/abs/2607.20883)

**<font color=#1a73e8>作者：</font>** Ming Hu, Mingyu Dou, Jianfu Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent one-step text-to-image (T2I) models enable efficient image synthesis and provide new opportunities for real-time image editing. However, existing one-step editing methods primarily rely on text conditioning for semantic transformation, lacking explicit spatial control over \textit{where} to edit. More importantly, even when spatial constraints are introduced, these methods often struggle to achieve strong and stable semantic modifications within the target regions. In this work, we revisit one-step image editing from a spatially controlled perspective and identify two key challenges: discovering editable regions and achieving effective localized semantic transformation. We reveal that existing methods perform global semantic transport, which limits high-intensity local editing under the one-step setting. To address this issue, we propose \textbf{WhereEdit}, a framework that reformulates one-step editing as localized adaptive editing. WhereEdit automatically identifies semantically relevant regions from internal model features and applies adaptive local modulation to enhance target-region editing while preserving non-target areas and structural consistency. Experiments on the PIE-Bench benchmark demonstrate that WhereEdit consistently outperforms existing one-step image editing methods, achieving superior editing quality while maintaining the efficiency of one-step generation. Additional experiments with region-level supervision further highlight the importance of explicit spatial reasoning for high-quality one-step image editing.

---


### 115. [TwistedMerge: Certified Higher-Order Diagnostics and Abstention for Model Merging](https://arxiv.org/abs/2607.20887)

**<font color=#1a73e8>作者：</font>** Ting Gong, Shitan Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines independently trained or fine-tuned models, but pairwise alignability does not imply globally consistent alignment. We formulate merging as a finite descent problem in which checkpoints are local objects, alignment maps are transitions, and cycle products are residuals. TwistedMerge is a conservative certification pipeline that separates fixed-chart averaging, synchronization-removable gauge inconsistency, a certified central obstruction on a specified comparison complex, and nonabelian holonomy. A residual is promoted to a cohomology class only after inverse-consistency, coefficient-identification, centrality, and closure tests; otherwise the method abstains and returns an ordinary or synchronized fallback. We prove a constant-edge no-go result, frozen-complex three-way and predeclared-family error-control theorems, and a refinement test for comparison-complex sensitivity. A planted neural alignment defect is removed by cycle-consistent synchronization, showing that a nonzero cycle score alone is not a higher obstruction. Controlled central systems recover the predicted non-coboundary and projective-rank behavior, while noisy estimates move from certification to abstention without false lifts on the tested controls. A trained low-rank-adapter audit shows that naive factor averaging depends on the chosen GLr representative, whereas global factor synchronization and dense-delta SVD are stable. On natural checkpoint collections, cycle residuals do not predict merge degradation and no natural central or period-index class is certified. The results position descent theory as a falsifiable certification and abstention framework.

---


### 116. [Engine-Native Editable 3D World Reconstruction with Objects and Lighting](https://arxiv.org/abs/2607.20889)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Xinghao Chen, Henghaofan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editable 3D scene creation requires object instances and lights that can be inspected, moved, and imported into standard engines, yet existing single-image methods largely stop at room-scale geometry, baked/global illumination, or text-driven generation. We introduce Lumera (Light-aware Unified Engine-native Reconstruction and Assembly), a benchmark and reference pipeline for engine-native, light-aware 3D scene parsing from a single image. Lumera-2K is built from 2,513 UE5 projects and provides 3.73M components, 63M object instances, 102.6K engine-native parametric lights, and 95.1K camera views. On this data, Lumera-Box and Lumera-Light adapt VLM to parse object boxes and parametric light tuples (x,y,z,r,g,b,I), which are assembled with per-object mesh reconstruction, HDR environment estimation, and a bounded agentic refinement loop. In a sanitized box benchmark against DetAny3D, SpatialLM, N3D-VLM, and WildDet3D, Lumera-Box obtains the strongest overall detection, geometry, semantic, and layout scores (merged mAP 0.1141, IoU-B 0.2472, F-score 0.2762), while WildDet3D remains stronger on anchor recall. For lights, Lumera-Light recovers almost all non-empty scenes (recall 0.998) but remains limited at individual-light localization (F1 0.209 at 0.5 m); matched lights have median position error 0.261 m, median {\Delta}E2000 4.59, and intensity Pearson r=0.628. These results establish parametric lights as a measurable editable-scene target and expose remaining bottlenecks in relation structure, light recall/intensity, and cross-engine generalization.

---


### 117. [Information-Theoretically Secure Aggregation for Lightweight Federated Learning: Resilient to Dropouts and Adversaries](https://arxiv.org/abs/2607.20890)

**<font color=#1a73e8>作者：</font>** Hyeong-Gun Joo, Songnam Hong, Dong-Joon Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device federated learning (FL) enables privacy-preserving and personalized model training on resource-constrained devices such as smartphones and IoT nodes. To reduce communication cost, sign-based methods (e.g., signSGD) transmit one-bit gradients. However, exposing gradient signs makes them vulnerable to inference attacks, while existing secure aggregation schemes are often incompatible with such methods or incur significant computational and communication overhead. We propose a lightweight and information-theoretically secure aggregation framework tailored for sign-based FL. The framework securely computes the majority vote (MV) polynomial through single-round secure multiplication, ensuring end-to-end information-theoretic security under the honest-majority assumption while revealing only the final aggregated sign to the server. To enhance efficiency and scalability, we introduce two key techniques. First, inverse-form exponent reduction halves the effective MV polynomial degree, reducing both communication and computation costs. Second, we propose single-round secure multiplication, achieving linear offline complexity and storage with only a single online communication. Together, these techniques reduce online communication by up to 99.5% and latency by up to 85.7% compared to conventional approaches. Also, by leveraging inherent MDS-code-based decoding, the framework achieves robustness against both dropouts and adversarial behaviors, yielding accuracy gains of up to 20.65% and 10.74%, respectively. Overall, the proposed framework establishes a practical foundation for large-scale, low-latency, and information-theoretically secure aggregation in sign-based FL.

---


### 118. [Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions](https://arxiv.org/abs/2607.20891)

**<font color=#1a73e8>作者：</font>** Pengyu Zhu, Lijun Li, Longju Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research agents extend LLM-based assistants into long-horizon workflows involving planning, retrieval, evidence synthesis, and report generation, yet their reliability in open information environments remains underexplored. A key concern is whether apparently credible but factually misleading knowledge encountered in such environments can propagate through these workflows and be adopted as false conclusions in final reports. To study this failure mode, we introduce MisKnow-Agent, a framework for constructing and validating misleading knowledge for Deep Research tasks. MisKnow-Agent generates misleading instances with controllable authority levels and styles, yielding 5,933 quality-controlled instances built on DeepResearch Benchmark tasks. Extensive experiments across open-source and closed-source Deep Research agents show that even limited exposure to misleading knowledge can induce false-conclusion adoption in final reports, revealing a broad reliability vulnerability in current Deep Research agents. Although search-enabled verifier models consistently identify the retained instances as misleading during focused corpus validation, the same instances can still be adopted during long-horizon research, revealing a disconnect between focused verification and workflow-level evidence use. Finally, we evaluate pre- and post-research defenses, both individually and in combination, finding that all three configurations mitigate but do not fully prevent false-conclusion adoption. Our findings suggest that reliable Deep Research requires evidence verification and correction capabilities at both the model and framework levels, beyond improvements in planning, retrieval, evidence integration, or report-generation abilities.

---


### 119. [HierarchicalDAEW: Domain-Aware Edge-Weighted Graph Convolution with Evidential Uncertainty for Multi-Section Spatial Gene Expression Prediction from H&E Histology](https://arxiv.org/abs/2607.20896)

**<font color=#1a73e8>作者：</font>** Kritanu Chattopadhyay, Soumya Chatterjee, Ondrej Krejcar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics assays remain costly and technically demanding, restricting transcriptome-wide profiling to specialist settings and preventing routine clinical deployment. Predicting spatially resolved gene expression from H&E histology could close this gap, yet current methods largely ignore the underlying tissue architecture and rarely quantify how their predictions can be trusted. We introduce HierarchicalDAEW, a dual-graph architecture that addresses both gaps. On the spot graph, a Domain-Aware Edge-Weighted convolutional operator learns separate projections for inter-domain, intra-domain, and boundary edges derived from Leiden clustering, allowing the model to treat tissue heterogeneity as an explicit structural signal rather than an implicit one. A second gene-level graph then fuses protein-protein interaction priors from STRING-DB with tissue-specific co-expression through learned attention gating, propagating predictions from a landmark gene set to a broader gene panel. Reliability is handled through evidential uncertainty estimation, which produces far better calibrated confidence intervals than Monte Carlo dropout under identical conditions. Across six human Visium sections spanning breast, colorectal, prostate, and cerebellar tissue, and against thirteen published baselines, HierarchicalDAEW achieves the strongest correlation with ground-truth expression, with gains that hold up under multi-seed reproducibility checks and negative controls that rule out positional shortcuts. Ablations further confirm that both the domain-aware edge typing and the hierarchical depth are necessary to this improvement, and calibrated uncertainty estimates identify low-confidence predictions for pathologist review before clinical action.

---


### 120. [MAGE-Vein: Multi-Instance Age and Gender Estimation from Finger Vein Images](https://arxiv.org/abs/2607.20897)

**<font color=#1a73e8>作者：</font>** Katsuki Tanaka, Koichi Ito, Takafumi Aoki 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Age estimation from finger vein images has been widely considered impractical due to severe demographic biases in public datasets and physiological confounding factors like gender. To overcome these limitations, we propose MAGE-Vein, a novel multi-instance, multi-task learning framework. Our approach extracts robust structural aging signs by employing a hybrid feature-level fusion of three fingers, effectively suppressing local imaging noise. Furthermore, simultaneous optimization of gender classification conditions the network to effectively eliminate gender-specific vascular variations. Evaluated on a demographically balanced dataset of 402 subjects, MAGE-Vein achieves a mean absolute error of 6.12 years and a correlation of 0.880. Our results not only overturn the conventional consensus regarding the limitations of the finger vein modality but also demonstrate that previous estimation failures were primarily artifacts of biased public datasets. Our code is available at this https URL.

---


### 121. [Sidewalk Moments: Are Richer Representations Always More Human-Aligned? Evidence from City-Walk Videos](https://arxiv.org/abs/2607.20903)

**<font color=#1a73e8>作者：</font>** Liu Liu, Freya Huying Tan, Fábio Duarte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We examine whether richer visual representations yield more human-aligned measures of urban engagement, using 61 first-person city-walk videos from YouTube segmented into over 50,000 ten-second clips and represented across four modalities: spatiotemporal video features, temporally averaged images (TAIs), audio embeddings, and text-based semantic descriptions. Spearman correlation analysis reveals the expected ordering along the temporal-richness continuum, with video features showing the strongest continuous alignment. However, this ordering breaks down under binary classification of high- versus low-engagement moments (the paradigm most commonly used to train perceptual scoring models), where TAIs consistently match or outperform video across most classifiers and quantile thresholds. An independent two-alternative forced-choice study on Amazon Mechanical Turk confirms that this parity reflects human judgment: participants identified engaging moments with comparable accuracy from TAIs and full video clips, while text performed substantially worse and audio remained near chance. Gap analysis reveals a functional dissociation: video features are advantaged in activity-driven scenes with dynamic content, whereas TAIs better align with human judgments in composition-driven scenes dominated by stable spatial structure. These findings challenge the assumption that richer representations are inherently more human-aligned, and suggest that perceptually grounded temporal compression can be a principled alternative to full video encoding.

---


### 122. [Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation](https://arxiv.org/abs/2607.20908)

**<font color=#1a73e8>作者：</font>** Quazi Ishtiaque Mahmud, Nesreen K. Ahmed, Ali Jannesari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful technique to enhance the reasoning capacity of LLMs for optimized code generation. However, existing RLVR approaches primarily rely on outcome-based signals such as correctness and speedup, overlooking performance-critical structural properties of programs that are essential for generating optimized code. In this work, we propose CudaPerf, a reflective RL framework that incorporates both verifiable execution rewards and structural code-aware rewards derived from parallelization features (e.g., memory coalescing, occupancy, Arithmatic Intensity, and synchronization patterns). CudaPerf operates in two stages: (1) an offline pairwise ranking module that learns to distinguish strong and weak program candidates via contrastive comparisons, and (2) an online RL training phase that jointly optimizes for correctness, performance, and structural efficiency through a unified reward signal. To further enhance learning, CudaPerf utilizes iterative refinement using execution feedback enabling progressive improvement of generated candidates. We also introduce a dataset comprising 2.9k C to CUDA and 1k PyTorch to CUDA programs, each paired with diverse input configurations and multiple CUDA implementations encompassing diverse optimization strategies. CudaPerf is evaluated across multiple benchmarks comprising both C to CUDA and PyTorch to CUDA transformations. Empirical findings suggest that CudaPerf significantly outperforms strong baselines, including Qwen-3-32B (for C to CUDA) and CUDA Agent (for PyTorch to CUDA) by achieving up to 5X & 3.32X improvements in speedup, and 17% & 7% improvements in correctness, respectively.

---


### 123. [Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction](https://arxiv.org/abs/2607.20911)

**<font color=#1a73e8>作者：</font>** Tencent WorkBuddy Bench Team, Siqi Cai, Shaopeng Chen 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Tencent WorkBuddy Bench, a multi-domain evaluation suite for coding agents; this report documents its construction methodology, scoring protocol, and a cross-model leaderboard. At its core is a unified evaluation framework for constructing and running distribution-informed coding-agent tasks across four work domains - Code, Web, Office, and Security. Rather than adapting public issue text, every task is reverse-engineered from a real commit, pull request, or business scenario and rewritten as a short, colloquial, role-played request, so that a task's prompt is not recoverable by web-searching the underlying issue, pull request, or commit thread. Because the dataset is released openly - task directories, environment images, evaluation harness, tests, and reference solutions - contamination resistance rests on this construction together with dataset versioning rather than on secrecy. The four subsets - repository-level engineering, front-end development, office and business workflows, and red-/blue-team security - probe complementary facets of real work, each with its own verification style. All are packaged in a uniform task-directory format and run, under a uniform and reproducible protocol, on two agent harnesses (CodeBuddy Code and Claude Code); the full open release makes the benchmark reproducible end to end and directly auditable, since any third party can re-run each task and inspect its content. Because each subset uses a different scoring instrument, scores are not comparable across subsets and the suite reports no suite-wide average. We report a cross-model leaderboard across several model families.

---


### 124. [Source-Prior-Driven Selective Adaptation for Efficient Diffusion Model Finetuning](https://arxiv.org/abs/2607.20913)

**<font color=#1a73e8>作者：</font>** Yi Xiong, Yuan-Yuan Cheng, Xiao-Ming Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large diffusion models for new domains or styles involves a trade-off: improving target-specific generation often degrades the pretrained model's broad generative capability. Existing full and parameter-efficient fine-tuning methods typically handle this trade-off only implicitly. In this work, we propose a novel source-prior-driven selective adaptation method to efficiently fine-tune diffusion models, achieving a favorable trade-off. Our method relies on two key observations: (1) the loss of general generative capability is highly inconsistent across pretrained parameters, and (2) parameters that have a relatively small impact on the model's general generative capability remain structurally inconsistent across layers and parameter types. Motivated by these observations, we first learn a static mask to explicitly identify parameters better suited for downstream adaptation, and then construct structured update strategies for the selected subset. Experiments show that our method achieves a better adaptation-retention trade-off than existing strong baselines.

---


### 125. [Three-Pronged Spectral Control for Federated Parameter Efficient Fine Tuning](https://arxiv.org/abs/2607.20914)

**<font color=#1a73e8>作者：</font>** Shiva Raj Pokhrel, Dipsan Bhattarai, Anwar Walid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated parameter-efficient fine-tuning (PEFT) enables communication-efficient adaptation of large pretrained models on decentralized edge data, but it remains fragile under non-IID client heterogeneity. In low-rank adaptation (LoRA), different clients may learn locally useful but spectrally misaligned update subspaces, causing high-variance aggregation and poor global transfer. We propose TRISHUL, a spectral-control framework for robust federated PEFT. TRISHUL follows the FL no-raw-data-sharing setting but does not itself provide formal privacy guarantees. TRISHUL uses shared frozen multi-head low-rank bases to obtain algebraically exact aggregation of compact core updates, applies nuclear norm proximal shrinkage to suppress client-specific high-rank spectral components before upload, and allocates adaptation heads non-uniformly across layers using a concave water filling budget rule derived from pretrained layer capacity. Because shrinkage is performed only on small core matrices, TRISHUL adds negligible computation and no extra per-round communication over the underlying multi-head PEFT protocol. Across vision and language benchmarks, including CIFAR-100, SVHN, 20 Newsgroups, MRQA, and GLUE with LLaMA3.2-1B, TRISHUL improves convergence, stability, and final performance over federated LoRA baselines, with greater gains under stronger heterogeneity.

---


### 126. [Traceable Scholarship: Page Anchors and Ariadne's Thread for Humanistic Inquiry in the Age of Generative AI](https://arxiv.org/abs/2607.20916)

**<font color=#1a73e8>作者：</font>** Deyu Jing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI lets large language models produce scholarly-looking text within seconds, yet fluency does not equal valid explanation. The deepest risk is not factual error alone but the appearance that an explanation is already established without clear sources, page numbers, editions, or evidence. We liken the page anchor to Ariadne's thread: within the labyrinth of generative fluency, it is the thread that leads the scholar back to the source. This paper proposes Traceable Scholarship as the minimum normative condition for AI-assisted humanistic research, situating it across the three revolutions of knowledge infrastructure: print, digital, and generative AI. We introduce page anchors, dual page numbers, citation-first generation, NO_EVIDENCE, human verification, four-level compliance, and Scope Contract, and present AIH-Infra as a three-layer reference implementation: Contexture (document structuring), Open WebUI AIH-Infra (traceable knowledge base), and AIH-Infra MCP Server (agent gateway). A case study on a 29-volume Kant Akademie-Ausgabe knowledge base illustrates how traceability supports retrieval correction, evidence grading, and judgment downgrading. Traceability is not a software feature; it is the condition under which humanistic research can remain public and refutable in the age of generative AI.

---


### 127. [OPOD: On-Policy Omni Distillation](https://arxiv.org/abs/2607.20918)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Yuyang Hu, Reed Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal models can handle text, images, and audio in one system, but improving all of these abilities together remains difficult. Training a single model on pooled multimodal data often fails to match models specialized for individual modalities. On-policy distillation (OPD) offers a way to combine such specialists: the student generates a response, and a teacher evaluates that same response, so the student learns directly from behaviors it actually produces. Yet using several teachers can introduce competing guidance and improve one modality at the expense of another. We present On-Policy Omni Distillation (OPOD), which routes each student response to the matching text, image, or audio teacher. OPOD keeps teacher guidance only on tokens where the teacher assigns a higher probability than the student, adjusts the influence of each modality teacher independently during training, and asks the routed teacher to assess both the final answer and whether the reasoning supports the correct answer. Across twelve benchmarks and three backbone sizes, OPOD achieves the best average score at every scale, reaching 70.8, 51.7, and 46.2 and exceeding the strongest comparator by 2.1, 1.8, and 1.7 points. On the 30B model, it outperforms both the base model and a counterpart post-trained jointly on pooled multimodal data on all twelve benchmarks, and ranks first or second on eleven even when the individual specialists are included. The specialists are discarded after training, leaving one deployable omni-modal model. These results show that coordinating modality-specific teachers is an effective way to improve a shared model while maintaining cross-modal balance.

---


### 128. [FA-LAM: Focus-Aware Large Avatar Model for One-Shot 4D Animatable Gaussian Head](https://arxiv.org/abs/2607.20922)

**<font color=#1a73e8>作者：</font>** Yingdong Hu, Yisheng He, Yiming Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose FA-LAM, a Focus-Aware Large Avatar Model for one-shot animatable Gaussian head creation, while simultaneously enabling static 3D and dynamic 4D full-head recovery. The core of our method lies in a thorough analysis of the attention mechanisms and the entangled reconstruction and animation training pipeline adopted by prior state-of-the-art approaches. Our analysis identifies two main factors that compromise the quality of 3D full-head generation: (1) incorrect and noisy attention activations, and (2) conflicts between the tasks of reconstruction and animation. To address the first issue, we introduce a symmetric and semantic attention regularization strategy that leverages the inherent semantics and structural symmetry of human heads. To disentangle the objectives of reconstruction and animation, we develop a novel dual-phase training pipeline that separates the model's capabilities for large-view hallucination and animation into distinct modules. Moreover, we enhance our model to support multi-view and streaming 4D reconstruction in an efficient and memory-friendly manner through a core autoregressive modification with tailored visibility-aware token fusion. Collectively, these innovations enable FA-LAM to reconstruct animatable Gaussian full heads with superior quality, particularly in fine facial regions and large viewing angles.

---


### 129. [MagicMakeup: A Region-Controllable Diffusion Transformer for High-Fidelity Makeup-Transfer](https://arxiv.org/abs/2607.20924)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Siming Zheng, Yang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Makeup-transfer applies the reference makeup to the source face while preserving the source identity. Despite advances in full-face editing by diffusion-based methods, strong regional controllability, makeup fidelity, and identity preservation remain challenging. The reasons are (i) pixel-to-attention misalignment that causes spillover into non-target areas and weakens regional control; (ii) unclear transfer/preservation concept separation under two-image conditioning, leading to coupling between makeup attributes and identity; and (iii) the lack of a high-resolution dataset that is identity-consistent and region-labeled for fine-grained supervision. In this paper, we propose MagicMakeup, a diffusion transformer-based framework for region-controllable and high-fidelity makeup transfer, built on spatial constraints and concept disentanglement. To enable precise region-specific editing while preserving identity, we propose Token-Aligned Region Gating, which aligns pixel masks with attention and applies region-specific logit gating. To clarify the concepts of transfer and preservation, we further introduce Cross-Modal Perception Guidance, which aligns text and image features to enhance cross-modal concept perception. We also design a pipeline for the generation of 1024 x 1024 data pairs through region-specific makeup removal and establish a unified benchmark in synthetic and real settings. Extensive quantitative and qualitative experiments show that MagicMakeup improves regional controllability, makeup fidelity, and identity preservation, with strong robustness across styles, races, and poses.

---


### 130. [Representing Entity Importance in AI Knowledge Systems: A Dual-Signal Framework of Audience Evaluation and Structural Authority](https://arxiv.org/abs/2607.20925)

**<font color=#1a73e8>作者：</font>** Shen Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI knowledge systems require representations of entity importance for retrieval, recommendation, evidence selection, and knowledge-intensive reasoning. Yet importance is often reduced to a single score derived from either human response or graph structure. Such compression may discard distinctions that matter when an AI system must choose among entities for different tasks. This study introduces an interpretable dual-signal representation in which each entity is characterized by an audience-evaluation dimension and a structural-authority dimension.
The framework is evaluated using movie entities as an empirical validation domain. IMDb non-commercial datasets provide a rating-based audience ranking, Wikidata supports entity alignment, and English Wikipedia hyperlinks form the knowledge network on which PageRank estimates structural authority. Experiments on 482 entities and 13,690 directed relationships reveal a statistically significant but weak association between the two dimensions (Spearman rho = 0.2275, p < 0.001). Their overlap is only 10% in the top 10 and 34% in the top 100, while entity-level divergence occurs in both directions.
The results show that audience evaluation and structural authority are non-redundant signals and should not automatically be collapsed into a single scalar notion of importance. The contribution is not a new ranking algorithm or learned embedding, but a minimal knowledge-representation framework and an empirical test of its dimensional necessity. The findings support task-aware AI knowledge systems that preserve distinct importance signals before applying context-specific selection or aggregation.

---


### 131. [SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration](https://arxiv.org/abs/2607.20926)

**<font color=#1a73e8>作者：</font>** Yinhao Tang, Youqing Fang, Yanan Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research involves complex information-seeking and reasoning workflows across heterogeneous sources. However, existing benchmarks primarily emphasize general-domain retrieval or static scientific question answering, and therefore fail to assess key capabilities required in realistic scientific research workflows. We introduce SciExplore, a benchmark designed to evaluate scientific information-seeking and reasoning capabilities of LLMs and agents. SciExplore comprises four task types covering 103 expert-curated tasks across more than ten scientific disciplines: scientific database navigation, ambiguous literature retrieval, missing reference completion, and cross-source structured knowledge synthesis, which probe progressively higher-level abilities from entity-level reasoning and document-level identification to evidence-level grounding and domain-level synthesis. We evaluate over ten state-of-the-art LLMs and autonomous agents on SciExplore, revealing substantial performance gaps with performance degrading sharply as task complexity increases and extremely low accuracy on the most challenging structured synthesis tasks. These results highlight significant limitations of current models and agents in realistic scientific information-seeking scenarios.

---


### 132. [Clustered Edge Intelligence: Beyond Just Convergence of Edge Computing and AI](https://arxiv.org/abs/2607.20937)

**<font color=#1a73e8>作者：</font>** Chinmaya Kumar Dehury, Boris Sedlak, Alaa Saleh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We are moving from an information age to the age of intelligence. A decade, or possibly less than that, data will not be the gold anymore rather the derived intelligence out of the data and the information we posses from the edge of the network. Existing Edge Intelligence research focuses mainly on two directions: using AI for edge resource management and deploying lightweight AI models on edge devices. However, existing edge computing research lacks an intelligence-centric framework in which derived intelligence is treated as a first-class, independently manageable entity that can be described, discovered, observed, shared, reused, and dynamically clustered across heterogeneous edge devices and applications. To address these research gaps, we introduced Clustered Edge Intelligence, a visionary intelligence-centric approach. The aim of CEI is to make intelligence a shareable and reusable first-class entity that can be independently represented, discovered, observed, exchanged, and managed across the distributed edge-cloud continuum. We present a three layer CEI architecture and examine enabling technologies and research dimensions, including intelligence inventories, semantic knowledge representation, communication, discoverability, observability, lifecycle automation, clustering mechanisms, marketplaces, interoperability, and standardization.

---


### 133. [Ms. Forcing: Efficient Streaming Video Generation with Multi-Scale Patchification and Attention](https://arxiv.org/abs/2607.20940)

**<font color=#1a73e8>作者：</font>** Zekun Li, Xiaoyan Cong, Hongyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video diffusion models have made substantial progress toward interactive and dynamic world simulation, but the nested autoregressive and denoising loops of conventional next-frame generation hinder real-time deployment. Recent rolling-window methods pipeline denoising across multiple consecutive frames at different noise levels, improving throughput and long-horizon stability. However, they tokenize every state at the same fine spatial granularity, leaving substantial noise-dependent redundancy in the joint denoising window. We propose this http URL, an efficient streaming video generation paradigm that adapts spatial granularity to each state's noise level. Its Multi-Scale Patchification (MSP) assigns coarser patches to noisier states, reducing the active-window token count by 45%, while Multi-Scale Self-Attention (MSSA) matches the density of visible non-sink keys and values to each query scale to further reduce attention cost. Because both schedules are fixed by window position, this http URL retains a static, hardware-friendly computation graph. We further introduce Homogeneous-Noise-Level DMD (H-DMD), which assembles each fake video from clean predictions sharing the same source noise level, thereby reducing the mismatch between DMD training sequences and inference-time rollouts. The multi-scale design helps offset the additional training cost of backpropagating through overlapping windows. We include both quantitative and qualitative experiments to show that this http URL reaches 22.84 FPS on a single H200 GPU, 39.6% faster than Rolling Forcing, while significantly improving VBench scores in both short video and long video generation setting.

---


### 134. [From a Word-Level Dictionary to Sentence-Level Semantics: Multilingual Grievance Labelling with Contextual Models](https://arxiv.org/abs/2607.20946)

**<font color=#1a73e8>作者：</font>** Lin Tian, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grievance is one of the warning signs analysts look for when assessing threats of violence. It is increasingly measured at scale from online text, most often with word-level lexicons like the Grievance Dictionary that score by matching weighted terms. Such matching is a fast and transparent proxy, but it cannot resolve whether a term is asserted, quoted, negated, or condemned. These lexicons are also often evaluated on pools enriched with the very examples they retrieve, so a high score partly reflects agreement with the lexicon's own selection rule. Examining a five-language, 2{,}000-item evaluation pool, we find its halves separated almost perfectly by the lexicon itself: every item labeled ``random'' is in fact lexicon-negative, so the lexicon's apparent macro-AUROC of 0.686 collapses to a 0.500 floor fixed by construction. We keep the dictionary's 22-construct ontology but replace term matching with context-reading models, evaluated on a non-circular benchmark that separates unconditional-random, lexicon-positive, and lexicon-negative strata across five languages. Reading the full post rather than the target sentence alone helps most where the lexicon is silent, raising average precision on lexicon-negative text from 0.14 to 0.20, with the largest gains on quoted, implicit, and cross-sentence grievance. Together, these results show that grievance is measured more faithfully by reading the surrounding context, and more honestly when tested on text the lexicon did not select. We release our code and benchmark at this https URL.

---


### 135. [RECO: Region-Aware Compensation for Extrinsic Perturbations in Roadside 3D Detection](https://arxiv.org/abs/2607.20947)

**<font color=#1a73e8>作者：</font>** Junsheng Du, Zhaocheng He, Yuhuan Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In intelligent transportation systems, roadside 3D object detection provides wide-area perception crucial for traffic understanding, cooperative early warning, and safe autonomous driving. However, existing methods suffer from high sensitivity to camera extrinsics; even slight deviations (whether manifesting as transient jitter or persistent drift) can be significantly amplified by projective geometry. This cascade results in severe feature misalignment and degraded localization. To mitigate this limitation, we propose RECO, a region-aware extrinsic compensation framework that corrects extrinsics using piecewise 6-DoF pose offsets. RECO predicts a learnable range boundary to partition the scene into near and far regions, estimating region-specific pose corrections. A differentiable sigmoid gate then smoothly blends the two compensated geometries to preserve continuous BEV sampling and facilitate stable optimization. To supervise the refinement of extrinsics, we introduce an auxiliary reprojection loss that compares 2D bounding boxes projected from 3D ground truth against 2D annotations, optimizing it jointly with the standard detection objective. Extensive experiments on the DAIR-V2X-I and Rope3D benchmarks under extrinsic perturbations demonstrate consistent improvements over state-of-the-art baselines across both yaw and $z$-axis deviations. RECO also generalizes from transient perturbations to persistent shifts, maintaining highly competitive performance under strict calibration uncertainty.

---


### 136. [Best-of-Evidence: Best-of-N Selection under Partial Verification](https://arxiv.org/abs/2607.20950)

**<font color=#1a73e8>作者：</font>** Cenwei Zhang, Teng Fang, Yuxia Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> BoN improves model outputs by sampling several candidates and selecting one with a proxy score, but it assumes that complete candidates can be evaluated reliably. Many vision-language tasks instead provide only partial verification: a finding, span, value, region, or relation may be checkable even when no dependable whole-response verifier exists. Moreover, the same claim may recur across candidates with opposing stances, allowing one observation to support part of the pool and contradict another. We introduce Best-of-Evidence (BoE), an inference-time selection framework that keeps the BoN candidate pool fixed, represents reusable claims with a signed candidate--factor graph, and allocates a limited budget to evidence actions that can change the final choice. BoE formalizes selection under partial verification and provides a practical score-based controller, with the zero-budget case recovering the underlying BoN decision. Theoretically, we show that residual evidence capacity limits any evidence-driven improvement and that shared factor queries can achieve an O(log K) versus {\Theta}(K) query separation in a factor-code model. Common-ledger experiments on four medical VQA settings show that BoE can improve fixed-pool selection and rescue some BoN failures when evidence is reliable, contrastive, and decision-relevant, while also revealing the channel-quality and candidate-generation limits that prevent universal gains.

---


### 137. [The Weight of Silence: A Causal Case for Weights Over the Scratchpad in Latent Chess Reasoning](https://arxiv.org/abs/2607.20952)

**<font color=#1a73e8>作者：</font>** Ishan S. Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent, or silent, reasoning lets language models carry out intermediate computation in continuous vector space instead of words, and is widely assumed to function as an internal scratchpad the model actively consults during inference. Whether that assumption survives reinforcement learning has not been tested directly: existing causal analyses of latent reasoning are confined to math and logic tasks, and compare a model's reliance on its thoughts within a single checkpoint, never before and after an RL stage. We train a chess-playing model through a staged latent-reasoning curriculum followed by reinforcement learning, and find legality climbs monotonically to 61% (from a 48% pre-RL baseline) while checkmate confabulation is eliminated entirely. To locate this gain, we run a six-condition causal intervention suite on the same model before and after RL: substituting or adding matched noise to the latent thought vectors leaves performance unchanged, ablating them causes only mild degradation, and only exact-zero vectors cause collapse. This robustness gap is itself the finding: under exact-zero corruption, legality collapses to 1% pre-RL versus 9% post-RL, a gap that survives correction for testing across the full battery; milder conditions trend similarly without independently reaching significance. RL appears to add robustness to disruption, not reliance on thought content. These results push back against the field's default assumption that latent thoughts function as an actively consulted inference-time scratchpad, and instead indicate latent reasoning's principal effect here is shaping the model's parameters during training. We also demonstrate a working RL gain in chess, a domain outside the math and logic settings where multiple groups report the same latent-reasoning-plus-RL recipe failing to improve accuracy over SFT.

---


### 138. [FSB-Net: Frequency-Spatial Boundary Network for Brain Stroke Lesion Segmentation in Non-Contrast CT](https://arxiv.org/abs/2607.20955)

**<font color=#1a73e8>作者：</font>** Linke Fan, Xianglong Li, Huixin Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of brain stroke lesions in non-contrast computed tomography (NCCT) scans is critical for rapid clinical decision-making, yet remains difficult due to the low contrast between lesion and normal brain tissue, heterogeneous lesion morphology across ischemic and hemorrhagic subtypes, and ambiguous boundaries caused by partial volume effects. Current deep learning approaches primarily optimize region-level overlap but lack explicit boundary modeling, leading to imprecise delineation that can affect volumetric assessment and treatment planning. We propose FSB-Net, a frequency-spatial boundary network that leverages frequency-domain analysis for boundary-aware stroke lesion segmentation. FSB-Net introduces three components: (i) a Wavelet Boundary Detection Head (WBDH) that applies the discrete wavelet transform to multi-scale encoder features, extracting high-frequency sub-bands as boundary representations; (ii) a Frequency-Spatial Cross-Attention Module (FSCAM) that performs bidirectional attention between wavelet boundary features and spatial decoder features for selective boundary enhancement; and (iii) a Spectral Boundary Loss that penalizes high-frequency discrepancies in the Fourier domain to optimize boundary sharpness. Built on a PVTv2-B2 encoder, FSB-Net is evaluated on a public Brain Stroke CT dataset containing both ischemic and hemorrhagic cases. Experimental results show that FSB-Net outperforms U-Net, UNet++, MANet, and DeepLabV3+ across all metrics, achieving state-of-the-art performance in mean Dice, mean IoU, and HD95.

---


### 139. [From Scalars to Time Series: Rethinking Implicit Neural Representations for Time-Varying Volumetric Data](https://arxiv.org/abs/2607.20970)

**<font color=#1a73e8>作者：</font>** Weihan Zhang, Xuan Zhao, Yenwen Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) for time-varying volumetric data are typically trained using dense sampling over spatiotemporal coordinates, where each observation corresponds to a single point in space and time. This coordinate-wise formulation requires extensive sampling during optimization, leading to high computational cost and inefficient use of temporal structure. In this work, we revisit this design choice and show that dense spatiotemporal sampling is not necessary for learning time-varying fields. Instead, we represent the data as a collection of spatially indexed time series and train INRs using sequence-level supervision over each spatial location, rather than coordinate-wise scalar samples. This reformulation eliminates the need for dense spatiotemporal sampling and instead learns each spatial location from its full temporal evolution in a structured manner. We demonstrate that this representation is compatible with a range of existing INR architectures and consistently improves reconstruction quality, while significantly reducing training cost. Furthermore, we show that this formulation can be combined with mixture-of-experts architectures, and that our MoE instantiation further improves reconstruction quality compared to both the base reformulation and existing MoE-based INR methods, providing a stronger capacity allocation under heterogeneous temporal dynamics.

---


### 140. [Unsupervised Metal Artifact Reduction in Dental CBCT using Fine-tuned Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/2607.20977)

**<font color=#1a73e8>作者：</font>** G.L.T. Chamika, S.N.A. Dhanapala, P.H.S.V. Nimalaweera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal artifacts generated by dental implants significantly degrade cone-beam computed tomography (CBCT) volumes, obscuring critical anatomical structures and compromising diagnostic precision. To address this, an unsupervised deep learning framework has been proposed for Metal Artifact Reduction (MAR) utilizing a Cycle-Consistent Adversarial Network (CycleGAN) optimized for high-fidelity restoration. Unlike supervised methods that rely on unattainable voxel-aligned paired datasets, the proposed approach leverages an unpaired dataset of approximately 4,000 images, curated from the public ToothFairy dataset. The architecture integrates U-Net-based generators and PatchGAN discriminators, specifically tuned to mitigate generative hallucinations and preserve morphological integrity. Quantitative benchmarking on a held-out test set demonstrates a 34.6\% improvement in the Blind/Referenceless Image Spatial Quality Evaluator (BRISQUE) score, a substantial reduction in Fréchet Inception Distance (FID) from 207.03 to 157.04, and a superior Structural Similarity Index Measure (SSIM) of 0.9105. The framework achieves real-time efficiency with a 3.03 ms inference time per slice, effectively suppressing artifacts while preserving anatomical detail. Expert validation confirms high fidelity; however, to ensure reliability in extreme cases, the architecture is recommended as a clinical decision-support tool under human-in-the-loop oversight. By enhancing diagnostic clarity via a scalable software pipeline, this study provides a robust solution for high-fidelity dental implant imaging.

---


### 141. [GuardianAgentBench: Where Agents Fail and How to Guard Them](https://arxiv.org/abs/2607.20982)

**<font color=#1a73e8>作者：</font>** Vishal Ishwar Naik, Chenyu Xu, Donna Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model agents increasingly operate autonomously with access to tools and external environments, ensuring their safe and reliable behavior becomes critical. We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara. The benchmark incorporates rigorous multi-stage validation and five adversarial attack modes. Experiments with six state-of-the-art models reveal that even the strongest configuration achieves only 74.8% overall accuracy and expose two distinct failure regimes: stronger models under-call required tools, while weaker models mis-select and over-call tools. Performance degrades monotonically with both tool-set size and sequential turn depth, with long-horizon planning proving the steeper bottleneck. Our guardrail implementation consistently outperforms system-prompt-based defenses across all models, recovering 19.9% of failures at a false positive rate of just 0.5%. These results demonstrate that execution-time structural intervention improves safety without disrupting correct agent behavior.

---


### 142. [Latent Variable-Mediated Cross-Learning for Few-Shot Acoustic Impedance Imaging](https://arxiv.org/abs/2607.20989)

**<font color=#1a73e8>作者：</font>** Junheng Peng, Yong Li, Mingwei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acoustic impedance imaging is a fundamental yet severely ill-posed problem in subsurface analysis: the seismic wavelet is unknown, observations are band-limited, and labeled well-log samples are extremely scarce (typically <1% of all traces). Existing semi-supervised deep learning methods mitigate few-shot problem by incorporating forward modeling, yet they either rely on inaccurate prior wavelet assumptions or introduce auxiliary networks, leading to unstable optimization and degraded performance. We propose RD-SCL, a novel framework that integrates regularized deconvolution with semi-supervised cross-learning. At its core lies a differentiable, closed-form first-order Tikhonov deconvolution operator that dynamically estimates the latent wavelet in the frequency domain during training, providing stable physics-guided feedback without explicit auxiliary networks and fixed wavelet priors. Building on this operator, we design a symmetric cross-learning that enforces consistency between predictions on labeled and unlabeled data, thereby effectively exploiting abundant unlabeled traces. Extensive experiments on the SEAM and Marmousi 2 benchmarks demonstrate that RD-SCL consistently outperforms state-of-the-art supervised and semi-supervised methods, achieving substantial gains with lower computational cost. With only 56.5k learnable parameters and competitive runtime, RD-SCL offers a practical, physically consistent, and efficient solution for acoustic impedance imaging.

---


### 143. [Sparse Concept Channels in Frozen 3D CT Vision Encoders](https://arxiv.org/abs/2607.20993)

**<font color=#1a73e8>作者：</font>** Farhad Nooralahzadeh, Lea Bogensperger, Christian Bluethgen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models are becoming increasingly dominant in 3D medical image interpretation, but we rarely know <i>which</i> internal units encode clinical findings or <i>where</i> that information lives in the representation. We first study this on a 3D chest vision-language model (Pillar-0) by probing its frozen vision embeddings. We show that (i) each radiological finding is encoded by a <i>sparse</i> set of ~10 vision-encoder channels that match full-feature classification performance and far exceed a zero-shot text prompting; (ii) turning off the channels tied to one finding, that finding's score collapses while unrelated labels stay stable; and (iii) the same sparse probe <i>replicates</i> on an architecturally unrelated 3D abdominal VLM (Merlin) suggesting a general property of frozen medical encoders. Our training-free concept channel probe (CCP) method, paired with a corpus-derived report template, outperforms published CT-CHAT on clinical efficacy and NLG metrics (F1 0.549 vs. 0.184; BLEU 0.483 vs. 0.373) at 22x lower latency. Our results provide a clear, reproducible characterization of how frozen medical encoders represent findings, demonstrating direct applicability across models.

---


### 144. [Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills](https://arxiv.org/abs/2607.20999)

**<font color=#1a73e8>作者：</font>** Zibin Lin, Shengli Zhang, Taotao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills package reusable procedural knowledge as external artifacts for frozen language-model agents, yet existing optimizers do not jointly resolve where a failure occurs in a workflow, which mechanism caused it, and how relevant knowledge from third-party Skills should be reused locally. We introduce Workflow-Localized Mechanism Learning (WML). Its Node--Mechanism Attribution identifies the failed workflow node, implicated mechanisms, and smallest valid edit target, routing single-mechanism defects to L3 resources and relational defects across mechanisms to L2 composition protocols. A six-module Workflow-Guided Skill Optimization (WGSO) loop then selects provenance- and scope-aware third-party knowledge, applies bounded patches, evaluates candidates, and stores verified outcomes in optimizer-side memory. On SpreadsheetBench, WML reaches 90.33 +/- 1.53 and 74.67 +/- 3.51 Hard Accuracy with DeepSeek and Qwen3.6-Flash, respectively; without additional optimization, the learned Skills transfer to WikiTableQuestions with 84.00 +/- 2.00 and 83.00 +/- 2.00 Denotation Accuracy. On Compiler-Supported50, WML attains both the highest hard-PASS rate and the lowest cost per successful task; compiled execution sharply reduces tokens and calls relative to a direct SkillAgent while retaining most of its successful tasks. Code and artifacts are available at this https URL.

---


### 145. [Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory](https://arxiv.org/abs/2607.21000)

**<font color=#1a73e8>作者：</font>** Hyuk Lim, Seunghyun Yoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-sequence memory tracking places two opposing demands on a recurrent state: near-lossless retention of stored bindings over long horizons, and active overwriting of stale ones. In our diagnostic suite, the strongest efficient baselines tend to solve only one side well. Continuous-time-parameterized state-space models (SSMs) such as Mamba obtain their discrete recurrence by zero-order-hold discretization of a continuous-time system; we argue that this detour is unnecessary for memory tracking and parameterize the discrete transition directly. Naju (Native Adaptive Junction Unit) factorizes the recurrent update, schematically $x_n = f_n\odot x_{n-1} + i_n\odot(B_n u_n)$, into an explicit discrete pole (a learned forget gate $f_n$), an independent write gain $i_n$, and input-dependent write/read maps. Since the sigmoid pole satisfies $0<f_n<1$, each frozen local coordinate is Schur-stable by construction, and the full time-varying recurrence satisfies a fading-memory/BIBO bound under uniform boundedness assumptions, with no stability regularizer. We formalize the key structural limitation of coupled designs: any non-expansive complementary single-gate recurrence ties the effective retention $r$ and write gain $w$ through $|r|+w\le 1$, so near-complete retention forces weak writing; decoupling $f_n$ from $i_n$ removes this constraint. Empirically, Naju is the only evaluated model that remains strong on both retention and overwriting at 4x the training length. Beyond the diagnostic suite, we evaluate Naju on WikiText-103 language modeling, Long Range Arena, and multi-query associative recall. Across these settings, Naju consistently combines strong long-range memory with competitive or superior performance, outperforming the Mamba baselines in the principal comparisons while remaining competitive with the Transformer and preserving linear-time, linear-memory scaling.

---


### 146. [ADABORD: a novel AdaBoost approach for ordinal classification](https://arxiv.org/abs/2607.21003)

**<font color=#1a73e8>作者：</font>** Rafael Ayllón-Gavilán, Francisco José Martínez-Estudillo, David Guijo-Rubio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordinal Classification (OC) deals with classification tasks where the classes follow a natural order. Despite the progress in OC, many existing approaches fail to fully leverage the ordinal information, treating the problem as nominal classification and thereby losing performance potential. In this work, ADABORD, an AdaBoost framework specifically designed for ordinal classification problems, is introduced. The ordinal nature of the classes is incorporated into two key components of the well-known AdaBoost algorithm: 1) the base estimator, where decision trees with the ordinal Gini splitting criterion are proposed; 2) the error function used to update sample weights at each stage and the weights of the classifier in the final ensemble model, given by the absolute ranked probability score, a measure that accounts for both the ordering and the distance between classes. ADABORD is extensively compared against seven state-of-the-art methods on the TOC-UCO repository, the largest benchmark collection for OC to date. The experimental results, supported by statistical analysis, show that ADABORD significantly outperforms competing methods, particularly on datasets with five or more classes, where the ordinal structure becomes more pronounced. Source code, along with all experimental protocols, is publicly available to ensure reproducibility and facilitate future research in OC.

---


### 147. [AUCH-Net: Action Unit-Based Consistency-Aware Hypergraph Network for Cross-Domain Few-Shot Facial Expression Recognition](https://arxiv.org/abs/2607.21004)

**<font color=#1a73e8>作者：</font>** Xinhan Qiu, Yan Yan, Rui Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, cross-domain few-shot facial expression recognition (CF-FER) has received considerable attention. However, the performance of existing CF-FER methods is still unsatisfactory due to inferior transferable feature learning under large domain discrepancy and limited target samples. Fortunately, the action units (AUs), which indicate the movements of different facial muscles, provide consistent conceptual semantics for describing expressions within and across domains. Inspired by this, we propose a novel Action Unit-based Consistency-aware Hypergraph Network (AUCH-Net), which constructs consistency-aware hypergraphs on AUs, for CF-FER. Specifically, AUCH-Net presents a new AU feature learning (AFL) module and a new visual feature learning (VFL) module. The AFL module learns AU features under the guidance of a novel relation consistency loss and an AU regularization loss, while the VFL module learns visual features supervised by a relation consistency loss and a classification loss. By learning consistent AU features, AUCH-Net effectively models the connections between AUs and expression categories. As a result, we can bridge the gap between fine-grained facial variations and high-level expression categories, greatly facilitating the learning of transferable feature this http URL experiments on both in-the-lab and in-the-wild datasets show that our method consistently outperforms several state-of-the-art methods. Our results clearly show that modeling the relationships among AUs holds significant potential for FER under cross-domain few-shot scenarios.

---


### 148. [Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay](https://arxiv.org/abs/2607.21005)

**<font color=#1a73e8>作者：</font>** Xiaolong Li, Zhangchen Zhou, Zhi-Qin John Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most explanations of training instability focus on \emph{learning-rate criticality}, typically characterized by the Edge of Stability, beyond which optimization becomes unstable. We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}. This criticality is induced by the interaction between normalization (which introduces scale-invariant components) and weight decay (which persistently shrinks parameter norms). As the weight decay coefficient increases, the norms of scale-invariant weights are progressively driven toward zero. Meanwhile, the sharpness of the loss landscape increases rapidly, destabilizing the optimization dynamics and resulting in abrupt loss spikes. This perspective provides a rationale for why weight penalties can improve generalization yet cannot be made arbitrarily strong: excessive decay drives scale-invariant weight norms past a critical boundary and destabilizes training. Our work provides a new mechanistic understanding of loss spikes through the lens of \emph{weight-norm criticality}. Moreover, \emph{weight-norm criticality} yields testable predictions that we validate empirically in networks with scale-invariant components, providing empirical support for the proposed mechanism.

---


### 149. [Explainable Deepfake Detection Challenge](https://arxiv.org/abs/2607.21007)

**<font color=#1a73e8>作者：</font>** Abhijeet Narang, Kartik Kuckreja, Shreya Ghosh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection is moving beyond binary classification decisions toward systems that can also explain the visual evidence supporting those decisions. This transition is important for real-world verification settings, where diverse users need to understand not only whether an image is manipulated, but also why it is considered suspicious. The Explainable Deepfake Detection Challenge at ACM Multimedia 2026 is designed to benchmark this joint capability. Built on XPlainVerse, a million-scale benchmark for explainable deepfake detection, the challenge evaluates methods on image classification and grounded natural-language explanation generation. Participants submit a real/fake label together with two explanations for each image: a detailed complex explanation for technical users and a concise simple explanation for general users. The evaluation combines classification metrics with semantic similarity, simplicity, and intent-aware grounding metrics that assess whether explanations identify the relevant manipulated entities and supporting visual evidence. The methodologies developed through the challenge will contribute to the development of next-generation explainable deepfake detectors. Evaluation script, baseline models, and accompanying code are available on this https URL.

---


### 150. [CultureTalk-ID: A Multi-Task Dialogue Benchmark for Cultural Commonsense in Indonesian Local Languages](https://arxiv.org/abs/2607.21016)

**<font color=#1a73e8>作者：</font>** Muhammad Dehan Al Kautsar, Salsabila Pranida, Bilal Elbouardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Culture is lived through conversation, yet existing Indonesian cultural commonsense benchmarks evaluate LLMs on short and isolated prompts, stripping away the dialogic context in which cultural nuances actually surface. We introduce CultureTalk-ID, the first dialogue-based benchmark for cultural commonsense in Indonesian and its local languages, comprising 4,496 culturally grounded dialogues across 11 languages and 13 culturally salient topics, curated through a multi-stage human pipeline with native speakers to ensure authenticity. CultureTalk-ID introduces three complementary tasks, namely dialogue-based multiple-choice cultural commonsense reasoning, culturally faithful machine translation, and language steering, which jointly probe whether LLMs can understand, transfer, and generate culturally grounded language.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
