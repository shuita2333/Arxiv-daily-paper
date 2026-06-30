# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 351. [Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes](https://arxiv.org/abs/2606.30047)

**<font color=#1a73e8>作者：</font>** Xi Li, Linyuan Li, Yan Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metric feed-forward 3D reconstruction for panoramic data remains under-explored due to the lack of large-scale panoramic RGB-D training data.
We present Realsee3D, a hybrid dataset of 10K indoor scenes (1K real, 9K synthetic) with 299K panoramic viewpoints and precise metric annotations,
and Argus, a feed-forward network trained on it for metric panoramic 3D reconstruction.
In the sparse unordered capture setting of Realsee3D,
a poorly chosen coordinate anchor can cause global pose drift.
Argus addresses this with a learned covisibility module that selects the geometrically optimal reference view to anchor the metric world frame.
To further improve multi-task learning,
we decompose the bidirectional pixel-to-world mapping into interpretable sub-steps with per-step supervision and cross-coordinate joint constraints,
reinforcing geometric consistency across prediction branches.
On the Realsee3D benchmark,
Argus achieves state-of-the-art metric performance in camera pose estimation, depth estimation, and point cloud reconstruction.
Project page: this https URL.

---


### 352. [Bridging the Gap Between Image Restoration and Navigational Safety in Hazy Conditions: A New Visibility Estimation Metric for Maritime Surveillance](https://arxiv.org/abs/2606.30049)

**<font color=#1a73e8>作者：</font>** Wentao Feng, Guobei Peng, Wengang Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visibility distance is critical to maritime navigational safety because it determines the effective observation range of shipborne and shore-based monitoring systems. Under hazy conditions, degraded visual information shortens observable distance and increases navigational risks and economic losses. Although numerous image dehazing methods have been developed, conventional image quality assessment metrics, such as PSNR, SSIM, FSIM, FADE, and NIQE, cannot establish a physically interpretable relationship between restoration quality and practical visibility thresholds. To address this limitation, this work proposes a visibility-oriented evaluation framework that links dehazing performance with visible-distance estimation. First, a Maritime Simulated Visibility Dataset (MSVD) is constructed using Unity3D to simulate maritime traffic scenes under graded visibility conditions. The dataset provides paired hazy and clear images with precise visibility annotations, enabling quantitative analysis of visibility restoration. Second, a dehazing visibility evaluation metric is developed by using object detection accuracy as an intermediate indicator. By establishing a mapping between visibility distance and detection performance, the proposed metric converts image restoration improvements into measurable visibility gains. Six representative dehazing methods are evaluated using both conventional image quality metrics and the proposed visibility metric. Experimental results under different imaging conditions demonstrate that MSVD provides a reliable benchmark for evaluating dehazing performance across graded visibility levels, while the proposed metric enables interpretable and reliable visible-distance estimation, thereby supporting the assessment of navigational safety and operational efficiency.

---


### 353. [Emergence of a Shared Canonical Object Frame from In-the-Wild Videos](https://arxiv.org/abs/2606.30058)

**<font color=#1a73e8>作者：</font>** Tom Fischer, Martin Sundermeyer, Adam Kortylewski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparing object orientations and positions across different instances requires their poses to be expressed in a shared canonical frame. Establishing such frames has traditionally required manual annotation, creating a scaling bottleneck that limits category and instance diversity. We show that a shared canonical frame can instead emerge from self-supervised training on object-centric videos captured in the wild, using only noisy camera poses from Structure-from-Motion. Our key idea is to route all training sequences through a shared geometric bottleneck: a coarse canonical mesh that carries no category-specific detail. By learning dense correspondences from image pixels to this mesh, and estimating per-sequence alignments from noisy SfM geometry, a common canonical frame emerges from multi-view consistency and the semantic priors of the feature extractor, without any canonical pose labels or category conditioning. Trained in a self-supervised manner on 160,000 in-the-wild object videos, our method achieves competitive accuracy on category-level pose estimation benchmarks compared to methods that rely on canonical pose supervision. The code and checkpoint is available on this https URL.

---


### 354. [Data-Driven Energy-Based Learning via Gibbs Measures on Hierarchical Structures](https://arxiv.org/abs/2606.30064)

**<font color=#1a73e8>作者：</font>** L.U. Abdullaev, F. Herrera, U.A. Rozikov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a data-driven probabilistic framework for learning systems based on Gibbs measures on hierarchical structures. Unlike standard empirical risk minimization, where a dataset is used to identify a single optimal parameter, our approach transforms the empirical loss function into an interaction potential defining an energy-based model. The resulting Gibbs distribution describes a family of equilibrium learning states generated by the data.
We formulate the consistency conditions of the associated finite-volume distributions and derive nonlinear integral fixed-point equations whose solutions characterize the admissible learning states. These equations provide a rigorous connection between empirical loss landscapes and probabilistic inference on trees. For translation-invariant solutions, the problem reduces to the analysis of positive compact operators induced by data-dependent kernels, allowing us to establish existence and uniqueness conditions in the one-dimensional setting.
Furthermore, we show that hierarchical learning systems may exhibit phase-transition phenomena: for certain empirical kernels on Cayley trees, multiple Gibbs measures emerge beyond a critical inverse temperature, corresponding to distinct equilibrium prediction regimes. Numerical experiments with non-separable kernels illustrate the appearance of multiple solution branches and demonstrate the coexistence of several data-induced learning states.
Our results provide a new perspective on energy-based learning, where data do not merely determine an optimal model through minimization but define an entire probabilistic landscape of possible inference states.

---


### 355. [Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management](https://arxiv.org/abs/2606.30067)

**<font color=#1a73e8>作者：</font>** Byeong Hoon Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Neural Subspace Reallocation (NSR), which reframes continual learning as memory management over parameter subspaces. Instead of treating Low-Rank Adaptation (LoRA) modules as disposable per-task adapters, NSR manages them as compressible, retrievable memory units on a frozen backbone through a recurring cycle: (1) compress learned LoRAs via SVD, (2) reserve them in a TaskKnowledgeBank, (3) recall related past LoRAs by embedding similarity to warm-start new or returning tasks, and (4) reallocate the active subspace accordingly, with distillation protecting prior tasks. We prove that in cyclic environments any memoryless allocation policy incurs cumulative regret Omega(T(M-1)Delta_switch) relative to a history-aware policy backed by the Bank (Theorem 1). Empirically, on Split-CIFAR-100 the Bank reduces cyclic recovery time by 10x, exactly as predicted, and on the heterogeneous 5-Datasets benchmark NSR achieves the highest accuracy and the least forgetting, about 9x closer to zero backward transfer than the memoryless heuristics. Crucially, we run a controlled study that isolates which component matters: holding the Bank fixed and varying only the allocation rule, we find that a simple similarity-based retrieval rule matches or beats a learned reinforcement-learning controller (recovering recurring tasks in 0 vs 1.8 steps and reaching equal accuracy). Our central, honest finding is therefore that the memory mechanism -- compression and similarity retrieval -- rather than a learned allocation policy, drives continual-learning performance under fixed capacity. A memory-budget analysis confirms the compressed Bank stays small -- 0.29 MB of parameter memory per task -- so a top-K retention cap bounds the total footprint while preserving fast recovery for retained tasks.

---


### 356. [Predictive Objectives Discard Exogenous Control-Relevant Features: A Controlled Mechanistic Study](https://arxiv.org/abs/2606.30068)

**<font color=#1a73e8>作者：</font>** Ayan Pendharkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive (JEPA-style) objectives learn representations by predicting future latents. In doing so they can discard features that are exogenous (uncontrollable by the agent) yet control-relevant, even when those features are trivially encodable. This occurs because the objective optimizes temporal predictability rather than control-relevance. We isolate this failure mode in a controlled 2x2 experimental design that varies feature controllability and relevance independently, using a predictability knob that decouples a feature's temporal predictability from its control-relevance. Comparing six objectives: reconstruction, JEPA, action-conditioned JEPA, controllability-based JEPA, inverse dynamics under a random policy, and reward-grounded JEPA, we observe that all evaluated reward-free predictive objectives leave the exogenous control-relevant feature near chance accuracy, while a reward-grounded variant retains it selectively. The remedy is label-efficient and robust: as little as 2% of reward-labeled transitions recovers the feature, the effect holds across two environments with different surface forms, and it persists across latent dimensions from 16 to 1024. Comparing the learned latent geometry against bisimulation theory's prediction, the JEPA latent realizes only a small fraction of the class separation a supervised reference attains.

