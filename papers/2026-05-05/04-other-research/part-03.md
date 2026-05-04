# 📦 其他研究 | 2026年05月05日

> 本类共 **180** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-180](./part-04.md)

---

### 101. [Federated Learning with Hypergradient-based Online Update of Aggregation Weights](https://arxiv.org/abs/2605.00458)

**<font color=#1a73e8>作者：</font>** Ayano Nakai-Kasai, Tadashi Wadayama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning using mobile and Internet of Things devices requires not only the ability to handle heterogeneity of clients' data distributions but also high adaptability to varying communication environments. We propose FedHAW (Federated Learning with Hypergradient-based update of Aggregation Weights) that implements online updates of aggregation weights. FedHAW updates the aggregation weights by using hypergradient, the gradient of the objective function with respect to the weights, which can be calculated with low computational overhead. Simulation results show that the proposed method possesses high generalization performance in heterogeneous environments and high robustness to communication errors.

---


### 102. [PAMod: Modeling Cyclical Shifts via Phase-Amplitude Modulation for Non-stationary Time Series Forecasting](https://arxiv.org/abs/2605.00466)

**<font color=#1a73e8>作者：</font>** Yingbo Zhou, Yutong Ye, Shuhao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series forecasting faces the fundamental challenge of non-stationary statistical properties, including shifts in mean and variance over time. While reversible instance normalization (RevIN) has shown promise by stationarizing inputs and denormalizing outputs, it relies on the strong assumption that historical and future distributions remain identical. We observe that in many practical applications, distribution shifts follow cyclical patterns that correlate with periodic positions (e.g., seasonal and holiday volatility). To this end, we propose PAMod, a lightweight yet powerful framework that models cyclical distribution shifts via Phase-Amplitude Modulation in the normalized feature space. PAMod learns periodic embeddings to modulate representations: phase modulation captures mean shifts, while amplitude modulation adapts to variance changes. Crucially, we prove mathematically that modulating in normalized space is equivalent to applying dynamic denormalization, offering an elegant unification of distribution adaptation and representation learning. Extensive experiments on twelve real-world benchmarks demonstrate that PAMod achieves state-of-the-art performance with fewer computational resources. Furthermore, our modulation mechanism, as a novel plug-and-play technique, can improve existing time-series forecasting methods with simple integration.

---


### 103. [Batch Normalization for Neural Networks on Complex Domains](https://arxiv.org/abs/2605.00467)

**<font color=#1a73e8>作者：</font>** Xuan Son Nguyen, Nistor Grozavu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Riemannian neural networks have proven effective in solving a variety of machine learning tasks. The key to their success lies in the development of principled Riemannian analogs of fundamental building blocks in deep neural networks (DNNs). Among those, Riemannian batch normalization (BN) layers have shown to enhance training stability and improve accuracy. In this paper, we propose BN layers for neural networks on complex domains. The proposed layers have close connections with existing Riemannian BN layers. We derive essential components for practical implementations of BN layers on some complex domains which are less studied in previous works, e.g., the Siegel disk domain. We conduct experiments on radar clutter classification, node classification, and action recognition demonstrating the efficacy of our method.

---


### 104. [Near-optimal and Efficient First-Order Algorithm for Multi-Task Learning with Shared Linear Representation](https://arxiv.org/abs/2605.00473)

**<font color=#1a73e8>作者：</font>** Shihong Ding, Fangyu Du, Cong Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) has emerged as a pivotal paradigm in machine learning by leveraging shared structures across multiple related tasks. Despite its empirical success, the development of likelihood-based efficiently solvable algorithms--even for shared linear representations--remains largely underdeveloped, primarily due to the non-convex structure intrinsic to matrix factorization. This paper introduces a first-order algorithm that jointly learns a shared representation and task-specific parameters, with guaranteed efficiency. Notably, it converges in $\widetilde{\mathcal{O}}(1)$ iterations and attains a \emph{near-optimal} estimation error of $\widetilde{\mathcal{O}}(dk/(TN))$, \emph{improving} over existing likelihood-based methods by a factor of $k$, where $d$, $k$, $T$, $N$ denote input dimension, representation dimension, task count, and samples per task, respectively. Our results justify that likelihood-based first-order methods can efficiently solve the MTL problem.

---


### 105. [From Local to Global to Mechanistic: An iERF-Centered Unified Framework for Interpreting Vision Models](https://arxiv.org/abs/2605.00474)

**<font color=#1a73e8>作者：</font>** Yearim Kim, Sangyu Han, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision models achieve remarkable accuracy, but explaining where evidence arises, what the model encodes, and how internal computations assemble that evidence remains fragmented. We introduce an iERF-centric framework that unifies local, global, and mechanistic interpretability around a single analysis unit: the pointwise feature vector (PFV) paired with its instance-specific Effective Receptive Field (iERF). On the local side, Sharing Ratio Decomposition (SRD) expresses each PFV as a mixture of upstream PFVs via sharing ratios and propagates iERFs to construct class-discriminative saliency maps. SRD yields high-resolution, activation-faithful explanations, is robust to targeted manipulation and noise, and remains activation-agnostic across common nonlinearities. For the global view, we introduce Concept-Anchored Feature Explanation (CAFE), which utilizes the iERF as a semantic label, grounding abstract latent vectors in verifiable pixel-level evidence. With CAFE, we address the challenge of non-localized sparse autoencoder latents--especially in Transformers, where early self-attention mixes distant context. To answer how representations are composed through depth, we propose the Interlayer Concept Graph with Interlayer Concept Attribution (ICAT), which quantifies concept-to-concept influence while isolating layer pairs; an interlayer insertion, deletion protocol identifies Integrated Gradients as the most faithful instantiation. Empirically, across ResNet50, VGG16, and ViTs, our framework outperforms baselines in both fidelity and robustness, successfully interprets dispersed SAE features, and exposes dominant concept routes in correct, misclassified, and adversarial cases. Grounded in iERFs, our approach provides a coherent, evidence-backed map from pixels to concepts to decisions.

---


### 106. [Scalable Context-Aware Graph Attention for Unsupervised Anomaly Detection in Large-Scale Mobile Networks](https://arxiv.org/abs/2605.00482)

**<font color=#1a73e8>作者：</font>** Sara Malacarne, Eirik Hoel-Høiseth, Erlend Aune 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile network operators must monitor thousands of heterogeneous network elements across the radio access network and the packet core, each exposing high-dimensional KPI time series. The scale and cost of incident labelling make supervised approaches impractical, motivating unsupervised anomaly detection robust to context shifts and nonstationarity.
We propose \textbf{C-MTAD-GAT} (\emph{Context-aware Multivariate Time-series Anomaly Detection with Graph Attention}), an anomaly detection framework designed to operate as a single shared model across large populations of network elements. The model combines temporal and feature-wise graph attention with lightweight static and dynamic context conditioning and a dual-head decoder for reconstruction and multi-step forecasting. It produces per-element, per-feature anomaly scores, converted to alerts via fully unsupervised thresholds calibrated from validation residuals.
On the TELCO dataset released with DC-VAE \cite{garcia2023onemodel}, C-MTAD-GAT improves event-level affiliation and pointwise F1 while generating fewer alarms than prior graph-attention and VAE-based baselines. We then apply the same system to nation-scale radio access and evolved packet core control-plane counter data from a mobile network operator, where it is deployed. Operator feedback indicates the alerts are actionable and support daily monitoring, showing scalability across domains without relying on labelled incidents.

---


### 107. [Zero-Knowledge Model Checking](https://arxiv.org/abs/2605.00487)

