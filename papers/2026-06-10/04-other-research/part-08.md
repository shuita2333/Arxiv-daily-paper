# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 351. [A Multi-Agent System for IPMSM Design Optimization via an FEA-AI Hybrid Approach](https://arxiv.org/abs/2606.09037)

**<font color=#1a73e8>作者：</font>** Jinseong Han, Sunwoong Yang, Namwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interior permanent magnet synchronous motor (IPMSM) design requires balancing conflicting objectives and multi-physics constraints, while modern optimization workflows face three bottlenecks: manual problem setup, high finite element analysis (FEA) cost, and unreliable surrogate-based search in sparse or out-of-distribution regions. To address these limitations, we propose an end-to-end automated IPMSM design optimization framework that integrates retrieval-augmented generation (RAG) for structured problem definition with an uncertainty-aware FEA-AI hybrid optimization pipeline. A Design agent, connected to a motor textbook through RAG, provides domain-knowledge-based options and engineering tips, and compiles an optimization card and a design-of-experiments plan for AI-model training. A Training agent automates electromagnetic FEA, records geometry-validation and solver-failure logs, analyzes failed geometries using ANOVA-based data analysis and LLM reasoning, and invokes a Design Sampling agent to redefine the design space and generate additional samples. An Optimization agent performs GA-based search with uncertainty-driven switching: low-uncertainty candidates are evaluated by AI-surrogate inference, whereas high-uncertainty and reliability-critical Pareto-front or top-K candidates are corrected by high-fidelity FEA and reused for iterative retraining. The framework converts manual, experience-dependent configuration into a reproducible workflow that balances computational cost and prediction reliability. Experimental results under a matched high-fidelity FEA budget show that the proposed hybrid approach achieves better objective performance while maintaining low and further reducible predictive uncertainty, outperforming FEA-only search, which is limited by early budget exhaustion, and AI-only search, which converges to a low-confidence optimum.

---


### 352. [DynaCF: Mitigating Shortcut Learning in Reward Models via Dynamic Counterfactual Sensitivity](https://arxiv.org/abs/2606.09043)

**<font color=#1a73e8>作者：</font>** Fengyuan Liu, Yongliang Miao, Zirui He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models trained from pairwise preferences often exploit superficial shortcut cues rather than learning true response quality. We propose DynaCF, a dynamic reweighting framework for mitigating shortcut learning in reward model training. Unlike static shortcut heuristics, DynaCF measures shortcut sensitivity online during optimization by applying semantics-preserving counterfactual perturbations and tracking the resulting margin shifts and preference flips under the current model. Samples with higher shortcut sensitivity are dynamically downweighted in the Bradley-Terry objective, encouraging the model to rely less on superficial patterns and more on task-relevant preference signals. Extensive experiments show that DynaCF consistently improves robustness in preference modeling.

---


### 353. [Beyond Convolution: Advancing Hypergraph Neural Networks with Hypergraph U-Nets](https://arxiv.org/abs/2606.09051)

**<font color=#1a73e8>作者：</font>** Fuli Wang, Wei Qian, Daniel L. Lau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convolutions have successfully transitioned from image processing to the complex realm of non-Euclidean higher-order domains, particularly in hypergraphs. Despite the success in convolution, the exploration of a popular architecture named U-Net remains largely unexplored for hypergraph data due to the lack of well-defined pooling and unpooling operations. This work pioneers the study of U-Net architectures for hypergraph data, addressing the critical challenge of designing effective pooling and unpooling operations that retain maximal structural information from the input hypergraph. Motivated by hierarchical clustering, we propose to construct the pooling and unpooling operators all at once by cutting the clustering dendrogram at different granularities, named the Parallel Hierarchical Pooling (PHPool) and Unpooling (PHUnpool) operators. Unlike existing pooling methods that risk local structural damage through a sequential learning procedure, our PHPool operators are designed in a global and parallel manner to ensure fidelity to the original hypergraph structure with efficient computation while the PHUnpool operators are tailored to perform inverse operations of the PHPools for hypergraph reconstruction. We validate our model through hypergraph reconstruction simulation, hypergraph classification, and node-level anomaly detection, where it demonstrates superior performance over existing state-of-the-art graph and hypergraph deep learning methods.

---


### 354. [INFUSER: Influence-Guided Self-Evolution Improves Reasoning](https://arxiv.org/abs/2606.09052)

**<font color=#1a73e8>作者：</font>** Siyu Chen, Miao Lu, Beining Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolution offers a scalable path to stronger reasoning: a pretrained language model improves itself with only minimal external supervision. Yet existing methods either depend on extensively curated or teacher-generated training data, or, when the generator runs unsupervised, reward it by a difficulty heuristic that need not improve the solver. We introduce INFUSER, an iterative co-training framework with two co-evolving roles: a Generator that drafts questions and reference golden answers from a pool of unstructured, automatically collected documents, and a Solver that improves by training on them. The solver is trained with standard correctness rewards against the generator-provided answers, while the generator is rewarded by an optimizer-aware influence score that measures whether each proposed question would actually improve the solver on the target distribution. Because this continuous, noisy influence score is poorly served by standard GRPO, we propose DuGRPO, a dual-normalized variant of GRPO, for generator training. Together, these turn the document pool into an adaptive curriculum that favors questions useful to the current solver, not just hard ones. On Qwen3-8B-Base, INFUSER outperforms strong self-evolution baselines with over 20% relative improvement on Olympiad and SuperGPQA benchmarks, and an 8B INFUSER co-evolving generator outperforms a frozen 32B thinking generator on math and coding. Ablations confirm each design choice is necessary, and two extensions, applying INFUSER to an instruction-finetuned anchor and augmenting it with rule-verifiable RLVR data, further demonstrate the flexibility and generalizability of the framework. Code is available at this https URL.

---


### 355. [MilliVid: Hierarchical Latents for Long-Range Consistency in Video Generation](https://arxiv.org/abs/2606.09056)

**<font color=#1a73e8>作者：</font>** Ishaan Preetam Chandratreya, David Charatan, Basile Van Hoorick 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generative models have become increasingly powerful, but long-range consistency remains challenging to achieve because even a few dozen frames require impractically long transformer sequence lengths. We show that this issue can be mitigated by generating video using coarse-to-fine rollout within a multi-scale token space. Our approach is simple: first, we pre-train an autoencoder that compresses each frame into a hierarchy of tokens, with levels ranging from the typical latent resolution to only a handful of tokens per frame. The coarsest levels capture the most consequential information, such as scene layout and semantics, while finer levels add high-frequency appearance and texture. Then, we train a video diffusion model to generate these tokens using coarse-to-fine rollout. By carefully controlling the level of detail at which frames are generated and used as context during each rollout step, we are able to preserve long-range consistency in geometry and object permanence while spending less compute on the long-range consistency of less perceptually relevant details. We validate this approach using a custom dataset of long Minecraft videos, where it produces substantially more consistent rollouts compared to existing baselines.

---


### 356. [Security-First Approach to API Pipeline Development with Zero-Trust Architecture](https://arxiv.org/abs/2606.09062)

**<font color=#1a73e8>作者：</font>** Mahima Agarwal, Keshav Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern enterprises face an accelerating onslaught of API-targeted threats amid a rapidly expanding attack surface. Record volumes of software vulnerabilities continue to accelerate dramatically, with 28,818 CVEs disclosed in 2023 (a 38% jump from 2022) and 40,009 CVEs in 2024 (another 38% increase), while the average time-to-exploit (TTE) of new flaws shrank to mere days (approximately 5 days in 2023, down from 32 days in 2021). At the same time, API usage dominates web traffic and has become a primary vector for breaches - 99% of organizations experienced API security incidents in the last year, with 22% suffering actual data breaches via APIs (based on industry vendor research). This paper proposes a comprehensive "security-first" framework for API pipeline development, leveraging Zero-Trust Architecture principles within DevSecOps practices to counter these trends. We introduce a five-pillar approach encompassing Governance & Planning, Secure Design, Continuous Testing, Pipeline Controls, and Runtime Protection, aligned with industry standards (OWASP API Security Top 10 2023, NIST Secure Software Development Framework) and recent cybersecurity advisories. The results show significant improvements in vulnerability mitigation and breach prevention (e.g., 30% reduction in security incidents and 40% fewer post-release vulnerabilities in representative case studies), highlighting the positive impact of proactive security integration. The paper concludes with a discussion on implementation challenges, the evolving threat landscape, and recommendations for organizations to adopt a security-first pipeline with Zero-Trust to fortify API development against current and future threats.

---


