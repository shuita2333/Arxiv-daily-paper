# 📦 其他研究 | 2026年11月22日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

---

### 201. [Backbone Matters: Benchmarking Encoder-Decoder Networks for Semantic Segmentation of Driving Scenes on BDD100K](https://arxiv.org/abs/2611.26191)

**<font color=#1a73e8>作者：</font>** Ehsan Rassekh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation gives an autonomous vehicle a dense, pixel-level description of its surroundings and is a core part of scene understanding. Most segmentation networks consist of an encoder (the backbone) and a decoder, yet the backbone is often chosen without a systematic comparison. This work studies this choice on the BDD100K driving dataset. Four widely used decoders (U-Net, FPN, LinkNet and PSPNet) are combined with 13 backbones from six families (ResNet, VGG, DenseNet, Inception, MobileNet and EfficientNet), and all 52 models are trained with one common protocol. The best model, an FPN decoder with an EfficientNet-B4 backbone, reaches 62.6% mean intersection over union (mIoU), 89.8% accuracy and a loss of 0.092. Only two of the 52 models, both FPN with EfficientNet, exceed the 56.9% mIoU reported with the BDD100K benchmark. The effect of the backbone depends strongly on the decoder: the same EfficientNet-B4 gives 42.6% mIoU with PSPNet but 62.6% with FPN, and the gap between the best and the worst backbone ranges from 12.0 points (U-Net) to 42.5 points (FPN). The results and the scope of this study are discussed.

---


### 202. [A version of the Cloude/van Zyl decomposition for full/quad pol synthetic aperture radar data](https://arxiv.org/abs/2611.26195)

**<font color=#1a73e8>作者：</font>** Allan Aasbjerg Nielsen, Paul Jacques Connetable, Henning Skriver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Based on the Cloude/van Zyl decomposition of reflection symmetric polarimetric SAR data we present a version for full/quad polarisation data. We demonstrate both versions on X-band F-SAR data over Vejers, Denmark. Differences between the original and our version of the decomposition occur especially for very bright man-made targets. These differences come with lower entropy for our version giving an improved focus on a more pronounced dominant scattering mechanism for these objects. Interpretation of the scattering mechanism related to the full/quad pol version of the decomposition is facilitated by means of the Cloude/Pottier $\bar{\alpha}$ angle.

---


### 203. [Learn, Freeze, and Transfer an Activation Function Across Architectures](https://arxiv.org/abs/2611.26201)

**<font color=#1a73e8>作者：</font>** Arun Prakash A  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning typically reuses knowledge acquired by a source network through its learned weights. We investigate whether a learned activation function can also be transferred and remain useful in networks trained from scratch. We study this complementary form of transfer through a learn-freeze-transfer protocol, in which the activation is optimized jointly with a source network in a single training run, and is then frozen and reused in target networks trained from scratch. A pointwise activation with globally shared parameters is independent of layer dimensions and can therefore be incorporated into networks of different architectures trained from scratch. We instantiate this protocol with FAct, a five-parameter activation represented by a two-harmonic truncated Fourier series, initialized from a Fourier approximation of GELU and learned in a Vision Transformer (ViT) on ImageNet-1K. When reused in a ViT of the same architecture trained from scratch on ImageNet-1K, the frozen activation (Frozen FAct) improves top-1 accuracy by 1.46 percentage points over GELU. Across four smaller target architectures (standard ViT, Swin Transformer, linear-attention ViT, and MLP-Mixer) and four image-classification datasets, it achieves the highest mean accuracy among eleven activation functions in 15 of 16 settings under a common training configuration, with improvements of up to 1.71 percentage points over the best conventional activation. When the learning rate and weight decay are tuned separately for each activation under the same search budget, Frozen FAct still ranks first in 11 of the 16 settings, second in four, and fourth in one. These results provide empirical evidence that a learned activation function can retain its usefulness when transferred across vision architectures, independently of the weights with which it was learned.

---


### 204. [SpecWM: Turning Verification into Refinement for Streaming World Models](https://arxiv.org/abs/2611.26211)

**<font color=#1a73e8>作者：</font>** Jiaming Li, Lingzhen Li, Xiaze Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference. Existing speculative methods combine their strengths through fast draft generation and selective target regeneration guided by rewards on decoded frames. However, verification covers only the external scorer's evaluation dimensions and adds decoding and scoring costs. Moreover, these scores provide no correction, requiring costly target regeneration for rejected drafts. To address these limitations, we propose Speculative World Model (SpecWM), a unified, training-free inference framework for streaming world models. It verifies draft chunks using the target's latent velocity field. Verification also yields a reusable correction; two thresholds select Accept, Refine, or Reject. Specifically, one-step refinement reuses it to improve perceptual quality, while three-step refinement strengthens camera following and trajectory consistency. These findings motivate transition-aware refinement. On WBench Navigation, SpecWM improves visual quality at 1.63$\times$ speedup over the target and raises NavScore from the draft's 75.99 to 85.63, achieving the best quality-speed-control trade-off. Additionally, our LongSpecBench shows sustained quality and control over long, multi-turn rollouts, while experiments on Hy-Nomas validate SpecWM across backbones and denoising budgets.

---


### 205. [MixReact: Physics-Based Reactive Humanoid Control from Multimodal Cues via a Discrete-Continuous Mixture of Transformers](https://arxiv.org/abs/2611.26218)

**<font color=#1a73e8>作者：</font>** Bin Li, Xing Zhu, Jingya Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humanoid agents in everyday environments are expected to react to diverse cues as humans do, with semantically appropriate and physically executable behaviors. Existing cue-driven reaction generation methods support only a narrow range of cue modalities and are limited to purely kinematic generation, leaving the resulting reactions susceptible to physical artifacts. To this end, we present MixReact, the first unified framework for physics-based reactive humanoid control from text, audio, and video cues, integrating a Discrete--Continuous Mixture of Transformers (DisCo-MoT) for state prediction with a History-aware Action Transformer (HAT) for physical execution. DisCo-MoT couples a discrete masked-modeling branch with a continuous autoregressive diffusion branch via one-way mixture attention within a MoT architecture. Guidance from discrete context mitigates collapse into averaged behaviors in one-to-many reaction generation, while direct prediction in continuous state space bypasses the decoding bottleneck of discrete representations. HAT then maps the predicted next state and observed execution history to executable actions, enabling robust closed-loop control in physics-based simulation. Experiments across all three modalities demonstrate consistent improvements over the baselines in fidelity, diversity, and physical consistency, while ablations validate the complementary contributions of the components. Our code will be released to facilitate future research. Project page: this https URL

---


### 206. [Attention Head Specialization: Phase Transitions in Sample Complexity](https://arxiv.org/abs/2611.26228)

**<font color=#1a73e8>作者：</font>** Léo Catteau, O. Duranthon, Lenka Zdeborová  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention heads specialize into distinct functions during training, often emerging in stages together with sharp changes in model behavior. While this phenomenon has mostly been studied as a function of training time, we ask how head specialization depends on the amount of available training data. Empirically, we find that heads specialized to syntactic relations in BERT emerge as the dataset size increases. We then study this phenomenon in a solvable high-dimensional model of multi-head attention and establish that, in this model, head specialization is a genuine phase transition in sample complexity, corresponding to a non-analyticity in the test error and other observables. Depending on data structure and regularization, specialization can follow uninformative head differentiation or occur through a cascade of phase transitions that progressively recover weaker latent features, providing a statistical form of simplicity bias. Finally, we relate these statistical transitions to the stagewise emergence of specialized heads during online learning, disentangling statistical from dynamical origins of head specialization.

---


### 207. [Time Series Structure Learning with Local Causal Parent Discovery](https://arxiv.org/abs/2611.26232)

**<font color=#1a73e8>作者：</font>** Jacqueline Maasch, Shu Wan, Hank Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning and inference on time series can pose significant statistical challenges, including autocorrelated observations, distribution shift over time, and the curse of dimensionality. These challenges complicate the practical application of causal discovery algorithms, which already suffer from high computational and sample complexity in the general case. To mitigate these issues, this work introduces Iterative Temporal Parent Discovery (ITPD): a sound and complete constraint-based procedure for causal structure learning on multivariate time series with causal nonstationarity. ITPD takes a local-to-global learning approach that discovers the global graph by sequentially discovering the parent set for each variable. ITPD exploits temporal structural priors, graph partitioning, and the local Markov condition to swap higher-order conditional independence tests for lower-order alternatives. With an exact oracle, ITPD performed the least number of tests and used the smallest average conditioning set sizes relative to baselines. In benchmarking simulations, ITPD sat on the Pareto frontier with respect to F1 and wall-clock time and was faster than baselines on large graphs ($\geq$ 1000 nodes). For graphs with 2000 nodes, ITPD ran $2.3\times$, $9.1\times$, and $40.9\times$ faster than iterative IAMB, DF-PC, and PCMCI, respectively.

