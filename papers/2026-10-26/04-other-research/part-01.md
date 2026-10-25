# 📦 其他研究 | 2026年10月26日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 1. [baseVultra: Compact Nonlinear Recurrence with Reallocated Capacity](https://arxiv.org/abs/2610.30154)

**<font color=#1a73e8>作者：</font>** Linke Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nonlinear recurrent networks remain useful for streaming sequence modeling, yet gated cell design is still dominated by LSTM and GRU. We study whether recurrent computation can be reallocated away from gate transforms and toward candidate generation. We propose baseVultra, a compact recurrent cell that concentrates the dense recurrent budget on a single H x H candidate-generation matrix, while replacing recurrent gate matrices with O(H) diagonal interactions. The candidate update combines this dense branch with two low-rank auxiliary branches, an EMA cache, and learnable output blending; the gates additionally receive lightweight second-order access to h_{t-2} through diagonal terms. On TinyShakespeare character-level language modeling, baseVultra achieves a validation loss of 1.594 in the compact one-layer 200K setting, compared with 1.604 for a parameter-matched LSTM and 1.616 for a parameter-matched GRU, while its dense recurrent matrix-vector computation is about 54% of GRU under matched hidden size for this configuration. On text8, a roughly 45x larger benchmark, baseVultra is competitive with full-gate cells (1.854 bpc vs. 1.849 for GRU and 1.837 for LSTM). On formal-language probes, the largest gains appear under constrained hidden-state capacity (0.991 vs. 0.761 GRU and 0.691 LSTM OOD2 accuracy on Counter at H=16) and vanish as hidden size grows. These results characterize where and when candidate-focused recurrent capacity allocation helps: the benefit is concentrated in compact regimes, while full-gate cells remain competitive at scale.

---


### 2. [MCP vs CLI for AI Agents: A Comparative Analysis of Tool Integration Strategies for Autonomous Systems](https://arxiv.org/abs/2610.30157)

**<font color=#1a73e8>作者：</font>** Arun Malik, Nitish Talasu, Bradley Klemick 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents require interfaces to interact with external systems such as files, APIs, databases, and cloud services. Two competing paradigms have emerged: CLI (Command Line Interface), where agents execute shell commands directly, and MCP (Model Context Protocol), a structured JSON-RPC protocol providing governed, typed tool access. This paper presents a comparative analysis across 14 evaluation dimensions, supported by worked examples, security assessment against established compliance frameworks, and economic modeling. Our analysis indicates that CLI provides superior efficiency for single-user, local-only workflows, while MCP addresses requirements that CLI fundamentally cannot satisfy, including fine-grained access control, credential isolation, structured audit, and multi-tenant governance. We further examine how progressive disclosure techniques eliminate MCP's historical weakness (context window overhead), yielding token efficiency comparable to CLI while preserving its architectural benefits. A hybrid architecture is recommended for production systems. This analysis draws upon academic, government, and industry sources including NSA formal guidance (CSI U/OO/6030316-26), OWASP security standards, and economic modeling from BCG and Gartner.

---


### 3. [V-JEPA 2 Meets AQA: Phase-Based Scoring and Reference-Based Feedback for Mountain Biking](https://arxiv.org/abs/2610.30160)

**<font color=#1a73e8>作者：</font>** Santhiya Rajan, Savio Cardoz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study mountain-bike action quality assessment (AQA) with weak labels and candidate feedback. The training corpus comprises 95 field-recorded jump clips with binary labels denoting good or poor technique. These are coarse categorical labels, not continuous expert quality scores; phase-boundary and aspect-level annotations are unavailable. Our pipeline summarizes four heuristic phases using frozen V-JEPA 2 video features and two-dimensional pose and motion measurements. A small transformer predicts a binary-label score. A separate reference layer compares phase-specific measurements with those of clips labelled as good technique to propose phase, body-parameter, and direction cues. We detail the measurements, network, and evaluation so that the limits of each output are explicit. In five-fold clip-level cross-validation, the full scorer obtained pooled out-of-fold AUROC 0.768 and average precision 0.812. These are exploratory figures because the reporting fold also selected the neural training epoch and riders were not separated between folds. Removing biomechanical scoring inputs raised AUROC to 0.809. A separate inner-selection run obtained AUROC 0.678, but used about 57 rather than 76 training clips per outer fold, so its difference from the test-selected run does not quantify selection bias. The unsupervised aspect head did not learn distinct factors. On a 17-clip external probe, an earlier checkpoint obtained binary accuracy 0.412 and Spearman association -0.135 with expert scores. Candidate cues had precision 0.118 and recall 1.0 against each of two coaches, with substantial disagreement about direction. These findings do not establish rider-independent scoring or reliable corrective feedback; they identify the empirical work needed to evaluate either use.

---


### 4. [Accelerating Wildfire Hazard Mapping Across Canada with an AI Surrogate Modelling Framework](https://arxiv.org/abs/2610.30170)

**<font color=#1a73e8>作者：</font>** Hager Radi Abdelwahed, Toluwaleke Olutayo, Chirag Goel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Canada's increasing wildfire activity requires frequent national hazard mapping to guide proactive mitigation, including fuel management, land-use planning, infrastructure protection, and evacuation routing. However, process-based wildfire simulation frameworks (e.g., BurnP3 and BurnP3+) rely on computationally intensive Monte Carlo simulations to model burn probability, fire intensity, and rate of spread. These workflows can take days to weeks to process a single regional modelling unit. To overcome these computational bottlenecks, we present three contributions developed through collaboration between AI researchers and wildfire modelling experts: (a) a standardized framework for training, fine-tuning, and evaluating AI surrogate models against process-based wildfire simulators; (b) a multi-task deep learning surrogate trained on national-scale data to emulate burn probability, mean fire intensity, and mean rate of spread at a fraction of the computational cost (seconds); and (c) domain-specific metrics and counterfactual evaluation protocols to probe out-of-distribution generalization. Integrating geospatial data (fuel, terrain, ignition likelihood) and regional weather, our model approximates BurnP3+ simulation outputs, achieving strong performance across agreement, rank-correlation, error, and spatial-overlap metrics. It preserves downstream hazard classifications and produces physically plausible responses to expert-informed counterfactual interventions. On a representative region, the surrogate achieves 806-fold end-to-end CPU acceleration and uses 13% of BurnP3+'s host memory, facilitating rapid scenario analysis.

---


### 5. [Neural Networks with Differentiable Belief-Function Layers](https://arxiv.org/abs/2610.30173)

**<font color=#1a73e8>作者：</font>** Antonin Sulc  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Yager's 1987 rule of combination $\boxplus$ was proposed on epistemic grounds: under high conflict, mass should be redistributed to ignorance rather than renormalised onto the class simplex. We observe that backpropagation needs the same rule: Dempster's normaliser $(1{-}\kappa)^{-1}$, where $\kappa$ is the conflict mass, puts a $(1{-}\kappa)^{-2}$ term in the gradient that diverges exactly when evidence sources disagree, while Yager's $\boxplus$ is bilinear and has no such term. Building on this, we construct a deep evidential pipeline in which every mass in the chain from heads to output is a valid Dempster--Shafer mass function, combined by Yager's rule. The output mass on the ignorance set, $m(\Theta)$, serves as the network's ``I do not know'' signal. The network is fit to hard labels and never sees an annotator distribution, yet $m(\Theta)$ orders human disagreement in two modalities, visual and linguistic. Dempster's rises too and ranks contested inputs about as well, but its normaliser divides the conflict out: Yager's vacuity is $9\times$ larger on the most contested CIFAR-10H images, so only Yager's is readable as an amount of ignorance without recalibration. For out-of-distribution detection it is competitive with strong single-pass baselines, while the clamped Dempster variant that scores higher becomes gradient-unstable once the clamp is removed.

---


### 6. [When Stable and Preferred Semantics Agree: A Path-Based Approach](https://arxiv.org/abs/2610.30176)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Kehan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate structural conditions under which preferred and stable semantics agree in abstract argumentation frameworks. Our approach is based on suitably chosen sets of paths in the attack graph and binary relations induced by them. We establish a general path-based criterion for semantic agreement and instantiate it with several classes of paths, obtaining sufficient conditions expressed in terms of well-foundedness of the corresponding relations.
The resulting conditions strictly generalize two principal structural criteria for preferred and stable agreement in the literature: Dung's limited controversiality condition and the SCC-symmetry condition. In particular, Dung's result is recovered as a special case by taking the relevant path set to be the set of even paths. We further introduce two infinite sequences of path sets, each yielding a family of agreement conditions. For the first sequence, a Collapse Theorem reduces the infinitely many associated well-foundedness conditions to three essentially distinct ones, whereas the second sequence gives rise to genuinely distinct conditions with no analogous collapse. Our results apply to both finite and infinite argumentation frameworks, admit simplified formulations in the finite case, and also yield sufficient conditions for the existence of stable extensions.