**<font color=#1a73e8>作者：</font>** Pascal Berrang, Mirco Giacobbe, Jacob Swales 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce a technology to formally verify that a software system satisfies a temporal specification of functional correctness, without revealing the system itself. Our method combines a deductive approach to model checking to obtain a formal certificate of correctness for the system, with zero-knowledge proofs to convince an external verifier that the system -- kept secret -- complies with its specification of correctness -- made public. We consider proof certificates represented as ranking functions, and introduce both an explicit-state and a symbolic scheme for model checking in zero knowledge. Our explicit-state scheme assumes systems represented as transition graphs. We use polynomial commitments to convince the verifier that the public proof certificates correspond to the secret transition relation. Our symbolic scheme assumes systems specified as linear guarded commands and uses piecewise-linear ranking functions. We apply Farkas' lemma to obtain a witness for the validity of the ranking function with public and secret components, and employ sigma protocols for matrix multiplication and range proofs to convince the verifier of the witness's existence. We built a prototype to demonstrate the practical efficacy of our two schemes on linear temporal logic verification examples. Our technology enables formal verification in domains where both the safety and the confidentiality of the system under analysis are critical.

---


### 108. [Trading off rewards and errors in multi-armed bandits](https://arxiv.org/abs/2605.00488)

**<font color=#1a73e8>作者：</font>** Akram Erraqabi, Alessandro Lazaric, Michal Valko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-armed bandits, the most-explored arms are the most informative, while reward maximization typically pulls only the best arm. We study the tradeoff between identifying arm means accurately and accumulating reward, and present an algorithm with regret guarantees that interpolates between the two objectives. We provide both upper and lower bounds and validate empirically.

---


### 109. [Revealing graph bandits for maximizing local influence](https://arxiv.org/abs/2605.00489)

**<font color=#1a73e8>作者：</font>** Alexandra Carpentier, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a graph bandit setting where the objective of the learner is to detect the most influential node of a graph by requesting as little information from the graph as possible. One of the relevant applications for this setting is marketing in social networks, where the marketer aims at finding and taking advantage of the most influential customers. The existing approaches for bandit problems on graphs require either partial or complete knowledge of the graph. In this paper, we do not assume any knowledge of the graph, but we consider a setting where it can be gradually discovered in a sequential and active way. At each round, the learner chooses a node of the graph and the only information it receives is a stochastic set of the nodes that the chosen node is currently influencing. To address this setting, we propose BARE, a bandit strategy for which we prove a regret guarantee that scales with the detectable dimension, a problem dependent quantity that is often much smaller than the number of nodes.

---


### 110. [Distance metric learning for conditional anomaly detection](https://arxiv.org/abs/2605.00490)

**<font color=#1a73e8>作者：</font>** Michal Valko, Milos Hauskrecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection methods can be very useful in identifying unusual or interesting patterns in data. A recently proposed conditional anomaly detection framework extends anomaly detection to the problem of identifying anomalous patterns on a subset of attributes in the data. The anomaly always depends (is conditioned) on the value of remaining attributes. The work presented in this paper focuses on instance-based methods for detecting conditional anomalies. The methods depend heavily on the distance metric that lets us identify examples in the dataset that are most critical for detecting the anomaly. To optimize the performance of such methods we study and devise a metric learning method that learns the distance metric to reflect best the conditional anomaly pattern.

---


### 111. [High-Speed Vision Improves Zero-Shot Semantic Understanding of Human Actions](https://arxiv.org/abs/2605.00496)

**<font color=#1a73e8>作者：</font>** Yongpeng Cao, Yuji Yamakawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human actions from visual observations is essential for human--robot interaction, particularly when semantic interpretation of unfamiliar or hard-to-annotate actions is required. In scenarios such as rapid and less common activities, collecting sufficient labeled data for supervised learning is challenging, making zero-shot approaches a practical alternative for semantic understanding without task-specific training. While recent advances in large-scale pretrained models enable such zero-shot reasoning, the impact of temporal resolution, especially for rapid and fine-grained motions, remains underexplored.
In this study, we investigate how temporal resolution affects zero-shot semantic understanding of high-speed human actions. Using kendo as a representative case of rapid and subtle motion patterns, we propose a training-free pipeline that combines a pre-trained video-language model for semantic representation with large language model-based reasoning for pairwise action comparison. Through controlled experiments across multiple frame rates (120 Hz, 60 Hz, and 30 Hz), we show that higher temporal resolution significantly improves semantic separability in zero-shot settings. We further analyze the role of tracking-based human joint information under both full and partial observation scenarios. Quantitative evaluation using a nearest-class prototype strategy demonstrates that high-speed video provides more stable and interpretable semantic representations for fast actions. These findings highlight the importance of temporal resolution in training-free action recognition and suggest that high-speed perception can enhance semantic understanding capabilities.

---


### 112. ["What Are You Really Trying to Do?": Co-Creating Life Goals from Everyday Computer Use](https://arxiv.org/abs/2605.00497)

**<font color=#1a73e8>作者：</font>** Shardul Sapkota, Matthew Jörke, Zane Sabbagh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in user modeling make it feasible to conduct open-ended inference over a person's everyday computer use. Despite longstanding visions of systems that deeply understand our actions and the purposes they serve in our lives, existing systems only capture what a person is doing in the moment -- not why they are doing it -- limiting these systems to surface-level support. We introduce striving co-creation, a process for inferring broader life goals from unstructured observations of computer use. Grounded in Activity Theory and Emmons' personal strivings framework, our system progressively constructs a hierarchical representation of a person's activities. Crucially, strivings are difficult to fully resolve from observation alone, as the same action can be driven by many different goals. Our system therefore supports an editing interface that gives people agency over how they are understood by the system, feeding their corrections back into subsequent rounds of striving induction. In a week-long field deployment (N=14), we find that our co-creation process produces strivings that are representative of participants' long-term goals and gives them greater agency than baseline methods.

---


### 113. [GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498)

**<font color=#1a73e8>作者：</font>** Yonghao Zhao, Yupeng Gao, Jian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have made it standard practice to reconstruct 3D scenes from multi-view images. Removing objects from such 3D representations is a fundamental editing task that requires complete and seamless inpainting of occluded regions, ensuring consistency in geometry and appearance. Although existing methods have made notable progress in improving inpainting consistency, they often neglect global lighting effects, leading to physically implausible results. Moreover, these methods struggle with view-dependent non-Lambertian surfaces, where appearance varies across viewpoints, leading to unreliable inpainting. In this paper, we present 3D Gaussian Object Removal in the Intrinsic Space (GOR-IS), a novel framework for physically consistent and visually coherent 3D object removal. Our approach decomposes the scene into intrinsic components and explicitly models light transport to maintain global lighting effects consistency. Furthermore, we introduce an intrinsic-space inpainting module that operates directly in the material and lighting domains, effectively addressing the challenges posed by non-Lambertian surfaces. Extensive experiments on both synthetic and real-world datasets demonstrate that our framework substantially improves the physical consistency and visual coherence of object removal, outperforming existing methods by 13% in perceptual similarity (LPIPS) and 2dB in peak signal-to-noise ratio (PSNR). Code is publicly available at this https URL

---


### 114. [Scaling Federated Linear Contextual Bandits via Sketching](https://arxiv.org/abs/2605.00500)

