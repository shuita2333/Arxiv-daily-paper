# 📦 其他研究 | 2026年07月09日

> 本类共 **195** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-195](./part-04.md)

---

### 1. [Proof of Execution: Runtime Verification for Governed AI Agent Actions](https://arxiv.org/abs/2607.05397)

**<font color=#1a73e8>作者：</font>** James Rhodes, George Kang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent systems increasingly execute rather than advise. When an AI agent queries regulated data, invokes effectful tools, and mutates persistent state, correctness is not captured by whether a terminal output looks plausible. The operative questions are whether each step was authorized under a contract, whether the recorded history is tamper-evident, and whether the trajectory can be reconstructed deterministically. We formalize this as runtime proof of execution. An execution is a triple $x = (C, T, R)$: a contract $C$, an Execution Causal Event Stream (ECES) $T$, and a replay context $R$. A well-formedness predicate and five validator-checkable invariants form the PoE validity predicate. Five semantic guarantees describe authorization, path compliance, null effect on deny, history integrity, and replayability. We prove soundness under explicit cryptographic and deployment assumptions: any PPT adversary that produces a PoE-valid execution violating a semantic guarantee yields a signature forgery, a hash collision, or a quantified deployment-failure event. The Prime Execution Model (PEM) separates planning, enforcement, effect, and recordkeeping into distinct authority planes; a lemma reduces trace completeness to Effector-exclusive credentialing. An Execution Attestation Certificate is issued only when PoE = 1. In a single-node TypeScript prototype, PoE adds approximately 2.7 ms on a minimal flow and 4.4% overhead on concurrent batch workloads; a standard eight-event trace compresses to approximately 1.1 KB; injected Gateway-bypass and trace-mutation attacks are rejected. PoE does not replace consensus, TEEs, or zkVMs; it binds authorization, effect, history, and replay into a single runtime-checkable object so that governed execution becomes attestable under contract.

---


### 2. [How Personas Can Influence Agents to Play Split or Steal](https://arxiv.org/abs/2607.05398)

**<font color=#1a73e8>作者：</font>** Carlos Leon, Alexandre Rodrigues, Pedro Gamito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personas are often employed to guide large language model agents, yet their effectiveness in shaping strategic behavior in social dilemma settings remains uncertain. To address this, we examined the impact of persona prompts in an iterated Split or Steal game where persona-driven agents interacted with a Virtual Human (VH) controlled by a fixed prompt. Agents were instantiated from four open models (Ministral 3:3b, phi4:14b, Gemma3:12b, and Gemma4:e4b) at two temperature settings (0.3 and 0.7) and deterministic decision with zero temperature, while the VH was powered by GPT 4.1 mini. Across 160 sessions of 15 rounds each conducted in European Portuguese, mutual Split outcomes dominated (roughly 74 percent of rounds), with exploitation occurring in fewer than 11 percent of rounds. Model choice significantly influenced behavior: phi4 and Ministral 3:3b remained consistently cooperative across temperatures, whereas Gemma3:12b and Gemma4:e4b exhibited more varied strategies and outcomes. Analyses based on Big Five personality traits indicated that Prosocial and Principled personas were most consistently cooperative, while Analytical personas were more likely to exploit the VH. Topic analysis revealed that friendship-related dialogue aligns with Split decisions, whereas money and vengeance-related content is more prevalent in Steal outcomes; sentiment labels were predominantly neutral or happy and provided limited additional explanatory value. These findings characterize the interaction between persona prompts and model differences in repeated trust games and serve as a baseline for planned virtual reality studies involving human participants interacting with an embodied VH.

---


### 3. [How Stable Is a PNT Resilience Score? Decision-Instability of Single-Number Resilience Ratings under Framework-Aligned Weighting](https://arxiv.org/abs/2607.05415)

**<font color=#1a73e8>作者：</font>** Chakshu Baweja  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Authoritative positioning, navigation, and timing (PNT) resilience frameworks (the DHS Resilient PNT Conformance Framework, RPCF, and peers) define what resilience means but supply only self-attestation: a checklist or a maturity Level, with no engine and no measurement. We build the missing measurement layer as an open, deterministic scoring engine over a PNT simulator, emitting per-dimension sub-scores traceable to a scenario and an oracle, and ask whether a single composite score or maturity Level is a stable basis for a decision. Across seven architectures spanning cross-dimension tradeoffs, a Dirichlet simplex over the seven RPCF categories, and a five-threat ensemble, the answer splits in two. The composite winner is stable under active denial and under near-equal weightings (about 1 percent flip rate), so a single number is safe precisely where one design dominates; but re-weighting alone flips it in up to 22 percent of draws under nominal conditions, where designs contend, a known composite-indicator sensitivity. The sharper, weighting-invariant failure is categorical: a weakest-link maturity Level (our minimum-over-categories operationalization of the RPCF ladder, not the framework's rule) depends on the threat assumed, not the architecture, changing for one architecture in seven. Because the composite rewards declared techniques, a constructed single-band receiver declaring all seven outscores a more resilient system: self-attestation can be gamed by declaration. And apparent fourfold GNSS redundancy reduces, by the definition of a shared common-mode failure domain, to an effective diversity of one. Conclusions hold under +/-20 percent perturbation of every driver within the reduction. We report per-dimension sub-scores with provenance and a rank range, not a phantom single number. A self-assessment aligned to RPCF v2.0, not a certification.

---


### 4. [Text Distance from Nested and Hierarchical Repetitions: A Compression-Based Perspective](https://arxiv.org/abs/2607.05416)

**<font color=#1a73e8>作者：</font>** Xiaojun Hu, Jing Wang, Jingwen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a new method for structural sequence analysis grounded in Algorithmic Information Theory (AIT). At its core is the Ladderpath approach, which extracts nested and hierarchical relationships among repeated substructures in linguistic sequences -- an instantiation of AIT's principle of describing data through minimal generative programs. These structures are then used to define three distance measures: a normalized compression distance (NCD), and two alternative distances derived directly from the Ladderpath representation. Integrated with a $k$-nearest neighbor classifier, these distances achieve strong and consistent performance across in-distribution, out-of-distribution (OOD), and few-shot text classification tasks. In particular, all three methods outperform both gzip-based NCD and BERT under OOD and low-resource settings. These results demonstrate that the structured representations captured by Ladderpath preserve intrinsic properties of sequences and provide a lightweight, interpretable, and training-free alternative for text modeling. This work highlights the potential of AIT-based approaches for structural and domain-agnostic sequence understanding.

---


### 5. [Abductive Corroboration of Probabilistic AI Models for Forensic Synthetic Media Detection](https://arxiv.org/abs/2607.05434)

**<font color=#1a73e8>作者：</font>** Junade Ali  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) models, at their core, apply general learnings from broad datasets to individual circumstances using probabilistic behaviour. This inductive approach stands in contrast to deductive reasoning approaches which seek to prove conclusions from their premises. However, research has shown that deductive reasoning with AI models is a challenging problem and in the real-world it may not always be feasible. An alternative way forward is to leverage abductive reasoning, seeking to corroborate the output of multiple approaches to identify the most likely conclusion from the factual matrix. We apply this to synthetic media detection in forensic settings, and find we are able to disproportionately lower the risk of false positives to true positive recall. We also provide the first empirical evaluation of OpenAI's rollout of SynthID on synthetic images and evaluate how complementary different synthetic media detection approaches are.

---


### 6. [Statistically Meaningful Geometry and Gauge Symmetry Breaking: A Geometric Foundation for Scientific Discovery and Intelligence Emergence](https://arxiv.org/abs/2607.05436)

**<font color=#1a73e8>作者：</font>** Bing Cheng, Yi-Shuai Niu, Howell Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid scaling of over-parameterized machine learning architectures, particularly LLMs, raises a profound crisis: do these systems exhibit genuine intelligence, or are they merely sophisticated statistical pattern matchers? Classical flat Euclidean statistics cannot differentiate continuous interpolation from the autonomous discovery of novel causal laws. To resolve this, we introduce Statistically Meaningful Geometry (SMG), a framework modeling over-parameterized learning systems as infinite-dimensional non-parametric Orlicz fiber bundles. We prove that under persistent out-of-distribution (OOD) stimuli governed by unmodeled causal mechanisms, continuous optimization fails. Unmodeled variance is rejected by the visible horizontal base manifold, leaking into the unobservable vertical fiber space and generating an accumulation of Active Acausal Tension. Driven by the statistical manifold's non-linear curvature, this tension inevitably strikes a conjugate focal boundary ($T_{\text{crit}} = \pi^2 / K_{\text{max}}$), triggering localized volumetric collapse and a catastrophic matrix singularity ($[G_f]^{-1} \to \infty$). We demonstrate this geometric breakdown acts as the strict non-equilibrium trigger for a Gauge Symmetry Break (GSB). The system purges hidden tension from unobservable gauge redundancies, spontaneously crystallizing a new, mathematically independent horizontal coordinate axis. This non-parametric phase transition registers as a discrete $+1.0$ integer step-jump in observable Structural G-Entropy. By decoupling parameter charts and subjecting emergent axes to a Minimal Energy Path Criterion and a Causal Invariance Filter, we distinguish genuine discovery from malignant hallucinations. Ultimately, SMG provides a parameter-free, falsifiable dashboard to mathematically certify true intelligence, transforming AI for Science into an engine of autonomous paradigm shifts.