---


### 7. [Detecting AI Training in Datacentre Power](https://arxiv.org/abs/2610.30182)

**<font color=#1a73e8>作者：</font>** Tom Kimpson, Mauricio Baker, Emlyn Graham  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI governance agreements require methods to detect large model training runs on a monitored computing cluster, without trusting the operator. We develop a method to detect synchronous model training in facility-level power by Viterbi tracking of the wandering iteration cadence. On simulated datacentre power, when the operator makes no attempt to hide, the Viterbi tracker detects at least $96\%$ of training runs against a declared inference workload, at a $1\%$ false-alarm rate and within $0.04$ of the Neyman--Pearson optimum, given a meter that samples at $2$ Hz or faster. Of eight adversarial strategies an operator might use to hide, only extreme variation of the work per iteration evades the tracker. Its strongest form hides training in up to $73\%$ of five-minute observations, but over a day at least $87\%$ of such runs are still caught, at a $0.1\%$ false-alarm rate per run. This adversarial strategy costs no throughput, but in small-scale training the operator needs $93$--$267\%$ more compute to reach the same loss. A modest passive meter is sufficient to make hidden training both detectable and expensive, which makes power metering a promising part of compute verification that does not depend on trusting the operator.

---


### 8. [When EVM Defaults Break: Three SDK Patterns for UTXO-Family Wallets](https://arxiv.org/abs/2610.30183)

**<font color=#1a73e8>作者：</font>** Hanzheng Zhang, Hongzhou Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mainstream Web3 SDKs (e.g., this http URL, viem) bundle three coupled assumptions: an account-based ledger, a single secp256k1 signer, and input-selection-free transaction construction. These assumptions fail once a chain adopts an extended-UTXO model (here, the Cell model on Nervos CKB), and once the wallet population spans heterogeneous cryptographic primitives (secp256k1, WebAuthn, Schnorr). Using CKBers' Codebase (CCC), a TypeScript SDK, this retrospective case study extracts three recurring patterns from release history and exported APIs: a Transaction Composer that makes capacity-aware input completion and fee estimation declarative, a Unified Signer Abstraction that normalizes signing across heterogeneous wallets behind one interface, and a Connector UI component that ships per-wallet onboarding as a drop-in. The contribution is the articulation of these patterns as transferable design lessons for SDKs targeting UTXO-family ledgers and heterogeneous wallet populations.

---


### 9. [Spectral Uncertainty Decomposition for Sparse Bayesian Learning](https://arxiv.org/abs/2610.30207)

**<font color=#1a73e8>作者：</font>** Ismail Huseynov, Stefan Haufe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating distributed neural sources from M/EEG measurements is an ill-posed inverse problem where principled uncertainty quantification remains challenging. The usual conditional Gaussian posterior covariance does not explicitly distinguish uncertainty along likelihood-visible source directions from uncertainty that is invisible to the measurements. We propose a spectral framework based on the singular value structure of the prior-preconditioned forward operator, which provides an exact, interpretable decomposition of the posterior covariance into data-informed and indeterminacy epistemic components. This formulation identifies uncertainty contributions that are reducible by better measurements from those that are fundamentally irreducible by sensing geometry. We further derive an equivalent subtractive decomposition that expresses the prior covariance as the sum of posterior and data-driven reduction terms, enabling precise accounting of uncertainty reduction through Bayesian learning. Together, these complementary representations offer both theoretical insight and practical tools for interpretable uncertainty quantification in M/EEG source imaging for linear-Gaussian Bayesian inverse solvers where the posterior covariance is available in closed form.

---


### 10. [Prediction Is Not Calibration: Item Parameter Recovery and Representation Coupling in Knowledge Tracing](https://arxiv.org/abs/2610.30211)

**<font color=#1a73e8>作者：</font>** Wenrui Yuan, Stéphanie M. van den Berg, Johannes Steinrücke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) models can estimate item parameters through an item response decoder trained solely for next-response prediction, yet predictive accuracy does not guarantee parameter recovery. We study 2PL, GPCM, and NRM decoders paired with LSTM, Transformer, and DKVMN encoders. Response-model derivatives show why discrimination and option slope updates depend directly on the scale and spread of estimated ability. Affine logit identities show how item-dependent shifts and rescaling in estimated ability are absorbed into item parameters without changing response probabilities. In simulations, difficulty, mean threshold, and correct-option intercept recovery remain high under shuffled order across representation widths, whereas discrimination and keyed option slope contrast recovery require wider item representations and degrade further under fixed item order. Separating the sequence item representation (width $d_S$) from the item parameter key (width $d_M$), and pairing a wide key with a thin sequence representation ($\mathrm{SK}(64,8)$), reduces fixed-order ability distortions and improves recovery and cross-order consistency without sacrificing test accuracy or increasing model size relative to a shared width-64 baseline ($\mathrm{SH}(64)$). On TIMSS and EdNet, widening $d_M$ consistently improves agreement with an offline IRT reference, while the trade-off from narrowing $d_S$ depends on the encoder's reliance on sequence width for prediction. These findings show why item parameters, especially discrimination and option slopes, must be evaluated separately from response prediction.

---


### 11. [When Reconstruction Is Not Enough: Doubly Robust Counterfactual and Interventional Mediation Analysis with Learned Multimodal Representations](https://arxiv.org/abs/2610.30220)

**<font color=#1a73e8>作者：</font>** Cong Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations of high-dimensional multimodal health records are increasingly used to adjust for confounding, yet they are usually trained to reconstruct the data rather than preserve the information that causal identification requires. We study counterfactual outcomes under alternative treatments, including phenotype-specific effects and patient-level counterfactual risk profiles of the kind digital twins provide, and interventional direct and indirect effects under exposure-induced intermediate confounding. We give conditions under which a representation preserves identification and show that interventional mediation is more demanding than counterfactual comparison. We prove that no covariate-only training objective, whether reconstruction, contrastive, or physics-informed, can certify that a representation is sufficient, and that, in a linear structural model, a representation can lose arbitrarily little reconstruction accuracy yet induce arbitrarily large bias. We decompose the error of cross-fitted doubly robust estimators into a first-order representation bias, which neither double robustness nor cross-fitting removes, and a second-order remainder of nuisance-estimation errors, so coverage worsens as the sample size grows when the representation is insufficient. We propose a workflow combining modality-specific variational autoencoders trained outside the estimation sample, cross-fitted doubly robust estimators, locked phenotypes, select-then-confirm pathway analysis, portable representations, and diagnostics for representation insufficiency, exposure leakage, and sensitivity. In simulations, discarding a rare, moderately strong confounder gave indirect-effect intervals with 2% coverage at n = 3,000; reconstruction loss missed the problem, and a simple predictive diagnostic flagged it in every replicate.

---


### 12. [GANet: A Lightweight Group Attention Network for Plant Disease Identification on Embedded Systems](https://arxiv.org/abs/2610.30225)

**<font color=#1a73e8>作者：</font>** Anubhab Tripathi, Bibek Das, Asfak Ali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global warming and climate change are major catalysts for plant diseases, significantly affecting food production worldwide. Addressing this issue requires continuous monitoring and early detection of plant diseases. While recent advancements in deep learning offer potential solutions, most models demand high processing power and struggle to perform efficiently on low-end electronic hardware. Furthermore, many existing works focus on specific crop diseases, limiting their broader applicability. This paper presents a lightweight Group Equivariance Attention Network (GANet) designed for the prediction and monitoring of 38 types of plant diseases. GANet introduces a novel Group Attention block and Group-Wise Feature Fusion block, making it both sparse and efficient. With only 0.001M parameters, the model achieves an impressive 99.99% accuracy on the PlantVillage dataset. Additionally, GANet is optimized for deployment on edge devices such as the Raspberry Pi 4b and Jetson Nano, where it reaches 5 FPS and 11 FPS, respectively, demonstrating its potential for real-time plant disease monitoring on low-power devices.

