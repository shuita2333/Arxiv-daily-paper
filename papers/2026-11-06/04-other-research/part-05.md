# 📦 其他研究 | 2026年11月06日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

---

### 201. [Fingerprinting the Dispatchers behind Distributed Model Extraction](https://arxiv.org/abs/2611.06661)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> API distillation campaigns try to hide model-stealing traffic by splitting requests across thousands of load-balanced accounts, which standard content classifiers often miss. However, request timestamps, specifically arrival time and stream completion time, reveal the underlying dispatching strategy, such as round-robin counters or key-shuffling pools. Using a 20 percent seed set, this timing analysis can forensically rank the remaining accounts of a campaign with 0.92 to 1.00 AUC within 20 minutes, even across thousands of real production accounts. While adaptive attackers struggle to hide rotating dispatchers using jitter, pinning keys successfully evades detection, though it can severely throttle throughput when quotas bind. Ultimately, timing exposes shared infrastructure patterns even when content filters fail.

---


### 202. [Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification](https://arxiv.org/abs/2611.06662)

**<font color=#1a73e8>作者：</font>** Hyeseo Jeon, Seonho Yoo, Jay-Yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search-augmented reasoning systems can reach correct answers while making errors in intermediate steps. Reliable auditing must check whether evidence $D$ covers the question $Q$, reasoning $T$ addresses $Q$, and $T$ is grounded in $D$. We introduce GraphRail, which represents requirements, evidence, and reasoning as structured claims and compares them without a generative judge or gold answer. Across three multi-hop QA benchmarks and three reasoning frameworks, GraphRail improves error recall over generative verifiers while remaining stable under stochastic extraction. Its diagnoses can also guide online reasoning, providing a traceable way to detect and correct intermediate errors.

---


### 203. [CardioDrift: Automatic Cardiac Motion Tracking on a 3D Atlas Mesh via Shape-aware Coherent Point Drift with Slice Shift Correction](https://arxiv.org/abs/2611.06664)

**<font color=#1a73e8>作者：</font>** Reza Akbari Movahed, Abuzar Rezaee, Shatha Alamri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic cardiac motion tracking from cine cardiac magnetic resonance (CMR) imaging is essential for quantifying myocardial motion abnormalities associated with cardiovascular disease. Existing methods fall into two groups: those that represent motion without anatomical correspondence across subjects and therefore limit inter-subject motion assessment; and those that represent motion with globally corresponding points, which typically require a time-consuming and error-prone semi-automatic step to fit a cardiac atlas to the subject space. To address these limitations, this study proposes CardioDrift, a fully automatic, atlas-based probabilistic framework that represents subject-specific cardiac motion on a 3D atlas mesh with globally corresponding points. The Coherent Point Drift (CPD) formulation is generalised to jointly register the atlas surfaces of multiple cardiac regions to the anatomically corresponding contours extracted from cine CMR segmentation maps throughout the cardiac cycle. Slice-shift correction is embedded in the same probabilistic model, estimating slice-wise translations that suppress the misalignment artefact limiting atlas-fitting accuracy. Evaluation on 1301 randomly selected UK Biobank subjects and the M&M dataset, CardioDrift attains Dice similarity coefficients (DSCs) of $92.23\pm8.70\%$, $82.11\pm7.56\%$, and $88.69\pm4.13\%$ for the left ventricle (LV), myocardium (Myo), and right ventricle (RV), exceeding the strongest baseline on every distance and overlap metric of both datasets.

---


### 204. [Self-Directed Apple Tasting](https://arxiv.org/abs/2611.06677)

**<font color=#1a73e8>作者：</font>** Tanmay Devale, Reed Phillips, Arvind Ramaswami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the classical apple-tasting setting, a partial feedback model in which the learner observes the true label only when it predicts $1$. A combinatorial characterization for the rates of this problem in the online adversarial setting has been studied by Raman et al. (2024). We study the self-directed setting, in which the learner can adaptively choose the order of the points it predicts on. In the realizable setting, we establish a tetrachotomy on the expected minimax number of mistakes made by any learner. Depending on the VC dimension, the $\emptyset$-centered star number, and the self-directed dimension, we show that the rates could possibly be $\Theta(1)$, $O(\log n) \cap \omega(1)$, $\tilde \Theta(\sqrt{n})$, or $\Theta(n)$. In the agnostic setting, the minimax regret is $\tilde \Theta(\sqrt{n})$ or $\Theta(n)$, depending on the VC dimension.

---


### 205. [Do unlearning algorithms learn the right features?](https://arxiv.org/abs/2611.06681)

**<font color=#1a73e8>作者：</font>** Polina Dolgova, Amartya Sanyal, Sebastian U. Stich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is commonly evaluated with standard post-deletion metrics that compare an unlearned model to one retrained on the remaining data. Such snapshot evaluations can conceal consequential differences in the features the two models encode. We prove that if an unlearned and a retrained model agree on their outputs but encode different features, a single gradient step on their prediction heads can break this agreement. We further show that deleting an arbitrarily small fraction of the data can cause retraining to select qualitatively different features, so matching retraining can require learning features that the full model never had. We then introduce a measure of feature recovery that separates missing from extraneous features. Across eight unlearning methods, models that perform well on standard metrics often fail to recover the retrained features. This mismatch predicts deviations from retraining under subsequent relearning and downstream adaptation, and directly correcting it systematically reduces these deviations.

---


### 206. [Sekai: Incremental Event Memory for Generalized Reasoning Video Segmentation](https://arxiv.org/abs/2611.06685)

