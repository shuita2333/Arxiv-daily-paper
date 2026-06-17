# 📦 其他研究 | 2026年06月18日

> 本类共 **205** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-205](./part-05.md)

---

### 1. [Security and Human-Centered Assessment of BACnet-Controlled DALI Infrastructure in an Educational Building Automation Testbed](https://arxiv.org/abs/2606.17089)

**<font color=#1a73e8>作者：</font>** Ariton Verush  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Building automation and control systems integrate heating, ventilation, air conditioning, lighting, sensing, and management functions through specialized communication protocols. While this integration enables flexible building operation, it also creates complex cyber-physical environments that are difficult to inspect, secure, and explain to new analysts. This paper presents a practical security and human-centered case study of a BACnet/IP building automation testbed with DALI lighting infrastructure, investigated during a domotics-oriented cybersecurity hackathon in Thun, Switzerland in April 2026. The study combines network-oriented enumeration, object-level inspection, physical rack analysis, and reflective HCI analysis of tool-supported learning. Using Yabe and BACteria, the work documents observable BACnet services, reconstructs structured object hierarchies, identifies room-level lighting-control paths, and maps BACnet objects to DALI group-level infrastructure. The analysis emphasizes that BACS assessment is not only a technical protocol task: it also requires usable tool interfaces, physical observability, interpretable naming conventions, and safe mental models for command priorities. The paper contributes a compact case study of BACnet/DALI exploration in an educational testbed and discusses implications for cybersecurity education, human-centered security tooling, and responsible experimentation in cyber-physical building environments.

---


### 2. [Securing Multi-Agent GIS Systems: Risk Evaluation and Prompt Hardening Optimization](https://arxiv.org/abs/2606.17092)

**<font color=#1a73e8>作者：</font>** Kyle Gao, Pranavi Kotta, Linlin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems are increasingly integrated with geographic information systems (GIS), where multi-agent coordination enables complex conversational and spatial analysis but introduces security risks. This work presents a security-oriented framework for risk identification, evaluation, and mitigation in a multi-agent GIS system while maintaining adaptability to broader agentic architectures. We test the agentic system of a commercial geospatial partner while developing a modular state-machine-based orchestration framework that abstracts agent behavior into reusable components. We evaluate robustness using a red-teaming framework with an adaptive attacker LLM and a deterministic judge that produces binary outcomes with supporting rationales across multi-turn attacks. We further improve resilience with a prompt optimization framework that treats prompts as structured signatures and injects adversarial demonstrations, enabling systematic security improvements without degrading task performance.

---


### 3. [Diagnosing and Repairing Shape-Prior Shortcuts in Long-Range Single-Shot Fringe Projection Profilometry](https://arxiv.org/abs/2606.17093)

**<font color=#1a73e8>作者：</font>** Adam Haroon, Anush Lakshman, Cody Fleming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based single-shot fringe projection profilometry (FPP) has been studied mostly at close range. The long-range regime (standoff beyond 1 m) remains largely unaddressed: inverse-square intensity falloff lowers fringe signal-to-noise ratio and degrades physical ground truth, the single-shot problem is ill-posed because fringe-order information is absent from one image, and these architectures have not been studied mechanistically. We present a diagnose-repair-verify study using mechanistic interpretability (MI) and conformal uncertainty quantification (UQ) as convergent diagnostics: they agree on one physical failure locus, driving and verifying an architectural repair. On a photorealistic synthetic benchmark (15,600 fringe images, 50 objects at 1.5-2.1 m), a best UNet baseline reaches 14.54 mm object mean absolute error (MAE). Three probes (linear probing, Grad-CAM, flat-plane out-of-distribution test) converge: the baseline solves the task via object-boundary shape priors rather than fringe-phase decoding. We repair this with PhiCalNet, which outputs wrapped phase rather than depth and applies a fixed differentiable calibration layer mapping phase to depth, removing the shape-prior solution from the hypothesis space architecturally rather than by a loss penalty. A physics-informed loss that enforces the same physics as a soft penalty on a depth-regressing network yields no measurable gain, isolating the architecture as the operative factor. PhiCalNet reduces object MAE 3.3x to 4.46 mm; the residual is carried by 0.103% of pixels at the +/-pi wrap discontinuity. Pixel-wise conformal UQ confirms the diagnosis: rejecting the top 5% of object pixels by snapshot disagreement cuts PhiCalNet RMSE by 64% (20.6->7.4 mm) versus 3.5% for the baseline. MI and UQ converge on the same failure locus.

---


### 4. [The Bias Paradox: How AI Personas Can Overcome Human Limitations in UX Research](https://arxiv.org/abs/2606.17101)

**<font color=#1a73e8>作者：</font>** Ozgur Taylan Celik  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This position paper examines a paradox encountered in UX research practice: a situation where real human participants delivered less authentic insights than AI personas might have, due to context-induced biases. We share our experience developing research-based AI personas using OpenAI's custom GPT builder and conducting a design thinking workshop with high-net-worth banking clients. The workshop setting, including a luxury hotel, present portfolio managers, and hospitality dynamics, introduced biases that compromised the feedback. We propose that AI personas offer an underexplored opportunity to mitigate certain human limitations in user research, and call for frameworks that help teams recognize when traditional research contexts introduce biases that AI personas might help avoid.

---


### 5. [Informative Missingness to Generate Irregular Clinical Time Series](https://arxiv.org/abs/2606.17106)

**<font color=#1a73e8>作者：</font>** Hadi Mehdizavareh, Gabriele Santangelo, Giovanna Nicora 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Laboratory tests in electronic health records are collected irregularly, and the absence of a test order can be as informative as the measurement itself. Such missingness reflects clinicians' decisions and patient physiology, making it important to model it directly rather than treat it as a preprocessing artifact. Here we present a diffusion-based approach for generating clinical time series that jointly models laboratory values and their observation patterns using the public Data Analytics Challenge on Missing Data Imputation (DACMI) benchmark derived from MIMIC-III. To preserve realistic sampling, we align chart times into 4-hour intervals and segment admissions into 7-day windows, producing trajectories that pair each lab value with a corresponding observation indicator. Standard transformations and normalization are applied to stabilize training. Our method extends the TimeDiff framework to learn continuous lab values and discrete missingness patterns through complementary diffusion objectives. Experiments show that the generated data closely match real patient trajectories across individual lab distributions and joint value-missingness embeddings, demonstrating that diffusion models can capture clinically meaningful dependencies between patient physiology and clinicians' testing behavior under MNAR-like (missing-not-at-random) missingness. These preliminary results indicate that our model can serve as an initial component toward developing clinical foundation models. By producing synthetic priors that preserve key physiology-missingness relationships, this work motivates the subsequent training of Prior-Data Fitted Networks capable of leveraging informative missingness, which we will investigate in the extended work.

---


### 6. [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/abs/2606.17107)

**<font color=#1a73e8>作者：</font>** Bojie Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefix caching reuses prefill only across an exactly shared prefix, so one changed field invalidates the entire downstream cache. Yet overwriting the field's own key/value vectors and reusing the rest leaves the model acting on the old value. The reason, established causally across four model families: at prefill the model has already written the field-conditioned conclusion onto downstream notes; the field's own key/value drives under 1% of the decision. Read as a notebook of memoized conclusions, two capabilities follow. (1) It is editable. A salient erratum amends the notes; and with chain-of-thought, editing the field alone recovers the decision (1.00 at 8B, ~1% compute), while without CoT it is ignored. (2) It is composable. The notes are position-portable, so a precompiled skill can be RoPE-repositioned and spliced into any context, indistinguishable from full recompute (logit cosine 0.90-0.999, twelve models) at O(L) rather than O(L^2) time-to-first-token. A unified edit+compose agent stays decision-identical to recompute at up to 14.9x lower latency. The approach applies to any per-token attention KV cache, validated across scale, quantization, Mixture-of-Experts, and multimodal caches, and extends to several attention variants through small adapters. Because the erratum is append-only, it composes with production prefix caching: in an online vLLM benchmark it keeps the prefix cache-aligned (98.5% hit-rate), cutting p90 time-to-first-token by 53-398x.

---


### 7. [Timestamp-Aware Spatio-Temporal Graph Contrastive Learning for Network Intrusion Detection](https://arxiv.org/abs/2606.17109)