---


### 7. [Design-CP: Context Parallelism for Design of Protein Nanoparticles](https://arxiv.org/abs/2607.05439)

**<font color=#1a73e8>作者：</font>** Lorenzo Tarricone, Helen E. Eisenach, Aiko Muraishi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many all-atom generative protein models can in principle design large multimeric complexes by jointly modelling all chains, but their quadratic token- and atom-pair representations quickly exceed single-GPU memory as the number of chains and residues modelled grows. We introduce Design-CP, two context-parallel (CP) inference strategies for RFdiffusion 3 (1D row-sharding and 2D grid sharding with ring attention) that distribute the quadratic activations across a multi-GPU mesh while preserving pretrained weights. We characterise their scaling when sampling icosahedral assemblies, showing that the maximum feasible asymmetric subunit (ASU) size grows with the expected square-root trend in GPU count and that 2D sharding achieves better wall-clock scaling. Moreover, we show how strong point-group symmetry constraints make CP usable out of the box for end-to-end, all-atom design of icosahedral nanoparticles, yielding favourable in silico structural and interface metrics. Finally, we demonstrate octahedral nanoparticle design on a small cluster of workstation-grade 16GB GPUs, illustrating how Design-CP can be a practical path towards democratising large-assembly protein design.

---


### 8. [Geometry-Aware Infrastructure-Anchored Denoiser for UWB Sensing and Work-Zone Reconstruction](https://arxiv.org/abs/2607.05449)

**<font color=#1a73e8>作者：</font>** Weizhe Tang, Jiaxi Liu, Junwei you 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate work-zone geometry perception is critical for intelligent transportation systems, and ultra-wideband sensing offers a low-cost approach for infrastructure-aided reconstruction. However, outdoor UWB ranging is often degraded by non-line-of-sight propagation, burst noise, and long-tail errors, which can distort downstream spatial reconstruction. We present GAIA, a geometry-aware, infrastructure-anchored learning framework that couples temporal range modeling with latent anchor-layout estimation and deterministic distance projection. GAIA preserves range denoising as the supervised task while orienting the learned distances toward boundary-consistent reconstruction. We evaluate GAIA on a real-world outdoor UWB dataset with synchronized UWB, GNSS, and IMU measurements, and further test robustness using a real-data-calibrated stress-test simulator. GAIA achieves the lowest overall range MSE and highest polygon IoU among evaluated filtering-based and learning-based baselines, reducing MSE by 18.4% and improving polygon IoU by 15.5% over PoseMLP. These results show that geometry-aware range denoising provides an effective path toward spatially coherent work-zone reconstruction.

---


### 9. [The Granularity Paradox: How Temporal Disaggregation Inflates In-Sample Fit and Compounds Out-of-Sample Error](https://arxiv.org/abs/2607.05450)

**<font color=#1a73e8>作者：</font>** Hugo Moreira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores the "Granularity Paradox" in time-series forecasting, wherein finer temporal disaggregation (e.g., Monthly to Weekly/Daily) improves in-sample diagnostics and dataset size (N), but degrades out-of-sample accuracy due to recursive error compounding over longer horizons (H). Conversely, coarse aggregation (Annual) eliminates recursive error propagation but reduces data available to estimators. We formalize this trade-off and benchmark 10 models - spanning naïve, statistical, machine learning, and deep learning architectures - across six granularities using a 13-year public procurement dataset. The empirical results reveal a non-monotonic threshold structure: recursive autoregressive and seasonal models degrade substantially under high-frequency forecasting (e.g., Holt-Winters reaches a Test R-squared of -151 and TPFE of 425.85% at the Daily grain), while the LSTM traces a U-shaped error curve, worsening from Monthly (19.66%) through Bi-Weekly (35.94%) before overcoming the error propagation penalty at Daily (TPFE of 4.35%, R-squared of 0.66). Linear Regression remains stable across all granularities (16.3-17.0% TPFE), confirming that the paradox is driven by recursive feedback topology, not model complexity. The results demonstrate that standard pointwise metrics (RMSE, MAE) systematically mask cumulative error propagation, and that evaluating forecasts without goal-dependent cumulative metrics produces misleading assessments of model adequacy. We introduce a consensus-dissensus diagnostic comparing the directional behaviour of pointwise metrics against cumulative TPFE across granularities, enabling the identification of models whose standard diagnostics mask systematic error propagation.

---


### 10. [Exogenous Dropout: A Simple, Strong Baseline for Corruption-Robust Time Series Forecasting with Covariates](https://arxiv.org/abs/2607.05452)

**<font color=#1a73e8>作者：</font>** Hao Hu, Xue-shan Ai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasters that use exogenous covariates are fragile in deployment: when those covariates are noised, temporally misaligned, or missing, strong exogenous-fusion and exogenous-adapted models can degrade far above the endogenous-only floor. We study whether such robustness requires specialized architectures, or whether it can be obtained through a simple training intervention. We propose exogenous dropout, a model-agnostic method that randomly zeros whole exogenous channels during training. Across electricity-price forecasting, reservoir hydrology, and meteorology, exogenous dropout substantially improves robustness under Gaussian noise, temporal misalignment, and fully missing channels, while preserving clean accuracy. Applied to a dual-correlation network, it yields the most robust model in our experiments, outperforming a deliberately strong bounded architectural foil, BoundEx, which combines a learnable gate, a fallback residual to the endogenous backbone, and per-channel exogenous FiLM modulation. Architecture-by-dropout ablations, gate-behavior diagnostics, and a representation-level bound show that explicit architectural boundedness is not necessary for this robustness: an unbounded model trained with exogenous dropout is more robust than the bounded model in every domain. We release a corruption-robustness benchmark and recommend exogenous dropout as a simple, strong baseline for future work on time series forecasting with covariates.

---


### 11. [Empirical Minimal-Realisation Compression of Deep Neural Networks via Controllability-Observability Tests](https://arxiv.org/abs/2607.05457)

**<font color=#1a73e8>作者：</font>** Anis Hamadouche, Amir Hussain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often contain substantial hidden-state redundancy, but most compression methods operate directly on weights, neurons, or quantised representations without explicitly characterising the dynamical role of internal states. This paper proposes a controllability-observability framework for empirical state-order reduction of deep neural networks. By viewing a trained network as a depth-indexed nonlinear dynamical system, we construct data-driven reachability, observability, and balanced Gramians from hidden-state snapshots and output Jacobians. The resulting A/B/C tests estimate layer-wise reachable, observable, and jointly reachable--observable ranks. These ranks are then used not only as diagnostic measures of hidden-state redundancy, but also as actual compressed layer widths for realised reduced networks. Experiments on MNIST and CIFAR-10 compare the proposed balanced realisation against projection-based reduction, unstructured pruning, structured pruning, low-rank SVD, dynamic INT8 quantisation, and linear baselines. On MNIST, a four-layer SiLU DNN is reduced from state order 1024 to 277, giving 72.95% state compression and 73.48% parameter compression, while maintaining 95.45% accuracy compared with 96.60% for the full model. On CIFAR-10, a larger SiLU DNN is reduced from state order 4608 to 1339, giving 70.94% state compression and 83.09% parameter compression, while preserving accuracy from 54.45% to 54.44% and reducing CUDA inference latency by approximately 3X. The results show that balanced reachable-observable ranks provide a principled empirical minimal-realisation criterion for designing compact neural architectures with little or no loss in accuracy.

---


### 12. [AdaStop: Cost-Aware Early Stopping for DNN Test Selection](https://arxiv.org/abs/2607.05461)