---


### 208. [Attention Drift Regularization with Adaptive Initialization for Domain-Robust Visual Recognition](https://arxiv.org/abs/2611.26234)

**<font color=#1a73e8>作者：</font>** Shivangi Rai, Vinod K Kurmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-free domain adaptation (SFDA) adapts a pretrained source model to unlabeled target domains without source data access, yet two critical failure modes remain unaddressed. First, attention drift: source-learned attention maps shift toward spurious or background features under distribution shift, destabilizing feature representations. Second, domain-gap-agnostic initialization: applying a single fixed source model uniformly across all target domains ignores domain gap severity, causing premature overfitting to noisy pseudo-labels under large shifts. We propose DGA-CAFC to address both failures. The Counterfactual Attention-based Feature Consistency (CAFC) module enforces feature stability by minimizing the discrepancy between representations computed under learned attention and those under counterfactual-inspired normalized perturbations, thereby promoting domain-robust features independent of spurious attention shifts. The Domain-Gap Aware Source Model Selection (DGASS) module estimates domain gap severity via target prediction entropy and selects the source model variant whose confidence level best matches the estimated gap, reducing negative transfer and stabilizing pseudo-label quality. Crucially, CAFC transfers beyond SFDA: applied as a lightweight regularizer to standard domain generalization objectives without target data. Extensive experiments across SFDA and DG benchmarks demonstrate that our method consistently improves over recent baselines, demonstrating the effectiveness and generality of the proposed framework. Project page is available at this https URL

---


### 209. [Beyond Covers and Titles: Evidence-First Ranking for Robust Cold-Start Recommendation](https://arxiv.org/abs/2611.26249)

**<font color=#1a73e8>作者：</font>** Fuyi Wang, Yuxin Cao, Yifan Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-video platforms rank new uploads before anyone has watched them, using content towers that read a video's cover, title and frames. Existing attacks on content-aware recommenders perturb pixels or features and ignore platform re-encoding, and existing defenses train against norm-bounded perturbations that neither match real edits nor preserve recommendation quality. We show with REAP, a realizable attack through {a simulated platform channel (H.264 transcoding, rescaling, cropping and JPEG)}, that packaging edits raise a cold video by 32.0 rank-percentile points in unrelated audiences. We then observe that cold-start ranking does not need the packaging at all: a tower that sees only the video body ranks cold items best. Building on this, we propose Evidence-First Ranking (EFR), which scores cold videos from their body, admits packaging only through a support-gated residual bounded by $\gamma$, and merges cold and warm rankings by rank percentile, yielding an exact certificate against any packaging edit. On MicroLens-100K, EFR cuts the attack gain by 81% and raises cold-start Recall@100 from 0.1133 to 0.170, while keeping the merged NDCG@10 within 4% of the undefended system.

---


### 210. [The Stability Gap in Continual Reinforcement Learning](https://arxiv.org/abs/2611.26252)

**<font color=#1a73e8>作者：</font>** Sebastian Pusch, Matthia Sabatelli, Gido M. van de Ven  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual reinforcement learning (CRL) aims to enable agents to adapt to changing tasks while preserving previously acquired capabilities. Evaluation often relies on final aggregate metrics that can hide temporary performance degradation during adaptation. This work introduces a simple CRL benchmark that varies observation representations while preserving environment dynamics and rewards, supporting proof-of-concept demonstrations, inexpensive experimentation, and easily reproducible sanity checks. Using this benchmark, we demonstrate the stability gap in CRL: a substantial drop in prior-task performance after the introduction of new tasks, followed by partial or complete recovery. This pattern occurs despite the agent having complete access to past tasks.

---


### 211. [Prism: Hierarchical Text Detection with Minimalist Design](https://arxiv.org/abs/2611.26254)

**<font color=#1a73e8>作者：</font>** Yuchen Su, Xuesheng Wang, Zhilong Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hierarchical text detection aims to localize words, text lines, and paragraphs while parsing their structural relationships. It provides essential structural cues for visual text understanding. To maximize accuracy, existing methods typically rely on complex multi-scale feature fusion necks and heavy-weight heads, resulting in bloated architectures and low inference efficiency. In this paper, we argue that a sufficiently pre-trained backbone can effectively replace these sophisticated external modules, while simple geometric inclusion suffices for hierarchical text structural parsing. Thus, we propose Prism, a minimalist framework for hierarchical text detection. Prism performs multi-granularity detection by attaching parallel lightweight heads to a single-scale backbone feature map, covering words, text lines, and paragraphs, and reconstructs the structural hierarchy via an efficient geometric inclusion algorithm. In addition, we systematically compare representative lightweight head archetypes and show that pixel-level regression offers the best accuracy-efficiency trade-off in this setting. Experiments on multiple public benchmarks show that our significantly simplified architecture achieves state-of-the-art (SOTA) performance with remarkable efficiency. Specifically, it runs $1.7\times$ faster than LRANet on CTW1500 while achieving higher accuracy, and surpasses the current SOTA method, OmniParser V2, by over 6 PQ points on the hierarchical HierText dataset. Code will be released soon.

---


### 212. [STAGE: Spatio-Temporal Augmented Graph Expansion for Weakly Supervised Cross-Tweet Event Causality Discovery](https://arxiv.org/abs/2611.26255)

**<font color=#1a73e8>作者：</font>** Hieu Minh Duong, Todd Gary, Eugene Levin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal relations in disaster-related social media of- ten span independent posts, making cross-tweet causal discovery difficult to supervise and model at scale. We propose STAGE, a framework that separates scalable cross-tweet weak-supervision construction from spatio-temporal relational learning over event occurrences. Starting from local causal seeds, STAGE retrieves semantically related event occurrences across tweets and uses a causal scorer to construct weakly labeled cross-tweet pairs. These pairs supervise a multi-head Graph Attention Network over semantically enriched event representations and a spatio- temporal context graph. We evaluate STAGE on California Wildfire and Hurricane Harvey using human-gold cross-tweet test sets and 15 baselines. Compared with local-only supervision, the constructed cross-tweet supervision improves STAGE AUPRC by 0.340 on Wildfire and 0.107 on Hurricane. STAGE achieves in-domain AUROC of 0.885 on Wildfire and 0.710 on Hurricane. Cross-disaster experiments reveal asymmetric transfer, highlighting sensitivity to dataset-specific spatio-temporal shifts. These results demonstrate the value of scalable cross-tweet supervision combined with relational event modeling for causal learning across fragmented disaster reports.

---


### 213. [Similarity-based OSF Logic for Flexible SPARQL Query Answering](https://arxiv.org/abs/2611.26261)

**<font color=#1a73e8>作者：</font>** Gian Carlo Milanese, Gabriella Pasi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an updated version of fosf, a reasoner for fuzzy order-sorted feature (OSF) logic, with support for flexible SPARQL query answering over RDF knowledge graphs. Fuzzy OSF logic is a knowledge representation and reasoning language where feature symbols denote functions and sort symbols denote fuzzy sets. Sorts are organized in a fuzzy subsumption relation that extends to OSF terms, record-like structures representing classes of entities. The unification algorithm for these structures provides a calculus of fuzzy type subsumption. The latest release of fosf introduces support for similarity-based reasoning by extending the OSF language with a similarity relation among sorts, alongside a translation engine for compiling OSF terms into standard SPARQL. Queries expressed as OSF terms undergo fuzzy ontology-aware rewriting prior to translation. This process incorporates an OSF theory of sort definitions, feature domain and range declarations, and fuzzy subsumption and similarity relations through fuzzy OSF constraint normalization. This rewriting enables flexible query answering by returning approximate solutions, allowing queries that would otherwise be inconsistent with the underlying ontology to yield relevant results.

---


### 214. [Digitization of Analogue Gauges using Computer Vision](https://arxiv.org/abs/2611.26262)

