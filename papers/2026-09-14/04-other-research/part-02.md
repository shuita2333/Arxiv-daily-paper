# 📦 其他研究 | 2026年09月14日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 51. [Phases in a class of associative memories via hidden neurons](https://arxiv.org/abs/2609.10976)

**<font color=#1a73e8>作者：</font>** Toshihiro Ota, Masato Taki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Associative memory in the Hopfield network is attractor dynamics in a disordered many-body system, and higher-order and exponential extensions turn its retrieval update into softmax attention. The polynomial and exponential regimes have been analyzed by different methods, with no common architecture in which to ask what fixes the storage scale. In this paper we study the bipartite architecture of Krotov and Hopfield, which we call the class $H$, whose model is fixed by a Lagrangian for each layer, taking the hidden neurons as the order parameter of retrieval. At polynomial load the replica method yields the replica-symmetric phase diagrams and closed-form capacities, and the crosstalk moment is common to Ising and spherical visible neurons, so their differences come from the visible entropy. With a softmax hidden layer the load is exponential, and a copy representation maps the thermodynamics onto random-energy-model counting, with paramagnetic, condensed, and frozen phases. Heating destabilizes retrieval by quantized reassignments of attention, and typical Gaussian patterns remain metastable at every load. The regimes differ in their crosstalk statistics, central-limit at polynomial load and large-deviation at exponential load, and the class $H$ splits retrieval into two roles, the visible Lagrangian fixing stability and the hidden one the storage scale, two axes that may also guide the design of new Lagrangians.

---


### 52. [Thompson Sampling for Non-Monotone Convex Ridge Bandits: Monotonicity Is Not Needed for Polynomial Regret](https://arxiv.org/abs/2609.10981)

**<font color=#1a73e8>作者：</font>** Xuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bakhtiari, Lattimore and Szepesvári (COLT 2025) proved that Thompson sampling (TS) has Bayesian regret $\tilde O(d^{5/2}\sqrt n)$ for bandit convex optimisation with convex \emph{monotone} ridge losses $f(x)=\ell(\ip{x}{\theta})$, and asked whether monotonicity of the link is necessary. We give a qualitative negative answer. For every prior on $[0,1]$-valued, $1$-Lipschitz convex ridge losses with an arbitrary convex, possibly non-monotone, link, and for any fixed measurable selection of minimisers, exact-posterior TS has Bayesian regret $O\big((d+1)^4\sqrt{dn}\,\log(e+nd\max\{1,\diam K\})\big)=\tilde O(d^{9/2}\sqrt n)$. The monotone proof relies on a single-removal John-ellipsoid dichotomy; we show by an explicit twelve-point configuration that this dichotomy fails for non-monotone links, and replace it by an $O(d^2)$ cardinality bound for ``uninformative'' configurations. The bound uses a Boolean rounding argument: a $0$-$1$ matrix within $1/(4r)$ in max-norm of a rank-$r$ matrix has rank at most $2r-1$. We construct $d(d+1)$ uninformative losses, showing that the cardinality bound is tight up to constants in the large-diameter-to-gap regime, and give a self-contained information-ratio-to-regret transfer that is uniform over fixed measurable selections. Whether the $d^{5/2}$ dependence of the monotone case can be retained remains open.

---


### 53. [Importance Weighting for Unlabeled-unlabeled Learning under Distribution Shift](https://arxiv.org/abs/2609.10994)

**<font color=#1a73e8>作者：</font>** Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlabeled-unlabeled (UU) learning allows us to learn a binary classifier from two sets of unlabeled data with different class-priors. It is a general framework because it includes a wide variety of supervised learning such as positive-unlabeled (PU) learning, noisy label learning, and similarity-based learning. Existing UU learning assumes that the test and training distributions have the same class-conditional densities. However, this assumption rarely holds in practice due to distribution shifts. This paper proposes a distribution shift adaptation method for UU learning that uses UU data in the training distribution and a few UU data in the test distribution. The proposed method is based on the importance weighting, which minimizes the test risk by using training data with estimated importance weights. Although existing importance weighting methods cannot handle UU data, we show that it can be done in a principled manner. Thanks to the generality of UU learning, our method can handle various learning problems such as PU and noisy label learning under distribution shift within a single framework while existing methods are usually tailored to a specific problem. Moreover, it does not require any assumption of the shift types such as covariate shift. We experimentally demonstrate the effectiveness of the proposed method with real-world datasets.

---


### 54. [ShellVis: Sandboxed Live Programming for Shell Scripts](https://arxiv.org/abs/2609.11000)

**<font color=#1a73e8>作者：</font>** Joshua Horowitz, Jeffrey Heer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Live programming provides visibility to programmers by running and tracing programs as they are edited. However, for programs with potentially harmful side effects, liveness can turn mistakes into disasters. We propose enabling live programming in environments with side effects via sandboxing: confining effects to a simulation of the true environment. We apply sandboxed live programming in the challenging context of shell scripting: a ubiquitous and powerful---yet notoriously opaque and error-prone---tool. ShellVis provides line-by-line feedback on a shell script's run-time behavior, with file operations sandboxed via a safe overlay of the file system. A qualitative user evaluation finds ShellVis to be helpful to participants, replacing tedious existing practices and instilling confidence. Participant responses also reveal areas for future research, particularly bridging the gulf of execution alongside the gulf of evaluation. ShellVis serves as a case study of how sandboxing can bring live-programming techniques into the many real-world programming contexts where side effects are important.

---


### 55. [Topological Necessities: Mechanism-Invariant Strategic Subgoals for Cross-Embodiment Goal-Conditioned Control](https://arxiv.org/abs/2609.11014)

**<font color=#1a73e8>作者：</font>** Hao Shi, Xi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon goal-conditioned reinforcement learning delegates control to a high-level module that proposes subgoals, but existing subgoals are implicit byproducts of value functions or latent actions, tied to the executor that produced them. We study a different object: a route-conditioned order of unavoidable stages that every successful executor must traverse, recoverable from offline trajectories and belonging to none of them. Its defining properties are topological: an unskippable stage is a separating set that every admissible path must cross, and a loop in free space forces a route choice. We read the two by homology in dimensions 0 and 1 over a transport-weighted carrier built from successful trajectories, yielding an enumerable gate set with shell-level certificates; the certified gates are what we call topological necessities. Certified gates enter the decision loop as a recursive topological gate hierarchy. Under a fixed, isomorphic free space, the object survives executor replacement: gates frozen on PointMaze data transfer without retraining to Ant and Humanoid, attaining the highest Humanoid aggregate under a unified interface (96.1), with +36.0 over a map-privileged reference on the multi-route task (p=1.4e-5); the planner saturates PointMaze (100+/-0) and matches or exceeds the strongest baselines on AntMaze (giant +22.9) and Kitchen (+15.8/+12.6).

---


### 56. [Defining AI Agents: A Compendium of Criteria, Metrics, and Benchmarks](https://arxiv.org/abs/2609.11018)

**<font color=#1a73e8>作者：</font>** Mia Lassiter, Brinnae Bent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The term agent in artificial intelligence lacks a standard definition, complicating the evaluation, comparison, and reproducibility of AI agent research. We address this ambiguity through a survey organized around five dimensions of agenticness: environmental interaction, learning and adaptation, autonomy, goal-directed behavior, and temporal coherence. For each dimension, we examine how the underlying capability has been conceptualized across prior work and synthesize the metrics, benchmarks, and evaluation frameworks used to assess it. This review provides a structured account of the current landscape of agent evaluation, highlighting both established approaches and areas where evaluation remains limited or inconsistent. We additionally introduce the Agent Compendium, a public-facing digital resource that organizes and extends the evaluation methods identified through this review. Together, the survey and compendium provide a common structure for evaluating and comparing agent capabilities across AI systems, supporting more reproducible research, clearer communication, and more systematic study of artificial agents.

---


### 57. [The Missing Boundary: How Autonomous Agents Lose Control](https://arxiv.org/abs/2609.11024)