---


### 13. [Benchmarking Model Compression Techniques Across Heterogeneous Edge Platforms: A Predictive Maintenance Use Case for Rotating Machinery](https://arxiv.org/abs/2610.30228)

**<font color=#1a73e8>作者：</font>** Matheus Calheira Guimarães de Oliveira, Marco Aurélio da Silva Cruz, Regis Cardoso 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To enable Industry 5.0, where autonomous systems are widely adopted and integrated with people to promote sustainable development in industries, it is imperative to adapt complex deep learning models to operate efficiently on resource-constrained hardware for edge inference. However, adapting these models remains challenging due to the hardware heterogeneity of edge computing in industrial settings, performance degradation caused by model compression, and the lack of clear guidance on which compression techniques are practical and effective for applications such as predictive maintenance. To address these challenges, this paper presents a comprehensive comparative analysis of four state-of-the-art model compression techniques applied to a high-performance convolutional neural network for predictive maintenance using a real-world dataset of rotating machinery, equipment typically used in industry. The compressed models were evaluated across a heterogeneous set of nine computing platforms, ranging from highly constrained edge computing devices to general purpose and high-performance processors, reflecting the diversity and fragmentation typical of industrial edge environments. By jointly prioritizing classification performance, inference speed, and compression ratio, we found that compression using knowledge distillation emerged as the most effective approach. The model had more than 90% speedup across all devices while maintaining a 91.22% balanced F-score, with a very small drop in predictive performance relative to the uncompressed model, along with a 98.9% size reduction. Through successful deployment across multiple edge platforms and a systematic comparison of compression strategies, we demonstrated a clear path to achieving Industry 5.0 targets, drastically cutting computational costs and, consequently, energy consumption without sacrificing predictive performance.

---


### 14. [Automated screening of privacy risks in medical AI](https://arxiv.org/abs/2610.30229)

**<font color=#1a73e8>作者：</font>** Konstantinos Vrettos, Eleftherios Tzanis, Haridimos Kondylakis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical artificial intelligence (AI) models are often shared without their training data, assuming this protects the patients who contributed them. However, a model can reveal whether a patient's records were used in training, a privacy breach known as a membership inference attack. This risk is usually reported as a cohort average, which can appear negligible while individual patients are almost certainly exposed. Identifying potentially vulnerable records before developing a production model could make privacy assessment more practical. We measured each patient's vulnerability to membership inference attack, across 7,789 models trained on six clinical datasets in four modalities, including two adapted pretrained medical models. Training choices changed how many patients had high attack scores, but the patients who ranked highest by risk largely stayed the same across the configurations we tested. Stronger weight decay reduced the exposed cohort up to threefold, yet largely the same patients remained most at risk across training recipes, architectures and initializations, including foundation models. Therefore, we developed a lightweight screening tool that uses four small models to identify patients with high risk of exposure before production-model training. We also assessed if flagged patients could be protected without removing their data. Privacy screening should become incorporated into data preparation for clinical AI.

---


### 15. [Breaking the high-degree barrier in Lehmer's problem with a human-AI discovery loop](https://arxiv.org/abs/2610.30277)

**<font color=#1a73e8>作者：</font>** Yuri Chervonyi, Sergei Gukov, Thang Luong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While artificial intelligence has made rapid progress in mathematical reasoning, many open problems depend on structure that is revealed only through large-scale computational exploration and analytical synthesis. One such example is Lehmer's problem from 1933. It asks whether the Mahler measure of an integer polynomial, which measures how far its roots stray from the unit circle, can be made arbitrarily small. Previously, constructing irreducible polynomials with integer coefficients and small Mahler measure has been carried out systematically only for even degrees $d \le 180$. At higher degrees, Boyd's analytical one-parameter family frequently factors, skipping nearly 50% of target degrees and leaving no general construction for arbitrary $d$. Here, we address the high-degree regime through a human-AI discovery loop, in which we extend the conversational prompting with a fast numerical pipeline, an exact symbolic verifier, and large-scale distributed search. The AI agent prototypes numerical and symbolic solvers locally, launches parallel searches across distributed clusters and works with the human researcher to extract and verify mathematical hypotheses. Through this interactive loop, we derive a five-parameter construction, which we call the Generalized Boyd algorithm. It eliminates degree-skipping and constructs irreducible polynomials with Mahler measure strictly below Boyd's limit point $\alpha_1 \approx 1.255434$ for every target degree. Evaluated across all even degrees up to 2000, our approach improves upon six previously published values and holds 99.6% of all best known records. With this work we release the verified dataset of polynomials with minimal Mahler measure across all studied even degrees.

---


### 16. [Generalizing Metropolis-Hastings for DAG Sampling](https://arxiv.org/abs/2610.30291)

**<font color=#1a73e8>作者：</font>** Daniele Nikzad, Mikko Koivisto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in Bayesian network structure learning lies in efficiently approximating the posterior distribution of directed acyclic graphs (DAGs). For large, high-dimensional datasets, the task remains beyond the capabilities of current methods. This work advances Markov chain Monte Carlo algorithms by introducing novel moves that simultaneously resample the parents for multiple nodes of the DAG. At the core of these moves is duet sampling, a new generalization of the Metropolis-Hastings algorithm that selects two proposal distributions from a pool at each iteration. One is used for generating a candidate state of the Markov chain and another for evaluating the return to the current state; both are ingredients of an appropriately crafted acceptance criterion. Pairing different proposal distributions provides additional freedom and enables constructing Markov chains that mix more efficiently than their basic Metropolis-Hastings counterparts, at no additional computational cost. Experiments show that our new moves, both individually and in combination, outperform the previous state of the art, which relies on a more restrictive pool of moves. This advantage persists even when letting the previous methods leverage duet sampling to enhance their performance.

---


### 17. [EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video](https://arxiv.org/abs/2610.30293)

**<font color=#1a73e8>作者：</font>** Chao-Yeh Chen, Tiffany Chen, Lin Duan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EgoHand, a monocular 3D hand reconstruction model that achieves state-of-the-art performance on egocentric video. Central to our approach is the curation of a high-quality training corpus of 14 million images, combining synthetic data, in-the-wild video, and multi-camera motion capture to balance scene diversity and supervision quality. The model adopts SOMA-Hand as its parametric representation and processes 2D hand crops with a transformer encoder, incorporating camera cues and an auxiliary 2D branch to improve geometric consistency and image alignment. Zero-shot evaluations on HOT3D, ARCTIC, and H2O demonstrate strong out-of-domain generalization, with lower joint-position, root-translation, and acceleration errors than competing baselines at an inference latency of approximately 9.69 ms. A blinded user preference study further shows that participants favor EgoHand's reconstructed hand poses over those from Apple EgoDex and Ropedia Xperience-10M. We release the EgoHand model and source code under the OpenMDW license, allowing free commercial use of the model.

---


### 18. [MoRE: Motion-Regularized Encoding for Articulated 3D Generation](https://arxiv.org/abs/2610.30337)

**<font color=#1a73e8>作者：</font>** Guantian Zheng, Shan Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating an articulated object from a single image requires recovering both its appearance and the mechanism governing its parts. A compact encoding of joint attributes does not by itself ensure that reconstruction preserves the resulting motion. We present MoRE, Motion-Regularized Encoding for articulated 3D generation. MoRE represents coordinate-aligned joint lines with axis classification and two axis-orthogonal Plücker moment coefficients, removing the arbitrary choice of an origin along the axis. During representation learning, decoded joint hypotheses are used to move corresponding three-dimensional anchors, and their motions are compared with those of annotated joints. A differentiable expectation over joint types and axis directions couples attribute reconstruction to the motion it induces. An image-conditioned flow learns the resulting functional latents, while a multi-state-adapted Gaussian model supplies appearance. At inference, recovered part assignments and joints articulate a single set of rest-pose Gaussians without regenerating the object for each state. Experiments on PartNet-Mobility and ACD show stronger part-box agreement, articulated-state geometry and visual similarity than the compared baselines, while joint prediction reduces axis, origin and range errors relative to ArtiLatent. Controlled ablations support the joint-line encoding and show that motion supervision reduces anchor-motion error. Code and pretrained checkpoints will be released in the future.

---


### 19. [Spike-Aware Gradient-Based Mixed-Precision Quantization of Spiking Neural Networks for Vision Applications](https://arxiv.org/abs/2610.30339)

