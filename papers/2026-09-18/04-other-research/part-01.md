# 📦 其他研究 | 2026年09月18日

> 本类共 **223** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 1. [DANTINOX: A Unified Framework for Multi-Paradigm Language Modeling](https://arxiv.org/abs/2609.17535)

**<font color=#1a73e8>作者：</font>** Marco Simoni, Aleksandar Fontana, Giulio Rossolini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language generation research increasingly spans three paradigms: autoregressive decoding, discrete masked diffusion, and continuous flow-matching. Comparing them is difficult because each lives in a separate codebase, so measured differences often reflect implementation details rather than the paradigms themselves. We present DantinoX, an open-source JAX/Flax library in which a single modular Transformer backbone serves all three paradigms. Switching the generation paradigm, attention mechanism, or hardware topology requires only a configuration change, while the backbone architecture, tokenizer, initialization strategy, and training infrastructure remain consistent. This enables controlled cross-paradigm comparisons within one API for training, streaming inference, and benchmarking.

---


### 2. [MudawanSn: A Gold-Standard Wolof-Arabic Parallel Corpus for Machine Translation](https://arxiv.org/abs/2609.17539)

**<font color=#1a73e8>作者：</font>** Mouhamed Mbaye, Thierno Diop  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MudawanSn, a gold-standard resource of 1,271 sentence-aligned pairs manually translated from Wolof into Modern Standard Arabic (MSA). The source texts are drawn from the MasakhaNER corpus and cover politics, society, religion, and sports in Senegalese news discourse. Although multilingual resources such as FLORES-200 and NTREX include both Wolof and Arabic, no publicly available parallel corpus is specifically designed for the Wolof-Modern Standard Arabic language pair. We describe the corpus construction protocol, sentence alignment procedure, and quality-control workflow. We benchmark four machine translation systems spanning three architectural families: NLLB-200 (600M), mT5-base, and two AfriNLLB variants, showing that fine-tuning on MudawanSn yields substantial improvements in both translation directions. The best-performing model, AfriNLLB-12, achieves 7.76 BLEU and 30.72 chrF++ for Wolof-to-Arabic, and 8.75 BLEU and 33.08 chrF++ for Arabic-to-Wolof. The corpus is released under the CC BY-NC license and is publicly available on Hugging Face and GitHub.

---


### 3. [Selective Prediction and Uncertainty-Aware Referral for Pap Smear Classification](https://arxiv.org/abs/2609.17545)

**<font color=#1a73e8>作者：</font>** Nisreen Albzour, Sarah S. Lam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for cervical cytology are almost always evaluated as if every prediction must be acted upon, yet a screening system deployed alongside a cytopathologist need not classify every slide: it can defer the cases it is least certain about. Evaluating such a system requires asking not only how often it is correct, but whether its confidence ranks its errors to the bottom. This paper studies selective prediction and uncertainty-aware referral on the Herlev Pap smear dataset under a binary Normal-versus-Abnormal formulation. Two lightweight transformer backbones (Swin-Tiny, TinyViT-5M) are fine-tuned on Herlev from ImageNet-pretrained weights with weighted random sampling, calibrated by post-hoc temperature scaling fit on a held-out calibration subset, and compared against a soft-voting ensemble of both models. Discrimination is reported alongside expected calibration error (ECE) and, as the primary endpoint, the area under the risk-coverage curve (AURC). No statistically significant difference was detected between the two configurations in accuracy or macro-F1, yet the ensemble halves AURC (0.0022 vs. 0.0045, a 51.8% reduction, lower in all five folds) and extends the coverage at which zero errors are made from 18.3% to 72.8% of the pooled test predictions. The same ensemble is nonetheless worse calibrated in absolute terms (ECE 0.0339 vs. 0.0247) and produces more false negatives (14 vs. 10). These results separate two properties that are frequently conflated: the ability to rank predictions by trustworthiness, and the accuracy of the confidence values themselves. Ensembling improves the former while degrading the latter, and the former directly governs the observed risk-coverage tradeoff, whereas the latter governs the interpretation of the reported confidence values.

---


### 4. [A Heisenberg Lift Descriptor for Order Sensitive Online Handwriting Recognition](https://arxiv.org/abs/2609.17565)

**<font color=#1a73e8>作者：</font>** Hassan Ugail, Newton Howard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online handwriting recognition systems typically represent pen trajectories through fixed-length Euclidean shape descriptors that capture the spatial outline of each stroke, but are insensitive to the order in which that outline is produced. Two strokes that trace the same region of the plane in opposite directions are indistinguishable to any such order-blind representation, yet their traversal directions may carry decisive class information in characters where loop orientation and stroke sequencing matter. This paper introduces a Heisenberg-lift framework that addresses this gap through a compact, interpretable, order-sensitive augmentation for online pen-trajectory features. The simplest instance is the terminal signed area, a single parameter-free scalar appended to an existing Euclidean descriptor at negligible computational cost. Evaluated on two standard online handwriting benchmarks, this one-scalar addition, consistently raises classifier accuracy over the Euclidean baseline. On the hardest character pair in our study, the letters o and y, the signed area alone achieves perfect separation while the Euclidean baseline falls short. The advantage grows further under additive coordinate noise, a practically relevant degradation in pen-trajectory data. A richer fifteen-dimensional extension, derived from a noncommutative Heisenberg-group subdivision scheme, provides additional gains in noisy and loop-structured conditions. Dimension-matched statistical controls confirm that all improvements reflect geometric information rather than feature-count inflation. The resulting descriptor is lightweight, closed-form, and directly interpretable, making it a practical augmentation for online handwriting and related document-trajectory classification pipelines in which the direction of stroke execution carries discriminative information.

---


### 5. [Adaptive Interpolatory Curve Subdivision with Learned Local Angles](https://arxiv.org/abs/2609.17566)

**<font color=#1a73e8>作者：</font>** Hassan Ugail, Newton Howard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Curve subdivision is pivotal in computer graphics for generating smooth geometric objects from control polygons. Interpolatory subdivision is especially attractive because the refined curve is guaranteed to pass through the designer's control points. Classical four-point and six-point schemes preserve this property, but their behaviour is governed by a single global tension parameter, limiting their ability to adapt across flat regions, sharp turns and varying local geometries. We introduce an adaptive local-angle formulation that keeps the interpolatory structure intact while learning how each new vertex should be inserted. A compact edge-wise predictor assigns one insertion angle per edge, while the original vertices are copied exactly at every refinement level. Interpolation is therefore a structural property of the operator and does not depend on the trained weights. The same predictor is used with geometry-specific geodesic primitives on the Euclidean plane, the two-sphere and the Poincaré disk. Under a matched-density evaluation protocol, the method reduces nearest-neighbour error by factors of five to seventeen over the best validation-tuned fixed-tension baseline, and by about 1.8 over centripetal Catmull-Rom in the Euclidean case. It also substantially reduces bending energy and tangent roughness, while remaining competitive with separately trained per-geometry models.

---


### 6. [Where Grokking Happens: Distributed Utility and Fourier Recoding Without a Module Switch](https://arxiv.org/abs/2609.17571)

**<font color=#1a73e8>作者：</font>** Dekun Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Where in a Transformer is the change from memorization to generalization functionally expressed? We introduce Transition Games--behavior-aligned exact activation games with paired non-generalizing controls--and find distributed utility gain with a prospective block-0 attention bias; selected degree-two modes account for 67--92% of its addition contrast across replacement games, and a disjoint exact path study confirms that block-1 MLP mediates more of their effect than all other tested downstream paths in 12/12 pairs. The sharper "MLP memorizes, attention generalizes" prediction instead reverses (-.331 bits/example at the memory anchor; 0/12 in the predicted direction), while routing onset, global rank collapse, and a prime-invariant architecture ridge also fail, identifying grokking here as spectral recoding of an existing distributed circuit rather than a module switch.

---


### 7. [When the Gradient Sees Rank: Provable Necessity, Causal Recruitment, and Composition in Trained Matrix Memories](https://arxiv.org/abs/2609.17594)

**<font color=#1a73e8>作者：</font>** Samuel Larson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can gradient-based training learn the rank needed to store and compose associations in a matrix memory? In our earlier study, we used a matrix-augmented reasoner on a task that admits a rank-1 solution, leaving this question open. We train matrix memories on $K$ fresh key-value bindings whose exact linear recovery requires $\mathrm{rank}(Z) \geq K$. A fixed linear readout queries a single matrix state without access to the original bindings. Experiments measure recovery by cosine similarity greater than 0.9, a threshold distinct from mathematical equality. Learned effective rank increases with $K$ across the tested grid (Spearman $\rho = 1.0$ at $d = 16$). Training-time rank caps produce a recovery transition near $k = K$: at $d = 8$, $K = 4$, rank 3 gives at most 0.0004 recovery and rank 4 gives 0.97. Four of five seeds retain at least 0.9996 recovery through 21-fold self-application of the trained operator. On the entity subspace, the learned operator has effective rank close to $K$ and approximates the ideal cycle. For the single converged seed capped below $K$, a calculation using the entity-subspace operator and ideal cycle predicts the measured cosine within 0.008 through seven applications. Extending training resolves several initial failures, but recovery still declines at larger matrix dimensions with encoder width fixed.

---


### 8. [Prior-Free Competitive Ratios for Improving Bandits: Scale, Curvature and Horizon Are Free, but Not Jointly Under Noise](https://arxiv.org/abs/2609.17595)

**<font color=#1a73e8>作者：</font>** Xuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the improving multi-armed bandits problem, each of $k$ arms has an unknown nondecreasing, discretely concave reward curve $f_i$, and pulling arm $i$ for the $t$-th time yields $f_i(t)$. For sufficiently long horizons, Blum and Ravichandran (ALT 2025) proved that randomized algorithms achieve an $O(\sqrt k)$ approximation to the best single arm when the scale $m=f^*(T)$ of the optimal arm is known ($T\ge2k$), and $O(\sqrt k\log k)$ when it is not ($T>4k$), against an $\Omega(\sqrt k)$ lower bound. The logarithmic factor is unnecessary: a one-page \emph{probe-and-commit} algorithm achieves competitive ratio $4\sqrt3\,\sqrt k$ for $T\ge2\lfloor\sqrt k\rfloor$, without any knowledge of the scale, and we determine the optimal ratio for every horizon, $\Theta(\sqrt k+k/T)$, also for unknown horizons. Without noise, \emph{no prior is needed at all}: a random-marginal probing algorithm reading neither the scale $m$, nor the concavity-envelope exponent $\beta$ of Blum, Garicano, Ravichandran and Sharma (UAI 2026), nor the horizon $T$, achieves the optimal $\Theta(k^{\beta/(1+\beta)}+k/T)$ simultaneously for every $\beta$ and every horizon. Under the multiplicative noise model of Blum and Ravichandran, probe-and-commit keeps the same all-horizon order $\Theta(\sqrt k+k/T)$ without knowing the noise level (and $\Theta(\sqrt k)$ on the same range), but the price of priors jumps: for any fixed noise level $\varepsilon\in(0,1/2]$, the uniform price of adaptation $\phi_\varepsilon(k)$ --- the worst case over horizons $T\ge16k$ of the loss relative to $k^{\beta/(1+\beta)}$ for algorithms knowing neither $m$ nor $\beta$ --- is $\Theta_\varepsilon(\sqrt{\log k/\log\log k})$, the lower bound asymptotic in $k$ at fixed positive $\varepsilon$ and matched by a nested random-permutation probing algorithm, whereas knowing either $m$ or $\beta$ alone restores a constant price.

---


### 9. [Making Political Text Scaling Comparable: Infrastructure and Hyperparameter Sensitivity for 17 Algorithms](https://arxiv.org/abs/2609.17602)

**<font color=#1a73e8>作者：</font>** Patrick Parschan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational text-based ideal point estimation (CT-IPE) methods are usually compared as named algorithms, yet applying them involves numerous researcher choices that configure how political text is turned into position estimates. This paper argues that CT-IPE methods are better understood as configurable measurement pipelines than as fixed estimators. Building on a large-scale comparative experiment spanning 17 CT-IPE algorithms, 5,537 experimental runs, and approximately 4.25 million left-right position estimates, I describe the shared infrastructure that makes these heterogeneous methods jointly executable and quantify how sensitive their estimates are to alternative hyperparameter choices. Variance-partitioning and SHAP-based sensitivity analyses show that, for most algorithms, hyperparameter profiles explain little residual variance through a shared shift: 13 of the 17 algorithms exhibit ICC values below .10. Where this profile-level sensitivity is present, it is concentrated in a small number of consequential researcher choices, most notably the selection of the underlying language or embedding model, the seed keyword lists that anchor the construct, and the number of topics.

---


### 10. [DualCount: Structurally Consistent Density and Point Modeling for Zero-Shot Object Counting](https://arxiv.org/abs/2609.17613)

**<font color=#1a73e8>作者：</font>** Xuan Cuong Ngo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot object counting aims to estimate the number of objects specified by a text query without category-specific training. Recent approaches primarily rely on density regression or detection-style instance prediction. While effective, density-based models often suffer from spatial ambiguity and background leakage due to weakly regulated mass allocation, leading to fragmented or part-biased representations that increase counting error in complex scenes. In this work, we propose an instance-aware dual-decoder framework that structurally couples density and point representations for zero-shot object counting. Instead of treating density estimation as independent pixel-wise regression, we interpret it as a structured mass allocation problem over a latent set of object instances. Predicted instance centers induce a soft instance-wise decomposition of the density map, upon which we enforce two geometric constraints: (1) per-instance mass conservation, ensuring each object contributes approximately one unit of density mass, and (2) center-of-mass alignment, encouraging each density component to concentrate around its corresponding predicted center. These constraints introduce instance-level geometric consistency and lead to more accurate mass allocation, thereby reducing counting error. Extensive experiments on FSC-147, PUCPR+, and CARPK show that our approach consistently reduces counting error and establishes new state-of-the-art performance in zero-shot object counting.

---


### 11. [Making AI-Assisted Claims Independently Challengeable: Publication Authority and a Protocol for Falsifiable Publication Records](https://arxiv.org/abs/2609.17631)

**<font color=#1a73e8>作者：</font>** Torsten Olivi Tiltack, Yifei Dong, Kun Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted claims can appear authoritative when evidence, analysis, human authorization, presentation, and correction history refer to different states. Provenance, attestation, and transparency expose history but alone do not specify the publication transition examined here. We develop Publication Authority as an exact-state, non-transferable, single-use publication capability and instantiate it in PAC-2026 (Publication-Accountability Calculus), a machine-readable AIJIM Protocol candidate. We evaluate its fourth bounded semantic freeze (SF-4), a fixed-profile specification designed for replaceable bindings. Six obligations govern evidence, runs and artifacts, measurement disclosure, authorization, surface correspondence, and lifecycle continuity. Each yields a target-bound witness, localized counterexample, or localized unverifiability; none can compensate for another. Only a fresh, complete all-pass record derives the permit consumed by one atomic publication transition. We use identity vectors, adversarial cases, finite models, and historical implementations. Ten models explored 110,764 safe reachable states; 76 unsafe configurations produced the expected violation or observer countermodel. A reader surface passing its correspondence check cannot authorize publication unless the accepted record admits that surface. SF-4 separates evidence horizon from verification time and rejects an authentic but causally invalid authorization. A historical predecessor path reproduced 17 frozen authorization-successor outcomes. A later in-house, instance-blind test of known case classes matched all 183 scored expectations; same-host package execution reproduced its 240 archived observations. Results support internal coherence, bounded safety, fault sensitivity, and limited constructibility, but not factual truth, general refinement, blind interoperability, field efficacy, or standards status.

---


### 12. [One Color Preprocessing Improves DSATUR](https://arxiv.org/abs/2609.17633)

**<font color=#1a73e8>作者：</font>** Adam Nouira, Lucas Isenmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Graph Coloring Problem (GCP) is NP-hard and DSATUR stands as one of the fastest heuristics for it despite producing colorings that typically use more colors than state-of-the-art coloring algorithms. We propose SSLD (Semidefinite Spectral Learning with DSATUR), which improves DSATUR by preprocessing a first good color class before letting DSATUR complete coloring the rest of the given graph. We obtain this color class from a Semidefinite Programming (SDP), similar to an SDP used to compute the Lovász theta number. To the best of our knowledge, SSLD is the first approach to improve DSATUR by preprocessing through fixed color classes. We evaluate SSLD against DSATUR and against a naive 1-color-class preprocessing algorithm on DIMACS instances, random graphs (Erdős--Rényi, Watts-Strogatz, Barabási--Albert), Frequency Assignment and Job Shop Scheduling instances. SSLD matches or beats DSATUR in almost every case across over 1600 benchmark instances, and out performs the naive GISD baseline, allows us to confirm the value brought by the SDP-guided choice of the first color class. This quality comes at a runtime cost of roughly 195 times slower that DSATUR, but demonstrating that SDP-guided preprocessing of a first color class is a direction for future improvements.

---


### 13. [Physics-Constrained Digital Twins for Sensor Integrity in Urban Pedestrian Flow: Detecting Stealthy False Data Injection with Conformal Guarantees](https://arxiv.org/abs/2609.17635)

**<font color=#1a73e8>作者：</font>** Oscar Mogollon Gutierrez, Fatemeh Ghasemi, Mohammadhossein Homaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> City pedestrian counting systems now feed economic indicators, planning decisions and safety operations, yet the twins built on top of them treat the incoming stream as ground truth. We study what happens when it is not. We formalise stealthy false data injection for city-scale pedestrian sensing, where the map from latent flow to observation is far more rank deficient than in the power and water networks for which stealth has been characterised. Our twin estimates directed flows on the pedestrian street graph, assimilates counts through a learned graph-localised gain, and is trained against a flow conservation residual that couples metered and unmetered segments. Detection combines the innovation with that residual, and the alarm threshold is set by adaptive conformal calibration rather than by hand. To measure what the physics buys, we define the attack margin, the relative reduction in worst-case corruption of the estimated flow field, achieved against a white-box adversary that optimises directly through the twin. On six years of Melbourne data the margin reaches 0.54 against a single compromised device and falls to 0.19 when a third of the fleet is compromised, on a network where only 1.18 per cent of walkable segments are metered. Replacing the street graph by a distance graph collapses it to 0.09, which shows that the gain comes from the conservation law rather than from locality.

---


### 14. [Lecture notes on Physics Informed Neural Networks, Neural Operators, and their applications](https://arxiv.org/abs/2609.17638)

**<font color=#1a73e8>作者：</font>** Alessandro Bombini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This is the set of lecture notes for the PhD course \href{this https URL}{\textit{Physics Informed Neural Network}, held at the University of Bozen/Bolzano} in the academic year 2025/2026.
The goal of the course was to introduce the concept of Physics Informed Deep Neural Networks (PINN) and Neural Operators (NOs), discuss their implementation from scratch in PyTorch and using advanced ad-hoc developed open-source libraries such as NVIDia PhysicsNeMo to address real-world problems in various fields (engineering, physics, petroleum reservoir). We discuss recent topics such as Mixture-of-Models, Fourier Neural Operators, Physics-Informed Kolmogorov-Arnold Networks (PIKANs) and Fourier Neural Operators.

---


### 15. [State Without a Landlord: An Architecture Proposal for Peer-to-Peer Replication of Durable Workflow State](https://arxiv.org/abs/2609.17645)

**<font color=#1a73e8>作者：</font>** Luca Maraschi, Matteo Collina  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Durable-execution frameworks commonly journal execution steps of a long-running function and reconstruct state by deterministic replay; the journal is therefore the workflow's authoritative state, and in current deployments it typically resides with whichever provider hosts the run. This paper examines what changes if the journal is instead an authenticated, append-only log replicated among the parties to the workflow. We propose an architecture in which runs are chains of single-writer epoch cores; executor succession is governed by quorum-finalized closure certificates; durability, timeout, and checkpoint decisions are carried by explicit certificates rather than implicit trust; and large payloads travel a separate content-addressed distribution plane. A threat model separates what signatures establish (authorship and order) from what they do not (truth of recorded effects). We state the design as a set of typed artifacts and invariants, identify which claims are established by existing systems and which are proposals requiring validation, and define the prototype experiments, including specific adversarial cases, that would validate or falsify the proposal's central mechanisms.

---


### 16. [Regularized Least Squares Training of Quadratic Neural Networks with Applications to System Identification](https://arxiv.org/abs/2609.17654)

**<font color=#1a73e8>作者：</font>** Luis Rodrigues, Zachary Yetman Van Egmond, Mohammad R. Amiri Fard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a least squares approach for the training of quadratic neural networks with regularization. The proposed methodology yields a lower bound on the solution of the training optimization problem for the case where the regularization coefficient is positive. Moreover, it yields closed-form expressions for the approximate solution and its sensitivity The lower bound is tight and the approximate solution is the optimal solution when the regularization coefficient is zero. Having a closed-form expression for the weights reduces considerably the computational time when compared with iterative numerical methods such as backpropagation that can get stuck in local minima. The proposed approach has three main contributions, namely, (i) it yields an analytical expression for the weights, (ii) an analytical expression for the sensitivity of the weights to errors in the data is also provided, (iii) it establishes a connection between the optimization to compute a lower bound and nuclear norm minimization. The proposed least squares training is successfully applied to a nonlinear system identification example where the proposed lower bound is compared with the optimal value.

---


### 17. [DSD: Learning Diverse and Reusable Motor Skills via Diffusion Skill Discovery](https://arxiv.org/abs/2609.17682)

**<font color=#1a73e8>作者：</font>** Sun Woo Kim, Xue Bin Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans efficiently learn new tasks by reusing a rich repertoire of motor skills across different goals and contexts. A similar strategy can also be used to enable simulated characters to efficiently perform new tasks by leveraging reusable motor skills. To support a wide range of downstream tasks, the learned repertoire should be diverse, consisting of distinct behaviors as well as spatial and temporal variation within each behavior. A commonly used method for learning diverse skills is by maximizing the mutual information between skill latents and the states produced by a policy. The marginal state entropy promotes broad behavioral coverage, while the conditional entropy encourages consistent behaviors from each latent. However, directly estimating the marginal state entropy is intractable in high-dimensional control problems. Prior methods therefore rely on indirect latent-space approximations or coarse estimators of the state distribution. These approximations may not effectively promote broad coverage of the state space, resulting in skills with limited behavioral diversity and reduced utility for downstream tasks. In this work, we propose Diffusion Skill Discovery (DSD), a skill discovery method that uses a diffusion model to approximate the entropy gradient of the policy-induced state distribution through score matching. The resulting objective encourages the discovery of skills that produce a broader range of behaviors for high-dimensional humanoid control. The learned skills are reused in two downstream control settings: hierarchical control with a task-specific high-level policy and zero-shot control through latent selection from offline trajectories. Our experiments show that DSD discovers a broader repertoire of reusable motor skills than prior skill discovery methods, leading to the emergence of complex and agile behaviors that can be reused across downstream tasks.

---


### 18. [Accelerating Diffusion Sampling via Speculative Draft Trees](https://arxiv.org/abs/2609.17691)

**<font color=#1a73e8>作者：</font>** Marcello Bullo, Yanxiao Liu, Öykü Sıla Güner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative sampling accelerates diffusion model generation by drafting inexpensive candidate states and correcting them under a coupling that preserves the target distribution exactly, reducing the number of expensive target evaluations. Existing diffusion samplers, notably those based on reflection maximal coupling, are topologically constrained: their lookahead drafts form a chain graph, a single linear sequence, which inherently limits the acceptance rate per target evaluation. We connect speculative sampling in diffusion models to relative entropy coding (REC). This perspective shows the lookahead need not be linear and motivates our central contribution, draft trees, which enrich the candidates considered per round and lower the target function evaluations. We further adopt greedy rejection sampling, an REC algorithm, as the draft-target coupling, improving acceptance while guaranteeing exact target samples. Experiments across diverse target and draft models demonstrate up to 8.3% acceleration over the reflection coupling baseline in practical settings.

---


### 19. [Composite-Gradient Learning for Shared Control Authority Between Deep Reinforcement Learning and Model Predictive Control](https://arxiv.org/abs/2609.17697)

**<font color=#1a73e8>作者：</font>** Giray Önür, Azita Dabiri, Bart De Schutter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated deep reinforcement learning (DRL) and model predictive control (MPC) methods are increasingly used to control autonomous systems by combining their complementary capabilities. DRL learns control policies through interaction with the environment. MPC uses a system model to optimize control inputs while accounting for constraints. In DRL-MPC frameworks with shared control authority, both the DRL agent and the MPC controller each determine part of the control inputs. However, common learning formulations treat MPC as part of the environment and therefore do not explicitly account for MPC's contribution to control or its interaction with the DRL agent. This paper proposes a novel composite-gradient learning (CGL) method that integrates the MPC controller into the learning process by representing the DRL and MPC control inputs as a joint action and accounting for their interaction when updating the DRL agent during training. CGL is evaluated on two multi-class freeway traffic networks with different strengths of interaction between the DRL and MPC control inputs and it is compared with alternative methods that treat MPC as part of the environment or that only partially incorporate MPC into learning. The results show that CGL offers limited benefit under weak interaction, but learns higher-performing control policies than the alternative methods in a subset of training runs under strong interaction, although the average control-performance gains remain modest.

---


### 20. [Participant-Mediated Collection of Sensitive Digital Trace Data: The CANDOR Research Infrastructure](https://arxiv.org/abs/2609.17722)

**<font color=#1a73e8>作者：</font>** Andrew Zhao, Rijul Magu, Ekta Raj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital trace data provide rich measures of behavior in everyday settings, but the research ecosystem supporting their collection is constrained by declining platform API access and a historical reliance on publicly observable data. Participant-mediated data donation offers a complementary approach in which individuals contribute selected portions of their own digital histories to research. Such data can include longitudinal and non-public behavior, span multiple platforms and modalities, and be linked to independently collected study measures, enabling study designs that are difficult to implement using public social media data alone. These opportunities also introduce methodological challenges around participant control, data minimization, heterogeneous platform exports, privacy, and governance, particularly when semantic or multimodal content is necessary to study the construct of interest. We present CANDOR (Collecting and Analyzing Networked Data for Open Research), an end-to-end infrastructure for participant-mediated collection and governance of sensitive digital trace data. CANDOR supports participant-directed selection of platforms, data types, and temporal ranges; modular platform- and modality-specific parsing and de-identification; linkage to independent study measures; and protected processing, storage, and access. We derive design requirements for this class of research and compare CANDOR with existing data donation infrastructures, identifying how different approaches support participant control, data minimization, scientifically necessary data richness, study-design flexibility, and governance. Together, this work provides a methodological and infrastructural framework for using participant-contributed digital traces in behavioral research, particularly when the data needed to address a scientific question are longitudinal, non-public, multimodal, or sensitive.

---


### 21. [A Systematic Evaluation of the COTQ Provincial Land Cover Product: Structural Consistency, Spectral Separability, and Relative Positioning Against ESA, ESRI, and Google Products](https://arxiv.org/abs/2609.17731)

**<font color=#1a73e8>作者：</font>** Étienne Clabaut, Samuel Foucher, Yacine Bouroubi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-resolution land use and land cover (LULC) products derived from Sentinel-2 imagery are widely used for environmental monitoring and land management, yet their performance can vary across regions with complex ecological gradients and heterogeneous surface conditions. In Quebec, these limitations motivated the development of a provincial 10-m land-cover product, the COTQ, designed to support annual monitoring of land occupation and soil artificialisation. This study presents a systematic evaluation of the COTQ product relative to three global 10-m LULC datasets: ESA WorldCover, ESRI LandCover, and Google DynamicWorld. This paper does not introduce a new mapping methodology but focuses on analysing the behaviour and consistency of the COTQ using complementary evaluation approaches. All products are harmonized under a common legend and compared using structural indicators (object-size distributions, shape complexity, Adjusted Rand Index, and Intersection over Union), spectral separability metrics derived from Sentinel-2 reflectance data, and a targeted photo-interpretation of disagreement areas. The analysis is conducted over eight Sentinel-2 tiles selected to represent the main bioclimatic domains of Québec, from temperate and boreal forests to northern tundra environments. The results show that the COTQ exhibits structural and spectral characteristics most similar to ESA WorldCover among the reference global products, while revealing systematic differences linked to class definitions and thematic priorities, particularly for urban areas, wetlands, and rocky or cryptogamic surfaces. This multi-criteria evaluation provides an objective characterization of the COTQ product and clarifies its relative positioning with respect to existing global land-cover datasets for operational land monitoring in Québec.

---


### 22. [Geometry-Driven Shadow Harmonisation for Composited Faces: A Multiplicative, Albedo-Preserving Relighting Pipeline](https://arxiv.org/abs/2609.17740)

**<font color=#1a73e8>作者：</font>** Vijesh KP  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face swapping and face compositing pipelines routinely produce a face that is geometrically well aligned but photometrically implausible: the donor face carries flat, near-frontal studio illumination while the host body and background carry directional scene light. Most existing remedies re-synthesise the face through colour transfer, neural relighting, or inverse rendering, and therefore risk altering identity, skin tone, and texture. We present a conservative alternative: geometry-driven form-shadow injection. The pipeline never repaints the face. It estimates a per-pixel gain field $g\in[g_{\min},1]$ from a rasterised 3D face proxy and multiplies it channel-uniformly onto linear RGB, so the operator can only darken and cannot shift chromaticity. A dense landmark mesh is rasterised into a depth buffer, from which we derive surface normals, a cavity term, and screen-space cast shadows. Key-light direction is estimated from host-side cues (body, background, hair halo); on-face cues are downweighted because they recover the donor's lighting. Shadow magnitude is not matched to the host: it is set by a three-parameter transfer $(\tau,\sigma,g_{\min})$. The shading field is divided by its 75th percentile over skin, then gated, scaled, clamped, smoothed, and re-clipped inside a feathered, skin-gated face mask. On an analytic face heightfield, the default $(\tau,\sigma,g_{\min})=(0.90,0.45,0.82)$ modifies 56.5% of face pixels with mean gain 0.938 (0.890 on modified pixels) and drives 3.4% of pixels to the floor. Hue invariance is a corollary of the operator. We analyse the transfer in closed form, ablate its parameters, and discuss failure modes of a monotone, darkening-only formulation, including double-shadowing of non-flat donors.

---


### 23. [REVERSAL-BENCH: A Reversibility Axis and Reset Oracle for Measuring the Reset-Free RL Cliff](https://arxiv.org/abs/2609.17745)

**<font color=#1a73e8>作者：</font>** Riyaaz Shaik, Chandru Venkataraman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central goal of autonomous reinforcement learning is continuous policy training without external resets. However, existing paradigms largely depend on underlying environmental reversibility, a property absent in real world manipulation, where events such as pushing objects off tables or spilling granular substances cannot be undone. We introduce REVERSAL-BENCH, a benchmark that controls reversibility via a continuous parameter $\rho \in [0, 1]$ and provides a reset oracle, a ground-truth verification mechanism to test state recoverability across eight manipulation settings in five physics engines. Evaluating a broad spectrum of policy architectures, including standard actor-critic algorithms, safe RL, and specialized reset-free frameworks, reveals a sharp reversibility cliff: reset-free agents are consistently absorbed into irrecoverable states as $\rho$ increases, whereas episodic agents maintain steady learning. We see this failure mode across autonomous reset-free baselines and constrained RL. Because reset-free agents lack external resets, any transition into an irrecoverable state results in permanent absorption, leaving the agent trapped where further learning halts. We show that this absorption phenomenon persists in full physics simulations under learned manipulation policies. By evaluating against geometrically identical reversible counterparts, we confirm that this breakdown is causally driven by irreversibility rather than obstacle complexity. We release the benchmark suite, a large multi-simulator dataset labeled with recoverability and a reset oracle. We also evaluate a safety shield that intervenes before irreversible failures occur, showing that while recoverability can be predicted accurately, active recovery primarily succeeds only when the agent can physically steer clear of the trap

---


### 24. [Is Trump's Vocabulary Poor? Vocabulary Richness Across Texts of Different Lenghts](https://arxiv.org/abs/2609.17747)

**<font color=#1a73e8>作者：</font>** Dominique Labbe, Cyril Labbe, Jacques Savoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study explores the vocabulary richness of oral political communication. A model explaining the lexicon growth is proposed by subdividing the whole vocabulary into terms generated by general and specialized glossaries.

---


### 25. [SAM-on-the-Curve: Sharpness-Aware Mode Connectivity for Robust Weight-Space Interpolation](https://arxiv.org/abs/2609.17748)

**<font color=#1a73e8>作者：</font>** Alejandro Calatrava, Xu Zhang, Ren Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks that are independently trained to similar performance can be connected by low-loss parametric curves in weight space, a phenomenon known as Mode Connectivity (MC). This geometric property underpins practical techniques such as weight averaging, model ensembling, and model merging. We argue that low-loss connectivity is an incomplete geometric criterion: it controls loss only along a one-dimensional trajectory while leaving the surrounding weight-space neighborhood unconstrained, so the optimized curve may traverse sharp ridges that become fragile under distribution shift. We therefore reformulate mode connectivity as a neighborhood-robust path optimization problem, seeking a curve whose entire local neighborhood maintains low loss. We propose Sharp Mode Connectivity (SMC), which applies a first-order sharpness-aware approximation to the resulting minimax functional, enforcing flatness along the entire curve rather than only on it. We derive a practical optimization algorithm for connectivity paths under this sharpness-aware objective. Under severe blur corruptions from CIFAR-10-C, SMC achieves up to 6.09\% absolute accuracy improvement over standard MC. Remarkably, SMC produces negative loss barriers, meaning that models obtained at interior points of the optimized path can outperform the average endpoint loss. These results, validated across ResNet-18, VGG16-BN, and ViT-Tiny on CIFAR-10 and ImageNet-100, establish path-wise flatness as a practical principle for robust weight-space interpolation.

---


### 26. [How to make effective use of domain experts for image classification?](https://arxiv.org/abs/2609.17749)

**<font color=#1a73e8>作者：</font>** Dieu-Donné Fangnon, Diane Lingrand, Aurélie Liard 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A lot of expectations have been put for years on integrating domain expert knowledge in image classification models. Several approaches have been explored, Concept Bottleneck Models (CBMs) opened up a new avenue of research leading to many variants, and more recently to Concept-based Embedding Models (CEMs). CBM consider binary encoding of each concept, while CEM expands this idea by embedding each concept through two vectors. However in real-life scenarii, domain experts' knowledge is usually organized in concepts determined by various attributes, each attribute encoded either with numerical values, or range of values, or binary values, or categorical values. In this work, we first finetune an image feature extractor for classifying attributes representing the downstream object classes, where the class attributes have been specified by experts under various encoding formats. A classification head is then learnt from these various attributes to categorize target objects. We experimentally show that it improves the classification for three datasets: Kaggle fish dataset, AWA2 and a more challenging new wood charcoal dataset. We then propose an automatic selection of potential missclassified data. In this second step, experts are asked for those data to eventually modify the predicted attributes in order to improve the classification.

---


### 27. [Beyond Performance Metrics: Uncertainty Mapping of Label Ambiguity in Fazekas Score Prediction](https://arxiv.org/abs/2609.17753)

**<font color=#1a73e8>作者：</font>** Susanne Schmid, Johanna Ospel, Richard Frayne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference labels used to train medical image classification models are not always as certain as they may appear, and this uncertainty has implications on performance metrics. In this study, we propose a framework to analyze model performance for periventricular Fazekas score prediction that goes beyond conventional metrics. The Fazekas score is an ordinal visual rating scale used to assess the severity of white matter hyperintensities and is known to be affected by inter-rater variability. While the best Fazekas score prediction model achieved a Matthews correlation coefficient (MCC) of 0.70, performance varied across data splits and loss functions, making interpretation of model capabilities difficult.
Rather than interpreting epistemic uncertainty of a model's prediction as an isolated scalar value, our approach of uncertainty mapping relates uncertainty to its position within the learned feature representation. This highlights regions of class-boundary transitions where cases appear more ambiguous and misclassifications are more likely. It also identifies potential label disagreement, including low-uncertainty misclassified cases that expert review found to be inconsistent with the original reference Fazekas score. Therefore, uncertainty mapping allows model behaviour to be examined in relation to class separation and potential model-label disagreement.
Loss function choice also influenced the uncertainty profile, with some models showing clearer class separation and more localized uncertainty in ambiguous regions than others. These findings suggest that uncertainty mapping for Fazekas score predictions can support model interpretation and targeted dataset review when reference labels are affected by ambiguity/ inter-rater variability.

---


### 28. [Evolution of US Oral Political Language](https://arxiv.org/abs/2609.17755)

**<font color=#1a73e8>作者：</font>** Jacques Savoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The analysis of US political language is usually based on the written form (e.g. presidential addresses) or posts broadcasted on various social networks. Oral production, however, which is even more frequent, can better reveal the style and mode of thinking of the speaker. This study covers this mode of linguistic communication by considering 19 candidates from the presidential elections between 1960 to 2024. Our main research objectives are to disclose the main trends hidden in those presidential debates. Do we observe a clear simplification of the US political language over time? Does Trump have poor language compared to the other candidates? Do unusual stylistic features occur only with a single, specific president? Moreover, can we detect a pattern explaining the success or failure of some nominees? Over time, this study demonstrates a significant reduction in political language complexity, a decrease of the mean sentence length, and a noteworthy decline of complex terms. Moreover, the emotional tone increases over the decades, while logical and rational thinking tends to lessen.

---


### 29. [Imitation Learning for Autonomous Driving in CARLA](https://arxiv.org/abs/2609.17757)

**<font color=#1a73e8>作者：</font>** Jordy Kieto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral cloning trains a policy offline on expert demonstrations, but deployment is closed loop: each action affects the observations the policy receives next. We study how much closed-loop driving competence a compact multimodal policy can acquire from offline demonstrations in the CARLA simulator. The policy uses five-frame histories of RGB images, LiDAR, vehicle telemetry, and lane waypoints to predict throttle, brake, and steering at 20 Hz. Demonstrations were collected in three stages, ending with a systematic route-generation procedure that enumerates spawn points and feasible maneuvers and verifies completed autopilot routes. The released 1.36 million parameter policy was trained on 236,882 windows, representing about 3.3 hours of driving from 448 captures. The resulting policy drives autonomously for hours on training and held-out routes. In our runs, it did so without collisions and also transferred qualitatively to an unseen CARLA town with different road geometry. We also observed recovery from large trajectory deviations, although we do not claim systematic recovery without controlled evaluation. We report offline metrics and distinguish measured results from qualitative closed-loop observations. We release the code, trained checkpoint, ONNX model, data sample, and an evidence audit for the reported claims.

---


### 30. [Is Luke the Author of a Gospel and the Acts of the Apostles?](https://arxiv.org/abs/2609.17762)

**<font color=#1a73e8>作者：</font>** Jacques Savoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> According to Christian tradition, Luke is credited with authoring a Gospel and the Acts of the Apostles, even if his name does not appear in either book, both originally written in Koine Greek. Several biblical scholars assume that both texts were written by a common author, while others deduce the presence of two authors. Different studies have been found to support either finding, some based on qualitative evaluation, while a few others consider the occurrence frequency differences between the two books. To propose an enhanced quantitative analysis, this study is grounded on two recent authorship attribution models. The Burrows' Delta, applied with eleven different feature sizes, demonstrates common authorship. An author verification model confirms this finding. The following experiments consider several stylistic representations, feature sizes, and distance functions to confirm that Luke is the true author of both books.

---


### 31. [Modular Deep Learning Mechanisms for Auditable Next-Day Wildfire Spread Prediction](https://arxiv.org/abs/2609.17763)

**<font color=#1a73e8>作者：</font>** Miguel Esparza, Aydin Ayanzadeh Ahmad Mousavi, Ali Mostafavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-day wildfire prediction requires models whose forecasts can be evaluated alongside the assumptions and historical evidence used in their computation. Although deep learning can learn spatial patterns from remote-sensing data, predictive performance alone does not establish physical fidelity or operational trustworthiness. This study investigates three modular augmentations for next-day active-fire prediction: wind- and slope-conditioned attention biases, physics-feature retrieval-augmented output correction, and fire conditioned dual-stream gating. The attention biases expose prescribed directional preferences, while the retrieval module selects historical tiles using a nine-dimensional environmental and fire-state descriptor and applies a learned correction to a frozen model's logits. The modules are evaluated across five backbones on the Next Day Wildfire Spread benchmark, using staged ablations, directional audits, retrieval perturbations, calibration measures, and computational comparisons. The three-seed mean F1 score and area under the precision--recall curve (AUC-PR) of a SwinUNETR model with all three augmentations are 0.4216 and 0.3673. Then, a mixed ensemble (two augmented architectures and one non-augmented architecture) model achieves 0.4292 and 0.3790. Benefits vary across architectures, and retrieval-related improvements in AUC-PR do not consistently translate into higher F1. The constructed wind bias aligns closely with input wind, but its alignment with observed next-day fire displacement is much weaker, distinguishing prior inspectability from predictive physical fidelity. The study contributes a framework for exposing and evaluating selected domain-informed components within wildfire prediction models. Together, the results presented show that predictive performance, operational trustworthiness, and computational practicality need not be competing objectives.

---


### 32. [How Calibration Content Shapes Attention-Based Reranking](https://arxiv.org/abs/2609.17764)

**<font color=#1a73e8>作者：</font>** Petros Karypis, Hossein Rajaby Faghihi, Peter Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention-based rerankers score documents by aggregating query-to-document attention and subtracting a null-query calibration pass to remove positional and structural bias. Although widely used, this calibration assumes that the null pass removes irrelevant signal from each document. We show that modern prompt content, e.g. constraints, instructions, personas, and demonstrations can violate this assumption when it enters the scoring readout, making the null pass relevance-aware rather than null. We find that calibration is especially harmful when applied to prompts containing longer, more detailed instructions as the null-pass step removes relevant signal. Based on these findings, we propose interpolated null calibration, a training-free modification that controls how much of the instruction content enters the null baseline. It recovers attention-based reranking performance on instruction-heavy tasks where standard calibration fails, while preserving calibration's benefits when the null pass remains relevance-agnostic. On instruction heavy tasks, the recovered rankings surpass generative rerankers. We also show that in-context demonstrations improve attention-based reranking with little calibration interference, since demonstrations act only through the query pass and leave the null pass unchanged.

---


### 33. [Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2609.17810)

**<font color=#1a73e8>作者：</font>** Weiying Chen, Edmond Lou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular reconstruction of wind-driven vegetation is severely underconstrained: motion along the viewing direction is largely unobservable, a moving canopy offers few reliable correspondences, and nearly the entire scene is dynamic, providing little static reference. Directly-learned deformation fields in 4D Gaussian Splatting therefore optimize photometric consistency rather than recover the motion that produced it. We replace that field with a physically parameterized deformation prior: one damped harmonic oscillator per rigid part, driven by the observed wind and integrated by differentiable RK4, supervised photometrically alone. To test whether such a prior is physically grounded rather than merely well fit, we build a controlled synthetic testbed of three procedurally generated trees spanning an order of magnitude in skeleton complexity, whose per-part natural frequency follows from its own geometry and whose damping ratio is a fixed constant, both held out of training. On it, we measure held-out views, temporal extrapolation, zero-shot transfer to unseen wind speeds, and recovery of the physical parameters themselves. The prior costs appearance fidelity on in-distribution views and extrapolates markedly better outside the training window and the training wind, while parameter recovery is far weaker than it first appears: frequency recovery survives an untrained null control on only the sparsest of the three trees, and damping is not recovered at all.

---


### 34. [GazeDiT: Gaze-Accurate Diffusion Image Generation for Eye Tracking via Spatial Conditioning](https://arxiv.org/abs/2609.17814)

**<font color=#1a73e8>作者：</font>** Dongze Wu, David Colmenares, Fengting Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are increasingly used to generate synthetic training data, but precise label control remains difficult when the conditioning signal is low-dimensional and coarse. Text-conditioned images are judged by broad prompt consistency, whereas supervised training requires precise correspondence between each image and its numerical label. This is challenging in eye tracking, where a 4D binocular gaze is expressed through subtle, spatially localized pupil and iris geometry. We introduce GazeDiT, a diffusion model that generates images for a requested 4D gaze through an internally constructed spatial condition that grounds the global gaze label in this local geometry. During training, a frozen SegFormer extracts pupil/iris geometry from diverse real images, allowing the model to learn realistic appearance conditioned on that geometry. At inference, a physical eye renderer samples gaze-consistent geometries by varying anatomy and camera state, enabling diverse synthesis without a source image. GazeDiT achieves substantially lower tail gaze-label error than other diffusion baselines, approaching the error of the same frozen gaze estimator on real images. Its generated data also improves the downstream eye tracker, reducing gaze error on difficult cases from 3.05° to 2.80° in the smallest cohort.

---


### 35. [Principled Koopman Representations with Kalman Inference for Efficient Time-Series Prediction](https://arxiv.org/abs/2609.17815)

**<font color=#1a73e8>作者：</font>** Ruiquan Li, Yuheng Bu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Koopman operator has been widely used for time-series prediction in dynamical systems. However, prior work that learns latent ``Koopman spaces'' using neural networks often did not construct a valid Koopman space for forecasting, as these representations may be mathematically inconsistent with the operator-theoretic formulation and fail to capture the intrinsic low-rank structure of system dynamics. To address this issue, we introduce K$^2$SVD, a method that explicitly learns the leading singular functions of the Koopman operator by optimizing a Hilbert-Schmidt objective. This yields a well-defined low-rank approximation of the Koopman operator with an interpretable linear combination, featuring a compact latent space with less than $10\%$ of the dimensions used in previous work. In the learned Koopman space, K$^2$SVD further captures temporal evolution with a linear Gaussian state-space model and performs inference via Kalman filtering, mitigating noise accumulation during multi-step prediction. Empirical results show that K$^2$SVD outperforms state-of-the-art methods across multiple datasets, with significantly faster prediction speeds and lower computational cost than previous efficiency-focused models. This highlights the benefits of principled low-rank Koopman representations and opens up broader potential for applications.

---


### 36. [The Free Inference Dimension: Complexity Measure for Zero-Collision Navigation under Hypothesis Mixtures](https://arxiv.org/abs/2609.17816)

**<font color=#1a73e8>作者：</font>** Luiz Carlos Castro Guedes, Edward Hermann Haeusler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solomonoff induction frames prediction as a mixture over computable hypotheses, typically leading to identification of the true environment. In a finite meta-reinforcement learning setting with nested constraint families, in our previous work, we observe a different regime: a value-mixture (VM) agent achieves near-optimal, zero-collision navigation without identifying the true environment, a phenomenon we call Free Inference. This regime persists up to a sharp density threshold, beyond which performance degrades and posterior-mode selection (PMS) becomes preferable.
We formalize this behavior via the Free Inference dimension dFI(S,N), a combinatorial measure of the environmental complexity a VM agent can handle while preserving trajectory coherence. We prove dFI is strictly smaller than the VC-dimension and relates to the Natarajan dimension up to a path-length factor, capturing the cost of non-decomposable loss. A PAC-style relaxation yields generalization bounds driven by dFI^(epsilon,delta). We also define a complementary PMS identification dimension and show that a hybrid strategy---averaging until the first collision, then switching to selection---is optimal, with links to Littlestone-type dimensions supported by grid-world experiments.

---


### 37. [CALIPER: Metric-Grounded Model-Free Recognition of Visually Similar Industrial Parts](https://arxiv.org/abs/2609.17820)

**<font color=#1a73e8>作者：</font>** Alankrit Gupta, Chenxi Tao, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained recognition of visually similar industrial parts is challenging when classes differ primarily in physical dimensions. Normalizing detected object crops to a fixed input size suppresses absolute scale, while CAD models and large class-specific datasets may be unavailable in evolving industrial inventories. We present CALIPER, a model-free RGB-D framework that couples support-based appearance matching with metric size evidence. Each training class is onboarded from a single turntable RGB-D video and one to two labeled real images; 3D reconstruction provides novel-view appearance support, while aligned depth yields a class-specific metric size profile. At inference, a coarse YOLOv8n-seg model localizes parts, and a frozen DINOv2 backbone with an episodically trained embedding head performs fine-grained support matching. Margin-conditioned metric fusion activates probabilistic size evidence only for appearance-ambiguous decisions. New classes are enrolled from a small RGB-D support set without updating network parameters. We evaluate CALIPER on 18 visually similar industrial parts: 16 classes are used for training, while two screws are reserved for training-free enrollment. CALIPER achieves 88.2% closed-set accuracy with 99.8% localization recall and 85.7% overall accuracy after 10-shot enrollment of the two unseen screws. Metric fusion improves unseen-class accuracy by up to 37.4 percentage points without statistically significant degradation of the original inventory. Robot-arm deployment identifies 17/18 parts without deployment-specific retraining.

---


### 38. [NObSP: Functional Decomposition of Neural Networks via Oblique Subspace Projections](https://arxiv.org/abs/2609.17825)

**<font color=#1a73e8>作者：</font>** Alexander Caicedo, Víctor De La Hoz, Santiago Alférez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how deep neural networks make decisions remains a fundamental challenge. We present NObSP (Nonlinear Oblique Subspace Projections), a framework that decomposes predictions into explicit per feature contribution functions and an interaction residual. NObSP exploits the linear final layer of a trained network and uses oblique projections in sample space to reduce double counting when learned feature subspaces overlap, thereby supporting both local explanations and global functional analysis. We establish connections to functional ANOVA and the Kolmogorov-Arnold representation theorem and derive an efficient partial regression algorithm for out of sample evaluation. For convolutional networks, NObSP-CAM produces class activation maps without backward passes after a one time calibration. Experiments on tabular and vision benchmarks show faithfulness comparable to established attribution methods. On a synthetic benchmark with known component functions, NObSP obtains a Function Reproduction Score of 0.989, compared with 0.966 for KernelSHAP and 0.922 for Integrated Gradients. On TinyImageNet, contribution vector embeddings improve mean nearest neighbor class purity from 0.654 for raw activations to 0.713 and reduce mean neighbor distance by more than half. These results indicate that NObSP complements scalar attribution methods by recovering functional contribution profiles with separable positive and negative evidence.

---


### 39. [Procedural Pretraining for Molecular Property Prediction](https://arxiv.org/abs/2609.17831)

**<font color=#1a73e8>作者：</font>** Moritz Friedemann, Zachary Shinnick, Philip Torr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction is often limited by the small size of labeled downstream datasets, motivating pretraining on large corpora of unlabeled molecules. In this work, we ask whether useful inductive biases can instead be learned from abstract, procedurally generated data before a model sees any molecular data. We introduce a three-stage training pipeline consisting of procedural pretraining, molecular pretraining on SMILES, and downstream fine-tuning, and evaluate several procedural tasks spanning sequence structure, cellular automata, and graph reasoning. We find that procedural pretraining can improve molecular property prediction even after subsequent molecular pretraining: on Lipophilicity, \textsc{Reverse} reduces test error by 4.8\%. For context, the magnitude of this improvement is roughly 90\% of the performance difference between our 250K-molecule baseline and the publicly released MoLFormer checkpoint pretrained on approximately 100M molecules. Our analysis shows that the benefit is strongest under downstream data scarcity, depends on the structure of the procedural data rather than only surface-level statistics, and does not increase monotonically with additional procedural training. Instead, transfer typically peaks at an intermediate procedural budget and deteriorates as the model approaches convergence on the procedural task. We further find that, for several tasks, much of the transferable information is localized in the attention layers, while feed-forward layers can contribute to over-specialization. These results show that procedural data can provide transferable structure for molecular learning and offer a complementary route to improving performance when labeled molecular data are limited.

---


### 40. [Adaptive hybrid coupling with operator inference, the overlapping Schwarz alternating method and reinforcement learning](https://arxiv.org/abs/2609.17837)

**<font color=#1a73e8>作者：</font>** Trishit Mondal, Irina Tezaur, Anthony Gruber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid domain decomposition methods provide a flexible framework for coupling full order models (FOMs) and reduced order models (ROMs), but typically assume the model assigned to each subdomain is fixed throughout a simulation. This is limiting for transient problems in which localized features propagate through the domain and the regions requiring high-fidelity resolution change over time. We introduce a reinforcement learning (RL)-based approach for online adaptation of FOM-ROM models coupled via the overlapping Schwarz alternating method (O-SAM), an iterative domain decomposition method that solves subdomain-local problems while exchanging solution information through transmission boundary conditions on overlapping interfaces. Deep Q-networks (DQNs) are trained offline to select among subdomain-local FOMs and pre-trained Operator Inference (OpInf) ROMs using a reward balancing accuracy, cost, and model-switching frequency. Once trained, the policies are deployed predictively on problem instances not seen during training, without requiring a reference FOM solution. We demonstrate the approach on two examples: a 1D advection-diffusion problem with a moving front, and a 3D linear elastic wave propagation problem implemented in the this http URL solid mechanics code. For the advection-diffusion benchmark, the learned policy dynamically allocates high-fidelity resolution as the front propagates and outperforms static FOM/ROM assignments; letting the agent also adapt the domain decomposition provides no further benefit. For the elastic wave benchmark, learned policies for two and three subdomain decompositions track the propagating wave by assigning FOMs to subdomains containing the wave and ROMs elsewhere, as expected. Our results demonstrate the potential of RL to enable predictive online adaptation of model fidelity within Schwarz-based hybrid simulations.

---


### 41. [Hybrid coupling with numerics-informed neural networks and the overlapping Schwarz alternating method](https://arxiv.org/abs/2609.17841)

**<font color=#1a73e8>作者：</font>** George Chumbipuma, Irina Tezaur, Alejandro Diaz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a hybrid modeling framework for coupling pre-trained numerics-informed neural networks (NINNs) with classical full order models (FOMs) using the overlapping Schwarz alternating method. We consider the two-dimensional advection-diffusion equation in the advection-dominated, Peclet-number 10^6 regime. We first demonstrate that, unlike the corresponding physics-informed neural network (PINN), a monolithic NINN can be accurately trained on our model problem without domain decomposition. We then employ overlapping multiplicative Schwarz as a deployment mechanism for coupling a pre-trained, subdomain-local NINN with a neighboring FOM, with the NINN weights held fixed throughout the Schwarz iteration. We consider two training approaches for the subdomain-local NINNs: a top-down approach, in which boundary data are obtained from a coupled Schwarz solve on the full domain with a FOM on each subdomain (FOM-FOM Schwarz), and a bottom-up approach, in which boundary traces are generated synthetically on the NINN subdomain without requiring any full-domain solves. The resulting hybrid NINN-FOM solutions agree closely with the corresponding FOM-FOM Schwarz solutions, with the top-down and bottom-up training approaches yielding comparable accuracy.

---


### 42. [RoboVAD: A Large Cross-Domain Evaluation Benchmark for Anomaly Detection in Robotic Arm Manipulation Videos](https://arxiv.org/abs/2609.17843)

**<font color=#1a73e8>作者：</font>** Alexandru-Bogdan Dura, Sebastian Balmus, Radu Tudor Ionescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) is an actively studied task, having wide applications in typical scenarios such as public surveillance and road traffic safety. The task is also relevant for robotic arm interactions, where it has several downstream applications, including learning better interaction and manipulation abilities, triggering recovery procedures when anomalies occur, etc. Despite its relevance, the exploration of anomaly detection in robotic arm manipulation videos is limited by the low number of available resources. To this end, we introduce RoboVAD, a large-scale benchmark for video anomaly detection that comprises challenging cross-domain evaluation scenarios, where certain actions (tasks executed by a robotic arm) and anomaly types (mistakes that occur while performing certain tasks) remain unseen during training. RoboVAD is designed to benchmark VAD methods in realistic scenarios, where robotic arms can perform unforeseen tasks, and thereby encounter new anomaly types. We train and evaluate several state-of-the-art VAD methods, including a novel method specifically adapted for robotic arm manipulation. While the proposed method outperforms many state-of-the-art competitors, all methods remain below a micro-averaged frame-level AUC threshold of 70% in the most challenging evaluation setup, confirming the difficulty of the proposed benchmark. We publicly release our dataset and code at this https URL.

---


### 43. [PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research](https://arxiv.org/abs/2609.17846)

**<font color=#1a73e8>作者：</font>** Xinle Yu, Fan Bai, Kaiser Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents aim to automate scientific workflows, from proposing ideas to conducting experiments and analyzing results. Yet current AI and research agents can propose more directions than available resources allow them to pursue. Moreover, each attempt could consume substantial resources, requiring agents to reconsider how to invest in subsequent research. Thus, deciding how to invest research effort strategically should be a defining capability of autonomous research agents. Accordingly, we introduce PrimeScientist, which jointly determines research direction and resource investment across successive research attempts. Specifically, we formulate this challenge of strategic research effort allocation as a sequential decision problem where remaining resources should explicitly guide the research policy. We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts. Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources. Comprehensive evaluations across AI research, systems and code optimization, and machine learning engineering show that strategic allocation improves research quality and sample efficiency together. Across 12 AI research tasks, PrimeScientist improves average reward by 10.3% with 50.6% fewer research attempts than AutoResearch under the same resource budget. We believe making research effort allocation an explicit optimization target establishes effective resource use as a core research capability for autonomous agents to drive scientific breakthroughs at scale.

---


### 44. [Learning Heterogeneous Preferences](https://arxiv.org/abs/2609.17847)

**<font color=#1a73e8>作者：</font>** Shiwali Mohan, Matt Hong, Dule Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from human feedback has become a central paradigm for training modern AI systems, where models of human utility are used as reward models in policy learning. Existing methods typically assume a \emph{universal utility} function shared across a population and treat disagreement between annotators as stochastic variation. While suitable for objective tasks, this assumption breaks down in subjective domains where preferences vary systematically across individuals. We study the problem of subjective preference learning, in which observed choices arise from heterogeneous but internally consistent utility functions. Drawing upon rational choice theory, RCT \parencite{tversky1981framing}, we introduce \emph{individuated utility} functions conditioned on both the individual and their decision context, and propose a novel multi-stage architecture for estimating them from multi-modal data. We evaluate our framework on a newly collected dataset of more than $575{,}000$ pairwise aesthetic judgments from $2{,}398$ participants comparing automotive wheel designs. Our experiments show that individuated utility models substantially outperform universal utility models including foundation model baselines. Our results demonstrate that disagreement reflects meaningful preference heterogeneity rather than annotation noise. More broadly, our findings highlight the importance of collecting annotator attributes and learning individuated utility functions, enabling reward models that explicitly account for whose preferences they represent and faithfully capture human decision diversity.

---


### 45. [SNOMED CT Concept Recommendation from Masked Clinical Context](https://arxiv.org/abs/2609.17855)

**<font color=#1a73e8>作者：</font>** Ali Noori  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standardizing clinical language to SNOMED CT supports interoperability, analytics, and reusable phenotyping, but concept recommendation remains difficult when relevant concepts are rare or absent from training data. We present a masked-concept recommendation benchmark using the SNOMED CT Entity Linking Challenge v1.2.1 data derived from MIMIC-IV-Note. The dataset contains 75,491 annotations across 272 discharge summaries, with 204 notes used for training and 68 for historical testing. For each unique note-concept pair, the target mention is masked from a local clinical context and the system ranks SNOMED CT concepts observed during training. We compare a popularity baseline, sparse TF-IDF concept prototypes, dense latent semantic analysis embeddings, sparse-dense fusion, retrieved-note evidence, and a retrieval-augmented hybrid. Sparse TF-IDF performs best, achieving Recall@1 of 14.81%, Recall@10 of 33.43%, MRR of 0.2114, and nDCG@10 of 0.2297. Retrieval augmentation does not improve this baseline, with Recall@10 of 31.99% and MRR of 0.1937. Performance is strongly affected by concept frequency: Recall@10 is 7.74% for concepts appearing in only one or two training notes versus 43.90% for concepts appearing in more than ten. In addition, 9.66% of test note-concept pairs contain concepts unseen during training. These findings show that local lexical context and terminology coverage are major determinants of recommendation quality in low-resource settings and provide a reproducible baseline for future ontology-grounded and biomedical-encoder retrieval systems.

---


### 46. [Investigating Adversarial Robustness of Heterogeneous Cooperative Perception](https://arxiv.org/abs/2609.17856)

**<font color=#1a73e8>作者：</font>** Chenyi Wang, Yutong Liu, Qingzhao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heterogeneous cooperative perception (CP) enables connected vehicles with diverse sensor setups to share spatial awareness via compact feature maps, where receivers reconcile these maps using learned translation modules for fusion and inference. Prior attacks against CP in a homogeneous setting reveal that the data exchange introduces a critical attack surface: a single malicious agent can transmit crafted features that erase real objects from a neighbor's fused scene. Yet, it is widely hypothesized that heterogeneity naturally defends against these attacks, as the attacker lacks knowledge of the victim's detector and the translation module scrambles adversarial gradients. We demonstrate that this protection is largely an illusion. Using a matched-objective harness to standardize the perturbation budget, objective, and forward path, we show that properly tuned iterative attacks close or reverse the apparent robustness gap. However, these optimization-based attacks require ground-truth labels and iterative backpropagation, meaning they do not represent a practical field threat running in real-time. To bridge this gap, we introduce HetPoison, a learned generator that crafts a removal perturbation in a single, label-free forward pass. HetPoison transfers across major heterogeneous designs without requiring access to the victim's detector, matching or exceeding the effectiveness of expensive optimizer-based attacks. Since heterogeneity itself is not a defense, we propose HetShield, a lightweight trust layer that validates the spatiotemporal consistency across features, recovering 83--95% of the accuracy degraded by attacks, outperforming prior art.

---


### 47. [Uncertainty-Aware Continual Learning for Open-World Intent Discovery Under an evolving Label Space](https://arxiv.org/abs/2609.17866)

**<font color=#1a73e8>作者：</font>** Pisante Aida, Formentin Simone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world intelligent systems increasingly operate under open-world conditions, where user intents are not fixed or exhaustively known a priori and may evolve as new interaction patterns emerge. This paper proposes a unified uncertainty-aware probabilistic framework for continual new intent discovery under an evolving label space. Each utterance is encoded through an adaptive $\beta$-VAE into a latent mean, used for classification and density modelling and a posterior uncertainty estimate acting as a global reliability signal. Classifier confidence, posterior uncertainty and DP-GMM likelihood are combined through a multi-signal decision mechanism to distinguish known intents from potentially novel samples. Candidate novel instances are clustered through a density-based discovery module and only reliable clusters are promoted to new labels, enabling controlled label-space expansion. Replay and Elastic Weight Consolidation mitigate catastrophic forgetting and preserve previously acquired knowledge. The paper formalises continual intent discovery as a structured multi-phase open-world problem, introduces adaptive label-space expansion under stability--plasticity constraints and uses posterior uncertainty to regulate trusted-sample selection, pseudo-labelling, novelty admission and replay. Experiments show high novelty precision, stable adaptation across sequential phases and limited forgetting. Near-zero NMI and ARI indicate limited reconstruction of the complete fine-grained intent taxonomy, consistent with the framework's conservative promotion strategy. Qualitative analyses nevertheless reveal dense and locally coherent semantic clusters, showing that reliable novel structures can be discovered without exhaustive recovery of the underlying taxonomy.

---


### 48. [TabPFN-3.5: Technical Report](https://arxiv.org/abs/2609.17895)

**<font color=#1a73e8>作者：</font>** Benjamin Jäger, Nick Erickson, Léo Grinsztajn 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TabPFN-3.5, our new flagship Tabular Foundation Model. It significantly outperforms its predecessor, TabPFN-3, and all existing baselines across a broad range of tabular problems. TabPFN-3.5 sets a new state of the art on standard tabular prediction in TabArena, and extends it to the data practitioners encounter in practice: non-i.i.d. data with temporal or grouped splits, tables with strings, text and images, high-cardinality categorical features, and wide tables with many features. These gains carry over to our task-specific harnesses: state of the art on relational data and stronger time-series forecasting. For faster inference, our variant TabPFN-3.5-Fast runs up to 3x faster than TabPFN-3 while keeping most of the accuracy gains. In addition, we upgrade TabPFN-3.5-Plus, expanding our multimodal capabilities with advanced text and date handling alongside proprietary inference optimizations. Finally, we release a new version of our Thinking mode, TabPFN-3.5-Thinking, which scales inference-time computation to push the state of the art further. It benefits from our stronger base model and from inference-time improvements that make it up to 12x faster than TabPFN-3-Thinking.

---


### 49. [When AI Agents Meet MEV: Cross-Chain Arbitrage in the Agentic Economy](https://arxiv.org/abs/2609.17897)

**<font color=#1a73e8>作者：</font>** Wei Ye, Jingyan Xu, Yuanhong Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study cross-chain arbitrage when autonomous AI agents, rather than humans or bots, are the searchers. We model agents as both arbitrage extractors and Maximal Extractable Value targets, derive the optimal trade size for a risk-averse agent under mean-variance utility with stochastic bridge delays, and formalize multi-chain path selection as a belief-weighted online learning problem whose belief estimates converge under a Robbins-Monro schedule. Using 23,000 Uniswap V3 swap events across Ethereum, Arbitrum, and Base, we find that Ethereum-Arbitrum price gaps average 0.044% at 10-second resolution and Arbitrum--Base gaps average 0.013%, so $10,000 trades clear in 63% of L2-L2 windows via CCTP while L1-L2 routes require $50,000 or more for comparable viability. Our adaptive path-selection algorithm outperforms standard baselines by 11% on average, and moderate randomization cuts MEV exposure by over 50% with only modest profit loss.

---


### 50. [Walking the Score Manifold: Continuous-time Generative Dynamics on Learned Data Manifolds](https://arxiv.org/abs/2609.17901)

**<font color=#1a73e8>作者：</font>** Jan Tauberschmidt, Brian B. Moser, Stanislav Frolov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling of time-dependent data is typically formulated on a discrete temporal grid, restricting supervision to the observed timestamps in the training data. We instead frame generation as continuous-time evolution on a learned data manifold. To this end, we leverage pretrained score-based models as geometric priors and learn a vector field that evolves data along score-induced interpolation paths. Because these dynamics follow transitions that respect the geometry learned by the score model, they support generation at arbitrary timestamps and temporal super-resolution beyond the discretization of the training data. Moreover, this geometric formulation allows us to train the vector field simulation-free through a regression objective. To improve long-horizon rollout robustness, we introduce an objective that promotes path-relative transverse exponential stability. While motivated by stability theory, it admits a practical interpretation as denoising score matching transverse to the interpolation path. Further, we extend the framework to a probabilistic setting that models a distribution over plausible future trajectories. We demonstrate the method on natural video and scientific dynamical data, including temporal super-resolution, PDE-based spatiotemporal fields, and molecular dynamics. Our results show that score-based priors provide a strong foundation for learning stochastic continuous-time generative dynamics.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