### 357. [See More, Think Deeper: Query-Expanded Visual Evidence and Answer-Clue Guided Reflection for Long Video Understanding](https://arxiv.org/abs/2606.09064)

**<font color=#1a73e8>作者：</font>** Shuning Wang, Zhiheng Wu, YiNuo Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Video Large Language Models (Video-LLMs) have enabled performance on long-video understanding tasks. However, existing methods still face two key limitations: evidence acquisition often relies on a single search intent, and answer generation lacks an effective visual feedback mechanism. To address these limitations, we propose \textbf{CoVER}, a Comprehensive Visual Evidence and Reflection framework for long-video understanding. CoVER enables Video-LLMs to \textbf{See More} by dynamically gathering query-expanded visual evidence, and \textbf{Think Deeper} by verifying draft answers with effective answer-specific visual feedback. Together, these mechanisms shift long-video understanding from answer-centric generation to evidence-centric and visually verifiable reasoning. Experimental results show that CoVER-7B substantially outperforms models with the same parameter scale and even surpasses state-of-the-art closed-source models on certain metrics.

---


### 358. [OnlyDense: Reduced-Order Modeling for Lagrangian simulation](https://arxiv.org/abs/2606.09065)

**<font color=#1a73e8>作者：</font>** Tu Do, Shannon Ryan, Santu Rana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In science and engineering, Lagrangian simulation methods such as Smooth Particle Hydrodynamics (SPH) or Material Point Method (MPM) are often employed to study the behavior of dynamic systems. However, these methods can be prohibitively computationally expensive, particularly when simulating multi-scale spatial or temporal phenomena, e.g., void growth and coalescence within macro-scale geometries, structural failure of spacecraft components resulting from hypervelocity impact of space debris particles, etc. In contrast to graph-based methods, where the state of the system is understood as a discrete set of particles, we propose a learning framework for scalable representation and dynamics modeling of massive particle systems by treating the system state as a function and its evolution as a trajectory in Hilbert space. Rather than representing the state as a discrete set of particles or embedding it in a nonlinear latent manifold, we approximate the state space with a linear subspace spanned by learned neural basis functions. This parameterization enables direct projection to obtain latent coefficients and explicit access to the basis functions, avoiding optimization over a nonlinear latent space. The resulting representation admits a natural interpretation: latent variables correspond to coefficients in Hilbert space, and basis functions correspond to spatial modes, analogous to Proper Orthogonal Decomposition. The framework thus unifies classical projection-based reduced-order modeling with modern deep learning, while remaining invariant to the number of discretization points. Experiments on large-scale SPH simulations with over one million particles, including dynamic events with extreme deformation and fragmentation, demonstrate that the proposed method accurately reconstructs and predicts dynamics, achieving an R$^2$ score above $0.99$ with as few as $32$ basis functions.

---


### 359. [REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074)

**<font color=#1a73e8>作者：</font>** Zhang Chen, Shuai Wan, Mengting Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing pruning methods for 3D Gaussian splatting (3DGS) suffer from either severe quality degradation or prohibitive computational overhead. In this paper, we propose REFINE, a highly accelerated 3DGS pruning framework centered on a novel rendering-free primitive importance metric. Our approach leverages an analytically approximated, rendering-aware Hessian field to quantify the expected perceptual error induced by the removal of individual primitives. By modeling the joint modulation of visibility, projection geometry and the content adaptive hyperparameter, we entirely bypass costly forward rendering passes and derive an anisotropic perceptual weight field that serves as a high-fidelity proxy for primitive importance. Extensive experiments across multiple benchmark datasets demonstrate that REFINE maintains highly competitive rendering quality while achieving an unprecedented $3,000\times$ reduction in pruning-related computational complexity compared to state-of-the-art pruning methods.

---


### 360. [Beyond Scalar Rewards by Internalizing Reasoning into Score Distributions](https://arxiv.org/abs/2606.09076)

**<font color=#1a73e8>作者：</font>** Xin Jin, Huanqia Cai, Zhen Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models are central to text-to-image post-training, but visual preference is subjective and better represented as a distribution over rubric scores than as a deterministic scalar. Existing scalar, score-token, and pairwise reward models over-compress uncertainty and fine-grained score differences, while reasoning-based generative rewards provide stronger judgments but are costly to deploy and difficult to use as direct optimization signals. We propose Z-Reward, a teacher-student reward modeling framework that decouples reasoning-heavy judgment from efficient reward deployment. The teacher is a large VLM that uses reasoning to infer rubric-aligned score distributions, and is trained with Group-wise Direct Score Optimization (GDSO), which combines policy-gradient rewards from distribution expectations with direct pointwise and pairwise supervision on score distributions and score gaps. The student is trained with Reasoning-Internalized Score Distillation (RISD), which transfers the teacher's reasoning-conditioned score distribution into a compact VLM without requiring explicit reasoning chains at inference time. On our internally annotated evaluation set, the 27B GDSO teacher reaches 89.6% human preference accuracy, outperforming SFT, RewardDance, and GRPO, while the 9B RISD student reaches 88.6%, outperforming the OPD baseline and closely matching the larger teacher. We further show that Z-Reward can serve as a differentiable reward signal for text-to-image optimization, yielding a 41.3% net human-preference improvement over the SFT baseline.

---


### 361. [Neural Legendre-Fenchel transform with Hessian Preconditioning](https://arxiv.org/abs/2606.09077)

**<font color=#1a73e8>作者：</font>** Basile Plus-Gourdon, Frank Nielsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Legendre-Fenchel (LF) transform is a fundamental tool in convex analysis and machine learning that maps lower semi-continuous functions to their convex conjugates. In practice, when closed-form formula are not available for expressing convex conjugates of given functions, one must approximate them using various techniques. One recent such versatile numerical method is the deep Legendre transform method which relies on neural networks although it remains challenging particularly for tackling ill-conditioned functions. This work builds on the reformulation of the LF transform as a projective polarity. A notable property of this framework is its affine invariance. We leverage this affine invariance to introduce a Hessian-based preconditioning strategy. Specifically, we apply an affine deformation around a minimizer so that the second-order Taylor approximation of the function coincides with the canonical paraboloid, whose conjugation map is the identity. A residual network initialized near the identity can then learn this simplified mapping, while the original conjugation map is recovered through the inverse deformation. The proposed preconditioning incurs only a modest computational overhead, consisting of a single eigendecomposition during initialization and two matrix-vector multiplications per query. Experiments on a diverse set of convex functions, including high-dimensional benchmarks, demonstrate improved convergence rates and enhanced numerical accuracy of the conjugation, with particularly significant gains for ill-conditioned problems. Finally, we discuss the scope of applicability of our proposed method and highlight several of its limitations.

---


### 362. [The Hidden Bias of Process Reward Models:PRISM for Rewarding the Right Reasoning](https://arxiv.org/abs/2606.09078)

**<font color=#1a73e8>作者：</font>** Aakriti Agrawal, Souradip Chakraborty, Armin Saghafian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) improve credit assignment for reasoning by providing step-level feedback. However, we identify a hidden bias in PRMs caused by severe imbalance in step-level training data. Standard cross-entropy training amplifies this bias, causing PRMs to overcredit plausible but incorrect steps and produce high false-positive rates. We show that these false positives have an asymmetric downstream effect: false negatives mainly slow exploration, whereas false positives actively steer Best-of-N selection, guided decoding, and policy optimization toward flawed reasoning. This suggests that PRM training should shift from pointwise label fitting to reliable relative comparisons. To address this, we propose PRISM (Precision Ranking for Improved Step Modeling), a policy-aware PRM training framework that learns from contrastive step-level comparisons and hard negatives generated by a temporal lookahead strategy, requiring no new human labels. We further use a difficulty-aware curriculum to optimize the contrastive step margin. Across PRMBench and ProcessBench, PRISM substantially reduces false positives (22% on PRMBench) and improves macro F1 over strong discriminative PRMs. When applied to policy optimization and search tasks, including guided decoding and Best-of-N selection, it consistently improves accuracy (up to 22% for guided decoding and 33% for Best-of-N) and robustness. More broadly, trustworthy process supervision is not just about assigning high rewards, but about rewarding the right reasoning for the right reasons.

---


### 363. [Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search](https://arxiv.org/abs/2606.09081)