**<font color=#1a73e8>作者：</font>** Hantao Yang, Hong Xie, Xutong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In federated contextual linear bandits, high data dimensionality incurs prohibitive computation and communication costs: local agents perform $O(d^3)$-time determinant computation and upload $O(d^2)$ parameters, making existing algorithms unscalable, where $d$ is the dimension of data. To relieve these scaling bottlenecks, this paper proposes Federated Sketch Contextual Linear Bandits (FSCLB). On the computation side, FSCLB uses SVD to indirectly obtain the determinant required for communication, eliminating the prohibitive cost of direct determinant calculation and cutting complexity from $O(d^3)$ to $O(l^2d)$ per round, where $l< d$ is the sketch size. On the communication side, FSCLB introduces a double-sketch strategy that reduces both upload and download costs from $O(d^2)$ to $O(ld)$. Naively involving sketch update into federated contextual linear bandits can destroy the local increment and invalidate the asynchronous communication condition; FSCLB solves this by replacing the covariance matrix with the sketch matrix when deciding whether to communicate. Theoretically, FSCLB achieves a regret bound of $\widetilde{O} ((\sqrt{d}+\sqrt{M\varepsilon_l})\sqrt{lT})$, where $\varepsilon_l$ is the upper bounded by the spectral tail of the covariance matrix; when $l$ exceeds the rank of the covariance matrix, the bound simplifies to $\widetilde{O}(\sqrt{ldT})$, matching the optimal no-sketch regret. Experiments on both synthetic and real-world datasets show that FSCLB significantly reduces computational and communication costs by over 90 \% while sacrificing only a negligible amount of cumulative reward.

---


### 115. [LambdaRankIC: Directly Optimizing Rank IC for Financial Prediction](https://arxiv.org/abs/2605.00501)

**<font color=#1a73e8>作者：</font>** Yan Lin, Yihong Su, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In financial predictions, the performance of machine learning models is often assessed by Rank IC, which is the Spearman rank correlation between the model predictions and the realized asset returns. Despite its wide adoption, most existing models are trained using regression losses or ranking objectives that may not align with Rank IC. We propose LambdaRankIC, a novel learning-to-rank approach that directly optimizes Rank IC. We circumvent the non-differentiability of the ranking operator by deriving the closed-form expression for the lambda gradients induced by the pairwise rank swaps, which enables efficient gradient-based optimization within the LambdaRank framework. We implement LambdaRankIC as a custom objective in XGBoost. Theoretically, we show that our approach optimizes an upper bound on Rank IC. We evaluate the proposed approach on both simulated and real-world financial data. In simulation studies, LambdaRankIC accurately recovers the true ranking structure in noiseless settings and consistently outperforms regression-based and NDCG-oriented ranking methods under low signal-to-noise ratios and heavy-tailed noise regimes. In empirical experiments using real market data, LambdaRankIC achieves the best out-of-sample performance on evaluation metrics commonly used in finance, including Rank IC, ICIR, monthly return, and Sharpe ratio. These results show that directly optimizing Rank IC can yield substantial improvements over conventional learning objectives in financial predictions when the full-order ranking quality is the primary goal.

---


### 116. [End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](https://arxiv.org/abs/2605.00503)

**<font color=#1a73e8>作者：</font>** Wenda Chu, Bingliang Zhang, Jiaqi Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive image modeling relies on visual tokenizers to compress images into compact latent representations. We design an end-to-end training pipeline that jointly optimizes reconstruction and generation, enabling direct supervision from generation results to the tokenizer. This contrasts with prior two-stage approaches that train tokenizers and generative models separately. We further investigate leveraging vision foundation models to improve 1D tokenizers for autoregressive modeling. Our autoregressive generative model achieves strong empirical results, including a state-of-the-art FID score of 1.48 without guidance on ImageNet 256x256 generation.

---


### 117. [Surprisal Minimisation over Goal-directed Alternatives Predicts Production Choice in Dialogue](https://arxiv.org/abs/2605.00506)

**<font color=#1a73e8>作者：</font>** Tom Utting, Mario Giulianelli, Arabella Sinclair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We model utterance production as probabilistic cost-sensitive choice over contextual alternatives, using information-theoretic notions of cost. We distinguish between goal-directed alternatives that realise a fixed communicative intent and goal-agnostic alternatives defined only by contextual plausibility, allowing us to derive speaker- and listener-oriented interpretations of different cost measures. We present a procedure to generate both types of alternative sets using language models. Analysing production choices in open-ended dialogue under both deterministic and probabilistic cost minimisation, we find that surprisal minimisation relative to goal-directed alternatives provides the strongest predictive account under both analyses. By contrast, uniform information density and length-based costs exhibit weaker and less consistent predictive power across conditions. More broadly, our study suggests that alternative-conditioned optimisation with LM-generated alternatives provides a principled framework for studying speaker and listener pressures in naturalistic language production.

---


### 118. [A Comparative Study of QSPR Methods on a Unique Multitask PAMPA dataset](https://arxiv.org/abs/2605.00508)

**<font color=#1a73e8>作者：</font>** Andrs Formanek, Anna Vincze, Richrd Bicsak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a unique, multitask dataset comprising 143 drug and drug candidate molecules, each evaluated on in vitro, parallel artificial-membrane permeability assays (PAMPA) using six different model membranes. Using this resource, we systematically assess the effectiveness of various molecular descriptors and regression models in predicting passive membrane permeability. The studied models range from simple linear regression to a modern pre-trained transformer architecture. Particular attention is given to the trade-off between predictive performance and model interpretability, highlighting the challenges introduced by machine learning approaches. To our knowledge, this is the most comprehensive study on simultaneous modeling of multiple organ-specific PAMPA membranes to date, offering novel insights into membrane-specific permeability profiles.
We found that expert-designed physico-chemical property descriptors are more fitting for a limited sample size permeabilty study than deep learning based representations.

---


### 119. [Scale-Aware Adversarial Analysis: A Diagnostic for Generative AI in Multiscale Complex Systems](https://arxiv.org/abs/2605.00510)

**<font color=#1a73e8>作者：</font>** Mengke Zhao, Guang-Xing Li, Duo Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex physical systems, from supersonic turbulence to the macroscopic structure of the universe, are governed by continuous multiscale dynamics. While modern machine learning architectures excel at mapping the high-dimensional observables of these systems, it remains unclear whether they internalize the governing physical laws or merely interpolate discrete statistical correlations. Standard Explainable AI (XAI) architectures, particularly perturbation-based and gradient-saliency methods, rely on pixel-wise perturbations, which generate unphysical artifacts and push inputs off the valid empirical distribution. To resolve this, we introduce a diagnostic framework driven by Constrained Diffusion Decomposition (CDD), a diffusion-based multiscale data decomposition algorithm that enables physically constrained data generation and model evaluation via scale-aware modifications. Applying this framework to a Denoising Diffusion Probabilistic Model (DDPM), we execute deterministic interventions directly within the continuous, CDD-based scale space. We demonstrate that under moderate physical perturbations, the unconstrained generative model exhibits localized structural freezing and non-linear instability rather than continuous PDE-like responses. The network fails to maintain cross-scale continuity, causing the generative trajectory to diverge when pushed into unseen physical states. By synthesizing a continuum of physically coherent states, this scale-informed methodology establishes a controlled test ground to evaluate algorithmic vulnerabilities, providing the rigorous physical constraints necessary for future architectures to respect the multiscale causality of the natural universe.

---


### 120. [ControBench: An Interaction-Aware Benchmark for Controversial Discourse Analysis on Social Networks](https://arxiv.org/abs/2605.00513)

