# 📦 其他研究 | 2026年09月14日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 1. [Rethinking Handwritten Character Recognition](https://arxiv.org/abs/2609.10572)

**<font color=#1a73e8>作者：</font>** Ranjit Raut, Aarav Subedi, Ashim Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-Latin handwritten character recognition (HCR) remains understudied. Dominant methods consider it as generic image classification, which uses model scale to implicitly learn stroke structure. Structural-prior efficiency---the principle that explicitly encoding script-geometric regularities as architectural inductive biases can be both more accurate and require fewer parameters. We introduce GraphemeNet, a unified multi-script architecture, governed by two orthogonal binary axes. Axis 1 operationalises stroke-level geometric regularity via Persistent Scaffold Injection (PSI): a script-specific asymmetric convolution injects a stroke scaffold as a weighted residual at every encoder stage, continuously anchoring learned features to script geometry---distinct from skip connections, auxiliary losses, or attention reweighting. Axis 2 selects between global average pooling with gated fusion and cross-scale attention with a Stroke Topology Module (STM), depending on whether glyph discrimination requires spatial relational reasoning. A Linear Capsule Routing (LCR) with $O(n)$ routing is shared universally. On fourteen benchmarks across eight writing systems, the architecture generalises with only scaffold and decoder topology varying per script, consistently challenging, outperforming published baselines, and establishing structural-prior efficiency as a broadly applicable principle for multi-script HCR.

---


### 2. [Probabilistic Focal Search: Accelerating Bounded-Suboptimal Search via Lower-Bound Advancement](https://arxiv.org/abs/2609.10584)

**<font color=#1a73e8>作者：</font>** Minh Vu Duc, Trung Le Huu, Hà Minh Hoàng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bounded-suboptimal search seeks a solution within a factor $w$ of optimal while reducing search effort. Focal Search (FS) uses heuristic guidance within FOCAL, the frontier nodes eligible under the threshold $w f_{\min}$, but its deterministic policy may leave $f_{\min}$ unchanged for many expansions. We introduce Probabilistic Focal Search (PFS), which follows the FS guided choice with probability $p$ and expands a minimum-$f$ OPEN node with probability $1-p$. The latter branch encourages the lower bound to advance, enlarging FOCAL and admitting nodes that may lead to feasible solutions. By balancing guidance and lower-bound advancement, this mechanism can reduce time to a bounded solution when progress is limited by delayed FOCAL admission. As a secondary transfer experiment, we apply the same scheduler to Dynamic Potential Search, yielding Probabilistic Dynamic Potential Search (PDPS). We benchmark PFS against FS on N-Puzzle, Pancake Sorting, and the Traveling Salesperson Problem (TSP), and evaluate its anytime extension on the Generalized Covering TSP (GCTSP), using multiple $w$ and $p$ values. Across these benchmarks, the largest gains occur when long $f_{\min}$ plateaus delay useful FOCAL admissions; in such settings, the probabilistic factor may reduce node expansions by about 90\% or more (e.g., on N-Puzzle and TSP). For the anytime algorithm family, Anytime Probabilistic Focal Search (APFS) outperforms all tested algorithms in evaluating anytime methods on GCTSP. We also observe that the benefit is smaller when the deterministic search already advances efficiently (e.g., Pancake Sorting), indicating that the probabilistic factor is most useful when FOCAL admission is a search bottleneck. The PDPS transfer shows that the mechanism also transfers to potential guidance, although its common-success effects remain domain- and bound-dependent.

---


### 3. [Halo: Improving forecast accuracy through heteroscedastic estimation](https://arxiv.org/abs/2609.10589)

**<font color=#1a73e8>作者：</font>** Adam Cataldo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heteroscedastic forecasting, where a network estimates a scale parameter alongside a location parameter, is normally motivated by uncertainty quantification. This paper shows it also improves the point estimate, in contrast to reported negative results for heteroscedastic estimation outside time series. Halo is a modification that reuses an existing deep forecaster's architecture, giving it a second output for the scale of its implied distribution and training it under the matching negative log likelihood. Adapting three state-of-the-art models --- a transformer, a graph network paired with a variational autoencoder, and a single-layer convolutional network --- under both Gaussian and Laplacian losses demonstrates the phenomenon. On the five electricity price markets of a standard forecasting benchmark, Halo improves MSE and MAE in 28 of 30 model-market-metric comparisons, cutting average MSE by 2.6% to 16.5% and average MAE by 1.7% to 11.0%. Two findings emerge: (1) whether the scale estimate comes from a second projection head or from a full parallel network matters far less than whether the network estimates scale, and (2) the improvement holds under the hyperparameters already tuned for the point-estimate baseline, so retuning is optional.

---


### 4. [Adaptive Diffusion Freezing: Privacy-preserving Diffusion Models Against Membership Inference Attacks](https://arxiv.org/abs/2609.10608)

**<font color=#1a73e8>作者：</font>** Jialu Guo, Xiao Han, Junjie Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in generative tasks across various areas, however their training process raises significant privacy concerns, particularly under membership inference attacks (MIAs). Prior studies on privacy-preserving of diffusion models fail to balance privacy, utility, and efficiency. To address this gap, we propose a novel framework of privacy-preserving diffusion models, Adaptive Diffusion Freezing (ADF), which can defend against MIAs with better trade-off. By leveraging cross-timestep adaptive freezing training, ADF explicitly control the participation of different data subsets across diffusion timesteps via a mask matrix, which reduces the over-memorization and leads to more uniform model behaviors between member and nonmember samples. To construct a freezing mask matrix that effectively reduce membership leakage without unnecessarily harming generation quality, we introduce a pretraining-based risk-aware freezing policy to estimate MIA risk based on memorization tendency, and suppress the contribution of the subset-timestep pairs with higher risk. Evaluations on multiple datasets demonstrate that ADF provides effective defense performance as well as state-of-the-art privacy-utility-efficiency trade-off performance compared to various baselines.

---


### 5. [PEARL: A Task-Aware Framework for Evaluating Differentially Private Synthetic Educational Data](https://arxiv.org/abs/2609.10612)

**<font color=#1a73e8>作者：</font>** Xianghui Meng, Yujing Zhang, Jionghao Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personalized learning systems rely on real learner data, including performance, behavior, and demographic information, but these data are highly privacy-sensitive. Differentially private (DP) synthetic data can support system development and educational research while reducing exposure of individual learners. Existing evaluations, however, assess privacy and predictive usefulness separately, without determining whether synthetic learner data remain usable for the intended personalized learning task. We introduce PEARL (Privacy-Equivalence Audit and Release Ledger), which approves a DP synthetic educational dataset only when it passes all required checks of validity, privacy protection, predictive usefulness, and suitability for the intended educational task, while recording why each rejected dataset fails. Across 96 study settings, each defined by a dataset, data-generation method, privacy budget, and random seed, only 12 produced synthetic datasets that passed all applicable PEARL checks. Many privacy-protected datasets were rejected for omitting important outcome groups, such as withdrawn students, or for failing to preserve the order of learning activities. Fairness analysis further showed that some datasets passing privacy and predictive-usefulness checks still yielded unequal at-risk prediction performance across groups defined by disability and socioeconomic background. Moreover, Deep Knowledge Tracing and Self-Attentive Knowledge Tracing learned no meaningful next-response patterns from any tested synthetic knowledge-tracing dataset, showing that privacy protection alone does not guarantee usefulness for dropout prediction, knowledge tracing, or adaptive tutoring.

---


### 6. [SoK: Privacy Attacks on Machine Learning via Explainable AI](https://arxiv.org/abs/2609.10627)

**<font color=#1a73e8>作者：</font>** Abdullah Caglar Oksuz, Anisa Halimi, Erman Ayday  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning explanations reveal model behavior beyond predictions, creating attack surfaces for model confidentiality and data privacy. We systematize 25 studies that exploit explanations for model extraction, membership inference, and model inversion, treating attribute inference as partial inversion. Existing work is often labeled only black- or white-box, obscuring substantial differences in what explanation signal reaches an adversary. We therefore separate model knowledge from explanation acquisition and identify five paths: target-released, attacker-derived, secondary disclosure, privileged access, and released global artifacts. Across these paths, explanations reduce extraction cost, expose membership signals through explanation statistics, recourse distance, and explanation-guided robustness, and support spatial or algebraic reconstruction of private inputs. We compare system and threat models, explanation signals, auxiliary knowledge, target models, modalities, query budgets, evaluation metrics, reported performance, and defenses. Our analysis shows that no explanation family is uniformly unsafe and no defense is uniformly effective. Risk depends on which signal is exposed, how it is acquired, which asset is targeted, and what the attacker already knows. We argue that explanation privacy should therefore be evaluated as an end-to-end disclosure problem, with defenses matched to the acquisition path and protected asset.