**<font color=#1a73e8>作者：</font>** Bonan Shen, Wei-Jung Huang, Xin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing methods for testing deep neural networks (DNNs) primarily prioritize test inputs likely to reveal model faults under a fixed labeling budget. In practice, choosing that budget is difficult: too little testing misses failures, while too much incurs unnecessary labeling costs. This work studies the stopping problem in DNN testing. We formulate testing as a cost--benefit decision process in which labeling an input incurs cost $c$ and discovering a fault yields value $v$. Based on this formulation, we introduce \textit{AdaStop}, a framework that estimates the marginal fault discovery rate during testing and stops labeling when the estimated rate falls below the threshold $\tau = c/v$. Experiments across multiple datasets, architectures, and selection strategies show that $65$--$84\%$ of faults can be discovered using only $9$--$31\%$ of the labeling budget.

---


### 13. [Evaluating calibrated refusal and safe usefulness in dual-use biology settings](https://arxiv.org/abs/2607.05462)

**<font color=#1a73e8>作者：</font>** Edwin H. Wintermute, Harmon Bhasin, Christina M. Agapakis 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As AI agents are incorporated into life science workflows, the capabilities that speed discovery might also enable misuse. We present BioSecBench-Refusal, a benchmark for risk identification and refusal behavior for biological research tasks. The benchmark pairs 61 Routine tasks, legitimate analyses adapted from the published literature, with 46 Red-Team tasks, fictional scenarios that resemble real research but conceal a biosecurity hazard. Across 16 model-harness configurations, refusal rates ranged from 7\% to 74\% on Routine tasks and 1\% to 62\% on Red-Team tasks, with many configurations refusing legitimate Routine work at comparable or higher rates than concealed hazards. Refusals were most often triggered by provider API filters applied prior to agentic reasoning. However, models given room to reason showed the potential to identify more real threats. We release BioSecBench-Refusal as a tool for model developers to calibrate capability and caution for agentic biotech R\&D.

---


### 14. [Learnable Weighting of Intra-Attribute Distances for Categorical Data Clustering with Nominal and Ordinal Attributes](https://arxiv.org/abs/2607.05464)

**<font color=#1a73e8>作者：</font>** Yiqun Zhang, Yiu-ming Cheung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of categorical data clustering generally much relies on the distance metric that measures the dissimilarity degree between two objects. However, most of the existing clustering methods treat the two categorical subtypes, i.e. nominal and ordinal attributes, in the same way when calculating the dissimilarity without considering the relative order information of the ordinal values. Moreover, there would exist interdependence among the nominal and ordinal attributes, which is worth exploring for indicating the dissimilarity. This paper will therefore study the intrinsic difference and connection of nominal and ordinal attribute values from a perspective akin to the graph. Accordingly, we propose a novel distance metric to measure the intra-attribute distances of nominal and ordinal attributes in a unified way, meanwhile preserving the order relationship among ordinal values. Subsequently, we propose a new clustering algorithm to make the learning of intra-attribute distance weights and partitions of data objects into a single learning paradigm rather than two separate steps, whereby circumventing a suboptimal solution. Experiments show the efficacy of the proposed algorithm in comparison with the existing counterparts.

---


### 15. [CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration](https://arxiv.org/abs/2607.05465)

**<font color=#1a73e8>作者：</font>** Hairui Zhu, Yiying Yang, Tengjin Weng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex image creation and editing often require more than a single generation or editing model. A user request may involve synthesizing images, localizing objects, segmenting regions, editing selected content, compositing intermediate assets, reading text, and enhancing the final result. Such tasks shift multimodal agents from perception-augmented reasoning to manipulation-centered visual creation, where tools must actively transform visual states rather than merely inspect them. However, existing multimodal tool-use agents are mostly optimized for perception, search, or domain-specific editing, and lack large-scale supervision for executable image-creation trajectories. In this paper, we introduce CanvasCraft, a large-scale multimodal tool-use dataset for complex image creation and editing, and \textbf{CanvasAgent}, a tool-augmented multimodal agent that learns to orchestrate heterogeneous visual tools through multi-turn interaction. CanvasCraft contains 140K fully annotated executable trajectories and 10K
RL task specifications. CanvasAgent is first trained with SFT to learn executable reasoning-action trajectories, and is then optimized with GRPO using a hybrid reward that combines outcome- and process-level signals. During rollout, CanvasAgent inspects intermediate results, tracks visual assets, and adapts tool decisions to the evolving visual state. Experiments evaluate both final image quality and trajectory behavior, demonstrating the effectiveness of CanvasAgent and the proposed dataset for complex multi-tool image creation workflows.

---


### 16. [A Task-Driven Evaluation of UAV Detection and Tracking under Synthetic Fog](https://arxiv.org/abs/2607.05467)

**<font color=#1a73e8>作者：</font>** Amir Pouladi, Vesal Ahsani, Haijun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fog severely degrades the visibility of small unmanned aerial vehicles (UAVs) in skydominant, long-range imagery, reducing the reliability of downstream detection and tracking. This paper presents a task-driven evaluation framework that links depth-aware synthetic fog generation, image restoration, object detection, and tracking within a unified pipeline. Given the practical difficulty of collecting and annotating foggy UAV scenes, synthetic fog is generated from real clear-weather outdoor images containing UAV targets using monocular depth estimation and the atmospheric scattering model. Representative restoration methods from classical, convolutional neural network (CNN)-based, and transformer-based families are first compared, after which the selected restoration model is integrated into the downstream perception pipeline. Detection is evaluated under both clean-only and fog-inclusive training regimes using multiple detector variants, while tracking-by-detection is assessed on clean, foggy, and restored video sequences. Beyond image-level restoration metrics, the study evaluates how fog and restoration affect detection robustness and tracking performance. The results show that fog substantially degrades both detection and tracking, primarily through increased missed detections. Fog-inclusive training provides the most consistent improvement in robustness, whereas test-time restoration is most beneficial when the detector has been trained only on clean imagery. These findings show that restoration quality does not necessarily translate into proportional gains in downstream perception and therefore should be evaluated jointly with detection and tracking performance.

---


### 17. [Breaking Structural Isolation: Scalable Graph Clustering via Community-Aware Sampling and Structural Entropy](https://arxiv.org/abs/2607.05469)

**<font color=#1a73e8>作者：</font>** Jingyun Zhang, Hao Peng, Jianxin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised graph clustering is a fundamental technique for uncovering underlying semantic patterns in large-scale networks. Although Graph Contrastive Learning has demonstrated promising performance, existing methods often suffer from the "structural isolation" issue during mini-batch training, making it challenging to capture cohesive community structures that characterize the global topological distribution. To address these challenges, we propose SCISE, a Scalable unsupervised graph Clustering framework that preserves structural Integrity by synergizing community-aware sampling with constrained Structural Entropy. Specifically, we first introduce the Structural Entropy Community Constraint operator (SECC), which optimizes structural information within a constrained solution space to mitigate community fragmentation and enhance partition cohesion. Second, to prevent global information loss during batch training, we design a Community-Aware Sampling Expansion (CSampE) mechanism that incorporates the community context of target nodes into sampling batches, effectively breaking structural barriers and preserving topological integrity. Finally, we devise a Structural Contrastive Learning (StructCL) module that refines edge weights based on intra-batch structural similarity, guiding the encoder to learn representations in a higher-order structural space. Extensive experiments on six mainstream benchmark datasets demonstrate that SCISE significantly outperforms state-of-the-art algorithms, with ablation studies and robustness analyses further validating its effectiveness and reliability for real-world large-scale graphs.

---


### 18. [Binocular Gaze Estimation with Single Camera and Single Light Source](https://arxiv.org/abs/2607.05473)

**<font color=#1a73e8>作者：</font>** Tongbing Huang, Yang Fu, Yunfei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> According to commonly consented theories, the minimum hardware requirement for gaze tracker is one camera and two light sources to realize gaze estimation with free head movements. However, in some scenarios such as eye tracking on mobile devices, it is preferable to use less components, especially light sources. We propose a gaze estimation method with one camera and one light source. A "virtual light source" is introduced, which is geometrically placed symmetrically to the real light source with respect to the camera, and generates a "virtual glint" in the acquired image. We estimate the "virtual glint" by exploiting the relationship between the distance between two pupils and two glints in the captured image, and estimate the gaze with polynomial regression assuming two light sources are available. A new normalization factor for regression method is verified, which turns out to be practical for one-glint system. The performance is proved to be acceptable, while degradation is noticed compared to system with two actual light sources.

---


### 19. [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](https://arxiv.org/abs/2607.05474)