**<font color=#1a73e8>作者：</font>** Wuming Lei, Yanbin Gao, Mingyan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) object detection requires compact detectors that retain small-object details under onboard computation and memory constraints. Repeated downsampling inlightweight networks weakens shallow spatial information, while manually adding attention orfusion modules may increase cost without stable gains. This study analyzes YOLOX-Nano underedge-deployment constraints by combining a P2 high-resolution detection branch with a quantum-inspired evolutionary algorithm (QIEA) for lightweight structure screening. The search space isdefined by lightweight priority and task specificity, and the evaluation jointly considers accuracy,floating-point operations (FLOPs), latency, memory consumption, and recall. On VisDrone, theP2 branch increases APamall by 31.10% over the YOLOX-Nano baseline. Compared with NanoDet-Plus with similar model size, YOLOX-Nano+-P2 improves this http URL by 17.5% and APamal by 44.9%.The QIEA-selected candidate obtains the highest Recallso, but +P2 remains the strongest AP-oriented variant after full training. Full 100-epoch verification of Random-best, GA-best, andSA/QUBO-best candidates further shows that proxy rankings do not necessarily transfer to finalAPse9s. These results support using P2 as the main small-object enhancement path and QIEA as alightweight tool for candidate screening and accuracy-cost analysis. The source code, configurationfiles, diagnostic scripts, and summarized results are available at this https URL

---


### 364. [DynaOD: Dynamic Origin-Destination Flow Generation with Discrete-to-Continuous Temporal Semantic Modeling](https://arxiv.org/abs/2606.09086)

**<font color=#1a73e8>作者：</font>** Jie Zhao, Xianqi Dai, Jie Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic origin-destination (OD) flow generation seeks to synthesize realistic mobility dynamics from temporal context alone, without relying on historical OD observations. A key challenge is to translate semantic temporal signals into temporally coherent OD patterns while preserving the inherent spatial heterogeneity of urban regions. We propose DynaOD, a semantic-driven framework that models temporal dynamics through two complementary perspectives: discrete directional trends that characterize qualitative shifts in urban activity patterns, and continuous temporal evolution that captures how such shifts unfold over time. By jointly encoding these temporal semantics, the framework constructs time-varying region representations that condition pretrained static OD generators in a lightweight and plug-and-play fashion. This modular design further supports scalable deployment and cross-city transferability. Extensive experiments on large-scale real-world datasets show that our method consistently outperforms representative baselines in both predictive accuracy and distributional fidelity. Code is publicly available at this https URL.

---


### 365. [Addressing Market Regime Changes and Heavy-Tailed Returns in Portfolio Optimization via Bayesian VAR and Elliptical Black-Litterman](https://arxiv.org/abs/2606.09104)

**<font color=#1a73e8>作者：</font>** Daniil Mikriukov, Ruoyu Sun, Angelos Stefanidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) frameworks for portfolio optimization have shown promise for their ability to learn allocation rules dynamically from market data. However, these models fail to account for fat-tailed returns, which characterize actual market behavior with more frequent extreme events. Furthermore, historical data is treated homogeneously, without accounting for temporal importance, leading models to fail during regime changes. We propose a new BAVAR-BLED algorithm that combines methods derived from Bayesian-Averaging Vector Autoregressive (BAVAR) and the Black-Litterman model using Elliptical Distributions (BLED) within a TD3 architecture. BAVAR captures a set of vector autoregressive representations that consider multi-scale temporal features, enabling adaptive allocation decisions based on regime-aware estimates of return expectations and dispersion matrices. These estimates serve as prior inputs to BLED, a model that uses Student's t-distributions, allowing for more realistic fat tail return estimates. The BAVAR-BLED algorithm uses transformer networks for view construction and CNNs for risk-aversion estimates, which modify dynamic allocation decisions based on market conditions. An evaluation of 29 Dow Jones Industrial Average constituents over a decade-long market period shows that BAVAR-BLED significantly outperforms state-of-the-art methods, achieving Sharpe and Sortino ratios of 1.72 and 2.70, respectively, and total returns of 57.26%.

---


### 366. [Graph2Idea:Retrieval-Augmented Scientific Idea Generation with Graph-Structured Contexts](https://arxiv.org/abs/2606.09105)

**<font color=#1a73e8>作者：</font>** Xu Li, Hanzhe Tu, Xun Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating novel, feasible, and high-quality research ideas is an important yet challenging task in scientific this http URL Large Language Model (LLM)-based methods often ground idea generation with retrieved literature, but the retrieved evidence is usually provided as flat text, such as titles, abstracts, or summaries. Such flat contexts may contain redundant or weakly relevant information, while making cross-paper relations among problems, methods, mechanisms, and findings difficult to identify and this http URL address this challenge, we propose Graph2Idea, a knowledge graph-guided framework for retrieval-augmented scientific idea generation.Graph2Idea first retrieves papers according to the input topic, transforms them into structured knowledge triples, and dynamically constructs a target-centered knowledge graph to make literature relations this http URL then extracts compact graph-derived contexts that retain target-relevant relational evidence while reducing noisy textual this http URL on these contexts, a two-stage generation process first identifies promising research directions and then guides the LLM to synthesize candidate ideas from graph-grounded this http URL on a scientific idea generation benchmark show that Graph2Idea outperforms representative baselines under the automatic evaluation this http URL with the strongest baseline scores, it improves Novelty from 0.45 to 0.52, Quality from 0.24 to 0.29, and Feasibility from 0.22 to this http URL results suggest that graph-structured evidence helps LLMs generate research ideas through more explicit, compact, and traceable recombination of prior scientific knowledge.

---


### 367. [Driving Video Retrieval for Complex Queries with Structured Grounding](https://arxiv.org/abs/2606.09109)

**<font color=#1a73e8>作者：</font>** Manyi Yao, Sparsh Garg, Christian Shelton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video retrieval at scale is central to data curation and safety validation in autonomous driving, where users want to find not only scenes but also dynamic events such as cut-ins and hard braking. Existing vision-language and keyword-based retrieval methods often miss these events because the relevant motion may not be explicitly described in text or captured by lexical overlap. Rule-based retrieval can encode such events more directly, but it is brittle: generated or hand-written rules often fail when their assumptions do not match real driving data. We propose STRIVE-D, a data-calibrated retrieval framework for driving videos. It uses weakly labeled in-domain videos to estimate when a query rule is reliable, adapt rules that mismatch observed data, and fuse calibrated rule scores with vision-language and keyword-based retrieval signals. Across three driving benchmarks, including newly released human-annotated event data on DrivingDojo, STRIVE-D delivers up to 84% relative improvement in top-1 accuracy over state-of-the-art methods.

---


### 368. [Illumination-Invariant Anomaly Detection for Sub-Canopy UAV Multispectral Point Clouds](https://arxiv.org/abs/2606.09111)

**<font color=#1a73e8>作者：</font>** Likun Chen, Yanfeng Gu, Xian Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicle (UAV) multispectral point clouds (MPC) provide high-dimensional spatial-spectral data for sub-canopy target detection; however, their efficacy is significantly compromised by severe illumination heterogeneity caused by vegetation shadows. To address this, we propose a prior-free anomaly detection framework capable of robustly handling lighting variations. First, we formulate solar angle estimation as an inverse optimization problem. By coupling spectral indices with a ray-tracing model, this strategy achieves Prior-Free Shadow Extraction without relying on flight metadata, effectively distinguishing dark objects from true shadows. Second, to mitigate spectral distortions, we introduce an Illumination-Consistent Sparse Representation mechanism. Unlike standard reconstruction methods, we construct a background dictionary strictly from neighbors sharing the same illumination state. This constraint effectively disentangles spectral reflectance from lighting variations, ensuring that targets are represented solely by physically consistent background points. Experimental results indicate that the proposed method significantly improves the separability between anomalies and background in complex forest environments, demonstrating superior performance over state-of-the-art baselines. This framework is particularly suited for identifying camouflaged military targets, mapping fallen tree trunks, and uncovering archaeological ruins hidden beneath dense foliage.

---


### 369. [Hybridizing Equilibrium Propagation with Ising Machines for Efficient Energy-Based Learning](https://arxiv.org/abs/2606.09112)

**<font color=#1a73e8>作者：</font>** Chen-Rui Fan, Bo Lu, Xing-Yu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of artificial intelligence has led to substantial advances in deep neural networks. Nonetheless, conventional GPU-based training remains highly energy-demanding, motivating the exploration of physical dynamics and compatible energy-based learning schemes, such as equilibrium propagation (EP). EP-based training, however, frequently suffers from convergence to local minima due to phase-space contraction. Here we introduce an Ising-dynamics-inspired equilibrium-propagation framework in which dissipative Hopfield relaxation is replaced by an extended phase-space dynamics with conjugate variables. The resulting training paradigm keeps the local two-phase learning rule of EP while changing the physical route by which neural states reach equilibrium. We show that this dynamics lowers effective energy barriers, accelerates convergence, improves noise robustness, and trains deep convolutional Hopfield networks on MNIST, FashionMNIST, and CIFAR-10 with performance comparable to backpropagation.