**<font color=#1a73e8>作者：</font>** Rajshekhar Rakshit, Devgokul B.V, Rakshitha Kalkura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, Spiking Neural Networks (SNNs) have gained massive attention as an energy-efficient neural computing paradigm due to their event-driven and sparse computing capability. However, maintaining accuracy under low-precision constraints, necessary for practical deployment, has been largely unexplored for SNN models. In addition, existing Hessian-based approaches for quantization, such as HAWQ-V2, incur significant memory and computational overhead due to temporal unrolling across multiple SNN timesteps. We propose a spike-aware gradient-based mixed-precision quantization framework for SNNs that adaptively assigns bit-widths using first-order gradient information, avoiding costly second-order Hessian computations. We evaluate our method across various SNN-based architectures, including VGG, ResNet, and Vision Transformer models obtained from both ANN-to-SNN conversion and direct training frameworks, on CIFAR10/100, ImageNet, and DVS-CIFAR-10 datasets. Notably, on ResNet-34 evaluated on ImageNet, our method achieves 73.30% accuracy at 4.78$\times$ compression, which is comparable to that provided by HAWQ-V2, while reducing memory consumption by 2.31$\times$ and bit-allocation runtime by 100$\times$. We also present an energy analysis for mixed-precision SNNs showing that the proposed quantization strategy enables energy-efficient deployment without compromising performance.

---


### 20. [Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles](https://arxiv.org/abs/2610.30340)

**<font color=#1a73e8>作者：</font>** NVIDIA, Sérgio Agostinho, Maximilian Apodaca 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Foundation4D, a unified feed-forward model for geometry estimation, 3D detection, semantic occupancy, and Gaussian reconstruction from multi-camera driving video. A shared backbone uses factorized spatiotemporal attention to efficiently combine observations across cameras and time. Our video inference pipeline uses pose graph optimization to refine camera trajectories and assembles object tracks across input windows. We also develop a data annotation pipeline and release PAI-Foundation4D, a benchmark with dense depth and semantic occupancy labels for 1,253 driving clips. With benchmark-specific fine-tuning, Foundation4D achieves the lowest depth AbsRel on Waymo and nuScenes, the highest detection mAP on nuScenes, and the highest occupancy mIoU on OpenOccupancy among the compared methods. Our task-combination study shows benefits for both detection and geometry: co-training detection with geometry and occupancy improves top-class mAP by 1.2 points over detection-only training, while co-training geometry with detection reduces camera-to-rig translation error by $13.4\%$ relative to geometry-only training. We further use the predicted geometry and trajectories as priors for lidarless NuRec, supporting reconstruction of driving scenes for simulation.

---


### 21. [FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking](https://arxiv.org/abs/2610.30347)

**<font color=#1a73e8>作者：</font>** Yash Kulthe, Vishal Asnani, Shruti Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose FiLM-CAM; a conditional-access image watermarking approach that enforces authorized encoding, decoding, and removal through keyed feature modulation. A secret key conditions a Feature-wise Linear Modulation (FiLM) mechanism that transforms the internal representation of the watermark signal before embedding, thereby coupling the payload to the key at the feature, rather than pixel level. The same key must be presented to condition the decoder to correctly recover the payload embedded in an image. To enforce conditional access, we train the system to maximize the performance gap between authorized and unauthorized use, ensuring reliable extraction under the correct key while inducing failure under incorrect keys. In addition, we design our encoder to estimate the watermark residual invariant to the presence of pre-existing watermarks. This design enables conditional watermark removal via simple re-encoding and subtraction of the residual using iterative refinement, contingent on knowledge of the secret key. We evaluate FiLM-CAM across multiple watermarking encoder-decoder backbones, demonstrating that keyed feature modulation serves as an effective, architecture-agnostic conditional access module (CAM) for image watermarking.

---


### 22. [Mirage: Targeted Jailbreaks Against Post-Generation Safety Checkers in Multimodal Diffusion Models](https://arxiv.org/abs/2610.30348)

**<font color=#1a73e8>作者：</font>** Shanghao Shi, Chaoyu Zhang, Heng Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-generation safety checkers are widely employed in diffusion-model pipelines to prevent unsafe generated content from reaching users. In this paper, we show that these safety checkers can still be bypassed by our proposed multimodal jailbreak attack, Mirage. Given an adversarial target, which can be either a reference NSFW image or a malicious text description, Mirage conceals the target within an imperceptible perturbation applied to a benign input image. Mirage exploits the shared representation space of multimodal encoders to jointly align the perturbed image with the cross-modal adversarial target while repelling its representation from commonly filtered NSFW concepts. Such semantic separation can transfer across representation spaces, enabling Mirage to evade heterogeneous safety checkers without accessing their internal details. We further employ lightweight black-box query refinement to improve evasion near the unknown safety boundary. We implemented Mirage on Stable Diffusion 1.5, Stable Diffusion XL, and Kandinsky 2.2, and evaluated it on two cross-modal NSFW datasets, covering both text-to-image and image-to-image generation scenarios. The experimental results demonstrate that Mirage achieves strong targeted jailbreak performance across diverse post-generation safety checkers with limited black-box queries while preserving high semantic alignment with the adversarial targets.

---


### 23. [Who Patches the Lightning Network? Evidence from Release Lines in Gossip, 2023-2026](https://arxiv.org/abs/2610.30350)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Every implementation of Bitcoin's Lightning payment network disclosed security vulnerabilities in 2026, and every advisory told operators to upgrade. Whether they do has never been measured, because Lightning gossip carries no software version. Matching the feature bits a node announces against the source of every LND, Core Lightning, Eclair and LDK release, we show that gossip reveals a node's release line after all. Where Core Lightning nodes state their version, the inferred line is exact for 132 of 136 node-line pairs. Across 814 daily snapshots of the public graph from 2023 to 2026, the network patches on release and platform schedules, not on disclosures. Half of LND nodes upgrade within 88 days of a release; small nodes and those that skipped releases lag far behind. The three largest upgrade waves came about a day after the Umbrel app store shipped a new LND version. Since June 2025, 17% of LND upgrades came in the 48 hours after a platform release, windows that cover 4.4% of the time. Disclosures, a median 256 days after the fix, moved few operators: of 12 we can test, only Core Lightning's of July 2026 sped up upgrades, and only among nodes one release line behind. Its later call to restart offline was followed mostly by nodes already patched. Two months after Lightning Labs' August 2026 batch, 71% of the LND nodes exposed at disclosure still ran an affected release. For maintainers, the lever on the nodes that lag is the platforms that package their releases.

---


### 24. [Exploring spatial configuration and group familiarity when co-watching 360-degree stories in social virtual reality](https://arxiv.org/abs/2610.30353)

**<font color=#1a73e8>作者：</font>** Portia Wang, Monique Santoso, Yujie Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While traditional cinematic viewing is often characterized as a social experience, engaging with immersive stories is predominantly researched as an individual activity. This mismatch becomes increasingly problematic in social virtual reality (VR), where features designed for typical social activities (e.g., virtual locomotion, spatial and social context) can become meaningful levers for shaping the user experience. To address our limited understanding of these effects, we conducted three exploratory experiments (N$_1$=109, N$_2$=116, N$_3$=88) examining how spatial boundary type, size of allocated personal space, and group familiarity influence co-watching 360-degree stories in social VR. Results shows that small communal spatial boundaries heightened social presence towards others compared to individual boundaries, but also increased mental demand. Reducing the size of the personal spatial boundary increased social presence towards others but also increased disorientation and frustration. Finally, participants with higher group familiarity reported stronger attentional focus on the story, as well as higher spatial presence and social presence towards story characters, but also reported greater physical and perceptual demand. We discuss systematic tradeoffs between engagement and cognitive effort, and suggest practical guidelines for designing shared immersive narrative experiences.

---


### 25. [CTRL-FM: Inference-Time Structural Control for Flow-Based Virtual Sensing under Long-Horizon Node Outages](https://arxiv.org/abs/2610.30362)