**<font color=#1a73e8>作者：</font>** Ta Thanh Thuy, Jiaqi Zhu, Xuan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how people argue across ideological divides online is important for studying political polarization, misinformation, and content moderation. Existing datasets capture only part of this problem: some preserve text but ignore interaction structure, some model structure without rich semantics, and others represent conversations without stable user-level ideological identity. We introduce ControBench, a benchmark for controversial discourse analysis that combines heterogeneous social interaction graphs with rich textual semantics. Built from Reddit discussions on three topics, Trump, abortion, and religion, ControBench contains 7,370 users, 1,783 posts, and 26,525 interactions. The graph contains user and post nodes connected by semantically enriched edges; in particular, user-comment-user edges encode both a reply and the parent comment that it responds to, preserving local argumentative context. User labels are derived from self-declared Reddit flairs, providing a scalable proxy for ideological identity without manual annotation. The resulting datasets exhibit low or negative adjusted homophily (Trump: -0.77, Abortion: 0.06, Religion: 0.04), reflecting the cross-cutting structure of real-world debate. We evaluate graph neural networks, pretrained language models, and large language models on ControBench and observe distinct performance patterns across topics and model families, especially when ideological boundaries are ambiguous. These results position ControBench as a challenging and realistic benchmark for controversial discourse analysis.

---


### 121. [PhysiGen: Integrating Collision-Aware Physical Constraints for High-Fidelity Human-Human Interaction Generation](https://arxiv.org/abs/2605.00517)

**<font color=#1a73e8>作者：</font>** Nan Lei, Yuan-Ming Li, Ling-An Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite substantial progress in text-driven 3D human motion synthesis, generating realistic multi-person interaction sequences remains challenging. Notably, body inter-penetration is a pervasive issue from both data acquisition to the generated results, which significantly undermines the realism and usability. Previous generative models either ignored this issue or introduced computationally expensive mesh-level loss functions to alleviate inter-body collisions. In this paper, we propose a general-purpose and computationally efficient optimization strategy named PhysiGen to explicitly integrate collision-aware physical constraints for human-human interaction generation. Specifically, we simplify the high-resolution human body mesh into geometric primitives to greatly reduce the cost of inter-person collision detection. Moreover, we identify the collision regions as the guidance of the optimization directions. PhysiGen is plug-and-play and can be readily integrated into existing human interaction generation models. Extensive cross-dataset and cross-model experiments show that our method can effectively reduce interpenetration and significantly improve visual coherence and physical plausibility compared to the state-of-the-art methods.

---


### 122. [The impact of coercive, normative, and mimetic Stress on Chinese teachers' continuance intention to use generative AI: An integrated perspective of the Expectation-Confirmation Model and Institutional Theory](https://arxiv.org/abs/2605.00522)

**<font color=#1a73e8>作者：</font>** Kunjie Jia, Kai Cui, Huimin He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates Chinese teachers' continuance intention to use generative artificial intelligence (AI) by integrating the Expectation-Confirmation Model with Institutional Theory. A sequential explanatory mixed-methods design was employed. Questionnaire data from 437 teachers were analysed using structural equation modelling, followed by semi-structured interviews with 15 teachers to further interpret the findings. The results indicate that confirmation, perceived usefulness, and satisfaction play important roles in shaping teachers' continuance intention, while institutional pressures, including coercive, normative, and mimetic influences, also contribute to continued use. Qualitative findings further reveal that teachers often use generative AI pragmatically to support tasks such as lesson preparation and idea generation, while simultaneously exercising caution and critically evaluating the reliability of AI-generated content. These findings highlight the combined influence of individual evaluations and institutional contexts on teachers' sustained engagement with generative AI in education.

---


### 123. [IdentiFace: Multi-Modal Iterative Diffusion Framework for Identifiable Suspect Face Generation in Crime Investigations](https://arxiv.org/abs/2605.00526)

**<font color=#1a73e8>作者：</font>** Weichen Liu, Yixin Yang, Changsheng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Suspect face generation remains a technical challenge in crime investigations. Traditional sketch-drawing workflows suffer from low efficiency and quality, while diffusion-based approaches still face intrinsic limitations on conditional ambiguity for text-to-image models and sampling variance for one-shot generation. We proposed IdentiFace, a novel diffusion-based framework for identifiable suspect face generation, which addressed these issues through (1) multi-modal input design to strengthen conditional control, and (2) an iterative generation pipeline enabling identifiable feature adjustment. We additionally contributed a facial identity loss and two task-specific datasets. Comprehensive experiments on synthetic datasets and in real-world scenarios indicate that IdentiFace achieves superior performance over existing methods, especially in terms of identity retrieval, and shows strong potential for practical applications.

---


### 124. [Vesselpose: Vessel Graph Reconstruction from Learned Voxel-wise Direction Vectors in 3D Vascular Images](https://arxiv.org/abs/2605.00538)

**<font color=#1a73e8>作者：</font>** Rajalakshmi Palaniappan, Christoph Karg, Nemesio Navarro-Arambula 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blood vessel segmentation and -tracing are essential tasks in many medical imaging applications. Although numerous methods exist, the prevailing segment-then-fix paradigm is fundamentally limited regarding its suitability for modeling the task of complete and topologically accurate vascular network reconstruction. Here, we propose an approach to extract topologically more accurate vascular graphs from 3D image data, building upon highly successful ideas from the related biomedical tasks of cell segmentation and -tracking. Our approach first predicts voxel-wise vessel direction vectors joint with standard vessel segmentation masks. Second, to extract the vascular graph from these predictions, we introduce a direction-vector-guided extension of the TEASAR algorithm. Our approach achieves state-of-the-art performance on three benchmark datasets, spanning both synthetic and real imagery. We further demonstrate the applicability of our approach to challenging 3D micro-CT scans of rat heart vasculature. Finally, we propose meaningful and interpretable measures of topological error, namely false splits and false merges for graphs. Overall, our approach substantially improves the topological accuracy of reconstructed vascular graphs, being able to separate closely apposed vessel segments and handle multiple vascular trees within a single volume.

---


### 125. [Beyond Continuity: Simulation-free Reconstruction of Discrete Branching Dynamics from Single-cell Snapshots](https://arxiv.org/abs/2605.00545)

**<font color=#1a73e8>作者：</font>** Junda Ying, Yuxuan Wang, Bowen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring cellular trajectories from destructive snapshots is complicated by the challenges of stochasticity and non-conservative mass dynamics such as cell proliferation and apoptosis. Existing unbalanced Optimal Transport (OT) methods treat mass as a continuous fluid, performing inference at the population level. However, this macroscopic view often fails to capture the discrete, jump-like nature of birth-death events at single-cell resolution, which is essential for understanding lineage branching and fate decisions. We present Unbalanced Schrödinger Bridge (USB), a simulation-free framework for learning underlying dynamics that effectively integrates both stochastic and unbalanced effects which also models the discrete, jump-like birth-death dynamics at single-cell resolution. Theoretically, USB provides a tractable solution to the Branching Schrödinger Bridge (BSB) problem, offering a rigorous microscopic interpretation where individual cells undergo both Brownian motion and discrete birth-death jumps. Technically, the method implements an efficient solver by introducing a simulation-free training objective that effectively scales to high-dimensional omics data. Empirically, we demonstrate on both simulated and real-world datasets that USB not only achieves trajectory reconstruction performance better than or comparable to deterministic baselines but also uniquely enables realistic discrete simulation of birth-death dynamics at single-cell resolution.

---


### 126. [Colorful-Noise: Training-Free Low-Frequency Noise Manipulation for Color-Based Conditional Image Generation](https://arxiv.org/abs/2605.00548)