---


### 370. [MAAM: Anchor-Preserving Compression and Contextual Calibration for Chinese Discriminatory Language Detection](https://arxiv.org/abs/2606.09114)

**<font color=#1a73e8>作者：</font>** Yuxin Fu, Shijing Si  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese discriminatory-language detection is challenging because harmful intent is often implicit and context-dependent. We propose MAAM (Myopia--Astigmatism Anchor Mechanism), a lightweight, model-agnostic framework inspired by functional visual blur: rather than preserving every token equally, MAAM retains discrimination-relevant semantic anchors and calibrates them with C--I--S contextual priors (Contextual Tone, Group Identity, and Stance Polarity). We also introduce ChLGBT, to our knowledge the first Chinese LGBT-focused discriminatory-language dataset, with 8,120 manually annotated samples and three ordinal labels: explicit bias, implicit bias, and emotional intensity. Across strong encoder baselines, MAAM improves all three prediction dimensions, with consistent gains in accuracy, F1, Brier score, and expected calibration error. Compared with frontier LLM baselines under zero-shot and few-shot prompting protocols, MAAM remains competitive while offering stronger compactness and stability. These results suggest that interpretable anchor preservation and contextual calibration provide a practical alternative to heavier model scaling for Chinese discriminatory-language assessment.

---


### 371. [Counterfactual Transport Flows for Offline Conservative Trajectory Refinement](https://arxiv.org/abs/2606.09115)

**<font color=#1a73e8>作者：</font>** Lena Krieger, Xuan Zhao, Zhuo Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) offers a path to policy improvement from logged data alone, using historical returns or other measurable outcomes as world feedback. A key difficulty is improving observed behavior without extrapolating beyond what the offline data supports. We propose \emph{counterfactual transport flows}, a source-conditioned trajectory refinement framework for offline decision-making guided by world feedback. Given a low-feedback candidate trajectory, we construct local preference pairs from offline data by retrieving nearby trajectories in latent trajectory space with higher task-specific feedback, and use them as weak supervision for conservative refinement. The framework learns instance-specific refinement directions: at inference time, a refinement strength parameter controls how far the candidate trajectory is transported, enabling a trade-off between preserving the original behavior and applying stronger improvement. Experiments on D4RL benchmarks, including AntMaze and MuJoCo tasks, show that our method improves behavior from historical returns as world feedback, while providing interpretable trajectory-level refinement paths.

---


### 372. [Optimizing Energy-based Neural Network Training with Coherent Ising Machine](https://arxiv.org/abs/2606.09117)

**<font color=#1a73e8>作者：</font>** Chen-Rui Fan, Bo Lu, Zhi-Hong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Ising machines serve as advanced physical solvers for the Ising model,enabling applications in combinatorial optimization and neural network training,their scalability for large-scale neural networks remains constrained by hardware connectivity limitations and suboptimal training methodologies. In this work,we leverage a Coherent Ising Machine (CIM) to train an energy-based neural network using Equilibrium Propagation, achieving performance comparable to existing software-based implementations. We further enhance the algorithm by integrating the Adam optimizer to solve for the ground state of a Hopfield energy network, significantly improving convergence speed and solution accuracy. Additionally, we demonstrate the scalability of our approach across deeper network architectures and convolutional operations. Our results highlight the potential of CIM dynamics as a scalable platform for training complex neural networks, offering a pathway toward energy-efficient implementations via analog circuits, optoelectronics, or integrated photonics. This work establishes a novel physical framework for next-generation AI hardware development.

---


### 373. [ComplexConstraints and Beyond: Expert Rubrics for RLVR](https://arxiv.org/abs/2606.09118)

**<font color=#1a73e8>作者：</font>** Sushant Mehta, Liudas Panavas, Edwin Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM capabilities advance rapidly, the evaluation methods used to assess them increasingly lag behind. Traditional benchmarks relied on programmatic verification of narrow, surface-level constraints, but real-world instruction following and agentic tasks demand assessment of nuanced, context-dependent behaviors that resist simple scripted checks. We present a systematic analysis of expert-curated rubric-based evaluation as an alternative paradigm, drawing on empirical evidence from two domains: complex instruction following and enterprise agentic tasks. We first articulate five design principles for constructing high-quality rubrics, including Maximum Viable Atomicity, intent-aware criterion design, and iterative LLM-judge calibration. To validate these principles, we introduce ComplexConstraints, a new expert-curated instruction-following dataset in which each prompt is paired with 10-40 atomic rubric criteria. We demonstrate that these expert rubrics are not only better evaluation instruments but also highly effective training signals: training on approximately 1,000 ComplexConstraints examples yields +15.5% improvement for a 4B-parameter model and +12.2% for a 235B-parameter model on instruction following, while single-epoch RL training on a rubric-graded enterprise environment produces gains that transfer to out-of-distribution benchmarks the model was never trained on (+4.5% BFCL, +7.4% Tau2-Bench, +6.8% Tool-Decathlon). Our findings establish that expert-authored rubrics improve both the measurement and the development of frontier LLM capabilities, serving as effective evaluation and RL training signals.

---


### 374. [An Enhanced Geometric-Spectral Feature Learning Framework for Airborne Multispectral Point Cloud Classification](https://arxiv.org/abs/2606.09123)

**<font color=#1a73e8>作者：</font>** Xian Li, Yanfeng Gu, Aleksandra Pižurica  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral point cloud (MPC) is composed of 3D spatial-spectral information, which holds tremendous potential for accurate land-cover classification. However, the representation power of classification models is limited by inherent high-dimensional and heterogeneous spatial-spectral information, unbalanced sample distribution, and inter-class spectral similarity of airborne MPCs. We build two MPC datasets and propose an enhanced geometric-spectral feature learning framework based on attentions for airborne MPC classification. A key component in our model is a two-stream feature fusion method with attention mechanisms, which enhances the representation capability of spatial-spectral features from high-dimensional heterogeneous MPCs. The first stream aims to extract position-encoded global spectral features with fusion self-attention, and the second stream comprises a multikernel point convolution and feature aggregation attention to extract spectral-guided geometric features. We then develop a residual attention fusion block to integrate the most informative geometric-spectral features from the two parallel streams. Another important contribution of this work is a joint loss function to improve the learning ability on unbalanced and interclass similar samples. Experimental results on two airborne MPC datasets demonstrate the effectiveness of the proposed method compared with the state-of-the-art methods. Furthermore, the codes and datasets used in this paper will be made available freely at this https URL.

---


### 375. [A Geometric Framework for Absolute Pose and Velocity Estimation with Event Cameras](https://arxiv.org/abs/2606.09139)

**<font color=#1a73e8>作者：</font>** Zibin Liu, Shunkun Liang, Banglei Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancements in event-based motion estimation, current geometric methods primarily focus on velocity estimation. However, absolute pose estimation, which is equally crucial for key applications such as robotic navigation and augmented reality, remains relatively underexplored. Consequently, the simultaneous recovery of absolute pose and velocity from event streams remains an open and challenging problem. To address this gap, we propose a geometric framework for absolute pose and velocity estimation by leveraging 3D lines in the scene and the events they trigger. At the core of the framework lie two key geometric constraints: the orthogonality between a 3D line and the normal vector of its corresponding event plane, and the collinearity of an event with the 2D projection of its associated line. Based on these constraints, we present both linear and polynomial solvers for absolute pose estimation. The former enables efficient computation, while the latter provides a globally optimal solution for rotation. For velocity estimation, we develop an efficient linear solver and a more accurate optimization-based solver to recover both angular and linear velocities. Notably, our methods require a minimum of three event-line correspondences to determine the 6-DoF absolute pose or velocities independently. Extensive experiments in simulation and on real-world datasets demonstrate that our methods achieve state-of-the-art performance, with significant improvements in accuracy and computational efficiency compared to existing methods. The demo code is publicly available at this https URL.

---


### 376. [DiffSight-Former: Modeling Structural Differences and Temporal Dynamics for Glaucoma Progression Prediction](https://arxiv.org/abs/2606.09140)

