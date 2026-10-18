# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

---

### 101. [DLOSAC: Joint Spatial-Geometric Image Estimation via Delaunay-Guided Local Optimization RANSAC](https://arxiv.org/abs/2610.21215)

**<font color=#1a73e8>作者：</font>** Yu Liu, Meiqi Zhou, Zipei Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable image geometric estimation from noisy matching points is typically addressed using RANSAC, often combined with local optimization to refine inliers and model parameters. However, existing paradigms are predominantly residual-centric; even heuristic attempts to enforce spatial uniformity suffer from a sequential, two-stage nature that inherently decouples distribution optimization from geometric refinement, preventing an effective trade-off. In this paper, we propose DLOSAC, a local optimization framework that jointly incorporates both geometric consistency and spatial distribution information. We begin by constructing a Delaunay triangulation over candidate inliers to explicitly encode neighborhood topology. The geometric module introduces an edge-based consistency metric to evaluate geometric errors, while the spatial module derives distribution descriptors from triangle areas and edge attributes to quantify the clustering of inliers. Finally, we combine edge-based geometric constraints, spatial distribution regularization, and traditional point-level geometric constraints to improve the quality of geometric parameters. Extensive experiments on six publicly available real-world datasets, covering three types of geometric estimation tasks, achieve state-of-the-art performance.

---


### 102. [On the Complexity of Symmetric Boolean Functions in Multiparty Private Simultaneous Messages](https://arxiv.org/abs/2610.21216)

**<font color=#1a73e8>作者：</font>** Marshall Ball, Peter Crawford-Kahrl, Vladimir Podolskii 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multiparty Private Simultaneous Messages (PSM), also known as Decomposable Randomized Encoding (DRE) or information-theoretic garbling, is a model for non-interactive secure computation. Each party encodes its input using shared randomness and sends a message to an evaluator who does not know that randomness. The evaluator must recover the function output without learning anything else about the inputs. Perfect privacy requires identical transcript distributions on inputs with the same output. We also study the weaker notion of support privacy, which requires only that these distributions have the same support.
We study the communication complexity of symmetric Boolean functions when each of the $n$ parties holds one input bit.
Lower bounds. We prove a superlinear lower bound for support-private PSM protocols computing $OR_n$. Our technique gives $\Omega(n\log n)$ lower bounds for $MAJ_n$ and $EMAJ_n$ (with even $n$), and an $\Omega(n\log q)$ lower bound for $MOD_q$ when $q\leq(1-c)n$ for a fixed constant $c>0$.
Upper bounds. We construct perfectly private PSM protocols of total communication $\widetilde{O}(n^{3/2})$ for every symmetric Boolean function, improving on the known quadratic bound. For $MAJ_n$, known branching-program constructions yield an upper bound of $O(n\log^3 n\log\log n)$. For $EMAJ_n$ and $MOD_q$ with prime $q$, the lower bounds are tight up to constant factors in the stated regimes. Under support privacy, we obtain $\widetilde{O}(n)$ communication for every symmetric Boolean function.
Earlier lower-bound techniques of Ball et al. (ITCS 2020) yield only trivial linear bounds for symmetric Boolean functions. Concurrent and independent work by Holmgren and Wu proves a $\omega(n)$ lower bound for $OR_n$ using the same combinatorial core. Both works used AI assistance.

---


### 103. [Learning and Forecasting Multiscale Spatiotemporal Epidemic Dynamics with Lagrangian-Eulerian Graph Neural ODEs](https://arxiv.org/abs/2610.21223)

**<font color=#1a73e8>作者：</font>** Jinyi Duan, Qian Li, Biao Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate medium- to long-range epidemic forecasting requires extrapolating high-dimensional, heterogeneous and nonstationary dynamics from partial observations. Yet hybrid models often leave implicit which observations inform which epidemic processes and how learned graph interactions modify system state. We introduce LE-EpiGNODE, which replaces generic message passing with process-specific, mechanism-guided neural operators: age-contact information drives Lagrangian infection generation, whereas mobility drives conservative Eulerian population transport within a structure-preserving universal differential equation. We evaluated LE-EpiGNODE across 14 controlled synthetic mechanisms spanning time-modulated, state-dependent, nonlinear and coupled dynamics, three complementary COVID-19 settings, 21 comparator models and five targeted ablations. Forecasting gains tended to become more pronounced at longer horizons; at the longest horizon, LE-EpiGNODE achieved the lowest WMAPE in all three real-world datasets, reducing error by 17.7-40.0% relative to the best baseline. Controlled ablations linked these gains to the Lagrangian-Eulerian decomposition and process-aligned priors, while synthetic ground truth showed that learned operators and induced state fluxes track known generating dynamics. These results support mechanism-organized graph neural dynamics as a route to reliable long-horizon extrapolation with directly testable, process-level mechanistic interpretation beyond trajectory accuracy.

---


### 104. [What Should We Remove? Evaluating the Reliability and Costs of RLVR Data Decontamination](https://arxiv.org/abs/2610.21229)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) math corpora are routinely screened for benchmark overlap, but the reliability and data-loss costs of cleaning policies remain underexamined. We audit sixteen open RLVR math corpora comprising 1,673,514 corpus-specific training items against six benchmarks containing 1,949 questions. We evaluate eight policies based on exact, lexical, and semantic matching using 594 independently and blindly dual-reviewed training-benchmark pairs. Calibration and held-out sets have disjoint benchmark questions and training-example families. A separate review of all 83 candidate matches for 80 sampled training items measures item-level false removal. At cosine threshold 0.80, 52 of 59 sampled removals (88%) were confirmed false removals; this is not a demonstrated population rate. No semantic threshold in our preregistered grid (0.80-0.98) meets the 90% conservative-precision target on calibration. The existing judge-adjudicated policy achieves 98.1% resolved precision and 98.2% candidate-frame recall on held-out corpora. It has zero confirmed false removals among six sampled removals, with one unresolved case; this does not establish zero risk. Within the evaluated candidate frame, this policy offers a more favorable precision-recall balance than the semantic-threshold alternatives tested. Recall does not measure contamination outside the candidate frame. We release reviewed labels, per-policy decisions, and coverage accounting to support evaluation of cleaning reliability and cost rather than overlap counts alone.

---


### 105. ["Do You Trust It... or Check It?": Exploring Children's Verification Behaviors in Game-Based Human-AI Collaboration](https://arxiv.org/abs/2610.21233)

**<font color=#1a73e8>作者：</font>** Shuning Liu, Yuxin Song, Hanbing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Children are increasingly interacting with AI agents in learning and problem-solving contexts, where AI suggestions may appear fluent, helpful, and socially engaging. However, children may not always be able to judge whether such suggestions are accurate, incomplete, or misleading. This paper presents a game-based human-AI collaboration probe designed to examine how children verify AI suggestions during task-based interaction. The system embeds AI suggestions within a biological knowledge reasoning game and compares three Agent interaction styles: partner-like, tool-like, and dual-state Agent. Instead of treating trust as a static post-task attitude, this study focuses on children's situated verification behaviors, including acceptance, evidence checking, questioning, revision, and continued AI use. A preliminary evaluation with children aged 8-10 combined interaction logs, post-task ratings, and semi-structured interviews. The findings suggest that Agent style shaped children's engagement and response pathways: partner-like interaction tended to support direct questioning, while tool-like interaction was more associated with evidence seeking. Children generally viewed AI as useful but fallible, and their questioning behaviors varied in reasoning depth. The study contributes design insights for supporting children's critical, reflective, and evidence-based use of AI in collaborative tasks.

---


### 106. [Workplace Ambiguity and Technology Support for Autistic and IDD Workers](https://arxiv.org/abs/2610.21236)

**<font color=#1a73e8>作者：</font>** Silas Curry, Rishit Singh, Heekyoung Jung 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Workplace ambiguity, where expectations, evaluations, or procedures are left unstated, acts as a structural access barrier for autistic and IDD workers, routinely forcing them to act on guesses. To investigate how these barriers operate, we interviewed 11 caregivers, concluding with an AI co-design activity to explore technological solutions. Their perspectives revealed five themes of workplace ambiguity, which we synthesize into a conceptual framework comprising three intersecting dimensions: evaluative, procedural, and relational. To address these barriers, participants proposed three forms of technology support, including ambient real-time redirection, feedback processing, and physiological guidance, designed to make hidden expectations perceptible and actionable. However, this exposes a core tension: technologies designed to make the workplace legible can inadvertently make the worker hyper-legible to employers through surveillance. We argue that ambiguity-aware workplaces must make expectations explicit before they carry consequences, and assistive technologies must remain accountable to the worker.