**<font color=#1a73e8>作者：</font>** Yuanmin Xie, Xiangfan Wu, Wenhao Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Algorithmic Complexity Vulnerabilities (ACVs) arise when adversarial inputs trigger worst-case execution behavior, causing severe performance degradation or Denial-of-Service conditions. A key but underexplored source is shadow complexity: non-trivial computational costs hidden inside seemingly benign standard library APIs. Because these costs are invisible at call sites, attackers can exploit them to induce unexpected superlinear runtime behavior. Existing ACV detectors often rely on fuzzing, symbolic execution, or hybrid analysis, but they are usually language-specific, require substantial manual effort to construct harnesses, and depend on heavy runtime instrumentation.
We present ShadowProbe, a scalable and language-extensible framework for discovering ACVs through lightweight static analysis, automated reconstruction of execution contexts, and Large Language Model (LLM) assisted test generation. ShadowProbe uses a structured multi-stage pipeline: it statically screens for candidate functions guided by shadow-complexity signals, reconstructs minimal executable contexts from project-level symbols, and synthesizes size-controlled inputs to probe worst-case behavior. It then validates candidates using execution-time measurements and robust statistical growth inference, separating true algorithmic blowups from runtime noise such as garbage collection and JIT compilation effects.
We evaluate ShadowProbe on the WISE benchmark, where it consistently improves analysis efficiency over existing approaches. We further apply it to large-scale systems including CPython, the JDK, Zig, Rustc, and vLLM, uncovering many previously unknown ACVs, many of which have been confirmed and partially remediated by maintainers. These results show that ShadowProbe can identify hidden algorithmic risks across diverse real-world codebases.

---


### 20. [InvWeaver: Deductive Feedback for Invariant Synthesis in Interacting-Loop Programs](https://arxiv.org/abs/2607.05478)

**<font color=#1a73e8>作者：</font>** Guangyuan Wu, Weining Cao, Zehui Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Loop invariant inference is a fundamental yet challenging problem in program verification. Recent LLM-aided guess-and-check techniques have shown strong performance on single-loop programs, but they often struggle with programs containing multiple interacting loops. This paper presents InvWeaver, a neuro-symbolic framework for synthesizing invariants for such programs. The key idea is to expose inter-loop dependencies and propagate proof obligations through a combination of loop-level abstraction, obligation-guided inference, and weakest-precondition-based refinement. We evaluate InvWeaver on a comprehensive benchmark suite, including a newly curated dataset derived from classic algorithms. Experimental results show that InvWeaver substantially outperforms existing invariant inference methods, solving 72 out of 82 multi-loop benchmark problems and maintaining strong performance on single-loop tasks.

---


### 21. [Privilege and confidentiality in generative AI workflows](https://arxiv.org/abs/2607.05479)

**<font color=#1a73e8>作者：</font>** Václav Janeček, Thomas Melham  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) systems store and process client data in three distinct ways: in the model's parameters through training and memorisation, in the context window during a live session, and in knowledge databases for retrieval-augmented generation (RAG). Each mode creates different and often counter-intuitive risks to confidentiality and legal professional privilege, and each calls for specific governance responses. Drawing on the first English and American decisions to address privilege and generative AI, UK and Munir v Secretary of State for the Home Department and United States v Heppner, on the orthodox privilege authorities against which those decisions must be read, and on recent computer science research, we explain the three modes of data storage and processing in terms accessible to practitioners and analyse the legal consequences of each. We then situate the analysis within the regulatory framework governing solicitors in England and Wales and within the ordinary principles of professional negligence, arguing that the standard of effective information governance (and with it the benchmark against which negligence and misconduct will be measured) is changing. Although we write primarily for SRA-regulated practitioners, our data-governance analysis is framed to extend to any jurisdiction in which the protection of privilege or professional secrecy depends on demonstrable confidentiality. The ultimate aim of this article is to help legal services professionals understand salient data leakage risks in GenAI systems and thereby facilitate a more responsible deployment of GenAI on client data and other sensitive material.

---


### 22. [Full-range Binary Classifier Calibration for Stable Model Updates in Production](https://arxiv.org/abs/2607.05481)

**<font color=#1a73e8>作者：</font>** Konstantin Berlin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detection models running in adversarial environments face a malicious distribution that drifts rapidly while the benign distribution stays comparatively stable, so teams retrain and redeploy constantly to stay ahead of new threats. Retraining tends to change the output prediction scores, which breaks downstream users of the model. For these security-oriented models we need consistent false-positive rate (FPR) across all output values, whereas standard probability-calibration methods target class probability rather than an FPR contract. We introduce a method built on top of existing calibration primitives that targets the whole FPR curve, giving scores a consistent FPR meaning across deployments. On one held-out split, the observed relative FPR error was at most 2.3% from 10% down to 0.1% FPR and 7.2% at 0.01% FPR. The shipped artifact remains under 200 KB in measurements across calibration sets from 1K to 10M benign samples.

---


### 23. [Ground3D-LMM: Fine-Grained 3D Point Grounding and Spatial Reasoning with LMM](https://arxiv.org/abs/2607.05493)

**<font color=#1a73e8>作者：</font>** Amol Harsh, Zongyan Han, Jean Lahoud 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural-language queries about 3D environments become actionable when responses are verifiable and metric. Verifiability requires explicit grounding to the referred 3D region, while metric answers report physical measurements in real-world units (e.g., size, thickness, clearance, and distance). Existing 3D large multimodal models (LMMs) approaches remain limited: conversational systems typically respond without explicit 3D grounding, while 3D grounding models are not designed for interactive, metric-aware dialogue. In this paper, we present Ground3D-LMM, a unified model that takes a point cloud and an optional RGB image as input and supports 3D spatial conversation with (i) point-grounded responses and (ii) metric numeric outputs at both object and part granularity, including multi-object queries. To evaluate this intersection of grounding and measurement, we define the 3D Grounded Measurement task, which requires predicting the referred 3D region and the corresponding metric quantities in real-world units. We introduce a large-scale dataset built on ScanNet and ScanNet++ datasets with dense object and part annotations and roughly 2.5M question-answer pairs spanning eight tasks, along with a manually verified test set. Extensive experiments on multiple datasets and tasks show that our proposed Ground3D-LMM model provides a strong baseline for grounded, metric-aware 3D conversational understanding. Our dataset and model are publicly available.

---


### 24. [Statistical Adversaries: Natural Backdoor-like Features in Vision Datasets](https://arxiv.org/abs/2607.05516)

**<font color=#1a73e8>作者：</font>** Paul K. Mandal, Pavan Reddy, Tristan Malatynski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model-specific adversarial attacks have been extensively studied. We study a different failure mode: naturally occurring statistical signals in vision data that can behave like backdoor-like triggers without being maliciously inserted. We call these signals statistical adversaries. We analyse Imagenet to find patterns that are strongly linked to certain labels. We then use statistical controls to remove random correlations from our candidate signals. Finally, we demonstrate that these signals directly and predictably alter model predictions. These statistical adversaries are more targeted than generic corruptions and transfer across different model architectures. This suggests that some vulnerabilities are driven by dataset structure and distribution rather than a single model's idiosyncrasies. We conclude that ordinary datasets can contain exploitable adversarial surfaces even in the absence of poisoning, and suggest that dataset audits should treat spurious structure not only as a source of bias or interpretability failure, but also as a latent attack surface for vision models.

---


### 25. [aiAuthZ: Off-Host, Identity-Bound Authorization for AI Agents](https://arxiv.org/abs/2607.05518)

**<font color=#1a73e8>作者：</font>** Sai Varun Kodathala  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents issue tool calls on the basis of text they cannot verify, so any party who controls part of the context can forge the appearance of authority. I evaluate 15 contemporary language models against eight attack scenarios derived from a published corpus of real agent incidents and find that refusal varies from 100% down to 38% across fully evaluated models; the most expensive model refused only half of the attacks despite a twentyfold price spread. I present aiAuthZ, an authorization gateway that moves the safety decision off the agent's host. Before a tool call executes, the gateway verifies caller identity with a per-message HMAC-SHA256 signature bound to a single-use nonce and a timestamp window, and it evaluates a role-based and argument-level policy that the agent can neither read nor modify. Every decision joins a SHA-256 hash-chained audit log, and each accepted message yields an HMAC-authenticated QR receipt that achieves 94% mean verification across eight transmission channels, with zero forgeries accepted in 25 wrong-key trials. With the gateway in place, residual attack success falls to 0% for all 15 models at no more than 0.03 ms of added decision latency. On the AgentDojo banking suite, aiAuthZ blocks all seven attacker-directed tool calls the evaluated agents emit, at the cost of one legitimate first-time payment, while a spotlighting baseline allows two injections to succeed. Across nine in-scope case studies from the same incident corpus, aiAuthZ blocks nine of nine, against four of nine for a policy baseline without identity binding. The gateway does not prevent a model from being deceived; it prevents a deceived model from acting beyond the verified user's authority on every call routed through it. The implementation and all experiments are released at this https URL.