**<font color=#1a73e8>作者：</font>** Erico Kayumba Mutonkole, Olasupo Ajayi, Omowunmi Isafiade  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analogue gauges remain prevalent in manufacturing industries for measuring physical quantities, yet manual monitoring by operators introduces human error and operational inefficiency. This research developed and evaluated an automated gauge reading system using computer vision and deep learning techniques. Three hybrid approaches were implemented and compared: OpenCV with Scikit-Image (traditional computer vision), OpenCV with ResNet18, and OpenCV with VGG19 (deep learning approaches). A comprehensive dataset of 1,848 pressure gauge images (0-10 BAR range) was curated through web scraping, synthetic generation, and augmentation techniques. The experimental results demonstrate that ResNet18 significantly outperforms the alternatives, achieving an accuracy of 97.3%, compared to VGG19's 64.4% and Scikit-Image's 63.8%. The study validates the effectiveness of residual learning architectures for industrial gauge digitization, providing a robust foundation for Industry 5.0 automation applications.

---


### 215. [Tracking Objects Through Assembly and Decomposition](https://arxiv.org/abs/2611.26269)

**<font color=#1a73e8>作者：</font>** Cheryl Lam, Yihong Sun, Bharath Hariharan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking objects through transformations is essential for understanding real-world dynamics. Recent work has extended traditional object tracking to detect state changes. However, existing methods require an initial object prompt and detect only its decompositions, missing assembly events, which begin with multiple objects rather than one. We therefore introduce a prompt-free formulation of this task, where the goal is to recover all object tracks and detect both decomposition and assembly events given only a video. Our key insight is that assembly is decomposition in reverse. Building on this insight, we present Atlas, a zero-shot system that constructs and jointly reasons over forward and reverse spatiotemporal partitions to recover object tracks and their transformations. We further introduce OmniST, a benchmark with dense annotations of objects and both transformation types. On OmniST, Atlas recovers more than twice as many state changes as prior methods while remaining competitive on existing benchmarks that only evaluate decomposition.

---


### 216. [BADAS-3.0: Real-Time Driving Perception and Planning from One Camera](https://arxiv.org/abs/2611.26294)

**<font color=#1a73e8>作者：</font>** Roni Goldshmidt, Hamish Scott, Lorenzo Niccolini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We ask how far a driving model can get with one camera and real-time latency. BADAS-3.0 is a 1B-parameter video encoder with four small heads. From two seconds of one forward camera, it predicts the current speed, the metric path just driven, a collision-risk score and six candidate futures over 6.4 seconds, in under 50 ms. Given the car's current speed, BADAS-3.0 has 44% lower minADE$_6$ over five trajectory benchmarks than the 34B Alpamayo 2 Super, which reads six cameras and runs over 100x slower. The gain comes from camera rigs that neither model was trained on. On the rig they share, the two are on par. Existing benchmarks are mostly nominal driving, so we add two open-loop safety benchmarks, one of real dashcam collisions and near-misses and one of Euro NCAP scenarios. On both, BADAS-3.0 has a higher pass rate than every published planner we tested.

---


### 217. [Language-Oriented Semantic Modeling for Target Language Extraction](https://arxiv.org/abs/2611.26317)

**<font color=#1a73e8>作者：</font>** Mehmet Sinan Yıldırım, Ke Zhang, Shuai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Target Language Extraction (TLE) aims to isolate speech in a target language from multilingual mixtures. Existing approaches primarily rely on acoustic modeling with language identity labels, which provide only coarse categorical guidance. In this work, we propose a language-oriented semantic modeling framework that augments acoustic extraction with language-specific semantic representations. A pre-trained speech semantic model is adapted via language-aware prompt conditioning and parameter-efficient fine-tuning to generate target-language-focused semantic representations from the mixture. {These capture high-level semantic structure of the acoustics and they} are integrated into the extraction model to provide structured semantic guidance beyond identity labels. Experiments on the CommonVoiceMix dataset show that incorporating semantic representations consistently improves over acoustic-only baselines, achieving up to 1.16 dB SI-SDR gain.

---


### 218. [A Control-Theoretic Approximation to Predictive Coding Dynamics](https://arxiv.org/abs/2611.26319)

**<font color=#1a73e8>作者：</font>** Ryan Fayyazi, Kyle Daruwalla, Mitra Javadzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation remains the dominant method for training deep neural networks, but its reliance on non-local computations has motivated the search for biologically plausible alternatives. Two prominent frameworks, predictive coding (PC) and deep feedback control (DFC), offer distinct approaches to local learning, yet their relationship remains unclear. Here, we show that DFC arises as a local approximation to predictive coding dynamics near fixed points, with exact equivalence in shallow linear networks and systematic deviations arising with depth, nonlinearity, and distance from equilibrium. We characterize how this approximation, which we call Approx PC, deviates from PC in its activity dynamics, and show that these deviations can be mitigated by relinearizing the feedback controller and approaching the output target through a sequence of intermediate nudges. In networks trained on MNIST and FashionMNIST, Approx PC reaches task performance comparable to PC trained with the same nudges, and weights learned with it transfer directly to PC inference. Our results unify energy-based and control-theoretic perspectives on learning and open the door to applying tools from control theory to the training of predictive coding networks.

---


### 219. [FirstCross: Convex Single-Photon 3D Reconstruction from Sparse Views](https://arxiv.org/abs/2611.26321)

**<font color=#1a73e8>作者：</font>** Chi-Wei Lee, Cheng-Han Chiang, Yi-Chun Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-photon lidar records the arrival time of each returning photon, enabling 3D reconstruction from few views and scarce photons. However, leading neural methods such as Transientangelo require over an hour of non-convex per-scene optimization, and their accuracy degrades as photon flux decreases. We propose FirstCross, a network-free approach that instead solves a short sequence of convex problems on a voxel grid. For a solid object, the Poisson likelihood of a ray with given signal and background rates depends on the scene solely through its first crossing, the point where the ray first enters the object. Decomposing this likelihood yields two tractable terms. The first penalizes surfaces in front of detected photons and admits a tight convex closure, namely volume rendering with a running-maximum transmittance in place of NeRF's product transmittance. The second accounts for photons that no surface explains and admits a convex upper bound once the object is assumed to be thick behind each detected surface point. Compared with Transientangelo under its own real-data protocol, FirstCross achieves lower depth error across every test scene, view count, and flux level. With three views and 100 times fewer photons than at the protocol's lowest flux, our mean object depth error stays under half of Transientangelo's with all photons. Given our detected surface points, the best classical fusion has 1.3 to 1.8 times our three-view error across flux levels. On real room-scale captures with 1% of their photons, TransientNeRF has 2.8 to 7.7 times our error. FirstCross lets few-view single-photon scanners cut exposure to 1% and reconstruct an object in about a minute on one GPU.

---


### 220. [Predicting Surface Displacement Fields of Laser Powder Bed Fusion Parts Using STL-Derived Graphs and Part-Level Descriptors](https://arxiv.org/abs/2611.26323)

**<font color=#1a73e8>作者：</font>** Saima Ahmed Suhi, Lang Yuan, Md Habibor Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting part distortion before fabrication remains challenging in laser powder bed fusion (LPBF), while thermomechanical simulation is computationally expensive for repeated design evaluations. This study presents a two-branch graph attention network (GAT) to predict three-dimensional surface displacement directly from STL-derived graphs. The first branch learns geometric relationships among connected vertices of a densified STL surface mesh, while the second incorporates 12 part-level descriptors of mass distribution, build-plate contact, overhang, size, and shape. Displacement labels from ANSYS Additive Print simulations are mapped onto STL vertices using Gaussian-kernel weighted averaging. Evaluated on 117 parts using five-fold cross-validation split by part, the model achieves an R^2 of 0.946 and a mean absolute error of 0.0178 mm for displacement magnitude. Relative to a node-wise multilayer perceptron, GAT improves R^2 from 0.913 to 0.946; for build-direction displacement, R^2 increases from 0.903 to 0.939. GAT also outperforms GraphSAGE (R^2 = 0.936) and a graph convolutional network (R^2 = 0.934) across all five folds. Ablation experiments show that removing mass-distribution descriptors reduces magnitude R^2 to 0.900, while removing build-plate contact and overhang descriptors reduces it to 0.920. These results demonstrate the value of combining local mesh connectivity with global geometric descriptors to predict LPBF distortion, enabling faster design iteration and earlier identification of distortion-prone geometries.