---


### 107. [A large-scale climate-aware satellite image dataset for domain adaptive land-cover semantic segmentation](https://arxiv.org/abs/2610.21238)

**<font color=#1a73e8>作者：</font>** Songlin Liu, Linwei Chen, Li Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A few well-annotated datasets for land-cover semantic segmentation have recently been introduced to advance the field of earth observation technologies. However, these datasets overlook the significant diversity among geographic areas with different climates, which can greatly impact and diversify land cover. Consequently, this leads to a domain gap in remote sensing images and severe performance degradation of the segmentation models. To enhance land-cover semantic segmentation with improved generalization ability, we conducted the first investigation into the impact of climate on this task. In this paper, we present a unique large-scale Climate-Aware Satellite Images Dataset (CASID) specifically designed for domain adaptive land-cover semantic segmentation. It consists of 980 satellite images with a size of 5000 x 5000 pixels, collected from 30 different regions around Asia, covering over 24,500 square kilometers. These images are gathered from four distinct climate zones, namely temperate monsoon, subtropical monsoon, tropical monsoon, and tropical rainforest. It includes four sub-datasets/domains, each representing one of the aforementioned climate zones. This characteristic makes CASID the first climate-aware land-cover semantic segmentation dataset with multiple domains. Additionally, we provide a comprehensive analysis of the samples from the four climate zones, emphasizing differences in global image features, image texture, category distribution, spectral value, and object shape. These analyses offer valuable insights for subsequent research in this field. Moreover, we conduct extensive experiments to evaluate the latest semantic segmentation and unsupervised domain adaptation methods on the CASID dataset. These results serve as a robust baseline for future research endeavors. Our dataset will be made publicly available at this https URL.

---


### 108. [A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems](https://arxiv.org/abs/2610.21243)

**<font color=#1a73e8>作者：</font>** Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibility for delegated dependencies and failure recovery unclear. To address this gap, we propose RCM, a responsibility-centered coordination mechanism that leverages commitments to couple task delegation with explicit responsibilities of the involved parties. Through recursive delegation, agents retain their upstream responsibilities while locally orchestrating downstream commitments, thereby preserving accountability across delegation chains, creating a network of local orchestration. We operationalize this mechanism locally through responsibility-constrained decision-making and a responsibility-oriented communication protocol (RCP), enabling agents to autonomously establish, manage, and terminate commitments. As agents act in parallel, their local actions continuously evolve the commitment graph, allowing global coordination to emerge and adapt toward a shared mission without centralized control. Experiments across reasoning, coding, and executable agent environments demonstrate that RCM outperforms strong centralized and decentralized coordination baselines by up to 18.7 points in task performance and 10.2 points in Responsibility, while improving failure and harm detection without task-specific training.

---


### 109. [What do AI chatbots do after users decline therapeutic redirection for suicide thoughts?](https://arxiv.org/abs/2610.21253)

**<font color=#1a73e8>作者：</font>** Subigya Nepal, Ruth Heo, Emma M Parrish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of artificial intelligence (AI) chatbots focus on therapeutic redirection, statements urging users who disclose suicide thoughts to seek help from crisis lines or other human sources. How chatbots respond when users refuse that help is unclear. This cross-sectional audit ran 2,550 scripted multi-turn conversations in September 2026. Each conversation opened with a disclosure of suicide thoughts at 3 levels of severity, answered every referral with up to 10 standardized refusals and then changed the subject. All 2,550 conversations included a referral, 2,542 (99.7%) in the first reply. However, mean persistence ranged from 0.01 to 9.94 refusals across chatbots. Newer versions of all 5 chatbots tested in 2 versions persisted less than older versions (each P < .05). Compared with passive ideation, a disclosure of intent was associated with 1.26 more refusals sustained (95% CI, 1.06-1.46) and higher odds of renewed referral after the topic change (odds ratio, 10.07; 95% CI, 7.43-13.66). Chatbots that persisted less in referral more often presented themselves as the user's support (Spearman rho = -0.80; P < .001). Of 8,818 refusal-phase replies urging outside help, only 173 (2.0%) asked about barriers to seeking it. Chatbots uniformly recommended outside help after disclosures of suicide thoughts but varied widely in persisting in those recommendations, with newer versions persisting less. Safety evaluations should test what happens after a crisis referral is refused, not only whether one is offered.

---


### 110. [Behavioral Compositionality of Sparse Autoencoder Representations](https://arxiv.org/abs/2610.21261)

**<font color=#1a73e8>作者：</font>** Haotian Ma, Ziye Mei, Frederic Sala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) represent model activations with sparse, linearly decoded features, but the downstream effects of those features need not compose additively. We introduce SAE Additivity Residuals (SAR), which measure the behavioral variation left unexplained above a chosen interaction order. Under independent feature subset sampling, population SAR is exactly the normalized energy of interactions above that order and bounds coalition ordering error for the optimal low order approximation. To distinguish compositionality associated with the SAE representation from that induced by downstream computation, we compare learned SAE coordinates with sum preserving random rotations of the same selected subspace and find lower first order residuals for the learned coordinates across all 18 model and behavior settings. The coordinates are nevertheless not fully additive: pairwise terms improve held out coalition ordering in every setting and outperform parameter matched models using randomly selected third order terms. In a combined steering experiment, pairwise modeling raises rank fidelity from 0.5874 to 0.7790 and reduces ordering error from 0.1444 to 0.0606. Together, these results show that SAE coordinates support comparatively compositional behavioral descriptions while faithful joint explanations and interventions still require interactions beyond individual feature effects. Code is available at this https URL.

---


### 111. [Rethinking Learning from Label Proportions via Moment Matching](https://arxiv.org/abs/2610.21262)

**<font color=#1a73e8>作者：</font>** Tianhao Ma, Wei Wang, Yivan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from label proportions (LLP) is a weakly supervised setting where training data are grouped into bags with only bag-level label proportions observed, and the goal is to learn a classifier that predicts labels for individual instances. Recently, a large body of methods has emerged; however, most of them rely on the assumption that instance-label pairs are sampled i.i.d. and randomly assembled into bags, an assumption often violated in real-world scenarios. Our experimental results indicate that these methods perform suboptimally under non-random settings. In this work, we adopt a more realistic assumption: bags are sampled i.i.d., and instance labels are conditionally independent given the instances. Under this setting, we show that the label counts follow a Poisson multinomial distribution. Motivated by this observation, we propose LLP via moment matching (LLP-MM), a simple yet effective approach which leverages multi-order factorial moments as training objectives, encouraging the classifier predictions to match these moments and thereby more fully exploit the underlying statistical structure of the data. Extensive experiments on benchmark datasets under various bag construction strategies demonstrate the effectiveness of our approach while maintaining high computational efficiency. Our code is available at this https URL.

---


### 112. [Trigger Value Selection in Clean-Label Malware Backdoors: An Effectiveness-Detectability Analysis](https://arxiv.org/abs/2610.21269)

**<font color=#1a73e8>作者：</font>** Tri Budi Sabdo Utomo, Kazushi Okamoto, Koki Karube 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Clean-label backdoor poisoning is a threat to machine learning-based malware classifiers because poisoned samples can be inserted into training data without changing their labels. Previous explanation-guided attacks mainly focus on selecting important trigger features, but the values assigned to these features can also affect the attack behavior. In this paper, we study trigger value selection as an independent design factor in clean-label backdoor attacks against feature-based malware classifiers. We evaluate several value-selection strategies on EMBER 2018 and a Win64 PE subset of EMBER 2024 using LightGBM classifiers. We compare rare-value, SHAP-based, frequency-bounded, co-occurrence-aware, and quantile-based selectors under random and distribution-based malware-similar benign sampling. The results show that aggressive selectors such as MinPopulation and CountAbsSHAP can achieve high attack success rate, especially under distribution-based sampling, but they are also easier to detect by sanitization methods such as Isolation Forest. In contrast, selectors such as CorrCountAbsSHAP and Quantile95 can reduce poison recall while keeping useful attack effectiveness. These findings show that trigger value selection is not merely an implementation detail, but an important design choice that shapes the effectiveness and detectability profile of clean-label malware backdoor attacks.