**<font color=#1a73e8>作者：</font>** Boshra Khalili, Andrew Smyth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon node outages are harder than conventional missing-value imputation because complete sensor trajectories remain unobserved for extended periods, while the usefulness of spatial and temporal dependencies varies across outage locations and operating regimes. Existing graph, diffusion, and flow-based methods typically impose a fixed structural bias, which can oversmooth abrupt changes or propagate errors from unreliable neighbors. We introduce CTRL-FM, an observation-preserving flow-matching framework that treats structural guidance as an outage-conditioned inference-time decision. A missing-only flow-matching backbone learns a conditional velocity field while keeping observed measurements exactly fixed. For each realized outage, CTRL-FM constructs self-supervised proxy outages from surviving measurements and uses their known values to select among uncontrolled, graph-dominant, temporal-dominant, and balanced control policies. The selected policy is locally modulated by graph and temporal reliability estimated exclusively from surviving observations, while boundary-anchored trends provide structural guidance. Control is applied only to missing entries and is rejected when proxy evidence does not sufficiently improve over uncontrolled sampling. Across PeMS08, METR-LA, Air-36, and AQI, CTRL-FM achieves the strongest overall performance under 30% and 60% node outages. Stress tests with up to 75% sensor loss further show graceful degradation and consistent gains over training-time and fixed structural control. These results demonstrate that validating, selecting, and locally adapting structural guidance for each realized outage is more effective than imposing a single global structural prior.

---


### 26. [Climbing the Ladder: Automating Data Pipelines and Reproducing Baselines in Low-Resource Settings](https://arxiv.org/abs/2610.30374)

**<font color=#1a73e8>作者：</font>** Donato Meoli, Eryk Wdowiak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The massively multilingual translation systems that now include Sicilian learned it from noisy, non-standardised web text. To obtain better translation quality, we redevelop the small neural machine translation (NMT) system that Wdowiak customized for Sicilian. We rebuild on maintained software the extraction of the parallel text from the PDFs of the bilingual journal Arba Sicula, whose sentences are aligned by a language-agnostic sentence encoder with thresholds tuned against an existing hand alignment and then filtered for the typical errors of automatic alignment. Furthermore, the tokenization and the desinence-biased subword segmentation of the original system are ported to a Perl-free implementation, and all the results are measured on a frozen test set drawn from the journal. We compare small Transformers trained from scratch with the pretrained NLLB model adapted by low-rank fine-tuning, in both directions and with Italian as a closely related bridge language, and we adapt to the pretrained model the reverse-training recipe of the original system, i.e., a stage on forward-scored back-translations of the web Sicilian followed by a stage on the curated literary text. The pretrained model is by far the better of the two, and the staged training improves the translation into Sicilian more than the translation from it. On the test set of the original system, and in the tokenized space in which it was scored, the staged model with a larger adapter and more back-translations is above the reverse-training recipe in the directions that involve English and below it between Sicilian and Italian. Yet, a multilingual adapter degrades the directions on which it was not trained, which limits its use as a general multilingual model.

---


### 27. [Rank Ceiling for Twiddle-Perturbation Faults on the Forward NTT](https://arxiv.org/abs/2610.30383)

**<font color=#1a73e8>作者：</font>** Chakshu Gupta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> NIST standardised ML-KEM and ML-DSA in 2024 for post-quantum key establishment and digital signatures. Both compute forward number-theoretic transforms (NTTs) on secret polynomials. Published attacks zero every fixed multiplier, or twiddle, during Kyber key generation with a single fault, or individual twiddles in one Dilithium signing variant; countermeasures detect or mask these faults. Nonzero replacements preserve invertibility, but the uncompressed correct-minus-faulted transform difference can still expose input information. This paper characterises the linear map from a secret polynomial to this difference under arbitrary static twiddle replacements, including bit-flips. For one fault, rank equals the number of butterflies sharing its twiddle, halving by layer from 128 to 2 for ML-KEM and to 1 for ML-DSA. Known positions, replacement values and the difference determine that many independent linear combinations of input coefficients. With one fault per layer, all but the constant and linear coefficients for ML-KEM, or the constant for ML-DSA, are determined; Lean 4 certifies this rank-and-kernel result. Those coefficients cancel for every fault set and choice of replacement values. NIST permits seed storage, motivating comparison of a known correct key with a released faulty key from the same seed. If only one ML-KEM secret-polynomial NTT is faulted, the key difference is a known matrix column times the transform difference; an invertible column entry reconstructs the latter. For ML-DSA, neither reconstruction nor the number of secret-polynomial candidates from compressed key differences is established. The per-layer ranks give a closed-form measure of raw exposure for countermeasure design.

---


### 28. [Bayesian Fixed-Confidence Best-Arm Identification with Abstention](https://arxiv.org/abs/2610.30384)

**<font color=#1a73e8>作者：</font>** Yuqi Huang, Yunlong Hou, Vincent Y. F. Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the Bayesian fixed-confidence best-arm identification problem in which a learner can abstain from making a terminal recommendation. Subject to a target error probability $\delta$ and an abstention budget $\alpha$, we propose Screen-and-Confirm (S&C) and analyze its expected stopping time. We further derive the minimum expected stopping time for any algorithm that satisfies these constraints. For Gaussian priors and rewards, as $(\delta,\alpha)\downarrow(0,0)$, we establish matching upper and lower bounds up to multiplicative constants, with rate $\kappa_\nu^2[1+\log((\alpha+\delta)/\delta)]/(\alpha+\delta)$, where $\kappa_\nu$ is the prior density of the top-two gap at zero, highlighting that nearly tied instances govern the sampling cost. When abstention is disallowed ($\alpha=0$), S&C yields the optimal $\Theta(1/\delta)$ dependence for fixed model parameters, removing the additional $\log(1/\delta)$ factor in the upper bound of Jang et al. (2024) under our Gaussian assumptions. We further characterize the exact multiplicative constant of the minimum expected stopping time for practical regimes including (i) fixed $\alpha \in (0,1)$ and (ii) $\alpha/\delta\to\infty$, which are also achieved by S&C.

---


### 29. [Latent Space Jam: Layout Guided Video Synthesis](https://arxiv.org/abs/2610.30390)

**<font color=#1a73e8>作者：</font>** Asaf Joseph, Moshe Mandel, Ohad Fried  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adding control to video generation often requires training, which demands additional computational resources, data, or architectural changes. We propose a training-free approach that utilizes pretrained video diffusion models to control object layout and motion using coarse layouts. Our method operates in two passes: first, it steers spatiotemporal placement through prompt-guided cross-attention to produce a coarse visual guide; second, this guide conditions the same model to generate a high-quality, layoutconsistent video. The approach enables coordinated motion with strong temporal consistency, supporting diverse trajectories and object interactions without additional training. Extensive experiments show that our method consistently outperforms prior work in overlap and trajectory accuracy, as well as visual quality across static, dynamic, and multi-object scene settings.

---


### 30. [Soft Ontology Priors over Latent Concept Posteriors for Weakly Supervised Neuro-Symbolic Learning](https://arxiv.org/abs/2610.30391)

**<font color=#1a73e8>作者：</font>** Tengwei Song, Robert Hoehndorf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuro-symbolic (NeSy) predictors that supervise only the task label suffer from reasoning shortcuts: distinct concept mappings achieve the same maximum likelihood, leaving the recovered concepts unidentifiable and unsafe for downstream reuse. We attack this failure by injecting a soft ontology prior over the latent concepts into the training objective and compiling it together with the task constraint into a smooth, decomposable probabilistic circuit. Under independent Bernoulli perception, the normalisers of the resulting structured concept posterior reduce to weighted model counts that are linear in the compiled circuit size, because the neural leaf weights fold into the circuit before evaluation. The soft compilation strategy places expert axioms in the circuit's weights rather than its support (task-structural axioms guaranteed by the data-generating process stay hard), so noisy expert axioms only redistribute prior mass and cannot empty the support. We characterise how the prior reweights label-restricted shortcut mass through differences in ontology violation energy, show that soft priors incur bounded log-density perturbations under bounded axiom noise, and prove that the hard-support counterpart can be made degenerate by a single corrupted axiom. We validate these predictions on an audited six-concept view of the real-world BDD-OIA driving benchmark and on controlled NeSy tasks.

---


### 31. [Escaping the Phylogenetic Trap: Persistent Homology Enables Cross-Species Ion Channel Classification via Multimodal Graph Neural Networks](https://arxiv.org/abs/2610.30394)