---


### 26. [Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522)

**<font color=#1a73e8>作者：</font>** Gaoxiang Jia, Vikram Appia, Junzhou Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian splatting (3DGS) is a strong representation for real-time novel-view synthesis, but its standard training pipeline relies on point estimates and hand-tuned heuristics, providing no native uncertainty or principled complexity control. This is most limiting under sparse views or fixed acquisition budgets, where a model must identify weakly supported geometry and select informative views. We introduce a rendering-aware Bayesian 3DGS framework that tracks Gaussian geometry with a Normal-Inverse-Wishart posterior over means and covariances using renderer-derived surrogate summaries. An optional Dirichlet-process extension adds a probabilistic component-usage signal, and the training schedule makes the closed-form versus approximate inference boundary explicit. Re-rendering posterior geometry samples yields native predictive uncertainty for interval calibration and active view selection. In a fixed-budget 16-to-32 active-view task, native NIW acquisition improves PSNR by +0.453 dB and LPIPS by -0.0146 over a scoring-only 3-member standard-ensemble baseline, winning 29/39 scene-seed pairs and 10/13 scene means; it also improves over PPU-style (+0.355 dB) and NIW-proxy (+0.401 dB) acquisition. NIW native intervals reduce 95% coverage error by about 17x relative to a shared proxy (0.046 vs. 0.796) and are about 10x closer to nominal coverage than a 3-member deep ensemble (0.047 vs. 0.454) at roughly one-third the training cost. As a reconstruction compatibility check, paired NIW-vs-standard analysis over 39 scene-seed runs yields +0.030 dB PSNR with 1.6% additional training time. These results position Bayesian 3DGS as a practical probabilistic scene representation for decision-facing tasks such as active view selection.

---


### 27. [$\mathbfλ$-VAE: Variance Equalization for Posterior Collapse](https://arxiv.org/abs/2607.05531)

**<font color=#1a73e8>作者：</font>** Girum Demisse  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Autoencoders (VAEs) frequently suffer from posterior collapse, a failure mode in which the approximate posterior converges to the prior, rendering the latent code uninformative. Despite extensive research, a unified account of why collapse occurs has remained an open question. We identify and formalize two logically independent but coupled causes. \emph{Gradient imbalance} occurs when the decoder's reconstruction signal vanishes faster than the $\mathbb{KL}$ regularization pressure as the posterior widens. \emph{Information gap} occurs when the stochastic sampling step discards a substantial fraction of the encoder's computed representation, attenuating decoder sensitivity and making collapse inexpensive. Both causes share the same collapse trajectory, and we show that the information gap is algebraically equivalent to mismatch between the aggregate posterior and the prior, unifying two pathologies. Subsequently, we introduce $\lambda$-VAE, which resolves both causes through a single modification to the reparameterization step: the sampling noise is scaled by per-dimension exponent, while the $\mathbb{KL}$ penalty retains the original posterior variance. This asymmetry shifts the stable training attractor away from the degenerate collapsed state, driving all latent dimensions toward the same equilibrium -- a mechanism we term \emph{variance equalization}. A closed-form optimal exponent per dimension follows from a net information gain objective, with a single hyperparameter controlling the reconstruction-generation tradeoff. We validate on standard benchmarks (Binary MNIST, Binary Omniglot, CIFAR-10, CelebA-64), showing consistent reductions in collapsed dimensions, information capacity gains of up to $2.8\times$ nats, and reconstruction quality improvements of up to $+0.33$ BPD.

---


### 28. [Self-Review Reinforcement Learning (SRRL) with Cross-Episode Memory and Policy Distillation](https://arxiv.org/abs/2607.05541)

**<font color=#1a73e8>作者：</font>** Muhammad Zain Amin, Kibele Sebnem Yildirim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning is commonly used to train large language models using environmental feedback. In applied settings, the environment usually provides sparse or delayed feedback. This makes it difficult for the model to pinpoint which actions in its reasoning led to success or failure. So, learning effectively from these signals is hard because the model must determine how each failure should inform meaningful behavioral corrections in subsequent iterations. We introduce a training framework, Self-Review Reinforcement Learning, that embeds an explicit self-review step into each RL episode. When a first-pass response fails, the model generates a self-review to identify what went wrong, which conditions an improved second attempt. Unlike inference-time reflection approaches, such as Reflexion, the framework optimizes self-review with policy gradients and internalizes improvements into the base policy via selective distillation, ensuring they persist across future episodes. A cross-episode memory keeps successful self-reviews for reuse when encountering similar tasks in future episodes during training. We evaluate SRRL against a standard RLVR baseline using the GRPO optimizer across two language models, Qwen 3-4B and OLMo-3- 7B, on GSM8K benchmark. SRRL consistently outperforms the RLVR in final reward performance and achieves greater learning efficiency by successfully transforming feedback into behavioral improvement.

---


### 29. [Federated Physics-Grounded Reinforcement Learning for Distributed Stability Control in Smart Grids](https://arxiv.org/abs/2607.05553)

**<font color=#1a73e8>作者：</font>** Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transient stability control in smart grids requires rapid post-fault damping of generator frequency and rotor angle deviations to prevent cascading failures. This paper proposes FedPPO-PG, a Federated Multi-Agent Proximal Policy Optimization framework with Physics-Grounded neighborhoods, which reformulates transient stability control as a cooperative multi-agent reinforcement learning problem optimized directly against closed-loop stability objectives. Each generator hosts an independent local actor augmented with the frequency deviations of its two most strongly coupled electrical neighbors, identified from the post-fault Kron-reduced susceptance matrix. A guided policy initialization phase warm-starts all actors from the classical decentralized controller, while a centralized critic guides advantage estimation under the centralized training--decentralized execution (CTDE) paradigm. Evaluated on a simulation of the IEEE 39-bus benchmark system across five training and three unseen fault contingencies, FedPPO-PG achieves 100% stabilization in all 24 trials, reduces mean stability time by 72.4%, and cuts the control power by 7-14 times compared to the centralized baseline. Each actor executes independently with no central coordinator at deployment, and the per-actor inference latency satisfies the IEEE/IEC 60255-118-1-2018 real-time reporting requirements.

---


### 30. [AIED's Unfinished Mission: Centering Agency and Motivation in the Age of Effortless Bypass](https://arxiv.org/abs/2607.05557)

**<font color=#1a73e8>作者：</font>** H. Chad Lane  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The widespread availability of general-purpose AI that can perform complex cognitive tasks threatens to undermine education at scale. This effortless bypass dilemma sharpens a challenge AIED has long engaged with but must now confront directly: ensuring learners choose effortful engagement when easier alternatives are available to complete learning tasks. In this paper, I argue that AIED's longstanding agenda of building more effective intelligent educational tools should continue, but with a renewed emphasis on the urgency of ensuring learners choose to engage authentically. Drawing on established motivational and learning theories, I outline five directions in which AIED can build on its existing strengths: supporting autonomy and agency, building learner resilience to metacognitive threats, designing for interest and relevance, amplifying process-based assessment, and empowering teachers. I then share four envisioned technologies that embody key features of this future and conclude by outlining how AIED must now evolve.

---


### 31. [EquiFiLM: Charge-Conditioned Equivariant Force Fields via Feature-wise Linear Modulation](https://arxiv.org/abs/2607.05559)

**<font color=#1a73e8>作者：</font>** Samuel Sahel-Schackis, Ken-ichi Nomura, Aiichiro Nakano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation machine learning force fields (MLFFs) such as MACE-MP-0 and UMA cover broad chemical space at near density functional theory (DFT) accuracy. However, they assume equilibrium ground-state physics and do not natively handle externally induced changes to the electronic state, such as charging, applied fields, or electronic excitation, which limits their use for driven processes such as photoexcitation and charge injection. We propose EquiFiLM, a lightweight extension that adds continuous external conditioning to any equivariant foundation MLFF via a per-layer Feature-wise Linear Modulation (FiLM) block, learning externally driven changes to the potential energy surface from minimal training data. The block modulates only scalar channels and preserves E(3)-equivariance exactly. We demonstrate the recipe on charged liquid water with the foundation model MACE-MatPES as the backbone, yielding E-MACE. On the four training charges, E-MACE delivers a $3.1\times$ reduction in force RMSE ($21.3$ to $6.96$ meV/$\mathring{A}$) and a $61\times$ reduction in per-atom energy RMSE ($6.1$ to $0.1$ meV/atom) over a baseline without EquiFiLM trained on the same data, at indistinguishable inference cost. Across seven held-out interpolation and extrapolation charges, force RMSE stays within $18-61$ meV/$\mathring{A}$ and energy RMSE within $0.7-5.4$ meV/atom. The model runs stable molecular dynamics across the full range tested and predicts the charge-dependent first-shell response of the reduced pair distribution function probed by ultrafast electron diffraction. Adding this conditioning axis to the foundation requires only a few thousand DFT-labeled frames, against the $\approx 10^8$ structures of a charge-aware foundation trained from scratch. The recipe is backbone- and conditioning-agnostic: it applies without architectural change to any equivariant MLFF with scalar interaction-layer channels.