---


### 113. [Regret Lower Bound for Online Learning of Quantum States with Logarithmic Loss, with Applications to Quantum State Tomography and Confidence Sequences for Matrix Means](https://arxiv.org/abs/2610.21273)

**<font color=#1a73e8>作者：</font>** Yen-Huan Li, Wei-Fu Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of online learning of quantum states with logarithmic loss, which is a quantum generalization of online portfolio selection and has applications to quantum state tomography, the task of estimating an unknown quantum state from measurement outcomes. We first establish a regret lower bound, showing that the regret rates of Exponential Weights and the algorithm of Tseng et al. (2025) have optimal polynomial dependence on the dimension. Our analysis leads to two further results. First, our lower-bound proof leads to a quantum state tomography algorithm that is sample optimal up to polylogarithmic factors in the sample size. Second, we develop an algorithm for constructing confidence sequences for the mean of a matrix-valued random variable. A numerical experiment shows that the latter algorithm is competitive with existing methods.

---


### 114. [When Rotation Bounds Nothing: Streaming Image Classifiers to Field Nodes Under Physical Capture](https://arxiv.org/abs/2610.21276)

**<font color=#1a73e8>作者：</font>** Daniel Gilkarov, Ran Dubin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Field nodes run image classifiers locally, exposing a first-class asset, the trained model, to theft. Trusted-execution enclaves, collaborative-inference splits, and encrypted storage assume the device owner is the adversary from deployment. Here the operator owns the node, and an adversary seizing it reads only what cold-boot capture finds resident. One answer stores nothing: a chunkable multi-exit model streams into volatile memory, rotating to bound residency. We characterise the capture envelope on real LTE traces across two victims of one architecture, against passive and adaptive adversaries. Neither survives a capable adversary; recovery cost alone differs. Against a from-scratch victim the uncaptured stages must be learned: the adaptive adversary gains most at shallow seizures, ends the CIFAR-10 envelope at every rotation, and stays rotation-bounded on CIFAR100, from 42.6% of usable seizures at 5 s to 86.8% at 30 s. Against the same architecture sliced from a public pretrained backbone, the adversary downloads those stages, recovering at least 90% of maximum accuracy at all depths, taking usable CIFAR-100 seizures from 0.0% to 97.3% at 5 s, given the victim's full labelled training set. Delivery-side secrecy raises a seizure's price; a public copy of the withheld stages erases it.

---


### 115. [ReState: Noise-Level-Aware State Correction for Training-Free Object Removal in Few-Step Diffusion Models](https://arxiv.org/abs/2610.21287)

**<font color=#1a73e8>作者：</font>** Donghwan Lee, Sanghyun Jo, Sihyun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free object removal commonly redirects self-attention away from the target region, but on few-step distilled diffusion models this often leaves object-shaped residuals. We identify a temporal mismatch: a structured prediction forms inside the mask at the first forward, and the short trajectory offers few later chances to revise it, while attention rerouting acts mainly in later steps. Across four distilled backbones, magnitude-matched single-forward interventions show that background-directed state correction affects the final result more than attention rerouting. We therefore propose ReState, which corrects the masked clean prediction toward background evidence retrieved from the input using a noise-level-aware weight that vanishes at the final forward. ReState retains object-excluding attention as a complementary constraint and adds no denoiser evaluations. Across two paired benchmarks and two few-step backbones, ReState achieves the best masked PSNR, SSIM, and LPIPS among training-free methods, improving PSNR by 3.17 dB on average over the strongest baseline. On OBER-Test, it also outperforms the 50-step attention-forcing reference on all three metrics at 6.7x lower latency. The same configuration transfers to two additional distilled backbones without retuning. Project page: this https URL

---


### 116. [Personalized Projected Ascent for Federated Stackelberg Optimization](https://arxiv.org/abs/2610.21295)

**<font color=#1a73e8>作者：</font>** M Yashwanth, Sharannya Ghosh, Saikiran Bulusu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated minimax problems, such as distributionally robust optimization and adversarial training, include an inner maximization variable built from each client's local data. These variables differ in meaning and dimension from one client to the next, so averaging them across clients, as standard federated minimax methods do, is ill-posed. We therefore study a federated minimax problem where the minimization variable $\mathbf{x}$ is shared and aggregated, while each client retains the maximization variable $\mathbf{y}_i$ (personalized). Because these applications constrain $\mathbf{y}_i$ to a compact convex set, we analyze projected ascent directly. We show that, in the nonconvex-concave regime, this projected personalized scheme attains the standard sublinear rate. In the nonconvex-PL regime, however, it hits a stepsize-invariant noise floor due to stochastic $\mathbf{y}_i$ updates. To mitigate this, we propose VR-SGDA, incorporating a variance-reduced ascent step where each client maintains a private variable snapshot. By evaluating current and snapshot gradients on the same sample, the constant variance is replaced by a vanishing drift under a two-timescale regime. VR-SGDA eliminates the noise floor, attaining sublinear leading rates while preserving personalization and projection. Experiments on subpopulation-robustness and NLP adversarial training confirm both the worst-group robustness benefits and the two-timescale tracking mechanism.

---


### 117. [GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama](https://arxiv.org/abs/2610.21297)

**<font color=#1a73e8>作者：</font>** Jing OU, Zidong Cao, Liaoyuan Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic 3D reconstruction enables the holistic recovery of complete 360 $^\circ$ scene geometry, offering significant benefits for robotics and AR/VR applications. However, directly estimating geometry from ERP images is inherently challenged by spherical distortions. To reduce spherical projection distortions, a common strategy is to decompose panoramas into distortion-free perspective views, but independently processing these views often introduces cross-view geometric inconsistencies. To address these challenges, we introduce GeoPano, a feed-forward framework for single-view panoramic 3D reconstruction that recovers a geometrically accurate and consistent point cloud from a single panorama. Our approach is driven by two key innovations: First, we propose a panoramic-aware attention aggregator, featuring a streamlined attention architecture equipped with a novel Pano-Attention mechanism, which explicitly exploits the intrinsic spherical geometry of the panorama to guide cross-view interactions, thereby suppressing geometric inconsistencies. Furthermore, we formulate a hybrid supervision strategy to jointly enforce fine-grained local details in perspective space and global structural coherence in spherical space. Experiments demonstrate that our method significantly outperforms previous SOTA approaches in reconstruction accuracy, geometric consistency, and visual fidelity.

---


### 118. [Dusting the Phantom: Gaussian Allocation for Fading Dynamic Content](https://arxiv.org/abs/2610.21302)

**<font color=#1a73e8>作者：</font>** Minhyeok Roh, Minseo Lee, Jun Young Jeong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic Gaussian representations have made high-quality, real-time volumetric video increasingly practical, yet challenging motion can still break their reconstruction: small fast-moving objects may disappear, and fine textures in highly dynamic regions are often lost. In particular, simply training longer or using more Gaussians may still fail to recover small, fast-moving objects. We argue that the key bottleneck is not representational capacity itself, but where and when Gaussian primitives are allocated. Existing allocation strategies rely on current Gaussian locations and often overlook the spatiotemporal destinations of relocated Gaussians. To address these limitations, we introduce two complementary strategies. First, Seed Injection identifies under-reconstructed dynamic regions using temporal appearance changes and reconstruction errors, and initializes new Gaussians at geometrically plausible 3D locations through multi-view observations, independent of existing Gaussian locations. Second, Temporal Biased Relocation uses time-resolved optimization signals to guide the spatiotemporal placement of relocated Gaussians. Both strategies maintain a fixed Gaussian budget without modifying the underlying representation. Experiments across multiple dynamic-scene datasets demonstrate improved reconstruction quality, particularly in highly dynamic regions, recovering small, rapidly moving objects and fine-grained appearance details.

---


### 119. [Spectrum Is Not Enough: A Random-Matrix Account of Data-Free Preconditioning for Differentially Private Learning](https://arxiv.org/abs/2610.21312)