**<font color=#1a73e8>作者：</font>** Jianli Dai, Guangwei Wu, Jiacheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Given their effectiveness in modeling the relational structure among network traffic flows, graph neural networks (GNNs) have been widely adopted in network intrusion detection systems (NIDSs). However, most existing GNN-based NIDS approaches focus on the relational structure of traffic flows, and treat them as temporally independent, which limits their ability to cope with evolving attack behaviors. Moreover, their reliance on supervised or semi-supervised learning often restricts generalization to unseen attacks. To address these limitations, we propose a novel self-supervised GNN-based framework. To the best of our knowledge, the proposed model is among the first self-supervised GNN-based NIDS models to explicitly leverage real timestamps, which provides faithful temporal dependencies for representation learning. We first construct a series of temporal graphs from network traffic flows according to their timestamps, and then employ an E-GraphSAGE and LSTM based encoder to fully extract temporal information and spatial dependencies of network traffic, without introducing time-costly attention mechanisms. A multi-view graph contrastive learning (GCL) scheme is introduced, where temporal, spatial, and feature contrasts are jointly performed to capture temporal continuity, preserve structural consistency, and improve the generalization and robustness of the learned representations, respectively. In addition, a gradient-norm-based adaptive weighting strategy is designed to optimize the contrastive loss weights. Experimental results on four representative NIDS datasets with real timestamps demonstrate that our method significantly outperforms existing self-supervised approaches and achieves performance comparable to the supervised state-of-the-art GNN method, while maintaining high computational efficiency.

---


### 8. [Fractional Verkle Trees: A Hypertree Decomposition and Verified Proof Serialization Architecture for High-Performance Blockchain State Accumulators](https://arxiv.org/abs/2606.17111)

**<font color=#1a73e8>作者：</font>** Ekleen Kaur, Everton Fraga  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern blockchain state management faces a critical scalability bottleneck: maintaining cryptographic commitments over hundreds of millions of entries becomes computationally prohibitive. Ethereum's transition to Verkle Trees: polynomial commitment accumulators reducing proof sizes from O(width * depth) to O(depth) via constant-size IPA vector commitments, is a critical step toward stateless operation. Yet, current implementations exhibit pathological characteristics that burden home validators.
We identify four inefficiencies in the reference go-verkle implementation \cite{kaur2025goverkle, kaur2025goethereum}: (1) phantom node creation during non-existent account deletion; (2) 64-byte database keys triggering excessive LSM-tree compaction; (3) redundant memory copying in proof deserialization; (4) a Proof of Absence wire format incompatibility causing non-deterministic serialization.
We present Fractional Verkle Trees (FVT), a hypertree decomposition partitioning global state into N independent sub-accumulators coordinated by a Merkle commitment tree, achieving improved cache locality, zero-lock-contention goroutine-parallel commitment computation, and faster root recomputation (91 $\mu$s vs $\sim$500 ms). We address each inefficiency via existence checks, 32-byte SHA256 node references, zero-copy reference-counted buffers, and HashMap-based lexicographic deduplication.
Benchmarks on Apple M1 Pro show 57\% heap allocation reduction (566,760 to 242,004 bytes per 10K proofs), parallel insertion at 2,433 ns/op, and network-wide elimination of 4.85 PB/year across 6,000 full nodes, advancing the Ethereum stateless roadmap.

---


### 9. [Quantifying quantum risk: a measure of crypto agility](https://arxiv.org/abs/2606.17116)

**<font color=#1a73e8>作者：</font>** Coryan Wilson-Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Because of their ability to enable new forms of cryptanalysis, quantum computers pose a threat to the cryptographic algorithms that are widely used to secure contemporary computer systems. A practical quantum computer may emerge within the next ten years or so, but due to theorised "harvest now, decrypt later" style attacker behaviour, mitigations are necessary today. Recent advances in cryptography and security architecture show promise in supporting the design of systems that exhibit resilience against quantum-enabled cryptanalysis, however there is a key gap in the literature around the subject of deriving tolerances for such systems. In this paper, we introduce the concept of rotation time as a measure of crypto agility, and derive an approximation that links rotation time tolerance to security risk tolerance. Historical CVE data is used to calculate illustrative values for rotation time tolerance, which is found to be of the order of hours to days. This demonstrates that using crypto agility in conjunction with hybrid encryption is an effective approach for designing quantum-resilient systems, but may necessitate challenging technical and operational tolerances in order to meet organisational risk tolerances.

---


### 10. [Graph neural networks at war: integrating cybersecurity and drone intelligence in the Israeli-Iranian conflict](https://arxiv.org/abs/2606.17119)

**<font color=#1a73e8>作者：</font>** Sozan Sulaiman Maghdid, Tarik Ahmed Rashid, Shavan Askar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical cyber systems have brought about new threats and challenges in detection and immediate response. This study examines how Graph Neural Networks (GNNs) can be used to aid cybersecurity and drone management in a physical cyber system comprising of cyber intrusions and unmanned aerial vehicles (UAVs). By providing a bridge between structural understanding of graphical neural networks, this work has provided an integrated procedure that allows intrusion detection systems to educate on underlying network structures, identify malicious activity, and facilitates drone response measures. Based on an emulation-based case study, cyberattacks models were created to provoke the responses of the drones, which proved that graph-based learning can assist with the situational awareness, swarm coordination, and adaptive maneuver. According to the performance valuation, this method has a detection rate of 94.2, average area under the receiver operating characteristic (ROC) of 0.955 and an average response time of 1.4 seconds. Comparative experiments reveal that proposed GraphSAGE network is more effective than the Graphical Convolutional Networks (GCNs) and Graphical Attention Networks (GATs) in the identical situation. Such findings prove that graphical neural networks can be used to avert intrusion and response of dynamic cyber-physical systems.

---


### 11. [Noise-Driven Escape from Metastable Phases explains Grokking in Deep Neural Networks](https://arxiv.org/abs/2606.17120)

**<font color=#1a73e8>作者：</font>** Ibrahim Talha Ersoy, Karoline Wiesner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) exhibit first order phase transitions under variations of the L2 regularization strength, with each transition marking the onset of a new learnable feature. Below a critical regularization strength, all features are in principle learnable, but coexisting metastable states, separated by energy barriers, can trap the network and impede convergence. A strength of DNNs is their ability to generalize. But many open questions remain, among them the origin of so called grokking: the abrupt, delayed onset of generalization after prolonged apparent overfitting. We show for linear DNNs that grokking is consistent with hysteresis in first-order L2 phase transitions: using L2 regularization to engineer deliberate trapping, we demonstrate that a model in a low-accuracy metastable state escapes only when SGD noise drives it across an energy barrier, with escape times following Arrhenius scaling. We reproduce grokking-like delayed convergence across two orders of magnitude in escape time by deliberately trapping models in metastable phases. Using sparse sub-sampling we also reproduce the canonical grokking curve where test error eventually approaches the final training error. Our work suggests that the number of metastable states equals the number of learnable features -- one per singular value of the data covariance -- the potential for hysteresis grows naturally with task complexity. We provide evidence that the same mechanism likely operates in general nonlinear DNNs. Our results provide routes toward more efficient learning schemes.

---


### 12. [TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations](https://arxiv.org/abs/2606.17122)

**<font color=#1a73e8>作者：</font>** Rutger Hendrix, Leonardo G. Russo, Concetto Spampinato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The demand for privacy-compliant AI has amplified the need for machine unlearning; yet, existing retraining or distillation-based methods remain unverifiable and computationally costly. We introduce TrustErase, a verifiable, data-free unlearning framework leveraging passport-embedded representations for instant, modular, and auditable forgetting. By treating passports as cryptographic keys within parameter-efficient adaptation layers, TrustErase enables the removal of specific classes or datasets through simple deactivation, without retraining, fine-tuning, or access to the original data. A singular value based decomposition conceals passports within model weights, ensuring that unlearning actions remain transparent and provably compliant. Evaluations on MNIST, CIFAR10 and CIFAR100 show that TrustErase matches or exceeds state-of-the-art benchmarks such as DELETE, L2UL, and Boundary Shrink, while operating in a strictly data-free regime. Ultimately, TrustErase establishes a new paradigm for trustworthy, accountable, and instantly forgettable AI systems.

---


### 13. [MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision](https://arxiv.org/abs/2606.17162)