---


### 7. [Automating Quadratic Unconstrained Binary Optimization (QUBO) Formulation Generation from Natural Language](https://arxiv.org/abs/2609.10629)

**<font color=#1a73e8>作者：</font>** Niloy Kumar Mondal, Md Rizwan Parvez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quadratic Unconstrained Binary Optimization (QUBO) is a central formulation for combinatorial optimization and has gained increasing attention due to its compatibility with quantum, hybrid quantum-classical, and quantum-inspired solvers. However, translating natural-language problem descriptions into correct QUBO formulations remains difficult, requiring the identification of binary variables, constraints, objective functions, penalty terms, and suitable penalty weights. This process is time-consuming and often demands substantial domain expertise. To address this challenge, we propose an end-to-end multi-agent framework that automatically generates QUBO formulations from natural-language problem descriptions, supported by structured or unstructured test cases. To evaluate its performance, We also introduce QUBOBench, a benchmark containing 100 combinatorial optimization problems across 12 application domains, curated from peer-reviewed literature, competitions, and canonical NP-hard problems. Experimental results show that our framework achieves 68% accuracy on QUBOBench, outperforming a direct single-call baseline by 22%. Further analysis identifies iterative self-repair as the most important component contributing to improved performance. The data and code are open-sourced at this https URL.

---


### 8. [From Cycle Space to Cycle Manifold: Limits and Achievability of Blind False Data Injection Attacks](https://arxiv.org/abs/2609.10631)

**<font color=#1a73e8>作者：</font>** Xin Li, Chenhan Xiao, Jonathan Cohen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A false data injection attack (FDIA) can change the estimated grid state while evading a residual-based bad data detector (BDD). Existing blind attacks learn a low-rank measurement subspace, but this algebraic view does not state the physical grid constraints that make an attack stealthy or the minimum information needed to recover the complete attack space. Under the connected direct-current (DC) branch-flow model, we show that the residual-sensitive subspace of the noiseless orthogonal test is exactly the weighted cycle space. Its orthogonal complement is therefore the complete stealthy attack space, making weighted cycle-space knowledge both necessary and sufficient for complete blind FDIA. This space identifies the topology only up to 2-isomorphism and the relative cycle-edge parameters only up to one scale per biconnected component; bridge parameters are neither identified nor required. We then formulate a computationally unconstrained benchmark and a tractable measurement-only reconstruction method. Experiments on IEEE systems compare BDD bypass rate at a 95% nominal-acceptance threshold against state impact. As a compact alternating-current (AC) extension, we characterize feasible branch P/Q measurements by a cycle manifold and demonstrate topology-assisted manifold fitting and measurement generation on a graphics processing unit (GPU). In the lossless fixed-voltage small-angle limit, the normal space of the active-power slice reduces to the DC weighted cycle space.

---


### 9. [HermiCache: Enclave-Aware Cache Replacement for Trusted Execution Environments](https://arxiv.org/abs/2609.10634)

**<font color=#1a73e8>作者：</font>** Oussama Elmnaouri, Pascal Cotret, Vianney Lapôtre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) protect enclave memory from untrusted software but remain vulnerable to cache-based side-channel attacks due to shared microarchitectural resources. Existing countermeasures use techniques such as cache partitioning or randomization: these solutions are not ideal if a designer wants fine-grained configurations and a deterministic protection. In this paper, we introduce HermiCache which is an answer to these requirements. HermiCache is designed for RISC-V cores and has been implemented in the OpenHwGroup CVA6 core with a Keystone TEE for the software layer. The solution has an area overhead of 6% on the processor core.

---


### 10. [Zero-shot rib design: merging training-free generative prior with topology optimization](https://arxiv.org/abs/2609.10643)

**<font color=#1a73e8>作者：</font>** Yongmin Kwon, Namwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural load-bearing patterns such as leaf venation, trabecular bone, and spider webs achieve high stiffness per unit mass, yet classical topology optimizers rarely reach such geometries, and few let engineers express structural design intent through natural language. This work treats a frozen text-to-image diffusion model as a training-free source of design knowledge and distills it into the physics loop of density-based topology optimization via score distillation sampling, so that a text prompt becomes an explicit, machine-interpretable representation of engineer intent. The prompt-induced generative gradient and the finite element sensitivity are combined at every iteration, letting physics decide which prompt-induced features survive. In 245 primary SDS runs spanning four geometric domains and two physics regimes, 38 of 49 prompt--domain combinations achieved statistically significant compliance reductions (up to $-31.5\%$ mechanical and $-23.0\%$ thermoelastic), outperforming gradient-based baselines. Cross-domain morphological analysis identifies a recurring structural signature of improvement: in most domains the generative prior suppresses dead-end branches in the rib skeleton, with endpoint--compliance correlation $r = +0.56$ to $+0.99$. A Heaviside projection with $\beta$-continuation resolves a pronounced intermediate-density tendency in this diffusion--physics coupling ($42.6\%$ to $<3\%$), and an automated skeleton-based pipeline converts optimized density fields into \rev{candidate geometry ready for computer-aided design. By retargeting the generative prior across domains, loading conditions, and physics objectives through a change of text prompt, with each new problem's physics setup specified separately, the framework uses a pretrained generative model as a reusable, training-free prior for engineering design.

---


### 11. [Byzantine-Robust Federated Fire Detection with a Rotating Coordinator](https://arxiv.org/abs/2609.10647)

**<font color=#1a73e8>作者：</font>** Georgia Argyrou, Aymen Bahrouny, Hedi Fendriy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the application of federated learning (FL) to indoor fire detection. Such fire-detection systems use edge cameras that record sensitive footage which cannot easily be collected at a central server. Existing federated solutions leave three practical obstacles unaddressed: limited uplink bandwidth, Byzantine (malicious or faulty) clients, and unconditional trust in a single, permanently fixed aggregation server. Our main contributions address all three. In particular, we provide (i) a curated indoor fire-detection dataset assembled from eight public sources; (ii) an edge-deployable detector whose model updates are compressed up to 10 time with only a small loss in balanced accuracy; and (iii) a semi-decentralized Byzantine-robust FL method that combines history-aware aggregation with a rotating coordinator, evicting stealthy attacks that per-round filters miss while removing the fixed-server single point of failure. On the held-out test set the rotating-coordinator method matches its fixed-server counterpart in accuracy and detection speed, and a physically distributed six-node cloud deployment confirms feasibility.

---


### 12. [Artificial Intelligence Algorithms for the Detection of Pathologies Related to Lung Cancer through Image Analysis using Convolutional Neural Networks and Data Augmentation: a systematic mapping of the literature](https://arxiv.org/abs/2609.10652)

**<font color=#1a73e8>作者：</font>** Pablo Ramirez Amador  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lung cancer is one of the leading causes of death worldwide, and its early diagnosis is crucial to improving patients prognosis and quality of life. However, the process of interpreting medical images for the detection of lung cancer is complex and requires trained experts. In this context, artificial intelligence (AI) and deep learning (DL) emerge as potential tools to automate and optimize image analysis. The objective of this work is to review the most recent and relevant applications of AI and DL in the field of radiology for the detection of lung cancer. To this end, an exhaustive search was carried out in scientific databases such as PubMed,IEEEXPLORE, Scopus and Web of Science, and 96 articles published from 2015 to the present addressing the use of AI and DL in biomedical engineering were selected. Emphasis is placed on the use of convolutional neural networks (CNN) with transfer learning and Data Augmentation as promising techniques to improve the accuracy and efficiency of the image interpretation process. The results show that the use of AI and DL can offer an effective alternative for the early diagnosis of lung cancer, with high sensitivity and specificity. However, current limitations and challenges that must be addressed to guarantee its responsible and safe application in clinical practice are also identified, such as the lack of standardized data, the ex plainability of the models, patient privacy, and the ethical and social implications. It is concluded that the use of AI and DL can have a positive impact on the care of patients with lung cancer, but further research and regulation are required to ensure its quality and reliability.

---


### 13. [A Multi-Stage Rule-Chaining Framework for Compositional and Interpretable Cognitive Reasoning](https://arxiv.org/abs/2609.10654)