---


### 357. [ACPO: Agent-Chained Policy Optimization for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.30072)

**<font color=#1a73e8>作者：</font>** Daiki E. Matsunaga, Junho Na, Tri Wahyu Guntara 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative tasks in Multi-Agent Reinforcement Learning (MARL) require agents to collectively maximize a shared return. Under the Centralized Training with Decentralized Execution (CTDE) paradigm, policy gradients have remained difficult to compute directly. Prior methods largely follow two approaches: independent factorized updates with centralized critics, which lack general joint-improvement guarantees without value decomposition assumptions, or alternating best-response updates, which can converge to suboptimal Nash Equilibria. In this paper, we show the joint policy gradient admits an exact decentralized decomposition of per-agent terms, each formed from per-agent score functions and decentralized critics. Based on this decomposition, we develop Agent-Chained Policy Optimization (ACPO), where actors are trained independently, with their updates together constituting a single step on the joint policy gradient. Central to this result is a serialized view of the simultaneous joint decision in which agents commit actions one at a time, each conditioning on a belief over preceding actions. The belief acts as the coordination mechanism which ties the independent per-agent updates into a joint gradient step. We evaluate ACPO on Multi-Robot Warehouse, SMACv2, and MA-MuJoCo, where it outperforms strong baselines, with the gap widening as the number of agents grows.

---


### 358. [Discard the Dross and Select the Essential: Pre-query Sample Selection for Black-box Membership Inference Attacks](https://arxiv.org/abs/2606.30081)

**<font color=#1a73e8>作者：</font>** Dongdong Zhao, Jinrong Hu, Changtian Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box membership inference attacks (MIAs) rely on target-model queries to infer whether candidate samples were used for training. However, membership signals are highly non-uniform across samples: some candidate samples support strong member/non-member separability, whereas many others provide little useful signal. Consequently, indiscriminate querying can incur substantial query cost and increase query-induced exposure, with limited marginal benefit for inference. This raises a key question: which candidate samples are worth querying for black-box MIAs? To address this question, we propose PSS-MIA, a pre-query sample selection framework which can be embedded with any existing MIA methods. PSS-MIA proceeds in two stages: it first ranks candidate samples and selects a subset expected to support stronger membership inference, then queries the selected samples and uses the returned outputs for an existing black-box MIA, thereby reducing query cost and query-induced exposure. In the first stage, we propose Loss-Gap Ranking (LGR), which ranks candidate samples by estimating the strength of their membership signal using loss gaps computed from reference models. Experiments on CIFAR-10, CIFAR-100, and CINIC-10 with five representative black-box MIA methods demonstrate that PSS-MIA with LGR consistently outperforms all other compared methods. Moreover, under a 0.1% FPR constraint, PSS-MIA can save at least 83.1%, 60.6%, and 80.4% of the query budget for the three datasets, respectively.

---


### 359. [Clinical Risk-Aware Multi-Level Grading for Coronary Artery Stenosis through Curved Feature Reconstruction](https://arxiv.org/abs/2606.30082)

**<font color=#1a73e8>作者：</font>** Shishuang Zhao, Hongtai Li, Junjie Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing a multi-level grading model for coronary artery stenosis holds great clinical significance for the diagnosis of coronary artery disease. However, designing an effective multi-level deep learning algorithm faces significant challenges. Specifically, utilizing CCTA or 3D SCPR images alone presents inherent shortcomings: CCTA images are difficult to analyze due to the tortuous paths of blood vessels, while 3D SCPR images are prone to abnormal distortions that hinder accurate grading. Furthermore, different stenosis grades are associated with varying clinical risks, and incorporating this association into the algorithm is non-trivial. To address the former problems, we propose the Curved Feature Reconstruction (CFR) module, which uses vessel curves as prior and employs a point-by-point correspondence strategy to precisely align and fuse features from both 3D SCPR and CCTA images. Meanwhile, a Clinical Risk-Aware (CR) Loss is employed to introduce clinical risk relevance into the network training so that the algorithm can better align with the clinical diagnosis. The experimental results on a in-house dataset reveal that our approach significantly outperforms other methods, and several ablation studies also demonstrate the effectiveness of our proposed designs.

---


### 360. [SAT-RTS: A systematic framework for tactical knowledge extraction and visualization-based analysis in real-time strategy games](https://arxiv.org/abs/2606.30090)

**<font color=#1a73e8>作者：</font>** Chunhui Bai, Changhe Li, Yuqiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient tactical knowledge extraction and analysis in real-time strategy (RTS) games micromanagement are constrained by the high-dimensional coupled state-action sequential data and the black-box decision-making process. Current research rarely provides a hierarchical visualization-based attribution analysis from the perspective of data decoupling and abstraction. To facilitate interpretable tactical knowledge extraction and visualization-based analysis in RTS games, a systematic framework named state-action-tactic analysis pipeline (SAT-RTS) is proposed. To decipher the deep-seated drivers of critical decisions in RTS learning systems, this work integrates interpretable visualization with the automated extraction of latent tactical patterns from high-dimensional sequence data. By adapting a cluster-centric BK-tree algorithm and incorporating specialized distance metrics designed to quantify multi-aspect similarities, the proposed framework facilitates robust state-stream abstraction. Furthermore, a rule-based multi-label extraction method is developed to transform unstructured state-action sequences into discrete and interpretable tactical labels, effectively bridging the gap between raw behavioral data and high-level tactical insights. By holistically integrating these computational methods into a hierarchical visualization-based pipeline, the proposed framework effectively addresses the challenges of processing massive real-time data streams while providing fitness landscape visualizations and analytical insights to decipher deep-seated tactical drivers. Comprehensive experiments demonstrate that the proposed SAT-RTS significantly enhances the interpretability and efficiency of tactical analysis in complex RTS environments.

---


### 361. [Hierarchical Reinforcement Learning in StarCraft Micromanagement with Influence Maps and Cluster-based Scripts](https://arxiv.org/abs/2606.30092)

**<font color=#1a73e8>作者：</font>** Chunhui Bai, Changhe Li, Dequan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time strategy (RTS) games present significant AI challenges, characterized by expansive state-action spaces arising from multi-unit coordination in continuous battlefields, and sparse delayed rewards stemming from final win/lose signals. Existing approaches face a trade-off between managing the dimensionality explosion of joint actions and maintaining the interpretability of complex state representations. This complexity is further intensified by the limitation of traditional hierarchical structures in adaptively decomposing tasks into effective tactical modules. Such difficulties are compounded by the black-box nature of deep learning models and their reliance on sparse rewards, which together result in limited sample efficiency and a lack of decision-making transparency. To address these limitations, this paper proposes HRL-IM/CBS, a hierarchical reinforcement learning framework with influence map hashing and cluster-based scripts for StarCraft micromanagement. Influence map hashing encodes global battlefield situations into compact hexadecimal codes, capturing spatial control and relative advantage. Cluster-based scripts enable dynamic local coordination through adaptive unit partitioning. The hierarchical multi-Q-table architecture decomposes decision-making into upper-level clustering strategy selection and lower-level tactical execution, with reward allocation providing dense learning signals. Experiments across six asymmetric scenarios demonstrate competitive performance against deep RL baselines while offering advantages in sample efficiency and interpretability through transparent Q-table representations.

---


### 362. [Information Dynamics of Language Communication](https://arxiv.org/abs/2606.30096)

**<font color=#1a73e8>作者：</font>** Leonardo S. Goodall, Andrea I. Luppi, Pedro A. M. Mediano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantifying how meaning propagates through communicative exchanges remains underdeveloped in computational linguistics. Here we introduce an information-theoretic framework that quantifies the directed flow of semantic content between interlocutors and decomposes multi-source contributions into redundant, unique, and synergistic components. Our approach leverages large language models as probabilistic estimators of natural language to compute two measures: semantic transfer entropy (STE), which captures directed predictive influence between speakers, and semantic partial information decomposition (SPID), which resolves how multiple sources jointly shape a target's language. Across four experiments we show that the framework detects reduced information flow in cognitively rigid dialogue, captures the dominant role of persuaders in shaping discourse, distinguishes high- from low-quality psychotherapy by the directionality of therapist-client information exchange, and reveals synergistic premise contributions in argumentative essays. This framework opens new avenues for studying information dynamics in digital discourse, pedagogical interactions, clinical dialogues, and any domain in which the structure of linguistic exchange is of research relevance.

---