**<font color=#1a73e8>作者：</font>** Zhengtao Liu, Jinrong Xu, Shiu-Hong Kao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online reasoning video segmentation (Online RVS) requires a model to segment query-referred objects as a video streams in, using only the frames observed so far. Existing formulations largely assume a fixed target set throughout the video, overlooking a fundamental property of streaming reasoning: as new events occur, the objects that satisfy a query may change over time. To address this, we propose a new task, Generalized Reasoning Video Segmentation (GRVS), where the target set depends on query-relevant events accumulated over the observed video history. As new evidence accumulates, the target set can evolve from empty to one or multiple objects, requiring a model to continuously maintain target validity while localizing the valid objects currently in view. To evaluate GRVS, we build Isekai, a diagnostic benchmark of 60 videos and 197 queries across 11 temporal query families, with 12,569 scoring points whose target sets are causally annotated over time. We further propose Sekai, an online framework with two complementary components: an Event Memory Reasoner (EMR) that maintains query-relevant events and evolving target states in structured memory, and a Memory-Grounded Decoder (MGD) that identifies valid targets from this memory and localizes them in the current frame. Experiments show that Sekai significantly outperforms existing online RVS methods, achieving 50.33 J&F and improving over the strongest baseline by 3.2 points. Code, example annotations, and evaluation scripts are available at this https URL.

---


### 207. [Don't Replace, Complement: A Detector-Agnostic Subspace Signal for Near-OOD Detection](https://arxiv.org/abs/2611.06688)

**<font color=#1a73e8>作者：</font>** Wonseok Shin, Songkuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc out-of-distribution (OOD) detection is mature on far-OOD yet remains weak on near-OOD. These two settings differ in their use of class-characteristic feature directions: far-OOD inputs largely fail to activate those of their predicted class, whereas near-OOD inputs activate them much as in-distribution samples do. Because the axis separating far-OOD leaves near-OOD almost indistinguishable from ID, a score optimized for one setting is misaligned with the other; where a detector already saturates far-OOD, added near-OOD sensitivity is bought partly against it. This divergence motivates a targeted near-OOD signal designed to complement existing scores. We propose PLUS (Per-class Low-dimensional sUbspace Signal). For each class, PLUS selects the $m$ most class-active neurons from a sparse autoencoder, orthonormalizes the corresponding decoder directions to form a low-dimensional subspace, and scores an input by its per-class whitened squared Mahalanobis distance $z$ within the subspace of its predicted class. Designed as a dedicated complement rather than a standalone detector, the signal $z$ is fused additively with any calibrated base score at a single, fixed weight. This weight is a single global constant: no value is adjusted per backbone, per OOD dataset, or per deployment, and all calibration statistics are estimated from ID validation data alone. When applied to 18 existing detectors spanning diverse method families, $z$ consistently improves near-OOD AUROC in all 126 detector--backbone combinations. Far-OOD performance is broadly maintained or improved, with only marginal declines where the base score is near-optimal, making $z$ a robust, detector-agnostic complement across backbones.

---


### 208. [You Know What You Will Like: People Predict Their Own Ratings Better Than Recommender Systems](https://arxiv.org/abs/2611.06696)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recommender systems usually learn what people want from what they have done. Platforms could also ask people directly, but asking is costly: 98.8% of the prompts in our data went unanswered. Theories of statistical prediction imply that a person's own forecast adds little to a recommender algorithm built from many people's behavior. Theories of dispersed knowledge imply that people hold information about their own taste that the data lack. We test the two with the MovieLens Beliefs dataset. In 2023-2024, a homepage prompt asked members how they expected to rate movies they said they had not seen. Of 26,020 such expectations, 551 from 277 members were followed by a rating at least a day later. We compare each expectation with four benchmarks: the platform's own predicted rating, two collaborative-filtering models (matrix factorization and an item neighborhood), and a stack trained on other members' outcomes. The trained models use each member's latest ratings. People predict their own ratings more accurately than all four benchmarks (correlation 0.69, against 0.34 for MovieLens and 0.54 to 0.59 for the trained recommenders). Added to all the machine forecasts and features, the expectation lowers out-of-sample mean squared error by 26%. The gain holds when models are trained on earlier expectations and tested on later ones. A member's earlier expectations about other movies do not replace the current one. In ordering a member's own movies, the trained recommenders are statistically indistinguishable from the person. On old, heavily rated movies, the machines do as well or better. The results reconcile the two theories: the crowd's data suffice where they are rich, and the person adds information about the specific item. We derive four design principles for preference elicitation and recommender evaluation.

---


### 209. [PINR-ESI: Physics-Informed Self-Supervised Implicit Neural Representation Framework for EEG Extended-Source Imaging](https://arxiv.org/abs/2611.06700)

**<font color=#1a73e8>作者：</font>** Zhiyong Zhou, Sheng Liao, Youshen Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG extended-source imaging aims to localize active cortical regions and characterize their spatial extent, yet supervised inverse networks typically depend on synthetic EEG-source pairs and may be sensitive to synthetic-to-real mismatch. We propose a physics-informed self-supervised implicit neural representation (INR) framework for spatial source reconstruction without paired source labels or simulation-based supervised pretraining. The lead field matrix encodes the source-to-sensor volume-conduction model and constrains the INR through agreement between predicted and measured EEG. Cortical current density is modeled as a continuous coordinate-conditioned field. A classical inverse estimate provides warm initialization and spatial constraints on source activity, while patch-integrated projection maps the field to discrete source coefficients for forward modeling. Simulations with varying noise levels, source counts, and source extents showed the clearest advantage in identifying active cortical regions, particularly for multiple and larger sources. Quantitative and qualitative evaluations using real EEG recordings from epilepsy patients and intracranial stimulation experiments further supported the feasibility of the framework for source imaging. These findings suggest the potential of physics-informed self-supervised INR for extended-source imaging.

---


### 210. [Agent-Driven Generative Priors for Pathology Image Synthesis and Segmentation](https://arxiv.org/abs/2611.06701)