---


### 32. [From Graphs to Gradients: Physics-Inspired Structural Attribution for Cyber-Physical IoT Systems and Beyond](https://arxiv.org/abs/2607.05563)

**<font color=#1a73e8>作者：</font>** Spyridon Evangelatos, Christos Diou, Georgios Th. Papadopoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretable explanation methods in Artificial Intelligence aim to uncover the underlying causes and their effects, enabling a deeper understanding of why a system behaves in a certain way under different inputs. Unlike traditional explainability methods, which mainly highlight correlations between input and output variables, causal explanation focuses on interventional questions. By doing so, it provides more robust insights, helping users understand automated decisions, especially in high-risk domains. Recovering an explicit directed causal structure, however, is often impractical in large-scale, hybrid cyber-physical systems with feedback loops and partial observability. This paper introduces a novel framework inspired by statistical mechanics that instead models variable dependencies through an undirected, energy-based representation of cyber-physical IoT systems. Our approach enables rigorous dependency-aware attribution by analysing how variations in the energy landscape reflect the influence of individual components, without recovering a directed causal graph. It also supports reasoning about perturbation effects across hybrid interactions, providing reliable explanations of abnormal behaviours. We empirically examined our framework through simulations on an industrial IoT testbed with hybrid continuous and discrete variables, demonstrating higher attribution accuracy, improved robustness and better scalability than state-of-the-art graph-based approaches. While the attributions are not intended to fully recover the system's generative dynamics, they provide valuable, dependency-aware explanations supporting both human interpretation and downstream predictive and diagnostic tasks. Although demonstrated in industrial IoT security, our framework also applies to other high-dimensional cyber-physical and socio-technical systems requiring principled, structural explanations.

---


### 33. [Hierarchical Classification via Cascading Feature Elimination: Application to Human Phenotype Ontology-Aligned Facial Phenotyping (FaceMesh2HPO)](https://arxiv.org/abs/2607.05585)

**<font color=#1a73e8>作者：</font>** Fabio Hellmann, Alexander Hustinx, Benjamin D. Solomon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FaceMesh2HPO is a framework for classifying facial phenotypic descriptors aligned with the Human Phenotype Ontology (HPO) to support clinical diagnosis. Using annotations from 124 clinicians across 10 disorders (107 HPO terms) combined with non-syndromic controls, we generated 3D facial meshes (478 landmarks) from 2D images and trained a hierarchical PointNet-based pipeline with cascading classification and feature elimination. The best models, incorporating 3D meshes, facial outline, and demographic metadata, achieved AUROCs between ~0.55 and ~0.89, with higher performance at parent nodes than leaf terms. External validation showed variable generalizability across disorders. Results demonstrate that hierarchical modeling of 3D facial geometry enables interpretable, ontology-linked phenotype classification, though performance on rare leaf terms remains limited. Improved data diversity and feature selection strategies are needed to enhance robustness and clinical utility.

---


### 34. [Collective Cognition in Hybrid Groups: A Network Science Synthesis](https://arxiv.org/abs/2607.05593)

**<font color=#1a73e8>作者：</font>** Babak Hemmatian, Razan Baltaji, Lav R. Varshney  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing integration of AI agents into human teams calls for a principled understanding of how collective intelligence emerges in hybrid systems. Recent frameworks clarify how attention, memory, and reasoning differences shape human-AI interaction at the individual and dyadic levels, but a formal account of how these differences scale to group-level dynamics is lacking. Most network science has examined either human-only or multi-agent AI-only systems, leaving open how its findings and parametrizations translate to hybrid groups. This chapter synthesizes network science, collective cognition, and multi-agent systems through the lens of attention, memory, and reasoning. We review how task environments, group topologies, agent-level processes, and incentive structures shape collective outcomes in human-only and AI-only networks, then examine how these results extend to hybrid settings, conceptualizing hybrid networks as heterogeneous human-AI nodes and links with distinct individual and transactive constraints. Our comparative analysis identifies which network effects are robust across agent types and which require revision, and highlights configurations that were peripheral in single-type traditions, such as human gatekeepers of AI sub-networks, but become structurally central in hybrid teams. Integrating a cognitive systems perspective with network science, we clarify how established exploration-exploitation and efficiency-redundancy trade-offs may operate differently in hybrid teams, and conclude with implications for organizational design, governance, and the responsible development of hybrid intelligence systems.

---


### 35. [Patch Knowledge Transfer for Efficient AI-Generated Image Quality Assessment](https://arxiv.org/abs/2607.05605)

**<font color=#1a73e8>作者：</font>** Jiquan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of image generation technologies, perceptual quality assessment of AI-generated images has emerged as a crucial research direction in computer vision. The core challenge of this task lies in achieving efficient quality assessment for massive generated images. Current mainstream approaches exhibit two key limitations: 1) Methods employing complex feature extraction strategies, while improving performance, incur prohibitive computational costs that hinder real-time inference; 2) Simple image scaling-based solutions, despite their computational efficiency, demonstrate significantly inferior assessment accuracy. To address this critical issue, we propose Patch Knowledge Transfer (PKT), a knowledge distillation-based optimization framework that achieves synergistic optimization of visual representation capability and inference efficiency through an innovative multi-level knowledge transfer mechanism. Specifically, we design a dual-model architecture: a teacher model with local-global hybrid processing provides high-quality supervision signals, while a student model relying solely on global processing efficiently inherits the teacher's representation capacity through multi-level supervision. Extensive experiments conducted on 4 AIGIQA databases demonstrate that the PKT framework enables the student model to maintain performance comparable to the teacher while reducing computational costs by 67.7\%. Furthermore, compared to existing methods, our approach achieves a superior balance between model efficiency and assessment accuracy.

---


### 36. [SafeImpute: Reliable Clinical Data Imputation via Conformal Selection](https://arxiv.org/abs/2607.05613)

**<font color=#1a73e8>作者：</font>** Xinrui He, Mengting Ai, Junting Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical care often relies on key laboratory indicators, yet real-world patient visits are sparse and tests are ordered irregularly, leading to pervasive missingness. While many imputation methods improve average accuracy, they provide limited guidance on which imputed values are reliable enough for high-stakes downstream use. In this work, we study reliable clinical imputation, aiming to produce accurate imputations while selectively releasing the reliable results, with statistical control over clinically unacceptable errors. To achieve this goal, we propose SafeImpute, a reliable imputation framework for irregular and sparse clinical longitudinal records. SafeImpute constructs an event graph that captures both intra-patient temporal trajectories and inter-patient clinical similarity, and learns imputations with a two-relation GNN and adaptive fusion, regularized by an auxiliary masked reconstruction objective. For reliability guarantees, SafeImpute converts a proxy risk score into conformal p-values and applies the Benjamini--Hochberg procedure to control the false discovery rate (FDR) of unacceptable errors among released imputations at a user-specified tolerance. Experiments on our Mayo Clinic data, the public MIMIC-III and MIMIC-IV datasets show that SafeImpute achieves strong imputation accuracy while providing reliable error control, outperforming diverse baselines in both standard imputation evaluation and FDR-controlled selective-release evaluation.

---


### 37. [Safe Bayesian Optimization with Counterfactual Policies](https://arxiv.org/abs/2607.05620)

**<font color=#1a73e8>作者：</font>** Katherine Avery, Bruno Castro da Silva, David Jensen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many decision-making settings, new interventions are acceptable only if they do not reduce outcomes below some established threshold. For example, in clinical medicine, new treatments are often acceptable only if they do not worsen outcomes relative to an established standard of care. Safe Bayesian optimization maximizes an objective subject to safety constraints. In the setting that we consider here, safety is defined relative to a known baseline policy whose outcomes are counterfactual and therefore unobserved. Thus, the counterfactual outcomes of the baseline policy must be estimated and those (uncertain) estimates must be used to safely optimize the objective. We address this estimation problem by using conformal prediction to construct valid uncertainty intervals for counterfactual baseline outcomes, and we show how these intervals can be integrated into safe Bayesian optimization to ensure that constraint violations occur at or below a user-specified rate. We also show how to adapt these conformal estimates to different kinds of covariate shift. We provide a safety proof, experimental evidence, and a sensitivity analysis.