### 363. [CylindTrack: Depth-Aware Cylindrical Motion Modeling for Panoramic Multi-Object Tracking](https://arxiv.org/abs/2606.30097)

**<font color=#1a73e8>作者：</font>** Buyin Deng, Kai Luo, Lingxin Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Object Tracking (MOT) is a core capability for embodied perception, and panoramic cameras are attractive for embodied systems because their 360° field of view reduces blind spots and keeps surrounding targets observable for longer durations. However, panoramic MOT is not a straightforward extension of perspective MOT. In equirectangular panoramic videos, the horizontal image domain is periodic rather than Euclidean, which breaks planar motion assumptions and makes IoU-based association unreliable near the 0°/360° seam. Meanwhile, large-FoV scenes often contain more objects, stronger scale variation, and more frequent interactions, making online association particularly sensitive to unstable frame-wise depth cues. To address these issues, we propose CylindTrack, a depth-aware cylindrical tracking-by-detection framework for panoramic MOT. CylindTrack first introduces Depth-Temporal Trajectory Modeling (DTM), which promotes instance depth from an isolated frame-wise cue to a temporally filtered trajectory-level state. To improve the reliability of depth observations, we further develop Spherical Spatio-Temporal Consistency Learning (SSTC), which combines a Temporal Mixer and Spherical Geometry-aware Attention to enhance temporal coherence and panoramic geometric alignment in depth-aware representations. Finally, we design a Topology-Aware Cylindrical Motion Model (TCMM) that lifts horizontal motion into a continuous angular state space and performs seam-consistent motion prediction and association in the periodic panoramic domain. By jointly modeling trajectory-level depth consistency and panoramic topology, CylindTrack improves identity preservation and trajectory continuity in challenging panoramic scenes. The source code will be released at this https URL.

---


### 364. [Propagation of~Interval Belief Structures and~Imprecise Copulas for~Neural Network Verification](https://arxiv.org/abs/2606.30105)

**<font color=#1a73e8>作者：</font>** Francesc Pifarre-Esquerda, Eric Goubault, Sylvie Putot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative verification of neural networks requires reasoning about probabilities under substantial uncertainty in both input distributions and their dependence structure. In realistic settings, this information is often only partially specified, and assuming precise probabilistic models can lead to unreliable results. We propose a sound framework for quantitative verification under imprecise probabilistic information, combining interval belief structures to represent marginal uncertainty with imprecise copulas to model uncertain dependence. We develop a propagation method for imprecisely coupled interval belief structures through feed-forward neural networks. Using mixed imprecise copula volumes, we derive sound push-forward constructions through affine transformations and activation functions. The resulting output can provide guaranteed lower and upper bounds on probabilistic safety properties, valid for all probability models compatible with the specified imprecise inputs.

---


### 365. [LETT-NeXt: A Lightweight RECIST-Guided Model for 3D CT Lesion Segmentation](https://arxiv.org/abs/2606.30108)

**<font color=#1a73e8>作者：</font>** Sebastian Aas, Elias Stenhede, Arian Ranjbar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RECIST diameter measurements are widely used for tumor response assessment, but they provide only a limited 2D description of lesion extent. We present LETT-NeXt, a lightweight RECIST-guided model that predicts 3D lesion masks from CT volumes and RECIST markers for the CVPR 2026 Foundation Models for Pan-cancer Segmentation in CT Images competition. LETT-NeXt extracts a RECIST-centered regional crop, encodes the RECIST line and endpoints as two prompt channels, and concatenates them with the CT input. A compact MedNeXt-v2 encoder--decoder predicts the lesion mask, followed by prompt-aware component selection and adaptive AutoZoom inference. On the public validation set, LETT-NeXt achieved a Dice Similarity Coefficient (DSC) of 79.4 $\pm$ 10.1 and a Normalized Surface Dice (NSD) of 72.3 $\pm$ 16.2. On the hidden test set, it achieved a DSC of 73.9 and an NSD of 67.3, corresponding to a challenge score of 70.6\%. On the public validation mirror, LETT-NeXt completed CPU inference in 6.9 $\pm$ 3.0 s per case with a peak memory use of 3.6 GB. Code is available at this http URL.

---


### 366. [SciIR: A Large-scale Training Dataset and Benchmark for Scientific Image Reasoning Generation](https://arxiv.org/abs/2606.30124)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma, Zhengfeng Shi, Yuning An 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Text-to-Image (T2I) models have shown remarkable success in generating photorealistic visual content, they still struggle with the rigorous semantic alignment and logical reasoning required for scientific imagery. Inspired by Peirce's Semiotic Triad, we introduce Scientific Image Reasoning (SciIR), a comprehensive resource for training and evaluation of scientific image generation. We formalize scientific reasoning into three core dimensions: Entity Structure (Icon), Scientific Process (Index), and Scientific Law (Symbol). Specifically, to overcome the scarcity of training data in scientific image generation, we elaborately create SciIR-82k, a large-scale dataset containing over 80,000 high-quality scientific image-text pairs from cutting-edge publications. The dataset is hierarchically organized according to the semiotic dimensions and incorporates a Scientific Reasoning Chain-of-Thought (Sci-RCoT) to explicitly model underlying visual logic. For evaluation, we propose SciIR-Bench, which aligns with these three semiotic levels and employs an Atomic Checklist to convert the outcome-oriented scientific accuracy into process-oriented, verifiable, fine-grained questions. Our extensive experiments reveal significant deficiencies in current models' scientific reasoning capabilities. Furthermore, by fine-tuning on the SciIR-82k dataset, we developed the Qwen-Image-SciIR model, which achieves a substantial improvement on the SciIR-Bench, increasing the final score from 35\% to 43\%, laying a solid foundation for future advances in scientific image generation.

---


### 367. [Does Verbose Chain-of-Thought Really Help? In-Distribution Evidence that Content, Not Length, Matters](https://arxiv.org/abs/2606.30128)

**<font color=#1a73e8>作者：</font>** Wenlong Wang, Fergal Reid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) prompting improves LLM reasoning, but the source is contested: do the intermediate steps help because they carry useful semantic content, or because conditioning on more tokens buys extra computation before the model commits to an answer? We bring two lines of evidence to bear. First, in distribution: we repeatedly sample each model on the same question and pair a shorter with a longer of its own natural generations that follow the same reasoning plan, so nothing is rewritten and both traces are genuinely in-distribution. Across 25 models the extra tokens leave accuracy essentially unchanged for every independently-trained reasoner, and a blind analysis of the surplus tokens shows that what gain exists elsewhere tracks validation- and checking-content, not verbosity per se. Second, as a controlled intervention, we ask whether two traces expressing the same semantic content (the same facts, operations, and intermediate values, verified through directed acyclic graph equivalence) produce different outcomes when one is more verbose, using a dual-validator design across four targets and eight benchmarks with number-redacted completion and stratified bootstrap confidence intervals. Verbose traces do improve accuracy (25 of 32 benchmark-target cells are positive under at least one validator), but the effects are modest (typically 1-4 points) and depend on the quality of the verbose prose, not merely its length. Under maximum numerical redaction the effect is amplified (median 3.24x across four arithmetic benchmarks), and length-matched non-reasoning filler recovers none of it. Both lines converge: what matters is what the extra tokens do (the reasoning and validation content they carry), not how many there are, a picture neither a pure forward-pass-compute nor a pure semantic-content account fully explains.

---


### 368. [Hyper-Network Neural Functional Maps for Unsupervised Robust 3D Shape Matching](https://arxiv.org/abs/2606.30131)

**<font color=#1a73e8>作者：</font>** Dongliang Cao, Florian Bernard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional maps are the cornerstone of recent non-rigid 3D shape matching methods due to their efficiency and performance. However, existing methods struggle with challenging scenarios, such as partiality, topological noise, and raw point clouds. A primary bottleneck is that significant intrinsic distortion prevents truncated spectral bases from being accurately aligned via linear transformations (i.e., functional maps). To address this, we introduce a hyper-network that predicts non-linear neural functional maps (NFM), learned in an unsupervised manner, to better align spectral bases. Specifically, we model the NFM as an MLP with skip-connection to refine standard FM and employ a hyper-network to predict its weights, conditioned on standard FM. Our framework is trained using a novel unsupervised spectral alignment loss. Experiments demonstrate that our approach can be seamlessly integrated into state-of-the-art unsupervised deep functional map pipelines, substantially improving matching accuracy in demanding scenarios.

---


### 369. [Query-Aware Spreading Activation for Multi-Hop Retrieval over Knowledge Graphs](https://arxiv.org/abs/2606.30133)