**<font color=#1a73e8>作者：</font>** Sicheng Yang, Rui Tang, Haipeng Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning methods for pathology are constrained by the limited availability and high cost of large-scale pixel-level annotations. Synthetic data can alleviate this limitation, but existing pipelines often lack reliable quality control and remain weakly connected to downstream analysis. To address these issues, we propose a three-stage framework that integrates automated data screening, generative representation learning, and efficient adaptation to downstream tasks. First, we develop a pathology agent system to assess image quality and filter samples, resulting in TCGA-200K, a dataset containing 217,030 pathology patches selected from the public TCGA repository. Second, we train a generative model on the screened data. In addition to image synthesis, its backbone learns structural and semantic representations that can be transferred to downstream tasks. Third, we adapt the pretrained generative backbone to semantic segmentation using a lightweight task-specific head. We further introduce PathSeg-380K, a semantic segmentation dataset with expert annotations for approximately 380,000 cells across 12 cell types. Experiments on multiple pathology datasets show that the proposed framework achieves state-of-the-art segmentation performance. Our code is publicly available at this https URL.

---


### 211. [ALTO: African and Levantine Tech-Facilitated Gender-Based Violence Corpus](https://arxiv.org/abs/2611.06706)

**<font color=#1a73e8>作者：</font>** Tianwei Zhang, Ivy Njoki Nyagwencha, Zahraa Dirani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tech-facilitated gender based violence (TFGBV) is a pervasive online harm affecting women and gender minority groups through its many direct and covert forms. Current models and annotated datasets for gendered harm detection are dominated by data from, and models trained in, Global North languages. In collaboration with civil society organizations (CSOs) from Jordan, Francophone West Africa, and Kenya, we developed a community-led approach to crowdsource culturally and linguistically relevant instances of TFGBV in Levantine Arabic, African French, and Swahili. We annotated the crowdsourced data using active learning to develop a small but performant dataset (N=3022) called ALTO to improve TFGBV detection in the three languages. Through benchmarking and fine-tuning experiments, we show that existing harmful content detection models show poor TFGBV recall within ALTO and improve with fine-tuning. We found that models often miss covert harms across all languages, while error rates are markedly higher in Swahili. We report the experimental results and release the annotation taxonomy, dataset, and trained models.

---


### 212. [Energy-Guided Transport for Projection-Free Physics-Informed Flow Matching](https://arxiv.org/abs/2611.06711)

**<font color=#1a73e8>作者：</font>** Giuliano Galadini, Aurelio Uncini, Danilo Comminiello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models, particularly Flow Matching frameworks, have emerged as powerful tools for synthesizing complex physical systems. However, standard architectures remain purely statistically driven and agnostic to the underlying governing equations, often violating fundamental physical constraints during inference. Existing zero-shot approaches designed to enforce these constraints typically rely on rigid algebraic projections. While effective for sparse boundary conditions, applying such discrete geometric corrections to dense, full-domain PDEs may disrupt the probability path, \rev{potentially deviating from the learned manifold and introducing substantial computational overhead}. To address these challenges, we introduce Energy-Guided Transport, a novel training-free framework that formulates non-linear physical constraints as a smooth potential energy landscape. Rather than interrupting the ODE integration, our method applies a continuous dissipative force directly to the intermediate generative states, steering them toward the physical manifold. By evaluating this force implicitly via reverse-mode automatic differentiation, our framework preserves the natural dynamics of the flow while maintaining an efficient $\mathcal{O}(N)$ algorithmic complexity. We extensively evaluate our framework across various 1D and 2D physical systems, including the chaotic Navier-Stokes equations. Our method achieves stable generation without structural divergence, significantly improves the stability-accuracy trade-off compared to state-of-the-art methods, and substantially accelerates inference with respect to exact projection strategies. Code available at: this https URL.

---


### 213. [Symmetry Breaking at the Edge of Stability via Central Flow Analysis](https://arxiv.org/abs/2611.06718)

**<font color=#1a73e8>作者：</font>** Naima Elosegui Borras, Georgios Arvanitidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous symmetries in neural networks lead to conserved quantities that are invariant under gradient flow, such as layer balancedness in linear and ReLU networks. Finite-step gradient descent need not preserve these laws, particularly at the edge of stability (EOS), where the iterates oscillate around a smoother trajectory, which can be described by the central flow dynamics (Cohen et al., 2025). We study how gradient flow conservation laws evolve under the central flow description of this regime. We show that the curvature correction induces a finite-dimensional drift determined by the oscillation covariance along critical parameter directions. We thus take the first steps to analyse which conservation laws remain and are broken at the EOS according to the central flow dynamics by analysing a scalar two-layer model, two-layer matrix factorisation, and a two-layer ReLU network, where the known conservation laws are shown to be complete (Marcotte et al., 2023).

---


### 214. [Coupled Scene Graph Anticipation: When With-Constraint Recall Hides Structural Inconsistency](https://arxiv.org/abs/2611.06738)