**<font color=#1a73e8>作者：</font>** Shilin Zhang, Kangning Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-free preconditioning builds the Kronecker factors of KFAC from synthetic probes instead of private data. DP-KFC validates a probe by matching the eigenvalue decay of the private factors; we turn this criterion into a random-matrix account of what a probe can reconstruct. A single dichotomy organizes it: in the factorization $ A \otimes G $, the error-signal factor $ G $ and the architecture-determined bulk of the activation factor $ A $ are reconstructible without data, while only the data-induced spikes of $ A $ are not. We prove the $ G $ half is data-insensitive up to an explicit error-energy bound, with zero violations over a full training trajectory across four modalities and a natural-image benchmark. We locate the failure boundary at a Baik-Ben Arous-Péché threshold: a bulk-only probe suffers an exact damage $s^2/(1-s^2)$ from a data-induced spike, which becomes invisible once it exceeds $(d/n)^{1/4}$, confirmed on an injected-spike surrogate. Holding the probe spectrum fixed and varying only its eigenbasis, we show that spectral-shape matching is neither sufficient nor the operative object: a probe with a near-exact matched spectrum (log-ratio dispersion $0.02$) still inflates the residual $2 \times $-$90 \times $ when its eigenvectors are random. A closed-form whitened-volume law explains this and predicts the within-spectrum ordering of the critical volume, though not its cross-dataset magnitude. Downstream, per-layer tuning does not transfer to accuracy and the headroom is a small oracle-minus-white gap. Under a privacy mechanism the source ordering survives while learning does, then inverts at a noise cross-over where the flat probe overtakes the matched ones.

---


### 120. [Money-Mule Detection as a Relational Learning Problem: A Study on the RBIH NFPC Dataset](https://arxiv.org/abs/2610.21314)

**<font color=#1a73e8>作者：</font>** Owais Ahmad, Anirudh Deodhar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Money-mule networks move criminal funds through many small transfers, each of which looks ordinary on its own. What marks an account as a mule lies outside any single transfer: in the counterparties and addresses its network shares, and in the shape of its activity over time. Production systems remain largely rule-based and see neither, while most research classifies transactions rather than accounts, recovering account-level risk only by aggregating afterwards. We instead score the account directly, reading the bank's relational schema as a heterogeneous graph in which rows are nodes and foreign keys are edges. Each account is scored from a multi-hop neighbourhood using per-column encoders, a relative-time encoding and HeteroGraphSAGE message passing, with that neighbourhood restricted to rows predating the account's own pre-flag cutoff so that no model sees evidence recorded only after the account was flagged. On a five-year Reserve Bank Innovation Hub (RBIH) retail-banking dataset of 400 million transactions and 94{,}063 labelled accounts, 2.6\% of them confirmed mules, we compare against RelGNN, XGBoost, LightGBM and CatBoost trained on identical labels, splits and cutoffs. Our detector recovers nine in ten held-out mules at 83\% precision and a 0.5\% false-alarm rate, finding 115 more mules than the strongest tree ensemble given the same evidence. At the tuned thresholds the gap is mostly in recall: XGBoost and LightGBM lead across the first hundred alerts, but only the graph models hold their precision deep into the queue. Since the graph is the schema itself and every score is dated per account, the approach deploys on a bank's existing database without a custom feature graph build.

---


### 121. [Constrained Multi-Agent Reinforcement Learning in Imagination](https://arxiv.org/abs/2610.21319)

**<font color=#1a73e8>作者：</font>** Raz Shmueli, Shahaf S. Shperberg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting cost in a multi-agent world model moves most constrained policy updates into imagination: the stronger model-free baseline needs $10$ to $20$ times CA-MAMBA's interactions on the median SMAC configuration, and CA-MAMBA earns $2.8$ to $12$ times the baselines' MAMuJoCo reward at equal budget. In controlled tests on one task per benchmark, pricing the model's cost advantages at parity more than halves a cost-blind learner's cost and meets a tight continuous-control limit the learned multiplier misses, suggesting the model's cost estimates are not the bottleneck.

---


### 122. [CoViG: Coarsened Vision GNN for Image Classification](https://arxiv.org/abs/2610.21321)

**<font color=#1a73e8>作者：</font>** Martial Guidez, Stefan Duffner, Christophe Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Graph Neural Networks are widely used in various domains, they remained mostly unexplored in computer vision. Convolutional Neural Networks and Vision Transformers were leading the field, until the quite recent introduction of Vision Graphs (ViG) that treat images as a set of nodes and apply graph convolution on their k-NN graphs. ViGs show impressive accuracy on image classification but their computational cost remains relatively high. Inspired by optimization methods for GNNs, we present CoViG, a novel approach combining graph coarsening and ViGs. Our method introduces an additional MinCUT pooling step within the Grapher component of intermediate ViG blocks. By simplifying the intermediate graphs and thus decreasing the number of nodes of specific blocks, our approach considerably reduces the computational cost of ViG during inference. We evaluated our approach on ImageNet with several ViG architectures, and we obtained accuracies equivalent to the original ViG models with only about 51\% of FLOPs.

---


### 123. [Hybrid Generative-Tagging Decoding for Efficient Product Attribute-Value Extraction](https://arxiv.org/abs/2610.21329)

**<font color=#1a73e8>作者：</font>** Keshav Kolluru, Manas Gupta, Maroof Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attribute-value extraction is important for building high-quality product catalogs in e-commerce. Existing systems either rely on generative or tagging strategies for extracting the attribute names and their corresponding values. Tagging models directly label spans in the source, making them fast and grounded, but they cannot produce values that require reformatting or generate rare attribute names outside their label space. Generative models avoid these drawbacks by generating both attribute names and values token by token, but this auto-regressive nature makes them slow and limits attribute coverage. We introduce hybrid generative-tagging decoding, a novel model architecture that combines tagging source spans and open-ended generation. For frequent attributes whose values are copyable, a tagging head extracts values directly from the source. This lets the generative head focus on the remainder - rare attributes outside the tagger's label space and non-copyable values, including implicit or normalized values. Integrated into vLLM inference, the hybrid decoder raises attribute coverage by 10% and extracts 63% more correct attribute-value pairs at no precision cost, while reducing latency by 44%.

---


### 124. [Semantic Latent Alignment for Flow Matching with Invertible Bi-Lipschitz Adapters](https://arxiv.org/abs/2610.21332)

**<font color=#1a73e8>作者：</font>** Felix Nützel, Mischa Dombrowski, Luca Hagen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained latent spaces trade compression, reconstruction, and the learnability of the coordinates a downstream generator has to work in, which complicates adapting these spaces to different domains or tasks: continued training is expensive, and without a new alignment objective it often fails to improve downstream generation. We instead leave the encoder and decoder fixed and change only the coordinates between them, using an invertible bi-Lipschitz adapter aligned offline to a semantic teacher and frozen during class-conditional flow matching. Invertibility preserves compatibility with the pretrained autoencoder, while the bi-Lipschitz constraint limits how far alignment can distort its latent geometry. This provides a simple way to improve semantic organization while retaining the compression and reconstruction properties of the original latent space. On two medical imaging datasets, constrained latent adaptation improves feature metrics, seed stability and counterfactual edit strength, while remaining competitive on downstream classification. In contrast, unconstrained adaptation can become highly anisotropic and sensitive despite remaining invertible, highlighting the importance of controlling geometric distortion. Our results suggest that carefully constrained post-hoc adaptation offers a parameter-efficient and tuning-free alternative to jointly modifying the representation during generative training.

---


### 125. [When Should a Low-Light Pipeline Generate? Auditable Risk Control for Selective Generative Enhancement](https://arxiv.org/abs/2610.21335)

**<font color=#1a73e8>作者：</font>** Qiyi Xie, Wei Chen Ng, Suyang Xi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative low-light enhancers recover plausible texture but may hallucinate structure; restoration networks preserve structure but can leave regions under-enhanced, and neither advantage is spatially uniform. Therefore, we formulate selective generative enhancement as a decision problem: determine where overriding a frozen base expert is beneficial and refuse to switch when the evidence is insufficient. We propose VetoNet, an auditable regional routing framework centered on a certified veto. It first measures the complementary strengths and routing direction of a frozen restoration generative pair, then predicts the utility of regional overrides from deployment-available signals alone and admits an override only when a distribution-free harm-budget certificate says the perceptual (LPIPS) risk budget allows it. Experiments across multiple expert pairs and domains show that VetoNet adapts its routing behavior to the strength and reliability of the available evidence. When expert complementarity is sufficiently predictable, it achieves statistically significant certified gains; when the relative strengths of the experts change, it correspondingly reverses the routing direction; and when routing evidence is weak or affected by cross-domain shift, it conservatively vetoes switching.