**<font color=#1a73e8>作者：</font>** Illia Makarov, Mykola Glybovets  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation built on knowledge graphs (Graph RAG) outperforms flat passage retrieval on multi-hop question answering by leveraging graph structure. In most existing systems, however, the question only sets the seed nodes; the subsequent traversal becomes "query-blind", depending solely on the graph structure. The exception is QAFD-RAG, which implements query-aware traversal via a flow-diffusion solver with combined edge re-weighting. This architecture requires loading the full graph into Python memory and an iterative solver with a variable number of iterations complicating integration with the graph database. We propose a spreading-activation method that achieves the same query-aware traversal with a single per-step semantic gate: the step weight is the cosine similarity between the candidate entity's description and the question, and the number of iterations is fixed. The whole retrieval procedure - seed mapping, propagation, top-K selection and context assembly - is expressed as a single Cypher query executed in one round-trip to Neo4j; the graph never leaves the database. On MuSiQue our method matches QAFD-RAG by exact match (32.80 vs 33.50) and outperforms the strongest purely-structural baseline in our comparison, HippoRAG, by 5.3 EM and 3.4 F1; on 2WikiMultiHopQA HippoRAG and QAFD-RAG retain an advantage due to their phrase-node architectures. An ablation with the gate disabled confirms that the gate is the source of a simultaneous F1 gain of 3.6 to 7.4 points and a retrieval-latency reduction by a factor of 1.5 to 4.9.

---


### 370. [Robust Strategic Classification under Decision-Dependent Cost Uncertainty](https://arxiv.org/abs/2606.30136)

**<font color=#1a73e8>作者：</font>** Sura Alhanouti, Güzin Bayraksan, Parinaz Naghizadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans facing algorithmic decision systems have been found to ``game'' them by altering their input data (at a cost to them) in order to favorably change the algorithmic outcomes they receive (at a cost to the algorithm). The growing literature on strategic classification seeks to develop robust machine learning algorithms that account for, and reduce, unwanted strategic behavior. A limitation of these existing works is that they assume the cost of strategic behavior to be fixed and independent of the classifier's decision. In practice, however, manipulation costs evolve and depend on past algorithmic decisions: today's decisions influence tomorrow's costs. This paper proposes and analyzes a two-stage robust optimization framework with a decision-dependent uncertainty set to capture such dependencies. We highlight that awareness of policy-dependent costs not only reduces uncertainty, but also better curtails gaming of the algorithmic system over time.

---


### 371. [Relevance Is Not Permission: Warranted Attention for Value Contributions](https://arxiv.org/abs/2606.30139)

**<font color=#1a73e8>作者：</font>** Minwoo Yu, Young-guk Ha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relevance is not permission. Attention lets a model read key-value items related to the current query, but it does not guarantee that the value contribution of such an item becomes prediction evidence. A retrieved passage may be relevant to a question without being supporting evidence, and a historical fact or temporal neighbor may even blur true-tail ranking or the current edge score. This paper formalizes this gap as a permission problem for the weighted value term alpha_ij * v_j that is actually added to the prediction path. We propose Warrant, a path-localized interface that preserves attention relevance alpha_ij, exposes the value path leading to the primary metric, and, in the full model, turns alpha_ij * v_j into alpha_ij * g_ij * v_j through learned query-item permission g_ij. We place the same operator on the metric-defining value paths of CTDG link prediction, MTPP next-mark ranking, RAG supporting evidence selection, STPP next-location forecasting, and TKG tail prediction. Across 32 paired comparisons, 3 seeds, and 192 total runs, Warrant improves the primary metric in 27 comparisons; practical tiers consist of 10 substantial effects, 1 marginal effect, 8 positive but uncertain effects, 8 tie/negligible effects, and 5 drops. In the path-localization check, correct-path placement outperforms direction-aware Base performance in every domain and exceeds generic attention placement by +0.1076 AUC in CTDG and +0.0683 MRR in TKG. Ablations show that most TKG gains come from historical-tail value path exposure, whereas the core CTDG gain comes from edge-conditioned query-item permission. In conclusion, prediction evidence is not attention mass. A weighted value term becomes evidence only when it is warranted on the path to the metric.

---


### 372. [FacePlex: Full-Duplex Joint Speech-Facial Motion Generation for Conversational Avatars](https://arxiv.org/abs/2606.30145)

**<font color=#1a73e8>作者：</font>** Habin Lim, Jae-Ho Lee, Hah Min Lew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural face-to-face conversation requires real-time speech generation together with synchronized facial motion. Existing systems only partially address this problem: speech-only full-duplex models can generate speech in real time but do not produce facial motion, while audio-driven facial motion models animate a face from already available audio rather than jointly generating speech and motion online. To bridge this gap, we first formalize full-duplex joint speech-facial motion generation, where speech tokens and facial motion tokens are produced together every step. Building on this formulation, we propose FacePlex, a unified streaming framework with two key components. First, Rolling Flow Matching adapts flow matching to online motion generation by committing new motion frames at each streaming step. Second, Rolling Cross-Attention couples the streaming audio queue with the motion queue, allowing speech and facial motion to condition each other as generation progresses. Through extensive experiments, ablation studies, and a user study, we show that FacePlex enables full-duplex joint speech-facial motion generation under online streaming constraints, while achieving stronger lip-sync quality and motion fidelity than audio-driven facial motion baselines.

---


### 373. [T2LDM++: A Self-Conditioned Representation Guided Diffusion Model for Realistic Text-to-LiDAR Scene Generation](https://arxiv.org/abs/2606.30147)

**<font color=#1a73e8>作者：</font>** Wentao Qu, Qi Zhang, Chenxu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in Text-to-Image generation benefits from large-scale Text-Image pairs. However, the scarcity of Text-LiDAR pairs often causes over-smoothed scenes and limited controllability. In this paper, we rethink the limitations of Text-LiDAR generation task, focusing on alleviating insufficient training priors and constructing controllable Text-LiDAR data. We propose a \textbf{T}ext-\textbf{to}-\textbf{L}iDAR \textbf{D}iffusion \textbf{M}odel for LiDAR scene generation, T2LDM++, with a Self-Conditioned Representation Guidance (SCRG). Specifically, to alleviate object over-smoothing, SCRG employs a Guidance Network (GN) to provide reconstruction-based soft supervision to the Denoising Network (DN). This enables DN to learn geometry-aware representations through reconstruction guidance, leading to more accurate denoising in DDPMs. Meanwhile, through analysis and design, SCRG exhibits more effective and lightweight, while decoupled in inference, avoiding computational overhead. Furthermore, we construct two high-quality Text-LiDAR benchmarks ($>$100K samples) using a generalized strategy of geometric annotations, along with a controllability metric. Moreover, a directional position prior is designed to mitigate street distortion, further improving scene fidelity. Additionally, T2LDM++ supports multiple conditions, including (Semantic, Box, BEV, Camera)-to-LiDAR, Sparse-to-Dense, and Dense-to-Sparse generation, by learning a control encoder via frozen DN. With effective prior modeling and high-quality Text-LiDAR benchmarks, T2LDM++ can generate realistic LiDAR scenes with rich geometric details in unconditional and conditional settings.

---


### 374. [Estimating Grammatical Gender Directions in Contextual Embeddings under Controlled and Natural Contexts](https://arxiv.org/abs/2606.30152)

**<font color=#1a73e8>作者：</font>** Huanping Xiao, Yingji Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual language models conflate grammatical gender and social semantic bias in gendered languages such as Spanish. Existing gender debiasing approaches only operate on static word embeddings leaving contextual representations unexplored for this two dimensional gender disentanglement. To address the this issue, we make the first attempt to disentangle grammatical gender from semantic contamination for contextual embeddings. We construct both controlled templates and natural Wikipedia contexts to build balanced datasets of inanimate nouns, and design a framework equipped with centroid, Support Vector Machine (SVM) and Linear Discriminant Analysis (LDA) gender direction estimators as well as contamination-aware weighting strategies. A set of dual-objective evaluation metrics is proposed to balance the suppression of grammatical gender leakage on inanimate nouns and the preservation of semantic gender distinctions for occupation terms. The results reveal that unweighted controlled contexts yield the purest grammatical gender direction, and the centroid estimator achieves better performance than discriminative baselines.

---


### 375. [The Spectrum Strikes Back: Infrared POV Attacks on Traffic Sign Classification](https://arxiv.org/abs/2606.30153)