**<font color=#1a73e8>作者：</font>** Yi Huang, Lei Bi, Jinman Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a leading cause of irreversible blindness worldwide, and early detection from fundus images is critical for effective disease management. While deep learning has achieved promising performance in fundus image analysis, most existing methods rely on single time-point images and fail to capture longitudinal structural and vascular changes associated with disease progression. Sequential fundus images acquired during clinical follow-up provide valuable temporal information; however, current sequential models often struggle to detect subtle early progression signals and commonly depend on fixed-length inputs or diagnostic cues from already glaucomatous images, limiting their clinical utility for early prediction. To address these limitations, we propose DiffSight-Former, a framework for glaucoma progression prediction from sequential fundus images. It incorporates a time-variant feature extraction module based on a fundus-specific foundation model to obtain robust anatomical representations. A multi-structure difference modeling module is introduced to quantify progression-related changes in the optic disc/cup region and retinal vasculature. These representations are integrated with temporal interval embeddings and processed by a time-aware Transformer to model disease progression and estimate the probability of future glaucoma onset. Experiments were conducted on two longitudinal datasets, SIGF (405 sequences) and GRAPE (263 sequences). On SIGF, DiffSight-Former achieved an AUC of 91.54% and a sensitivity of 92.16% for progression prediction. On GRAPE, it achieved an average accuracy of 87.48% across three clinical visual-field progression criteria. Compared with existing approaches, DiffSight-Former demonstrates strong performance and robustness across different temporal settings, highlighting its potential for longitudinal glaucoma monitoring and early risk prediction.

---


### 377. [Ultra Flash: Scaling Real-Time Streaming Video Generation to High Resolutions](https://arxiv.org/abs/2606.09150)

**<font color=#1a73e8>作者：</font>** Luxury, Jie Huang, Zihao Fan 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent autoregressive video diffusion models achieve remarkable streaming quality, they remain confined to low resolutions (e.g., 480P), leaving efficient, scalable, real-time high-resolution video generation a fundamental open challenge. To bridge this gap, we present Ultra Flash, a cascaded streaming framework capable of real-time high-resolution video generation. Ultra Flash achieves ~30 FPS at 1K resolution and ~18 FPS at 2K resolution on a single GPU through three key contributions: (1) an architecture-preserving T2V-to-TV2V super-resolution training paradigm coupled with an AIGC-oriented data degradation pipeline that effectively preserves the generative capability of the base model, enabling enhanced high-resolution detail when cascaded after mainstream low-resolution generative models; (2) a causal streaming latent upsampler paired with a high-resolution decoder, which enhances spatiotemporal coherence while enabling efficient latent spatial scaling and precise high-resolution decoding with negligible computational overhead; and (3) a cascade high-resolution streaming video generation optimization scheme that first performs hybrid-reward-enhanced sparse causalization and single-step distillation of the super-resolution model, then introduces cascaded streaming self-forcing preference optimization with dynamic cache management, jointly enhancing overall coherence, improving quality, and enabling real-time high-resolution streaming video generation. Extensive experiments demonstrate that Ultra Flash reliably produces ultra-high-resolution streaming video while maintaining state-of-the-art visual quality and superior efficiency.

---


### 378. [Customization under Fire: Plugin Poisoning in Text-to-Image Ecosystem](https://arxiv.org/abs/2606.09151)

**<font color=#1a73e8>作者：</font>** Jiahao Chen, Xing He, Yong Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The prosperity of text-to-image (T2I) models has fostered a vibrant share-and-play ecosystem centered on Low-Rank Adaptation (LoRA) plugins, which allow users to customize and share model capabilities with ease. This democratization, however, comes with a hidden but severe security risk. Malicious users could share and distribute seemingly benign LoRA plugins that contain hidden functionalities to poison the model-sharing market, like Civitai or Liblib, severely undermining the user trust that underpins this collaborative ecosystem and threatening the safety of countless downstream applications. Despite these risks, plugin poisoning in the real-world T2I ecosystem remains underexplored. This paper introduces PoisonLoRA, the first systematic study of LoRA plugin supply-chain risks that exploits the trust and characteristics within the T2I ecosystem. We identify two primary attack instances: (1) Concept Hijacking, where a hijacked LoRA could generate images to influence public opinion and spread propaganda, and (2) Task Injection, where a LoRA is injected to produce harmful content (e.g., NSFW images) only activated by a secret key. Critically, the malicious payload persists with virus-like propagation. Such propagations weaponize the very act of creative collaboration (e.g., LoRA merging) to spread its contagion, turning every remix into a new carrier. Extensive experiments validate that PoisonLoRA is both effective and stealthy. Specifically, we achieve approximately 100% attack success rates (ASR) on both Civitai and Liblib on 6 datasets across 4 scenarios, without being detected by the platforms. The poisoned LoRA demonstrates extreme robustness, with nearly 100% ASR even transferred to different base models and remixed more than 5 times.

---


### 379. [Improved Convergence Analysis of Topology Dependence in Decentralized SGD](https://arxiv.org/abs/2606.09154)

**<font color=#1a73e8>作者：</font>** Yuki Takezawa, Anastasia Koloskova, Sebastian U. Stich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized SGD is a fundamental algorithm in decentralized learning, although the influence of an underlying network topology on its convergence behavior is not yet fully understood. Existing convergence analyses have shown that topologies with a small spectral gap significantly deteriorate the convergence rate of Decentralized SGD in both homogeneous and heterogeneous cases. However, many prior papers have reported that indeed the choice of the topology has a significant experimental impact in the heterogeneous case, but has little experimental impact on training behavior in the homogeneous case. In this paper, we present a tighter convergence analysis of Decentralized SGD, offering a more precise understanding of how topologies affect the convergence rate than the prior analysis. Specifically, unlike existing convergence analyses that used only the spectral gap as a property of the topology, our novel analysis shows that all eigenvalues of the mixing matrix affect the convergence rate. Throughout the experiments, we carefully evaluated the convergence behavior of Decentralized SGD and demonstrated that our novel convergence analysis can more accurately describe the effect of topology on the convergence rate.

---


### 380. [OmniGen-AR: AutoRegressive Any-to-Image Generation](https://arxiv.org/abs/2606.09156)

**<font color=#1a73e8>作者：</font>** Junke Wang, Xun Wang, Qiushan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) models have demonstrated strong potential in visual generation, offering superior performance with simple architectures and optimization objectives. However, existing methods are typically limited to single-modality conditions, e.g., text, restricting their applicability in real-world scenarios that demand image synthesis from diverse controls. In this work, we present OmniGen-AR, a unified autoregressive framework for Any-to-Image generation. By discretizing various visual conditions through a shared visual tokenizer and text prompts with a text tokenizer, OmniGen-AR supports a broad spectrum of conditional inputs within a single model, including text (text-to-image generation), spatial signals (segmentation-to-image and depth-to-image), and visual context (image editing, frame prediction, and text-to-video generation). To mitigate the risk of information leakage from condition tokens to content tokens, we introduce Disentangled Causal Attention (DCA), which separates the full-sequence causal mask into condition causal attention and content causal attention. It serves as a training-time regularizer without affecting the standard next-token prediction during inference. With this design, OmniGen-AR achieves new state-of-the-art or at least competitive results across a range of benchmark, e.g., 0.63 on GenEval and 80.02 on VBench, demonstrating its effectiveness in flexible and high-fidelity visual generation.

---


### 381. [Crop Recommendation and Agricultural Query Answering System Using Spatio-Temporal Graph Neural Networks and Hybrid Retrieval Augmentation](https://arxiv.org/abs/2606.09160)

**<font color=#1a73e8>作者：</font>** Prajwal Thapa, Yagya Raj Pandeya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a unified system designed to support precision agriculture by integrating advanced weather prediction, crop recommendation, and a question-answering tool for farmers. We propose two deep learning models -- a Transformer-based Graph Neural Network and a Spatio-Temporal Graph Convolutional Network (STGCN) -- to forecast weather conditions for the next 30 days using data from 1,359 locations in Nepal. The STGCN outperforms the Transformer-based model in accuracy (MSE ~0.011 vs. 0.013), effectively modeling both spatial and temporal dependencies in climate data. These predictions are combined with static soil properties such as pH, moisture, and organic content to generate localized crop recommendations through a scoring algorithm that matches each crop's optimal growing conditions. Additionally, we develop a Retrieval-Augmented Generation (RAG) chatbot that leverages domain-specific agricultural documents to answer farmers' questions in natural language. The entire system is deployed via a mobile application, offering real-time suggestions and conversational support. User feedback confirms the system's usability and relevance, especially in rural settings where personalized farming guidance is limited. Overall, our approach demonstrates how combining machine learning models with local agricultural data can empower farmers with actionable insights, promoting more informed decisions, better crop yields, and increased resilience to climate variability.

---