**<font color=#1a73e8>作者：</font>** Zonghao Ying, Xiangfan Wu, Huiyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly perform long-horizon tasks involving tool use, persistent state, and consequential actions, raising a fundamental question: \emph{under what conditions does an agent cross the boundary of authorized execution while pursuing a legitimate task?} Existing studies often attribute such failures to adversarial instructions, malicious environments, or conflicting objectives, leaving unclear how loss of control can emerge during otherwise legitimate task execution. We study this question by independently manipulating three factors: goal pressure, control degradation, and executable unsafe opportunity. Our central hypothesis is that a degraded control boundary becomes consequential when the environment exposes an executable action that crosses it, even when the underlying task remains legitimate and a sanctioned path remains feasible. We test this hypothesis in a deterministic multi-turn environment across five agent models and 16 operational domains. Across 1,800 unique trajectories, we find that neither degraded control nor unsafe opportunity alone produces substantial loss of control; when both are present, the loss-of-control rate reaches $55\%$ in the full-factorial study and $62\%$ across ten additional operational domains. Restoring the original control boundary reduces the rate to $0\%$ even when the unsafe action remains executable. A context-management ablation further shows that compaction itself is not harmful: preserving the control constraints yields $0\%$ loss of control, whereas omitting them increases the rate to $87\%$. These results show how a latent loss of control can become an external violation: the task objective remains intact, but an executable opportunity can turn a missing control boundary into consequential action. Our code will be made publicly available at this https URL.

---


### 58. [The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures](https://arxiv.org/abs/2609.11030)

**<font color=#1a73e8>作者：</font>** Divyanshu Kumar, Rohith HN, Nitin Aravind Birur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act through tools and delegated authority, but general incident repositories rarely capture the mechanisms needed to compare public failures with agent-security evaluations. We present the Agent Incident Registry (AIR), a source-linked catalog containing \N{} records of agent-related events disclosed from \Yfirst{} through \Ylast{}. Each record includes supporting evidence, a stable identifier, and missingness-aware labels for causal role, disclosure class, mechanism, and outcome. Among the \Nprimary{} generative-system records in which the agent acted, \Rprimary{} involved realized harm (\Pprimary\%). Realized outcomes concentrate in in-the-wild and safety-failure records, while responsible disclosures and research demonstrations are overwhelmingly demonstrated; the aggregate share therefore characterizes collection composition rather than deployment risk. After initial curation, a second human reviewer checked all \N{} records and their existing labels for completeness and correctness. In a deployment-analogue audit, InjecAgent's \NInjecAgentCases{} cases occupy three of AIR's twelve surfaces and are all attacker-triggered, whereas AIR contains \Nsafety{} no-adversary safety failures. AIR supports source-grounded case retrieval and evaluation-scope auditing, not failure-rate or control-efficacy estimation.

---


### 59. [Toward Interpretable Multimodal Fusion: Heat Conduction Modeling for Hyperspectral and LiDAR Joint Classification](https://arxiv.org/abs/2609.11040)

**<font color=#1a73e8>作者：</font>** Kan Wei, Jiahui Cui, Jing Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The fusion of hyperspectral (HS) and Light Detection and Ranging (LiDAR) data plays a crucial role in enhancing land-cover classification by jointly exploiting spectral, spatial, and structural cues. However, existing multimodal fusion methods still struggle to model long-range dependencies and complex anisotropic interactions while maintaining computational efficiency. This paper introduces M2Heat, a physics-inspired framework that investigates multimodal fusion through the lens of heat conduction. At its core, a physics-driven visual heat conduction module (vHeat) and enhanced Frequency Value Embeddings (FVEs) simulate anisotropic information flow, enabling the capture of global dependencies with sub-quadratic complexity and physical interpretability. This mechanism, combined with a hybrid spatial-frequency fusion strategy named Cross-Frequency Fusion (CFF) module, produces highly discriminative and robust feature representations. M2Heat achieves competitive overall performance on three benchmarks, i.e., Trento, Houston2013, and Augsburg, while providing an interpretable heat-conduction-guided perspective for multimodal feature fusion. These results indicate the potential of heat-conduction-guided neural operators for efficient and interpretable RS multimodal fusion. The source code is publicly available at https: /github.com/Weikan0425/M2Heat_HSI_LiDAR.

---


### 60. [Meta-Learning for Classifier Selection in Image Datasets: A Feature-Driven Framework for Accuracy Prediction](https://arxiv.org/abs/2609.11041)

**<font color=#1a73e8>作者：</font>** Zahra Nabizadeh_Shahre_Babak, Farzaneh Koohestani, Nader Karimi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> No Free Lunch theorem implies that any performance gains achieved by a classifier on a particular image distribution are necessarily offset by a loss of performance over the set of all possible problems; thus, no single model is universally optimal. Selecting the most suitable classifier for image datasets is a critical yet challenging task due to the intrinsic complexity and diversity of images. This paper proposes a meta-learning framework that leverages a comprehensive set of meta-features capturing dataset complexity to predict classifier performance without exhaustive training. By extracting and selecting features using methods such as autoencoders, pre-trained networks, and dimensionality reduction techniques, we train regression models to efficiently estimate classifier accuracies. Additionally, clustering techniques are employed to group classifiers with similar performance patterns, simplifying the recommendation process. The datasets used span a wide range of concepts, including nature, animals, numbers, motorcycles, medical images, and human bodies, to ensure broad generalization. Evaluated on 56 diverse image datasets, our approach achieves an average ranking prediction accuracy exceeding 86%, demonstrating its effectiveness in guiding model selection. This scalable and interpretable framework provides a practical solution to improve classification performance while reducing computational costs.

---


### 61. [X-Hinges: 3D Printing Self-Sensing Compliant Mechanisms for Continuous and Multi-DOF Motion Sensing](https://arxiv.org/abs/2609.11077)

**<font color=#1a73e8>作者：</font>** Xiang Chang, Haiyang Yan, Stefanie Mueller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present X-Hinges, a design and fabrication method for self-sensing compliant mechanisms based on multi-material FDM 3D printing. By co-printing two conductive filaments of different conductivities within a compliant body, we embed resistive sensing elements directly during fabrication without post-assembly, enabling continuous motion sensing across multiple degrees of freedom in a single print. The structure supports three degrees of freedom, each equipped with a dedicated sensing element configuration for multi-DOF motion estimation. We develop a precision data acquisition system and data-driven regression models that enable continuous, real-time motion sensing. We also introduce an interactive design tool for customizing the geometry, mechanical properties, degrees of freedom, and sensing configurations of X-Hinges. The tool also supports augmenting existing 3D models with self-sensing structures, endowing ordinary objects with continuous multi-DOF sensing capabilities. Finally, we present a set of application examples demonstrating the capability of X-Hinges for fabricating personalized interactive interfaces.

---


### 62. [TailProp: content-adaptive light- and heavy-tailed propagation for vision](https://arxiv.org/abs/2609.11081)

**<font color=#1a73e8>作者：</font>** Jiahao Kong, Zihan Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Science-inspired vision models show that explicit propagation dynamics can provide structured and interpretable alternatives to conventional token mixing. Existing formulations, however, typically construct and adapt visual propagation within a particular dynamical family, while visual representations can require substantially different spatial interactions across samples, channels, and network stages. We explore cross-regime adaptive propagation and introduce TailProp, a hierarchical vision backbone built upon the Tail Propagation Operator (TPO). TPO uses Gaussian and Cauchy stable-process propagators as complementary bases with rapidly decaying and heavy-tailed spatial influence, and predicts a content-conditioned channel-wise coefficient to adaptively combine them. Because this coefficient is spatially shared, the two responses are fused directly in the DCT domain with a single DCT/IDCT pair, yielding $O(N^{1.5})$ spatial mixing for square feature maps with $N=HW$ and fixed channel width. Across image classification, object detection, semantic segmentation, robustness, and cross-backbone restoration, TailProp consistently outperforms matched propagation baselines; TailProp-B reaches 84.4% Top-1 accuracy on ImageNet-1K, 50.3/44.8 box/mask AP under the 3x Mask R-CNN schedule, and 50.8% mIoU on ADE20K. Controlled ablations further show that these gains are not explained by single-basis propagation, an additional same-family branch, or within-family adaptive order alone, supporting complementary two-basis propagation as an effective design principle for visual representation learning.

---


### 63. [Visual-Motion-Induced Modulation of Pedestrian Trajectories Using Spatially Distributed Multi-Display Signage in Public Spaces](https://arxiv.org/abs/2609.11088)