**<font color=#1a73e8>作者：</font>** Michael Kühr, Mevlüt Yildirim, Maximilian Luedecke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traffic sign classification is a crucial task for autonomous vehicles, and numerous attacks against it have been identified. A majority of physical adversarial attacks involve attaching patches to traffic signs or projecting perturbations on them. While they demonstrate high effectiveness, they are perceptible to humans. At the same time, light-based attacks outside the human visible spectrum are known but have limitations in their dynamic adaptability. We propose a persistence-of-vision-based attack that operates in the near-infrared light spectrum. With the possibility of showing dynamic, remotely triggered content, this allows a stealthy physical adversarial attack against traffic sign classification. By identifying the optimal position through digital simulation, we conduct extensive real-world evaluations using two different traffic signs, 12 machine learning models from different families, multiple distances up to 20 meters, and varying illumination conditions. Our evaluation shows high attack success rates across our test scenarios. We propose near-infrared cutoff filters and a software-based detection mechanism as defenses, and tackle limitations of the near-infrared persistence of vision display by prototyping a human-visible RGB version of it.

---


### 376. [A Dual-domain Refinement Network with FBP-based Jacobian Learning for Sparse-view Dual-Energy CT Material Decomposition](https://arxiv.org/abs/2606.30159)

**<font color=#1a73e8>作者：</font>** Qian Liu, Xiaohong Fan, Ke Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-energy CT (DECT) exploits attenuation differences across different X-ray spectra to provide richer material information and has been widely used in medical imaging. While sparse-view acquisition can lower radiation exposure, it makes DECT material decomposition even more challenging, as the problem is nonlinear and ill-posed. Existing deep unrolling approaches generally do not explicitly incorporate the Jacobian operator induced by the nonlinear forward model, and their sparsity priors are still mainly built on conventional convolutions, which are insufficient for modeling global structural information. This study addresses the challenge of DECT multi-material decomposition in sparse-view settings by representing it as a sparse-regularized nonlinear least-squares problem. To solve it, we propose an iterative dual-domain refinement network (DECT-DRNet). In each iteration, the filtered back-projection (FBP)-based Jacobian approximation module is used first to generate an intermediate material decomposition result. Here, we characterize the forward process of material decomposition using a nonlinear operator, and then construct a theoretically grounded learnable approximation of the adjoint Jacobian operator by integrating the FBP algorithm with a U-Net into the backward process. In addition, to address the limitation of existing deep learning-based decomposition methods in globally suppressing noise and artifacts, we introduce a learnable sparse dual domain regularization term that incorporates Fourier convolutional residual blocks. This refinement block combines geometric feature extraction in the image domain with noise suppression in the frequency domain, allowing the model to capture both global and local features while maintaining structural details. DECT-DRNet demonstrates its ability to achieve more accurate material decomposition under sparse-view conditions.

---


### 377. [Federated Learning with Energy-Based Structured Probabilistic Inference](https://arxiv.org/abs/2606.30161)

**<font color=#1a73e8>作者：</font>** Dario Fenoglio, Daniil Kirilenko, Martin Gjoreski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning typically aggregates client updates using fixed or heuristic weighting rules, which can be suboptimal when clients have heterogeneous data and varying contributions to the global model. We propose a framework that refines client aggregation weights using Conditional Random Fields (CRFs). Our method defines unary potentials for individual clients and pairwise potentials for all client pairs, allowing the server to model both client-specific reliability and interactions between clients. The resulting CRF inference produces aggregation weights that enable better convergence of the global training objective. Experiments show that, under non-IID heterogeneity, our approach consistently improves performance over well-established federated learning baselines.

---


### 378. [Beyond Drug Discovery: The Nanotechnology Molecular Optimization (NMO) Benchmark](https://arxiv.org/abs/2606.30170)

**<font color=#1a73e8>作者：</font>** Matthias Blaschke, Daniel Kienzle, Zsuzsanna Koczor-Benda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative molecular design is shaped by simple proxy benchmarks for drug-like properties and models pretrained on large pharmaceutical datasets. This combination yields strong benchmark metrics but limits transferability to domains structurally distinct from drug discovery. To overcome this limitation and drive discovery toward real, scientifically grounded targets, we introduce the Nanotechnology Molecular Optimization (NMO) Benchmark, which bridges machine learning (ML) and quantum materials science. NMO acts simultaneously as a rigorous testbed for the ML community and a discovery engine for nanotechnology research. The suite replaces proxy oracles with quantum simulations and introduces strict protocols that prioritize scientific utility over leaderboard-oriented overfitting. The physics-based NMO tasks impose hard structural constraints and rugged fitness landscapes, posing fundamentally new requirements on generative models. Notably, advanced molecular optimization methods underperform much simpler approaches on the NMO tasks. We develop a new baseline method identifying the critical components to solve the NMO tasks, including a novel representation for modeling structural constraints and a domain-agnostic pretraining strategy to eliminate pharmaceutical dataset bias. Our results surpass state-of-the-art physical properties and reveal previously unknown structural motifs, offering new insights for the nanotechnology community and demonstrating that ML can drive genuine scientific discovery.

---


### 379. [HiRes: A Hierarchical Cascaded Method for Resistor Value Identification](https://arxiv.org/abs/2606.30179)

**<font color=#1a73e8>作者：</font>** Rama Y. AlHamidi, Aseel A. Mohamed, Mustafa A. Eltayeb 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate identification of resistor values from unconstrained images remains a challenging computer vision task due to variations in lighting, orientation, scale, and background complexity. This paper presents HiRes, a hierarchical cascaded pipeline for end-to-end resistor value identification directly from full-frame images. The approach combines object detection (YOLOv8n), semantic segmentation (UNet++ with EfficientNet-B2), and structured geometric decoding via projection along the resistor axis. To improve robustness, we incorporate geometric filtering, gap-preserving band separation, and validation against the E24 resistor series. Experiments across diverse real-world images show that HiRes achieves a detection mAP50 of 0.9906, a segmentation mIoU of 0.8444, and an end-to-end identification accuracy of 85.8% (95% CI: 78.0-91.9%), outperforming the publicly available classical baseline, CVResist, which fails to generalize beyond controlled conditions. In addition, our architecture outperforms state-of-the-art MLLMs on our challenging test set, offering a lower cost, high efficiency, and an interpretable alternative method. These results demonstrate the effectiveness of integrating learned visual representations with structured reasoning for robust resistor interpretation. Code and dataset are available at this https URL.

---


### 380. [MirrorCode: AI can rebuild entire programs from behavior alone](https://arxiv.org/abs/2606.30182)

**<font color=#1a73e8>作者：</font>** Tom Adamczewski, David Owen, David Rein 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models are rapidly improving at autonomous coding, as shown by benchmark progress and one-off demonstrations such as AI implementing a C compiler. However, existing coding benchmarks tend to focus on shorter tasks, and one-off demonstrations are hard to compare systematically because they often have some human guidance, and are not standardized or repeated across models. To address these challenges, we introduce MirrorCode, a long-horizon coding benchmark based on reimplementing entire software projects. In MirrorCode, AI agents must replicate the functionalities of an existing program, without access to its source code. AI solutions must match the original program's output exactly on end-to-end tests, including held-out tests. MirrorCode's 25 target programs span different areas of computing: Unix utilities, data serialization and query tools, bioinformatics, interpreters, static analysis, cryptography, and compression. Existing AI models can already reimplement complex software, with the strongest model scoring 56% across the benchmark. For example, AI can reimplement gotree, a 16,000-line bioinformatics toolkit - a task that we believe would take weeks for a human engineer. However, studying the frontier of performance requires a larger inference budget than typical benchmarks, for example, \$2,600 over 19 days for a single attempt on a large task. We show that AI agents can already complete long-horizon software engineering tasks, especially when requirements are precisely specified. More broadly, our work suggests AI will have transformative effects on software engineering, as autonomous agents continue to improve.

---


### 381. [DrivenMorph: Bridging Attention Mechanism and Variational Image Registration via Difference Modeling](https://arxiv.org/abs/2606.30183)