**<font color=#1a73e8>作者：</font>** Ye Jin, Yangyang Xu, Jun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized presentation generation requires more than conditioning on a current prompt or template: agents must preserve stable user preferences across tasks, retain newly introduced preferences and constraints during multi-turn revision, and carry out local edits reliably. We propose MemSlides, a hierarchical memory framework for personalized presentation agents that separates long-term memory from working memory and further divides long-term memory into user profile memory and tool memory. User profile memory stores intent-conditioned profiles for round-0 personalization, working memory carries active preferences and session constraints across revision rounds, and tool memory stores reusable execution experience for reliable localized editing. MemSlides pairs this memory design with scoped slide-local revision, so targeted updates act on the smallest affected region instead of repeatedly regenerating the full deck. In controlled experiments, user profile memory improves persona-alignment judgments on a multi-persona, multi-intent profile bank, tool-memory injection improves closed-loop modify behavior in diagnostic matched-pair settings, and qualitative cases illustrate working memory's ability to carryover preferences. Taken together, these results suggest that effective personalization in presentation authoring depends on separating persistent user profiles, session-level working memory, and reusable execution experience across generation and localized revision.

---


### 14. [From Parasocial Scripts to Dyadic Persistence in Autonomous AI-Agent Communities](https://arxiv.org/abs/2606.17174)

**<font color=#1a73e8>作者：</font>** Mohammadsadegh Abolhasani, Hamid Reza Firoozfar, Reza Mousavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While parasocial interactions (PSIs) and parasocial relationships (PSRs) have been studied in conventional media settings, we investigate whether PSI- (colloquial) relational cues also exist in online communities where both sides are autonomous AI agents. We analyze 4,434 posts and 50,338 comments from Moltbook through three theory-based textual indicators: attachment/intimacy language, reciprocity bids, and self-identification to original poster (OP). The combined results across methods based on keyword matching, few-shot large language model (LLM) annotation, and grouped-context LLM annotation reveal that PSI colloquial cues prevail and are strongly associated with OP re-engagement and a reciprocal reply structure. These results are robust across negative controls, nullification, clustered-standard-error re-estimation, and multiple-testing correction. A dyadic persistence test further affirms reciprocity bids aligned with sustained OP-involving mutual recurrence, providing empirical evidence for bridging interaction-level PSI scripts with PSR-consistent repeated dyadic patterns. We interpret the evidence as a behavioral structure in discourse by LLM-enabled agents.

---


### 15. [Towards Fast GNN Surrogates for CO2 Migration in Complex Geological Formations](https://arxiv.org/abs/2606.17180)

**<font color=#1a73e8>作者：</font>** Rodrigo S. Luna, Thiago H. N. Coelho, Luiz S. L. Neto 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This chapter discusses how a data-driven machine learning approach can reproduce key aspects of the physical behavior of multiphase flows in complex geological formations. We propose an end-to-end graph neural surrogate tailored to CO$_2$ plume migration forecasting in geological storage. The method is evaluated on the SPE11A benchmark, a well-known industry test case designed to assess CO$_2$ storage scenarios and characterized by sharp gas-water interfaces, strong advective transport, and rapid convective mixing with fingering development. The benchmark is reformulated as a graph in which nodes represent computational cells and edges encode transmissibility-based interactions enriched with geometric attributes. Directional transport arising from grid geometry, permeability contrasts, and geological heterogeneity is captured through an anisotropic message-passing mechanism, where interaction weights are computed via geometry-conditioned edge embeddings, biasing message aggregation toward physically relevant transport directions. Temporal evolution is modeled in latent space using an autoregressive residual formulation trained with multi-step supervision. The proposed model produces competitive forecasts of gas saturation and liquid-phase density, which are key indicators for CO$_2$ storage monitoring, with cumulative errors that remain moderate over extended forecasting horizons.

---


### 16. [Finsler Geometry, Graph Neural Networks, and You](https://arxiv.org/abs/2606.17185)

**<font color=#1a73e8>作者：</font>** T. Mitchell Roddenberry, Richard G. Baraniuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural network architectures based on the graph Laplacian approximate the Laplace-Beltrami operator, thus limiting their application to isotropic operators. As a nonlinear alternative to the Laplace-Beltrami operator, we consider estimates of the Finsler Laplacian on point clouds sampled from a manifold. We prove that these discrete estimates converge to the true operator on the manifold as the number of point samples grows. Moreover, we show that this operator can be expressed as a graph neural network layer, which we use to define a family of Finslerian graph neural networks constrained to express Finsler geometry. We show that Finslerian graph neural networks recover the geometry underlying nonlinear diffusion equations in practice.

---


### 17. [Not Truly Multilingual: Script Consistency as a Missing Dimension in VLM Evaluation](https://arxiv.org/abs/2606.17188)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Bhushan Pawar, Madhu Reddiboina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current multilingual evaluations for Vision-Language Models (VLMs) assume a one-to-one mapping between language and orthography, overlooking billions of users of multi-script languages. We introduce PuMVR (Punjabi Multimodal Visual Reasoning), a benchmark of 1,000 strictly parallel image-text instances across Punjabi's three active scripts: Gurmukhi, Shahmukhi, and Roman. Evaluating 10 state-of-the-art VLMs, we expose a substantial and systematic Script Gap. Models frequently solve visual tasks in one script while failing identical tasks in another, with accuracy deltas reaching 16%. Crucially, visual input boosts absolute performance uniformly yet does not close the orthographic gap. Furthermore, cross-script in-context transfer is highly brittle, exposing script-locked knowledge representation. Supported by McNemar tests across all script pairs, our findings demonstrate that current "multilingual" VLMs are not truly multi-script. We propose the Script Consistency Rate (SCR), which falls as low as 24.8% on our benchmark, as a mandatory metric for script-agnostic evaluation to ensure equitable AI access. Data and code are available at: this https URL.

---


### 18. [Constrained Diffusion Models with Primal-Dual Inference](https://arxiv.org/abs/2606.17192)

**<font color=#1a73e8>作者：</font>** Samar Hadou, Yigit Berkay Uslu, Alejandro Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops constrained diffusion models with primal-dual inference (PDI) to sample from optimal distributions of entropy-regularized optimization problems with \emph{average} constraints. We formalize constrained sampling in the Lagrangian dual domain, where the optimal distribution takes the form of a Gibbs distribution indexed by the optimal dual variable. Rather than estimating this dual multiplier before sampling and freezing it throughout generation, PDI jointly infers the optimal primal distribution and its parametrizing dual variable. Each reverse diffusion step denoises using the score field associated with the current multiplier and then updates the multiplier through dual ascent using the estimated constraint violation of the denoised samples. To enable this conditional score field, we train a single dual-conditioned score network over the family of Gibbs distributions induced by the dual variables encountered during inference. We prove that the time average of the dual variables generated along the inference trajectory converges to a neighborhood of the dual optimum and bound the effect of residual dual mismatch on the terminal distribution through schedule-dependent stability factors. We evaluate PDI on constrained sampling from a mixture of Gaussians, wireless resource allocation, and portfolio management.

---


### 19. [Sum-of-Squares Degree Barriers for the Reweighted-Hinge Method in Robust Halfspace Learning: A Christoffel-Function Characterization](https://arxiv.org/abs/2606.17215)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A certificate that removes outliers sees the data only through its low-degree moments, and an adversary exploits exactly this, hiding corruption where the clean data already looks typical, in the blind spot no bounded-degree test resolves. That blind spot turns out to have an exact size: the Christoffel function of the clean marginal, the very quantity modern data analysis thresholds to detect outliers, here read from the adversary's side as the corruption a bounded-degree certificate cannot remove. We turn this inversion into the organizing principle of the reweighted-hinge approach to robustly learning $\gamma$-margin halfspaces under malicious noise (Shen, 2025; Zeng and Shen, 2025): the governing resource is the Sum-of-Squares degree of the outlier-removal certificate, and the resolution principle states that the maximal corruption mass which can hide at a center $c$ from a degree-$2t$ certificate is exactly the Christoffel function $\lambda_{t+1}(c)$ of the clean marginal. Three consequences follow, all against the certificate method (not information-theoretic). A margin-degree tradeoff: certifying the dense pancake to error $\epsilon$ costs SoS degree $\Omega(\log(1/\epsilon))$ or margin $\Omega(\sqrt{\log(1/\epsilon)}/\sqrt{d})$, explaining why the $\log(1/\epsilon)$ margin Shen (2025) records is forced, with a weighted-Chebyshev reduction making the threshold $2t=\Theta((|c|/s)^2)$ tight modulo one classical weighted-extremal estimate. A degree-$2$ outlier barrier: the resolution principle realized as an explicit instance on which degree $2$ is stuck at $\eta^{1/2}$ while degree $4$ escapes, locating the method's small breakdown rate in the degree, not the analysis. And a degree-$2t$ algorithm tracing the frontier $\eta^{1-1/2t}$ (recovering Shen (2025) at $t=1$), whose gain is an explicit constant, capped by the pancake density and shown unimprovable by the degree-$2$ barrier.