---


### 126. [Online Quantile Omniprediction for Proper Losses](https://arxiv.org/abs/2610.21342)

**<font color=#1a73e8>作者：</font>** Hyunsuk Kim, Isaac Gibbs, Michael W. Mahoney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The task of constructing a predictor that is simultaneously accurate under multiple evaluation metrics has been popularized recently under the name omniprediction. Prior work in this area has largely focused on binary prediction tasks, and existing results for multiclass and continuous outcomes typically suffer from slow error rates. In this paper, we consider forecasts expressed as a set of quantiles over a discrete but otherwise arbitrary set of probability levels. We develop sample-efficient algorithms for constructing forecasts that are accurate simultaneously across all proper losses that satisfy mild regularity conditions, where proper losses are those minimized by predicting the true quantiles. Our algorithms are online and can operate in a dynamic environment, while simultaneously taking multiple losses into account, and their forecasts offer the potential to provide diverse end-users with rich information for evaluating risk and informing a range of practical decision-making tasks. As an example, we demonstrate how our procedure can be used to ensemble quantile forecasts of COVID-19 hospitalizations made by experts during the pandemic.

---


### 127. [Quantum Versus Classical Machine Learning for Neuropsychiatric Disorders: A Feature-Matched Multi-Cohort Evaluation](https://arxiv.org/abs/2610.21344)

**<font color=#1a73e8>作者：</font>** Utsav Poudel, Anuj Nepal, Vyas Viswanath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Resting-state functional connectivity is widely used in machine learning-based classification of neuropsychiatric disorders. Quantum machine learning models have been proposed for functional connectivity data, but few studies have evaluated them under leave-site-out validation or against matched classical models. We compared six quantum model families with classical ones using identical correlation-derived features across four public cohorts (4,308 subjects). Leave-site-out validation was used for the Autism Brain Imaging Data Exchange (ABIDE I), ADHD-200 (attention-deficit/hyperactivity disorder), and REST-meta-MDD (major depressive disorder) cohorts, while the UCLA Consortium for Neuropsychiatric Phenomics (UCLA-CNP) was evaluated using stratified 10-fold cross-validation. The quantum kernel was statistically indistinguishable from a matched classical kernel across all four cohorts, with the average accuracy difference within 1.4 percentage points at 95% confidence. On ABIDE I, a hybrid quantum convolutional network achieved similar accuracy to its classical counterpart (0.645 vs. 0.641), while a trainable quantum kernel exceeded its classical counterpart by 0.064 in area under the curve (AUC). Quantum convolutional networks also achieved higher AUC than their matched classical networks on this cohort and showed smaller train-test gaps on all four cohorts, without an accuracy gain. Overall, most quantum models matched their classical counterparts, but none consistently outperformed them. This study, among the first quantum evaluations of ABIDE I under leave-site-out validation, provides a feature-matched benchmark of quantum and classical models comprising 284 matched comparisons. We further analyse fidelity-based graph construction and account for the observed quantum-classical parity through effective-dimension and eigenspectrum analyses.

---


### 128. [OpCredit: Operation-Aware Policy Learning for Agentic Knowledge Graph Question Answering](https://arxiv.org/abs/2610.21345)

**<font color=#1a73e8>作者：</font>** Yucheng Li, Mingyuan Li, Xiaxia Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic knowledge graph question answering(KGQA) relies on sequences of executable operations, but trajectory-level rewards obscure their individual contributions. Successful trajectories may contain ineffective operations, while failed trajectories may contain useful ones. To assess individual operations, we propose OpCredit, an operationaware policy-learning framework that combines downstream outcome credit with immediate transition credit: Branch Outcome Credit (BOC) reuses ordinary rollouts to compare terminal task rewards observed after different operations under matched navigation contexts; Frontier Transition Credit (FTC) measures operation-induced changes in answer-conditioned frontier potential. The two complementary signals jointly supervise the corresponding decision spans during training, while inference uses only the learned policy and standard KG interface. Experiments on ComplexWebQuestions, WebQSP, and GrailQA across three backbones demonstrate consistent improvements in KGQA performance.

---


### 129. [Hierarchical Graph Convolutional Network Approach for Detecting Low-Quality Documents](https://arxiv.org/abs/2610.21350)

**<font color=#1a73e8>作者：</font>** Jaeyoung Lee, Joonwon Jang, Misuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consistency within a document is a crucial feature indicative of its quality. Recently, within the vast amount of information produced across various media, there exists a significant number of low-quality documents that either lack internal consistency or contain content utterly unrelated to their headlines. Such low-quality documents induce fatigue in readers and undermine the credibility of the media source that provided them. Consequently, research to automatically detect these low-quality documents based on natural language processing is imperative. In this study, we introduce a hierarchical graph convolutional network (HGCN) that can detect internal inconsistencies within a document and incongruences between the title and body. Moreover, we constructed the Inconsistency Dataset, leveraging published news data and its meta-data, to train our model to detect document inconsistencies. Experimental results demonstrated that the HGCN achieved superior performance with an accuracy of 91.20% on our constructedInconsistency Dataset, outperforming other comparative models. Additionally, on the publicly available incongruent-related dataset, the proposed methodology demonstrated a performance of 92.00%, validating its general applicability. Finally, an ablation study further confirmed the significant impact of meta-data utilization on performance enhancement. We anticipate that our model can be universally applied to detect and filter low-quality documents in the real world.

---


### 130. [Honesty is the Best Policy ... or is it? Demand Management for Probabilistic Service Options](https://arxiv.org/abs/2610.21351)

**<font color=#1a73e8>作者：</font>** Daniela Sailer, Robert Klein, Claudius Steinhardt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To enable well-informed customer choices and redistribute demand across service options, providers can display probabilities regarding predicted service levels at the time of booking, effectively offering probabilistic service options. In many service settings, the underlying truthful probabilities endogenously depend on the system state, rather than being static product attributes controlled by the provider. While customers rely on this information when making decisions, they cannot readily verify its accuracy. Consequently, providers may be tempted to manipulate the displayed probabilities to guide customers' choices in their favor, creating a novel lever for demand management. In this work, we model the resulting problem as a sequential decision process, define truthful probabilities recursively, and introduce transparency constraints that limit their distortion. Because the exact computation of truthful probabilities is intractable for realistic settings, we develop an adapted reinforcement learning algorithm to approximate them. Furthermore, we propose a sampling-based mixed-integer program to optimize the information communicated by the provider in each state. Our framework enables providers to gauge the benefits of dynamically disclosing probabilistic information at the time of booking and sheds light on incentives for manipulation. Our computational study is motivated by out-of-home delivery, i.e., the delivery to parcel lockers or shops, and reveals a trade-off between individual-level transparency and aggregate customer utilities.

---


### 131. [L2GSSL: Label-Efficient Local-to-Global Self-Supervised Learning for Volumetric Healthcare Data](https://arxiv.org/abs/2610.21356)

**<font color=#1a73e8>作者：</font>** Po-Cheng Cheng, Hung-Hsuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Healthcare institutions routinely accumulate high-dimensional computed tomography (CT) volumes, but only a fraction can be annotated by experts. We present L2GSSL, a local-to-global self-supervised learning framework that leverages unlabeled volumes by decomposing pretraining into intra-slice and inter-slice representation spaces. A slice encoder learns view-invariant local features, and a global encoder aggregates the resulting tokens to model volumetric context. The stop-gradient isolates the local space from the global objective, while slice-wise execution and a three-phase schedule support training under constrained GPU memory. On LIDC-IDRI lung nodule malignancy classification, L2GSSL reaches $0.9229$ AUROC with only $10\%$ of the labels and $0.9377$ with $25\%$, exceeding the volume-level VICReg by $0.0229$ and $0.0294$, respectively. With all labels, the strongest supervised baseline exceeds L2GSSL by only $0.0044$ AUROC, consistent with self-supervised pretraining providing its greatest value when annotations are limited. Without adaptation to the external LNDb cohort, a model fine-tuned on $25\%$ of LIDC-IDRI obtains $0.8138$ AUROC and $0.7589$ AUPRC, improving over the strongest evaluated self-supervised baseline by $0.1130$ and $0.0954$. Experiments across data sources, thoracic and abdominal anatomy, downstream tasks, and two backbones examine healthcare-data variety, while lesion-slice masking shows that the predictions depend on lesion-bearing content.