**<font color=#1a73e8>作者：</font>** Nadav Z. Cohen, Ofir Abramovich, Ariel Shamir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models generate images by gradually converting white Gaussian noise into a natural image. White Gaussian noise is well suited for producing diverse outputs from a single text prompt due to its absence of structure. However, this very property limits control over, and predictability of, specific visual attributes, as the noise is not human-interpretable. In this work, we investigate the characteristics of the input noise in diffusion models. We show that, although all frequencies in white Gaussian noise have comparable statistical energy, low-frequency components primarily determine the images global structure and color composition, while high-frequency components control finer details. Building on this observation, we demonstrate that simple manipulations of the low-frequency noise using low-frequency image priors can effectively condition the generation process to reconstruct these low-frequency visual cues. This allows us to define a simple, training-free method with minimal overhead that steers overall image structure and color, while letting high-frequency components freely emerge as fine details, enabling variability across generated outputs.

---


### 127. [A11y-Compressor: A Framework for Enhancing the Efficiency of GUI Agent Observations through Visual Context Reconstruction and Redundancy Reduction](https://arxiv.org/abs/2605.00551)

**<font color=#1a73e8>作者：</font>** Michito Takeshita, Takuro Kawada, Takumi Ohashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents that interact with graphical user interfaces (GUIs) require effective observation representations for reliable grounding. The accessibility tree is a commonly used text-based format that encodes UI element attributes, but it suffers from redundancy and lacks structural information such as spatial relationships among elements. We propose A11y-Compressor, a framework that transforms linearized accessibility trees into compact and structured representations. Our implementation, Compressed-a11y, applies a lightweight and structured transformation pipeline with modal detection, redundancy reduction, and semantic structuring. Experiments on the OSWorld benchmark show that Compressed-a11y reduces input tokens to 22% of the original while improving task success rates by 5.1 percentage points on average.

---


### 128. [Linking Behaviour and Perception to Evaluate Meaningful Human Control over Partially Automated Driving](https://arxiv.org/abs/2605.00556)

**<font color=#1a73e8>作者：</font>** Ashwin George, Lucas Elbert Suryana, Lorenzo Flipse 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Partial driving automation creates a tension: drivers remain legally responsible for vehicle behaviour, yet their active control is significantly reduced. This reduction undermines the engagement and sense of agency needed to intervene safely. Meaningful human control (MHC) has been proposed as a normative framework to address this tension. However, empirical methods for evaluating whether existing systems actually provide MHC remain underdeveloped. In this study, we investigated the extent to which drivers experience MHC when interacting with partially automated driving systems. Twenty-four drivers completed a simulator study involving silent automation failures under two modes - haptic shared control (HSC) and traded control (TC). We derived behavioural metrics from telemetry data, subjective perception scores from post-trial surveys and used them to test hypothesised relations between them derived from the properties of systems under MHC. The confirmatory analysis showed a significant negative correlation between the perception of the automated vehicle (AV) understanding the driver and conflict in steering torques. An exploratory analysis also revealed a surprising positive correlation between reaction times and the perception of sufficient control. Qualitative feedback from open-ended post-experiment questionnaires revealed that mismatches in intentions between the driver and automation, lack of safety, and resistance to driver inputs contribute to the reduction of perceived MHC, while subtle haptic guidance aligned with driver intent had a positive effect. These findings suggest that future designs should prioritise effortless driver interventions, transparent communication of automation intent, and context-sensitive authority allocation to strengthen meaningful human control in partially automated driving.

---


### 129. [Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output](https://arxiv.org/abs/2605.00557)

**<font color=#1a73e8>作者：</font>** James Mooney, Zae Myung Kim, Young-Jun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is an extended process of ideation--surveying prior work, forming hypotheses, and refining reasoning--yet existing approaches treat this phase as a brief preamble despite its central role in research. We introduce SCISENSE, a sensemaking-grounded framework that operationalizes ideation as a structured sequence of eight cognitive stages (Pirolli \& Card, 2005). We construct SCISENSE-Traj, a 100K-scale dataset of citation-conditioned research trajectories in two modes: Target, where an LLM reconstructs the ideation path leading to a known paper from its cited works, and Infer, where the LLM proposes novel directions from the same citations. We distill these into SCISENSE-LM, a family of sensemaking LLMs spanning 3B to 70B parameters. Contrary to the assumption that looser supervision promotes greater exploration, Target-trained models achieve a 2.0\% improvement in trajectory quality over Infer-trained models while also producing more novel and diverse outputs. This advantage propagates downstream: coding agents conditioned on Target trajectories produce research artifacts with higher executability and quality than those conditioned on Infer trajectories. This suggests that targeted ideation reduces cognitive burden on downstream agents, freeing them to explore more creatively. SCISENSE offers both a practical tool for augmenting LLM-driven research workflows and a principled testbed for studying how planning shapes scientific discovery.

---


### 130. [Pick and Sort for Graphical Authentication](https://arxiv.org/abs/2605.00558)

**<font color=#1a73e8>作者：</font>** Argianto Rahartomo, AmirHossein Jamshidipoor, Mohammad Ghafari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a graphical authentication scheme that follows a simple ``Pick and Sort'' design in which users choose visual elements and arrange them within a grid. Both the number of selected elements and the grid size are configurable, and the visual elements can be customized for specific user groups, such as children. A preliminary study with a prototype implementation indicated that the scheme is easy to learn and flexible to deploy. Although login times are longer than those of conventional authentication methods, the additional interaction may be acceptable in scenarios that are not time-critical, such as infrequent-access use cases or as a secondary authentication mechanism.

---


### 131. [Depth-Guided Privacy-Preserving Visual Localization Using 3D Sphere Clouds](https://arxiv.org/abs/2605.00562)

**<font color=#1a73e8>作者：</font>** Heejoon Moon, Jongwoo Lee, Jeonggon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The emergence of deep neural networks capable of revealing high-fidelity scene details from sparse 3D point clouds has raised significant privacy concerns in visual localization involving private maps. Lifting map points to randomly oriented 3D lines is a well-known approach for obstructing undesired recovery of the scene images, but these lines are vulnerable to a density-based attack that can recover the point cloud geometry by observing the neighborhood statistics of lines. With the aim of nullifying this attack, we present a new privacy-preserving scene representation called \emph{sphere cloud}, which is constructed by lifting all points to 3D lines crossing the centroid of the map, resembling points on the unit sphere. Since lines are most dense at the map centroid, the sphere cloud mislead the density-based attack algorithm to incorrectly yield points at the centroid, effectively neutralizing the attack. Nevertheless, this advantage comes at the cost of i) a new type of attack that may directly recover images from this cloud representation and ii) unresolved translation scale for camera pose estimation. To address these issues, we introduce a simple yet effective cloud construction strategy to thwart new attack and propose an efficient localization framework to guide the translation scale by utilizing absolute depth maps acquired from on-device time-of-flight (ToF) sensors. Experimental results on public RGB-D datasets demonstrate sphere cloud achieves competitive privacy-preserving ability and localization runtime while not excessively compensating the pose estimation accuracy compared to other depth-guided localization methods.

---


### 132. [2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569)

**<font color=#1a73e8>作者：</font>** Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for generating photorealistic renderings of a scene in real-time. However, the volumetric nature of 3DGS limits its ability to accurately capture surface geometry. To address this, 2D Gaussian Splatting (2DGS) was proposed to enable view-consistent and geometrically accurate surface reconstruction from multi-view images. However, 2DGS can be sensitive to the initialization of the Gaussian primitives. Reliance on Structure-from-Motion (SfM) initializations, which can produce poor estimates on challenging image sets, may lead to subpar results. In this work, we enhance 2DGS by incorporating monocular depth and normal priors to improve both geometric accuracy and robustness. We propose a depth-guided initialization strategy for Gaussians and introduce a clustering-based technique for pruning degenerate Gaussians. We evaluate our method on the DTU dataset, where it achieves state-of-the-art results in mesh reconstruction while preserving high-quality novel view synthesis.