**<font color=#1a73e8>作者：</font>** Arezoo Bybordi, Favour Achimba, Mariam Gelashvili 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein classifiers are highly sensitive to evaluation protocol: random train/test splits induce phylogenetic leakage, allowing models to exploit taxon-specific correlations and substantially overestimate out-of-distribution performance. This issue is particularly acute for venom compound classification by ion-channel target (Ca2+, K+, Na+), where reported accuracies of 80-90% do not reflect generalization to unseen taxa. We formulate cross-species prediction as a structured distribution shift in which taxonomic identity acts as a confounder, requiring representations that capture structural features invariant across phylogeny. Using a shared multimodal backbone that fuses ESM-2 sequence embeddings with a disulfide-aware graph attention network, we systematically compare five structural inductive biases (spectral, Riemannian, SE(3)-invariant, statistical-manifold, and persistent-homology representations) under a leave-one-taxon-out evaluation protocol on a benchmark of 1,373 ColabFold-predicted venom compounds spanning five taxa. The persistent-homology representation summarizes backbone geometry through topological descriptors that are robust to local structural perturbations, providing an inductive bias toward phylogenetically invariant learning. Under conventional i.i.d. splits, all models achieve similar accuracy (81-86%), masking differences in inductive bias. Under taxonomic shift, this parity collapses: a sequence-only baseline drops to approximately 30%, the remaining geometric priors cluster at 54-55%, while our persistent-homology model (PH-GNN) achieves 63.4%, outperforming the next-best method by over 8 percentage points. These results demonstrate that random-split evaluation obscures meaningful differences in representation quality and identify topological representations as an effective inductive bias for learning under structured biological distribution shift.

---


### 32. [HAWC-Leak: Heterogeneous Architecture Workload Classification utilizing Side-Channel Leakage](https://arxiv.org/abs/2610.30400)

**<font color=#1a73e8>作者：</font>** Muhtasim Alam Chowdhury, Arthur Kim, Rozhin Yasaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern heterogeneous computing platforms, which integrate general-purpose processors with specialized accelerators such as FPGAs, have become the standard for high-performance and embedded applications. However, the shared physical resources of these systems introduce critical security vulnerabilities, where power consumption patterns can leak sensitive runtime information. While side-channel analysis is well established for extracting cryptographic keys from isolated algorithms, existing methods struggle to profile complex, dynamic systems where diverse workloads coexist on shared hardware resources. This paper presents HAWC-Leak, a dynamic workload classification framework designed to identify specific hardware accelerator tasks in real time using non-invasive power analysis. Unlike prior studies focused on extracting cryptographic secrets from isolated implementations, our approach profiles heterogeneous runtime behavior using machine learning to predict active workloads from features extracted from power traces. We implement a complete hardware-in-the-loop measurement testbed using the ChipWhisperer CW305 Artix-7 FPGA platform to capture high-resolution power signatures of diverse workloads including Advanced Encryption Standard (AES-128), Elliptic Curve Cryptography (ECC P-256), Secure Hash Algorithm (SHA-256), Convolutional Neural Network (CNN), and a system idle state. We develop a Hierarchical Random Forest classifier that processes real-time power data to identify the executing application in controlled mixed-activity scenarios where multiple accelerators are instantiated but only one executes at a time. Experimental results demonstrate that this framework achieves 100% classification accuracy across all evaluated scenarios, confirming that power consumption patterns serve as a reliable and distinctive fingerprint for profiling heterogeneous runtime behavior.

---


### 33. [VisCurate: Evaluating Behavioral Equivalence of Visual Skills](https://arxiv.org/abs/2610.30405)

**<font color=#1a73e8>作者：</font>** Md Farhan Ishraq, Md Farhan Ishmam, Reaz Hassan Joarder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision-based agents have shifted toward skill-based problem-solving, where a skill is an executable image-to-image operation, e.g., cropping, thresholding, or edge detection. As these skill libraries grow, they accumulate duplicated, mislabeled, and defective skills. The signals normally used to curate them (a skill's name, description, or source code) say little about how the skill visually changes the image. We present VisCurate, a framework and benchmark that curates visual skill libraries from observed execution rather than from text. VisCurate runs each candidate skill pair on a shared probe battery and assigns one of six behavioral relations, each tied to a library edit that is safe to make. The benchmark injects seven defect types into a clean library at controlled rates, producing 300 reproducible instances with ground-truth relations and repairs. While text baselines accept up to five of six false merges on hard negatives, our verifier accepts none and recovers 51.2% of the pairs that are truly mergeable. On two real, uncurated libraries, VisCurate finds that 92% of the skills a package shares with its downstream copy are redundant, while execution confirms only 10 of 17 published equivalence claims. The curation problem also remains open, as the strongest of the nine automated curators recovers only about half of the repairs. We emphasize that visual skill libraries should be curated by behavior, not by description.

---


### 34. [AcoustiPrint: Physics-Guided Neural Design of Manufacturable Acoustic Structures](https://arxiv.org/abs/2610.30411)

**<font color=#1a73e8>作者：</font>** Shanmuka Sadhu, Harshvardhan C. Takawale, Yehia Zakaria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work in additive manufacturing and neural inverse design enables the creation of complex three-dimensional structures to manipulate physical fields, yet these designs must also adhere to discrete, non-differentiable fabrication constraints. Current methods limit the design space by imposing differentiable soft manufacturability loss penalties, or by fixing structures through post-processing, causing a discrepancy between the geometry optimized by the physics model and the final fabricated result. Thus, we present AcoustiPrint, a physics-informed neural architecture for constrained inverse design that represents three-dimensional geometries with an implicit neural representation (INR) and passes each candidate through a printability operator before evaluating its final response. The printability operator executes layer-wise self-support, discrete material selection, and whole-body connectivity, assuring fabrication feasibility. To allow for backpropagation through the discrete non-differentiable operations, we use surrogate gradients for the backward pass and a self-supervised printability objective that progressively drives the INR toward a valid design domain. We demonstrate AcoustiPrint for personalized transcranial focused ultrasound, where inter-patient differences in acoustic properties and head geometry deform wave propagation and requires patient-specific acoustic focusing. AcoustiPrint jointly optimizes three-dimensional geometry and material composition through differentiable wave physics while ensuring manufacturability. Experiments show manufacturable acoustic structures with enhanced focal accuracy and over density-based and phase-based baselines, demonstrating a generalized methodology for neural design through non-differentiable manufacturing constraints and differentiable physics.

---


### 35. [Memory-Augmented Online Test-Time Adaptation for EEG Motor Imagery via Perturbation Consistency and Confidence Calibration](https://arxiv.org/abs/2610.30422)

**<font color=#1a73e8>作者：</font>** Kunkun Zhang, Kehao Wu, Zhitao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, electroencephalography (EEG)-based brain--computer interfaces (BCIs) have gained traction as portable neural measurement systems. However, the practical deployment of these instruments is often hindered by nonstationarity and cross-subject distribution shifts, which lead to significant intersubject inconsistency. Existing adaptation methods remain impractical for real-time measurement scenarios, as they typically require offline access to source or aggregated target data. To address these challenges, this article proposes memory-augmented online test-time adaptation (OTTA) with perturbation consistency and confidence calibration (MOPC), a source-free framework designed to enhance the reliability of BCI instrumentation. MOPC enables the measurement system to update its decoding parameters on the fly during the inference stage, facilitating single-pass adaptation without accessing sensitive source data. We introduce random-mask perturbations to enforce prediction consistency against inherent EEG signal noise and acquisition artifacts. Furthermore, a confidence-calibrated reweighting loss is designed to integrate feature-space similarity, effectively mitigating unreliable pseudolabels and class imbalance during continuous signal acquisition. To ensure system stability and prevent the catastrophic forgetting of established neural patterns, a lightweight memory module is incorporated to regularize parameter updates within a tight latency budget. Evaluated on the BCI IV IIb and OpenBMI datasets, MOPC achieves state-of-the-art performance, outperforming prior methods by 2.22~\% and 3.67~\%, respectively, while keeping the per-trial adaptation latency to approximately 40--60 ms. This study provides a robust, recalibration-free solution for real-time EEG decoding, marking a significant advancement in the precision and usability of practical BCI measurement instruments.

---


### 36. [Secure Agentic AI and Multimodal Intelligence in 6G Communication Systems](https://arxiv.org/abs/2610.30436)