---


### 221. [Context as a Resource](https://arxiv.org/abs/2611.26346)

**<font color=#1a73e8>作者：</font>** Xufei Tian, Han Hu, Wenli Du  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Managing concurrent tasks across separate agent sessions quickly exhausts human attention, motivating always-on personal agents behind a single continuous interface. Yet when every context shares identical frozen backbone weights, funneling interleaved dialogues and external events into one linear session induces cross-topic constraint bleed and head-of-line stalling. Conversely, router-ticket hierarchies incur lossy prose handoffs, heavy routing overhead, and blind merges - collapsing true-conflict repository merges to a 33.3% three-run mean despite high isolated branch passes. Rather than scheduling anthropomorphic roles, we introduce ClonAct, a routerless architecture that virtualizes context blocks directly through a pluggable single-pass non-generative Context MMU, in-place Context Cells, a footprint-aware Synaptic Bus with an isolated trial merge gate, and a wave-flushed Shared Trunk. Across three programmatic multi-stream benchmarks and three model families, our portable trial merge gate lifts true-conflict merges to 63.3%, while ClonAct's routerless virtualization attains this ceiling with 45.9% fewer prompt tokens and prevents compact-model router collapse. Under continuous surge streams, ClonAct matches top completion (95.0%) with the lowest median wait and zero timed-out status checks.

---


### 222. [OffBeat: Multicoset Sampling for 4D Capture Beyond the Camera Frame Rate](https://arxiv.org/abs/2611.26347)

**<font color=#1a73e8>作者：</font>** Chi-Wei Lee, An-Kai Chen, Cheng-Han Chiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For 4D reconstruction, a synchronized multi-camera rig records all views at the same timestamps and misses the motion between them. Staggered triggers spread the same frames over more timestamps. However, when the cameras along each row fire one after another, as in 4DSloMo's schedule on the N3DV rig, the row acts as one moving camera that confounds depth with motion. We introduce OffBeat, which models a staggered rig as a spatially distributed multicoset sampler: shifted copies of one sampling grid. From the calibration alone, OffBeat derives camera groups that fire together and their firing order. Since one group records each timestamp, a short-lived primitive can fit an error its cameras share, such as a color offset, and flicker in novel views. We show that a primitive's opacity over time weights all groups equally, for every number of groups, only if it lasts at least one camera frame interval. On Spacetime Gaussians, a minimum lifetime approximates this bound, and a closed-form smoothed box of that length satisfies it exactly, with less flicker than a Gaussian in its place at nearly equal PSNR. In simulated staggered capture on N3DV, OffBeat outperforms the full 4DSloMo pipeline with video diffusion on every test frame, by 3.04 dB in mean dynamic-region PSNR. Between the first and last synchronized frame, it outperforms the best synchronized method of each scene, with or without frame interpolation, by 1.98 dB in mean dynamic-region PSNR, while synchronized capture is better at its own frames. On PanopticSports, in this frame range, OffBeat is comparable in PSNR to synchronized capture with interpolation. On every N3DV scene, replacing 4DSloMo's schedule with ours raises the dynamic-region PSNR of Spacetime Gaussians, 4DSloMo without diffusion, and our reconstruction. Multi-camera rigs could follow faster motion at the same frame count by changing only when each camera fires.

---


### 223. [TRCF: Temporal-Reference Complementary Forecasting for Irregular Multivariate Time Series](https://arxiv.org/abs/2611.26351)

**<font color=#1a73e8>作者：</font>** Xudong Zuo, Shusen Ma, Qirui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular multivariate time series forecasting supports healthcare monitoring, environmental analysis, and activity recognition. Channel-independent (CI) approaches capture each variable's temporal patterns but do not explicitly use observations from other variables. Channel-dependent (CD) modeling exploits relationships among variables, yet asynchronous measurements make these relationships difficult to learn. Incorporating cross-variable information while preserving each variable's irregular history therefore remains a key challenge. We propose Temporal-Reference Complementary Forecasting (TRCF), a framework that augments a compact CI forecaster with a complementary CD branch. ANCHOR aggregates observed values and timestamps at shared temporal locations, retaining observation support to form compact CI features. BRIDGE constructs complementary features through history completion. It first estimates each variable's historical values from its own observations, then uses differences between other variables' observed and estimated values at nearby times to correct missing entries. The completed history preserves observed values and is encoded to supply context alongside the direct CI representation. Finally, the two representations are fused, combined with the query-time embedding, and passed to a shallow multilayer perceptron for forecasting. Experiments on four real-world datasets show that TRCF achieves the lowest mean squared error and mean absolute error in the main benchmark comparison, while reducing measured peak inference memory by 17.28% to 87.98% relative to APN.

---


### 224. [Mamba Flow Matching Neural Processes: Linear-Time Inference for Irregularly Observed Spatial Fields](https://arxiv.org/abs/2611.26355)

**<font color=#1a73e8>作者：</font>** Cosmo Santoni, Giovanni Charles, Timothy James Hitge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpolating a spatial field, such as daily maximum temperature, from sparse, irregularly located observations recurs across the environmental and health sciences. Standard Gaussian-process kriging refits hyperparameters and solves an $O(N^3)$ system for every new field. When many related fields are observed, such as daily maps from one sensor network, neural processes (NPs) instead learn the interpolation map from past fields and predict a new field in one forward pass. Joint-predictive variants, which sample whole fields rather than independent per-location values, typically use self-attention over context and query points, costing $O(K^2)$ in the combined point count $K$ and limiting practical use to a few thousand points. State-space models offer a linear-time alternative, but a direct state-space adaptation compresses the context into one hidden state before reading queries, reducing what the decoder sees. We propose MambaFlowNP, a linear-compute joint-predictive NP trained with conditional flow matching. A multi-directional Mamba-2 scan reads context and query tokens in one shared sequence, so each query's velocity is read from its own scan position rather than a compressed context summary, and because queries only read the scan state, predictions are consistent across query sets. MambaFlowNP is competitive with the strongest attention-based joint-predictive baselines on synthetic Matérn Gaussian-process benchmarks, and on regional to continental-scale NOAA temperature interpolation it attains the lowest RMSE and CRPS and near-nominal coverage on every tier, while running 114--784$\times$ faster than the strongest joint-predictive baseline. A single forward pass scales to $10^6$ points on one NVIDIA L40S GPU in under a second. This makes joint prediction feasible for continental-scale, irregularly sampled sensor networks; predictive quality is evaluated up to $K=5{,}580$.

---


### 225. [Learning from Context: Leave-One-Out Prediction in Jump Diffusions](https://arxiv.org/abs/2611.26359)

**<font color=#1a73e8>作者：</font>** Christian Wald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion models generate discrete data through stochastic dynamics in an embedding space. We consider jump diffusions that additionally reset coordinates to embeddings of categorical values. A coordinate's own corrupted state can make prediction easy, potentially reducing the pressure to learn dependencies between coordinates. We study leave-one-out (LOO) prediction, in which each coordinate is predicted from the corrupted states of the other coordinates. We show that, under stated assumptions, jump diffusions with complete coordinate resets and state-independent clocks preserve the prescribed marginals when reset destinations use exact LOO probabilities and the drift uses the full endpoint posterior. We further show that this drift can be constructed from LOO probabilities by analytic likelihood completion without additional network evaluations. We evaluate unrestricted, LOO, and completed predictions on Text8 and LM1B text generation and ZINC250k molecular graph generation. LOO-based variants improve key generation metrics over matched unrestricted controls on all three datasets. Controlled interventions assess reliance on local inputs and context, and we analyze the effect of analytic likelihood completion.

---


### 226. [World Models Favor Learned Priors over Visual Evidence](https://arxiv.org/abs/2611.26366)