**<font color=#1a73e8>作者：</font>** Deblina Kar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Abstraction and Reasoning Corpus (ARC) benchmarks cognitive generalization, the ability to infer and apply abstract rules from limited examples. This paper presents a multi-stage rule-chaining framework that performs compositional reasoning across symbolic, structural, and conceptual levels. The framework integrates three complementary solvers:
(1) a deterministic rule discovery module that induces atomic transformations through geometric, color, and object-based analysis;
(2) a pattern-composition engine that reconstructs outputs via block merging, repetition, and spatial heuristics; and
(3) a structural abstraction layer that infers hierarchical and nested relationships across grids.
These solvers operate sequentially within a progressive fallback hierarchy, where each stage reuses prior reasoning traces to enhance interpretability and generalization. Training passed for 995 tasks out of 1000, further evaluated on 105 tasks out of 120 and solved 230 test tasks out of 240 ARC-AGI-2 tasks. The system achieved strong coverage across deterministic, compositional, and abstract categories, demonstrating an overall accuracy exceeding 95 percent. The proposed architecture bridges symbolic reasoning and pattern synthesis, providing interpretable insight into cognitive generalization. The results suggest that rule chaining and hierarchical composition can advance machine reasoning toward transparent, human-aligned abstraction without relying on task-specific tuning.

---


### 14. [Understanding LoRA Rank Trade-offs in Diffusion Model Fine-Tuning](https://arxiv.org/abs/2609.10656)

**<font color=#1a73e8>作者：</font>** Iman Khazrak, Narges Nejad, Mostafa M. Rezaee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Selecting LoRA rank for diffusion fine-tuning requires balancing quality and compute cost. We present a controlled study on CIFAR-10 using a DDPM U-Net with ranks {2,4,8,16,32}, fixed optimization settings, and a reproducible local-folder pytorch-fid protocol. We report FID, trainable parameters, runtime, and GPU memory, then validate trends with extended-budget DDPM runs (20 epochs; ranks 4/8/16) and a Tiny DiT backbone (10 epochs; ranks 4/8/16). Results show moderate ranks are most efficient: rank 4 achieves the best DDPM FID (124.1380), rank 8 is close (124.2136), and higher ranks provide limited gains despite larger adaptation cost. These findings support small-to-moderate ranks as practical defaults under fixed training budgets.

---


### 15. [Quantifying the Memorization-to-Generalization Transition: Scaling Laws and Phase Structure in Grokking](https://arxiv.org/abs/2609.10657)

**<font color=#1a73e8>作者：</font>** Anish Kataria  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks trained past memorization frequently undergo a delayed transition to generalization, a phenomenon known as grokking. Despite theoretical progress on \emph{why} this transition occurs, the quantitative structure of \emph{when} it occurs in hyperparameter space remains uncharacterized. We map the memorization-to-generalization boundary across 384 configurations of two-hidden-layer MLPs on modular arithmetic, fitting a power-law scaling relation for generalization onset time: $T_{\mathrm{grok}} \propto H^{-0.27}\, D^{-2.04}\, \eta^{-0.50}\, \lambda^{-0.64}$ ($R^2 = 0.732$; $0.821$ with interactions). The exponent hierarchy reveals that data complexity ($D^{-2.04}$) is the dominant driver of regime transition, not model capacity ($H^{-0.27}$): doubling data accelerates generalization by ${\sim}4\times$, while doubling width yields only ${\sim}1.2\times$. A sharp phase boundary at weight decay $\lambda \gtrsim 1.0$ separates grokking from non-grokking configurations, and weight norm trajectories show monotonic compression during the transition, consistent with implicit regularization selecting low-complexity solutions. These results provide a quantitative foundation for predicting and controlling regime transitions in overparameterized networks.

---


### 16. [Data-Efficient Language Modeling: From Frontier Advancement to Principle-Guided Model Improvement](https://arxiv.org/abs/2609.10702)

**<font color=#1a73e8>作者：</font>** Shuxing Yang, Kaihao Zhu, Junjie Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning from limited text requires models to use context, generalize to new inputs, and retain useful capabilities. Qiushi Engine conducted a long-horizon, end-to-end autonomous research program on BabyLM 2026 Strict-Small, within 10 million corpus words and 100 million cumulative word presentations. Three stages connected frontier advancement, principle discovery, and principle-guided model improvement. Stage I combined compact restatements, budget reinvestment, and residual incremental learning to build a frontier model. Stage II found that exact repetition and aligned restatement produce different patterns of context use, depending on target relations and prediction windows. In controlled tasks, recovering familiar performance did not ensure that unseen inputs could still use learned computations. These findings support a testable data-efficient learning principle: organize experience around the contextual dependencies needed for prediction; separately design visible information, supervision, and preservation; test learning, generalization, and retention. Stage III retained source text, masked more local clues, supervised selected targets, and preserved predictions on ordinarily masked inputs. Two continuation seeds from the same parent outperformed ordinary continuation on the complete nine-metric aggregate. Overall rose from 42.02 to 42.25 across two generations; the second achieved the highest Overall in the public Strict-Small snapshot of 8 September 2026. Further studies addressed compression, relational anchors, shared representations, and measurement. Models are available on Hugging Face; code and research records accompany the GitHub repository. Together, these stages illustrate Research RSI: recursive self-improvement of the research process. Scientific understanding and method innovations change subsequent questions and designs; new experiments test and refine them.

---


### 17. [Architecting the Secure AI-SOC: A Neurosymbolic Framework for Pipeline Integrity and Threat Mitigation](https://arxiv.org/abs/2609.10707)

**<font color=#1a73e8>作者：</font>** Anna Gazani, Spyridon Kounoupidis, Panagiotis Katsaros 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into Security Operations Centers (SOCs) streamlines threat intelligence but introduces critical vulnerabilities, notably indirect prompt injection via log poisoning. Adversaries exploit this vector to execute multistep ``promptware'' kill chains by embedding malicious payloads within system logs to hijack the LLM's operational logic. Securing this pipeline presents a dichotomy: deterministic defenses are computationally efficient yet semantically blind, while purely neural evaluations introduce prohibitive latency and probabilistic flaws. To address this, we propose a novel neurosymbolic defense-in-depth architecture that ensures end-to-end pipeline integrity. The primary layer employs customized SIEM decoders as a deterministic pre-filter, performing immediate structural sanitization to neutralize volumetric padding and signature-based injections at the ingestion edge. The secondary layer leverages NeMo Guardrails to enforce strict semantic boundaries through self-checking validation on the structured SIEM alerts prior to LLM processing. Furthermore, the framework integrates a closed-loop telemetry system, providing critical Human-in-the-Loop (HITL) visibility into thwarted attacks directly within the SOC dashboard. We present a comprehensive experimental evaluation mapped to the MITRE ATLAS taxonomy, assessing the framework against diverse prompt injections. Our results demonstrate that this synergistic approach effectively dismantles the promptware kill chain - bounding LLM stochasticity with verifiable constraints, and delivering a resilient, highly observable defense mechanism for next-generation AI-SOCs.

---


### 18. [AcFlow: Controlling Text-to-Image Diffusion Transformers via Learned Conditional Activation Flow](https://arxiv.org/abs/2609.10723)

**<font color=#1a73e8>作者：</font>** Junran Wang, Zehao Jin, Tianyu Luan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion transformers (DiTs) are powerful generators, yet direct prompting provides limited control interface for style intensity and can fail to suppress unwanted concepts. To enable these controls, we introduce AcFlow, an inference-time controller that transports intermediate layer image-token activations through a learned concept-conditioned velocity field while keeping the base DiT frozen. A textual concept description specifies the desired intervention, while the integration horizon provides a continuous control parameter. The field produces token-varying, activation-dependent updates. With parameters shared across concepts within each task family, the field supports fine-grained descriptions and generalizes to concepts unseen during training without per-concept fitting. On style control, AcFlow achieves the best style--content trade-off among the evaluated baselines in the high-style-alignment regime. At a fixed operating point, AcFlow attains style--content alignment of 0.5365/0.2860, compared with 0.4397/0.2684 for the baseline with the highest style alignment. Qualitative results demonstrate suppression of diverse concepts, including cases where direct prompting fails. Our analyses support the learned velocity field as an adaptive control mechanism, with update directions varying across tokens and depend on their activation states. Our code is available at this https URL.

---


### 19. [Conformal Calibration Transfer](https://arxiv.org/abs/2609.10737)