---


### 133. [Instance-Aware Parameter Configuration in Bilevel Late Acceptance Hill Climbing for the Electric Capacitated Vehicle Routing Problem](https://arxiv.org/abs/2605.00572)

**<font color=#1a73e8>作者：</font>** Yinghao Qin, Xinwei Wang, Mosab Bazargani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithm performance in combinatorial optimization is highly sensitive to parameter settings, while a single globally tuned configuration often fails to exploit the heterogeneity of instances. This limitation is particularly evident in the Electric Capacitated Vehicle Routing Problem, where instances differ in structure, demand patterns, and energy constraints. This paper investigates instance-aware parameter configuration for Bilevel Late Acceptance Hill Climbing, a state-of-the-art metaheuristic for the Electric Capacitated Vehicle Routing Problem. An offline tuning procedure is used to obtain instance-specific parameter labels, which are then mapped from instance features via a regression model to enable parameter prediction for unseen instances prior to execution. Experimental results on the IEEE WCCI 2020 benchmark and its extensions show that the proposed approach achieves an average objective value reduction of $0.28\%$ across eight held-out test instances relative to a globally tuned configuration. This corresponds to a significant cost reduction in multimillion-dollar transportation operations.

---


### 134. [DySRec: Dynamic Context-Aware Psychometric Scale Recommendation via Multi-Agent Collaboration](https://arxiv.org/abs/2605.00574)

**<font color=#1a73e8>作者：</font>** Yanzeng Li, Xiaoning Cao, Jialun Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Choosing suitable psychometric scales is an essential and difficult step in psychological consultation, which requires clinicians to integrate patient information, behaviors, and dynamic contextual information. Existing systems mainly use static pipelines to choose scale, or directly predict symptoms according to user inputs, limiting their ability to support dynamic assessment, risk management, and transparent decision-making. To address these limitations, we propose DySRec, a multi-agent conversational system for dynamic psychometric scale recommendation. DySRec operates as an interactive chatbot that engages users in multi-turn dialogue, models scale selection as a continuous conversational decision process, and coordinates specialized agents to maintain user context, recommend assessment scales, monitor psychological risk, and log decision trajectories. In this way, DySRec can integrate and capture heterogeneous signals, including semantic, interaction behaviors, assessment history, and content state, to dynamically update user representations and calculate scale-context compatibility score for recommending most matched scales. Moreover, DySRec incorporates a closed-loop refinement mechanism. Recommendation agent will feedback the missing or uncertain attributes and guide the conversation to elicit the targeted information. In this paper, we showcase the prototype design and architecture of DySRec, and this system has been verified in a real-world application.

---


### 135. [Federated Distillation for Whole Slide Image via Gaussian-Mixture Feature Alignment and Curriculum Integration](https://arxiv.org/abs/2605.00578)

**<font color=#1a73e8>作者：</font>** Luru Jing, Cong Cong, Yanyuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) offers a promising framework for collaborative digital pathology by enabling model training across institutions. However, real-world deployments face heterogeneity arising from diverse multiple instance learning (MIL) architectures and heterogeneous feature extractors across institutions. We propose FedHD, a novel FL framework that performs local Gaussian-mixture feature alignment tailored for WSI analysis. Instead of exchanging model parameters, each client independently distills semantically rich synthetic feature representations aligned with the distribution of real WSIs. To preserve diagnostic diversity, FedHD adopts a one-to-one distillation strategy, generating a synthetic counterpart for each real slide to avoid over-compression. During federation, a curriculum-based integration strategy progressively incorporates cross-site synthetic features into local training once performance plateaus. Furthermore, an optional interpretation module reconstructs pseudo-patches from synthetic embeddings, enhancing transparency. FedHD is architecture-agnostic, privacy-preserving, and supports personalized yet collaborative training across diverse institutions. Experiments on TCGA-IDH, CAMELYON16, and CAMELYON17 show that FedHD consistently outperforms state-of-the-art federated and distillation baselines.

---


### 136. [AI Washing Inflates Expected Performance but Not Interaction Outcomes: An AI Placebo Study Using Fitts' Law](https://arxiv.org/abs/2605.00582)

**<font color=#1a73e8>作者：</font>** Nick von Felten, Luisa Ella Müller, Johannes Schöning  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Expectations about the support of artificial intelligence (AI) may influence interaction outcomes similar to placebos. Such expectations may result from AI washing, a practice of overstating a system's AI capabilities when actual functionality is limited. For example, some computer mice are marketed as "AI-assisted" despite lacking AI in core functions. In a within-subjects study, 28 participants completed Fitts' Law tasks with a computer mouse under three conditions: no support, supposed predictive AI support, and supposed biosignal-enhanced AI support. Objective Fitts' Law performance indicators and subjective performance expectations, perceived workload, and perceived usability were measured. Compared to baseline, participants expected significantly improved performance in placebo conditions. However, these expectations did not translate into differences in objective or subjective assessments. This paper contributes evidence that AI washing inflates user expectations without altering actual interaction outcomes, highlighting a critical transparency issue. By exposing how deceptive AI marketing can shape user expectations, we underscore the need for accountability in AI product claims. Further, we establish Fitts' Law as a rigorous methodological lens for auditing AI-labelled input devices.

---


### 137. [Fairness of Classifiers in the Presence of Constraints between Features](https://arxiv.org/abs/2605.00592)

**<font color=#1a73e8>作者：</font>** Martin C. Cooper, Imane Bousdira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Machine Learning, an accepted definition of fairness of a decision taken by a classifier is that it should not depend on protected features, such as gender. Unfortunately, when constraints exist between features, such dependencies can be obscured by the constraints.
To avoid this problem, we propose that a decision be considered fair if it has a fair explanation. We define a fair explanation as a prime-implicant reason for the decision that does not contain any protected feature (where the constraints are taken into account in the definition of prime-implicant). Surprisingly, ignoring constraints can completely change the fairness of a decision (according to this definition) even in the absence of constraints between protected and unprotected features.
Three possible definitions of fairness of a classifier are that for all its decisions (1) there are only fair explanations, (2) there is at least one fair explanation, or (3) changing protected features does not change the outcome. We identify the relationships between these different definitions of fairness and study the computational complexity of testing fairness of classifiers.

---


### 138. [Robust Fusion of Object-Level V2X for Learned 3D Object Detection](https://arxiv.org/abs/2605.00595)

**<font color=#1a73e8>作者：</font>** Lukas Ostendorf, Lennart Reiher, Onn Haran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception for automated driving is largely based on onboard environmental sensors, such as cameras and radar, which are cost-effective but limited by line-of-sight and field-of-view constraints. These inherent limitations may cause onboard perception to fail under occlusions or poor visibility conditions. In parallel, cooperative awareness via vehicle-to-everything (V2X) communication is becoming increasingly available, enabling vehicles and infrastructure to share their own state as object-level information that complements onboard perception. In this work, we study how such V2X information can be integrated into 3D object detection and how robust the resulting system is to realistic V2X imperfections. Using the nuScenes dataset, we emulate object-level cooperative awareness messages from ground truth, injecting controlled noise and object dropout to mimic real-world conditions such as latency, localization errors, and low V2X penetration rates. We convert these messages into a dedicated bird's-eye view (BEV) input and fuse them into a BEVFusion-style detector. Our results demonstrate that while object-level cooperative information can substantially improve detection performance, achieving an NDS of 0.80 under favorable conditions, models trained on idealized data become fragile and over-reliant on V2X. Conversely, our proposed noise-aware training strategy, coupled with explicit confidence encoding, enhances robustness, maintaining performance gains even under severe noise and reduced V2X penetration.