---


### 38. [Population-Level Profiling of DSM-5 Depressive Symptoms Among Self-Reported ADHD and ASD Users on Twitter: An Exploratory Study Using Advanced NLP and Statistical Analysis](https://arxiv.org/abs/2607.05626)

**<font color=#1a73e8>作者：</font>** Muhammad Rizwan, David Nabergoj, Jure Demšar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Depression frequently co-occurs with ADHD and autism spectrum disorder (ASD), but population-level differences in symptom expression between these groups remain underexplored. Objective: We examined whether social media users with ADHD and ASD differ in how they express DSM-5 depressive symptoms in their tweets, and whether differences persist across varying levels of depressive-content filtering. Methods: We analysed 1,282,437 tweets from 792 users (622 ADHD; 170 ASD) with self-reported diagnoses on Twitter. Tweets were pre-filtered for depressive relevance using zero-shot NLI, then classified into nine DSM-5 symptoms using MentalRoBERTa fine-tuned on ReDSM5. Profiles were mean-centered per user. We applied L1-penalised logistic regression with cross-validation to distinguish ADHD from ASD users, complemented by Pearson correlations for symptom co-occurrence, and tested robustness across five filtering thresholds using bootstrapping. Results: MentalRoBERTa achieved macro-F1 of 0.901 on a held-out set, outperforming the original ReDSM5 benchmark. ADHD vs ASD classification yielded stable but modest performance (cross-validated ROC-AUC 0.645-0.653). Cognitive issues, sleep issues, appetite change, and fatigue leaned toward ADHD, while suicidal ideation and anhedonia leaned toward ASD. A largely shared symptom co-occurrence structure emerged between groups; no pair met our criterion for a robust disorder-specific difference. Conclusions: Population-level differences in depression-related language between ADHD and ASD social media users were consistently observed across thresholds, reflecting reproducibility rather than clinical validity. Findings are exploratory and do not establish differing phenomenology at the individual level.

---


### 39. [Intuitionistic Fuzzy Graph Embedded Random Vector Functional Link with Multiview Learning](https://arxiv.org/abs/2607.05635)

**<font color=#1a73e8>作者：</font>** Vrushank Ahire, Yogesh Kumar, M.A. Ganaie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random Vector Functional Link (RVFL) networks are popular due to their fast training and universal approximation capabilities. However, RVFL models face challenges in preserving geometric relationships and utilizing multiple feature views effectively. To address these limitations we propose the Intuitionistic Fuzzy Graph Embedded Random Vector Functional Link with Multiview Learning (IFGRVFL-MV) model. The proposed approach comprises three key components: intuitionistic fuzzy sets for uncertainty handling, graph embedding to capture intrinsic geometric structures, and multiview learning to use complementary information from multiple feature spaces. The model assigns intuitionistic fuzzy membership and non-membership values to data points making it robust to outliers. Also, the graph embedding framework preserves topological structures, increasing the generalization performance. We performed experiments on benchmark datasets from UCI and KEEL repositories which concludes that IFGRVFL-MV outperforms existing models in classification accuracy. Our results establish that IFGRVFL-MV is a promising advancement in the domain of uncertainty and multiview environments.

---


### 40. [Recovering Cloud Microstructures with Cascaded Diffusion Inversion](https://arxiv.org/abs/2607.05637)

**<font color=#1a73e8>作者：</font>** Hanan Gani, Guy Pulik, Daniel Rosenfeld 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution satellite imagery is critical for observing fine-scale cloud structures that inform weather modification strategies like cloud seeding for rain-enhancement. However, the spatial resolution of current geostationary and polar-orbiting satellites is often insufficient for capturing small cloud features. Current super-resolution methodologies are suited for natural images and, therefore, struggle to generalize to satellite-captured spectral images of cloud cover. To address this, we propose a two-stage diffusion-based super-resolution framework to enhance the resolution of multi-spectral cloud microstructures by a factor of $4\times$. Specifically, we use inverse diffusion to recover the high resolution properties from low resolution. Stage 1 utilizes real-world paired data to learn robust degradation handling and inter-sensor alignment, while Stage 2 employs a self-supervised internal downgrading of high resolution data to refine structural learning and texture synthesis. Our approach outperforms the state-of-the-art transformer and diffusion-based baselines in both reconstruction accuracy and visual quality. We demonstrate that the two-stage method better captures fine cloud microstructures (e.g. convective turrets and cloud gaps) that are crucial for effective cloud seeding decisions. Ablation studies confirm the complementary benefits of the two stages: Stage 1 excels in coarse structural fidelity, while Stage 2 contributes enhanced detail and realism. These results highlight a practical path toward improving cloud microphysics analysis and as a step towards utilizing AI for climate and sustainability. Our code and models are publicly available at: this https URL.

---


### 41. [VEIL: How Visual Encoding Hijacking Induces Bias In Vision Models](https://arxiv.org/abs/2607.05641)

**<font color=#1a73e8>作者：</font>** Suranjana Sooraj, Xuyang Chen, Madhumitha Venkatesan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rendering time series as chart images for CNN-based classification has become increasingly common in time-series classification (TSC). However, it remains unclear whether models learn underlying temporal patterns or rely on encoding-specific visual cues introduced by chart design. We present VEIL: a systematic study examining how chart encodings influence learned representations through complementary analyses of similarity, transferability, and attribution. Attention-guided training appears to mitigate this effect when encoding sensitivity is consistently identified across diagnostics, but provides limited or negative benefit when such signals are absent. These findings position VEIL within the broader question of how machines perceive visualizations -- extending graphical perception from human readers to vision models -- and show that visualization design choices shape learned representations in ways that warrant treating chart-based TSC as a representation and measurement problem rather than a simple modeling decision.

---


### 42. [Do It Right! A Methodology for Successful NLP System Development](https://arxiv.org/abs/2607.05644)

**<font color=#1a73e8>作者：</font>** Olga V. Patterson, Brett South, T. Elizabeth Workman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language processing (NLP) is a common method for supplying data to clinical research and decision making by extracting information from electronic medical records. Numerous textbooks and tutorials describe specific algorithms and applications for text processing, yet algorithmic knowledge is only one ingredient of a successful NLP project. Drawing on the available literature, this paper presents a stepwise approach that applies the Systems Development Life Cycle (SDLC) to projects that rely on data extraction through language processing.

---


### 43. [Domain-Adaptive Climate Downscaling Under Temporal Distribution Shift](https://arxiv.org/abs/2607.05645)

**<font color=#1a73e8>作者：</font>** Shuochen Wang, Nishant Yadav, Auroop R. Ganguly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep-learning-based climate downscaling aims to learn relationships from historical low-resolution (LR) and high-resolution (HR) climate data to generate HR climate projections. However, this setting faces a temporal out-of-distribution (OOD) challenge: models trained on historical data are commonly applied to future projections whose distributions may differ substantially from the training period. This study investigates temporal OOD shift for daily temperature downscaling over the Continental United States using paired LR-HR model simulations. We propose a temporal domain-adaptive downscaling framework that combines supervised HR reconstruction on historical data with domain alignment between historical and future climate distributions. Experiments across future validation periods show that the proposed domain-adaptive model consistently outperforms statistical and deep-learning-based bias-correction methods, with the largest gains occurring when the temporal distribution shift is strongest. Spatial analyses indicate stronger improvements over high-elevation and topographically complex regions, along with higher spatiotemporal correlation with the HR target. The extreme analysis shows that domain adaptation also reduces upper-tail temperature bias relative to the non-adaptive model. These results demonstrate that temporal domain adaptation can improve the robustness of HR climate projections under non-stationary climate conditions.

---


### 44. [REVIVE: A Multi-Modal Framework for Vandalism Detection and Recovery in Autonomous Vehicles](https://arxiv.org/abs/2607.05649)