**<font color=#1a73e8>作者：</font>** Satyam Gaba, Devanshu Motwani, Siva Sai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sixth-generation (6G) communication systems are expected to support immersive, intent-driven, and latency-critical services through tight integration of multimodal intelligence, edge computing, and autonomous network control. In this setting, agentic AI systems can reason over heterogeneous inputs, use tools and network functions, coordinate across distributed entities, and adapt to dynamic environments. These capabilities make agentic multimodal intelligence promising for 6G applications such as semantic communications, digital twins, and zero-touch network management, but they also introduce security and privacy risks that extend beyond conventional AI and network security models. Vulnerabilities can propagate across multimodal data pipelines, memory, tools, communication interfaces, and inter-agent coordination loops. We survey multimodal intelligence and agentic AI for 6G cross-layered communication systems from the perspectives of privacy and security. We present a 6G-oriented system view spanning perception, memory, tool use, and multi-agent orchestration; analyze threat models and attack surfaces across sensing, cognition, action, memory, and communication layers; organize existing attacks into a structured taxonomy; and review mitigation strategies including prompt and memory defenses, inter-agent trust mechanisms, secure orchestration, and privacy-preserving learning. We conclude by outlining open research directions for trustworthy multimodal multi-agent 6G systems.

---


### 37. [Towards Faithful Data Selection: Statistical Limits and Scalable Algorithms](https://arxiv.org/abs/2610.30442)

**<font color=#1a73e8>作者：</font>** Ahmed Mehdi Inane, Mahdi Haghifam, Gintare Karolina Dziugaite 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What does it mean to have an optimal data selection algorithm? Optimality is conventionally framed as finding a subset that minimizes the population error of the classifier trained only on that subset. Our starting point in this work is first to show that this goal is information-theoretically impossible unless the data selection algorithm has access to a validation set order-wise larger than the training set. This impossibility result motivates shifting from unverifiable population risk minimization to a one-sided guarantee that we refer to as faithfulness: for any candidate subset, we provide an estimable proxy that upper-bounds the difference between training on the full training data and on only the subset. We model training with the Unadjusted Langevin Algorithm and bound the Kullback--Leibler divergence between subset-trained and full-data-trained parameter distributions by the trajectory-accumulated gradient discrepancy. Minimizing this discrepancy gives a principled way to select a subset. Even though the resulting problem is NP-hard, we propose a swap-based local search that decreases the bound at every accepted step. It can therefore refine the output of any selector without worsening its bound. Finally, we provide experimental results on CIFAR10 and CIFAR100 showing that it matches existing data selection baselines. Implementation of our algorithm and the code for reproducing the results are available at: this https URL.

---


### 38. [SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.30443)

**<font color=#1a73e8>作者：</font>** Zijian Guo, İlker Işık, H. M. Sabbir Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-task generalization is an important yet underexplored problem in multi-agent reinforcement learning (MARL). Many real-world applications require multi-agent systems to generalize across complex, temporally extended tasks with diverse inter-agent coordination requirements. We introduce a specification language that combines temporal-logic task specifications with operators for expressing such requirements. We propose SpecMAGIC, a hierarchical framework that leverages the automaton structure of task specifications for subtask decomposition. A centralized high-level planner identifies and allocates compatible subtask sequences across agents, while decentralized low-level policies execute individual subtasks. This enables zero-shot generalization to new tasks by composing reusable subtask policies according to new specifications, without retraining. We establish soundness and probabilistic completeness of the high-level planner. Experiments on multi-agent navigation tasks show that SpecMAGIC substantially outperforms existing approaches on unseen task specifications and maintains strong performance as the number of agents increases.

---


### 39. [Stability Analysis of Signed Graphs under Structural Perturbations](https://arxiv.org/abs/2610.30444)

**<font color=#1a73e8>作者：</font>** Ning Zhang, Li Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Signed graph learning has emerged as a powerful framework for modeling networks with both positive and negative interactions. While graph-filter-based methods have achieved promising empirical performance on signed networks, their stability under edge perturbations remains less well understood. Existing stability analyses primarily focus on unsigned graphs and do not account for sign-flip perturbations. In this paper, we study the stability of signed graph filters under edge additions, deletions, and sign flips. Our theoretical analysis reveals how signed edge perturbations and node feature correlations jointly determine the learned representation stability. Based on this analysis, we propose a theory-guided perturbation strategy that selects structurally influential signed-edge modifications. Experiments on synthetic and real signed graphs show that the proposed method consistently induces larger embedding drift, polarity change, and downstream link prediction degradation than baselines. These results highlight the importance of \textit{sign-aware} and \textit{distribution-aware} stability analysis for signed graph learning.

---


### 40. [A Three-Pillar Governance Framework for Safe and Trustworthy AI Agents](https://arxiv.org/abs/2610.30445)

**<font color=#1a73e8>作者：</font>** Edward C. Cheng, Jeshua Cheng, Alice Siu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents capable of autonomous decision-making introduce significant challenges related to safety, alignment, accountability, and human oversight. Existing Human-in-the-Loop (HITL) and responsible AI approaches provide important foundations, but many remain fragmented across system design, governance, and operational deployment. This paper presents a Three-Pillar (3P) model and framework for developing safe and trustworthy AI agents through transparency, accountability, and trustworthiness. The framework defines an evolutionary path in which increasing agent autonomy is introduced through progressive validation, structured human oversight, and auditable operational controls. We further describe how the model supports agent lifecycle monitoring, decision traceability, escalation management, and human-agent collaboration within enterprise agentic environments. By integrating oversight principles with operational mechanisms, the proposed framework provides a practical foundation for deploying AI agents that remain aligned with human intent while enabling controlled progression toward higher autonomy.

---


### 41. [aggmetrics: Aggregating Classification Performance Measures for Machine Learning](https://arxiv.org/abs/2610.30456)

**<font color=#1a73e8>作者：</font>** Ronaldo Cristiano Prati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> aggmetrics is a Python package that extends any binary performance measure expressed in the four confusion-matrix counts to multiclass, multilabel, ordinal, cost-sensitive, soft-label and cross-validation settings, by substituting one of four aggregation operators for what libraries usually expose as an average switch. The package also stores, for every measure, the structural properties that decide which identities apply to it, can infer those properties from a user-supplied formula, and uses them to warn when a measure is used where it does not behave as commonly assumed. Its test suite encodes the results of the companion theory as executable tests. The package is BSD-3 licensed, depends only on NumPy, and is available at this https URL documentation at this https URL.

---


### 42. [Short-to-Long: Detached Features for Long-Horizon Value Learning](https://arxiv.org/abs/2610.30461)

**<font color=#1a73e8>作者：</font>** Tong Che, Boris Ivanovic, Marco Pavone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning useful representations from continually changing value targets remains a challenge in deep reinforcement learning. We study the temporal horizon of this supervision: smaller discounts make these targets less sensitive to distant bootstrap changes, but using them for behavior changes the control objective. We introduce Short-to-Long (S2L), which supplies a long-horizon behavior learner with features trained by smaller-discount source networks. Detached connections prevent the behavior value loss from updating the sources, allowing each source to follow its own value objective while the behavior discount remains unchanged. Across Atari, online continuous control, and offline continuous control, the approach yields aggregate performance gains, improving the paired terminal median on 40 of 57 Atari games. Matched Atari ablations support the roles of feature transfer, smaller source discounts, and gradient isolation. Fixed-trajectory measurements further show reduced drift in source value targets with mixed discounts.

---


### 43. [SplatLab: Autonomous Scientific Discovery for 3DGS Research](https://arxiv.org/abs/2610.30468)

**<font color=#1a73e8>作者：</font>** Seemandhar Jain, Manmohan Chandraker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reproducing a published 3DGS paper takes weeks of expert engineering before any extension can be proposed. Prior autonomous-research systems read papers, draft hypotheses, and write code, but are limited by short fixed templates, low executability, and weak traceability, and none has been demonstrated end-to-end in a live computer-vision subfield with intense activity. SplatLab is an autonomous research system for 3D Gaussian Splatting that addresses these limitations. Given a research prompt, a target-paper URL, or no input at all, it reproduces a published baseline, proposes an extension, trains and ablates across Mip-NeRF 360 and LLFF, writes the manuscript, and binds every reported number to a logged training run. Five design choices distinguish it: (i) candidates mutate plugins from a verified-reproduction backbone matched to published baselines; (ii) a cascade-weighted Elo tournament across eight islands scores candidates on measured GPU PSNR with verbal-gradient feedback; (iii) a standing falsifier subtracts Elo on failure, integrating stress-test survival into selection; (iv) every reported number is bound to a logged training run, and the run cannot terminate while any claim is unbacked; (v) a seven-category 3DGS taxonomy wraps EVOLVE-BLOCK markers in domain-aligned scaffolds transferable across 3DGS repositories. On PSNR-targeted runs, SplatLab's manuscripts beat their reproduced targets by +0.18 to +3.78 dB, including +3.78 dB on astrophotographic nebula rendering, for which no prior 3DGS method exists. The research cycle compresses from months of graduate-student time to days of mostly autonomous compute. Code, all manuscripts, experiment ledgers, and the cross-run paper store are available on the project page.