---


### 139. [Possibilistic Predictive Uncertainty for Deep Learning](https://arxiv.org/abs/2605.00600)

**<font color=#1a73e8>作者：</font>** Yao Ni, Jeremie Houssineau, Yew Soon Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve impressive results across diverse applications, yet their overconfidence on unseen inputs necessitates reliable epistemic uncertainty modelling. Existing methods for uncertainty modelling face a fundamental dilemma: Bayesian approaches provide principled estimates but remain computationally prohibitive, while efficient second-order predictors lack rigorous derivations connecting their specific objectives to epistemic uncertainty quantification. To resolve this dilemma, we introduce Dirichlet-approximated possibilistic posterior predictions (DAPPr), a principled framework leveraging possibility theory. We define a possibilistic posterior over parameters, projects this posterior to the prediction space via supremum operators, and approximates the projected posterior using learnable Dirichlet possibility functions. This projection-and-approximation strategy yields a simple training objective with closed-form solutions. Extensive experiments across diverse benchmarks demonstrate that our approach achieves competitive or superior uncertainty quantification performance compared to state-of-the-art evidential deep learning methods while maintaining both principled derivation and computational efficiency. Code will be available at this https URL.

---


### 140. [Affinity Is Not Enough: Recovering the Free Energy Principle in Mixture-of-Experts](https://arxiv.org/abs/2605.00604)

**<font color=#1a73e8>作者：</font>** Man Yung Wong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse MoE routing fails at domain transitions, where the current token belongs to one distribution and the next to another. In a controlled experiment (4 experts, 5 seeds), standard affinity routing assigns only 0.006 +/- 0.001 probability to the correct expert at the transition. Three lightweight gate modifications raise this to 0.748 +/- 0.002 (124x), cutting experts needed for 99% coverage from infeasible to a small constant: temporal memory (beta), a per-expert LIF membrane potential accumulating routing context across tokens; precision-weighted gating (Pi), a per-expert inverse variance of recent prediction error, yielding 31x contrast between reliable and unreliable experts; and anticipatory routing, a next-state predictor conditioned on the beta-accumulated hidden state. The mechanisms draw from Friston's Free Energy Principle and use LIF dynamics from spiking neural networks. An ablation across all 2^3 subsets reveals a super-additive beta x Ant interaction: anticipation alone gives nothing (+0.000 +/- 0.001); beta alone gives modest gain (+0.295 +/- 0.013); combined they close 75% of the oracle gap (+0.741 +/- 0.002, exceeding the sum by +0.446 +/- 0.014). This is structural: a stateless predictor cannot detect approaching transitions because pre-transition tokens are distributionally identical to within-domain tokens. In a character-level MoE LM (5 seeds), beta-routing reduces transition-step BPC from 6.56 +/- 0.01 (Standard) to 4.01 +/- 0.15 (beta-MoE); the beta + Ant gate places 0.86 +/- 0.02 probability on the correct domain expert before that domain appears in input, vs 0.42 +/- 0.12 for Standard MoE. Reference implementations (~200 lines each): this https URL

---


### 141. [Faithful Extreme Image Rescaling with Learnable Reversible Transformation and Semantic Priors](https://arxiv.org/abs/2605.00605)

**<font color=#1a73e8>作者：</font>** Hao Wei, Yanhui Zhou, Chenyang Ge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most recent extreme rescaling methods struggle to preserve semantically consistent structures and produce realistic details, due to the severely ill-posed nature of low- to high-resolution mapping under scaling factors of $16\times$ or higher. To alleviate the above problems, we propose FaithEIR, a diffusion-based framework for extreme image rescaling. Inspired by singular value decomposition, we develop learnable reversible transformation that enables invertible downscaling and upscaling in the latent space. To compensate for information loss due to quantization, we propose an adaptive detail prior, a high-frequency dictionary that captures the empirical average of commonly occurring structures in the training data. Finally, we design a lightweight pixel semantic embedder to provide semantic conditioning for the pretrained diffusion model. We present extensive experimental results demonstrating that our FaithEIR consistently outperforms state-of-the-art methods, achieving superior reconstruction fidelity and perceptual quality. Our code, model weights, and detailed results are released at this https URL.

---


### 142. [KingsGuard: Enclave Data Protection Under Real-World TEE Vulnerabilities](https://arxiv.org/abs/2605.00613)

**<font color=#1a73e8>作者：</font>** Saltanat Firdous Allaqband, Deepanjali S, Rohit Srinivas R G 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) have emerged as a cornerstone for securing sensitive computations by providing isolated enclaves protected from untrusted software. However, their security guarantees are undermined by vulnerabilities in both the enclave code and the underlying hardware design, which can allow sensitive data to leak despite strong isolation guarantees. This paper presents KINGSGUARD, a novel TEE design that systematically monitors and controls the propagation of sensitive data within an enclave. By enforcing fine-grained data flow tracking and checks in hardware, our approach ensures that sensitive data does not leave the enclave boundary, thus bridging the gap between the idealized threat models of TEEs and their practical realizations. Additionally, to balance security with practical functionality, we introduce controlled declassification at enclave boundaries, allowing intentional release of data to the outside world. Our implementation of KINGSGUARD on a RISC-V processor has a 10.8% hardware area overhead when synthesized on FPGA and a 5.69% performance overhead.

---


### 143. [Is Textual Similarity Invariant under Machine Translation? Evidence Based on the Political Manifesto Corpus](https://arxiv.org/abs/2605.00618)

**<font color=#1a73e8>作者：</font>** Daria Boratyn, Damian Brzyski, Albert Leśniak 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the extent to which cosine similarity between paragraph embeddings is invariant under machine translation, using the Manifesto Corpus of over 2,800 political party platforms in 28 languages translated to English via the EU eTranslation service. Rather than measuring translation-induced semantic shift directly we measure the stability of pairwise similarity relationships across embedding models, and use inter-model disagreement on original-language text as a calibrated invariance threshold. This yields a per-language non-inferiority test for four hypotheses about how translation interacts with embedding choice, with verdicts that distinguish languages where translation demonstrably preserves semantic structure from those where it demonstrably degrades it and from those where the available evidence does not resolve the question. The framework is corpus- and pipeline-agnostic and extends naturally to downstream tasks. Applied to our data, it identifies ten languages with translation invariance and four with detectable distortion.

---


### 144. [Defense against Poisoning Attacks under Shuffle-DP](https://arxiv.org/abs/2605.00625)

**<font color=#1a73e8>作者：</font>** Siyi Wang, Qiyao Luo, Yihua Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential Privacy (DP) has become the gold standard for protecting individual privacy in data analytics, and the shuffle-DP model has attracted significant attention from both academia and industry due to its favorable balance between privacy and utility. However, existing shuffle-DP protocols rely on a strong assumption: all users behave honestly. In real-world scenarios, adversarial users can exploit this vulnerability through poisoning attacks, compromising both privacy guarantees and the utility of analytical results. While defending against poisoning attacks in the shuffle-DP model has recently gained interest, existing solutions are limited to frequency estimation tasks. To address this issue, we propose the first general defense framework for all union-preserving queries, capable of transforming any shuffle-DP protocol into a version resilient to poisoning attacks. Beyond robust defense against poisoning attacks, our framework achieves high utility of analytical results. Compared to the original shuffle-DP protocol, it retains asymptotically equivalent error in attack-free settings and incurs only a polylogarithmic increase in error when a constant number of attackers are present. We demonstrate the generality of our framework on several common queries, including summation, frequency estimation, and range counting. Experimental results confirm that our approach effectively defends against poisoning attacks while maintaining strong utility and communication efficiency.