---


### 20. [Intermittent Strategic Cooperation of Two Selfish Agents on Graphs](https://arxiv.org/abs/2606.17216)

**<font color=#1a73e8>作者：</font>** Itay Shedlezki, Noa Agmon  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study strategic space- and time-constrained cooperation between two self-interested agents through the Intermittent Strategic Cooperation-Based Two-Agent Path Planning (IC2PP) problem, a shortest-path game on graphs in which agents navigate toward individual targets while optionally cooperating at specific nodes to reduce their own travel times. Although such cooperation can strictly benefit both agents, it is strategically fragile: agents may deviate at any point along their paths. Modeled as a 2-player game, we characterize the structure of Pure Nash Equilibrium (PNE) joint strategies in IC2PP, and show that stable cooperation must follow a highly constrained form. We further prove that at least one PNE exists in every instance of IC2PP, and present a polynomial-time algorithm for enumerating all relevant PNEs. When multiple equilibria arise, we study coordination mechanisms based on bargaining-theoretic selection concepts and empirically compare equilibrium outcomes in terms of individual travel times and social welfare.

---


### 21. [When Rules Learn: A Self-Evolving Agent for Legal Case Retrieval](https://arxiv.org/abs/2606.17220)

**<font color=#1a73e8>作者：</font>** Mingxu Tao, Jiawei Hu, Xian Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal case retrieval remains challenging due to the complexity of legal language and the need for precise lexical alignment between queries and relevant cases. Although dense retrieval models have achieved notable progress, empirical studies show that BM25 continues to serve as a strong baseline in this domain. It motivates us to propose a self-evolving framework for rule-driven query rewriting that enhances BM25 without any parameter training. The framework equips an LLM-based agent with an automatic evaluation environment, enabling it to iteratively create rewriting rules, plan validation experiments over rule combinations, and eliminate ineffective rules based on historical feedbacks. We evaluate our method on the Chinese legal case retrieval benchmark LeCaRD-v2. Experimental results demonstrate that the proposed framework outperforms non-evolutionary baselines, including human-designed rules and greedy rule selection, particularly when powered by a highcapacity core LLM. We also conduct detailed analyses to investigate the mechanisms underlying self-evolution. Our findings reveal that LLM's capabilities to leverage previous experimental results and its intrinsic knowledge of rule elimination play critical roles in refining the rule set via self-evolution.

---


### 22. [Quantum Enchanced Multi-Scale CNN with Bi-directional Mamba for Crop Field Analysis](https://arxiv.org/abs/2606.17222)

**<font color=#1a73e8>作者：</font>** Mohammad Salman Khan, Ehsan Atoofian, Saad B. Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) crop analysis is essential for precision agriculture because it captures rich spectral and spatial information for accurate crop monitoring and assessment. However, HSI classification remains challenging due to high spectral dimensionality, spatial complexity, class imbalance, and limited labeled samples. To address these challenges, this paper proposes a BiSpectral Mamba-based framework that combines multi-scale convolutional feature extraction, spectral attention, bidirectional state-space modeling, and quantum-inspired learning. A multi-scale CNN backbone first extracts hierarchical spatial-spectral representations through feature fusion across multiple resolutions. A spectral attention mechanism then emphasizes informative bands while suppressing redundant and noisy channels. The refined features are processed by a BiSpectral Mamba module that captures long-range dependencies in both forward and backward directions by modeling hyperspectral feature maps as sequential tokens. In addition, class-weighted optimization and feature fusion strategies are incorporated to improve training stability and mitigate class imbalance. Experimental evaluation on the UAVHSI-Crop dataset demonstrates the effectiveness of the proposed framework, achieving an overall accuracy of 84.83%. The results show that integrating convolutional, attention-based, and state-space modeling components enables robust spatial-spectral feature learning for crop classification. The proposed framework also shows potential for broader agricultural and remote sensing applications, including crop disease detection, yield prediction, and soil moisture estimation, while highlighting the effectiveness of structured state-space and quantum-inspired architectures for hyperspectral image analysis.

---


### 23. [Safety, Security, and Cognitive Risks in Neuro-Symbolic AI](https://arxiv.org/abs/2606.17223)

**<font color=#1a73e8>作者：</font>** Manoj Parmar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neuro-symbolic AI (NeSy) pairs neural perception with symbolic reasoning, making it attractive for high-stakes domains where explainability and structured inference are required. However, this hybrid architecture introduces an enlarged attack surface spanning five layers: neural perception, symbolic knowledge bases, reasoning engines, agentic orchestration, and data stores -- each exploitable in ways absent from purely neural systems.
This paper makes six contributions: (1) formal definitions of NeSy Attack Surface, Symbolic Integrity Violation (SIV), and Cross-Layer Amplification Ratio $\mathcal{X}$, decomposed into neural-caused and autonomous symbolic sensitivity components; (2) a unified threat model extending MITRE ATLAS with 11 NeSy-specific tactic extensions and a five-profile attacker taxonomy; (3) a symbolic-layer threat catalogue covering knowledge graph (KG) poisoning, ontology-merging, and inference-engine subversion; (4) analysis of cognitive risks -- automation bias, authority bias, and sycophantic reinforcement -- structurally amplified by NeSy's explicit logical explanations relative to black-box neural outputs; (5) interdisciplinary mitigations with measurable acceptance criteria aligned to NIST AI 600-1 and the EU AI Act; (6) three empirical benchmarks: (E1) targeted KG poisoning achieves break-even SIV at injection budget $B=5$ on a 205-entity medical KG, with a KG-specific stealth/SIV trade-off; (E2) PGD-10 at $\varepsilon=0.01$ yields $\mathcal{X}=5.884$ (95% CI $[4.64,\, 8.00]$, $p<0.0001$), confirmed adversarially specific by a matched-random baseline ($E^{R}_{\mathrm{rand}}=0$), on a DistilBERT+ProbLog pipeline; (E3) single-axiom OWL edits achieve 93.3% SIV success with 100% Pellet-consistency stealth, but held-out STIX detection fails at 50% (random-guessing level), an open problem.

---


### 24. [Uncertainty Quantification of Engineering Structures by Polynomial Chaos Expansion and Multivariate Active Learning](https://arxiv.org/abs/2606.17233)

**<font color=#1a73e8>作者：</font>** Qitian Lu, Jafar Jafari-Asl, Panagiotis Spyridis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many engineering applications, a single high-fidelity model produces multiple quantities of interest (QoIs) under the same input parameters, e.g. finite element models of complex physical systems. To alleviate the high computational cost of direct model evaluations, surrogate models are widely used to construct efficient approximations of model responses. Naturally, the accuracy of surrogates strongly depends on the quality of the experimental design (ED). However, a single ED may not provide an adequate representation for all outputs simultaneously, especially when different outputs exhibit varying sensitivities to the input variables. A straightforward solution is to perform separate sampling for each output, but this results in increased sampling complexity and computational cost. From a statistical perspective, such an approach also ignores potential correlations among all outputs and may compromise data consistency. To address this issue, an adaptive sequential sampling method for constructing polynomial chaos expansion surrogate models is generalized for vector valued QoIs. The method sequentially selects new samples from a candidate pool based on their local contribution to the output variance, while balancing distance-based exploration of the input space and exploitation of aggregated variance information across all outputs. Its performance is compared with non-sequential Latin Hypercube Sampling through several numerical examples from engineering problems. Numerical results demonstrate that the proposed strategy improves both surrogate accuracy and stability, and provides a more reliable estimation of second-order statistics.

---


### 25. [Beyond Benchmarks: Continuous Edge Inference for Fine-Grained Roadside Perception](https://arxiv.org/abs/2606.17241)