**<font color=#1a73e8>作者：</font>** Zeno Nongmaithem, Anushttha Srivastava, Anshit Sinha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Graph Anticipation (SGA) predicts object relationships in future video frames. Continuous-time SGA models evolve each subject-object pair with an independent Neural ODE, so relationships sharing an entity cannot influence one another during integration, and nothing prevents mutually exclusive predictions, such as "sitting on" and "standing on", for the same pair. We introduce CoupledSGA, which links such relationships through a Relationship Interaction Graph with graph attention inside the ODE vector field, and adds a Structural Consistency Loss ($\mathcal{L}_{SC}$) based on a matrix of mutually exclusive predicates.
Developing CoupledSGA revealed a limitation of the evaluation protocol. With-Constraint evaluation keeps one predicate per group for each subject-object pair, so its R@K and mR@K cannot capture the within-group violations targeted by $\mathcal{L}_{SC}$: we prove they are unchanged whenever each group's winning predicate and its score are held fixed. We further show that the gradient of $\mathcal{L}_{SC}$ depends on predicate scores rather than ground-truth labels: for two-predicate rules it amplifies the ordering the model already holds, and when all scores in a group are equal it suppresses predicates in more exclusion rules more strongly, explaining why the penalty can lower recall while improving consistency.
On Action Genome, activating $\mathcal{L}_{SC}$ after two warm-up epochs reduces R@20 from 42.21% to 35.18% while lowering the No-Constraint contradiction rate from 45.92% to 4.07% (matched-budget R@20: 40.48% CoupledSGA vs. 44.78% SceneSayerODE). CoupledSGA is a testbed, not a state-of-the-art claim: With-Constraint recall captures the cost of enforcing structural consistency but not the improvement. We recommend reporting No-Constraint results alongside a contradiction rate for methods that constrain predicate co-activation.

---


### 215. [Continual Classification Beyond the Kernel Regime: Harnessing the Sparsity Bias of L2 Regularization in Diagonal Linear Networks](https://arxiv.org/abs/2611.06759)

**<font color=#1a73e8>作者：</font>** Gilad Karpel, Itay Evron, Ron Meir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study logistic regression for continual learning with linear predictors in a high-dimensional statistical setting. Existing theoretical work has largely focused on continual linear regression with variants of L2 regularization, motivated by their analytical simplicity and connection to the kernel regime of neural networks. We first derive the optimal L2 regularization strength for continual linear classification and characterize its generalization performance, recovering behavior analogous to prior results for continual linear regression. Next, we examine the effect of L2 regularization in deeper models using a minimal two-layer diagonal linear network. In the single-task setting, L2 regularization on the weights of such models is known to promote sparsity in the resulting predictor, yielding a rich, sparse feature-learning regime beyond the kernel regime (a similar effect arises in two-layer ReLU networks). However, in continual learning, where L2 regularization is typically centered on previous-task weights, this sparsity bias is no longer preserved. We therefore propose a weighted variant of L2 regularization that extends this beneficial sparsity bias to continual learning. We show theoretically and empirically that, for a sufficiently sparse teacher, our variant converges substantially faster than directly learning a linear predictor with conventional continual L2 or L1 regularization, trading some long-horizon bias for markedly improved performance over moderate task horizons.

---


### 216. [Semantic Residual Vector Quantization for Sign Language Generation](https://arxiv.org/abs/2611.06781)

**<font color=#1a73e8>作者：</font>** Chang Liu, Ke Han, Niccolò Biondi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language generation (SLG) maps written sentences into signing motion while preserving both lexical content and fine-grained articulation. This requires a model to decide what signs should be expressed and to realize them through precise handshape, trajectory, facial expression and body coordination. Existing pose-based systems and reconstruction-only motion tokenizers often entangle these two decisions, leaving the generator without an explicit text-aligned intermediate target for what to sign before refining how to sign it. To address this issue, we introduce Semantic Residual Vector Quantization (SRVQ), a framework for SLG that frames generation as a two-level process moving from semantics to kinematics. The newly introduced SRV Quantizer learns a hierarchy in which the first residual level encodes sign content and subsequent levels refine pose, handshape, trajectory, and body coordination, all within a single quantizer and without separate semantic representations or external planning stages. Through word-aware conditioning for hierarchical code generation, a masked semantic generator predicts semantic codes and a kinematic generator completes the residual codes for full SMPL-X motion synthesis. We evaluate using retrieval and FID in a shared text-motion embedding space, alongside standard geometric metrics. On CSL-Daily and Phoenix-2014T, SRVQ achieves R@1 of 82.3 and 70.3, outperforming the previous SOTA by 30 and 46 points, respectively.

---


### 217. [FedFiOT: Fisher-Weighted Optimal Transport for Model Merging in One-Shot and Few-Round Federated Learning](https://arxiv.org/abs/2611.06783)

**<font color=#1a73e8>作者：</font>** Quan Minh Nguyen, Hoang M. Ngo, Bhakti Chowkwale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot and few-round federated learning (FL) reduce communication burden by constructing a global model within one or a few communication rounds, but often achieve lower performance than conventional multi-round FL. Without frequent synchronization, client models may drift apart, causing neurons that learn similar features to occupy different positions across clients. At the same time, local data heterogeneity can cause corresponding parameters to differ in their importance to each client's predictions. Together, these challenges cause direct averaging to combine mismatched neurons and assign equal weight to parameters despite differences in their importance. We propose FedFiOT, a Fisher-weighted optimal transport framework for one-shot and few-round FL that leverages Fisher information to quantify parameter importance and guide neuron alignment and model aggregation. FedFiOT jointly optimizes neuron correspondences and global model parameters through alternating minimization of a shared Fisher-weighted objective. Theoretically, we show that FedFiOT's optimization procedure monotonically decreases the layer-wise merging objective and establish a stationarity bound that quantifies the effects of client heterogeneity and nonuniform Fisher this http URL across multiple datasets demonstrate consistent improvements over competing baselines in both one-shot and few-round federated learning settings.

---


### 218. [Go-Go-Go: the game of Go without turns](https://arxiv.org/abs/2611.06786)