---


### 44. [Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility](https://arxiv.org/abs/2610.30469)

**<font color=#1a73e8>作者：</font>** Germán Pardo-González, Shaghayegh Vosough, Katerina Papadaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Traffic management has traditionally focused on toll-based and road pricing solutions. However, road pricing often raises concerns about accessibility and public dissatisfaction, leading to its prohibition in some places, such as Finland. This study optimises the dynamic allocation of incentives to drivers, encouraging them to reroute onto alternative (potentially longer) paths to achieve greater societal benefit, reduced total travel time (TTT) and total emissions in the transportation network, contributing to sustainable urban mobility. We employ a multi-agent reinforcement learning approach to dynamically assign incentives to drivers to reduce both TTT and emissions, with travel times estimated using traffic simulation software. We demonstrate that, with an unlimited budget and an objective of minimising travel time, the incentive scheme reduces TTT by 16%, compared to the dynamic User-Equilibrium (UE) with a budget equivalent to about 11% of the UE total time. When the goal is to minimise emissions, a 9% reduction in CO2 emissions is observed under an unlimited budget. We demonstrate a critical trade-off: minimising TTT leads to an increase in emissions, while prioritising emission reductions raises TTT. However, with the right combination of weights in the multi-objective function, both TTT and total emissions are improved beyond the baseline.

---


### 45. [DiffLTM: Continuous Diffusions Large Tabular Models for Conditional Generation](https://arxiv.org/abs/2610.30472)

**<font color=#1a73e8>作者：</font>** Alankrita Bhatt, Mukur Gupta, Andrea Montanari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional generation is a key capability to be supported by Large Tabular Models, enabling a number of applications. Accurate conditional generation has to contend with two key challenges: $(i)$ Data comprise a mixture of numerical and categorical entries, the latter often with high cardinality and heavily unbalanced proportions; $(ii)$ Conditional generation becomes increasingly difficult for rare sub-populations. The best models in this class use a hybrid of continuous and discrete diffusions. In this paper, we design a continuous diffusion model with strong generation quality. An important element is the use of cross-entropy loss for categoricals, for which we provide a first theoretical justification. We introduce metrics that focus on rare subpopulations. Further, we generalize conditional generation techniques to enable new types of conditioning. Finally, we show that our model (trained on labor data) can capture classical insights from econometrics.
Code is available at this https URL

---


### 46. [Rethinking SAE Evaluation: An Atomic Interpretable Unit Framework Reveals Hidden Polysemanticity and Redundancy](https://arxiv.org/abs/2610.30474)

**<font color=#1a73e8>作者：</font>** Riteng Zhang, Xiaoqian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) were originally motivated by discovering monosemantic features, a property that characterizes individual features but does not specify what the learned feature set should look like as a whole. As SAEs have increasingly been adopted for attribution, circuit discovery, and intervention, researchers have begun evaluating metrics that describe global properties of the feature set, such as sparsity, dead feature rates, reconstruction fidelity, and disentanglement, a diverse set that extends far beyond monosemanticity. However, this implicit shift beyond monosemanticity has not been formalized as a clear, well-defined objective that comes before these evaluation metrics. Without such an objective, existing metrics remain ad hoc, with their necessity unjustified. In this work, we formalize this ultimate objective by introducing a new paradigm for SAE evaluation: requiring that SAE features, and more generally dictionary-based decompositions of model representations, form an atomic interpretable unit basis, a coordinate system for semantically meaningful explanation. Under this paradigm, we organize existing and new measurements such as DAME (Dominance-Aware Monosemanticity Evaluation) as proxy metrics and introduce a comprehensive benchmarking framework. Evaluating hundreds of SAEs across multiple architectures and model families, we uncover failure modes in which some SAEs appear monosemantic under existing evaluation metrics while remaining functionally polysemantic: the most dominant features, those contributing most to model computation, are systematically less interpretable and more redundant. These failure modes warrant attention from SAE researchers as targets for improved training and architectures, and motivate dominance-aware evaluation as a standard check for practitioners before SAE features are deployed for attribution, circuit tracing, or intervention.

---


### 47. [AVAtt: A Free-Viewing Eye-Tracking Dataset and Benchmark for Visual Attention on Paintings](https://arxiv.org/abs/2610.30481)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kerkouri, Marouane Tliba, Aladine Chetouani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency and scanpath models are developed almost exclusively on natural photographs, yet paintings are composed by artists to guide the viewer's eye and differ from photographs in texture, colour and abstraction. We introduce \avatt, a free-viewing eye-tracking dataset on \nImages{} paintings spanning sixteen art movements and five centuries, with \nScanpaths{} scanpaths and \nFixations{} fixations from \nParticipants{} participants (\spPerImageMin--\spPerImageMax{} observers per painting). For every painting we release individual scanpaths with fixation timing and eye--screen distance, fixation maps, saliency maps smoothed at one degree of visual angle, temporal saliency videos and rich art metadata. We benchmark classic and deep saliency models against human agreement, revealing substantial headroom for art-aware models, and rank 44 scanpath-similarity measures, including a new language-free family of image-encoder metrics built on ten CNN, ViT and self-supervised encoders. With controls that remove viewing biases, we show that faces are fixated \faceEnrich$\times$ more than expected and within half a second, that local structure draws the eye, that composition rules fitted from image content predict where people look, and that art style shapes how much viewers agree. Dataset, code and a Python package are available at: this https URL.

---


### 48. [Optimal Multitask Representations Under a Rate Constraint: An Information Bottleneck Analysis](https://arxiv.org/abs/2610.30493)

**<font color=#1a73e8>作者：</font>** Nicholas Stiles, Gregory W. Wornell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which pretraining objective yields the best representation for downstream tasks under an information budget? We formalize this problem as a multitask information bottleneck, using a mutual information constraint to model incomplete information retention. For Gaussian inputs and tasks, we characterize optimal representations and show that a weakly task-aligned specialist can outperform a reconstruction generalist at low rates but lose at high rates. We also construct task families for which every fixed Gaussian prediction objective incurs arbitrarily large relative regret, driven by reversals in optimal allocation priorities. Conversely, the average task information matrix defines an objective with a uniform relative-regret bound controlled by maximum task SNR. CelebA and dSprites experiments illustrate that compression can change which pretraining objective performs best, and even task-aware training can reverse which downstream task is better preserved as rate increases.

---


### 49. [Membership Inference Attack on Private Evolution](https://arxiv.org/abs/2610.30514)

**<font color=#1a73e8>作者：</font>** Daniil Filienko, Sikha Pentyala, Martine De Cock  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic Data Generation (SDG) is an actively studied way to enable safe sharing of private data more broadly. Inference-only SDG methods, such as Private Evolution (PE), are particularly appealing, as they can leverage black-box access to pre-trained foundation models to generate high quality data without the need for model fine-tuning on the private data. PE is explicitly designed to produce synthetic data under Differential Privacy (DP). Yet formal DP guarantees do not eliminate the need for empirical privacy auditing of the practical susceptibility of released synthetic data to adversarial attacks. In this work, we introduce the first white-box Membership Inference Attack (MIA) tailored to the voting-based algorithm underlying the PE framework. By exploiting how the iterative filtering process biases the survival and proximity of synthetic candidates toward private instances, our attack achieves empirical performance indicating private data leakage in the PE applications across image, text, and tabular modalities.

---


### 50. [Protegrity-PII Technical Report](https://arxiv.org/abs/2610.30518)

**<font color=#1a73e8>作者：</font>** Hardeep Bassi, Hui Ma, Luís Seabra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Protegrity-PII, a new PII decision model for structured and unstructured text. Protegrity-PII achieves a typed recall of 0.915 with a precision of 0.907 on a new benchmark we propose, PII-SCOPE. Our model processes text in 0.49 seconds per million characters at \$0.0005 per million characters on a single RTX 6000 using batched inference. Due in part to the expansive nature of the entity type taxonomy used in training, Protegrity-PII achieves superior out-of-distribution generalization when benchmarked against a selection of state of the art models and datasets.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