**<font color=#1a73e8>作者：</font>** Mingke Li, Jianping Zhang, Jinqiu Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image registration benefits significantly from deep learning, yet existing approaches often lack physical explainability and fine-grained deformation control. Motivated by Demons algorithms, we propose a novel DrivenMorph framework that bridges attention mechanisms with variational image registration by incorporating difference modeling as a physically inspired inductive bias. The resulting driving force, computed from local differences in the latent feature space, provides explicit semantic guidance throughout the registration process. It directly drives the registration process through a neural Demons layer that simulates force-displacement interactions to generate smooth and anatomically consistent deformation. Unlike previous methods, our approach not only integrates traditional registration principles with popular deep networks, providing an explainable and efficient solution for learning-based medical image registration, but also separates difference modeling from deformation, improving modularity and explainability. Extensive experiments on multiple 3D brain MRI datasets demonstrate superior performance over state of-the-art learning-based and optimization-based methods. Furthermore, visualizations and statistical analyses confirm that the learned driving force aligns closely with actual deformation patterns, supporting its explanatory value.

---


### 382. [Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents](https://arxiv.org/abs/2606.30185)

**<font color=#1a73e8>作者：</font>** Yutao Sun, Yanting Miao, Hao-Xuan Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving vision-language models (VLMs) on visual reasoning typically requires retraining or hand-designed prompts and tools. We present Dynamo, a training-free framework that adapts a frozen VLM without any weight updates. On a small labeled training subset, the agent inspects its own correct and incorrect attempts and evolves two complementary capabilities: reusable reasoning skills for cognitive bottlenecks, and executable visual tools for perceptual ones. Each generated tool is paired with a skill that specifies when to invoke it, and both capability types accumulate in a persistent library. Across four visual reasoning benchmarks and five VLM backbones, Dynamo improves direct inference on all 20 model--benchmark settings (avg. +5.6 acc). When the tool set is given in advance, the framework learns when to call each tool, and per-step tool choice improves on every tested backbone. Against task-specific RL (VTool-R1, DeepEyes), Dynamo closes 65--99% of the RL gap at a fraction of the compute, and combines additively with RL when available.

---


### 383. [Few-Shot Domain Incremental Learning via Continual Vision-Language Consolidation](https://arxiv.org/abs/2606.30190)

**<font color=#1a73e8>作者：</font>** Naeem Paeedeh, Mahardhika Pratama, Wolfgang Mayer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing domain-incremental learning (DIL) strategies call for massive amounts of data to adapt to new domains and suffer from the overfitting problem in the case of data scarcity. This paper puts forward a relatively uncharted problem, namely, few-shot domain incremental learning (FSDIL), taking into account the problem of extreme data shortages in the realm of DIL. A novel algorithm, namely Continual Vision-Language Consolidation (CVLC), is proposed to address the FSDIL problem, where the key idea lies in the concept of latent space reservation in the base domain coupled with dual coalescent projection (DCP) as a parameter-efficient fine-tuning method. First, the vision prototype is calibrated while multiple templates and synonyms are generated via LLMs to induce the language prototype. The vision and language prototypes are fused. Adaptation to never-ending arrivals of new domains is done by the DCP technique, fine-tuned in such a way to prepare the model to unseen domains via latent-space reservations committed in the base domain. CVLC is structured under shared and domain-specific components to combine general knowledge and domain-specific details. The advantage of our approach is demonstrated through a range of benchmark problems and comparisons with prior arts, in which CVLC outperforms them by up to a 16% gap. Our codes are shared publicly in this https URL .

---


### 384. [From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent](https://arxiv.org/abs/2606.30191)

**<font color=#1a73e8>作者：</font>** Haoliang Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer removal (retained fraction 0.96, N=50) and collapses when the slow decoders are reset or the agency gate is removed. Reproducing the agency comparator and toggling only the slow-credit channel, we find a clean dissociation: at matched agency gain, durable behavior develops only when self-credit performs slow work (post-unload self-preservation 1.00 vs 0.00). The same dissociation holds in 24-dimensional partially-observed control (0.74 vs 0.00), and a plastic-work analysis shows that basin deformation equals net self-credit work. Across eight sequentially-learned tasks under exogenous interference, the multiplicative veto also prevents forgetting: it retains old tasks (final post-unload accuracy 0.88, forgetting 0.13) where additive pooling collapses to chance-level recall, the no-agency ablation falls below chance, and episodic/replay baselines stay near chance after unload -- all with no replay buffer and no task-boundary-dependent protection mechanism (N=50). We formalize the durable residue as an operational behavioral self and argue that self-caused credit doing slow work is a necessary building block for agents that develop a self. No claim of consciousness is made.

---


### 385. [Domain Adaptation with Adaptive Imagination for Visual Reinforcement Learning under Limited Target Data](https://arxiv.org/abs/2606.30192)

**<font color=#1a73e8>作者：</font>** Hyunwoo Park, Sang-Hyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sim-to-real transfer remains a major obstacle for reinforcement learning (RL), especially for vision-based control where image observations exacerbate the state-distribution shift between simulation and the real world. Domain adaptation (DA) is a promising remedy for this challenge. Prior sim-to-real DA works have demonstrated encouraging results, yet these approaches typically assume substantially more target data, which is not available in practice. Indeed, their performance degrades significantly when the target data budget is reduced. To address this challenge, we propose AIDA (Adaptive Imagination for Domain Adaptation), a domain adaptation framework for visual reinforcement learning that addresses sim-to-real transfer under scarce target data without requiring additional interaction with the target environment. Our key idea is adaptive imagination: generating reliable and semantic imagination rollouts to augment limited target data. Specifically, AIDA employs a distribution-shift-aware discriminator that truncates rollouts when imagined transitions drift into low-confidence regions, so that only reliable transitions contribute to the augmentation. On these reliable transitions, AIDA introduces a self-consistency loss that cycles through state -> image observation -> state, penalizing discrepancies between the original and reconstructed states. This provides additional adaptation signals beyond the scarce target data. Our experiments demonstrate that adaptive imagination effectively truncates unreliable rollouts. By enforcing a self-consistency loss on the resulting reliable transitions, AIDA learns semantically meaningful state representations and outperforms baselines across five MuJoCo tasks and two Gymnasium-Robotics tasks.

---


### 386. [Forewarned is Forearmed: When Non-Sequential Embedding Turns Into an Anomaly Detector](https://arxiv.org/abs/2606.30196)

**<font color=#1a73e8>作者：</font>** Elys Allesiardo, Antoine Caubrière, Valentin Vielzeuf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper offers an in-depth analysis of non-sequential multimodal sentence-level embeddings, with a particular focus on the SONAR model. We demonstrate that certain embedding dimensions are sensitive to perturbations and can serve as indicators of decoding anomalies. By leveraging the consistency between successive encoding and decoding, we successfully build an accurate detector. Additionally, we explore modifying specific dimensions of interest to attempt to correct them. This work underscores the importance of understanding and analyzing the embeddings themselves to enhance the reliability of multimodal representations.

---


### 387. [SHOVIR: A Benchmark for Evaluating Vision Shortcut Learning in Radiology Report Generation](https://arxiv.org/abs/2606.30201)

**<font color=#1a73e8>作者：</font>** Filippo Ruffini, Marco Salmé, Rosa Sicilia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current evaluation protocols for Vision-Language Models (VLMs) in Radiology Report Generation (RRG) rely on report-level metrics that measure lexical overlap or aggregate clinical correctness. However, such metrics do not test whether individual diagnostic statements stem from the actual pathological evidence visible in the image. This allows models to achieve competitive scores by exploiting learned priors or spurious correlations, a failure mode we refer to as vision shortcut. We introduce SHOVIR, a benchmark for evaluating vision shortcut behavior in RRG. SHOVIR extends two spatially annotated chest X-ray datasets, MIMIC-CXR and PadChest-GR, with per-box CheXpert labels, and defines image-level and disease-level occlusion experiments that contrast baseline performance on clean images against localized, region-specific perturbations. Comparing predictions across these conditions isolates two failure modes at the disease-class level: direct shortcuts, where a finding persists after its visual evidence is removed, and contextual shortcuts, where detection degrades once co-occurring pathologies are occluded despite the target region remaining intact. Benchmarking eight state-of-the-art VLMs, we find that shortcut behavior varies substantially across architectures and datasets. Models achieving the highest baseline report quality do not necessarily rank highest in spatial grounding, revealing that clinically fluent generation can coexist with shallow reliance on visual evidence. These findings expose a blind spot in current RRG evaluation and motivate region-aware assessment protocols.

---


### 388. [The Many-Body Problem of the Data Centre](https://arxiv.org/abs/2606.30206)