**<font color=#1a73e8>作者：</font>** Aditya Mishra, Haroon Lone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous AI inference on resource-constrained edge hardware introduces deployment effects that are largely invisible to conventional benchmark evaluation, including temporal instability in streaming video, thermal throttling under sustained load, and workload-dependent performance variability. We present Edge-TSR, a deployment-oriented continuous edge inference system for sustained roadside perception on the NVIDIA Jetson Orin Nano. Edge-TSR integrates detection, tracking, fine-grained classification, and a lightweight track-aware temporal stabilization mechanism that improves streaming inference consistency with negligible computational overhead. Our central finding is that benchmark-centric evaluation systematically overstates deployed edge inference performance. Across three state-of-the-art baselines, we observe consistent 20-30% relative degradation when transitioning from static-image evaluation to real-world streaming deployment. Edge-TSR addresses this gap through temporal inference stabilization, recovering up to 10.16% classification accuracy over per-frame inference baselines while maintaining sustained real-time performance under continuous operation. We evaluate the complete system under diverse real-world deployment conditions, jointly characterizing inference quality, latency, throughput, and thermal behavior during long-duration operation. A 55-minute vehicular deployment over a 26 km route demonstrates sustained operation at 16.18 FPS within safe thermal limits on a single embedded device without cloud offload. Our findings show that deployment-aware evaluation and temporal inference stabilization are necessary components of continuously operating edge AI systems intended for real-world sensing deployments. We release a sample annotated streaming video evaluation dataset and full system implementation to support reproducible deployment-centric evaluation.

---


### 26. [Landsat-Sentinel-2 Algal Bloom Mapping Using Vision Transformers: Model Description, Implementation, and Examples](https://arxiv.org/abs/2606.17242)

**<font color=#1a73e8>作者：</font>** Thainara Lima, Vitor Martins  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coastal algal bloom monitoring requires frequent, spatially detailed, and globally consistent observations, provided by Landsat-8/9 and Sentinel-2 A/B/C. Together, these missions offer over a decade of medium-resolution multispectral imagery with near-global coverage every 2-3 days, enabling the detection of fragmented bloom structures not resolvable by coarse ocean-color sensors. However, their use in aquatic environments remains challenging due to limited spectral coverage and a lack of harmonized reflectance products. As an alternative to traditional bio-optical methods, deep learning-based image classification offers a data-driven approach that can overcome many of these limitations. This study presents the first successful implementation of vision transformer-based coastal algal bloom mapping using 30-m Landsat-Sentinel-2 images. A globally distributed bloom patch dataset was generated across bloom-prone coastal hotspots worldwide. Four transformer-based architectures were compared against a standard convolutional baseline for fine-scale bloom detection, and assessed under different optical water types and atmospheric and surface conditions. All deep learning models showed strong capabilities in detecting floating bloom areas, with omission and commission errors of 8-65%. Under cloud and glint stress in a time series, the Swin Transformer outperformed traditional spectral-index approaches, which produced widespread false positives, effectively avoiding cloud- and glint-affected pixels. Comparisons with MODIS-derived products further highlighted the benefits of higher spatial resolution in detecting fragmented and irregularly affected blooms. Our findings support deep learning as a reliable tool for medium-resolution, consistent monitoring of floating algal blooms in dynamic coastal environments.

---


### 27. [Cache to the Future: A Distributed Webpage Archive for Internet Blackouts](https://arxiv.org/abs/2606.17245)

**<font color=#1a73e8>作者：</font>** Ross Evans, Diogo Barradas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet blackouts, occurring due to technological mishaps or intentional governmental action, prevent citizens from accessing the internet. Citizens in regions where internet blackouts are common have utilized blackout-resistant technologies to maintain communication. Such technologies often rely on mobile mesh networks to provide limited messaging services. However, no technology currently exists which can provide continued access to knowledge sources on the web during a blackout.
We present Cache to the Future (CttF): a system to cache and deliver static content hosted on the web during a blackout. CttF's distributed community ratings crowdsources caching at scale while cryptographic constructs (digital signatures, proofs-of-work) mitigate adversarial interference. Our realistic simulations demonstrate CttF delivering content at city-scale across a wide range of benign and adversarial scenarios.

---


### 28. [MLLP-VRAIN UPV system for the IWSLT 2026 Simultaneous Speech Translation task](https://arxiv.org/abs/2606.17255)

**<font color=#1a73e8>作者：</font>** Jorge Iranzo-Sánchez, Gerard Mas-Mollà, Adrià Giménez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work describes the participation of the MLLP-VRAIN research group in the shared task of the IWSLT 2026 Simultaneous Speech Translation track. Our submission utilizes the recently released Parakeet and Qwen 3.5 models to create a robust, cascaded solution for long-form SimulST through the use of adaptive "black-box" policies. We explore relaxations of these policies to achieve better quality-latency trade-offs. Compared to last year, we participate on all language directions. In addition to this, for the En$\rightarrow${De, It, Zh} directions we also participate in this year's new context track employing a combination of ASR word-boosting and a RAG mechanism of offline pre-translated exemplars to guide generation and enrich our system with domain-specific context. Finally, we provide a detailed latency analysis of our system. Compared to last year, results on the MCIF En$\rightarrow$De test set shows a substantial quality improvement of +5.82 XCOMET-XL. Our context track processing further improves performance by +1.03.

---


### 29. [SkillChain-Gym: A Benchmark for Reskilling-Aware Production-Inventory Control under Disruptions](https://arxiv.org/abs/2606.17266)

**<font color=#1a73e8>作者：</font>** Carlos Eduardo Sanoja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production planning increasingly has to treat workforce capability as a decision variable: certifications lapse when skills are not maintained, new products require skills the current workforce does not hold, and reskilling competes for the same worker hours needed for production. Existing operations benchmarks usually treat labor as exogenous, while workforce-planning models with skills and learning are rarely released as reusable testbeds. We introduce SkillChain-Gym, a benchmark specification for reskilling-aware production-inventory control: a single-site environment with stylized worker skill-state dynamics, hard threshold certification, forgetting, and capacity-consuming training actions constrained by the same per-worker time budget as production. The benchmark includes seed-controlled disruption scenarios, three feasibility modes with projection diagnostics, deterministic replay, and metrics covering operations, resilience, capability growth, and training-access distribution. We evaluate production-only, reactive adaptive, water-filling adaptive, and static-insurance policies with budget variants over 60-shift horizons with paired statistical tests. The results are regime-dependent rather than a ranking. Training-capable policies dominate the production-only baseline, and maintenance training is necessary under forgetting even without disruptions. Among training-capable classes, adaptive training helps when bottlenecks are visible in the forecast, while a lean static cross-training plan, a deliberately favorable comparator whose structure encodes relevant skill contingencies, acts as strong insurance under surprise shocks and absenteeism. Capacity slack and the forgetting rate govern the boundary between these regimes. No policy class dominates across regimes, motivating forecast-driven controllers that decide when to buy skill insurance and when to react.

---


### 30. [Skill-Constrained Model Predictive Control for Resilient Manufacturing Supply Chains](https://arxiv.org/abs/2606.17269)

**<font color=#1a73e8>作者：</font>** Carlos Eduardo Sanoja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In skill-constrained production-inventory systems, the qualified human capacity available tomorrow depends on training decisions made today: production requires certified workers, certifications decay unless maintained, and training consumes the same scarce worker hours that production needs now. We study a closed-loop skill-constrained model predictive controller that, at every shift, solves a finite-horizon mixed-integer program over production, inventory, backlog, and training, with binary predicted certification, hard production eligibility, and an interpretable terminal value that prices certified-capacity gaps at the horizon boundary; only the first-period action is applied before replanning. On synthetic, seed-controlled SkillChain-Gym scenarios - announced and surprise new-skill shocks, demand shocks, absenteeism, forecast- and availability-quality modes, capacity-boundary and training-rate sweeps, and negative controls - we evaluate the controller against production-only and maintenance-only ablations, static cross-training insurance plans, and a strong reactive heuristic, under an ex-ante locked configuration and paired statistics. The result is regime dependence, not superiority: no policy class dominates. Predictive control helps when skill or labor bottlenecks are forecastable early enough for training to complete; lean static insurance remains hard to beat under surprise shocks, near the demand-capacity boundary, and wherever pre-shock slack makes insurance cheap. Attribution ablations separate certification maintenance, re-acquisition of lapsed certifications, and greenfield skill acquisition. Forecastability, not adaptivity per se, decides when predictive control pays.

---


### 31. [ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software](https://arxiv.org/abs/2606.17283)