**<font color=#1a73e8>作者：</font>** Achref Doula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction converts point predictions into set-valued predictions with coverage guarantees under exchangeability between calibration and deployment data. We study conformal calibration transfer, where this requirement fails because labeled calibration is available only in a source space, while prediction sets are needed in a target space linked to the source through unlabeled paired observations (e.g., paired modalities or sensor changes). We propose Transported Conformal Calibration (TCC): we transport labeled source calibration into the target space using the paired data, and then correct residual post-transport mismatch using only unlabeled target inputs. We instantiate this correction with two complementary methods: TCC-KS, which uses a label-free uncertainty surrogate to detect mismatch and adjust calibration conservatively, and weighted-TCC, which reweights transported calibration toward the target domain for improved efficiency when weights are stable. We provide finite-sample target-domain coverage guarantees that adapt to an observable measure of mismatch. Across CIFAR-100-C, Tiny-ImageNet-C, and SEN12MS, we show reliable target-domain coverage transfer without labeled target calibration data, with label-free diagnostics that predict when correction is needed.

---


### 20. [Temporal and Multimodal Deep Learning for Cyberattack Detection in LEO Satellite Systems](https://arxiv.org/abs/2609.10746)

**<font color=#1a73e8>作者：</font>** Kyle Stein, Guillermo Francia III, Eman El-Sheikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing reliance on Low-Earth Orbit (LEO) satellite communication systems has increased the need for intelligent methods capable of detecting cyberattacks across complex and dynamic space environments. Unlike conventional network intrusion detection, satellite systems generate heterogeneous information across radio-frequency (RF) links, onboard hardware, and orbital operations. However, many existing approaches either rely on terrestrial intrusion datasets or evaluate individual observations independently, limiting their ability to capture temporal attack behavior specific to LEO satellites. In this work, we conduct a systematic study of deep-learning-based cyberattack detection using the recently introduced satellite-specific UNSW-IoTSAT dataset. We investigate structured learning architectures that preserve hardware, orbital, and RF information, including a Subsystem-Fusion MLP and a hierarchical multimodal Transformer that models both cross-subsystem interactions and temporal evolution. We further evaluate leakage-resistant row-level and temporal settings, along with cross-satellite generalization, to characterize how model architecture and evaluation protocol influence satellite cyberattack detection. Experimental results demonstrate the value of structured multimodal modeling and rigorous evaluation, with the hierarchical Transformer achieving up to 91.66% accuracy and 85.63% macro F1 under the leakage-resistant evaluation protocol.

---


### 21. [Meta-Learning for Data-Efficient Plant Growth Estimation via Vision Transformers and Fuzzy Clustering](https://arxiv.org/abs/2609.10749)

**<font color=#1a73e8>作者：</font>** Sheikh Hasan Elahi, Rusith Chamara Hathurusinghe Dewage, Habib Ullah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate plant growth estimation is essential for greenhouse monitoring, yet obtaining labeled data remains costly and time-consuming. To address this, we propose a few-shot regression framework that combines Vision Transformer (ViT) feature embeddings, clustering-based task construction, and gradient-based meta-learning, and show that task construction in embedding space is a primary driver of performance. The approach leverages an unlabeled image pool to organize data into structured tasks using fuzzy c-means clustering, enabling efficient learning from a small number of labeled samples. We systematically evaluate meta-learning methods and show that second-order methods (e.g., Model-Agnostic Meta-Learning variants such as MAML++) outperform classical baselines in the few-shot regime. Furthermore, intra-cluster support selection has a limited and dataset-dependent impact. Experiments on two plant datasets show that structured task design combined with meta-learning enables reliable plant growth estimation under severe label scarcity.

---


### 22. [Adaptive Margin Ordinal Loss: Penalizing Center-Class Hedging in Ordinal Classification](https://arxiv.org/abs/2609.10752)

**<font color=#1a73e8>作者：</font>** Manisha Kandel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard cross-entropy loss causes neural networks trained on ordinal classification tasks to hedge predictions toward center classes, a failure mode we term \emph{center-class hedging}. This occurs because predicting the middle class minimizes expected symmetric loss, making it the path of least resistance regardless of the true label. Existing ordinal losses address related problems such as large-error penalization and rank consistency, but none directly suppresses center-class hedging as a function of where the true label lies relative to the ordinal center. We propose the Adaptive Margin Ordinal Loss (AMOL), a multiplicative weight applied to per-class loss terms of the form $m(k,y) = 1 + \alpha \cdot (1 - |k-c|/c) \cdot (|y-c|/c)$, where $c$ is the center class, $k$ is the candidate class, and $y$ is the true label. The weight encodes a joint condition: it is large only when the candidate class is near center and the true label is far from center, collapsing to standard behavior otherwise. We further introduce the Center-Hedging Rate (CHR) as a diagnostic metric that directly quantifies this failure mode. Across four ordinal classification benchmarks and five random seeds, AMOL achieves the best or tied-best Quadratic Weighted Kappa (QWK) on all four datasets compared to cross-entropy, OLL, and SORD baselines. An asymmetric variant (AMOL-asym) eliminates center-class hedging entirely on the Abalone dataset ($\text{CHR} = 0.000 \pm 0.000$ across all five seeds, $n \approx 266$ extreme-class test samples per run), compared to $0.074 \pm 0.005$ for standard cross-entropy.

---


### 23. [GRADE: Single-Frame Generative Radar Depth Estimation Under Visual Degradation](https://arxiv.org/abs/2609.10756)

**<font color=#1a73e8>作者：</font>** Bin Zhao, Patrick Chiou, Nakul Garg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense 3D depth perception fails under smoke, fog, and darkness because optical sensors cannot penetrate airborne particulates. mmWave radar remains usable and measures range accurately under these conditions, but its small aperture limits angular resolution. We present GRADE, which grounds a pretrained generative prior in single-frame radar geometry to estimate high-fidelity metric depth. GRADE first maps raw 4D radar spectra to coarse metric depth. A latent diffusion backbone then recovers structural detail while conditioning every denoising step on this estimate. A pixel-space adapter uses residual camera cues when available and is trained across clear, smoke-degraded, and occluded inputs so the full output approaches the radar-conditioned path as visibility degrades. Trained and evaluated on ~95K frames across 12 buildings with real smoke, GRADE achieves an MAE of 0.303 m in clear scenes and 0.313 m under smoke, outperforming existing baselines. Code and datasets are available at this https URL.

---


### 24. [A Bellman Optimality Equation for Plasticity](https://arxiv.org/abs/2609.10776)

**<font color=#1a73e8>作者：</font>** Jeremy Lucas, Doina Precup  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In continual reinforcement learning, carefully managing the stability-plasticity tradeoff remains a core challenge. Recent work by Abel et al. (2025) formalized this dilemma by defining plasticity as the generalized directed information from an agent's observations to its actions, and empowerment as the generalized directed information from its actions to its observations. This formulation successfully reframes the traditional stability-plasticity tradeoff as an empowerment-plasticity tradeoff. However, while extensive literature exists on optimizing for empowerment, there is currently no research addressing the optimization of plasticity under this new definition. This paper presents preliminary work toward optimizing plasticity within Markov decision processes. We show that there exists a Bellman optimality equation for optimizing plasticity similar to previous work for empowerment.

---


### 25. [Counterfactual Marginalisation: Framework for Evaluating Robustness to Nuisance Variables](https://arxiv.org/abs/2609.10778)

**<font color=#1a73e8>作者：</font>** Yasin Ibrahim, Hermione Warr, Robin J. Evans 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models can achieve strong test performance while relying on demographic or acquisition-related shortcuts. We propose counterfactual (CF) marginalisation as a test-time evaluation procedure for assessing robustness of classification models to such variables. Given a CF image generator, we intervene on nuisance parent variables such as age or sex, generate CF versions of each test image, and average predictions over a target intervention distribution. This produces intervention-aware predictions that marginalise demographic effects while preserving patient-specific latent information. We use these predictions to define metrics for CF risk, calibration, stability and worst-case sensitivity. We demonstrate this framework's utility for quantitative robustness evaluation.

---


### 26. [From Connectivity to Rewards: Dense Reward Learning with Directed State Graphs](https://arxiv.org/abs/2609.10781)