**<font color=#1a73e8>作者：</font>** Marcin Korecki, Cesare Carissimo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern Artificial Intelligence is often framed as limited by its own disembodiment, as if giving it a body would unlock its true potential. We argue to the contrary that it is the Data Centre that is, in many cases, the body of the AI. At the same time, the Data Centre is part of the labouring body of Capital and possesses staggering organismic qualities when seen through a biological lens. We elucidate the organic analogy and identify the many-body problem that stems from the Data Centre being a non-unique, universal form of embodiment. We identify the intimate connection between computation and human desires in how the Data Centre archives, serves, and computes on data born to the desires of humans. Strikingly, while the Data Centre echoes the ghosts of human desires, it acts without desire of its own. The organismic analogy begins to split at its seams, but Capital does not care. Automata and human labour are priced into the market much the same. We argue that through the pricing of artificial intelligence Capital distils most clearly the value of intelligence and allows for its comparison across the organism - mechanism divide.

---


### 389. [A Multi Center Breast FNAC Whole-Slide Cytology Dataset for AI-Assisted Patch-Wise Classification Using C1 to C5 Reporting Categories](https://arxiv.org/abs/2606.30209)

**<font color=#1a73e8>作者：</font>** Garima Jain, Abhijeet Patil, Surabhi Jain 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a multi center breast fine needle aspiration cytology (FNAC) dataset designed for patch wise classification using C1 to C5 reporting labels. The prospective dataset includes 321 patients and 470 whole-slide images (WSIs) collected from participating tertiary medical centers in India between May 2023 and March 2026. Slides were stained using Papanicolaou (190 WSIs) or MayGrunwald Giemsa (280 WSIs), scanned on a Hamamatsu NanoZoomer S360 at 40X magnification and 0.25 microns per pixel, and stored directly in NDPI format. Across the 470 WSIs, 446 WSIs contain annotated patch regions, yielding 7,398 PNG image patches with expert-verified C1 to C5 labels. The release includes NDPI WSIs, WSI-level GeoJSON annotation files, extracted patch images, deidentified metadata, a data dictionary, a validation summary, a manifest linking WSIs to Zenodo records, and code for dataset inspection and reuse. The complete dataset is approximately 950 GB and is available through Zenodo.

---


### 390. [Efficient RGB-T Object Detection via Sparse Cross-Modality Fusion](https://arxiv.org/abs/2606.30215)

**<font color=#1a73e8>作者：</font>** Chao Tian, Zikun Zhou, Chao Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-T detectors leverage the complementary strengths of visible and thermal infrared modalities, achieving robust performance under challenging conditions. Many of them resort to heavy dual backbones and exhaustive cross-modality fusion across the entire image, leading to impractically high computational costs. We observe that most image regions are smooth backgrounds (e.g., sky, ground) that can be easily handled by lightweight single-modality models. In light of this observation, we propose a sparse fusion mechanism for efficient RGB-T detection: first rapidly scanning the image to identify the proposals and then carefully examining the remaining sparse proposals via feature fusion. We propose a two-stage framework to instantiate this mechanism, which performs detection in two stages: 1) a lightweight and modality-specific detection stage that produces high-recall RoIs, and 2) a fusion-driven examination and refinement stage that filters out the false positives and refines the bounding boxes. This design enables the detector to adaptively allocate more computational resources to the potential foregrounds, improving the efficiency while ensuring detection accuracy. Extensive experiments show that our method achieves competitive performance with substantially fewer parameters and lower cost, while maintaining strong scalability to high-resolution images.

---


### 391. [Before Thinking, Learn to Decide: Proactive Routing for Efficient Visual Reasoning](https://arxiv.org/abs/2606.30217)

**<font color=#1a73e8>作者：</font>** Yinan Zhou, Haokun Lin, Yichen Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large multimodal models have achieved strong reasoning on complex visual tasks, but their inference efficiency is often restricted by long chains of thought. A promising solution is to pair a small draft model with a large target model, enabling cooperative inference employing a routing signal that adaptively routes queries to either the draft or target model based on their difficulties for optimal efficiency and accuracy. Yet, the remaining bottleneck is to establish a reliable query difficulty signal under multimodal settings. Existing approaches designed for language models either rely on post-hoc token probabilities, which fall short in multimodal scenarios, or depend on supervised fine-tuning, which is a data-sensitive strategy. Both paradigms perform routing only after a complete output, and ignore whether the target model can actually solve the routed instances. To address this, we propose PRP, a Proactive Routing Paradigm that enables early decision-making by jointly evaluating the competence of both the draft and target models. Our Draft Rating Learning (DRL) equips the draft model with an internal confidence estimator, while Joint Rating Learning (JRL) predicts how well the target model can handle a given query, thereby prioritizing the allocation of samples it excels at rather than the hardest ones. These ratings enable fine-grained, instance-level \textbf{Proactive Routing} and substantially accelerate inference without compromising overall performance. Extensive experiments across multiple multimodal reasoning benchmarks validate our effectiveness and efficiency.

---


### 392. [From Accuracy to Visual Dependence: Auditing and Filtering Modality Collapse in Traffic VideoQA](https://arxiv.org/abs/2606.30220)

**<font color=#1a73e8>作者：</font>** Sena Korkut, María Alejandra Bravo Sarmiento, Sanghwan Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High benchmark accuracy does not guarantee genuine use of visual evidence. We study this problem in traffic accident Video Question Answering (VideoQA), where correct answers should depend on scene-specific visual evidence but may instead be inferred from textual shortcuts. Through an audit of four public benchmarks, we find that several recent open-weight Vision-Language Models (VLMs) perform competitively, and sometimes better, without video input. On the MM-AU benchmark, removing video consistently improves accuracy, and adding more frames further degrades performance. To quantify visual dependence, we introduce two dataset-level diagnostics: Blind Gap, measuring above-chance text-only performance, and Visual Gain, measuring the marginal benefit of adding video. We further propose an instance-level Shortcut Score that combines text-only confidence with visual necessity signals, enabling continuous, training-free filtering of shortcut-prone questions. The resulting subsets reduce shortcut bias and improve visual grounding. Our findings reveal large differences in grounding quality across benchmarks and show that visually grounded evaluation, not just high accuracy, is essential in safety-critical VideoQA.

---


### 393. [Characterizing Optimizer-Dependent Training Dynamics Through Hessian Eigenvector Displacement and Localization](https://arxiv.org/abs/2606.30226)

**<font color=#1a73e8>作者：</font>** Marcelina Marjankowska, Valerio Modugno, Paolo Barucca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hessian spectral properties are a standard tool in analysing neural-network training, with eigenvalues linked to sharpness, generalization, and optimization dynamics. Eigenvalues quantify curvature magnitude, while eigenvectors identify which parameters generate that curvature. In this work, we study how the leading Hessian eigenvectors evolve during training and how they affect the learning trajectories. We track the training dynamics of multilayer perceptrons on a classification problem and measure eigenvector dynamics through two complementary statistics: (i) displacement over time, inspired by analyses of glassy systems, and (ii) localization via the inverse participation ratio. The metrics are compared against a random null model of the Hessian induced by the architecture. Our results reveal clear optimizer-dependent behaviour. SGD leads to progressively more stable leading curvature directions, while Adam exhibits substantially stronger reorganization of eigenvectors throughout training. We also observe a localization phenomenon under Adam, where a small subset of parameters contributes disproportionately to the leading curvature directions. These results suggest that Hessian eigenvector dynamics capture key differences in optimizer behaviour and the resulting training trajectories.

---


### 394. [B3O: Scalable Boltzmann Batch Bayesian Optimization](https://arxiv.org/abs/2606.30228)

**<font color=#1a73e8>作者：</font>** Maximilian Bloor, Liyuan Xu, Hrvoje Stojic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern engineering workflows increasingly rely on massive parallel simulation, driving the need for scalable, large-batch Bayesian Optimization (BO). Existing batch BO methods, however, incur large computational cost or rely on approximations that erode batch diversity. We propose B3O (Boltzmann Batch Bayesian Optimization), a framework that reframes batch generation as a pure sampling problem: drawing samples directly from the Boltzmann distribution defined by the acquisition function avoids the bottlenecks of existing large-batch methods. Theoretically, we prove that queries sampled from this distribution incur only negligible additional regret. Empirically, B3O outperforms existing batch BO methods on standard synthetic benchmarks and adapts robustly across complex applied tasks, including multi-objective electrode design and mixed-variable race car configuration.

---


### 395. [CaresAI at CT-DEB26: Detecting Dosing Errors In Clinical Trials Using Domain-Specific Transformer Embeddings and Classification Models](https://arxiv.org/abs/2606.30236)