**<font color=#1a73e8>作者：</font>** Andrea Cambiaghi, Marco Tarini  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The study of variants of classic games has a long history, with chess alone inspiring countless variants that have been proposed, analyzed, and studied. The game of Go, despite rivaling chess in age, cultural relevance, popularity, and strategic depth, has seen drastically fewer variants.
We introduce Go-Go-Go, a variant of the classic game of Go where there are no turns, and players play stones simultaneously and asynchronously on the board. The variant (which is to be played through a computer) includes a basic mechanism to avoid excessive spamming of moves, by imposing a minimal delay between moves that depends on their relative spatial distance. Apart from the lack of time discretization, most of the ruleset of the original game is either directly maintained or adapted in a natural way that preserves the original spirit. The first playtesting indicates that this results in the preservation of much of the emerging strategies and "flavor" of Go, while replacing the long strategic reasoning with fast paced, instinctive action fueled by quick reflexes. Play testers also report the need to balance immediate but suboptimal reactions with more reasoned but slower plays.
We offer a publicly available, playable, OpenSource, and online reference implementation of Go-Go-Go at this http URL

---


### 219. [Integrated Identity Protection for Semantic Communications in Embodied IoT Systems](https://arxiv.org/abs/2611.06788)

**<font color=#1a73e8>作者：</font>** Yu Zhang, JingQi Liu, Shuangrui Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embodied Internet of Things (IoT) systems are promoting the adoption of task-oriented semantic communication (SemCom), in which the trustworthy task decisions require both semantic information reliability and source legitimacy. However, existing trustworthy designs in SemCom mainly focus on semantic content recovery and protection, with limited attention to source legitimacy. Motivated by this limitation, this paper establishes a new information exploitation paradigm for integrated SemCom-identity protection to address active source impersonation and passive identity inference by treating each SemCom signal as an inherent carrier of both task-relevant semantic information and transmitter physical identity information. We first examine these two information resources and then analyze their integration feasibility at the observation, processing, and decision levels. To exploit these resources for trustworthy decision making, we further develop a dual-branch identity protection mechanism under different operating modes. In the authentication mode, semantic recovery and physical-layer source verification are performed in parallel using the same received observation. In the concealment mode, identity exposure is suppressed while semantic recovery quality is maintained to support anonymous sensing reports. The resulting outputs are jointly interpreted to support task decisions under mode-specific identity protection requirements. Finally, two representative case studies on active source impersonation and passive identity inference are presented to evaluate the proposed framework.

---


### 220. [A Frame-Level View and Image-Quality Annotation Tool for Fetal Echocardiography: Comparison with Spreadsheet Annotation](https://arxiv.org/abs/2611.06791)

**<font color=#1a73e8>作者：</font>** Mohamed Azzam, Ziyang Xu, Quinlan Couch 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Objective: To develop the Cardiologist Annotation Tool (CAT) for frame-level cardiac view and image-quality annotation in fetal echocardiography and compare it with spreadsheet-based annotation.
Methods: CAT provides cine playback, frame navigation, and keyboard-based labeling without manual frame-range entry. Experts annotated 25 studies using both methods, and spreadsheet annotations were audited for predefined data-entry errors. In a randomized crossover study, six medical students annotated two normal studies, one with each method, against an expert reference.
Results: Among 1,746 spreadsheet-annotated files, 6.2% contained major or critical data-entry errors, more frequently in congenital heart disease than normal studies (10.9% vs 3.4%). CAT yielded more annotated view segments per clip (3.6 vs 1.5). Rates of labeled and correctly labeled frames per minute were 1.77 and 1.68 times those with spreadsheets, respectively (both P = 0.031), with gains in all six students. No detectable difference in view-label accuracy was observed.
Conclusion: CAT eliminates manual frame-range entry and enables finer-grained, structured annotation of fetal echocardiography, providing a practical approach to preparing datasets for AI research.

---


### 221. [Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3](https://arxiv.org/abs/2611.06793)

**<font color=#1a73e8>作者：</font>** Harsidak Singh Banwait  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample-efficient fluid intelligence requires agents that rapidly form working models of unfamiliar interactive environments. ARC-AGI-3 tests this across uninstructed visual games scored by Relative Human Action Efficiency, which penalizes exploratory waste quadratically. When frontier models read raw integer grids, serialization destroys spatial topology, and they spend hundreds of actions rediscovering basic boundaries and symmetries. We introduce SARBLOH, an open-weight agent built on the premise that spatial perception, not planning capacity, governs interactive reasoning on ARC-AGI-3. A zero-parameter O(HW) perception engine turns each frame, in 35 ms, into an object inventory with bipartite temporal tracking, a geometric briefing that separates proven invariants from affordance hypotheses, and an annotated canvas. Paired with a code-as-action runtime, the agent writes algorithmic hypotheses instead of low-level moves. Across eight presentations, grounded perception raises the rubric score from 3/28 to 25/28 points while cutting token use by 89.4%. On 23 held-out games, geometric invariants generalize with 100% accuracy, while single-frame affordance guesses fall to 6-50%, so active verification probes remain necessary. On the public set, Run A (briefing off) solved 143 of 183 levels in 8.2 hours at 59.4% single-pass efficiency; Run B (briefing on) reached 63.5%. Within the nine-hour budget on one Kaggle RTX PRO 6000 GPU, SARBLOH scored 16.53 on the hidden Kaggle evaluation, 13.7x the first Milestone winner.

---


### 222. [VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796)