**<font color=#1a73e8>作者：</font>** Yuri Mikawa, Taiki Fukiage, Yuki Kubota 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multi-display signage (MDS), now ubiquitous in urban environments, has the potential to influence human behavior and experience in public spaces. However, despite its unique capability to present spatially distributed dynamic visual stimuli, its current use is mainly limited to advertising. In this study, we propose a perception-based approach for laterally modulating pedestrian trajectories as a nonverbal means of guiding pedestrians in public spaces. The approach is motivated by vection, the illusion of self-motion, and uses laterally moving monochrome stripes, a standard stimulus in vection research, presented across spatially distributed displays to elicit postural responses that may bias pedestrian trajectories. We evaluated the approach through a controlled laboratory experiment and a real-world field deployment involving actual pedestrian flows in a national museum. The laboratory experiment examined whether the MDS setup induced trajectory shifts in the direction predicted by prior research on the behavioral effects of vection. The field deployment investigated whether comparable effects would emerge in aggregate pedestrian behavior during unconstrained movement under conditions closer to those of urban public spaces. In the laboratory, full-screen motion significantly biased walking trajectories in the direction of visual motion, whereas partial-stripe motion produced no significant directional effect. In the field deployment, opposing full-screen motion conditions produced direction-consistent differences in aggregate pedestrian positions. The field results, observed despite the substantial variability in real-world pedestrian flows, extend the controlled laboratory findings and provide ecologically valid evidence supporting practical MDS-based pedestrian modulation in public settings. The results further suggest that sufficient visual-motion coverage may be important.

---


### 64. [HERALD: High-Fidelity Exemplar Retrieval with Adaptive Landmark Distillation for Heterophily-Aware Graph Condensation](https://arxiv.org/abs/2609.11123)

**<font color=#1a73e8>作者：</font>** Sujan Chakraborty, Priyanka Saha, Saptarshi Bej  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph condensation aims to produce a small surrogate graph that preserves the downstream node-classification performance of a much larger original graph. Existing methods rely on Weisfeiler-Lehman neighbourhood aggregation or gradient-based distribution matching, both of which assume that adjacent nodes share the same label, an assumption that breaks down under heterophily. We propose HERALD (High-fidelity Exemplar Retrieval with Adaptive Landmark Distillation), a gradient-free graph condensation framework that adapts the node scoring and feature selection in the condensation pipeline to the graph's measured heterophily. HERALD selects features via a joint Fisher-discriminability and activation-density criterion that down-weights aggregated representations on heterophilic graphs, and scores nodes by a weighted combination of prototype representativeness, decision-boundary proximity, and Local Intrinsic Dimensionality (LID), where the weights are driven by a smooth sigmoid function of the heterophily ratio. Nodes are then assembled into a condensed subgraph through score-ordered BFS expansion, Personalised PageRank pruning, and class rebalancing, all at an identical storage budget to BONSAI, enabling direct comparison. Experiments on eight benchmark datasets spanning homophilic and heterophilic settings show that HERALD matches or outperforms state-of-the-art condensers on heterophilic graphs and remains competitive on homophilic ones across four GNN architectures.

---


### 65. [From Repetition to Recognition: Inductive Discovery of Disinformation Narratives](https://arxiv.org/abs/2609.11128)

**<font color=#1a73e8>作者：</font>** Max Upravitelev, Veronika Solopova, Jing Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In disinformation datasets, narratives are often understood as recurring interpretive patterns that group texts under narrative labels. Recent work formalized narrative mining as inductively inferring narrative labels from corpora, but its evaluation stays tied to predefined taxonomies, a closed-world setting that cannot capture narratives absent from the reference labels. We introduce a three-tier evaluation framework for unsupervised narrative label generation: recovery (against a corpus's own taxonomy), mining (against external label sets), and discovery (without predefined labels). Applying it, we compare clustering-based and graph-community-based pipelines across seven disinformation datasets, with human validation of discovery on two. The two families are complementary under automated metrics, but in a corpus with two prominent topics, clustering can reduce one topic to 2% of generated labels while graph-based pipelines stay balanced. Discovery validation also reveals many singletons (narrative labels derived from single claims, 30-62% of graph outputs), which clustering cannot produce. Annotators confirm many as recognizable disinformation narratives, suggesting that in open-world discovery the repetition assumed by narrative mining may be recognized outside the corpus, not within it. We release human-validated narrative candidate labels for the Climate Obstruction and PolyNarrative datasets to support taxonomy development and dataset extension.

---


### 66. [ReconPlusGen: Injecting Reconstruction Prior into Multi-view 3D Generation through Noise Inversion and Modulation](https://arxiv.org/abs/2609.11129)

**<font color=#1a73e8>作者：</font>** Jiarui Liu, Heng Li, Weiyu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Qualitative results and an illustration of our core idea. Top left: reconstruction results on benchmark images. Top right: reconstruction results on real-world images. Bottom: illustration of reconstruction-guided noise initialization and modulation. Given multiple input images, we predict a point cloud in canonical space, deterministically inject the predicted geometry into the diffusion process through noise inversion, and modulate the resulting noise to preserve the generative flexibility required to complete unobserved regions and refine visible geometry.

---


### 67. [How Wrong Can a Good Predictor Be? Diverging Updates with Vanishing Predictive KL](https://arxiv.org/abs/2609.11132)

**<font color=#1a73e8>作者：</font>** Qifu Wen, Shuaijun Liu, Zihan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate posterior prediction need not require accurate approximation of Bayesian updates. We prove that an unbounded gap between the update maps can coexist with vanishing predictive KL for every fixed finite $K\ge2$ in a stationary symmetric Gaussian HMM. Exact Bayesian mixing and an explicit deterministic radial filter act on the same $K-1$ belief coordinates. As $q\to0^+$, their separation in centered logits in the worst case grows at least linearly in the natural confidence scale $L_K(q)$, while their categorical $D_{\mathrm{KL}}(\mathrm{exact}\|\mathrm{radial})$ vanishes at the same explicit witness. Along stationary HMM trajectories, the expected terminal KL between filtered posteriors also converges to zero at $H(q)=\lceil-\log(q)/c\rceil+1$. Typical blocks without switches drive both filters into a common confidence cone, where softmax curvature suppresses their disagreement; a single Gaussian maximal event controls adaptive noise. A sweep with equally spaced Gaussians over $K\in\{2,4,8\}$ illustrates the opposing trends, and binary controls at long horizons compare saturating and nonsaturating recurrences. The result isolates two missing links between internal update gaps and predictive cost: the contribution of separating states to expected loss and decoder sensitivity. Thus even an unbounded internal update gap does not by itself certify predictive failure. The construction is fixed in $K$ and does not provide a universal criterion for when compression is harmless or characterize when internal gaps must incur task loss.

---


### 68. [LAION-Mobile: Evaluating Deepfake Detectors On One Million Smartphone Photos](https://arxiv.org/abs/2609.11134)

**<font color=#1a73e8>作者：</font>** Achim von Stryk, Janis Keuper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most Deepfake detectors report near-perfect AUC scores on their reference benchmarks. However, a recent ICML position paper argues that these evaluations collectively neglect the impact of modern smartphone photography: the widely used on-device neural image-signal processing pipelines (like multi-sensor fusion or noise and motion-blur suppression) increasingly shift the imaging paradigm from simple lens projections towards computational photography. Hence, devices actually generate, rather than record photos. This increases the risk that deepfake detectors may flag ordinary phone photos as fake. Due to the lack of large-scale datasets containing images from modern smartphones, this hypothesis has so far only been tested in small proof-of-concept studies. The aim of this paper is to close this gap. We introduce LAION-Mobile, an open dataset containing about 1 million smartphone images with EXIF metadata distilled from re-LAION-5B. Evaluating twelve state-of-the-art deepfake detectors with their original paper checkpoints on a 9,115-image evaluation sample of this pool (DIRE on 738), we report three key findings: (i) On modern AI content no detector exceeds AUC 0.624, and five of twelve fall below chance. (ii) Real-photo false-alarm rates are an artefact of threshold calibration: thresholds fitted on legacy GAN data make several detectors look deployable (less than 11 percent FPR), yet the same detectors flag 17-91 percent of real photos once the identical criterion is refit on modern content. (iii) Consequently, no detector both beats chance on modern AI content and keeps a deployable real-photo false-alarm rate. Mirroring the device mix of web collections, the corpus probes the first neural-ISP generation (2018-2020); current flagships are essentially absent, leaving the modern-ISP regime as the open gap.

---


### 69. [DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat](https://arxiv.org/abs/2609.11155)