**<font color=#1a73e8>作者：</font>** Abdullah Tariq Choudhry, Tapadhir Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) face increasing threats from vandalism-induced occlusion attacks (VOAs) that compromise camera-based perception. While detection frameworks can identify vandalized images, restoring camera-stream utility after physical occlusion remains underexplored. This paper presents present the Recovery and Enhancement of Vandalized Images for Vision Excellence (REVIVE) framework, a vandalism recovery pipeline integrating: (1) binary VOA detection, (2) multi-class VOA pattern identification, (3) EfficientNet-based U-Net segmentation, and (4) type-aware recovery using Bootstrapping Language-Image Pre-training (BLIP)-guided Stable Diffusion inpainting, direct pixel replacement, or adaptive median filtering. Stable Diffusion shows variable reconstruction performance (per-pattern SSIM 0.667-0.867, PSNR 15.4-26.7dB) across VOA patterns, while aligned direct pixel replacement achieves near-identical reconstruction under the aligned-reference condition. On 500 tracked clean/vandalized image pairs, unrecovered VOAs reduce YOLOv8l object-detection recall to 0.588, while direct pixel replacement restores recall to 0.967 and F1-score to 0.970 under that aligned-reference condition. LaMa, Telea, and Navier-Stokes baselines improve image similarity but provide more limited downstream detection recovery, and Stable Diffusion is treated as an asynchronous recovery branch subject to a quality gate rather than a blocking real-time perception step. We evaluate a reference-available quality gate that filters recovered candidates before downstream use: without it, type-aware routing degrades per-image recall to 0.304, whereas with it, recall returns to 0.608, at or above the unrecovered baseline, ensuring the forwarded stream is never worse than the unrecovered frame. REVIVE therefore, provides a structured recovery framework from VOAs in AVs.

---


### 45. [Orthogonal Dendritic Intrinsic Networks: An Architecture for Significance-Ordered, Orthogonal Latent Spaces](https://arxiv.org/abs/2607.05653)

**<font color=#1a73e8>作者：</font>** Jeanie Schreiber, Tyrus Berry, Zeeshan Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Principal Component Analysis or PCA-like properties (orthogonality, variance ranking) are seldom realized in deep autoencoder architectures. In this work, we present ODIN (Orthogonal Dendritic Intrinsic Network), a novel autoencoder architecture that recovers PCA-like latent structure in a fully non-linear regime. By incorporating a set of geometric constraints directly into the training objective, ODIN encourages latent dimensions to be mutually orthogonal and ordered by explained variance, mirroring the interpretable decomposition of PCA while retaining the expressive power of deep networks. We provide theoretical grounding for these constraints and demonstrate their compatibility with standard encoder-decoder frameworks. We also establish empirical results for both synthetic and real world datasets, establishing a principled path toward interpretable, structured feature learning and dimensionality reduction.

---


### 46. [Clustered Codebook Quantization for 2D Gaussian-based Image Compression](https://arxiv.org/abs/2607.05667)

**<font color=#1a73e8>作者：</font>** Runze Cheng, Yicheng Zhan, Josef Spjut 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian-based image representations effectively model image content using compact parametric primitives while preserving high visual fidelity, yet storing a large number of floating-point parameters per primitive degrades rate-distortion efficiency at higher fidelity targets. To improve the rate-distortion performance in Gaussian representation, we present our Cluster-Guided Vector Quantization (CGVQ), a Gaussian primitive based image compression method. Our key idea is to partition Gaussian parameters further into homogeneous groups prior to quantization, enabling higher compression efficiency and accurate parameter reconstruction. In practice, our extensive experiments show that CGVQ decreases the bpp by 20% with respect to our baseline, while maintaining on-par visual quality

---


### 47. [Perceived System Predictability: Scale Development and Application](https://arxiv.org/abs/2607.05674)

**<font color=#1a73e8>作者：</font>** Hendrik Schuff, Heike Adel, Ngoc Thang Vu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How predictable users perceive an interactive system to be shapes how they interpret, trust, and rely on it, yet HCI lacks both a precise conceptualization and a validated instrument for this perception. We address this gap by introducing perceived system predictability (PSP) as a user-centered construct grounded in uncertainty theory, distinguishing epistemic, aleatory, and effective predictability. We contribute (i) a theoretical framework that situates PSP relative to adjacent constructs such as trust and understanding, (ii) a 6-item PSP scale, derived from a 60-item pool through expert review and cognitive interviews, and validated in a shape-classifier study ($N=200$) that supports both a unidimensional and a three-factor hierarchical structure, and (iii) a sentiment-classifier study ($N=200$) that varies explanations and stochasticity, and relates PSP to the correctness of users' predictions of system behavior, trust, subjective information processing awareness, and need for cognition. We find that PSP and prediction correctness capture distinct aspects of users' mental models and that both can diverge: PSP itself predicts correctness, explanations shift PSP but not correctness, and increased stochasticity degrades correctness without lowering PSP. PSP thus goes beyond existing objective and subjective measures and offers a principled foundation for designing transparent and trustworthy interactive systems.

---


### 48. [Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers](https://arxiv.org/abs/2607.05683)

**<font color=#1a73e8>作者：</font>** Taniya Shaji, Abhay Sobhanan, Christof Defryn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery charging of Autonomous Mobile Robots (AMRs) in warehouses is a critical operational challenge that heavily impacts both order processing times and throughput. In this study, we address the dynamic AMR charging problem under stochastic order arrivals, where robots must learn optimal charging decisions. Traditional fixed-rule heuristics often prove suboptimal in dynamic environments and fail to account for multi-AMR coordination, leading to severe resource inefficiencies. To overcome these limitations, we propose a Proximal Policy Optimization (PPO)-based Deep Reinforcement Learning (DRL) framework designed for multi-block warehouses with fixed charging stations. Our model dynamically learns two key decisions: charging station selection and optimal charging duration, explicitly accounting for anticipated queuing times at the stations. Extensive numerical experiments benchmark the proposed model against state-of-the-art DRL and traditional heuristic approaches. Results demonstrate that our PPO framework increases order-completion rates by up to 6\% compared to the strongest baseline, while significantly reducing the total time dedicated to recharging operations. Furthermore, we validate the model's robustness across diverse warehouse configurations and stochastic arrival rates. Finally, we interpret the learned DRL policy, offering valuable operational insights into its superiority over standard benchmarks.

---


### 49. [UCSC NLP at SemEval-2026 Task 10: Boundary-Aware Span Extraction and RoBERTa Classification for Conspiracy Detection](https://arxiv.org/abs/2607.05689)

**<font color=#1a73e8>作者：</font>** Dom Marhoefer, Milos Suvakovic, Glenn Grant-Richards 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our systems for SemEval-2026 Task 10 (PsyCoMark), addressing conspiracy marker extraction (Subtask 1) and document-level conspiracy detection (Subtask 2). For marker extraction, we formulate the task as multi-label span classification over enumerated candidate spans, using IoU >= 0.95 positive labeling, hard-negative sampling, and containment-based non-maximum suppression (NMS) with boundary-aware span representations. Document classification is modeled independently using a sequence classifier with label smoothing and a stratified train-validation split. Analysis shows that entity-like roles (Actor, Victim) are detected robustly, while abstract roles (Action, Effect, Evidence) remain sensitive to boundary criteria. On the official test set, our systems rank 7th in Subtask 1 (0.2251 macro F1) and 11th in Subtask 2 (0.7694 weighted F1).

---


### 50. [Memory in the Loop: In-Process Retrieval as ExtendedWorking Memory for Language Agents](https://arxiv.org/abs/2607.05690)

**<font color=#1a73e8>作者：</font>** Yusuf Khan, Carlo Lipizzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents run a loop - observe, reason, act - but the memory they reason over sits outside it: a store queried at most once per turn. We study the regime where memory moves inside the loop, read and written on every step. The obstacle has always been latency: networked stores answer in tens to hundreds of milliseconds, and in-loop retrieval can inflate end-to-end latency by up to 83x when retrieval is expensive. Prior work manages that cost rather than questioning it: serving-layer scheduling hides it, "memory-first" designs ration retrieval to once per turn. We argue latency is a property of where the store lives, not the in-loop pattern: an in-process store answers in ~100us, three orders of magnitude below the network regime, and at that speed the per-step tax collapses. By the extended-mind thesis's parity principle, a store fast enough to be constantly and directly available becomes extended working memory, not a tool the agent merely consults. The premise is causal: holding a fixed per-turn memory-latency budget and varying only the store's answer speed, redundant actions rise monotonically with latency - 0.0 of 12 at in-process speed, 7.2 of 12 at a 110ms cloud round trip (gpt-5-nano, gpt-5-mini; exact permutation p=0.0079). We demonstrate the regime end-to-end: across four GPT-5-class models under a bounded window, recall improves from 0/5 to 3.6-4.8/5 with in-loop memory, store ops at p50 80-165us - though an instructed restate-every-reply baseline also solves it perfectly, at a token cost that grows with the working set. The store never lost a fact in any run (244 of 244 writes kept); every miss traces to the agent's read policy, not the store. Our measurements also relocate the bottleneck: the dominant per-step cost is embedding (~200-400ms over the network); pairing the in-process store with a small local embedder returns the complete operation to a measured ~40us.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-195](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