**<font color=#1a73e8>作者：</font>** Yihong Luo, Tianyu Pang, Tianyang Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation offers efficient generation with diffusion and flow models, but preserving quality with only a few sampling steps remains challenging. Distribution-matching methods via score distillation provide a strong foundation, yet they rely on accurately tracking the student's changing distribution. At intermediate generation steps in few-step sampling, student-score estimation can be difficult, and commonly used estimators may describe a different distribution from the one used to update the student. Flow matching allows a more flexible approach to supervision through velocity fields constructed from the student's sampling process. Building on this perspective, we introduce Velocity Adversarial Distillation (VAD), which uses a learned critic to compare student and teacher fields and turn their disagreement into feedback for learning. VAD unifies score distillation, Fisher-based matching, and moment matching, also explaining existing heuristic MMD updates and delivering new training objectives. We further develop VA-TDM, which follows trajectory distribution matching: providing supervision for partial denoising along the student trajectory. Beyond this, VA-TDM combines transition-aware online velocity learning and dual-form VAD supervision across intermediate student transitions. Extensive results show that VA-TDM is powerful for learning few-step generators, achieving state-of-the-art four-step performance in both text-to-image and text-to-video generation across various backbones and scaling effectively to 33B MiniMax-H3. In particular, our VA-TDM-H3 notably outperforms the few-step Fast-H3 and is closer to the original many-step H3 according to human preference.

---


### 223. [Message-passing graph persistence](https://arxiv.org/abs/2611.06801)

**<font color=#1a73e8>作者：</font>** Jorge Luiz Franco, Arthur Queiroz Moura, Moacir Ponti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing graph neural networks (GNNs) are limited in expressive power by the one-dimensional Weisfeiler-Leman test. Persistent homology (PH) provides topological descriptors that can complement GNN representations, but existing approaches typically compute persistence separately from the representation learning process. In this paper, we introduce Message-Passing Graph Persistence (MGP), a family of topological descriptors that incorporates message passing into graph filtrations. At each filtration step, node embeddings are updated using the current subgraph and associated with persistence events. These embeddings also determine the representatives of connected components during persistence computation. We prove that MGP is invariant under graph isomorphism and that it is strictly more expressive than the PH-based descriptors it extends. We evaluate MGP on an expressivity benchmark and on several graph classification and regression datasets. Experiments show that MGP outperforms other PH-based descriptors on most of these datasets.

---


### 224. [Context-Aware Autoregressive Image Generation for Emerging Reasoning Properties](https://arxiv.org/abs/2611.06838)

**<font color=#1a73e8>作者：</font>** Jixuan Ying, Haoyu Liu, Timing Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive image generation has recently emerged as a competitive visual generation paradigm, yet its generation order is often predefined or heuristic, such as next-patch prediction, random-order prediction, or one-step generation for specific scales. We observe that these strategies can cause models to overlook important structural dependencies in images, thereby limiting both structural robustness and reasoning capability. In this work, we propose a context-aware autoregressive generation framework, where the model dynamically determines the next token location based on global context and current local information. Rather than following a fixed or random order, our method allows the generation process to adapt to image structure and semantic dependencies. Extensive experiments show that context-aware generation significantly improves structural robustness across different image AR paradigms, including masked autoregressive and scale-wise autoregressive models. Beyond quantitative improvements, we further observe emerging reasoning properties: the model can better understand complex semantic instructions and generate images that more faithfully follow the given guidance. These findings suggest that generation order is a critical yet underexplored factor in image autoregressive modeling, and that context-aware decoding can unlock stronger reasoning-aware visual generation capabilities. Code is available at this https URL.

---


### 225. [Navigating Disagreement Among Criteria for Evaluating Explanation Faithfulness](https://arxiv.org/abs/2611.06846)

**<font color=#1a73e8>作者：</font>** Grant Shanklin, Jiří Němeček, Asia Biega  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faithfulness requires that algorithmic explanations accurately reflect the model's behavior. Yet existing operationalizations of faithfulness can disagree about whether the same explanation is faithful, leaving developers and auditors to choose among conflicting evaluations. In this paper, we investigate disagreement among evaluation criteria and offer a practical path forward for evaluating explanation faithfulness. We first identify how operationalizations of faithfulness differ. We introduce a faithfulness functional that locates their disagreements in what an explanation claims about the model, which comparisons bear on that claim, and how agreement across those comparisons should be aggregated, and we reconstruct existing evaluation criteria within it. We argue these reconstructions support understanding faithfulness as a common though incompletely specified relation between the model and explanation, so the differences reflect choices left open by the general requirement. Justifying an operationalization then comes down to justifying these choices, which, on our view, draws on explanatory, institutional, and normative considerations. We support this argument with a case study of adverse action notices, reconstructing the evaluation implicit in an industry-proposed procedure and identifying which of its choices the setting justifies and which remain open. Our work gives auditors and practitioners a way to navigate disagreeing evaluations of faithfulness. It also explains why the literature should expect multiple operationalizations, while showing how concrete settings can narrow the choice among them. More broadly, our analysis shows how a shared requirement of faithfulness can support contextually justified evaluations despite disagreement among existing metrics.

---


### 226. [Trainspotting: Learning Object-Centric 3D Reconstruction from Found Photos](https://arxiv.org/abs/2611.06849)

**<font color=#1a73e8>作者：</font>** Hanyu Chen, Noah Snavely  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art feedforward reconstruction models perform poorly on in-the-wild object-centric photo collections. They are trained largely on single-session object captures whose images vary in viewpoint while the object and its environment remain nearly fixed. Public photo archives contain a different form of multi-view data. They hold found photos of the same object or design: photos taken independently by many people across years, environments, cameras, and sometimes physical units. In this work, we introduce Trainspotting, a dataset of 12,068 objects and 311,886 photos from Wikimedia Commons. We reconstruct each object to recover camera poses, multi-view stereo depth, and object masks. We categorize the objects into three regimes: objects fixed at one site, objects that move between sites, and designs shared by many physical units. Evaluating recent feedforward reconstruction models on Trainspotting shows that they fail most severely in the last two regimes. Fine-tuning VGGT-$\Omega$ on Trainspotting significantly improves camera pose, depth, and 3D geometry on held-out objects. We observe similar improvements on the independent NAVI in-the-wild benchmark, which contains photos of each object in different environments. Performance on conventional benchmarks remains largely unchanged.

---