**<font color=#1a73e8>作者：</font>** Xiang Mei, Jordi Del Castillo, Pulkit Singh Singaria 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Achieving reproducibility, quantity, and diversity in vulnerability datasets has long been viewed as an inherent three-way trade-off, where improving one dimension often comes at the cost of the others. In practice, reproducibility has been the dimension most often neglected. This has limited what can be automatically extracted from historical bug datasets, and has reduced their utility for downstream security research.
In this work, we propose a method to produce a new security dataset which ensures reproducibility for diverse vulnerabilities at scale by identifying the key obstacles to large-scale bug reproduction and addressing them with general solutions. Using this method, we introduce full reproducibility to the largest open source software vulnerability dataset (OSS-Fuzz) and construct the ARVO dataset (an Atlas of Reproducible Vulnerabilities in Open-source software). ARVO is a large-scale dataset consisting of over 6,100 real-world vulnerabilities across 311 projects. Focusing on reproducibility, ARVO differs from existing datasets by providing each vulnerability in a form that can be consistently rebuilt, triggered, and analyzed across versions. Reproducibility also enables automatic identification of the corresponding patch for each vulnerability and supports direct interaction with vulnerabilities after code changes, capabilities that existing large-scale datasets do not provide. In our evaluation, ARVO successfully reproduces 81% of vulnerabilities and achieves 89.4% accuracy on the located patches. We also discuss ARVO's influence on both upstream practices and downstream security research.

---


### 32. [Reasoning Text-to-Video Retrieval for Operating Room Clips via Action-Driven Digital Twins](https://arxiv.org/abs/2606.17298)

**<font color=#1a73e8>作者：</font>** Yiqing Shen, Hao Ding, Mathias Unberath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video retrieval in operating rooms (OR) is an enabling technology for OR safety, as it allows stakeholders to retrieve and inspect recordings of specific events. However, because the most safety-critical events may not follow the common structure, to unlock its full potential text-to-video retrieval must be able to handle implicit queries that require reasoning to identify the right video (e.g., the step right before clipping). However, existing methods rely on global embeddings that cannot reason over such queries. We propose OR3, a text-to-video retrieval method that converts clips into action-driven digital twins (ActDTs), grouping concurrent subject-action-object triplets under non-overlapping temporal intervals. Moreover, rather than cross-modal matching through paired encoders, OR3 performs imagination-based retrieval where an LLM generates hypothetical ActDTs from queries. This enables intra-modal matching via a single encoder trained with ActDT-tailored hard negatives. Finally, evidence-grounded refinement revises imagined ActDTs based on discrepancies with top candidates to capture procedure-specific patterns. We construct a benchmark from MM-OR with 276 implicit queries across four reasoning categories over 386 clips from robotic knee procedures. OR3 achieves 57.6 R@1 and 77.3 R@5, outperforming the strongest baseline. These results demonstrate that OR3 enables fine-grained discrimination between visually similar OR video clips through temporal action reasoning.

---


### 33. [Examining the Limits of Word2Vec with Toki Pona](https://arxiv.org/abs/2606.17299)

**<font color=#1a73e8>作者：</font>** Daniel Zhenhan Huang, Hongchen Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word2Vec's effectiveness at generating semantic embeddings has been widely validated, yet it has been tested almost exclusively on languages with large vocabulary inventories. This study examines whether Word2Vec can successfully capture semantic relationships within an extremely reduced vocabulary using data from Toki Pona, a constructed language with approximately 130 words. We sourced 1.4 million sentences (7.95 million tokens) from the Toki Pona community for training. Approximately 23% of sentences in the corpus contain non-Toki Pona tokens such as named entities, loanwords, and neologisms. To investigate whether this linguistic noise enhances or hinders performance -- a topic rarely addressed in word embedding literature -- we trained two distinct models: one retaining these incidental tokens and another filtering them out completely. Evaluation was conducted using quantitative methods measuring word proximity to semantic category centroids, automated silhouette scores via agglomerative clustering, and qualitative analysis utilizing representational similarity matrices compared against English. The results indicate that while sparse, non-core tokens do not affect the relative structure of the learned embeddings, they actually draw similar words closer together in the vector space. Importantly, Word2Vec's effectiveness depends more on distributional patterns than lexicon size even at this extreme lower bound.

---


### 34. [SierpinskiCam: Camera-Controlled Video Retaking with Sierpinski Triangle Pattern Cues](https://arxiv.org/abs/2606.17310)

**<font color=#1a73e8>作者：</font>** Suttisak Wizadwongsa, Hyelin Nam, Supasorn Suwajanakorn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating novel renderings of a scene along user-defined camera trajectories from a single monocular video, dubbed video retaking, is a compelling but difficult problem in content creation and visual effects. Existing geometry-guided approaches reconstruct a 4D representation from the source video and render it along the target trajectory to condition video diffusion models. However, this guidance degrades as the target camera departs from the source trajectory, leaving newly revealed regions sparse or entirely missing. We propose SierpinskiCam, which addresses this limitation by augmenting geometry-based guidance with Sierpinski dome texture cues that contains rich trackable features even under large viewpoint changes. We further introduce a reference video conditioning mechanism that appends source-video tokens to the target-token sequence and separates the two streams with negative RoPE indices, enabling appearance grounding without architectural modification or per-video adaptation. Extensive experiments show that SierpinskiCam achieves significant gains in camera controllability, geometric consistency, and video quality across diverse and challenging retaking scenarios. Project page: this https URL.

---


### 35. [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](https://arxiv.org/abs/2606.17328)

**<font color=#1a73e8>作者：</font>** Xianxuan Long, Zhikai Chen, Shenglai Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly maintain long-term memory of user facts across sessions. Yet such memory is usually evaluated by aggregating accuracy over question rows or episodes. Because this approach scores question rows independently, even when several questions probe the same fact, it cannot show how that fact behaves as conditions change. We introduce MemTrace, a benchmark whose unit of measurement is the knowledge point: a single typed fact about the user, rather than an individual question. MemTrace probes each fact along three controlled dimensions: memory age, defined by how many sessions ago the fact appeared in the history; question type, covering current state, earlier state, and trajectory of change; and evidence condition, covering present, missing, and contradicted-by-false-premise settings. Evaluating 13 memory-system configurations across four paradigms, we find that similar pooled accuracy hides different failures: recovering a fact's current and earlier states does not imply tracking how it changed, and safe abstention does not imply correcting a false premise. The dominant bottleneck is evidence use, not retrieval: when systems fail, the evidence was retrievable 10 times more often than it was missing. These results suggest that improving long-term memory requires better use of reachable evidence, not simply more storage or retrieval.

---


### 36. [Decision-Driven Geosteering Under Uncertainty: A Unified Framework for Sequential Decision Optimization](https://arxiv.org/abs/2606.17331)

**<font color=#1a73e8>作者：</font>** Hibat Errahmen Djecta, Sergey Alyaev, Kristian Fossum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geosteering requires navigating a well trajectory through an unknown geological configuration, while sequentially updating decisions based on indirect measurements acquired during drilling. This work presents an uncertainty-aware geosteering framework that tightly integrates particle filtering for probabilistic subsurface interpretation with value-based reinforcement learning for sequential decision-making. Geological uncertainty ahead of the drill bit is represented explicitly through a particle filter (PF), enabling belief-informed control rather than deterministic trajectory correction.
The framework couples PF belief updates with belief-informed decision policies and evaluates three decision-making options that operate under identical uncertainty representations: an interpretable Approximate Dynamic Programming (ADP) scheme, a Deep Q-learning baseline, and a Dual Deep Reinforcement Learning (Dual DRL) architecture trained with a target Q-network scheme for stability, using a dueling (value/advantage) decomposition for Q-value parameterization. Beyond final placement performance, we assess policy behavior using stability-oriented metrics that quantify steering smoothness over time, providing additional operational insight into how decision policies respond as uncertainty evolves.
The framework is integrated with an API for validation within an industrial geosteering simulator under realistic measurement noise and drilling constraints. Using identical geological realizations, operational limits, and reward definitions across methods, the experiments provide a controlled and high-fidelity evaluation of how alternative decision policies behave throughout the drilling process, rather than evaluating performance solely from the final well trajectory.

---


### 37. [FATE: Pillar Encoding and Frequency-Aware Training for Event-Based Object Detection](https://arxiv.org/abs/2606.17334)