**<font color=#1a73e8>作者：</font>** Shuyuan Zhang, Zihan Wang, Xiao-Wen Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of graphs with Goal-Conditioned Hierarchical Reinforcement Learning (GCHRL) has received increasing attention, as graphs naturally encode task hierarchies for effective subgoal sampling. However, existing methods often overlook intrinsic connectivity information, failing to fully leverage the underlying topology for efficient learning. Most graph-based GCHRL methods use the graph as a stochastic sampling tool rather than as an environmental model that encodes connectivity and state-accessibility information. This limitation is particularly acute in quasimetric environments, where the inherent asymmetry of state transitions poses a fundamental challenge to stable policy learning and robust path planning. In this paper, we address these problems by introducing a state connectivity model designed to predict pairwise state connectivity strength in asymmetric environments. We transform these connectivity strengths into scalar auxiliary dense rewards, providing continuous guidance across multiple hierarchical levels. We demonstrate that our proposed framework, Graph-Guided Quasimetric Dense Reward (G2QDR), can theoretically be integrated into any existing GCHRL architecture, and the state connectivity model is efficiently implemented via a neural network trained on a directed state graph generated during exploration. Empirical results across a wide range of sparse reward environments indicate that, in general, G2QDR can enhance the performance of baseline GCHRL approaches with acceptable computational overhead.

---


### 27. [Shedding Light: A Benchmark for Evaluating Lighting Understanding in Generative Image Models](https://arxiv.org/abs/2609.10787)

**<font color=#1a73e8>作者：</font>** Justine Giroux, Jack Oliver Hilliard, Yannick Hold-Geoffroy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate modelling of illumination is central to realistic image synthesis and scene understanding. Yet, there is little exploration into whether image generative models are good at this task or whether physical plausibility remains a key challenge for them. Clearly, significant progress has been made in realistic image synthesis, but do models truly understand lighting in a physically accurate manner? To answer this question, this work proposes a benchmark to assess the lighting understanding and harmonisation capabilities of generative models. Our key insight is that evaluating lighting understanding for such models only requires testing how well they insert novel objects into real photographs whilst maintaining consistent illumination. To do so, we use a multi-illumination dataset with images containing simple objects serving as ``light probes'', and prompt models to inpaint the same object onto the original image, then compare the generated results against the ground-truth light probes. We then estimate the lighting direction, colour and radiance distribution from the inpainted probes, providing a quantitative measure of illumination accuracy and photometric realism. Our work establishes a scalable evaluation protocol to systematically assess how well generative models capture and reproduce real-world lighting, offering a foundation for benchmarking the photometric accuracy of any future models. All code and data are available at this https URL .

---


### 28. [Two-Parameter Flow Map Learning for Continuous-Time Diffeomorphic Image Registration](https://arxiv.org/abs/2609.10789)

**<font color=#1a73e8>作者：</font>** Mohammadjavad Matinkia, Nilanjan Ray  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffeomorphic image registration is central to medical image analysis, enabling anatomically consistent alignment across subjects. Most learning-based diffeomorphic methods model autonomous ODEs(ordinary differential equations) by parameterizing a stationary velocity field and recovering deformations via scaling-and-squaring. While non-autonomous ODEs with time-dependent velocities increase expressiveness, existing approaches rely on numerical integration to implicitly enforce flow structure that entangles model expressiveness with discretization accuracy. We propose a framework to directly learn the continuous-time solution of a non-autonomous ODE formulated as a two-parameterflow map. By enforcing cocycle consistency, a fundamental structural property of time-varying flows, we learn the flow maps without time discretization and velocity integration during training. The framework recovers diffeomorphic mappings at inference using a small number of compositions. Our proposed framework seamlessly incorporates standard registration backbones and improves alignment accuracy consistently across nine datasets while preserving diffeomorphic structure. Notably, the proposed method achieves an average Dice improvement of 2.1% on brain MRI benchmarks, a 12% TRE reduction on lung CT, and a 2.6% Dice gain on cardiac MRI and ultrasound datasets.

---


### 29. [Analyzing Traditional and Neural Approaches to Multilingual Readability Assessment](https://arxiv.org/abs/2609.10792)

**<font color=#1a73e8>作者：</font>** Joshua Wong, Chris Tanner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based models excel at Automatic Readability Assessment (ARA), yet feature-based models remain in active use because their predictions tie back to linguistic properties. This matters because readability labels are subjective and rater-dependent, so high accuracy on noisy ground truth may reflect surface patterns rather than the linguistic structure that defines difficulty. We test whether transformers internalize the same features as traditional models across Arabic, English, French, Hindi, and Russian using the ReadMe++ dataset. Shapley Additive Explanations (SHAP) identify the features driving traditional classifiers, which we then use as TCAV concept sets to probe multilingual XLM-R and language-specific encoders. Transformers recover surface-length, syntactic, and lexical-diversity signals, and reflect the ordinal CEFR structure of the traditional models. Alignment varies by model family, language, and layer, with language-specific encoders tracking traditional models more clearly than XLM-R. High linear separability does not always imply directional influence, limiting linear probing for count-based readability features.

---


### 30. [DR-LabStack: Design and Implementation of a Clinician-Facing Web System for Diabetic Retinopathy Prediction](https://arxiv.org/abs/2609.10796)

**<font color=#1a73e8>作者：</font>** Yingfan Xu, Tieming Liu, Ye Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained diabetic retinopathy (DR) prediction models differ in their input fields, serialization formats, preprocessing requirements, and output semantics. Making these models accessible through a common clinical interface therefore requires explicit coordination between the user interface and the inference service. We designed and implemented DR-LabStack, a React-Flask web system integrating four externally developed pretrained models: RuleFit, Pruned RuleFit, Elaborative XGBoost, and Two-level Ensemble. A shared form retrieves ordered model features, renders model-specific numerical and categorical controls, and constructs a positional input vector. Backend adapters load heterogeneous artifacts and apply the ensemble's accompanying scaler, while a common JSON response supports binary classification display alongside method and source information. Functional evaluation on September 8, 2026 used copied application files and real model artifacts in a documented isolated environment. All four models loaded and exposed their 14-, 6-, 8-, and 25-field contracts. Sixty-two Flask test-client requests characterized service behavior; 12 limited-vector checks confirmed invocation-path and threshold consistency. Twenty-four browser-component scenarios with mocked transport verified input ordering and result rendering and characterized input-validation behavior. The resulting system demonstrates a reusable interaction and serving workflow for heterogeneous DR models. The contribution is web-system design, integration, and software functionality; clinical effectiveness and clinician usability require separate evaluation.

---


### 31. [RiVaT-Fuse: Reliability-Calibrated Variational Tensor Fusion for Multimodal Prediction under Modality Uncertainty](https://arxiv.org/abs/2609.10798)

**<font color=#1a73e8>作者：</font>** Yingfan Xu, Tieming Liu, Ye Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Image-metadata prediction requires fusing heterogeneous evidence whose reliability can vary across samples and latent factors. Existing representation-level fusion methods typically choose an aggregation architecture, such as concatenation, gating, conditional modulation, or attention, without explicitly defining what the fused representation should mean under modality uncertainty. We propose RiVaT-Fuse, a reliability-calibrated variational tensor fusion framework that defines fusion as sample-wise latent-state estimation. Rather than producing a fused vector by direct aggregation, RiVaT-Fuse estimates a consensus latent state through a variational objective that balances image evidence, metadata evidence, structured cross-modal interaction, and stability. The resulting framework replaces scalar modality confidence with matrix-valued trust geometry, decomposes interaction into additive, multiplicative, and relational components, and couples the latent state with conditional robustness and structured multi-task prediction. We provide well-posedness and stability interpretations of the latent solve and instantiate the framework with efficient low-rank-plus-diagonal trust operators. On an image-level image-metadata prediction benchmark, RiVaT-Fuse achieves the strongest overall predictive rank among direct representation-level baselines while improving probability and label stability under perturbation.

---


### 32. [How Much Velocity Does Off-Ball Space Value Need? A Broadcast-Viewport Benchmark](https://arxiv.org/abs/2609.10801)