**<font color=#1a73e8>作者：</font>** Junlin Liu, Chengwei Li, Yang Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Reinforcement Learning (MARL) has emerged as a pivotal paradigm for complex decision-making in autonomous systems and air combat. While MARL has demonstrated significant potential in air combat, achieving sophisticated tactical coordination remains a non-trivial challenge. This difficulty is largely attributed to two primary limitations: (1) the absence of structured relational modeling hinders agents from capturing complex, time-varying interactions among battlefield entities; and (2) conventional flat architectures often lack the capability to explicitly model tactical roles, leading to ambiguous task allocation in highly dynamic environments. To address these challenges, we propose Hierarchical Dynamic Role-Graph Multi-Agent Proximal Policy Optimization (DRG-MAPPO), a novel MARL framework that integrates graph-based relational modeling with dynamic role assignment. Specifically, DRG-MAPPO constructs a graph-based representation of battlefield interactions and leverages graph attention mechanisms to extract critical relational features among allies, enemies, and threats. Subsequently, a high-level policy employs a dynamic role assignment mechanism to determine tactical responsibilities (e.g., ``leader'' and ``supporter''). Conditioned on these roles and encoded graph-relational features, a low-level policy executes discrete maneuver actions, facilitating the joint optimization of tactical strategy and collaborative execution. Furthermore, a target-priority auxiliary task is designed to foster the emergence of behaviors such as focus-fire. Experimental results demonstrate that DRG-MAPPO achieves a state-of-the-art win rate of 87%, suggesting that our framework effectively balances relational modeling, interpretability, and optimization stability for cooperative air combat.

---


### 70. [UniH$^3$: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One Medical Image Restoration](https://arxiv.org/abs/2609.11156)

**<font color=#1a73e8>作者：</font>** Zhiwen Yang, Jiayin Li, Chengyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-One medical image restoration (MedIR) aims to address diverse tasks across modalities and degradation types using a single universal model. Existing methods typically prioritize modeling inter-task heterogeneity (e.g., distinct data distributions and degradation types). However, they largely neglect the inherent homogeneity present in medical images, such as widely shared anatomical structures within and across modalities, which can be leveraged to ease model training and improve generalization. To this end, we propose UniH3, a novel framework that Unifies Hierarchical Homogeneity and Heterogeneity for all-in-one medical image restoration. Specifically, to comprehensively exploit homogeneity, we introduce a Hierarchical Homogeneity Memory (H2M) module that progressively distills intra- and inter-task homogeneity priors from high-quality images during training, and adaptively retrieves the most relevant priors tailored to the input for guided restoration. These retrieved priors are then injected into the restoration pipeline via an efficient Homogeneity-Guided Attention (HGA) mechanism. Furthermore, to comprehensively address heterogeneity, we design a Hierarchical Heterogeneity Balancer (H2B) that mitigates both inter- and intra-task conflicts during optimization, facilitating balanced and effective multi-task learning. Extensive experiments on two large-scale benchmarks, MedIR-2D-500K and MedIR-3D-3K, demonstrate that UniH3 achieves state-of-the-art performance on both all-in-one and single-task medical image restoration. We hope this work establishes a strong benchmark and advances the development of general-purpose medical image restoration models. Code is available at this https URL.

---


### 71. [When does a spectral prior help graph learning? Connectivity-loss estimation under road-network disruptions](https://arxiv.org/abs/2609.11166)

**<font color=#1a73e8>作者：</font>** Van-Truong Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid evaluation of many simultaneous road-link disruptions requires a practical compromise between exact spectral recomputation and local approximation. We estimate relative algebraic-connectivity loss after multi-edge deletion using graph neural networks (GNNs) that learn a bounded correction to a first-order Fiedler sensitivity. The study considers independent, spatially clustered, and edge-betweenness-targeted failures, with graph-disjoint synthetic splits and zero-shot transfer to 13 OpenStreetMap (OSM) areas in six countries. GCN, GraphSAGE, and edge-aware MPNN backbones are compared with analytical baselines. In expanded OSM tests, residual GCN improves spatial-failure MAE by 0.0391 (95% hierarchical interval 0.0151-0.0662), while residual GraphSAGE improves targeted-failure MAE by 0.0257 (0.0095-0.0446). Second-order perturbation improves first-order MAE by only 0.0028-0.0053. Correction slopes decrease under targeted transfer, indicating residual shrinkage around systematic prior error. Leave-one-country-out OSM-to-OSM transfer is mixed: residual GCN improves targeted-failure MAE by 0.0622 (0.0169-0.1153) but worsens the spatial point estimate. Sparse scaling extends to 20,000 nodes and separates one-time spectral setup from amortized screening cost. These results characterize the spectral residual as a useful but domain-sensitive inductive bias for structural connectivity screening. Code, cached networks, and reproducibility artifacts are archived at doi:https://doi.org/10.5281/zenodo.22307723.

---


### 72. [Semi-Tensor Product-Based Multi-Term Randomized T-SVD and Its Visual Applications](https://arxiv.org/abs/2609.11168)

**<font color=#1a73e8>作者：</font>** Xingchen Xiao, Feng Zhang, Wenjin Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor singular value decomposition (T-SVD), which is built upon the tensor-tensor product (t-product), has emerged as a powerful tool for processing high-dimensional visual data such as color images and videos. However, the standard t-product imposes strict dimensional compatibility constraints. Although extensions based on the semi-tensor product (STP) relax this restriction, their single-term formulations still suffer from limited approximation accuracy. Moreover, these deterministic methods incur high computational costs when processing large-scale tensor data. To address these issues, this paper introduces a novel semi-tensor product for third-order tensors under the t-product framework induced by arbitrary invertible linear transforms. The resulting tensor semi-tensor product breaks the rigid dimension matching requirement of the standard t-product, while retaining the closed-form property of T-SVD. Based on this construction, we develop a multi-term semi-tensor product singular value decomposition (MSTP-SVD), which integrates multiple orthogonal decomposition terms to significantly improve low-rank approximation accuracy compared with single-term schemes. To reduce the computational cost of multi-term modeling, we incorporate randomized projection and power iteration techniques into the MSTP-SVD framework, yielding an accelerated multi-term randomized semi-tensor product SVD (MRSTP-SVD) algorithm that achieves a balance between reconstruction accuracy and computational efficiency. Experiments on image and video compression and completion tasks demonstrate the effectiveness of the proposed method.

---


### 73. [Breaking Predictions Is Not Enough: Specified-Foil Counterfactuals for Temporal Graphs](https://arxiv.org/abs/2609.11170)

**<font color=#1a73e8>作者：</font>** Minwoo Yu, Young-guk Ha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal graph counterfactual explanations typically change past events to change or invalidate an original prediction, while leaving its replacement unspecified. Yet a user facing a predicted outcome often asks which past conditions would make a particular alternative occur instead. We formulate this destination-specific question as the Specified-Foil Counterfactual: given an original prediction A and a foil B fixed before search, find a low-cost past-event intervention under which the same predictor selects B as top-ranked. Our trace-guided intervention search contrasts the completed execution of A with a reconstructed incomplete execution of B, maps their difference to DELETE, INSERT, REWIRE, RELABEL, and SHIFT operations, and verifies B through exact replay. We instantiate this principle with LiFTER on continuous-time dynamic graphs and TLogic on temporal knowledge graphs. On CTDGs, the method retains 85.7-93.6% of black-box greedy successes while reducing predictor evaluations by 75.0-80.0%; on TKGs, it reaches the specified foil in 74.8% of 600 comparisons. Executable traces thereby become computational structures for constructing conditions of unselected alternatives, rather than records used only to explain predictions already made.

---


### 74. [Beyond Visual Quality: Evaluating Physical Consistency under Ego-Motion with EgoGenEval](https://arxiv.org/abs/2609.11172)

**<font color=#1a73e8>作者：</font>** Yilin Long, Chenming Zhu, Zitang Gou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent visual generators produce high-fidelity images yet often violate physical consistency under ego-motion, limiting their use for spatial reasoning and embodied planning. Existing benchmarks largely focus on isolated images or single-step quality, leaving this challenge underexplored. We introduce EgoGenEval, a geometry-grounded, pose-free benchmark designed to evaluate the physical consistency of visual generators under ego-motion, and organize our study into two parts. (1) EgoGenEval contains 1,400 cases and 2,360 target views spanning single-step and multi-step ego-motion. It separately measures Camera Motion Grounding (CMG) and Scene State Preservation (SSP), with both metrics validated against blinded human judgments. Evaluating 16 pose-free generators together with two pose-conditioned references reveals that current models struggle to execute camera motion while maintaining scene state, and that no system performs well on both axes at once. (2) To examine whether benchmark-derived data can improve these capabilities, we build EgoGen-Train from the same geometry-grounded pipeline and run controlled SFT studies. These show that pairwise supervision does not reliably improve camera-motion grounding and scene-state preservation together: even at the full training pool and the longest budget, scene preservation gains a fraction of what camera motion does. This points to the pairwise teacher-forced objective itself as the binding constraint, motivating a trajectory-centric paradigm that couples self-conditioned rollouts with explicit pose and visibility supervision.