### 382. [Zero-Parameter Geometric Gating for Temporally Stable Low-Altitude UAV Video Semantic Segmentation](https://arxiv.org/abs/2606.09162)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Fengxian Ji, Zhengzhao Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video semantic segmentation for low-altitude UAVs requires temporal consistency, yet dense optical flow introduces spatially structured noise in the planar regions that dominate aerial imagery. We propose a zero-parameter geometric gate that uses RANSAC homography inlier ratios on a $16\times16$ spatial grid to route each region to either homography or optical flow warp before fusion via Semantic Similarity Propagation. The gate requires no learned parameters -- only a median-threshold binary decision on RANSAC statistics -- adding only 211K trainable parameters (the SSP fusion layer) to a frozen backbone. On synthetic UAVid, the method achieves +4.24--4.91\% mIoU improvement over base models across two architectures (SegFormer-b2 and Hiera-S+UPerNet). Mechanism diagnostics reveal that flow residuals in planar regions are spatially autocorrelated (Moran's I = 0.32, $p < 0.001$), predict boundary instability (Spearman $\rho = 0.66$), and that rigidification recovers temporal consistency from 62\% to 92\% (+29.5pp) in homography-valid regions.

---


### 383. [EnclaveScale: Hardware-Assisted Edge-DP for Secure Data Centre Power Telemetry](https://arxiv.org/abs/2606.09163)

**<font color=#1a73e8>作者：</font>** Hung Dang, Tue Nguyen, Minh Vo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EnclaveScale is a distributed, hardware-assisted telemetry architecture providing post-extraction attestation, enabling operators to collaboratively model high-resolution generative AI power transients. Existing cryptographic techniques scale poorly for 10-Hz streaming or fail to authenticate origins, permitting malicious hosts to spoof sensor inputs. We implement and evaluate a post-extraction pipeline utilizing DCAP attestation, differential privacy noise injection, and Byzantine rejection across 32 GCP Confidential VMs, achieving 0\% post-extraction attack success rate. This edge-DP approach distils continuous GPU transients into discrete Markov-chain transition matrices, guaranteeing event-level differential privacy. To mitigate pre-ingestion vulnerabilities, we propose an SPDM-authenticated first-mile layer. While current platforms lack attested I/O, emerging hardware architectures integrate PCIe IDE and TDISP to natively prevent host-level synthesis, securing the end-to-end provenance boundary. A Global Aggregation Enclave verifies these cryptographic proofs prior to capacity-weighted aggregation. Evaluation demonstrates a steady-state throughput of $131{,}406$ samples/s per enclave, amortising attestation overhead to $0.23\,\mu$s/sample. On empirical NVML-sampled H100, A100, and L4 traces, EnclaveScale achieves a dynamic orchestration margin error of $1.3$\,MW compared to $0.1$\,MW for an honest-aggregator central-DP baseline. EnclaveScale establishes a secure foundation for dynamic multi-tenant power orchestration, obfuscating sub-second anomalies locally and protecting macro-workload confidentiality via spatial dilution during global aggregation.

---


### 384. [Reliable to Expressive: A Curriculum for Rubric-Following Safety Judges](https://arxiv.org/abs/2606.09165)

**<font color=#1a73e8>作者：</font>** Yongtaek Lim, Hyeji Choi, Minwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety judges are increasingly deployed to evaluate model outputs against evolving criteria, yet recent meta-evaluation work shows they remain brittle under prompt and rubric variation, with false negative-rate swings of up to 0.24 reported for stylistic perturbations alone. We argue that safety judgment is fundamentally a rubric-following problem: a robust judge must apply the given evaluation criteria consistently across rubric formulations rather than memorize one specific template. We propose a training strategy that combines (i) instance-conditioned dynamic rubrics generated from prompt-response-label triples to expose the judge to the variability of evaluation criteria, and (ii) a reliable-to-expressive curriculum that begins with clean fixed-rubric supervision and progressively introduces noisier dynamic-rubric data. We evaluate on a single human-labeled set under three contrasting rubric prompts (HarmBench-style, ShieldGemma-style, and a domain-specific rubric). Our 12B curriculum judge achieves 94.12-94.88% accuracy across the three rubrics with a cross-rubric range of only 0.76, outperforming general-purpose LLMs, dedicated safety classifiers, and reasoning-oriented judges up to 30B in both peak accuracy and stability. An ablation shows that naively mixing dynamic rubrics into SFT increases cross rubric variance (1.44 -> 3.60); only the curriculum schedule recovers and improves on the fixed rubric baseline (variance 0.76).

---


### 385. [sketch-plot: Progressive Editing for Text-to-Image Academic Figures](https://arxiv.org/abs/2606.09171)

**<font color=#1a73e8>作者：</font>** Yinghao Tang, Yupeng Xie, Yingchaojie Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Text to image (T2I) models such as gpt-image-2 can now generate publication grade academic figures from a short prompt, but the output is a flat raster: a user who wants to change one arrow, one label, or one icon has to regenerate the whole image, which also disturbs the parts they wanted to keep. We present sketch-plot, an interactive system that closes this controllability gap with a three layer progressive editing pipeline: a generated PNG, an addressable puzzle of editable pieces, and a per piece SVG. The user stops at the layer that gives them enough control for the change at hand, so the cost of decomposition and vectorisation is paid only on the pieces that need it. Realising this pipeline is not trivial. General segmentation models lack the semantic discriminability to decompose a research figure cleanly, and end to end image vectorisation produces incomplete shapes and loses semantic structure. We therefore route both stages through a human in the loop interface that lets the user accept, refine, or reject decomposition and vectorisation decisions on a piece by piece basis. We validate the design with an expert user study, in which participants found sketch-plot effective for making targeted edits to AI generated academic figures and preferred it over regenerating the whole image. A demonstration video is available at this https URL.

---


### 386. [Demonstrating chart-plot: Closing the Last Mile of Academic Chart Generation](https://arxiv.org/abs/2606.09174)

**<font color=#1a73e8>作者：</font>** Yinghao Tang, Yupeng Xie, Yingchaojie Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models can translate a researcher's intent into runnable matplotlib code, yet the resulting chart rarely lands in a paper without multiple rounds of manual revision. We argue that the open problem is not chart code generation but chart publication: making the output look like a top-venue figure, survive the target layout, and respond to precise author edits. We present chart-plot, an agentic harness that closes this last mile through three components: (1) a style-aware code generator conditioned on a textual style skill distilled from accepted figures at the target venue, (2) a deployment-aware render loop that compiles the chart inside the target LaTeX context and revises until layout constraints are met, and (3) a structured edit layer that exposes every chart element as a directly manipulable handle. We report early results on three chart-type case studies (grouped bar, scaling line, paired distributions) and a small user study.

---


### 387. [CANS: Accelerating Multiuser Collaborative Edge Inference via Cooperative Autodidactic NeuroSurgeon](https://arxiv.org/abs/2606.09175)

**<font color=#1a73e8>作者：</font>** Zheshun Wu, Ziyang Zhang, Changyao Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, mobile edge computing (MEC)-enabled collaborative deep neural network (DNN) inference has emerged as a promising approach for delivering intelligent services to resource-constrained mobile devices. A representative scenario is multi-user collaborative edge inference, where distinct devices independently partition their DNN models and offload backend computation to a common edge server over wireless networks. However, determining the optimal DNN partition for each device is challenging due to unknown and time-varying system conditions, including fluctuating wireless links and diverse device capabilities. To address this problem, we propose Cooperative Autodidactic NeuroSurgeon (CANS), a collaborative edge inference framework that enables devices to adaptively learn optimal DNN partitions by sharing informative feedback during online inference. To handle the challenge of device heterogeneity and better leverage offline inference experience, we integrate a novel FedLinUCB-DW algorithm that groups devices of the same type and warm-starts online exploration using local offline early-exit inference experience. Furthermore, we provide theoretical guarantees for FedLinUCB-DW by deriving the regret upper bound. We also validate our method on both a simulated environment and a hardware prototype system. Empirical evaluations demonstrate that CANS achieves lower inference latency compared to state-of-the-art baselines. Especially, in prototype experiments on two edge devices, the proposed CANS reduced average inference latency by up to 50% compared to the non-cooperative baseline.

---


### 388. [Performance Evaluation of Social Learning](https://arxiv.org/abs/2606.09176)