**<font color=#1a73e8>作者：</font>** Seongjin Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Velocity-aware pitch control is standard, but under a broadcast viewport half the players are off screen and on-screen velocities come from a drifting calibration. We ask at which layer of broadcast off-ball analysis velocity changes the answer. Inheriting our off-screen imputation protocol (three Metrica matches, 44 m viewport, block-bootstrap CIs), we score four velocity regimes -- none, viewport-legal observed, true-for-visible, true-for-all -- against a velocity-aware ground truth at three layers: imputation, the control surface, and team verdicts. Velocity is nearly useless for imputation (-0.2 pp against a 12--14 pp velocity-free surface MAE), first-order for the surface (-1.5 to -1.8 pp, 11--15% of that MAE), and ten times smaller for verdicts (-0.12 to -0.19 pp). The velocity that matters is the visible channel: perfect occluded-player velocity adds 2--6% of the visible gain, and no last-seen decay policy we tested exceeds that. Omitting velocity blurs the surface (per-frame |e| 2.2--2.6 pp) with small time-averaged bias (per cell <=0.4 pp), whereas imputation error is a structured bias against the defending team's deep zone (5--9 pp). At a fixed velocity window, a noise ladder of eleven jitter settings, including sigma_v-matched pairs, is ordered to first order by one velocity-noise axis sigma_v with break-even ~1 m/s; eleven SoccerNet-GSR clips from one match through our pipeline measure sigma_v=1.65 m/s yet recover 24--36% of the benefit: 43% of the variance is frame-common, which the surface tolerates, and the residual is heavy-tailed and clustered, which Gaussian controls matched on component RMS do not reproduce (+0.03 vs. +0.36). The share of velocity-free error that velocity removes grows with viewport width (7% at 36 m, 21% at 60 m): fix imputation on tight shots, velocity on wide ones. Code and logs are released.

---


### 33. [TrajFusionNet+: Transformer-Based Prediction of Pedestrian Crossing Intention via Fusion of Trajectory Representations and Scene Graphs](https://arxiv.org/abs/2609.10806)

**<font color=#1a73e8>作者：</font>** François G. Landry, Moulay A. Akhloufi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The pedestrian crossing intention task involves predicting whether pedestrians are likely to cross the road from the point of view of an autonomous vehicle. We introduce TrajFusionNet+, a novel transformer-based model for pedestrian crossing intention prediction. TrajFusionNet+ combines sequential and visual representations of pedestrian trajectory with a graph-based representation of the scene context in order to predict pedestrian crossing intention. The proposed architecture builds upon our previous model, TrajFusionNet, and comprises three branches: a Sequence Attention Module (SAM), which processes a sequential representation of past and predicted pedestrian trajectories; a Visual Attention Module (VAM), which utilizes a visual representation of the pedestrian trajectories by overlaying observed and predicted bounding boxes onto scene images; and a Graph Attention Module (GAM), which extracts pedestrian-centric graphs from segmented scene images and captures the relational dependencies between pedestrians and traffic elements. TrajFusionNet+ achieves improved state-of-the-art performance on the two most widely used pedestrian crossing intention datasets, PIE and JAAD. Furthermore, we introduce a new evaluation protocol in which models are trained jointly on the PIE and JAAD datasets but evaluated separately on each. Under this setting, TrajFusionNet+ demonstrates superior generalization compared to existing approaches.

---


### 34. [Overpainting: Localized Context-aware Diffusion Image Editing](https://arxiv.org/abs/2609.10811)

**<font color=#1a73e8>作者：</font>** Sam Sartor, Iliyan Georgiev, Michael Fischer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present "overpainting", an image editing operation which offers both control over the location of the edit and awareness of the previous content in that location. The overpainted area is given by a trimap, where white-annotated pixels must be edited, gray-annotated pixels may be edited, and black-annotated pixels must not be edited. This enables both precise and loose control, depending on user intent.
We implement overpainting by adapting a pretrained image editing diffusion model using a combination of joint attention and low-rank adaption across input images with attention-dropout to balance the information flow between noise, source and mask images. We present a novel, automated, training data generation pipeline that (1) generates a set of candidate image pairs leveraging existing language-based editing models, (2) carefully curates those pairs, and (3) extracts a trimap from each usable pair. We demonstrate the versatility of our overpainting model on a wide range of editing tasks.

---


### 35. [Tapes Together Strong: The Co-evolution of Computation and Cooperation](https://arxiv.org/abs/2609.10817)

**<font color=#1a73e8>作者：</font>** Kunal Jha, Francesco Cicala, Blaise Agüera y Arcas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> How does cooperation evolve in complex agentic systems? Prior work in evolutionary game theory studies why individuals are incentivized to cooperate by isolating social interactions from the physical costs of behavior, while artificial life models traditionally study emergent self-replication without formalizing the dilemma between acquiring resources and preserving the shared energy needed to reproduce. In contrast, we introduce Autopoietic Game Theory, a computational model where social interactions, replication mechanisms, and their associated computational costs are endogenous and simultaneously co-evolving. We study these dynamics using a computational substrate of randomly initialized programs in Z80 machine code, showing empirically, and motivating with a simplified theoretical model, that embedding a social dilemma directly into the physics of computation can favor the emergence of self-replicating, cooperative strategies. When resources are scarce, our analysis shows that defection can become self-limiting even in well-mixed populations: parasitic stealing destroys shared energy, slows execution, and can prevent reliable replication. Empirically, evolved programs suppress stealing across several Z80 environments, while spatial assortment further supports structural complexity and task performance. We further show that the framework can incorporate exogenous pressures, such as math tasks structured as sequential social dilemmas, when rewards are tied to computation budgets. These results suggest that coupling an agent's capacity for computation to its available energy transforms cooperation into a dominant scaffolding for building sustainable, self-organizing systems.

---


### 36. [Processing and classifying bird songs using wavelet techniques and supervised learning](https://arxiv.org/abs/2609.10826)

**<font color=#1a73e8>作者：</font>** Laura Lucia Dominguez Barrios, Fidel Aniano Causil Barrios, Alex Rodrigo dos Santos Sousa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study proposes an integrated framework for the processing and classification of invasive bird species vocalizations within natural soundscapes, characterized by high levels of environmental noise. We address the challenge of signal degradation by employing a Bayesian wavelet shrinkage methodology based on the Epanechnikov kernel prior, which offers a closed form decision rule and high computational efficiency for processing large bioacoustic datasets. The methodology was applied to recordings of three species obtained from the iNaturalist platform: \textit{Euphonia violacea}, \textit{Leiothrix lutea}, and \textit{Passer domesticus}. After signal denoising, we extracted a comprehensive set of features, including Mel-Frequency Cepstral Coefficients (MFCCs) and spectral indices such as entropy and zero-crossing rate. Several supervised learning models: Random Forest, Multinomial Logistic Regression and Support Vector Machine (SVM) were evaluated across different feature dimensionalities. Our results demonstrate that the proposed wavelet based preprocessing significantly enhances classification performance, with the SVM model achieving the highest accuracy (up to 0.9398) under a 10-dimensional MFCC configuration. This research provides a robust statistical tool for automated ecological monitoring and the management of biological invasions.

---


### 37. [Are We Really Doing Few-Shot Learning? A Critical Examination of Pre-Training Assumptions](https://arxiv.org/abs/2609.10851)

**<font color=#1a73e8>作者：</font>** Alejandro Galan-Cuenca, Marcelo Saval-Calvo, Antonio Javier Gallego  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot learning is commonly evaluated under protocols that pre-train a model on a large auxiliary set whose classes are disjoint from the target episodes yet drawn from the same visual domain. This paper examines whether such protocols truly reflect low-data learning. We systematically compare no pre-training, class-disjoint in-domain pre-training, supervised out-of-domain pre-training, and label-free out-of-domain pre-training across eight datasets, three few-shot architectures, and multiple way-shot settings. Our results show that class disjointness alone is insufficient to remove the influence of target-domain data. In-domain pre-training improves over no pre-training by 33.41 percentage points on average, whereas supervised out-of-domain pre-training yields 23.75 percentage points, revealing a 9.66-point optimistic bias associated with domain overlap. Although out-of-domain pre-training is more realistic in applications where target-domain data are scarce, its effectiveness depends strongly on the compatibility between source and target domains. We further show that labeled source data are not strictly required, with an augmentation-based label-free strategy reaching an average gain of 27.71 percentage points and closely matching supervised out-of-domain pre-training at 27.97 percentage points. Finally, we introduce a descriptor-based source-selection strategy that estimates source-domain suitability before pre-training, reaching a median gap of only 1.37 percentage points to oracle selection. These findings highlight the need to move beyond in-domain pre-training as the default few-shot evaluation protocol, since it can overestimate performance in realistic scenarios where target-domain data are scarce.

---


### 38. [Flow Duality and Source Geometry for Categorical Generation](https://arxiv.org/abs/2609.10863)