**<font color=#1a73e8>作者：</font>** Han Xiao, Zhiyong Bao, Xiaotong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used to simulate physical interactions, but training a separate model for each environment limits scalability. Cross-environment prediction requires identifying the current physical rule, which appearance alone may not reveal. We therefore study visual calibration: using object motion and interactions in a short video as direct evidence to infer the current rule and predict motion under that rule from a different initial state. However, differences in data availability across physical conditions can yield a long-tailed training distribution, biasing models toward common rules even when evidence supports rare ones. To study this challenge, we introduce TailWorld, which evaluates the transfer of demonstrated rules across initial states while independently controlling training imbalance and calibration informativeness. The benchmark compares predictions with two reference futures from the same prediction initial state, one following the demonstrated rule and the other a common rule, to measure prediction bias toward common dynamics. We further propose Rule Inference for Transfer (RIFT), which learns how different rules affect object motion, infers the current rule from calibration interactions, and applies it to prediction from a new initial state. RIFT explicitly controls the influence of training frequency on rule inference, allowing sufficiently informative observational evidence to support rare rules. Experiments on TailWorld show that RIFT improves prediction accuracy and physical consistency across varying training imbalances and distribution shifts, with gains in predicting rare dynamics.

---


### 227. [Contactless Estimation of Respiratory Frequency Using 3D-CNN on Thermal Images](https://arxiv.org/abs/2611.26367)

**<font color=#1a73e8>作者：</font>** Federica Gioia, Filippo Pura, Alberto Greco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring physiological parameters such as respiratory rate ($f_R$) is essential for diagnosing and managing various pathological conditions. Thermal imaging offers a promising contactless alternative to traditional methods, which often rely on partially invasive sensors or obtrusive wearable systems. However, existing approaches for $f_R$ estimation from thermal signals typically require extensive pre-processing and manual or semi-automatic region-of-interest (ROI) tracking, limiting their practical applicability. This study proposes a deep learning-based method for estimating $f_R$ directly from thermal videos, eliminating the need for complex pre-processing and ROI tracking. A 3D Convolutional Neural Network (3D-CNN) is developed to operate on raw thermal video data. To address challenges related to small datasets, the model is trained using data augmentation and transfer learning from synthetic datasets. Experimental results demonstrate that the proposed approach achieves a validation $R^2$ score of approximately 0.61 on both pre-processed and raw thermal videos. By simplifying the workflow, this method holds promise for enhancing the feasibility of thermal imaging in real-world applications, such as remote healthcare and driver monitoring in automotive applications.

---


### 228. [From Benchmarks to the Bench: Preference, Correspondence and Selectivity in Bidirectional Drug-Target Screening](https://arxiv.org/abs/2611.26369)

**<font color=#1a73e8>作者：</font>** Jiangjie Qiu, Chengrui Xu, Xiaonan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying active molecules for known targets and potential targets for existing drugs is central to drug discovery and repurposing. Drug-target interaction (DTI) models can rank vast numbers of drug-target pairs, but limited experimental capacity restricts testing to a small number of candidates. We compared the bidirectional recommendations of 13 released systems across 711 molecular structures of FDA-approved drugs and 614 human proteins. For the same target or drug, pairs of models produced completely disjoint Top-10 molecule and protein lists in 77.8% and 70.1% of comparisons, respectively. Even where recommendations overlapped, agreement between some systems largely reflected recurring preferences for the same candidates. Published inhibition measurements for 79 molecules and 65 kinases revealed that some systems enriched active candidates, yet their hit yields changed little when recommendations were matched to different drugs or targets, whereas other systems lost substantially more hits. Some of the former systems also rarely ranked both molecules and kinases correctly when two drugs favoured different kinases. We further retrained the same architecture on the same data, with the training objective fixed and random seeds varied. Despite similar test performance, mean pairwise Top-10 overlap on a separate screening catalogue was about two candidates. Our study moves DTI model evaluation beyond benchmark performance to assess whether model predictions can guide meaningful experimental decisions in drug discovery and target identification.

---


### 229. [Fast Self-Supervised Generative CT Denoising via Few-Step Sampling](https://arxiv.org/abs/2611.26370)

**<font color=#1a73e8>作者：</font>** Xingyi Yao, Zhengtao Ma, Zhennong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-dose and thin-slice computed tomography (CT) images suffer from elevated noise that obscures anatomical detail, while clean references for supervised denoising are often unavailable. Although Noise2Noise permits self-supervised training from noisy pairs, direct regression tends to oversmooth fine structure. Averaging multiple independently generated samples mitigates this blur, though repeating multi-step diffusion sampling is costly. We introduce Noise2Noise with Improved Mean Flow (N2N-iMF) to accelerate this process via few-step sampling. N2N-iMF learns to generate one noisy image conditioned on its paired counterpart; at inference, independent outputs are sampled and averaged to suppress noise. We evaluated image quality and sampling efficiency on simulated thin-slice brain and low-dose abdominal CT across four sampling methods and averaging counts from 1 to 20, and validated the approach on real-world photon-counting CT (PCCT) brain scans. With ten samples per conditioning input and three network evaluations per sample, N2N-iMF achieved a mean absolute error of 2.60 HU on brain CT and 14.02 HU on abdominal CT, outperforming 50-evaluation denoising diffusion implicit model (DDIM) sampling (2.91 and 14.53 HU). On the same GPU, per-output generation time dropped from 7.29 to 0.43 s. Across eight PCCT cases, N2N-iMF reached a mean gray-white matter contrast-to-noise ratio of 1.341, versus 0.916 for Noise2Noise and 1.176 for DDIM. N2N-iMF accelerates self-supervised generative CT denoising without distillation while keeping the number of averaged outputs adjustable at inference.

---


### 230. [Evidence from a Multi-Regime Causal Discovery Benchmark: UCMT Algorithms, Comparative Performance, and Controlled Ablation Studies](https://arxiv.org/abs/2611.26383)

**<font color=#1a73e8>作者：</font>** Mahyar Eslami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an internal, pre-registered evaluation of the UCMT causal discovery algorithm family alongside established alternatives across heterogeneous benchmark regimes, complemented by a separately pre-registered, controlled study of UCMT v2 Global components. The contribution is both empirical and methodological: a family-stratified comparison of three actively developed algorithm configurations and targeted evidence about which internal stages affect their outcomes. In the main benchmark, UCMT v2 Global has higher directed F1 than NOTEARS and DAGMA in selected real, semi-synthetic and Gaussian-network comparisons at the paired-run level, while trailing leading permutation-search methods in other settings. The BOSS-based UCMT v4 produces a CSuite-specific directed-F1 improvement over BOSS (mean paired difference +0.279; pair-level Holm p < 0.001), but the dataset-level adjusted result is not significant (p = 0.188). In a separate fixed-skeleton ablation, UCMT v2 Global exceeds an adapted R^2-SortnRegress orientation baseline on standardized iSCM data (directed F1 0.537 vs 0.468, dataset-level Holm p = 0.031); absolute orientation accuracy is 0.563 and there is no established broad advantage over RESIT, ANM or DirectLiNGAM. Controlled ablations show that sparsity and BIC-based refinement materially affect some outcomes, whereas the examined arbitration and automatic regime-selection mechanisms do not yield confirmed general improvements. We report performance shortcomings, multiple-testing correction, runtime costs, evaluation limitations and reproducibility checks. The results support UCMT as an implemented and empirically investigated algorithm family, not a claim of overall superiority, independent validation or demonstrated commercial impact.

---


### 231. [A Complete Geometric Message-Passing Architecture for Point Clouds](https://arxiv.org/abs/2611.26384)

**<font color=#1a73e8>作者：</font>** Nadav Dym, Tal Amir, Gia Chi Dang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Three-dimensional point clouds are a fundamental data modality, and a large family of machine learning architectures has been developed to respect their natural symmetries to rigid motions and permutations. A principled way to compare these architectures, which vary widely in complexity and cost, is through their expressive power. That is, an architecture is complete if it can distinguish any two inputs not related by the symmetries it respects. Simple distance-based message-passing networks are known to be incomplete, and while there exist complete alternatives, they typically rely on computationally intensive mechanisms like high-order representations of the rotation group or higher-order Weisfeiler-Leman-type tests.
In this work, we devise a novel, simple, equivariant message-passing architecture for point clouds, and prove that it is complete. We complement our theoretical result with experiments showing that our architecture separates challenging point clouds that distance-based message passing provably cannot distinguish. Our results suggest that high-order equivariant features may not be necessary to enhance the expressivity of point cloud architectures, and can help settle completeness for other equivariant architectures for which such results are currently unknown. We give initial evidence for this by proving completeness of a slightly modified version of SEGNN.

---


### 232. [SEEC: A Large-Scale Dataset and Benchmark for Self-Supervised External-Eye Representation Learning](https://arxiv.org/abs/2611.26386)