### 227. [Balancing hierarchical representation and quantization: A performance trade-off in text embeddings](https://arxiv.org/abs/2611.06859)

**<font color=#1a73e8>作者：</font>** Kai Ponel, Marco Polignano, Erasmo Purificato 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency. This work is an empirical benchmark study of how these two orthogonal, already-established techniques interact. We evaluate 38 tasks from the Massive Text Embedding Benchmark (MTEB) using four transformer-based embedding models, covering 1D and 2D hierarchical representations combined with 32-bit, 8-bit, and binary quantization, for 168 configurations per task. We report each efficiency dimension separately: theoretical per-vector storage and end-to-end evaluation time. Under a Friedman test with Nemenyi post-hoc analysis, int8 quantization is statistically indistinguishable from float32 for pair classification and re-ranking and costs at most 1.5 percentage points overall, whereas binary quantization is significantly worse across every task category. Halving the embedding dimension once is not statistically detectable above $m=16$; two successive halvings always are. Combining an 8x dimensionality reduction with int8 yields a 32x reduction in per-vector storage at 94.4% of baseline effectiveness. Because evaluation times were measured once, we treat them as indicative: we find no evidence that quantization speeds up evaluation, whereas sampling from intermediate layers shortens it substantially. Retrieval degrades far faster than every other category, so we report findings per task category.

---


### 228. [CounterFactual Retrieval for Evidence-Aware Individual Animal Identification](https://arxiv.org/abs/2611.06864)

**<font color=#1a73e8>作者：</font>** Ankit K. Upadhyay, Aleksandr Algasov, Ekaterina Nepovinnykh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated identification of individual animals is moving from small curated studies toward shared benchmarks and reusable foundation models. This progress is useful, but current evaluation leaves the evidence behind a match unresolved, i.e., high retrieval accuracy does not show whether a model used animal features or identity-correlated shortcuts. We address this with Counterfactual Foreground Retrieval (CFR), an evidence-aware evaluation protocol. CFR evaluates the same query-gallery task under different views: full image, foreground-only, and shortcut-only. The full-image measures standard retrieval performance; the foreground-only measures foreground-supported retrieval; and shortcut-only view measure how much identity signal is recoverable from background, or silhouette. This turns a retrieval score into an evidence profile: how well the model performs on the original images, how much of that performance remains when only the animal is visible, and how much identity signal remains recoverable when the animal is removed. We release around 0.5M masks for 34 datasets and code for mask generation and CFR evaluation.

---


### 229. [PixelSpline: Continuous Space-Time Video Super-Resolution via Endpoint-Anchored Shared Pixel Trajectories](https://arxiv.org/abs/2611.06870)

**<font color=#1a73e8>作者：</font>** Wanqi Yuan, Nianyi Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing continuous space-time video super-resolution methods often infer motion from only two endpoint frames and model the two motion directions independently, making them vulnerable to ambiguous correspondence and inconsistent trajectories. We introduce a continuous STVSR framework that combines long-context encoding, continuous HR feature lifting, and an endpoint-anchored PixelSpline. Long-range observations provide more reliable endpoint representations, while continuous upsampling constructs detailed appearance features directly on the requested HR grid. PixelSpline explicitly models each pixel's motion as a single continuous trajectory shared by both endpoints. Using this trajectory, our method warps endpoint colors into a coarse intermediate frame and aligns the HR features for residual reconstruction. Experiments across spatial and temporal upsampling settings demonstrate that the proposed framework offers a favorable quality--efficiency trade-off.

---


### 230. [Learning to Decode Linear Codes with Generalized Belief Propagation Network](https://arxiv.org/abs/2611.06874)

**<font color=#1a73e8>作者：</font>** Samira Malek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Error correcting codes are a fundamental component of communication systems, enabling reliable data transmission over noisy channels. Recently, neural decoders have demonstrated notable performance gains over classical iterative algorithms. In this paper, we propose a Generalized Belief Propagation Network (GBPNet) that preserves message-passing symmetry while enhancing the decoder's learning capability. The architecture uses cascaded variable-node updates and learned element-wise message scaling while retaining the Tanner graph structure. We also introduce two training strategies, progressive training and high-SNR training, that improve decoding accuracy. Experimental results on several linear codes show that GBPNet achieves lower bit error rates than conventional belief propagation and the evaluated state-of-the-art neural decoders.

---


### 231. [Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes](https://arxiv.org/abs/2611.06879)

**<font color=#1a73e8>作者：</font>** Benjamin Jacob Bodner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optimization engines with online probes of curvature, plateaus, separability, kinks, basins and fractal structure. Each probe has a default, a dimension-by-budget validity range and a cost charged to the budget. In its pre-registered development loop on bbob, 32 of 36 predictions held over the last 16 confirmations. AMM was then tested once on held-out bbob instances 101-110 (D=2-40, 10*D-1000*D) against up to seven competitors. It has the highest target share in 382 of 600 function-dimension-budget cells (236 outright, 146 tied) and, by a descriptive posterior rule, is credibly behind in 35, mostly at 10*D and 30*D. At every budget it also leads the controls built from its own engines (the best engine alone, the best engine per dimension and budget, and a greedy schedule), narrowly at 10*D and 30*D, and nevergrad's NgIohTuned. In pre-registered runs its lead over IPOP-CMA-ES holds under affine and box transformations, on box-constrained bbob and, pooled, on rotated f2-f4, but rotating the separable f3 and f4 removes most of the lead there. On held-out MA-BBOB its final share at 2000*D is level with IPOP-CMA-ES's and its anytime area lower. We published AMM as an open-source Python package (pip install amm-optimizer; this https URL).

---


### 232. [Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890)