**<font color=#1a73e8>作者：</font>** Felice Scala, Marco Carpentiero, Vincenzo Matta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Social Learning is a decentralized decision-making paradigm in which spatially dispersed agents collect streaming observations regulated by one of a finite number of models (the hypotheses). The agents are interested in assigning probability scores (the beliefs) to the possible hypotheses. To this end, the agents exchange their beliefs according to a certain communication graph. It has been shown that, under reasonable conditions on the identifiability of the decision model and the network connectivity, each agent ultimately places all the belief mass on the true hypothesis governing the data. However, several questions remain unanswered regarding the evaluation of the social learning performance. One recently adopted performance metric is the rejection rate, i.e., the rate at which the beliefs about the erroneous hypotheses vanish. One contribution of this work is to establish that the rejection rate leads to several paradoxes, which make it unsuitable as a valid performance measure. We then focus on studying the error probability measure. For a binary Gaussian problem, we derive an analytical formula characterizing the ratio between the individual agents' probabilities and the optimal Bayesian probability. The formula shows that this ratio is expressed by the product of two terms quantifying the effect of the network connectivity and the role of the prior information. As a result, an irreducible gap emerges between the decentralized and the centralized error probabilities, which is agent-dependent and does not disappear asymptotically.

---


### 389. [Culturally-Adapted Red-Teaming Across East and Southeast Asian Contexts: A Methodological and Comparative Analysis](https://arxiv.org/abs/2606.09178)

**<font color=#1a73e8>作者：</font>** Hyeji Choi, Yongtaek Lim, Minwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual safety evaluation of large language models (LLMs) has predominantly relied on direct translation (DT) of English benchmarks into target languages - an approach that converts surface-level linguistic form while failing to reflect the cultural context embedded in threat scenarios, social norms, and legal frameworks. We construct paired DT and culturally-adapted (CA) datasets via 1:1 seed matching for four languages - Korean (KO), Japanese (JA), Thai (TH), and Khmer (KM) - and compare Attack Success Rate (ASR) and Cultural Realism scores across four open-source LLM. CA prompts yield Delta-ASR > 0 across all 16 language x model combinations (mean +9.3 pp), and DT-based evaluation underestimates risk in 44 of 48 category x language combinations. Language-level analysis reveals that the distribution of threat forms is heterogeneous across languages. Cultural Realism analysis further shows that DT Cultural Depth (C3) scores remain consistently below 1.0 out of 3.0 across all four languages (mean 0.17), whereas CA scores reach up to 2.51, indicating that direct translation produces inputs systematically divergent from those encountered in real-world multicultural settings. These findings demonstrate that adapting benchmarks to language-specific cultural contexts - rather than relying on linguistic translation alone - is necessary for valid multilingual LLM safety evaluation.

---


### 390. [Counterfactual Reasoning for Fine-Grained Evidence Disentanglement in VideoQA](https://arxiv.org/abs/2606.09181)

**<font color=#1a73e8>作者：</font>** Zhou Du, Hamid Krim, Xiao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video multimodal models have significantly improved VideoQA performance. However, these systems often rely on spurious statistical correlations rather than answer-relevant causal evidence, resulting in unfaithful and brittle reasoning, especially in complex real-world scenarios. Existing methods either rely on cross-modality correlations, costly curated training resources, or insufficient causal assumptions and constraints, and typically operate at the time-interval level. As a result, they fail to explicitly disentangle causal visual cues from confounders and provide limited fine-grained evidence localization. To address this issue, we propose a Counterfactual Reasoning framework for fine-grained Evidence Disentanglement (CREDiT). CREDiT formulates the VideoQA process using a structural causal model and learns cross-modality representations that are explicitly decomposed into causal and non-causal components under independence and minimality constraints. To facilitate faithful disentanglement, we introduce feature-level causal interventions and construct counterfactual inputs that approximate causal effects while suppressing non-causal correlations. Extensive experiments on NExT-GQA, SportsQA, and SPORTU-video demonstrate that CREDiT consistently improves answer accuracy and reasoning reliability across both generic and complex sports scenarios, leading to more trustworthy VideoQA systems.

---


### 391. [DuplexOmni: Real-Time Listening, Seeing, Thinking, and Speaking for Full-Duplex Interaction](https://arxiv.org/abs/2606.09186)

**<font color=#1a73e8>作者：</font>** Muye Huang, Lingling Zhang, Xingyu Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human interaction is continuous, multimodal, and full-duplex by nature. Although recent omni models have made substantial progress in unified speech, vision, and text modeling, combining seamless real-time interaction with complex reasoning and tool use remains challenging. We present DuplexOmni, a method for real-time multimodal full-duplex interaction. DuplexOmni separates model capability into an interaction layer and a thinking layer, which collaborate asynchronously in parallel. The interaction layer is implemented by the DuplexOmni model, an end-to-end system that processes streaming audio and video inputs while generating text and speech responses in real time. The thinking layer is a pluggable module that provides complex reasoning and tool-use capabilities. To support this method, we further develop a Writer-Director pipeline for constructing continuous-interaction training data. Experiments show that DuplexOmni achieves strong performance on multiple public benchmarks and exhibits natural full-duplex interaction ability.

---


### 392. [CP4D: Compositional Physics-aware 4D Scene Generation](https://arxiv.org/abs/2606.09187)

**<font color=#1a73e8>作者：</font>** Hanxin Zhu, Cong Wang, Tianyu He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D generation (\textit{i.e.}, dynamic 3D generation) has recently emerged as a rapidly growing research frontier due to its powerful spatiotemporal modeling capabilities. However, despite notable advances, existing approaches typically fail to capture the underlying physical principles, producing results that are both physically inconsistent and visually implausible. To overcome this limitation, we present CP4D, a novel paradigm for photorealistic 4D scene synthesis with faithful adherence to complex physical dynamics. Drawing inspiration from the compositional nature of real-world scenes, where immutable static backgrounds coexist with dynamic, physically plausible foregrounds, CP4D reformulates 4D generation as the integration of a static 3D environment with physically grounded dynamic objects. On this basis, our framework follows a three-stage pipeline: \textbf{1)} Firstly, we leverage pre-trained expert models to generate high-fidelity 3D representations of the environment and foreground objects respectively. \textbf{2)} Subsequently, to produce physically plausible trajectories and realistic interactions for these objects, we propose a hybrid motion synthesis strategy that integrates priors from physical simulators with the common sense embedded in video diffusion models. \textbf{3)} Finally, we develop an automated composition mechanism that seamlessly fuses the static environment and dynamic objects into coherent, physically consistent 4D scenes. Extensive experiments demonstrate that CP4D can generate explorable and interactive 4D scenes with high visual fidelity, strong physical plausibility, and fine-grained controllability, significantly outperforming existing methods. The project page: this https URL.

---


### 393. [Asymptotic Optimality of Thompson Sampling for Risk-Averse Bandits with Sub-Gaussian Rewards](https://arxiv.org/abs/2606.09191)

**<font color=#1a73e8>作者：</font>** Joel Q. L. Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that $\rho\text{-}\mathrm{NPTS}_{\mathrm{SG}}$, an anchor-free nonparametric Thompson Sampling algorithm for risk-averse bandits, achieves regret matching the instance-dependent lower bound to leading order in $\log n$, establishing it as asymptotically optimal for any continuous risk functional $\rho$ (CVaR, mean-variance, Sharpe ratio, distortion risk measures, and more) on the class of distributions with bounded density and sub-Gaussian tails, including Gaussian arms. Both this result and its bounded-support counterpart require only continuity of $\rho$: strictly weaker than the dominance condition of prior parametric Thompson Sampling results, and strictly weaker than the Lipschitz condition of UCB-type algorithms, yielding the first instance-optimal guarantees for non-Lipschitz functionals such as the Sharpe ratio without parametric reward assumptions. The bounded-support case is developed first as a stepping stone sharing the same proof structure. The key technical contributions are a discretisation lemma (bounded support) and a truncated discretisation lemma (sub-Gaussian tails), each projecting the growing-alphabet Dirichlet posterior onto a fixed grid via the Dirichlet aggregation property, holding all polynomial prefactors at fixed degree independent of sample size and breaking the super-exponential barrier that blocked prior proofs.

---


### 394. [Minimal Solvers for Full-DoF Motion Estimation from Asynchronous Differential SfM](https://arxiv.org/abs/2606.09218)