**<font color=#1a73e8>作者：</font>** Etrit Haxholli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous and discrete flow matching are usually treated as separate constructions. This paper identifies a duality between them: projecting continuous convex-interpolant paths with one-hot targets through a position-wise argmax yields discrete convex-interpolant paths. The result requires source laws with appropriate coordinate symmetry and boundary regularity, and it makes the continuous source distribution an explicit design choice for categorical generation. We derive the induced discrete interpolation behavior for Gaussian, bounded-uniform, and centered negative-exponential sources, showing that different source geometries lead to qualitatively different transition timing and vocabulary-size dependence. Small visual diagnostics and a short language-modeling pilot suggest that these source-design effects can also appear in learned transports and early generative quality.

---


### 39. [Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations](https://arxiv.org/abs/2609.10866)

**<font color=#1a73e8>作者：</font>** Tong Li, Saunak Kumar Panda, Yisha Xiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) agents deployed in real-world environments are often vulnerable to adversarial perturbations in state observations, creating risks in safety-critical applications. Certification methods can improve robustness against adversarial perturbations by providing lower bounds on expected cumulative rewards. Existing certification methods, however, mainly focus on risk-neutral objectives. In this paper, we extend certification methods to risk-sensitive objectives by establishing lower bounds on the exponential utility of cumulative rewards under $l_{p}$-norm-bounded state adversarial perturbations ($1\leq p <\infty$). By introducing a $\phi$-divergence relaxation of the perturbation set, we formulate the risk-sensitive certification problem as a convex optimization and derive its dual to obtain a tractable approximation of the certified lower bound. We further propose an empirical method that improves certified lower bounds by selecting the training risk-aversion parameter $\beta$ independently of the risk level used during evaluation. Experiments on both OpenAI Gym environments and a machine replacement problem show that, compared to risk-neutral training, risk-averse training generally yields policies with higher certified lower bounds, particularly under larger perturbation budgets. Moreover, under both risk-neutral and risk-averse evaluation settings, increasing risk aversion during training leads to non-monotonic certification performance, where certified lower bounds initially improve but eventually decrease due to overly conservative policies.

---


### 40. [Learning Orthogonal Multi-Index Models Beyond Small Initialization: Incremental Learning, Competitive Dynamics and Symmetry](https://arxiv.org/abs/2609.10879)

**<font color=#1a73e8>作者：</font>** Mo Zhou, Weihang Xu, Simon S. Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has identified incremental learning in shallow networks trained on single-index and multi-index models. However, existing analyses often rely on simplifying settings, such as small initialization, correlation loss, or layer-wise training. These choices reduce neuron interactions and leave some feature learning dynamics under standard initialization unexplored. We study training dynamics for polynomial-width two-layer networks learning orthogonal multi-index targets under standard initialization using polynomially many samples. We first prove that incremental learning still occurs: the loss decreases sequentially according to the Hermite expansion of the target, with lower-order components learned before higher-order components recover the individual target directions. In this standard initialization regime, training also shows a competitive reallocation of parameter mass: after the total mass fits the target mean and stabilizes, mass shifts into the target subspace and then concentrates on aligned neurons. Our theoretical analysis uses slightly modified gradient flow, while vanilla gradient descent empirically exhibits the same qualitative dynamics. Technically, we introduce a symmetry-based finite-width approximation via symmetrized networks, rather than comparing directly with an infinite-width limit. This yields better control of approximation errors and may be of independent interest.

---


### 41. [AspisAI: A Canonical, Machine-Interpretable Governance Framework for Automated Multi-Standard Compliance Monitoring](https://arxiv.org/abs/2609.10881)

**<font color=#1a73e8>作者：</font>** Tsafac Nkombong Regine Cyrille, Hasan Dag, Reiner Creutzburg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organisations operating in regulated and critical-infrastructure sectors must satisfy multiple, heterogeneous cybersecurity and privacy instruments simultaneously, including but not limited to ISO/IEC~27001, the NIST Cybersecurity Framework~2.0, Cyber Essentials, and the GDPR. In practice, these obligations are managed through manual mappings, spreadsheet-based tracking, and periodic audits that are costly to maintain, inconsistent across standards, and weak in traceability. This paper presents \emph{AspisAI}, a bounded, standard-agnostic governance framework that translates selected requirements from several frameworks into a canonical, machine-interpretable control model, and evaluates submitted evidence against condition-based decision rules to produce explainable, traceable compliance determinations. Within a bounded scope of 26 representative requirements, the framework is evaluated in a controlled simulation against five governance-oriented criteria and, critically, against two external reference points that mitigate the circularity of single-author evaluation: its cross-standard mappings are validated against NIST's own published informative references, with 57\,\% exact agreement and divergences confined to same-family controls, and the framework is applied to real third-party evidence from the OpenSSF Scorecard, surfacing genuine governance gaps in a live open-source project. The controlled results, comprising full requirement encoding, 88.5\,\% mapping coverage, complete traceability, and correct detection of all introduced gaps, establish functional correctness, while the external validation provides evidence of applicability beyond the simulation. The contribution is therefore a demonstration that a canonical, provenance-preserving governance model can render multi-standard compliance both automatable and auditable.

---


### 42. [Relatively Smart II: Tractable or Semi-Supervised Instance-Optimal Learning](https://arxiv.org/abs/2609.10886)

**<font color=#1a73e8>作者：</font>** Shaddin Dughmi, Alireza F. Pour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We continue the study of relatively smart learning, introduced by Dughmi and Pour (2026), which asks a supervised learner to compete, marginal by marginal, with every distribution-fixed error guarantee soundly certifiable from unlabeled data. They showed that the One-Inclusion Graph (OIG) learner is relatively smart with a quadratic sample-complexity blowup, and that no relatively smart learner can do better, leaving open whether ERM or another natural or tractable learner achieves comparable guarantees. They also left open whether the blowup can be restricted to unlabeled data.
Our firs results shows that ERM---and in fact any proper consistent learner---is relatively smart for binary classification in the distribution-free setting. We show that a small certifiable error with $m$ samples implies a similarly small error on the uniform distribution over a random sample of size $O(m^2)$, yielding a cover of size at most $2^{m+1}$ on that sample. This suffices to control the error of proper consistent learners with $O(m^2)$ samples.
We then show that semi-supervised relatively smart learning is information-theoretically possible with a quadratic blowup only in unlabeled sample complexity and no blowup in labeled sample complexity. The learner uses a natural generalization of OIG to a leave-most-out transductive problem, where labels of part of a finite pool are revealed and the remaining labels are predicted.
Finally, this label efficiency comes at a cost in simplicity and tractability. If the hypothesis class is accessed only through an agnostic ERM oracle, any semi-supervised relatively smart learner with substantially sub-quadratic labeled-sample blowup requires super-polynomially many oracle calls. This holds even when the marginal is given explicitly, and thus also yields an intractability result for distribution-fixed learning that may be of independent interest.

---


### 43. [Symmetry-aware super-resolution of crystal orientation maps via invariant latent-space learning](https://arxiv.org/abs/2609.10898)

**<font color=#1a73e8>作者：</font>** Umang Garg, Warren Zamudio, McLean P. Echlin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crystal-orientation maps are physical fields defined only up to crystal symmetry; electron backscatter diffraction (EBSD) resolves them experimentally, but acquisition-time constraints limit spatial resolution. Unlike conventional images, EBSD data lie on the quotient space $\mathrm{SO}(3)/G$, where $G$ is the crystal-symmetry group. Standard Euclidean interpolation can therefore mix symmetry-equivalent representations and blur grain boundaries. We introduce the Symmetry-Group-Aware Super-Resolution Attention Network (SG-SRAN), which incorporates crystal symmetry and boundary preservation by design. A frozen, locally isometric encoder maps equivalent orientations to a common latent representation in which Euclidean distance approximates misorientation. Super-resolution is performed in this space, with each high-resolution token restricted to a feature-consistent local support to prevent cross-boundary mixing. A dictionary-based decoder then recovers valid orientations. Across FCC and HCP benchmarks, SG-SRAN matches 15-16 million parameter backbones using only 27-49k trainable parameters, while achieving the lowest p68 errors, highest inverse-pole-figure fidelity, and zero-shot transfer to unseen alloys.

---


### 44. [HiPerViT: A Hierarchical Perceiver-Vision Transformer Architecture for Multi-Scale Texture Recognition](https://arxiv.org/abs/2609.10917)