**<font color=#1a73e8>作者：</font>** Jack Nugent, Jia Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For many computer vision tasks, neural networks can be trained to produce a low average error, yet they still fail on seemingly simple scenes. Reducing these failures requires first finding them, but they may not be in a fixed dataset. We study procedural adversarial learning (PAL), a framework of minimax training and adversarial evaluation which searches the input space of a procedural generator for difficult instances. The procedural generator is an interpretable program mapping a low-dimensional vector of control parameters (e.g. layout, lighting, pose) to a rendered image and its label. We introduce the Simple-PAT algorithm, which uses zeroth-order optimization in the procedural generator's parameter space to propose adversarial training samples that are generated on demand. We also create PAL-Dojo, a collection of efficient procedural generators for surface normal estimation, image segmentation, and human pose estimation. Against a cross-model black-box adversary with 50M aggregate queries, Simple-PAT reduces worst-case error by a geometric mean of 3.15x compared to standard training and 2.63x compared to the strongest robust training baseline. Code is available at this https URL.

---


### 233. [Occlusion for Free: Detecting Occlusion from the Disagreement Between Two Monocular Distance Cues](https://arxiv.org/abs/2611.06899)

**<font color=#1a73e8>作者：</font>** Chibueze Praise Onyenweaku, Toyibat Adele, Sikirulahi Opeyemi Abdulkareem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowing that a pedestrian is occluded is useful to a robot even when the detector cannot recover the hidden pixels, but occlusion estimators are normally trained on occlusion annotations that deployment settings rarely have. We show that occlusion can be read off two distance estimates a camera-only pipeline already computes. Apparent height is largely unchanged by occlusion, because the detected box still spans the whole person; monocular metric depth is pulled toward the occluder, because the nearest surface inside the box is what a depth map reports. Only their ordering matters, so no focal length, stature, or depth scale is needed, provided the depth model's error is close to a pure gain, a condition that can be checked without labels. The score detects heavy occlusion on KITTI with AUC 0.909 (0.888 over all annotated pedestrians, including those the detector misses), requires no training and no occlusion labels, and is not a proxy for range: within fixed distance bands it holds AUC 0.894-0.925 while true distance alone sits near chance. On synthetic CARLA scenes with measured visibility it reaches 0.819, against 0.644 for distance alone. We arrived here after measuring three standard architectural responses to occlusion, depth fusion, occlusion-simulating augmentation, and attention, none of which improved detection outside its training distribution in the configurations we tested, and after finding that a detector trained on German roads loses half its accuracy on self-annotated street scenes in Lagos, Nigeria. Signals that need no local annotation are worth more in settings that benchmarks do not represent.

---


### 234. [Motion-guided Contrastive Regularization For Latent World Models](https://arxiv.org/abs/2611.06901)

**<font color=#1a73e8>作者：</font>** Yiwen Chen, Qiqi Hou, Jisoo Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify static collapse, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because static content is temporally predictable yet diverse across episodes, this failure can persist despite regularizers such as SIGReg. A controlled study on OGBench-Cube shows that introducing randomized backgrounds substantially degrades planning performance while leaving the underlying manipulation task unchanged. To address this problem, we propose motion-guided contrastive regularization. Our approach compares predicted latent transitions with transitions to candidate observations from the same episode, reducing the usefulness of static background identity for distinguishing action outcomes. Optical-flow similarities provide soft contrastive targets, allowing candidates with similar motion to receive similar supervision. Combined with latent prediction and SIGReg, our objective encourages representations to preserve within-episode state distinctions and similarities between related transitions. Our method improves planning success over LeWorldModel (LeWM) from 52% to 78% on OGBench-Cube with randomized backgrounds and from 14% to 54% on LIBERO-Object, while maintaining comparable performance on four other visual-control benchmarks.

---


### 235. [Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905)

**<font color=#1a73e8>作者：</font>** Michal Korniak, Marco Bagatella, Ralf Römer 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The introduction of generalist robot policies has enabled a single, large model to learn to perform a variety of tasks from a vast pre-training corpus. While these models often exhibit powerful zero-shot generalization capabilities, they typically require an adaptation phase to achieve sufficient performance in deployment. Iterated self-improvement via reinforcement learning (RL) has demonstrated promise in enabling this adaptation, yet such approaches have been largely explored in single-task settings - where the goal is to simply improve on a narrow deployment task - which lies in stark contrast to the multi-task capabilities of the base policy. In this work we ask whether generalist robot policies are capable of multi-task, generalist improvement in deployment - targeting many diverse tasks simultaneously - and what algorithmic recipe enables this. To answer this question, we first develop a set of structured evaluations to test generalist improvement capabilities, and systematically evaluate algorithmic and practical design choices regarding value estimation, policy extraction and resource allocation. We show that not only can generalist policies be improved online across diverse tasks, but that the right recipe can enable generalization and increase performance on tasks not considered during online training. We characterize when this generalization occurs and show that both the training task distribution and the use of value-based RL are critical. To the best of our knowledge, this is among the first evidence for online generalist improvement for robot foundation models.

---


### 236. [FrontierPhysics: Evaluating Agents for End-to-End Physics Research](https://arxiv.org/abs/2611.06910)

**<font color=#1a73e8>作者：</font>** Bingran You, Wenjun Ke, Ria Rosenauer 等 72 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics. Each task requires agents to review the literature, develop a research plan, conduct research and experiments, and produce structured outputs and scientific manuscripts. Combining deterministic verifiers with expert-authored rubrics, FrontierPhysics evaluates whether agents' research is correct and publishable. Across 22 models in 26 configurations, no configuration passes more than 46 of its 168 rollouts. Manual review of agent trajectories shows that frontier agents' main weaknesses are insufficiently rigorous reasoning and limited expert intuition, rather than gaps in physics knowledge or execution errors.

---


> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