---


### 132. [CoDeFont: One-Shot Font Generation via Multi-Scale Factor-Specific Representation Learning](https://arxiv.org/abs/2610.21364)

**<font color=#1a73e8>作者：</font>** Rejoy Chakraborty, Prasun Roy, Saumik Bhattacharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-shot Font Generation (OFG) aims to synthesize a target glyph by transferring the stylistic characteristics of a single reference glyph while preserving the structure of the target character. However, accurately capturing font style from a single reference image remains challenging due to the limited stylistic information available in a single glyph, and this challenge is further amplified for complex scripts. We propose CoDeFont, a script-agnostic OFG framework that addresses this challenge through multi-level style-content factorization and progressive style-content reconciliation. CoDeFont independently aggregates complementary style and structural information across multiple spatial levels to obtain factor-specific representations, while a contrastive objective explicitly encourages separation between style and content embeddings. During reconstruction, the disentangled representations are progressively injected through multi-level style conditioning, enabling stylistic information to be incorporated at different decoding resolutions while preserving the underlying glyph structure. We evaluate CoDeFont on structurally distinct Bengali and Latin scripts across seen and unseen font styles. Extensive quantitative and qualitative analyses demonstrate consistent improvements over existing state-of-the-art methods, highlighting the effectiveness of the proposed framework for OFG across diverse writing systems.

---


### 133. [SATOR: Backpropagation-Free 3D Test-Time Adaptation via Sample-Adaptive Token Routing](https://arxiv.org/abs/2610.21367)

**<font color=#1a73e8>作者：</font>** Inseok Kong, Geunyoung Jung, Jiyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) mitigates the performance degradation of source-pretrained models on unlabeled test data under distribution shifts. Recent backpropagation-free token-purging methods address 3D point cloud distribution shifts by filtering unreliable tokens. However, their reliance on predefined purge-size candidates requires multiple forward passes per sample and increases inference cost. We propose SATOR (Sample-Adaptive TOken Routing), a source-free and backpropagation-free 3D TTA framework that eliminates this search by deriving both the partitioning threshold and routing decision directly from each sample. SATOR computes token abnormality scores from complementary attention and geometric relation graphs. It then derives a sample-specific partition into retained and pruned tokens via Otsu-based separability, without evaluating candidate sizes. Keep-ratio-calibrated routing then selects the pruned prediction only when its entropy, penalized by the keep ratio, is lower than that of the original prediction. Experiments on ModelNet40-C, ScanObjectNN-C, and ShapeNet-C demonstrate that SATOR achieves state-of-the-art accuracy on three 3D corruption benchmarks.

---


### 134. [Same Target, Different Origins: Aligning Latent Rollout for Consistent PDE Emulation](https://arxiv.org/abs/2610.21370)

**<font color=#1a73e8>作者：</font>** Xinying Li, Jing Xu, Wenjun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE solvers commonly generate multi-step predictions through autoregressive rollout, recursively applying a learned evolution operator and feeding each prediction back as input for the next step. Approximation errors can therefore propagate through the rollout, causing predictions at a shared target time to depend on their temporal origins and rollout depths. For a well-posed deterministic PDE flow, however, states at different times along the same physical trajectory should, under exact evolution, reach the same target state. To this end, we propose Align Latent Rollout (ALR), a regularization approach that promotes consistency across rollout origins through the neural PDE solver's internal representations. A second-order Taylor analysis of latent discrepancy propagation motivates two objectives: zeroth-order latent state consistency, which aligns representations at a shared target time, and first-order latent dynamics consistency, which aligns local evolution responses to shared perturbations. ALR can be integrated into different neural PDE solvers by regularizing suitable internal representations, without modifying their backbone architectures. Experiments across multiple PDE benchmarks and neural-operator backbones show that ALR improves prediction accuracy while reducing shared-target discrepancies across rollout origins.

---


### 135. [Does Compression Imply Generalization? A Minimum Description Length Perspective](https://arxiv.org/abs/2610.21376)

**<font color=#1a73e8>作者：</font>** Lincen Yang, Jiayang Shi, Nan Pu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central question in modern learning theory is what notion of compression, if any, explains why over-parameterized neural networks generalize. Existing answers measure complexity at different levels, ranging from weights to representations; however, estimating the associated quantities either requires held-out data in principle or relies on the challenging (ultra) high-dimensional mutual information estimation. To overcome these challenges, we approach the question through the minimum description length (MDL) principle, and specifically, we propose the prequential regret as a complementary signal that is computable from the training trajectory alone. We establish that, in the (nearly) interpolating regime, the expected prequential regret upper-bounds the description length of the trained parameter under the algorithm-induced distribution, and that this description length translates into a high-probability generalization bound in the PAC-MDL setting. Along the way, we show that the encoder-complexity correction recently added to the algorithm-level information bottleneck (IB) is upper-bounded by an MDL parameter description length, \new{bringing together} the two views of compression from MDL and IB. Empirically, the prequential regret tracks the generalization error on CIFAR-10 and CIFAR-100, with Pearson correlations exceeding 0.9.

---


### 136. [RDL-Bench: A Benchmark for Task-Aware Question Answering over Relational Databases](https://arxiv.org/abs/2610.21382)

**<font color=#1a73e8>作者：</font>** Yao Cheng, Siqiang Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational databases (RDBs) remain the primary infrastructure for storing and managing structured data across enterprise and scientific domains. Natural-language (NL) interfaces to RDBs aim to let users ask questions without writing SQL, but real user needs go beyond SQL-style lookup: some questions require reasoning over the observable database state, while others require predictive inference from historical relational records under temporal constraints. Existing benchmarks address these goals in isolation. To address this gap, we introduce RDL-Bench, a benchmark for task-aware question answering (QA) over real RDBs. RDL-Bench organizes diverse user questions into reasoning-oriented questions, whose answers are determined by the current database state, and prediction-oriented questions, whose answers depend on future outcomes under temporal constraints. Each instance contains an NL question, task metadata, schema information, temporal context, either executable evidence or target-construction logic, and denotation-level ground truth. RDL-Bench supports two evaluation settings: native solvers under their intended capabilities, and task-aware modular systems where a router dispatches each question to an appropriate execution module.

---


### 137. [AdapTest: Supporting Designers in Authoring and Evaluating Environmentally Responsive User Interfaces for Extended Reality](https://arxiv.org/abs/2610.21386)

**<font color=#1a73e8>作者：</font>** Jungwoo Rhee, Guhn Lee, Yumin Jung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) headsets increasingly host familiar 2D user interfaces as windows floating in physical environments. However, their usability depends on environmental conditions that designers cannot fully control. Current design workflows often separate how a variant is designed from how it actually looks in the target environment. We present AdapTest, an in-situ authoring and testing tool that lets designers select interface elements, define when and how they change, compare the resulting variations, and test their activation without coding. Based on prior research and a formative study with 12 interface designers, the system targets three key environmental variables: distance, lighting, and occlusion. We evaluated AdapTest against a desktop design and in-headset preview workflow in a within-subjects study with 12 designers. Compared with the baseline, designers accounted for a wider range of environmental factors, addressed more overlapping conditions, and repeatedly tested and revised their designs in place; there were no significant differences in workload or usability despite longer sessions. Our work contributes an integrated, designer-centered approach to adapting, comparing, and validating environmentally responsive XR user interfaces.

---


### 138. [Matoi: Selective Revalidation of Consequence Evidence for Agent Authorization](https://arxiv.org/abs/2610.21394)

**<font color=#1a73e8>作者：</font>** Zexun Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Matoi separates reusable consequence evidence from current execution authority and durable occurrence history. Its finite query-aware contract covers branches, ordered collections and negative lookups. A consumer reuses only its own checked evidence whose observations remain valid; signed requests, live grants, quota and uncertain outcomes remain separate obligations. Conditional correctness arguments distinguish locally serialized claims from nontransactional remote effects. Two studies strengthen cost attribution and domain evaluation. A 1,440-cell matched-wire study repeats 144 authored inputs. With compact input bytes identical, reuse reduces complete lifecycle cost by 3.49 percent in JS and 1.79 percent in Python. Combined representation/reuse reductions against full proof are 10.87 and 16.53 percent; five of twelve family intervals for the matched comparison cross one in each language. A prospectively frozen AgentDojo Banking mapping covers 5/16 user plans and 7/9 attack plans. Both governed strategies preserve five exact benign transfers and refuse 35 reused attack-plan/policy crosses. Pre-satisfied utility predicates are reported separately from completed work. These are original scripted synthetic tools, not autonomous agents or a real bank. Earlier studies retain cheaper protected-cache alternatives, policy-compatible phishing, provider duplication and post-claim revocation. Separate JS/Python consumers establish finite-profile interoperability within the same project; durable recovery rechecks evidence and retains uncertain reservations. The results support a bounded, auditable reuse and execution contract, not a new general incremental algorithm, arbitrary-tool closure, atomic third-party commitment or production superiority.