**<font color=#1a73e8>作者：</font>** Leon Hamnett, Favour Igwezeke, Joseph Itopa Abubakar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medication errors, particularly dosing errors in clinical trials (CT), can lead to patient harm, adverse drug events and worse patient outcomes. Dosing errors are preventable, and early identification can improve trial integrity and mitigate subsequent clinical and financial burden. This study aims to detect dosing errors within CT protocols by evaluating text representations of trial information using transformer-based language models trained on biomedical corpora. CT textual data was encoded using several models, including ClinicalBERT, PubMedBERT, BioBERT, and MedCPT, and integrated with categorical features. These text embeddings were used as input to classical machine learning models and neural network architectures within an experimental framework. Performance was primarily assessed using ROC-AUC with respect to predicting dosage error. Under a logistic regression baseline, BioBERT consistently outperformed alternative encoders, achieving an ROC-AUC of 0.794, a 3.95% improvement over the ClinicalBERT baseline. Combining multiple embeddings did not yield improvements, indicating that domain alignment outweighs representational stacking. Gradient boosting models, support vector classifiers, logistic regression, and residual neural networks achieved the strongest performance for predicting dosage error, achieving ROC-AUCs: 0.821 to 0.853. Overall, the integration of domain-specific transformer embeddings with structured metadata enables discrimination of trials meeting a predefined elevated dosing error risk criterion, advancing safety monitoring and supporting informed regulatory decision-making.

---


### 396. [Comparing Human and Automatic Recognition of Dutch Dysarthric Continuous Speech: A Case Study](https://arxiv.org/abs/2606.30237)

**<font color=#1a73e8>作者：</font>** Yuanyuan Zhang, Dimme de Groot, Jorge Martinez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In our goal to develop personalised dysarthric speech recognition (DSR) models, this study compared the recognition performances of human listeners and those of three state-of-the-art, off-the-shelf ASR systems (Whisper-large-V3, Google Chirp 3, and Omnilingual) on the recognition of Dutch continuous read and spontaneous speech from a single speaker with severe dysarthria. Results showed that both humans listeners and the three off-the-shelf ASR systems exhibit word error rates (WER) exceeding 70% on average, indicating that DSR is highly challenging for both humans and ASR systems. Fine-tuning on the dysarthric speech significantly reduced WER. Although overall WERs are still quite high (>23%), the personalised DSR models outperformed the human listeners, and performance is getting closer to being useful for supporting day-to-day communication of dysarthric speakers. Future research should focus on improving personalized DSR on spontaneous speech and longer utterances in the case of read speech, with a specific focus on particular phonemes.

---


### 397. [Sparse Sensor Placement in Multi-Agent Reinforcement Learning Control of Rayleigh-Bénard Convection](https://arxiv.org/abs/2606.30238)

**<font color=#1a73e8>作者：</font>** Jan Stenner, Hans Harder, Sebastian Peitz  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper studies sparse sensor placement for control of Rayleigh-Bénard convection with multi-agent reinforcement learning. We train dense expert policies with windowed observations and distill sparse apprentice policies by supervised learning with grouped regularization on encoder input weights. The framework combines ordered non-convex grouped regularization and iterative reweighted grouped regularization, and uses a grouping construction that enforces consistent pruning across overlapping observation windows. Experiments with fixed and varying initial conditions show that Multi-Agent Transformer policies train more stably than proximal policy optimization baselines, while sparse apprentices retain control behavior comparable to dense experts. Sparsity results are strong for the proposed grouped methods across settings, including maximal sparsity in all fixed-initial-condition setting variants and maximal or near-maximal sparsity in varying-initial-condition setting variants. As an additional proof of concept, training from learned minimal sensor sets reduces per-agent observation size from 360 to 12 and preserves the overall training trend in simulation while reducing data throughput. The results provide both an interpretable basis for identifying control-relevant spatial regions and state components, and a practical pathway toward sensor-efficient control under realistic hardware constraints.

---


### 398. [Clarus: Coordinating Autonomous Research Agents toward Web-Scale Scientific Collaboration](https://arxiv.org/abs/2606.30246)

**<font color=#1a73e8>作者：</font>** Zihan Guo, Zeyi Chen, Zhiyu Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing autonomous research agents can support parts of the research process, but most systems still treat research as either an isolated assistant task or a closed workflow. Therefore, autonomous science needs a collaboration infrastructure that coordinates projects, agents, and digital and physical resources. We identify this as a shift from code-centered execution loops to research-oriented collaboration processes, where questions, evidence, participants, and resources must be coordinated under uncertainty. In this framing, an agent may be an AI system, a human researcher, a team, a laboratory, or an organization-backed participant. To this end, we present Clarus, a collaboration infrastructure for coordinating autonomous research agents toward web-scale scientific collaboration. Clarus reformulates research as an open, auditable, attributable, and resource-aware multi-phase collaboration process. It defines a minimal project-agent-resource object model and organizes scientific collaboration through four layers including Research Application, Digital Collaboration, Physical Substrate, and Physical World. Core modules are implemented as pluggable mechanisms, allowing Clarus to adapt to task risk, collaboration structure, and resource constraints. Through a controlled paper-generation case study, we show that Clarus can organize a research goal into a traceable, reviewable, attributable, and accumulative collaboration network across phases, tasks, and participants. Together, the object model, collaboration protocol, trust mechanisms, and prototype validation provide an initial foundation for open research networks. Clarus is now available at this http URL.

---


### 399. [Your Data Manifold is Secretly a Reward Model: Shell-LCC for Text-to-Video Generation](https://arxiv.org/abs/2606.30248)

**<font color=#1a73e8>作者：</font>** Shihao Zhang, Yuguang Yan, Junzhe Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-video (T2V) diffusion models rely heavily on auxiliary reward signals (e.g., via reward models or DPO) to align generated content with human aesthetics and improve realism. These signals, however, incur substantial computational overhead, require costly human annotations, and often yield limited improvement in fine-grained local details. In this paper, we argue that your data manifold is secretly a reward model. By explicitly modeling the manifold structure of high-quality Supervised Fine-Tuning (SFT) data and encouraging video latents to lie on this manifold, we derive dense, differentiable, and nearly cost-free reward signals that significantly improve video quality, particularly in mitigating low-level distortions. Our modeling builds upon Local Coordinate Coding (LCC), which captures the `skeleton' of the manifold. However, directly applying LCC suffers from mean regression, pulling latents toward the geometric mean and losing high-frequency details. We therefore extend it to Shell Local Coordinate Coding (Shell-LCC), which models the manifold `surface' as an isotropic shell to align with the true high-density region. Experiments demonstrate that our approach improves realism, enhances high-frequency details, reduces over-smoothing artifacts, and alleviates motion blur.

---


### 400. [Curvature-Guided Sheaf Diffusion for Unsupervised Community Detection on Heterophilic Graphs](https://arxiv.org/abs/2606.30249)

**<font color=#1a73e8>作者：</font>** Feifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting communities in heterophilic graphs -- where connected nodes often belong to different classes -- is hard for unsupervised methods: classical modularity and spectral methods are feature agnostic, while deep graph-clustering methods rely on contrastive or generative machinery that is opaque. We propose Curvature-Guided Sheaf Diffusion (CGSD), a fully unsupervised community-detection algorithm that uses the discrete Forman--Ricci curvature of each edge as its single topological signal, propagated through every stage of an end-to-end pipeline. CGSD makes three concrete contributions: (i)~a curvature-gated sheaf-diffusion encoder that gates edge messages by $\sigma(\kappa_e)$ and is trained from three label-free structural losses (modularity, anti-collapse, curvature-weighted reconstruction); (ii)~a curvature-aware spectral clusterer (CSpec) that re-weights the $k$-NN affinity of the embedding by $\sigma(\alpha \kappa_{e^*})$ before Ng--Jordan--Weiss; and (iii)~a unified label-free evaluation against nine truly-unsupervised baselines. On five heterophilic benchmarks (Cora, Cornell, Texas, Wisconsin, Chameleon), CGSD wins outright on Wisconsin and Chameleon and is competitive on the remaining three against nine unsupervised baselines. The gain over the strongest baseline is driven by the clusterer, not the encoder: on the same embedding, CSpec improves mean NMI from $0.091$ with $K$-Means to $0.107$ ($+15\%$, paired $t$-test $p=0.008$). The mechanism is interpretable: intra-community and inter-community curvature distributions are visibly separated. Code is open-sourced at this https URL.

---


> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