**<font color=#1a73e8>作者：</font>** João Pedro C. A. de Sá, Odemir Martinez Bruno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Texture recognition remains challenging for modern vision models because discriminative evidence is often carried by higher-order spatial statistics rather than by object shape alone. While Vision Transformers provide strong long-range modeling capacity, their standard object-centric representations do not explicitly expose such statistical structure, which limits texture sensitivity in fine-grained recognition settings. We present HiPerViT, a compact vision-only architecture that injects an explicit second-order statistical prior into a transformer-based recognition pipeline. The method combines global and local image views with a compact bilinear descriptor encoded as a statistical token, and integrates this token with first-order spatial representations through Perceiver-style latent distillation. This design enables direct interaction between spatial tokens and second-order feature co-occurrence statistics, providing the model with explicit access to texture-relevant information without requiring multimodal pretraining or ensemble construction. Across six texture recognition benchmarks, HiPerViT achieves consistent improvements over strong vision-only baselines under the reported evaluation protocols, including gains of +3.05 percentage points on DTD, +10.48 on GTOS-Mobile, and +10.10 on 1200Tex. Beyond benchmark performance, our analyses show that these gains are largely invariant to the backbone depth used to extract second-order statistics and to the ordering of interaction and distillation stages. This pattern suggests that the primary source of improvement is not a specific fusion topology, but the explicit availability of second-order statistical information as a first-class representational signal. These results support explicit statistical tokenization as an effective and robust design principle for texture-centric visual recognition.

---


### 45. [AUC Maximization from Biased Positive-unlabeled Data with Confidence](https://arxiv.org/abs/2609.10928)

**<font color=#1a73e8>作者：</font>** Atsutoshi Kumagai, Tomoharu Iwata, Hiroshi Takahashi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maximizing the area under the receiver operating characteristic curve (AUC) is a standard approach to imbalanced binary classification. Although positive and negative data are required for maximizing the AUC, negative data are often difficult to collect in some real-world applications due to privacy concerns or the need for specialized expertise to annotate them. Thus, AUC maximization from positive and unlabeled (PU) data has been attracting attention. Existing methods assume that labeled positive data are unbiased samples from the true positive distribution. However, this ideal assumption is often violated in practice. In this paper, we propose a method to maximize the AUC from biased PU data. To address the bias, our key idea is to exploit {\it confidence}, i.e., the probability that an instance is positive, associated with the small number of labeled positive data. We derive an estimator of the AUC risk using biased PU data with confidence, enabling AUC maximization under such bias. We further show that the rewritten AUC risk induces a Bayes-optimal AUC ranking even when the available confidence is any strictly increasing transformation of the true posterior probability. We experimentally show the effectiveness of our method on eight real-world datasets.

---


### 46. [Empirical Evaluation of Membership Inference Attacks on NLP Text Classifiers: A Baseline Study on SST-2](https://arxiv.org/abs/2609.10935)

**<font color=#1a73e8>作者：</font>** William Novak, Muhammad Abusaqer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) try to determine whether a specific record was used to train a model, a privacy risk that matters in natural language processing (NLP), where training data can contain sensitive user text. This paper presents a controlled benchmark of membership inference vulnerability for text classification on the GLUE SST-2 sentiment dataset. A TF-IDF + Logistic Regression pipeline and a fine-tuned DistilBERT classifier are compared under a loss-threshold MIA, with utility measured by development accuracy and macro F1. DistilBERT reached 0.9466 accuracy and 0.9460 macro F1 against 0.8756 and 0.8727 for Logistic Regression, yet both models leaked membership signal (Attack AUC 0.5615 and 0.5800, respectively). Two mitigations were tested. Stronger regularization reduced leakage for Logistic Regression at a visible utility cost, whereas fine-tuning DistilBERT for 2 epochs instead of 3 reduced leakage with negligible accuracy loss. Lightweight training adjustments can improve the privacy-utility trade-off without complex defenses.

---


### 47. ["Coder first, advocate second, college student third": The Liminality of Going to College as a Blind Computing Student](https://arxiv.org/abs/2609.10942)

**<font color=#1a73e8>作者：</font>** Isabela Figueira, Josahandi M. Cisneros, Stacy M. Branham  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Blind or low vision (BLV) students are less likely to graduate from college, particularly in computing. Prior work documents accessibility challenges in high school and college, but we lack understanding of the transition process that produces this "leaky pipeline." To address this, we interviewed ten BLV college students about going to college to study computing. We analyzed our data through the lens of life transition, specifically Intersecting Liminality. Our findings reveal that some BLV students face such immense digital accessibility and college acclimation barriers that the only way forward as coders is to take on a "second job" as a blind advocate or drop out of the computing major. We argue that the college transition is a critical point for analysis and technological intervention, and further, that Intersecting Liminality provides a useful lens for HCI scholars to unpack the compounding challenges that prevent some BLV students from completing computing degrees.

---


### 48. [Robust Multimodal Sentiment Analysis with Incomplete Modalities via Semantic-aware Completeness based Reconstruction](https://arxiv.org/abs/2609.10950)

**<font color=#1a73e8>作者：</font>** Han-Jun Choi, Byunggill Joe, Saim Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multimodal sentiment analysis studies increasingly adopt text-centric fusion approaches to exploit the rich sentiment information inherent in the textual modality. However, these approaches often suffer from performance degradation during inference due to partially missing or noisy data in real-world scenarios, especially when sentiment-related cues are missing. To address this issue, we introduce a new completeness estimation approach that quantifies the degree of sentiment-relevant information preserved in incomplete data to guide the reconstruction of missing semantics. Furthermore, we propose a training strategy that stabilizes multi-task learning while jointly optimizing sentiment prediction and completeness estimation. Extensive experiments and in-depth analyses on three benchmark datasets demonstrate that the proposed approach enables more accurate semantic reconstruction, leading to more precise sentiment prediction.

---


### 49. [Empirical Evaluation of Data Poisoning Attacks in Supervised Learning](https://arxiv.org/abs/2609.10952)

**<font color=#1a73e8>作者：</font>** Toshif Khan, Muhammad Abusaqer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data poisoning corrupts training data to degrade a model or to plant attacker-controlled behavior. This study evaluates two representative training-time attacks, label flipping and backdoor poisoning, on MNIST and Fashion-MNIST with three baseline classifiers: Logistic Regression, Linear SVM, and Random Forest. Clean training is compared with poisoning rates of 5%, 10%, and 20% using clean-test accuracy, macro-precision, macro-recall, macro-F1, and, for backdoors, attack success rate. Label flipping caused clear degradation, largest for Logistic Regression and Linear SVM, while Random Forest stayed comparatively stable. Backdoor poisoning reached attack success rates from 0.9667 to 1.0000 on both datasets and all three models while often keeping clean-test performance near baseline. The results separate indiscriminate poisoning, which shows up in standard metrics, from targeted backdoor poisoning, which stays comparatively stealthy while embedding highly effective malicious behavior, and they support security-oriented evaluation beyond conventional clean-test metrics.

---


### 50. [Measuring the Value of World-Model Updates: A Counterfactual Utility Protocol for Continual Adaptation](https://arxiv.org/abs/2609.10954)

**<font color=#1a73e8>作者：</font>** Anqi Peter Li, Kaden Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual world models must decide whether new data justify changing the model. Fixed replay schedules and prediction-error triggers specify when to update, but neither reveals the value of an individual update: one deployment run cannot show how the same model would have performed at that moment had it held its parameters. We introduce the fork ledger, which branches a deployment stream at pre-registered decision points into matched update and hold continuations under common random numbers. It evaluates both continuations on the same episodes and records $\Delta R = R_{\mathrm{update}} - R_{\mathrm{hold}}$. Always applying one fixed update mechanism lowers return on all three simulated control tasks: CartPole ($-144.0$; checkpoint-bootstrap $95\%$ CI $[-185.4,-116.1]$, against a converged return near $650$), Walker ($-82.8$; $[-101.1,-61.7]$) and Cheetah ($-18.6$; $[-29.0,-6.6]$). Divergence is an outcome of applying the update, so the estimand counts every attempted fork; restricted to the $693$ of $720$ that did not collapse, CartPole and Walker are unchanged in sign ($-113.4$ and $-82.1$) and Cheetah becomes unresolved ($-3.9$; $[-17.5,+13.0]$). The task is the unit of inference: each contributes $240$ attempted forks over five pretrained checkpoints crossed with two drift directions. The ledger makes counterfactual utility observable for a fixed mechanism, allowing triggers to be judged by the updates they select rather than by surprise detection alone.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