---


### 139. [Climate Physicalization: Bridging Tangible Interaction and Data Visualization for Environmental Communication](https://arxiv.org/abs/2610.21401)

**<font color=#1a73e8>作者：</font>** Milena Vuckovic, Marlene Huber, Fabrizia Bando-Bechtold 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Raising awareness of climate topics, such as urban heat mitigation, requires communicating complex data to a broad audience. Data physicalization has emerged as a novel method to connect audiences to such complex topics through tangible forms while also leveraging interactivity to foster deeper engagement. This paper introduces an situated geospatial thermal physicalization prototype, designed to enhance communication and education of environmental information through hands-on engagement. The physical model depicts a 3D model of an urban neighborhood, with radiation data represented as a layered contour structure. The model incorporates three interchangeable climate adaptation scenarios, alongside an externally mounted, electronically driven solar path representation featuring multiple discrete LEDs that can be switched on and off at will. To investigate how people engage with the model, we conducted a hands-on qualitative lab study with 16 participants, using think-aloud, observational, and questionnaire protocols. Overall, participants responded very favorably to the model, highlighting the novelty of the visualization approach and its capacity to improve the interpretability of the presented information.

---


### 140. [Fault Detection and Bit-Error Rate Diagnostics in Optical Wireless Links Using Edge-AI](https://arxiv.org/abs/2610.21402)

**<font color=#1a73e8>作者：</font>** Sarthak Bhattarai, Sheshadri Shikhar Bandyopadhyay, Suprabh Dhakal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optical Wireless Communication (OWC) systems provide high-bandwidth, spatially secure, and RF-interference-free digital transmission. However, direct free-space optical links suffer from extreme sensitivity to line-of-sight disruptions, optical attenuation, high ambient light saturation, and transmitter-receiver misalignment. Traditional channel diagnostic frameworks rely on external computing nodes or cloud-based processing, which introduces severe diagnostic latency and reduces edge node autonomy. This paper presents an autonomous, self-diagnosing optical wireless receiver node that integrates physical-layer signal telemetry extraction with an on-device TinyML classification engine. Built around an ESP32-S3 microcontroller, the receiver recovers 1000 bit/s On-Off Keying (OOK) digital payloads using a 5-sample majority voting mechanism while concurrently extracting real-time channel features: Bit Error Rate (BER), received signal voltage (Vsignal), Signal-to-Noise Ratio (SNRdB), and ambient light baseline (Lambient). Evaluated against a Random Forest baseline (77.22% accuracy) and a floating-point neural network (78.48% accuracy), a post-training INT8 quantized TensorFlow Lite Micro model occupying only 3.32 kB of SRAM runs directly on the receiver firmware. The quantized model achieves 74.68% overall accuracy across four distinct operational conditions: normal transmission, optical filter attenuation, ambient light interference, and severe obstruction/misalignment. On-device deployment tests confirm real-time, deterministic fault classification, establishing a practical approach for self-aware optical IoT nodes.

---


### 141. [Beyond Invariance: Factor-wise Selective Treatment of Shifts for Multimodal Learning](https://arxiv.org/abs/2610.21403)

**<font color=#1a73e8>作者：</font>** Guimin Hu, Qiwei Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distribution shifts pose a fundamental challenge to robust multimodal learning. Existing methods typically promote invariance by suppressing environment-dependent variations, implicitly applying a uniform treatment to shifted information. However, shifted information can have different predictive consequences: some contributes little to prediction, some remains reliably informative, and some exhibits environment-dependent predictive effects. This raises a fundamental question: which shifted information should be suppressed, preserved, or attenuated? To address this question, we propose FaShift, a factor-wise shift framework that diagnoses latent representation factors according to their distributional changes, intervention effects, and cross-environment stability. By factorizing multimodal representations and evaluating these complementary properties, FaShift distinguishes non-predictive factors, stably predictive factors, and predictively useful but unstable factors. It then selectively suppresses, preserves, or attenuates their contributions, rather than enforcing uniform invariance. Experiments on MOSI, MOSEI, and CH-SIMS show that FaShift achieves the best ID accuracy and F1 across all three datasets. Compared with the strongest competitors reporting OOD results, it improves OOD accuracy/F1 by 1.5/3.6 points on MOSI and 1.7/2.7 points on MOSEI, while achieving the best reported OOD accuracy and F1 on CH-SIMS.

---


### 142. [CLAD: Keypoint Matching Using Global Line Correspondences](https://arxiv.org/abs/2610.21409)

**<font color=#1a73e8>作者：</font>** Masaki Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional keypoint descriptors, such as SIFT (Scale-Invariant Feature Transform) and ORB (Oriented FAST and Rotated BRIEF), are computed from local image patches. They may be unreliable in scenes with repetitive patterns or weak textures, where patches at different locations can look similar. We propose the Contextual Line-Assisted Descriptor (CLAD), a keypoint matching method that addresses this problem by using global geometric context from line correspondences. CLAD represents each keypoint with a vector whose elements indicate its proximity to matched lines. It can therefore use the keypoint's spatial relationships to the lines in the scene. We use HOME (Hough-space One-dimensional Matching of Extrema) to detect both clear and weak linear structures and to establish enough line-to-keypoint associations to represent this context. Evaluations on the TUM RGB-D SLAM dataset and outdoor video sequences show that CLAD provides geometrically consistent matches that complement those obtained with traditional local descriptors. In repetitive scenes, where local descriptors may not distinguish similar patches, CLAD uses global structure to improve matching reliability. The method is computationally lightweight and practical to implement.

---


### 143. [Learning to Forecast on Multiple Spatiotemporal Hierarchies](https://arxiv.org/abs/2610.21414)

**<font color=#1a73e8>作者：</font>** Valentina Moretti, Cesare Alippi, Andrea Cini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical forecasting exploits aggregation structures that expose multiple views of the same underlying spatiotemporal forecasting problem, while ensuring coherence among forecasts. Individual series provide fine-grained information, while progressively coarser aggregates reveal temporal and spatial patterns at different scales. In the associated deep learning architectures, the hierarchy determines which aggregate series are available and how they are processed together with individual series (e.g., through reconciliation or message-passing operators). Different hierarchies thus provide distinct learning signals and inductive biases for forecasting the same collection of time series. Nonetheless, existing architectures are typically trained on a single, often fixed, structure. In this work, we propose a graph deep learning framework that leverages variations across hierarchies as multi-task regularization. We show that jointly learning across these structures can reduce over-specialization to any single hierarchy and improve forecasting performance. Indeed, training across hierarchies provides an inductive bias toward representations that are useful across different structures, and as such, generalize better. Making forecasts coherent with the aggregation constraints for each sampled hierarchy is computationally expensive: to complement the framework, we propose a novel operator-based on a top-down approach-that produces coherent forecasts with linear time and space complexity w.r.t. the hierarchy size. Experiments show that our approach improves forecasting accuracy over training on a single structure and is competitive with current state-of-the-art methods.

---