**<font color=#1a73e8>作者：</font>** George R. Nahass, Michelle Fleishaker, Sanjay Ganesh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> External-eye photography captures clinically relevant periocular anatomy at low acquisition cost, yet no large-scale standardized resource exists for evaluating self-supervised external-eye representations. We introduce a 4.35-million-image Standardized External-Eye Corpus (SEEC) derived from fourteen heterogeneous public face datasets, together with a benchmark for external-eye representation learning. For evaluation, we provide held-out evaluation distributions, landmark-annotated anatomical probe sets, and clinical disease-classification experiments spanning ptosis, thyroid eye disease, and craniofacial syndromes. We evaluate representations at two complementary levels: (a) the representation level, by assessing embedding geometry across multiple data distributions, and (b) the functional level, by assessing anatomical recovery, out-of-distribution anatomical transfer, and disease classification. Our models include ResNet-101 and ViT-B encoders pretrained using InfoNCE, VICReg, and LeJEPA objectives and compared with DINOv2 and MAE. Our results indicate that representation-level and functional-level evaluations are dissociable: broader embedding-space utilization does not consistently correspond to anatomical transfer or disease-classification performance, and no single encoder is universally optimal. Domain-specific external-eye encoders outperform DINOv2 and MAE on cross-dataset anatomical transfer despite being pretrained at substantially smaller scale, while external-eye-pretrained ViT models match or outperform these general-purpose baselines on frozen disease-classification probes. We release benchmark code, evaluation scripts, and preprocessing pipelines to reproduce SEEC at this https URL

---


### 233. [GateTrace: Where Do Crowd Crossings Go Missing Under Occlusion?](https://arxiv.org/abs/2611.26388)

**<font color=#1a73e8>作者：</font>** Ao He, Qianchen Yu, Vivian W. H. Wong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> At large events, pedestrian tracking supports entrance and passageway counts, but totals hide which crossings were missed. In a stadium study, the system recorded about four in five clearly visible crossings but fewer than one in three mostly obscured crossings. The videos lacked trajectories annotated across frames, so we turned to MOT20, which provides pedestrian trajectories and visibility. We introduce GateTrace to locate missed crossings and assess changes to counting rules. It derives reference crossings from annotations under fixed rules, matches reports by person, direction, time and position, and traces misses through saved boxes and counting decisions. With a shared detector, ByteTrack, OC-SORT and BoT-SORT recover 38.9-46.7% of low-visibility reference crossings on development sequences, versus 98.1-99.0% at high visibility. The gap recurs on two further sequences under a protocol fixed in advance. Published outputs of MOT20-tuned BASE recover 63-78% at low visibility across both sequence groups. Losses stop at different stages across systems. Across four systems and both groups, 47-79% of low-visibility misses have no nearby output linked to the person or no possible crossing in the saved tracks. Removing later checks from BASE on development sequences leaves most misses unresolved and lowers precision against the fixed reference list from about 96% to 77%. Misses also remain among sampled reference crossings that two human annotators supported after checking the videos. GateTrace shows where crossings are lost and measures the recovery and precision costs of changing later checks. We will release the code and per-crossing records.

---


### 234. [ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step](https://arxiv.org/abs/2611.26389)

**<font color=#1a73e8>作者：</font>** Kaiwen Zhang, Yiming Gao, Zeqi Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of decisions. We present ViDecide, a decision-centric framework that trains video diffusion models to predict state transitions causally and decide when to stop, with a decision-focused training schedule. We further propose Corrective Fine-tuning (CFT), which corrects failed decisions by mapping their noise to the model's own successful continuations, achieving stable improvement without policy-gradient optimization. Across abstract games, planning tasks, and a new benchmark of multi-step robot planning, ViDecide achieves an average strict success rate of 83.8%, far above 23.3% for standard fine-tuning and 67.8% for the strongest prior method, and generalizes to larger puzzles and unseen layouts. Our framework therefore unlocks greater potential for video generation models as reliable reasoners and planners in the visual world. Project page: this https URL.

---


### 235. [Rethinking Utility in Differentially Private Visualization: A Channel-Centric Perspective](https://arxiv.org/abs/2611.26396)

**<font color=#1a73e8>作者：</font>** Jing Yang, Sarayu Pacca, Zhaocong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) is increasingly adopted to protect sensitive data in visualization, but understanding how privacy-induced noise affects visual representations remains fragmented. Prior work has examined the impact of DP noise on specific chart types, yet these findings are typically tied to particular chart types and evaluation settings, making it difficult to generalize across contexts. In parallel, visualization research has long established that visual channels, the visual properties of marks that encode data attributes, differ in perceptual effectiveness under noise-free conditions. However, these principles have not been systematically revisited under DP, where noise is deliberately introduced into the data to protect privacy. In this paper, we present a channel-centric perspective to reframe prior empirical and theoretical results. Our synthesis drawson prior findings to motivate a channel-read-mechanism hypothesis: the utility of DP visualizations may depend on the task-relevant reads made salient by visual channel configurations and DP mechanism choice jointly. Moreover, this perspective highlights the role of channel choice throughout the privacy-preserving visualization pipeline, from disclosure framing and DP algorithm design to utility evaluation and interpretation of noisy outputs. The synthesis also identifies gaps in the existing evaluation literature and highlights research opportunities for channel-aware DP visualization.

---


### 236. [FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities](https://arxiv.org/abs/2611.26419)

**<font color=#1a73e8>作者：</font>** Bassam El Said, Adam Sobey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Each fibre-reinforced composite structure has a unique material architecture. The manufacturing methods used and the presence of defects lead to local variations which require material-scale models that can resolve the response in real time at every location in the structure. Concurrent multi-scale schemes provide this capability, but at a prohibitive computational cost for large structures as the number of integration points and time increments scales with size. Surrogates have been studied extensively as replacements for material-scale models to mitigate these computational limitations. A surrogate must represent an arbitrary local architecture including defects, track the irreversible material state over an unknown number of increments, remain stable when driven recursively by its own predictions, and fit within the memory available at every integration point. Here, a Composites World Model based on a Multi-Modal Spiking Transformer architecture is designed to meet these requirements. The proposed architecture combines a material encoder, a Spiking Neural Network memory block that tracks the long-term internal state of the material, and transformer blocks that learn the short-term applied strain state. The system is trained in three stages: material architecture encoding, base training on short time windows, and recursive fine-tuning with scheduled sampling to suppress cumulative error drift. The trained model is disassembled at inference and coupled to a non-linear FE solver, enabling structural scale simulation of composites containing embedded defects. Benchmarks against experimental results for IM7/8552 laminates under tension, compression and transverse shear, for pristine and wrinkled composites, show that the SNN memory block successfully tracks the material internal state and results in prediction errors between 0.4% and 4.8%.

---


### 237. [FFGaussType: Feed-Forward Conversion of Glyph and SVG Geometry into Compact Gaussian Assets](https://arxiv.org/abs/2611.26431)

**<font color=#1a73e8>作者：</font>** Haoan Feng, Tianfu Wang, Peimeng Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immersive 3D content allows text and graphical elements, such as subtitles, annotations, and icons, to be placed inside a scene rather than displayed as flat overlays. Placed this way, they respect occlusion and perspective and take on user-assigned materials and lighting while preserving their original shapes. In Gaussian scenes, however, each new glyph or icon requires its own iterative optimization, which limits scalable content creation. We present FFGaussType, which converts extruded glyph and SVG outlines into Gaussian assets in a single forward pass. A point encoder maps anchors sampled on the known surface to a single feature plane, from which a decoder shared by all assets predicts neural Gaussians carrying surface normals. This separates geometric conversion from material and lighting choices, and the feature plane supports image and video coding for compact delivery. We construct a paired dataset of 27,221 glyph and SVG icon assets with anchors and calibrated normal and silhouette renderings, holding out font families for evaluation. Conversion from prepared anchors takes 9.1 ms per asset, at a fraction of the compute and memory of prior baselines. On unseen font families and test icons, FFGaussType achieves $1.62^\circ$ normal error and $0.985$ silhouette IoU, the best among the compared feed-forward converters, matching the fidelity that per-asset fitting needs thousands of steps to reach. The code and dataset will be released after publication.

---


### 238. [AdaPixFlow: Learning Continuous-Time 3D Dynamics Across Scenes from Sparse Multi-view Observations](https://arxiv.org/abs/2611.26433)