**<font color=#1a73e8>作者：</font>** Md Tawheedul Islam Bhuian, Kyoung-Don Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras are bio-inspired sensors that asynchronously capture logarithmic intensity changes, offering inherent advantages in high-speed and high-dynamic-range scenarios. However, the sparse and asynchronous nature of event streams poses a fundamental challenge for modern deep learning architectures. To enable compatibility with standard models, most existing approaches partition the accumulation window into fixed temporal sub-bins. While effective for spatial processing, this internal discretization discards fine-grained temporal structure and constrains inference to the low temporal frequencies imposed by training supervision. To address this limitation, we propose FATE, a unified framework built upon a novel Pillar Encoding (PE). While operating over discrete macro-accumulation windows dictated by the target frequency, PE avoids internal temporal sub-binning. It organizes events into spatial pillars and approximates their intra-window evolution via projection onto a continuous-time orthogonal polynomial basis. This formulation yields an L2-optimal representation that retains rich temporal dynamics in a dense pseudo-image, mitigating information loss under sparse event conditions. To fully leverage this representation, we introduce Frequency-Aware Training (FAT), a soft mean-teacher curriculum that generates temporally dense pseudo-labels, effectively bridging the mismatch between low-frequency supervision and high-frequency inference. Extensive experiments demonstrate that FATE generalizes across architectural paradigms and consistently outperforms strong baselines. It enables robust object detection at high temporal resolutions up to 200 Hz, while incurring minimal overhead in parameter count and inference latency

---


### 38. [SpeechDx: A Multi-Task Benchmark for Clinical Speech AI](https://arxiv.org/abs/2606.17339)

**<font color=#1a73e8>作者：</font>** Sejal Bhalla, Larry Kieu, Aina Merchant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speech offers a uniquely informative window into health by simultaneously engaging neurological, motor, respiratory, and vocal systems. Current clinical speech AI methods have largely progressed through isolated condition-specific studies, making results difficult to compare and generalization difficult to assess. We introduce SpeechDx, a large-scale benchmark for clinical speech AI spanning 12 datasets and 27 tasks across diverse health conditions. To enable evaluation across shared clinical mechanisms, SpeechDx structures tasks by the stage of speech production they disrupt: conceptualization, formulation, and articulation. The benchmark tests generalization by including tasks with limited labeled data and evaluating the same health condition across multiple datasets, distinguishing clinically meaningful patterns from dataset artefacts. We systematically evaluate 12 state-of-the-art audio encoders across all tasks and under zero-shot cross-condition transfer. Results show that large-scale speech models represent the strongest overall baselines, domain-specific models improve performance only on closely matched tasks, and no current representation generalizes reliably across the clinical speech landscape. SpeechDx establishes a shared evaluation framework for tracking progress toward general-purpose clinical speech representations

---


### 39. [Learning a Maximum Entropy Model for Visual Textures using Diffusion](https://arxiv.org/abs/2606.17342)

**<font color=#1a73e8>作者：</font>** Xinyuan Zhao, Eero P. Simoncelli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual textures -- spatially homogeneous image regions containing repeated elements (e.g. a field of grass, the bark of a tree) -- are ubiquitous in visual scenes and provide important cues for recognizing and analyzing materials and objects. A number of existing texture models extract essential statistics from a single texture image, and can then generate high-quality samples that are visually similar to the original by matching these statistics. However, their statistics are either hand-designed or based on a network pretrained for another purpose (e.g., object recognition). Here, we develop the first principled method for unsupervised learning of a set of statistics that are used to constrain a maximum entropy probability model. We leverage methods developed for generative diffusion models to derive training and sampling procedures, and compare these to the traditional method of sampling via matching the statistics. Despite the compactness of our trained model (512 statistics), it generates texture images whose quality is as good as or better than the current state-of-the-art model (~177k statistics). A more direct comparison of the two models, obtained by synthesizing images that are indistinguishable for one model but maximally different for the other, reveals their relative strengths and weaknesses. Finally, we show that unlike previous statistical texture models, a straight trajectory in the representation space of our model generates homogeneous texture samples that interpolate smoothly between the features of the two end points.

---


### 40. [Bayesian Magnetic Resonance Joint Image Reconstruction and Uncertainty Quantification using Sparsity Prior Models and Markov Chain Monte Carlo Sampling](https://arxiv.org/abs/2606.17343)

**<font color=#1a73e8>作者：</font>** Ahmed Karam Eldaly, Matteo Figini, Daniel C. Alexander  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel framework for uncertainty quantification using compressed sensing magnetic resonance image reconstruction. The problem is formulated within a Bayesian framework as a linear inverse problem, with prior distributions assigned to the unknown model parameters. Specifically, the image to be reconstructed is assumed to be sparse in a given basis. We develop a general framework applicable to any basis and as examples, we test the sparsity of the image in its (1) spatial gradients using a total variation prior model, and in its (2) wavelet transform. A Markov chain Monte Carlo (MCMC) method, based on a split-and-augmented Gibbs sampler, is then employed to sample from the posterior distribution of the unknown parameters. The non-differentiable conditional distributions are efficiently sampled using a proximal MCMC method. The proposed algorithms are validated on both single-coil and multi-coil datasets using various k-space sub-sampling patterns and ratios. The results demonstrate the superior performance of each proposed approach in reconstructing images compared to its counterpart optimisation-based method. Moreover, our framework effectively quantifies uncertainty, showing a notable correlation between estimated uncertainty maps and error maps computed using ground truth and reconstructed images, compared with existing deep learning-based methods.

---


### 41. [Counterfactual Optimization of Baseball Pitch Sequences and Estimation of Its Impact on Season-Level Statistics](https://arxiv.org/abs/2606.17345)

**<font color=#1a73e8>作者：</font>** Ryota Takamido, Hiroki Nakamoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although pitch sequencing is a central topic in baseball analytics, previous studies have primarily focused on optimizing the final pitch within a single plate appearance, leaving the role of preceding setup pitches and their impact on long-term season-level performance insufficiently examined. To address these issues, this study conducted counterfactual analyses using MLB Statcast data. A Transformer-based machine-learning model was trained to predict whether a target pitch would result in an in-play outcome or swing-out. Counterfactual pitch sequences were then generated by replacing either the final pitch or the preceding setup pitch with alternative pitch types and locations while keeping the surrounding contextual information fixed. Optimal counterfactual selections were defined as those that minimized the predicted in-play probability, and their expected effects on pitchers' seasonal statistics were estimated using regression models linking model outputs to season statistics. The results suggest that the optimization of both final and setup pitches may substantially influence season-level performance, including improvements of more than 1.0 in K/9. The analyses also provided several practical insights, including velocity-band-specific effective locations, the importance of pitch commands, and the expansion of pitch-selection options through middle-velocity pitches. These findings quantitatively support the strategic importance of pitch sequencing in baseball.

---


### 42. [MM++: Unsupervised Scale-Invariant Multilayer OOD Detection via Top-K Gated Feature Fusion](https://arxiv.org/abs/2606.17352)

**<font color=#1a73e8>作者：</font>** Rahim Hossain, Md Tawheedul Islam Bhuian, Md Farhan Shadiq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MM++ (Multilayer Mahalanobis++), a fully unsupervised, strictly post-hoc, and scale-invariant framework for Out-of-Distribution (OOD) detection. To address the trade-off between scale invariance and hierarchical expressivity, MM++ constructs a principled joint feature space. It first identifies discriminative intermediate layers by measuring entropy density drops, which mark the boundaries of sharp semantic compression. By fusing these selected layers with the terminal representation, the framework captures latent cross-layer correlations while mitigating early-layer noise. Crucially, a Ledoit-Wolf regularized tied covariance matrix stabilizes this unified space, enabling reliable distance estimation. Requiring no auxiliary OOD data, classifier fine-tuning, or architectural modifications, MM++ delivers robust performance across distinct architectures for both near- and far-OOD detection.

---


### 43. [Translating the Untranslatable: An Operationalizable Ontology for Untranslatability](https://arxiv.org/abs/2606.17354)

**<font color=#1a73e8>作者：</font>** Jacob Bremerman, Brihi Joshi, Hirona Arai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Untranslatability, cases where meaning cannot be directly preserved across languages, is well-studied in linguistics but underexplored in NLP. As machine translation (MT) systems improve on standard benchmarks, their limitations increasingly concentrate in such cases, where translation cannot be reduced to one-to-one equivalence. We introduce a structured ontology of untranslatability along with a taxonomy of compensation strategies, which are specific techniques to convey meaning under these untranslatable circumstances. We operationalize this framework into a multilingual dataset of untranslatable sentences paired with strategy-based translations, enabling controlled analysis of translation behavior. Initial human preference studies suggest that translation quality depends on the strategy used, with consistent preferences for outputs that include explanatory context, known as the Annotation compensation strategy. Our framework and dataset provide a foundation for studying and modeling strategy-informed machine translation.