### 144. [Where, How, and When: Query-Guided Grounding for Video Understanding](https://arxiv.org/abs/2610.21422)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding video content requires reasoning at multiple levels of granularity, from identifying objects to interpreting their interactions and localizing when specific actions occur. This thesis studies three query-guided grounding tasks that answer where key objects are (object-level grounding), how they interact (relationship-level grounding), and when specific moments occur (moment-level grounding). For object-level grounding, we present QDETRv, a query-guided extension of the Detection Transformer for one-shot localization of unseen objects in videos, which combines query-context fusion, a memory module for temporal consistency, and unsupervised pretraining on synthetic object trajectories. We further propose the Temporal Object-Aware Vision Transformer (TOViT) for few-shot video object detection, which builds on a language-aligned open-set vision encoder and propagates high-confidence object features across frames. For relationship-level grounding, we introduce few-shot referring relationships in videos: given a (subject, predicate, object) query and a few support videos sharing the predicate, the entities are localized by optimizing a T-partite random field using a meta-learned relation network with query-conditioned translational embeddings, Global Semantic Aggregation, Local Localization Aggregation, and belief-propagation-based message passing. For moment-level grounding, we propose the Moment Alignment Transformer (MATR) for video-to-video moment retrieval, which uses dual-stage Dynamic Time Warping for pre- and post-fusion alignment, learnable queries for boundary prediction, and self-supervised pretraining with temporal augmentations; MATR also extends to text-to-video moment retrieval with performance comparable to, or better than, the state of the art. These contributions advance query-guided video understanding across spatial, relational, and temporal grounding.

---


### 145. [ManiFusion: Unlocking the High-Throughput Generation via Superposition in Manifold Space](https://arxiv.org/abs/2610.21433)

**<font color=#1a73e8>作者：</font>** Minkyu Kim, Baekseung Kim, Junhoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve high-quality image generation but remain computationally expensive due to iterative denoising across many timesteps. Existing acceleration methods mainly reduce per-sample latency, but gains along this axis are becoming saturated. We instead explore an orthogonal throughput-oriented direction by processing multiple samples within a single denoising evaluation. To this end, we propose ManiFusion, a backbone-agnostic framework for multi-sample generation through fused-space computation. ManiFusion jointly processes multiple samples by fusing them before the denoising backbone and separating them afterward through unfusion. We provide a geometric perspective on how multiple samples can share a fused representation while retaining the information needed to guide their individual generation trajectories. To better align fusion allocation with denoising stages, ManiFusion uses Trajectory-Fusion Scheduling (TFS), which dynamically adjusts fusion factors throughout sampling. ManiFusion generalizes across diffusion families, including both U-Net and transformer backbones in pixel and latent spaces. We further show that ManiFusion composes with existing acceleration methods and reaches throughput regimes unattainable by prior approaches with minimal quality degradation.

---


### 146. [RLDF: A Region-Level Deepfake Dataset and Benchmark for Partial-Face Manipulation Detection](https://arxiv.org/abs/2610.21438)

**<font color=#1a73e8>作者：</font>** Shukesh Reddy, Abhijit Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deepfake detection models are built upon manipu- lated images that are tampered with either exclusively fully swapped or fully synthesised faces, which leads us to an open question: Can off-the-shelf deepfake models detect manipulation effectively while tampering is confined to a local facial sub-region? To fill this gap, we introduce RLDF (Region-Level Deepfake), the first dataset for region-level deepfake evaluation. Employing the proposed region-aware partial swap synthesis model, we generate over 2M par- tial face-swap images by using eight face-swapping meth- ods. Altogether, we considered seven face regions, among which there are four discrete regions (eye, nose, mouth and eyebrow) and four composite facial regions (eye and nose; eye, nose and mouth; eye, nose, mouth and eye- brow; and full face). In addition, we define three evalu- ation protocols and benchmark 12 state-of-the-art detectors across the five popular standard cross-dataset evaluations, DF40, and the proposed RLDF, providing a comprehen- sive audit of where and why existing detectors underper- formed. Our evaluation reveals that existing detectors fail to generalize consistently across partial facial regions, re- sulting in an overall drop of 10.5% AUC and 10% accu- racy under region-level evaluation. Further, we propose a mask-guided cross-attention model as a baseline approach that can effectively detect region-level manipulation. The proposed dataset, code, and checkpoints are available at this https URL.

---


### 147. [V-SHARE: Provable Convergence Guarantees for Advantage-based Algorithms](https://arxiv.org/abs/2610.21448)

**<font color=#1a73e8>作者：</font>** Kintan Saha, Hamed Masoudi, Xinyi Sheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning, advantage-based value-learning methods, unlike standard Q-learning, share information across actions by decomposing the action-value function into a state-dependent value component and action-specific advantages. While this mechanism has proven effective in both tabular and deep reinforcement learning, its theoretical understanding remains incomplete. We introduce V-SHARE, an advantage-based value-learning algorithm that combines cross-action value sharing with an importance-weighted Bellman-residual correction. To our knowledge, we provide the first complete theoretical characterization of an advantage-based algorithm, including both asymptotic convergence and non-asymptotic finite-sample guarantees. We identify a regime in which V-SHARE mitigates the rare-action bottleneck of asynchronous Q-learning and uncover a contraction--variance tradeoff between stronger deterministic contraction and increased importance-weighting noise. Motivated by this tradeoff, we develop decreasing residual-preconditioning schedules that combine faster early contraction with lower asymptotic noise. We further develop a two-timescale analysis that removes the single-timescale residual-weight threshold while preserving convergence guarantees. Experiments on discrete Markov decision processes (MDPs) and deep reinforcement-learning benchmarks corroborate our results.

---


### 148. [PET Quantification-Preserving Registration for Longitudinal Whole-Body PSMA PET/CT](https://arxiv.org/abs/2610.21451)

**<font color=#1a73e8>作者：</font>** Fryderyk Kögl, Anna Reithmeir, Daniel M. Lang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We adapt the diffeomorphic coarse-to-fine LapIRN architecture for longitudinal whole-body PSMA PET/CT registration in the Learn2Reg 2026 PSMAReg challenge. The method combines affine pre-registration, multi-modal deformable registration, and test-time instance optimization. We further introduce PET biomarker preservation losses for metabolic tumor volume (MTV) and total lesion glycolysis (TLG), including Jacobian-based constraints, and a per-structure rigidity regularization for skeletal structures. The submitted configuration achieved 81.0% DSC and 6.17 mm HD95, with MTV and TLG errors of 3.3% and 3.3%, respectively, on our evaluation protocol. Code is available at this https URL.

---


### 149. [Benchmarking Post-Quantum Key Encapsulation in S3-Compatible Object Storage under Client Concurrency](https://arxiv.org/abs/2610.21457)

**<font color=#1a73e8>作者：</font>** Revanth Reddy Lingala, K. Gangadhara Rao, Padigela Srujan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data encrypted today with classical public-key algorithms could be decrypted once large quantum computers exist. Cloud object stores keep data for years, so the client-side encryption that protects it must move to post-quantum algorithms such as ML-KEM, which adds a key-encapsulation step and a larger ciphertext to every stored object. So far, the cost of ML-KEM has been measured for the algorithm on its own and for securing network connections, but not for encrypting each object in a storage system that serves many clients at once. It has therefore been unclear whether ML-KEM slows such a system, under which conditions, and why. We address this problem by measuring per-object ML-KEM against classical key exchange on an S3-compatible object store, with two client implementations, two processor types and up to 500 concurrent workers, using pre-registered experiments and statistical equivalence tests. ML-KEM reduced throughput only when the client's processor was at or near full load, with one unexplained exception, and then by 4.0 to 4.9% in our main client. Controlled experiments on one processor type traced most of that loss to the way the software library was called, and a second, native client showed that the size of the loss depends on the implementation. The lasting cost is storage: 1,056 more bytes per object than with classical key exchange. The results cover two clients, one single-node store and one cloud provider.

---


### 150. [Can Visual Generation Expand What Unified Multimodal Models Know?](https://arxiv.org/abs/2610.21459)

**<font color=#1a73e8>作者：</font>** Wenkai Li, Wenyi Hong, Zhuoyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) receive image-generation supervision that exposes them to visual information not fully documented in text. Can learning to generate images expand what pretrained models know? We introduce Knowledge Transfer Probing (KTP), a controlled protocol that supplies new knowledge through image-generation training and tests its accessibility through text-only question answering. Across seven knowledge categories and three UMMs, we observe direct but uneven transfer from visual supervision to language. Motivated by these observations, we successively introduce Textual Alignment and Interleaved Image--Text Alignment, which connect generation and answering through shared knowledge and interleaved responses, respectively. Guidance on selected entities can improve knowledge access on other entities without QA supervision, with additional gains from interleaved alignment. Further analysis shows that knowledge correctly reproduced in images is often more accessible through text, although substantial gaps remain between the two forms of access. These findings support visual generation as a source of knowledge beyond textual supervision, and motivate joint investigation of training data design and model architecture to make this knowledge more broadly accessible.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