**<font color=#1a73e8>作者：</font>** Hrishikesh Viswanath, Aniket Bera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how objects move in dynamic scenes requires recovering their 3D motion from visual observations and predicting their positions at unobserved times. Existing methods either optimize scene-specific velocity fields or impose predefined physical and kinematic assumptions. We instead study learning a continuous-time dynamics operator across scenes, mapping multi-view visual observations to 3D object kinematics. We introduce Adaptive Pixel Flows (\ours{}), which learns this operator from multi-view RGB-D observations without per-scene optimization or predefined motion models. The method fuses observations from all cameras into a shared voxel grid in world coordinates, from which the network predicts a continuous-time velocity field. Because the operator is trained across scenes, it learns motion priors that carry over to unseen scenes. The field can then be integrated from observed states to predict object positions between observations and beyond the observed sequence. On held-out PhysInOne scenes, \ours{} improves F1 over the strongest competing method by 2.5\% for in-between prediction and 15\% for future prediction. Compared with per-scene velocity-field methods, the improvements are 30\% and 85\%, respectively. Applied zero-shot to Spring-Gaus, it improves future-prediction F1 by 12\%.

---


### 239. [HumanCOIN: A 12,500-Hour Dataset for Human Intent in Egocentric Manipulation](https://arxiv.org/abs/2611.26434)

**<font color=#1a73e8>作者：</font>** Shihan Wu, You Liu, Chunyu He 等 51 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> First-person manipulation datasets treat the observation-action pair as the atomic unit and compress the generation and execution of an action into a policy network's weights, rendering the intent state behind the action unobservable. Human motor control research shows that intent mediates between observation and action and leaves observable traces along the intent pathway from decision to effect: gaze reaches the target before the hand, muscle load builds before contact, and cortical activity precedes the motor command. To record this pathway at scale, we present HumanCOIN, a first-person manipulation dataset built around human intent: 12,500 hours across 38 scene classes with three tiers of proxies. At the output end, the L1 attention tier (10,000 h) infers gaze from headband camera video, exposing the operator's next object of attention and reach before the hand moves. Midway, the L2 exertion tier (2,000 h) records surface EMG from armbands, making load expectations readable before execution is complete. At the origin, the L3 cognition tier (500 h) records scalp EEG, giving early readouts of task decisions and monitoring. Each tier inherits all proxies from the tiers below. The dataset further provides multi-view RGB images, depth maps and point clouds, 6-DoF head and wrist pose, and step-level action and object annotations. The controlled L3 setting additionally measures gaze, hand pose and finger kinematics directly. Clock and calibration data are released with the dataset so that any read rate can be re-aligned. The three tiers cover three stations, from visual orienting to cortical preparation, making the process behind visual-action pairs available for modeling at dataset scale. Project page: this https URL.

---


### 240. [Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware](https://arxiv.org/abs/2611.26437)

**<font color=#1a73e8>作者：</font>** Víctor Rodrigo González, Pablo M. Olmos, Ignacio Peis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier text-to-image (T2I) foundation models predominantly rely on multi-billion parameter Diffusion Transformers (DiTs) pretrained across massive compute clusters, creating an accessibility barrier for academic laboratories. When training DiTs from scratch on single consumer GPUs (e.g., an NVIDIA RTX 4090 with 24\,GB VRAM), practitioners encounter three primary bottlenecks: quadratic attention sequence costs, Just-In-Time (JIT) compilation graph breaks induced by variable aspect-ratio bucketing, and an autoencoder throughput wall where frozen Variational Autoencoder (VAE) operations dominate step latency. In this work, we introduce \textbf{Asuka-FM}, an end-to-end system and architectural framework demonstrating that competitive dual-stream DiTs ($\sim$206M parameters) can be pretrained from scratch on a single consumer GPU in $\sim$160 GPU hours for under \$55. Asuka-FM integrates four core designs: (i) an AdaLN-free dual-stream DiT backbone reducing parameter count; (ii) structured sequence sparsification via Sparse-Dense Residual Fusion (SPRINT) to cut attention FLOPs by over 50\%; (iii) continuous aspect-normalized Rotary Position Embeddings (RoPE) coupled with shifted square crop training, guaranteeing static tensor shapes while unlocking zero-shot virtual camera control; and (iv) a pixel adaptation phase utilizing a lightweight (10M parameter) Patch Detailer Head operating under velocity regression ($v$-prediction). Evaluated on open-domain benchmarks without benchmark-specific fine-tuning, Asuka-FM achieves GenEval 0.588 / DPG 78.96 scores at 256px and GenEval 0.609 / DPG 78.51 scores at 512px, setting a new Pareto-optimal efficiency standard for democratic foundation modeling.

---


### 241. [Learning to Defer under Expert Drift](https://arxiv.org/abs/2611.26440)

**<font color=#1a73e8>作者：</font>** Ziyao Mou, Andrea Wynn, Eric Nalisnick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The learning to defer (L2D) framework enables safety in machine learning and AI systems by allocating difficult or critical decisions to a human expert. However, most prior work on L2D assumes fixed expert reliability, overlooking temporal fluctuations in human performance due to factors such as fatigue and cognitive biases. Humans commonly exhibit such substantial, systematic performance shifts across a wide range of domains, from high-stakes settings such as radiology, aviation, and judicial decision-making, to everyday tasks such as crowdsourced image annotation. We propose Expert-Drift-Adapted Learning-to-Defer (EDA-L2D), a novel expert-aware L2D framework that explicitly models these temporal shifts by conditioning the deferral head on recent histories of expert outcomes via a sequence model. This history-aware approach enables adaptive deferral policies that anticipate reliability fluctuations and better allocate decisions between human and machine over time. We provide comprehensive experiments across three diverse tasks -- image classification, medical diagnosis, and hate speech detection -- including generalization analyses under realistic deferral conditions and irregular shifts in expert reliability. Our results show that EDA-L2D adapts more effectively than prior L2D methods to diverse temporal patterns of expert reliability, resulting in improved system performance and more effective deferral decisions. Code is available at this https URL.

---


### 242. [Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific Guidance](https://arxiv.org/abs/2611.26456)

**<font color=#1a73e8>作者：</font>** Hongyu An, Fanghua Yu, Kainan Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image restoration have greatly improved global image fidelity, producing visually plausible results across most regions of an image. Nevertheless, even high-quality restorations often exhibit localized failures, including artifacts in semantically important regions such as faces and text, structural inconsistencies, and texture mismatches. Although these errors typically affect only a small portion of the image, they often dominate the overall perceptual quality of the result. In this work, we propose Failure-Aware Image Restoration (FAIR) to address the "last-mile" problem in image restoration. Rather than applying one uniform generative prior over the whole image, we condition a single-pass restoration model on both where local failures are likely to occur and what corrective guidance each region requires. This region-bound conditioning enables fine-grained and controllable restoration that improves semantic accuracy and stylistic consistency in critical regions while maintaining faithful, high-quality restoration elsewhere. Our method complements existing restoration pipelines by shifting the emphasis from global fidelity to local perceptual acceptability. Extensive experiments show that the proposed approach resolves common failure cases and improves perceptual quality, bridging the gap between technical accuracy and practical usability.

---


### 243. [Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential Uncertainty Quantification for Nonlinear Dynamics](https://arxiv.org/abs/2611.26463)

**<font color=#1a73e8>作者：</font>** Chuanqi Chen, Nan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensive and often relies on an explicit dynamical model. In this paper, we develop the Neural Conditional Gaussian Model (Neural CGM), a data-driven dynamical model that maps unobserved physical states into a learned latent space, where the dynamics of the latent states follow a conditional Gaussian structure. This structure allows closed-form DA updates in the latent space, while nonlinear encoder-decoder mappings retain the flexibility needed to represent complex dynamics in physical space. A key feature of Neural CGM is its treatment of uncertainty in DA. The latent posterior mean and covariance are mapped to the physical variables through a Gaussian decoder that combines local moment propagation with learned nonlinear corrections. The resulting physical-space posterior statistics depend on the sequentially updated latent distribution rather than on a separate post-processing estimate. The same statistics enter a Gaussian negative log-likelihood during training, so both the posterior mean and uncertainty affect the learned model. Because Neural CGM learns the dynamical model itself, it can also be used for state forecasting and simulation without explicit knowledge of the governing equations. Numerical experiments on benchmark nonlinear dynamical systems show accurate state estimation and forecasting while substantially reducing online assimilation cost relative to conventional nonlinear DA methods. Neural CGM is therefore suited to repeated state estimation, uncertainty quantification, and prediction from partial observations.