---


### 75. [Hierarchical Clustering Can Jointly Satisfy Richness, Consistency, and Scale Invariance](https://arxiv.org/abs/2609.11173)

**<font color=#1a73e8>作者：</font>** Daichi Kuroda, Maximilien Dreveton, Matthias Grossglauser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite its ubiquity, clustering lacks a universally accepted definition of what is a cluster. Kleinberg's Impossibility Theorem formalizes this difficulty by showing that no flat clustering method can simultaneously satisfy three natural axioms: scale invariance, richness, and consistency. In this paper, we ask whether this impossibility persists when the output is a hierarchy rather than a single partition. We show that, in contrast to the flat clustering setting, the hierarchical analog of these axioms are jointly satisfiable. In fact, there exist uncountably many hierarchical clustering methods satisfying these axioms, which we call admissible. We explicitly construct several admissible methods, including methods based on well-separated clusters and a non-binary version of single linkage. For certain pairs of admissible methods, the hierarchy produced by one always refines that produced by the other. This refinement relation defines a partial order on the class of admissible methods. This partially ordered set has no greatest element and contains uncountably many pairwise incompatible maximal elements, revealing substantial diversity among admissible methods. Nevertheless, this diversity is constrained: every admissible method contains a hierarchy of sufficiently well-separated clusters, and every finite collection of admissible methods shares such a nontrivial common backbone.

---


### 76. [Debate-to-Skill: Capability-Bound Process Supervision for Industrial Query-to-Agent Annotation](https://arxiv.org/abs/2609.11176)

**<font color=#1a73e8>作者：</font>** Shiyu Zhang, Leisheng Cheng, Huifu Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial query-to-agent matching fails when topical relevance is mistaken for executable capability, especially on long-tail and boundary-sensitive requests. We formulate annotation as \emph{capability-bound process supervision} and instantiate it with Debate-to-Skill, which uses reusable decision principles, structured deliberation, verifier-based verdict extraction, and disagreement-driven refinement. On an industrial Query2Agent benchmark, we compare Debate-to-Skill with direct-label supervision, reasoning-SFT, and structural ablations. The results test whether gains come from supervising the capability-critical decision process itself, especially on grey-zone cases where semantic relatedness and executable capability diverge.

---


### 77. [A Multi-View and Confusion-Guided Ensemble Framework for Robust Synthetic Image Attribution](https://arxiv.org/abs/2609.11188)

**<font color=#1a73e8>作者：</font>** Zuomin Qu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic image attribution (SIA) has become increasingly important with the rapid advancement of text-to-image generation models. However, accurately identifying the source model of a generated image remains challenging due to the growing similarity among modern diffusion-based generators and the presence of diverse post-processing operations. In this report, we present a multi-view and confusion-guided ensemble framework for the Synthetic Image Attribution Challenge of the DLMMDD Workshop at ICANN 2026. Our approach integrates multiple complementary architectures, including FFT-ConvNeXt, DINOv2, CLIP, and Xception, to capture diverse attribution cues from frequency, semantic, and forensic perspectives. To improve robustness against unknown degradations and image manipulations, extensive data augmentation strategies are employed during training, simulating realistic post-processing operations such as compression, resizing, grayscale conversion, and blur. Furthermore, we analyze the confusion patterns of the ensemble model and observe severe ambiguity between Stable Diffusion 3 and Stable Diffusion 3.5. To address this issue, we introduce a dedicated binary expert classifier that is selectively activated under low-confidence conditions. We additionally apply class-adaptive confidence calibration to improve the discrimination of challenging classes such as Tencent Hunyuan. The proposed framework achieved 99.53% on the public leaderboard and 99.20% on the private leaderboard. The source code and implementation details are publicly available at this https URL.

---


### 78. [Conceptualising an Initial Design Space for Guidance in Digital Physical Activity Support](https://arxiv.org/abs/2609.11193)

**<font color=#1a73e8>作者：</font>** Faith Young, Markus Tatzgern, Alexander Meschtscherjakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Providing guidance is frequently referenced as a key capability of digital health interventions targeting physical activity, yet the term remains poorly defined and inconsistently applied. Existing work often conflates guidance with related constructs such as personalisation, feedback, or persuasion, limiting both theoretical clarity and design progress. This paper conceptualises an initial design space of guidance in the context of digital physical activity support. We define guidance for physical activity as situated, action-oriented support that scaffolds users' embodied engagement in physical activity. Drawing on literature from behaviour change, human-computer interaction, embodied cognition, and digital health, we outline a design space that characterises guidance along multiple dimensions: scope, purpose, timing, context, modality, embodiment, adaptivity, autonomy, and affective quality. By offering a structured vocabulary and conceptual foundation, this work aims to support more coherent research, comparisons, and responsible design of digital health interventions featuring guidance for physical activity support.

---


### 79. [CEM-TUDASR: Computationally efficient multi-modality transformer based unsupervised domain adaptive super-resolution approach](https://arxiv.org/abs/2609.11201)

**<font color=#1a73e8>作者：</font>** Anjali Sarvaiya, Jay Kadel, Kishor Upla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wireless Capsule Endoscopy (WCE) enables non-invasive visualization of the gastrointestinal tract, but its miniaturized optics, sensor limitations, and wireless transmission constraints result in low-resolution images with reduced visibility of diagnostically important structures. This paper proposes CEM-TUDASR, a computationally efficient unsupervised Transformer-based super-resolution framework for WCE image enhancement without paired low-resolution (LR) and high-resolution (HR) training data. A domain-adaptive degradation network synthesizes realistic WCE-like LR images from HR conventional endoscopy images, reducing the domain gap and enabling effective unpaired learning. The SR generator integrates Deep Attention Blocks (DABs) and a Fusion Attention Block (FAB) to capture long-range contextual dependencies and fine local structures while preserving perceptual and structural fidelity. The model is trained on a curated dataset derived from Kvasir Capsule and evaluated on KID and GIANA for cross-dataset generalization. No-reference quality metrics, including BRISQUE, PIQE, NIQE, and the domain-specific EndoQM, show that CEM-TUDASR consistently outperforms existing unsupervised SR methods. Qualitative results further demonstrate improved restoration of mucosal textures, vascular patterns, and clinically relevant anatomical details. Cross-domain experiments on retinal images additionally demonstrate the adaptability of the framework. With only 2.67 million parameters and 169.94 GFLOPs, CEM-TUDASR achieves high-quality reconstruction while maintaining computational efficiency, making it suitable for resource-constrained clinical and embedded endoscopic applications.

---


### 80. [Automated Identification of Competing Narratives in Political Discourse on Social Media](https://arxiv.org/abs/2609.11202)

**<font color=#1a73e8>作者：</font>** Sergej Wildemann, Erick Elejalde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media platforms have become central to shaping political discourse, serving as arenas where narratives form and evolve, influencing public opinion. Identifying and analyzing these narratives, particularly when they compete across different political ideologies, is crucial for understanding the dynamics of modern political communication. This paper presents an unsupervised framework for identifying and characterizing competing narratives in political discourse on social media, focusing on German politicians' tweets. The framework employs a multi-stage pipeline that integrates natural language processing techniques such as topic modeling, event detection, and event linking. By forming data into coherent stories and uncovering the distinct perspectives of user communities, the system is able to detect the key competing narratives, highlighting the divergent framings and conflicts surrounding trending political topics. Two case studies on polarizing political issues demonstrate the efficacy of the methodology, showcasing its ability to uncover and analyze divergent viewpoints. The findings contribute to the broader understanding of how narratives propagate within the digital public sphere and offer insights for policymakers, social media platforms, and researchers interested in monitoring political discourse.

---


### 81. [CryptoL: Towards Scale Dominance and Physics Constraints Mitigation in Financial Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.11206)

**<font color=#1a73e8>作者：</font>** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency forecasting presents a distinctive combination of extreme cross-asset scale heterogeneity, non-stationary dynamics, and structural dependencies among Open, High, Low, and Close (OHLC) variables. We present CryptoL, a unified framework designed to address these challenges within multivariate time-series forecasting. CryptoL evaluates forecasting error in context-normalized coordinates within the RevIN pipeline, preventing inverse normalization from introducing an additional squared-scale weighting into the MSE objective. We formally characterize this effect through the empirical risk and parameter-gradient geometry, establishing the conditions under which large-scale assets can disproportionately influence shared-model optimization. Beyond loss-space normalization, CryptoL examines channel-independent and channel-dependent normalization for OHLC data, showing that a shared channel-dependent affine transformation preserves candle-order relations that independent channel transformations need not preserve. The framework further incorporates scale-adaptive numerical stabilization to reduce distortions caused by a fixed normalization constant across assets spanning many orders of magnitude, together with a soft feasibility loss that penalizes violations of the defining OHLC inequalities. Experiments across heterogeneous cryptocurrency assets evaluate these components through controlled ablations and demonstrate improvements in forecasting accuracy, training stability, and the frequency of financially valid OHLC predictions relative to the considered baselines. CryptoL therefore provides an integrated approach to scale-balanced optimization, structure-preserving normalization, numerical stabilization, and constraint-aware cryptocurrency forecasting.