---


### 145. [Class Angular Distortion Index for Dimensionality Reduction](https://arxiv.org/abs/2605.00637)

**<font color=#1a73e8>作者：</font>** Kaviru Gunaratne, Stephen Kobourov, Jacob Miller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction (DR) techniques are often characterized by whether they preserve global, high-level structures in the data or local, neighborhood structures. This distinction matters in visualization: global methods can obscure clusters while local methods can over-emphasize them. Yet, even when clusters appear distinct, their relative arrangement in the projection may be arbitrary or misleading, a common issue in techniques such as t-SNE and UMAP. Existing cluster quality metrics either only measure cluster separability or assume spherical, globular clusters in the original space. We introduce the Class Angular Distortion Index (CADI), a metric that uses internal angles among point triples to determine the faithfulness of cluster organization in a projection. We show cases on both real and synthetic data where existing cluster metrics fail, but CADI provides an interpretable result. Since it relies on computing angles, CADI is also differentiable, enabling optimization. We demonstrate this with a CADI-based DR technique.

---


### 146. [Unlearning Offline Stochastic Multi-Armed Bandits](https://arxiv.org/abs/2605.00638)

**<font color=#1a73e8>作者：</font>** Zichun Ye, Runqi Wang, Xuchuang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to unlearn data points from a learned model, offering a principled way to process data-deletion requests and mitigate privacy risks without full retraining. Prior work has mainly studied unsupervised / supervised machine unlearning, leaving unlearning for sequential decision-making systems far less understood. We initiate the first study of a foundational sequential decision-making problem: offline stochastic multi-armed bandits (MAB). We formalize the privacy constraint for offline MAB and measure utility by the post-unlearning decision quality. We conduct a systematic study of both single- and multi-source unlearning scenarios under two data-generation models, the fixed-sample model and the distribution model. For these settings, our algorithmic design is built on two canonical base algorithms: Gaussian mechanism and rollback, and we propose adaptive algorithms that switch between them according to the data regime and privacy constraint. We further introduce a mixing procedure that elucidates the rationale behind these baselines. We provide performance guarantees across the above settings and establish lower bounds under both dataset models. Experiments validate the predicted tradeoffs and demonstrate the effectiveness of the proposed methods.

---


### 147. [Knowing when to trust machine-learned interatomic potentials](https://arxiv.org/abs/2605.00640)

**<font color=#1a73e8>作者：</font>** Shams Mehdi, Ilkwon Cho, Olexandr Isayev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prevailing machine-learned interatomic potential (MLIP) uncertainty-quantification methods rely on ensembles of independently trained backbones. These methods scale unfavorably with foundation-scale MLIPs, and their member-disagreement signals correlate weakly with per-molecule prediction error. Here we probe the frozen per-atom representations of a pretrained MLIP with a compact discriminative classifier, recasting MLIP uncertainty quantification as selective classification rather than error regression. The resulting method, PROBE (Post-hoc Reliability frOm Backbone Embeddings), produces a per-prediction reliability probability that monotonically tracks actual error without modification to the underlying model. Across large held-out evaluation sets and two structurally distinct MLIP architectures, PROBE outperforms ensemble disagreement as a binary reliability signal, which strengthens with the expressiveness of the backbone representation, implying a favorable scaling trajectory toward foundation-scale MLIPs. Multi-head self-attention additionally yields per-atom importance maps, providing chemically interpretable diagnostics at no additional computational cost. PROBE is post-hoc and architecture-agnostic, and is directly deployable on any MLIP that exposes per-atom representations.

---


### 148. [Bridging Graph Drawing and Dimensionality Reduction with Stochastic Stress Optimization](https://arxiv.org/abs/2605.00641)

**<font color=#1a73e8>作者：</font>** Daniel Hangan, Stephen Kobourov, Jacob Miller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Both Dimensionality Reduction (DR) and Graph Drawing (GD) aim to visualize abstract, non-linear structures, yet rely on different optimization paradigms. This contrast is evident in Multidimensional Scaling (MDS), which typically depends on the SMACOF algorithm despite graph drawing results showing that simpler stochastic optimization schemes can be more effective for the same objective. We bridge these domains by adapting Stochastic Gradient Descent (SGD) techniques from graph drawing to vector data embedding. We present a scikit-learn compatible estimator that minimizes global stress through local pairwise updates, improving upon the existing implementation. Experiments on standard high-dimensional benchmarks show that our stochastic solver converges substantially faster than SMACOF while achieving comparable or lower stress.

---


### 149. [Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Daiqing Wu, Huawen Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) grounding maps natural language instructions to the visual coordinates of target elements and serves as a core capability for autonomous GUI agents. Recent reinforcement learning methods (e.g., GRPO) have achieved strong performance, but they rely on expensive multiple rollouts and suffer from sparse signals on hard samples. These limitations make on-policy self-distillation (OPSD), which provides dense token-level supervision from a single rollout, a promising alternative. However, its applicability to GUI grounding remains unexplored. In this paper, we present GUI-SD, the first OPSD framework tailored for GUI grounding. First, it constructs a visually enriched privileged context for the teacher using a target bounding box and a Gaussian soft mask, providing informative guidance without leaking exact coordinates. Second, it employs entropy-guided distillation, which adaptively weights tokens based on digit significance and teacher confidence, concentrating optimization on the most impactful and reliable positions. Extensive experiments on six representative GUI grounding benchmarks show that GUI-SD consistently outperforms GRPO-based methods and naive OPSD in both accuracy and training efficiency. Code and training data are available at this https URL.

---


### 150. [From Prediction to Practice: A Task-Aware Evaluation Framework for Blood Glucose Forecasting](https://arxiv.org/abs/2605.00645)

**<font color=#1a73e8>作者：</font>** Alireza Namazi, Heman Shakeri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical time-series forecasting is increasingly studied for decision support, yet standard aggregate metrics can obscure whether a model is actually useful for the task it is meant to serve. In safety-critical settings, low average error can coexist with dangerous failures in exactly the high-risk regimes that matter most. We present a task-aware evaluation framework for blood glucose forecasting built around two downstream uses: hypoglycemia early warning and insulin dosing decision support. For early warning, we evaluate on real data from three clinical cohorts using event-level recall and false alarms per patient-day, metrics that reflect operational alarm burden rather than aggregate accuracy. We show that models appearing acceptable overall, with recall above 0.9 on the full test set, can fail badly in the post-bolus slice, where insulin-on-board is elevated and missed warnings carry the greatest clinical consequences. Standard forecasting evaluation, however, does not test whether a model can reason about the effects of actions, a requirement for supporting insulin dosing decisions. We therefore add a second, interventional arm using the FDA-accepted UVA/Padova simulator, where we evaluate whether forecasters can predict glucose responses to altered insulin plans in paired factual/counterfactual scenarios. We show that models that look strong on real-data forecasting often fail to predict the direction, magnitude, or ranking of intervention effects, and choose poor insulin doses when evaluated under a clinically motivated cost. Taken together, the two arms reveal a consistent gap between forecasting accuracy and task-relevant usefulness. We release the benchmark, the standardized preprocessing pipeline for public cohorts, and the simulator-based interventional dataset as a reproducible toolkit.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-180](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