---


### 244. [Monte Carlo Pass Search for Setpieces](https://arxiv.org/abs/2611.26464)

**<font color=#1a73e8>作者：</font>** Andrew Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Set pieces produce about a third of non-penalty expected goals (xG), yet they are usually evaluated by what happened next. We present Monte Carlo Pass Search (MCPS) for set pieces, which treats a corner or a lofted free kick as a distribution over plausible executions and plausible futures instead of a single realised event. From the pre-kick state, MCPS proposes counterfactual deliveries and counterfactual set-ups (where the attackers stand at the kick), plays each out many times in a world model (3D ball physics, a generative model of all 22 players, the keeper's come-or-stay decision and a Player-to-Touch model) and scores every future with a value model. On 249 deliveries from 30 Serie A 2025/26 matches, with every model applied only to matches it never saw, the best available delivery is worth 0.0085 xG more than the one kicked (+28 %), mainly because it reaches an attacker before the keeper. Searching where the attackers stand as well adds +0.0027 xG with the observed ball and +0.0033 on top of the best ball; designing their runs too adds +0.0007 more. We show how to keep such a search honest, and estimate how much more data each component needs before a club could rely on it.

---


### 245. [SHUSH: Emission-Aware Reward Design for Proactive Video Assistants](https://arxiv.org/abs/2611.26478)

**<font color=#1a73e8>作者：</font>** Shawn Liang, Soamar Homsi, Gourav Datta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive video assistants must decide not only what to say, but also when to speak. Existing reinforcement-learning objectives can reward timely, correct responses without accounting for response volume, thereby encouraging unnecessary or repeated emissions. We identify this failure mode in MMDuet2, whose proactive area-under-the-curve (PAUC) reward promotes timely responses but does not price the number of emissions. We show analytically that this makes additional responses weakly penalized or effectively free, systematically encouraging over-emission. We then propose an emission-aware F1 reward for interval-valued annotations, using exclusive span--emission matching to price false emissions and missed spans. Under MMDuet2's training recipe, our policy on the visual subset of OmniPro replies 2.5x less often than MMDuet2 while raising timing F1 from 0.259 to 0.396 and content-aware F1 from 0.103 to 0.154; a more conservative variant cuts replies by 82.5% and raises precision from 0.161 to 0.418. On ProactiveVideoQA, the same reward adds replies where the baseline is nearly silent, and PAUC ranks a heavily over-emitting policy second despite near-last F1, because it is insensitive to response count. Our results indicate that proactive assistants should be trained and evaluated with objectives that price emissions.

---


### 246. [FLUID: Flexible, Evidence-Grounded Situated Task Guidance](https://arxiv.org/abs/2611.26491)

**<font color=#1a73e8>作者：</font>** Yunqi Zhao, Run Peng, Ze Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time task guidance is inherently flexible: when an agent guides a user through a task, multiple responses and timings can be appropriate, and sometimes the best action is to remain silent. Existing benchmarks often miss this flexibility by treating synthesized dialogues as fixed targets for what to say and when to say it. We introduce FLUID (Flexible, Evidence-Grounded Situated Task Guidance), a unified framework for modeling, evaluating, and enabling flexible interaction in multimodal task guidance. Using naturally occurring human-human guidance from WTaG and HoloAssist, FLUID grounds interventions in their supporting evidence, necessity, and timing flexibility, and uses this representation both to evaluate flexible guidance and to build a real-time agent for task guidance. Our agent achieves the strongest overall balance of response correctness, intervention precision, timely guidance, and response latency among evaluated systems, while still leaving room for improvement in avoiding speech overlap. Together, FLUID moves situated task guidance beyond rigid reference matching toward more natural and adaptive human-AI interaction. Project page: this https URL.

---


### 247. [SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention](https://arxiv.org/abs/2611.26493)

**<font color=#1a73e8>作者：</font>** Aoxiang Fan, Maria Pilligua, Corentin Dumery 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward models have been very successful in 3D reconstruction with ad hoc attention designs that relate all view patches densely. However, the cost of this dense global attention grows quadratically with the number of views, preventing the model from applying to larger-scale reconstruction settings. In this paper, we argue that most dense attention computations are unnecessary from a classical structure-from-motion perspective: 3D structures stem from geometrically matching regions in 2D. We bring this principle to learning-based feed-forward reconstruction with our Sparse Geometric Attention Reconstruction (SGAR) method. In SGAR, each patch token attends to only a small set of patch tokens from other views, chosen by a lightweight learned key selection module trained to predict cross-view 3D proximity of tokens. Thus, dense global attention is replaced by much more efficient geometric-similarity-guided sparse attention. SGAR is a general method that can be applied to different feed-forward models by fine-tuning. In our experiments, we show that SGAR is the fastest among both state-of-the-art dense and sparse methods and the most accurate sparse one. It runs up to 12-times faster than dense attention at 1,000 views with stable pose accuracy where existing sparse methods fail, and shows the best performance in reconstructing more complete geometries on the same time budget.

---


### 248. [Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning](https://arxiv.org/abs/2611.26504)

**<font color=#1a73e8>作者：</font>** Élodie Côté-Gauthier, Doina Precup, Isabeau Prémont-Schwarz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $\theta_i = 1/(1-\gamma\lambda_i)$, where $\lambda_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.

---


### 249. [Visual Attribution Limits and Graded Provenance Auditing in Commercial Video-Generation APIs](https://arxiv.org/abs/2611.26508)

**<font color=#1a73e8>作者：</font>** Haocheng Mei, Yuchuan Tian, Yingte Shu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commercial video-generation APIs bill by model and tier, while intermediaries could substitute cheaper models, lower tiers, or cached clips. What can a delivered file establish about its origin? We combine measurements of passive attribution and cryptographic provenance into a graded audit. We test attribution probes and zero-shot detectors under re-encoding, downscaling, and frame-rate changes, and survey C2PA and GB 45438 metadata across 19 commercial endpoints. Only authenticated provenance supports accusations: tier contradictions or duplicate signed instances under fresh-generation contracts, excluding retries and idempotent returns. Unverifiable signed-endpoint deliveries trigger original-file demands under pass-through clauses; archive-reuse and delivery-parameter screens support review only. Six-model container and bitstream accuracy falls from 83.9% on raw files to 45.3% after uniform re-encoding, using different feature sets. Subsampling real references from 24 to 3 fps raises pooled D3 AUROC from 0.845 to 0.988. Only BytePlus authenticates tier claims under our pinned policy, including 187/187 audited deliveries across three Seedance tiers; tested remuxing and re-encoding leave processed Seedance files unverifiable. The audit identifies authenticated contradictions in 100/100 raw 720p signed tier-swap cases, with zero observed false flags on the tested honest pools.

---


### 250. [Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain](https://arxiv.org/abs/2611.26511)

**<font color=#1a73e8>作者：</font>** Shuang Wu, Jiachen Qian, Youtian Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, from vecset and triplanes to structured sparse voxels. Despite their architectural differences, these methods all share the same premise: geometry is first compressed into a latent space and only then modeled by the generator. We take a different route and propose Direct3D-V3, a latent-free diffusion transformer (DiT) framework that discards the VAE altogether and operates in the native voxel domain, directly modeling raw SDF voxel grids during both training and sampling. To make this direct voxel formulation geometrically reliable, we introduce an implicit manifold regularization over neighboring voxels to suppress non-watertight surfaces, and convert predicted SDF grids into meshes via Marching Cubes so that rendered normal losses can supervise the model directly from its predicted SDF. To improve alignment between the conditioning image and generated geometry, Direct3D-V3 also predicts the camera parameters of the conditioning image as an auxiliary task, encouraging the DiT to learn the mapping from image observations to 3D shape. This latent-free design removes the reconstruction bottleneck, brings training under an objective in the native voxel domain, and yields meshes with substantially richer local detail. The predicted camera and native SDF voxel output further make Direct3D-V3 extensible to generative reconstruction, where diffusion is interleaved with normal-guided refinement to improve alignment with the observed view while the generative prior completes unseen regions. Project page: this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