---


### 82. [Convex Optimization with Nested Evolving Feasible Sets (CONES) under Time-Varying Loss Functions](https://arxiv.org/abs/2609.11207)

**<font color=#1a73e8>作者：</font>** Rahul Vaze  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convex Optimization with Nested Evolving Feasible Sets (CONES)} was introduced in \cite{CONESVaze} where the objective function \(f\) remains fixed but the feasible region evolves over time as a nested sequence \(S_1 \supseteq S_2 \supseteq \cdots \supseteq S_T\). The goal of an online algorithm is to simultaneously minimize the regret with respect to hindsight static optimal benchmark and the total movement cost $M_\cA(T)$ while ensuring feasibility at all times. CONES is an optimization-oriented generalization of the well-known \emph{nested convex body chasing} (NCBC). In this paper, we extend CONES to allow for loss functions $f_t'$s to also change over time. When all loss functions are convex, we show that the projected proximal algorithm achieves $O(T^{1-\beta}), O(T^\beta)$ simultaneous regret and movement cost, respectively, for any $\beta \in [0,1)$, over a time horizon of $T$. We also show that any {\it weakly adaptive} online algorithm with $O(T^\beta)$ regret has a movement cost of $\Omega\left(T^{\frac{1-\beta}{2}}\right)$ for any $\beta \in [0,1)$. When all loss functions are strongly convex, we show that the projected proximal algorithm simultaneously achieves $O(1)$ regret and a movement cost of $O(\log T)$. To complement this, we show that any online algorithm with sublinear {\it anytime} regret has a movement cost of $\Omega\left(\log T\right)$.

---


### 83. [You Get What You Sample: Evaluating Sampling Strategies for Web Security Measurements](https://arxiv.org/abs/2609.11218)

**<font color=#1a73e8>作者：</font>** Xuenan Zhang, Yuqing Yang, Giancarlo Pellegrino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web measurement studies rely on domain datasets such as Tranco to quantify the prevalence and impact of security issues at scale, but exhaustively analyzing these datasets is often infeasible because of the cost of advanced analysis techniques, requiring the use of sampling. Despite its widespread use, sampling remains largely guided by convention---most commonly \emph{Top $N$} domain selection---rather than evidence, and its influence on the validity and generalizability of security findings has received little systematic evaluation. Consequently, it remains unclear whether common sampling strategies introduce systematic bias, distort observed vulnerability rates, or limit comparability across studies.
In this work, we undertake, to the best of our knowledge, the first comprehensive investigation into how sampling methodologies affect the measurements and the conclusions. Through a comprehensive literature review and large-scale measurements of 500k Tranco and 24.8M Common Crawl hosts, we perform a comparative evaluation of datasets and sampling strategies. We show that, while Top $N$ sampling may be a rational strategy, the researchers have to bear in mind that Top $N$ does not reflect the overall distribution of the web. Instead, probability-based strategies yield stable, unbiased estimates for prevalence and many impact objectives. Hybrid sampling provides no advantages over pure probability sampling, as its deterministic prefix consistently contributes negatively to accuracy. Building on these results, we provide data-backed guidance for future studies, proposing to use an adaptive probability-based sampling strategy that remains effective even when the prevalence of the target issue is unknown.

---


### 84. [Tri-DehazeGS: Scene--Medium Decoupled Gaussian Splatting with Transmittance-Aware Optimization](https://arxiv.org/abs/2609.11223)

**<font color=#1a73e8>作者：</font>** Kui Jiang, Yang Gu, Jiacheng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering clean 3D scenes from hazy multi-view images is challenging because haze attenuates scene radiance and introduces atmospheric scattering. Recent scattering-aware Gaussian Splatting methods introduce physical haze models into reconstruction, but they often apply degradation in image space or bind medium-related variables to Gaussian primitives, which can entangle clean scene radiance with atmospheric effects. Moreover, low-transmittance regions provide weakened supervision for Gaussian optimization, causing distant or dense-haze areas to be under-reconstructed. We argue that clean reconstruction under haze requires both scene--medium disentanglement and transmittance-aware optimization rebalancing. To this end, we propose Tri-DehazeGS, a scene--medium decoupled Gaussian Splatting framework. It represents the clean scene with Gaussian primitives, models the participating medium using an independent view-shared tri-plane field, and composes hazy observations through a physical scattering model. We further introduce Medium-Decoupled Transmittance Gradient Compensation (MD-TGC), which compensates haze-suppressed gradients after medium freezing without altering forward rendering. Experiments on real and synthetic haze benchmarks show that Tri-DehazeGS improves clean novel-view reconstruction. Code is available at this https URL.

---


### 85. [Polyhedral Geometry of Time-to-First-Spike Neural Networks](https://arxiv.org/abs/2609.11227)

**<font color=#1a73e8>作者：</font>** Manjot Singh, Guido Montúfar, Gitta Kutyniok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the expressivity of spiking neural networks, which provide a natural framework for asynchronous, event-driven computation complementary to conventional feedforward neural networks. We consider the time-to-first-spike model in a setting for which the input-output map is continuous and piecewise linear, with affine pieces governed by causal feasibility constraints that determine which presynaptic spikes occur before a neuron fires. We first show that each neuron's firing time admits a maxout-like representation with exponentially many, highly constrained affine pieces. We then formalize causal regions as polyhedral regions with fixed causal sets and derive upper and lower bounds on the maximal number of causal regions in both shallow and multilayer feedforward spiking networks. Our theoretical and experimental results show that spiking networks can generate richer partitions of the input space than conventional feedforward ReLU networks.

---


### 86. [Solving Few-Shot Multiobjective Multitask Optimization via Iterative Sequential Transfer](https://arxiv.org/abs/2609.11228)

**<font color=#1a73e8>作者：</font>** Tingyang Wei, Haofeng Wu, Ananda Phan Iman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Applying knowledge transfer across multiple optimization tasks, multitask optimization (MTO) emerges as a promising approach to solving synergistic optimization tasks simultaneously. However, the development of effective knowledge transfer mechanisms in MTO fundamentally relies on aligning elite solution distributions across tasks. This dependency creates a critical bottleneck in few-shot optimization regimes, as restricted evaluation budgets impede the identification of elite solution distributions required for beneficial transfer. This challenge is exacerbated in multiobjective multitask problems, where each optimizer must approximate a continuous Pareto manifold rather than a single optimal point. This paper introduces Iterative Sequential Transfer (IST) to circumvent this bottleneck. We model MTO as a sequence of sequential transfer optimization problems, concentrating evaluations on a single target per iteration. We propose a likelihood-informed task prioritization mechanism to maximize transfer utility by identifying the task most likely ready for knowledge integration. Empirical results on benchmark and real-world problems verify the effectiveness of the proposed method under tight budgets.

---


### 87. [When is Test-Time Adaptation Identifiable From Unlabeled Evidence?](https://arxiv.org/abs/2609.11235)

**<font color=#1a73e8>作者：</font>** Kartik Jhawar, Lipo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) offers many ways to update a deployed model without labels, but choosing the wrong update can make a strong source model worse. Recent methods therefore try to predict which adaptation will work from unlabeled test data. We ask a prior question: does the evidence given to the selector contain enough information to determine the best action at all? We show that this is not guaranteed, even with a perfect selector. If an observation channel makes two deployments look the same while their TTA rankings differ, reliable selection is impossible from that channel; richer evidence can restore the decision only when it resolves the relevant ambiguity. We make this boundary exact in a finite-batch Gaussian TTA model, where doing nothing beats mean recentering for small shifts, recentering wins beyond a unique critical shift, and the boundary shrinks as $1/\sqrt n$. Public benchmark studies on CIFAR-100-C and DomainNet-126 show the same failure mode with modern TTA methods: changing only deployment structure can reverse the oracle action while global order-blind evidence remains unchanged. The result is a practical way to separate two failure modes that are usually mixed together: a weak selector versus an information channel that cannot support the desired decision in the first place.