**<font color=#1a73e8>作者：</font>** Shuo Pan, Banglei Guan, Bin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a bio-inspired intelligent sensor, event cameras have introduced a new paradigm in the intelligent perception of spatiotemporal information and visual motion estimation, characterized by their high temporal resolution, low latency, and minimal power consumption. However, their asynchronous data streams present significant challenges to traditional synchronous, frame-based algorithms. To address these challenges, this paper presents a novel framework for full degree of freedom (DoF) egomotion estimation directly from asynchronous optical flow, specifically targeting the joint recovery of angular and linear velocities. We decouple the differential epipolar constraint into distinct angular and linear velocity components, and derive its formulation for asynchronous data. Based on this formulation, an optimization algorithm is developed that enables full-DoF egomotion estimation leveraging at least five points. Furthermore, by applying a first-order approximation to rotational dynamics, we transform the constraint equations into a polynomial form, resulting in the first algebraic minimal 5-point solver for this formulation. To ensure real-time performance in high-speed scenarios, we additionally propose an accelerated solver achieved by truncating high-order angular velocity terms. Extensive evaluations on both synthetic and real-world datasets demonstrate that the asynchronous approach outperforms traditional synchronous methods, particularly in its accuracy and robustness to spatiotemporal noise. We believe that this work establishes a critical foundation for efficient and accurate continuous-time motion estimation in high-speed robotics applications.

---


### 395. [Semi-supervised Source Detection in Astronomical Images: New Benchmark and Strong Baseline](https://arxiv.org/abs/2606.09219)

**<font color=#1a73e8>作者：</font>** Longhan Feng, Zihuang Cao, Ali Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source detection in modern observational astronomy is a cornerstone for localizing and identifying stellar sources accurately. It is crucial for studies such as stellar population synthesis and cosmological parameter estimation. However, the characteristics of astronomical images, including high density, the effect of point spread functions and low signal-to-noise ratios, significantly challenge the latest advanced object detectors. Besides, fully-supervised detection methods are hardly practical, due to the significant difficulty in annotating dense, small, and faint sources in astronomical images. To tackle the scarcity of astronomical datasets, we introduce a new comprehensive benchmark (LAMOST-DET), comprising 18,400 astronomical images and 728,898 source instances. Upon the dataset, we further devise a novel semi-supervised learning framework coined Nova Teacher, capable of detecting dense sources effectively given sparse annotations. It integrates source light enhancement module, confidence-guided pseudo-supervision, and cross-view complementary mining in a dual-teacher paradigm. Extensive experiments on LAMOST-DET show that, Nova Teacher consistently improves previous competitors by 4.04% and 5.22% mAP under two semi-supervised settings. Additionally, our method competes against other detectors on a natural image dataset, validating its generalization ability to various scenarios. The source code is available at this https URL.

---


### 396. [Trustworthy Smart Fabs via Professional Proxies: Scaling Safe and Sustainable by Design (SSbD) through Industrial Data Spaces](https://arxiv.org/abs/2606.09227)

**<font color=#1a73e8>作者：</font>** Han-Teng Liao, Chang-Yi Kao, Karen Ang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The convergence of the 2026 European Union Safe and Sustainable by Design (SSbD) framework, Corporate Sustainability Due Diligence Directive (CSDDD), and Carbon Border Adjustment Mechanism (CBAM) introduce a severe governance bottleneck for advanced semiconductor manufacturing facilities ("Smart Fabs"). Regulatory compliance demands have surpassed the capacity of manual corporate reporting, creating a direct conflict between multi-stakeholder transparency and corporate data privacy. This paper addresses this challenge by introducing a zero-trust socio-technical orchestration framework that operationalizes a six-layer SSbD reference architecture within trustworthy industrial data spaces. We propose a shift from reactive automation to autonomous governance through "Professional Proxies"-role-based agentic workflows executing within hardware-isolated trust zones. Structured as an interoperable network protocol stack, the framework coordinates an automated, five-step "relay race" between Facility, Process Engineering, and Finance proxy teams to align factory-floor yield models with macro-level sustainability mandates. By executing Virtual Metrology (VM) predictions and Federated Machine Learning (FML) inside hardware-rooted Trusted Execution Environments (TEEs), this architecture resolves the Data Sovereignty Paradox, demonstrating how fabs can export cryptographically signed compliance tokens via International Data Spaces (IDS) connectors without exposing proprietary process recipes. Ultimately, this framework provides technology managers with a verifiable, evidence-based pathway toward resilient, net-zero Industry 5.0 ecosystems.

---


### 397. [Orange Lab: Lowering Barriers to Data Mining through Embedded Interactive Workflows](https://arxiv.org/abs/2606.09239)

**<font color=#1a73e8>作者：</font>** Matej Bevec, Aleš Erjavec, Vesna Tanko 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While visual programming of data analysis workflows has become an important vehicle for the democratization of data science, such systems remain largely confined to standalone applications and offer limited support for transitioning their visual analytics solutions into interactive web environments. As a result, data analysis pipelines are difficult to share, embed, and adapt into user-facing analytical tools. We present Orange Lab, a web-based collaborative environment for visual data analytics. At its core, Orange Lab enables users to visually construct machine learning workflows from modular components, where interactions in any component propagate seamlessly through the workflow, turning static pipelines into dynamic, reactive systems that support exploration and data-driven storytelling. Our key contribution is component exposition, a paradigm that allows authors to embed selected workflow components, or parts of their interfaces, into arbitrary web contexts, creating synchronized, interactive interfaces while hiding underlying workflow complexity. This enables the development of tailored analytical views and narrative-driven experiences that integrate data analysis directly into online materials. We demonstrate the approach through deployments in data literacy education, where embedded components guide students in hands-on exploration of machine learning concepts without requiring knowledge of the underlying system, showing that Orange Lab effectively lowers barriers to entry and supports the democratization of data science.

---


### 398. [Conceptualising Reflective Use: Toward A Process Perspective On Human-AI Interaction](https://arxiv.org/abs/2606.09242)

**<font color=#1a73e8>作者：</font>** Thimo Schulz, Christina Speck  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid diffusion of generative artificial intelligence (genAI) systems reshapes how individuals engage with information systems, requiring users to monitor, assess, and adapt their interaction with non-deterministic systems. Existing constructs capture elements of this engagement but do not account for the situated dynamics of the entire evaluative process in genAI use. This research-in-progress, situated in a larger endeavour towards a scale development, derives an initial conceptualisation of reflective use: a behavioural-knowledge capability that unfolds across pre-use, in-use, and post-use phases, reinforced through situated reflective knowledge gained in practice. Drawing on expert interviews and a focus group, we identify four core components of reflective use and show how they form an iterative capability cycle anchored within the motivational needs outlined in self-determination theory. Understanding reflective use is essential to ensure appropriate reliance and high decision quality, and thus provides a foundation for promoting responsible and effective human-AI interaction.

---


### 399. [EgoTactile: Learning Grasp Pressure for Everyday Objects from Egocentric Video](https://arxiv.org/abs/2606.09243)

**<font color=#1a73e8>作者：</font>** Yuan Zeng, Yujia Shi, Tiao Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating full-hand grasp pressure from egocentric video is critical for immersive VR and robotic manipulation, yet dense tactile sensing often relies on intrusive hardware. Existing vision-based methods predominantly rely on planar surfaces or fingertip contacts, failing to generalize to complex 3D object interactions. Therefore, we introduce EgoTactile, a benchmark pairing egocentric video with full-hand pressure supervision for diverse everyday objects, incorporating a bare-hand transfer subset to enable generalization to natural scenarios. Leveraging this benchmark, we first establish EgoPressureFormer as a discriminative baseline. Beyond this, to explicitly address the uncertainty in partial observations, we propose EgoPressureDiff, a conditional diffusion framework that adapts a large-scale pre-trained video diffusion backbone. By combining rich world knowledge priors with a Physically-Informed Feature Rectification layer to inject semantic constraints, our approach effectively infers plausible contact patterns and resolves visual-physical ambiguities. Extensive experiments demonstrate that our method achieves superior performance on the benchmark and robust transferability to in-the-wild scenarios. Our project page is available at this https URL.

---


### 400. [Proposal Refinement for Few-Shot Object Detection](https://arxiv.org/abs/2606.09245)

**<font color=#1a73e8>作者：</font>** Yuan Zeng, Bin Song, Jie Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot object detection has gained widely attention in recent years. Some excellent algorithms have been proposed to handle this task. However, most of these algorithms rely on the performance of few-shot classification. Unlike previous attempts, our work focuses on the problem of unbalanced distribution of region proposals between the novel classes and the base classes. In order to alleviate this unbalanced distribution, we propose the proposal refinement approach for different training phases. Specifically, refinement loss is designed for the base training phase to enhance sensitivity of the model to novel classes, and refinement branch is introduced as an auxiliary branch for RPN (Region Proposal Networks) to generate more novel proposals in the fine-tuning phase. By rebalancing the proposal distribution, the proposed approach outperforms the baselines methods by roughly 1\%$\sim$6\% on current benchmarks without increasing any inference time. Through extensive experiments, we prove that we establish a new state-of-the-art method for the few-shot object detection task.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