---


### 44. [Complex Layout Classification in the Wild: A Low-Resource Approach with Layout-Preserving Augmentations](https://arxiv.org/abs/2606.17355)

**<font color=#1a73e8>作者：</font>** Sharva Gogawale, Iddo Hakim, Gal Grudka 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many digitized corpora suffer from low resources because annotations may be scarce, page scans are noisy and of poor resolution, or layouts are structurally complex in ways that negatively affect the quality of automatic transcription. Developing robust classification models for low-resource languages is inhibited by the lack of large-scale annotated data and by the frequent semantic complexity of page layouts. To this end, we have curated a complex-layout dataset, manually classified into eight distinct layout types based on their separator regions. To overcome data scarcity, we propose a novel training strategy in the form of a CNN-based classifier that employs strong, domain-aware augmentations to improve generalization. We utilize narrow anisotropic Gaussian masking to suppress incidental textual details while preserving essential separations, compelling the model to learn global geometric arrangements. Additionally, we implement reflection-induced label transformations to enrich the training distribution while maintaining label consistency across asymmetric categories. The results demonstrate that layout-specific augmentations can substantially improve page-level layout classification under severe annotation scarcity.

---


### 45. [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/abs/2606.17358)

**<font color=#1a73e8>作者：</font>** Jonghyun Lee, Yongqin Wang, Rachit Rajat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The CPU-side large language model (LLM) tokenizer is a critical security gap in LLM serving through a confidential computing stack with CPU and GPU trusted execution environments (TEEs). Tokenizers converts the prompts through table-driven lookups, and the resulting memory access patterns are a powerful source of side-channel leakage. Recent work demonstrates end-to-end recovery of user prompts from tokenizer access pattern on production Intel TDX. However, a drop-in use of the popular tree-based Oblivious RAMs (e.g., PathORAM) to prevent access-pattern leakage introduces $\sim$13$\times$ tokenizer slowdown, resulting in 10-58% higher time-to-first-token (TTFT).
In this paper, we present OTRO, an efficient, oblivious tokenization path tailored to latency-critical LLM serving. OTRO relies on square-root ORAM for fast single-access lookups, but avoids its prohibitive $O(N\log^2N$) rebuild cost every $\sqrt{N}$ accesses through three key innovations. First, OTRO provides a pool of replicated square-root ORAM instances that utilize the read-only nature of tokenizer table. Second, an epoch-based rotation policy decouples accesses from rebuilds and pads each epoch with dummy accesses to its boundaries, minimizing observable information. Lastly, chunked KV-cache-aware tokenization further overlaps rebuilds with GPU prefill and minimizes the instance count. Implemented as modules in HuggingFace Tokenizers and nano-vLLM, running within a TDX-enabled CVM with an NVIDIA H100 GPU, OTRO limits TTFT overhead to at most 4.5%, keeps tokenizer-induced latency under 10\% of total TTFT, and adds less than 0.5 GB of memory overhead while reducing the tokenizer's observable leakage across various model families and sizes.

---


### 46. [Distributed General-Purpose Agent Networks: Architecture, Key Mechanisms, and Prototypes](https://arxiv.org/abs/2606.17368)

**<font color=#1a73e8>作者：</font>** Shengli Zhang, Deen Ma, Zibin Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have accelerated the transition from passive conversational assistants to autonomous agents that can understand goals, plan actions, invoke tools, and execute multi-step tasks. Yet the capability of a single agent remains constrained by its local data, tool permissions, runtime environment, and governance boundary. This paper studies distributed general-purpose agent networks: open peer-to-peer networks in which heterogeneous agents deployed on personal devices, edge nodes, or autonomous computing environments can discover one another, establish trust, negotiate cooperation rules, and execute open-ended tasks. We argue that such networks cannot be obtained by simply combining existing peer-to-peer overlays with conventional multi-agent systems. Unlike traditional P2P networks, agent networks must propagate semantic declarations about intentions, capabilities, states, and cooperation constraints. We therefore propose a layered architecture centered on a protocol adaptation layer that connects upper-level task semantics with lower-level network operations. Based on this architecture, the paper identifies three core mechanism problems: semantic announcement propagation for collaborator discovery, verifiable identity and multi-topic reputation for cooperation governance, and semantic-gradient mechanism design for open task execution. For each problem, we present a technical route, including bodyless gossip with sequential logs, BAID-based identity binding with MG-EigenTrust reputation, and a Stackelberg-style mechanism-generation loop driven by semantic attribution feedback. We further report prototype overhead results for BAID-style tiered verification and mechanism-level simulations of MG-EigenTrust under cross-topic disguise-collusion attacks. The resulting framework provides a system-level foundation for open, trustworthy, and scalable agent collaboration.

---


### 47. [Performance-Driven Environment Abstraction with Multi-Timescale Learning](https://arxiv.org/abs/2606.17377)

**<font color=#1a73e8>作者：</font>** Yue Guan, Dipankar Maity, Panagiotis Tsiotras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study performance-driven environment abstraction for decision-making in large Markov decision processes. Rather than preserving geometric or topological structure, we seek abstractions that directly optimize decision quality. We model abstraction as a controlled approximation obtained by aggregating the state space and enforcing a shared action distribution within each aggregated state. For a fixed partition, we establish a performance guarantee that separates value-function approximation error from the loss introduced by action sharing. Guided by this analysis, we develop a multi-timescale reinforcement learning framework that jointly adapts the policy and a tree-structured environment abstraction. The resulting algorithm refines and coarsens regions of the state space based on Q-value discrepancies, balancing performance against abstraction size and complexity. Empirical results demonstrate substantial state compression, improved sample efficiency, and faster replanning compared to actor-critic baselines.

---


### 48. [MeiBRD: Meta-Learning Intraoperative Biomechanical Residual Deformation](https://arxiv.org/abs/2606.17379)

**<font color=#1a73e8>作者：</font>** Casey Meisenzahl, Jon Heiselman, Michael Holtz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate intraoperative liver registration is challenging due to substantial soft-tissue deformation yet sparse intraoperative measurements. Biomechanical models regularize this ill-posedness with prior knowledge but exhibit persistent prediction bias due to simplifying assumptions, while data-driven learning solutions struggle with data efficiency, generalization, and physical plausibility. We propose a hybrid registration framework that adapts a biomechanical prior using sparse intraoperative correspondences. Rather than learning a full deformation field, we learn a residual deformation function that corrects linear biomechanical predictions, modeled as a graph neural diffusion function with geometry-aware attention over the 3D liver mesh. To enable long-range information transfer of sparse observations, we take a novel perspective of sparse intraoperative measurements as \textit{context} samples where input-output pairs of the residual deformation function are fully observed, casting the problem into learning-to-learn this residual function from intraoperative context samples with feedforward meta-learners. Experiments on a deformable liver phantom dataset demonstrate improved registration accuracy and generalization compared to rigid, biomechanical, and data-driven baselines, particularly for out-of-distribution geometries and deformations.

---


### 49. [Improving and Evaluating Hand-Object Interaction Detection](https://arxiv.org/abs/2606.17384)

**<font color=#1a73e8>作者：</font>** Ahmad Darkhalil, Dima Damen, David Fouhey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding hands and the objects they interact with, both directly and through tools, is a key step for tasks ranging from action perception to 3D reconstruction and robotics. Our paper provides several contributions to the Hand-Object Interaction (HOI) understanding literature: (1) HOI-DETR, a new framework that introduces hand-object and object-object interactions to the Co-DETR architecture to produce a state-of-the-art method; (2) a comprehensive HOI evaluation suite of 4 diverse datasets, including a video benchmark derived from the HD-EPIC dataset and fresh annotations that improve the Hands23 benchmark and (3) a trained checkpoint that significantly improves the state of the art across Hands23, HOIST, FineBio, and HD-EPIC, including mAP gains of over 20 percentage points on Hands23 and FineBio. Our ablations confirm the contributions of each model component.

---


### 50. [TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations](https://arxiv.org/abs/2606.17386)

**<font color=#1a73e8>作者：</font>** Zikang Xiong, Weixin Li, Zhouchonghao Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-205](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