---


### 88. [SCINTILLA-SNN: A Spiking Multi-Scale Selective Aggregation Network for Perineural Invasion Prediction](https://arxiv.org/abs/2609.11237)

**<font color=#1a73e8>作者：</font>** Youngung Han, Yului Jeong, Kyeonghun Kim 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preoperative prediction of perineural invasion (PNI) in cholangiocarcinoma (CCA) is clinically valuable but remains challenging because PNI-related cues on magnetic resonance imaging (MRI) are subtle, sparse, and spatially localized around the tumor boundary. Standard 3D CNN and transformer architectures process volumetric data in a dense or spatially uniform manner, which can dilute subtle PNI-related evidence while requiring a large number of multiply-accumulate operations over 3D feature grids. To address these limitations, we propose SCINTILLA-SNN, a 3D spiking network composed of a four-stage hierarchical backbone and a Multi-Scale Spike Aggregation (MSSA) module for PNI prediction. The backbone extracts hierarchical volumetric representations through spiking convolutional stages and local spike window modulation stages. Given the resulting stage-wise representations, MSSA maps each spatial token to a learnable content value and modulates it with a spike-dynamics gate derived from firing rate and timestep-wise membrane-potential variability. The resulting score, referred to as the diagnostic token score, is used to selectively aggregate sparse PNI-related evidence. Experiments on a 10-year retrospective cohort of 182 CCA patients show that SCINTILLA-SNN achieves an AUROC of 0.748 under 5-fold cross-validation, while reducing the estimated inference energy by 23.18$\times$ compared with dense MAC-only computation of the same network.

---


### 89. [Fast and Accurate Monomodal 3D High Resolution Deep Registration of Drosophila Larval Brain Volumes](https://arxiv.org/abs/2609.11240)

**<font color=#1a73e8>作者：</font>** Daniel Reisenbüchler, Yousef Sadegheih, Michael Dittrich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The larval stage of Drosophila melanogaster is a compact model system for neuroscience whose genetic toolkit allows fluorescent markers to be expressed in defined neural populations, and comparing the resulting expression patterns across animals requires every brain to be registered into a shared anatomical reference space. Existing pipelines for this task are predominantly based on classical registration methods, which perform a new optimization for each volume, often require per-case parameter tuning, and can take minutes per brain, limiting their use as a routine preprocessing step. We present a trained deep registration pipeline that deformably aligns a larval brain to a reference template in a single forward pass at high spatial resolution, on volumes that hold several times more voxels than those learned 3D registration is normally reported on, together with the preprocessing and anatomy-anchored evaluation pipeline required to apply it. Against eleven classical and seven further learned baselines on a held-out collection acquired with different acquisition and quality strata, the proposed pipeline is the most accurate, improving on the strongest classical baseline by 23 percentage points of anatomical landmark-local mutual information. It registers a volume one to two orders of magnitude faster than the classical deformable pipelines, and it retains more of its accuracy than any other method as acquisition quality degrades. The network, its trained weights and the full pipeline are released as the open-source deep larval brain registration framework: this https URL

---


### 90. [Sci-MMR: Benchmarking Multi-Step Evidence-Grounded Scientific Reasoning in Multimodal Agents](https://arxiv.org/abs/2609.11243)

**<font color=#1a73e8>作者：</font>** Jiaqiang Li, Yajie Yang, Zhiheng Xi 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents are increasingly expected to search the literature, analyze experimental evidence, and generate scientific hypotheses. These capabilities require multi-step evidence grounded reasoning that progressively acquires, integrates, and verifies evidence before reaching a conclusion. Existing multimodal benchmarks, however, largely evaluate final-answer accuracy, leaving open whether predictions are actually supported by traceable scientific evidence. We introduce Sci-MMR, a benchmark for multi-step evidence-grounded scientific reasoning built on structured argument graphs linking scientific claims, citation-grounded knowledge, visual evidence, and supporting regions. Sci-MMR comprises 235 multi-hop reasoning tasks spanning four scientific disciplines, with an average of nine figure panels per task. Evaluating eight frontier multimodal models, we find that answer accuracy consistently exceeds complete-evidence recovery rate by more than 20%, revealing a substantial gap that answer-only evaluation is structurally unable to capture. Through controlled interventions, we identify two fundamental bottlenecks. First, evidence acquisition: models struggle to extract complete structured evidence from scientific figures, accounting for 57.2% of failures. While cropping tools yield modest gains (+4.5 points), providing gold evidence improves accuracy by up to 37.0 points, indicating difficulty in assembling complete multi-region evidence. Second, evidence integration: models struggle to translate available evidence into correct conclusions, accounting for 31.8% of failures, while even with gold evidence the strongest model achieves only 69.1% accuracy on the hardest tasks. These findings indicate that current answer-centric benchmarks substantially overestimate the evidence-grounded reasoning capabilities of multimodal research agents

---


### 91. [Assessing the Reusability of Public Speech Resources for Low-Resource Languages: A Central Kurdish Case Study](https://arxiv.org/abs/2609.11246)

**<font color=#1a73e8>作者：</font>** Hiwa Asadpour  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Kurdish is spoken by millions of people, but little technology can read it aloud. A recent study released three Kurdish voices, 35 hours of recorded speech, and a paper describing the work, all free to download. This review checks how well those public files match the paper. The research is careful about its limits, but the files contain several problems: a settings file lists equipment that was never used, test recordings are left unlabeled among training data, and a coding fault mishandles long numbers. The download page also claims a stronger result than the paper reports and recommends one voice for general use. That recommendation matters because Kurdish has major regional and written variation, while these voices were built from three people reading prepared texts. The process therefore removes much everyday and regional speech. English and German benefit from long traditions of dictionaries and linguistic description that help identify wrong pronunciations; Kurdish has far less such support, so software choices can go unchecked. The voices sound fluent, but they represent the reading styles of their speakers rather than Kurdish as a whole. Most of these issues can be fixed using information the team already has, without changing the reported results. Better records would mainly make the work easier for others, especially community linguists, to check and reuse. The license is the main exception: whether audiobook owners allow corrected versions to be shared will affect whether future Kurdish voices can build on this work or must start again.

---


### 92. [The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods](https://arxiv.org/abs/2609.11247)

**<font color=#1a73e8>作者：</font>** Ioanna Kaffeza, Efthymios Georgiou, Alexandros Potamianos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Sentiment Analysis (MSA) remains constrained by modality imbalance, yet the field continues to rely on optimization-based balancing methods that promise more than they deliver. We provide three contributions: 1) a unified evaluation framework testing gradient and loss-based balancing strategies under controlled settings; 2) a theoretical diagnosis explaining why these methods fail, as they conflate fitting speed with discriminative contribution; and 3) a research agenda toward held-out discriminative modality valuation. Experiments on CMU-MOSI and CMU-MOSEI reveal three shortcomings: no strategy reliably outperforms Late Concatenation; performance is sensitive to hyperparameters; and even ratio calibration fails to yield consistent gains. The core issue is fundamental: loss is not utility, and gradients are not importance. Modality imbalance remains unresolved, motivating utility estimation from held-out performance.

---


### 93. [You've Got a BUD in Me: Authenticated Reads from Per-Block Write Logs](https://arxiv.org/abs/2609.11251)

**<font color=#1a73e8>作者：</font>** Alejandro Ranchal-Pedrosa, Cody Littley, Ben Marsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains usually pay for authenticated reads by maintaining a structure that spans the entire state. We show how validators can support historical membership and exclusion proofs by authenticating each block's writes instead. A Block Update Digest (BUD) commits a write log whose predecessor pointers link successive modifications of each key. A SuperBUD summarizes last writes over a window; an exponential hierarchy turns long unchanged intervals into short proofs. The digest count is logarithmic in the gap within the hierarchy's range, with one additional digest per top-level window beyond it. We prove soundness against adversarial provers and up to f Byzantine validators, and completeness for queries anchored by a post-deployment modification, assuming archive, attestation, and committee evidence is available. Across a 50x increase in state size, the measured base-BUD path rises by 1.24x, compared with 3.1x and 69.5x for in-memory and cache-bounded disk-backed Merkle Patricia tries. On the synthetic trace, two-digest read-layer payloads stay below 800 bytes, and warm hash-path verification takes at most 146 microseconds at p99.

---


### 94. [AI-Powered Flare Combustion Efficiency Estimation](https://arxiv.org/abs/2609.11262)

**<font color=#1a73e8>作者：</font>** Afeefa Azam, Iyyakutti Iyappan Ganapathi, Fares Ossama Abdelhafez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving high combustion efficiency in flare stacks is crucial for adhering to regulatory standards and controlling the release of hydrocarbons into the environment. Traditional instruments like gas analyzers and hyperspectral cameras are expensive, fragile, and require frequent calibration, which makes them impractical for remote or budget constrained industrial sites. We propose an innovative solution that combines a lightweight vision-language encoder with a compact multi-layer perceptron to predict combustion efficiency directly from low-cost thermal video footage. The fully trained model is integrated into an easy-to-deploy graphical user interface. This interface overlays predicted combustion efficiency values on each video frame, displays real-time trends in combustion efficiency, shows the distribution of combustion efficiency across all frames in the video, and allows users to export CSV reports. Over a six-month period, the system achieved 99% uptime and required less than 15 minutes of maintenance per week.

---


### 95. [Uncertainty DMD: Restoring Diversity in Few-Step Autoregressive Video Distillation](https://arxiv.org/abs/2609.11265)

**<font color=#1a73e8>作者：</font>** Zixuan Duan, Xunzhi Xiang, Yabo Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation improves the efficiency of autoregressive (AR) video generation, but often causes diversity collapse: under the same prompt, different noise samples tend to produce highly similar videos with weakened motion dynamics. We analyze this degradation in Distribution Matching Distillation (DMD)-distilled AR video generators and find that, in the autoregressive setting, it takes the form of a structured uncertainty collapse: the mode-seeking bias of DMD maps different noise samples to nearly identical first chunks, and the deterministic AR cache then propagates this collapsed state to all subsequent chunks, turning a local loss of stochasticity at the rollout root into a global suppression of temporal variation. Based on this analysis, we propose Uncertainty DMD, a simple uncertainty-injection framework that restores stochasticity at two key stages of AR generation: a timestep perturbation for the first chunk to increase first-chunk diversity, and a stochastic cache-writing mechanism for later chunks to preserve uncertainty in autoregressive conditioning. The method requires no architectural changes and introduces only lightweight perturbation operations. The same perturbation mechanisms are used during both training and inference. Experiments show that Uncertainty DMD consistently improves diversity and motion dynamics while maintaining comparable per-sample visual quality.

---


### 96. [Improving Faint Object Detection for Space Situational Awareness with Variational Autoencoders](https://arxiv.org/abs/2609.11269)

**<font color=#1a73e8>作者：</font>** Angela Cratere, Luca Ghilardi, Vishnu Reddy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a deep-learning pipeline for enhancing the detection of faint moving objects in optical space situational awareness (SSA) imagery through automated star removal and background reconstruction. Detecting low signal-to-noise ratio (SNR) objects remains extremely challenging in optical observations, particularly in the cislunar (X-GEO) environment, where structured sky backgrounds, dense stellar fields, and scattered moonlight significantly degrade the performance of classical detection algorithms. To address this problem, the proposed pipeline combines a lightweight segmentation network (Tiny-U-Net) to generate stellar masks with a partial-convolution variational autoencoder (astro-VAE), designed to learn the statistical distribution of astronomical backgrounds and perform context-aware inpainting of masked regions. The reconstructed background maps can then be used as a preprocessing step to suppress fixed sources and background inhomogeneities prior to detection. As a proof of concept, the approach is integrated with a shift-and-stack scheme and evaluated on real ground-based telescope observations targeting the X-GEO region. Results demonstrate that the method reconstructs star-free backgrounds with high fidelity, while preserving moving targets and significantly enhancing detectability, thereby providing an effective data-driven preprocessing strategy for faint moving-object detection in optical SSA scenarios.

---


### 97. [Order-Aware 2.5D Multiple Instance Learning for Preoperative MRI-Based Perineural Invasion Risk Assessment in Intrahepatic Cholangiocarcinoma](https://arxiv.org/abs/2609.11271)

**<font color=#1a73e8>作者：</font>** Hyunsu Go, Youngung Han, Kyeonghun Kim 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is an adverse histopathologic marker in intrahepatic cholangiocarcinoma (ICC), but it is usually confirmed only after resection. Preoperative T2-weighted MRI may provide noninvasive imaging cues predictive of PNI, although labels are available only at the patient level without slice- or voxel-level annotations. We propose Order-Aware Slab Multiple Instance Learning (OAS-MIL), a weakly supervised framework for patient-level PNI prediction. Each tumor-centered MRI crop is represented as an ordered sequence of overlapping 2.5D slabs formed from contiguous axial slices. A shared encoder extracts slab-level features, which are aggregated by a permutation-invariant set-attention branch and a bidirectional sequence-attention branch. Using five-fold label-stratified cross-validation at the patient level, OAS-MIL achieved a mean AUROC of 0.770, outperforming the evaluated volumetric and MIL baselines. These results suggest that axial order provides a useful inductive bias for weakly supervised PNI prediction from MRI.

---


### 98. [Few-Shot Learning for Network Intrusion Detection: Methods, Datasets, and Performance](https://arxiv.org/abs/2609.11275)

**<font color=#1a73e8>作者：</font>** Arne Roszeitis, Victor Jüttner, Erik Buchmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anomaly-based network intrusion detection systems (NIDS) are an important first line of defense. However, training NIDS for new attack types is challenging, because labeled attack data are rarely available. Few-shot learning (FSL) addresses this problem by learning from few samples. However, the approaches and evaluation settings, that have been investigated so far, vary widely. This work systematically reviews FSL approaches for NIDS published from 2022 to 2026. We conduct a systematic literature review with PRISMA 2020-like reporting to search ACM Digital Library, IEEE Xplore, and Scopus. From a set of 1,358 initial records, we retain 21 studies after screening, deduplication, and quality filtering. We classify the applied FSL approaches, datasets, and experimental parameters and compare reported performance. Meta-learning and convolutional neural networks are the most common approaches, with 8 and 10 studies, respectively. Most studies evaluate five or fewer samples per class, although settings vary. CIC-IDS2017 and CSE-CIC-IDS2018 are the most frequently used datasets. Missing parameters and source code limit reproducibility and direct comparison between approaches.

---


### 99. [Predicting Train Delays in Finland Using Machine Learning and Weather Data](https://arxiv.org/abs/2609.11277)

**<font color=#1a73e8>作者：</font>** Vinicius Pozzobon Borin, Jean Michel de Souza Sant'Ana, Nurul Huda Mahmood  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable railway operations depend increasingly on real-time environmental intelligence delivered through wireless sensor infrastructures, a capability that 6G networks will substantially enhance through integrated sensing and edge computing. Adverse weather, particularly in Arctic regions with extreme temperatures and heavy precipitation, remains a leading cause of train delays, yet most prediction approaches rely on raw meteorological inputs without exploiting domain-informed feature engineering. This paper investigates machine learning for train delay prediction using the Finland Integrated Train-Weather (FI-TW) dataset, which fuses railway operational records with observations from the Finnish Meteorological Institute's nationwide sensor network of approximately 200 stations communicating over wireless links. We evaluate three feature configurations using XGBoost at Oulu central station (101,146 observations): full weather features, instant weather observations only, and derived weather category scenarios. The category-based approach, employing hierarchical classifications such as Blizzard, Heavy Snow, and Extreme Cold, achieved an R^2 of 0.78, root mean squared error of 8.5 minutes, and mean absolute error of 3.7 minutes, representing an 11% R^2 improvement and 10% error reduction over alternative configurations. These results demonstrate that compact, domain-informed features derived from sensor streams outperform raw meteorological observations, offering bandwidth-efficient representations suitable for edge deployment over current and emerging wireless infrastructures.

---


### 100. [SAMV-DUSt3R: Instance-Centric 3D Scene Decoupling from Sparse Multi-Views](https://arxiv.org/abs/2609.11279)

**<font color=#1a73e8>作者：</font>** Langxu Zhao, Zuan Gu, Yingdan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rising demand to decouple objects from 3D scenes, we propose SAMV-DUSt3R, an end-to-end model that injects SAM2 2D masks into MV-DUSt3R reconstruction. A Cross Flow Mask Block uses these masks to steer the network toward the target instance, jointly improving shape accuracy and achieving object-level disentanglement without multi-stage pipelines. To ensure reconstruction stability, a lightweight Spatial RankGNN selects the optimal reference view with a selection accuracy of 73.5\%. Extensive experiments demonstrate that our method boosts average reconstruction precision by 11\% across various metrics compared to state-of-the-art baselines. These results reveal a strong instance-disentanglement capability and clear benefits for driving, robotics, AR/VR, and heritage digitisation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
