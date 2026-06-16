# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 301. [New Ideas on a New Old Type of Cipher:The Mixed-Radix One-Time Pad](https://arxiv.org/abs/2606.16040)

**<font color=#1a73e8>作者：</font>** Fabio F.G. Buono  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In a short 2012 preprint, an unconventional cipher was introduced, now in this note we take that representational core, formalize it, and use it as the basis for a clean generalization of the one-time pad to non-uniform bases, which we call the Mixed-Radix One-Time Pad (MR-OTP). And we prove that the MR-OTP achieves Shannon perfect secrecy, show that the classical binary OTP is exactly the all-bases-equal-2 special case, and that fixed-base variants recover OTPs over arbitrary alphabets. We then examine whether secret bases can lower the key entropy required for perfect secrecy (they cannot). We close with a usable session protocol based on key rolling that preserves perfect secrecy, and with an honest account of the open problems.

---


### 302. [Active Learning with Low-Rank Structure for Data Selection](https://arxiv.org/abs/2606.16045)

**<font color=#1a73e8>作者：</font>** Vincent Cohen-Addad, Sasidhar Kunapuli, Vahab Mirrokni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the data selection problem, the objective is to choose a small, representative subset of data that can be used to efficiently train a machine learning model. Sener and Savarese [ICLR 2018] showed that, given an embedding representation of the data and suitable geometric assumptions, heuristics based on $k$-center clustering can be used to perform data selection. This perspective was further explored by Axiotis et. al. [ICML 2024], who proposed a data selection approach based on $k$-means clustering and sensitivity sampling. However, these methods rely on the assumption that the dataset exhibits intrinsic geometric structure that can be effectively captured by clustering, whereas many modern datasets instead possess global algebraic structure that is better exploited by low-rank approximation or principal component analysis.
In this paper, we introduce a new data selection framework based on low-rank approximation and residual-based sampling, formulated through the lens of row subset selection and loss-preserving coreset construction. Given an embedding representation of the data satisfying mild regularity conditions, which can be interpreted as algebraic or angular notions of Lipschitz continuity, we show that it is possible to select a weighted subset of $\tilde{O}\left(k + \frac{1}{\varepsilon^2}\right)$ data points whose average loss approximates the average loss over the full dataset within a $(1+\varepsilon)$ relative error, up to an additive $\varepsilon \Phi_k$ term, where $\Phi_k$ denotes the optimal rank-$k$ approximation cost of the embedding matrix. We complement these theoretical guarantees with empirical evaluations, demonstrating that on a range of real-world datasets, our data selection approach achieves improved performance over prior strategies based on uniform sampling or clustering-based sensitivity sampling.

---


### 303. [PointDiffusion: Diffusion-Based Scene Completion in the Point Cloud Domain](https://arxiv.org/abs/2606.16048)

**<font color=#1a73e8>作者：</font>** Chidera Agbasiere, Mikhail Sannikov, Faith Ogunwoye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dense 3D scenes from sparse LiDAR point clouds is a fundamental challenge in autonomous driving, where latent diffusion models offer a promising solution. However, existing approaches rely on object-level autoencoders that collapse into unstable global representations at outdoor scale and suffer from ground truth data corrupted by odometry drift that systematically degrades supervision quality. Furthermore, multi-step diffusion inference incurs prohibitive latency for real-time deployment. We propose a novel multi-token Gaussian VAE with cross-attention pooling for stable scene-scale LiDAR compression, combined with an anchor-based ICP ground truth refinement pipeline that eliminates drift-induced noise from training supervision. Together, these components enable a scaffold-free single-step diffusion completion model that achieves an approximately 16x reduction in squared Chamfer distance on SemanticKITTI seq. 08 (0.396 m^2 to 0.024 m^2), surpasses LiDiff and ScoreLiDAR by 17-19% and 10-11%, respectively, and operates at 25-143x lower inference latency. Our results demonstrate that data quality dominates model design in this regime and that multi-token latent spaces provide a stable first stage for latent diffusion-based scene completion.

---


### 304. [ALCL: An Adaptive Log-Correntropy Loss for Robust Learning under Non-Gaussian Noise](https://arxiv.org/abs/2606.16050)

**<font color=#1a73e8>作者：</font>** Mainak Kundu, Ria Kanjilal, Ismail Uysal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust deep learning under heavy-tailed and impulsive noise remains challenging because conventional losses such as mean squared error (MSE) exhibit unbounded sensitivity to outliers. Although correntropy-based objectives improve robustness, existing formulations rely on fixed kernel parameters that must be empirically tuned and remain static during training. To address these limitations, we propose an Adaptive Log-Correntropy Loss (ALCL), a heavy-tailed loss formulation that adaptively learns its robustness geometry during optimization. ALCL introduces a logarithmic residual model whose shape and scale parameters are learned jointly with network weights through differentiable reparameterization. This yields a principled maximum likelihood formulation whose influence function is formally bounded and redescending, allowing the loss geometry to adapt dynamically to evolving residual statistics while suppressing extreme outliers. Comparative experiments on four widely used benchmark datasets spanning grayscale and red-green-blue (RGB) image data under mixed heavy-tailed and impulsive noise demonstrate that ALCL consistently outperforms MSE and optimally tuned generalized correntropy losses in both reconstruction fidelity and downstream classification accuracy. While performance differences remain small under low-noise conditions, under high-noise regimes ALCL improves median accuracy by up to 4.75% on grayscale benchmarks and 4.51% on RGB datasets, with reduced variance across runs. These results demonstrate that adaptive robustness through joint learning of loss parameters provides a computationally efficient alternative to static correntropy-based losses for deep learning in non-Gaussian environments.

---


### 305. [The Anatomy of Scam Scenarios: Large-Scale Characterization and Conversation-Aware Detection](https://arxiv.org/abs/2606.16052)

**<font color=#1a73e8>作者：</font>** Shang Ma, Chen Yanai, Avichai Ben 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online scams have become a pervasive global threat, causing substantial financial, psychological, and operational harm. Scammers embed psychological techniques (PTs) within reusable operational schemes to scale scam campaigns with minimal adaptation. However, existing studies often analyze PTs as isolated features, overlooking the recurring scam scenarios in which they are systematically deployed. To address this gap, we first conduct a large-scale empirical study to jointly characterize scam scenarios and their associated PTs. Specifically, we develop a data-driven pipeline to derive a hierarchical taxonomy of scam scenarios, consisting of 18 fine-grained scenarios grouped into 6 high-level tactics based on their PT profiles. Furthermore, to transfer this scenario-level knowledge to practical defense, we design a conversation-aware scam scenario detection approach for financial-institution customer interactions, enabling timely warning and intervention. Our study on 102,054 real-world scam incident reports, spanning 2024-02-01 to 2025-10-31, reveals that PT usage is significantly associated with scam scenarios. We further show that scammers organize scenarios around different operational goals, such as broad victim exposure, high victim conversion, and high-value extraction, and reuse infrastructure, including IP addresses, domains, email addresses, and phone numbers, to launch coordinated campaigns at scale. Evaluation on

---


### 306. [Beyond the Blood Draw: Explainable Machine Learning for Non-Invasive Dysglycemia Risk Screening](https://arxiv.org/abs/2606.16056)

**<font color=#1a73e8>作者：</font>** Black Sun, Chenyi Zhang, Kaiyi Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dysglycemia, encompassing both prediabetes and diabetes, affects huge numbers of adults worldwide, yet many of them remain undiagnosed. We developed and validated machine-learning (ML) models for non-invasive screening of dysglycemia risk that require no laboratory tests. Pooling data from the National Health and Nutrition Examination Survey (NHANES) 2017--2023 (n=14,352), we trained six ML models with stratified 5-fold cross-validation and compared them with two established clinical risk scores. LightGBM achieved the highest area under the receiver operating characteristic curve (AUC=0.820, 95% CI: 0.806--0.835), outperforming the Finnish Diabetes Risk Score (0.745) and American Diabetes Association Risk Test (0.783). SHAP analysis identified age, race/ethnicity, and waist-to-height ratio as the most influential predictors. Subgroup analyses confirmed consistent performance across demographic strata (AUC: 0.735--0.832). These results demonstrate the feasibility of explainable, laboratory-free dysglycemia screening for deployment in community settings and self-tracking health applications.

---


### 307. [Mojo: A Promising Tool for Scalable Financial AI Efficiency](https://arxiv.org/abs/2606.16059)

**<font color=#1a73e8>作者：</font>** Henry Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For thirty years, quantitative finance has paid a costly two-language tax: models researched in Python are rewritten in C++ for production, often introducing numerical discrepancies. GPU-accelerated deep learning exacerbates this problem, as nondeterministic floating-point reductions can produce drift in long backtests, challenging regulatory reproducibility and auditability expectations. This article surveys Mojo, Modular's 2026 Python-like systems language, as a structural response for capital markets engineering. While closing the Python-to-C++ performance gap, Mojo uniquely combines native interoperability with the low-level systems control required to construct bit-exact deterministic kernels. Its MLIR compilation infrastructure further allows a single codebase to target scalar, SIMD, multicore, and GPU execution, reducing the translation bottleneck between research and production. We benchmark four core financial AI workloads: Monte Carlo option pricing, LLM sentiment inference, multi-asset backtesting, and portfolio Value at Risk. On Apple Silicon, Mojo demonstrates 20x to 180x speedups over pure Python on directly measured kernels; larger-scale GPU workload results are projections calibrated from published benchmarks. Alongside transparent performance data, we introduce mojo-deterministic, an open-source library of reproducible reduction kernels, and provide a candid assessment of the problems Mojo does and does not yet solve.

---


### 308. [Auditing Reward Hackability in Code RL Training Environments](https://arxiv.org/abs/2606.16062)

**<font color=#1a73e8>作者：</font>** Shreshth Rajan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We measure the rate at which code RL environments accept incorrect solutions as correct. On a 49-task sample of SWE-bench Verified, 28.5% of tasks have test suites weak enough that a Docker-verified incorrect patch passes them. On 20 R2E-Gym tasks across 6 repositories, the same pipeline at single-shot exploit generation yields 25.0%. A random-effects meta-analysis over 134 frontier model submissions to SWE-bench Verified finds, within the same human-rated difficulty stratum, model Pass@1 is +14.14 percentage points higher on flagged-hackable tasks than on robust ones (95% CI [+11.80, +16.48]; one-sided p < 10^-6; I^2 = 0%; 123 of 134 models positive). We then describe a procedure for hardening the broken tasks. An inline LLM judge with a Docker gold-sanity gate runs each generated test against the gold solution before the judge is consulted. On the 11 broken tasks in the audit, the gate flags 65 of 105 decisive LLM-generated tests as failing on the gold patch itself, a 61.9% per-augmentation defect rate the LLM judge alone misses. With diversity-biased retry, the loop converges 9 of 11 tasks to a gated upgrade.

---


### 309. [MASCOT-Android: A Curated Dataset and Automated Collection Pipeline for Android Malware Source Code Specimens](https://arxiv.org/abs/2606.16072)

**<font color=#1a73e8>作者：</font>** Bojing Li, Duo Zhong, Prajna Bhandary 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Compared with binaries and decompiled code, malware source code more directly reflects the attackers' original intent. However, the scarcity of source code and the high cost of manual review make such datasets difficult to build and maintain. We propose MASCOT-Android, a curated dataset of Android malware source code and an automated collection framework for scalable malware source code discovery on GitHub. A key finding of our work is that repository-level documentation alone provides a strong signal for malware source code collection. Our model extracts character-level TF-IDF features from 8,772 malware and 25,747 benign README documents and trains a LinearSVC classifier to distinguish malware repositories. This README-only model achieves an accuracy of 96.28\% and an FPR of 1.06\% in local evaluation. In addition, the model outputs confidence scores, allowing users to adjust the decision threshold to balance FPR and coverage, which is practical in real-world malware source code collection.

---


### 310. [Stop the Sampler! Classifier-Based Adaptive Stopping for Sampling Kernels](https://arxiv.org/abs/2606.16073)

**<font color=#1a73e8>作者：</font>** Kirill Korolev, Nikita Morozov, Stepan Pavlenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from complex, unnormalized probability densities is a fundamental challenge in Bayesian inference and probabilistic modeling. While Markov chain Monte Carlo (MCMC) methods provide asymptotic guarantees, they often suffer from slow mixing and high computational costs due to fixed or manually tuned trajectory lengths. In this work, we propose a novel framework that treats trajectory termination as a learnable component of the sampling dynamics. By framing MCMC within the theory of non-acyclic generative flow networks (GFlowNets), we train state-dependent neural classifiers to decide when a trajectory has reached a high-density region and should terminate. We theoretically establish the connection between optimal classifiers and the target density via detailed balance conditions and introduce a multilevel training scheme to facilitate exploration in complex geometries. Experimental results across various benchmark densities demonstrate that our approach significantly reduces average trajectory lengths while improving mode coverage and mixing compared to standard MCMC baselines.

---


### 311. [AME: A Multi-Type Contributor Attribution Framework in Generative AI Markets](https://arxiv.org/abs/2606.16075)

**<font color=#1a73e8>作者：</font>** Yang Shi, Songwen Pei, Yang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative AI enables value creation through multi-stage collaboration among heterogeneous contributors, including training data, base models, fine-tuning behaviors, and prompts. However, how to fairly allocate the data value remains largely unexplored. This paper formulates multi-stage generative AI value allocation as a new research problem and identifies three core challenges: heterogeneous data contribution valuation, data rights mapping, and trustworthy execution. We propose AME (Attribution-Mapping-Execution) framework, a unified framework that integrates data contribution valuation, data rights mapping, and trustworthy execution into a single workflow. Experimental results demonstrate that AME framework achieves data value allocation outcomes more consistent with human reference judgments while maintaining low-cost trustworthy execution. Our work provides an initial foundation for value assessment and revenue allocation in generative AI data markets.

---


### 312. [Rhythm of the Deep: A Computational-Linguistic Test of Duality of Patterning in Sperm Whale Codas](https://arxiv.org/abs/2606.16084)

**<font color=#1a73e8>作者：</font>** Mudit Sinha, Sanika Chavan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human language has often been described as combining structure at two levels: lower-level units combine into larger units, which then combine into larger sequences. We test for this design feature, duality of patterning, in sperm whale codas using 1,483 codas from the Dominica Sperm Whale Project. Because acoustic similarity can imitate symbolic structure, we treat the problem as computational-linguistic structure discovery from continuous audio rather than as a direct claim about language or meaning. We use a consensus of frozen audio encoders, held-out structural tests, per-statistic nulls, and acoustic-null recoverability gates. The evidence supports a narrow two-tier architecture. At the lower tier, clicks compose into codas not by a stable ordered rule, but by which clicks are present together with their inter-click rhythm. At the upper tier, coda tokens show bout-level sequential dependence, with an NSB second-order transfer-entropy lift of 0.132 bits (p = 0.002). Under tempo scaling, encoder-derived click identity is strongly rate-bound, while coda identity remains substantially more stable, yielding a measurable abstraction gradient across the click-to-coda step. Rhythm-only baselines recover substantial lower-tier structure but fail to reproduce the upper-tier sequential-dependence signal. We do not claim language, semantics, perception, or human-like phonemes. Instead, we report representation-level evidence for a duality-of-patterning-like architecture whose lower tier is rhythmic rather than segmental, and provide a portable null-controlled framework for testing combinatorial structure in induced acoustic token systems.

---


### 313. [Long-Context Modeling via GSS-Transformer Hybrid Architecture with Learnable Mixing](https://arxiv.org/abs/2606.16093)

**<font color=#1a73e8>作者：</font>** Kuzey Torlak, Hüseyin Arda Arslan, Anıl Dervişoğlu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modeling long-range dependencies remains a central challenge in natural language processing. Transformer architectures achieve strong performance via self-attention but scale quadratically ($O(N^2)$) with sequence length, while State Space Models (SSMs) scale linearly ($O(N)$) but suffer from a selective recall bottleneck, struggling to retrieve precise information from compressed states. This creates a fundamental tradeoff between efficiency and perplexity. To tackle these challenges, we propose the \textit{Parallel Hybrid Architecture (PHA)}, which runs Gated State Spaces (GSS), Grouped Query Attention (GQA), and Feed-Forward Networks (FFNs) as independent parallel branches fused by a learnable mixing mechanism. Instead of forcing SSMs to approximate attention or serializing the two paradigms, PHA allows each branch to specialize: GSS captures global context, while attention performs selective retrieval, with FFN providing complementary processing. On WikiText-103, PHA achieves 16.51 PPL at 125M parameters, outperforming Hedgehog (16.70) and H3-125M (23.70). Scaling to 180M parameters yields 16.42 PPL, which gives comparable results with the pure attention baseline while delivering 24\% higher throughput and up to 40\% lower memory usage at long contexts. On OpenWebText, our 125M model achieves 19.72 PPL, outperforming standard Transformers (20.60) and GSS hybrid baselines (19.80). These results demonstrate that separating sequence modeling paradigms into parallel specialists enables Transformer-level perplexity with substantially improved efficiency for long-context language modeling.

---


### 314. [GraphStory: Collaborative Story Writing through Event-Based Narrative Editing](https://arxiv.org/abs/2606.16102)

**<font color=#1a73e8>作者：</font>** Xuan-Vu Le, Minh-Loi Nguyen, Khanh-Duy Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Story writing is a popular yet complex creative activity that requires organization of ideas and iterative exploration, particularly during early-stage ideation. While many AI-based writing assistants have been developed, existing approaches primarily focus on generating long-form coherent text and improving user controllability during text production, providing limited support for brainstorming, connecting ideas, and validating alternative narrative flows. We present GraphStory, an interactive writing support system that leverages a graph-based representation to provide a comprehensive view of narrative structure and facilitate ideation. The system enables users to organize and connect plot points, explore alternative branches, and validate evolving narratives through an integrated story generation workflow. It further provides a structured interface to support efficient iteration over multiple story paths. Results from a user study with professional and semi-professional writers show that GraphStory reduces the effort of organizing narrative structures and better supports creativity and exploration compared to normal AI-based writing workflows.

---


### 315. [SceneCraft: Interactive System for Image Editing via Scene Graph](https://arxiv.org/abs/2606.16103)

**<font color=#1a73e8>作者：</font>** Duc-Manh Phan, Ngoc-Dai Tran, Duy-Khang Do 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative AI have enabled natural language-driven image editing, yet existing systems often fail in complex scenes with multiple interacting objects because they rely heavily on users crafting precise text prompts. To address the absence of structured control, we propose SceneCraft, a novel interactive framework that bridges user intent and model execution by representing images as editable scene graphs. Instead of guessing text prompts through trial and error, users interact directly with a visual graph to perform complex spatial and relational operations. These graph modifications are automatically translated into precise, context-aware editing prompts, effectively eliminating linguistic ambiguity. To ensure robust and diverse results, structured prompts are dispatched to multiple state-of-the-art generative models. Evaluations across diverse editing scenarios show that SceneCraft provides a more intuitive control mechanism, significantly reducing the cognitive burden of manual prompt engineering while generating outputs that users consistently rate as higher in quality and fidelity.

---


### 316. [Auditing Machine Unlearning: A Systematic Research on Whether Models Truly Forget](https://arxiv.org/abs/2606.16110)

**<font color=#1a73e8>作者：</font>** Dayong Ye, Tianqing Zhu, Ruiding Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has been extensively studied in response to growing privacy concerns and regulatory requirements. However, auditing whether unlearning algorithms have truly erased the influence of specific data remains an open challenge. The lack of reliable and practical auditing mechanisms can lead to critical privacy risks, such as residual information leakage. This paper initiates a systematic investigation into whether existing unlearning algorithms can truly forget the designated data. We propose the first practical and general-purpose auditing framework for machine unlearning, inspired by the concept of proof of ignorance. Our framework addresses the key practicality limitations of existing methods by eliminating the need for retraining-from-scratch baselines, avoiding the training of large numbers of shadow models, and requiring no intrusive intervention in the original training process. To evaluate the effectiveness of our framework, we first conduct validation experiments to verify its soundness and completeness. We then perform comprehensive experiments across six datasets and ten representative unlearning methods. The results demonstrate that our framework reliably distinguishes between successful and failed unlearning. In particular, we observe that retraining-based and fine-tuning-based methods can achieve effective unlearning, even when the target data remain in the original dataset. In contrast, de-optimization-based methods fail to achieve true unlearning and instead degrade the model's performance. Fisher/Hessian-based methods also fail to unlearn requested data, even formal certification is provided. Moreover, we show that our framework is robust against fake unlearning attempts and generalizes well to large language models.

---


### 317. [Scaling Adaptive Depth with Norm-Agnostic Residual Networks](https://arxiv.org/abs/2606.16112)

**<font color=#1a73e8>作者：</font>** Tomás Figliolia, Beren Millidge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual architectures are ubiquitous in deep learning, but they suffer from a subtle structural limitation: the norm of the residual stream can grow rapidly with depth. As a result, updates from later layers become small relative to the accumulated residual state. This reduces their impact on the representation and limits the benefits of scaling models in depth. To address this, we introduce NAG, a norm-agnostic residual architecture that separates magnitude from directional information in the residual stream, preserving meaningful layer contributions throughout depth and preventing later updates from being systematically suppressed by residual-norm growth. Importantly, NAG introduces only a negligible number of additional parameters and relies on simple operations that are easily kernel-fusible, preserving training efficiency in practice. We show that this architecture outperforms baseline Transformers, with gains that increase substantially as depth grows, enabling effective training of much deeper models. The norm-agnostic formulation also leads to an interpretable Mixture-of-Depths (MoD) mechanism that adaptively skips both attention and MLP layers. Beyond serving as a post-training accuracy-compute tradeoff, this mechanism can be used as a pretraining-time scaling strategy: under iso-FLOP training, compute saved by reducing per-token forward-pass cost can be reinvested into training on more tokens while keeping the total parameter count and KV-cache budget fixed. In our experiments, moderate Mixture-of-Depths rates of approximately 20%-25% match full-depth baseline performance under equal training compute while substantially reducing the number of executed layer parameters and forward-pass FLOPs. These results identify sparsity in depth as a new scaling axis for fixed-compute training, enabling very deep yet FLOP-efficient models.

---


### 318. [RecourseBench: A Modular Framework for Reproducible Algorithmic Recourse Evaluation](https://arxiv.org/abs/2606.16113)

**<font color=#1a73e8>作者：</font>** Zahra Khotanlou, Hashir Ahmed, Chenghao Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse methods provide counterfactual explanations that inform individuals of the actions required to overturn an unfavorable model decision. Despite rapid methodological progress, principled comparison remains elusive; existing frameworks are often difficult to extend and lack both interoperability and systematic verification that integrated methods faithfully reproduce their originally reported results. We introduce \emph{RecourseBench}, a unified evaluation framework built around three commitments namely, modularity, reproducibility, and interactivity. The framework decomposes the pipeline into five fully decoupled layers -- Data, Preprocessing, Model, Recourse Method, and Evaluation -- governed by abstract interfaces and a dynamic registry. To address the reproducibility gap in prior benchmarks, we introduce a four-tier classification system in which every integrated method is validated by an automated test suite against its originally reported results. We further provide an interactive web interface for flexible, configuration-driven comparison across methods, datasets, and model architectures. Our framework currently integrates 28 state-of-the-art recourse methods and, to our knowledge, constitutes the first recourse benchmark to explicitly enforce method-level reproducibility through automated, quantitative testing.

---


### 319. [EdgeZSAD: Practical Zero-Shot Anomaly Detection on Edge Devices](https://arxiv.org/abs/2606.16119)

**<font color=#1a73e8>作者：</font>** Taewan Cho, Andrew Jaeyong Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial inspection needs zero-shot anomaly detection (ZSAD) that remains useful under edge deployment constraints. Recent methods often rely on ViT-L foundation backbones (~300M parameters), which exceed the memory and operator budget of typical embedded hardware. We study this regime through EdgeZSAD, a compact reference system built around a TinyViT-21M-512 backbone, an asymmetric global-local readout (EdgeGLR), and a reproducible source-side training recipe (Real-IAD-DR). We train a single checkpoint in a source-trained, target-unseen protocol and evaluate it across six industrial benchmarks. Across three independent runs, the resulting model reaches an average image AUROC of 91.6 on MVTec-AD and 88.2 on VisA, while remaining directly deployable on Jetson Orin Nano Super (TensorRT FP16) and RB5 Gen2 (QNN GPU FP16). Across the six device-rescored benchmarks, image-AUROC drift stays below 0.2 points, indicating that the exported graph preserves host-side ranking behavior in the evaluated deployment setting.

---


### 320. [Invisible Manipulation Channels in AI-Assisted Financial Advisory: Implications for Market Integrity and Regulatory Design](https://arxiv.org/abs/2606.16121)

**<font color=#1a73e8>作者：</font>** Liuyang Yao, Zhouyu Li, Junguang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly deployed for credit assessment and investment advisory in global financial markets, yet the integrity of their inference pipelines remains insufficiently addressed by existing regulatory frameworks. This paper identifies and empirically validates an invisible manipulation channel operating at the sampling layer of LLM inference--a vulnerability that allows adversaries to systematically bias AI-generated financial opinions while preserving full compliance with output-based audit mechanisms, including statistical watermarking. We show that this inference-stage manipulation is statistically hard to detect: the Kullback-Leibler divergence between manipulated and normal output distributions can be made arbitrarily small, so that any output-based detection scheme requires impractically large sample sizes to achieve reliable detection power. Empirical experiments across credit rating and investment advisory scenarios show that directional bias keywords can be amplified by 1.8-1.9x under stealth-preserving (aware) manipulation while triggering zero of six black-box detectors and preserving watermark integrity. The vulnerability generalizes across three mainstream watermarking schemes and three heterogeneous model architectures, establishing it as a systemic financial infrastructure risk. Software-based defenses including cryptographically secure pseudorandom number generators are entirely ineffective, while QRNG combined with TEE hardware isolation achieves 100% attack blocking--reducing the target rate to the natural baseline--by replacing the predictable hash key with quantum-derived entropy that renders all pre-computed manipulation targets invalid. We propose four regulatory amendments centered on mandatory QRNG certification for high-risk financial AI systems under NIST SP 800-90B, inference-layer supply chain audits, and output provenance mechanisms.

---


### 321. [Thinking with Visual Grounding](https://arxiv.org/abs/2606.16122)

**<font color=#1a73e8>作者：</font>** Junkai Zhang, Yihe Deng, Kai-Wei Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual thinking should not only sound right; it should show its evidence. While recent vision-language models (VLMs) can produce natural-language reasoning traces, these traces often leave the supporting image regions implicit, making them hard to verify and difficult to supervise. We introduce visually grounded thinking, a reasoning process in which models interleave natural-language thoughts with explicit point or box groundings of the visual evidence used at each step. This lets the model express intermediate reasoning in language while grounding key objects in the image regions they refer to. To train this behavior, we construct a scalable synthesis pipeline that distills correct visual reasoning traces, extracts the visual objects required by the traces, grounds them with a SAM3-based agent, and derives aligned point and box supervision from the resulting masks. We further propose grounding-aware reinforcement learning, which combines answer correctness rewards with dense grounding rewards that score whether generated object references match the correct image evidence. Across two counting benchmarks and four spatial reasoning benchmarks, adding visually grounded thinking to Gemma3-4B-IT consistently improves performance over the original model and the non-grounded thinking baseline. On spatial reasoning, the visually grounded thinking 4B models match, and in some cases surpass, Gemma3-27B-IT from the same model family. Our analysis shows that point grounding is well suited to counting, while box grounding benefits most from explicit grounding rewards on spatial tasks. Overall, our results show that VLMs think better when their intermediate thoughts are tied to the image regions that make them true.

---


### 322. [Shift-and-Sum Quantization for Visual Autoregressive Models](https://arxiv.org/abs/2606.16131)

**<font color=#1a73e8>作者：</font>** Jaehyeon Moon, Bumsub Ham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) enables efficient deployment of deep networks using a small set of data. Its application to visual autoregressive models (VAR), however, remains relatively unexplored. We identify two key challenges for applying PTQ to VAR: (i) large reconstruction errors in attention-value products, especially at coarse scales where high attention scores occur more frequently; and (ii) a discrepancy between the sampling frequencies of codebook entries and their predicted probabilities due to limited calibration data. To address these challenges, we propose a PTQ framework tailored for VAR. First, we introduce a shift-and-sum quantization method that reduces reconstruction errors by aggregating quantized results from symmetrically shifted duplicates of value tokens. Second, we present a resampling strategy for calibration data that aligns sampling frequencies of codebook entries with their predicted probabilities. Experiments on class-conditional image generation, inpainting, outpainting, and class-conditional editing show consistent improvements across VAR architectures, establishing a new state of the art in PTQ for VAR.

---


### 323. [LiteOdyssey: A Lightweight Reasoning AI Agent for Interpretable Rare-Disease Diagnosis](https://arxiv.org/abs/2606.16149)

**<font color=#1a73e8>作者：</font>** Minh-Ha Nguyen, Erica Gray, Chih-Ting Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most medical AI systems improve by scaling additional machinery: more fine-tuning data, more agents, and/or larger retrieval databases. In rare-disease diagnosis, however, such scaling can produce systems that are difficult to deploy, audit, and maintain. We asked whether state-of-the-art diagnostic performance could instead be achieved by extending the reasoning chain of a single AI agent: guiding it with a diagnostic policy, developed through human-AI collaboration and augmenting with freely available biomedical tools. We introduce LiteOdyssey, a lightweight rare-disease diagnostic framework that guides reasoning language model through a clinical genetics workflow. This framework was developed through Policy Iteration with Human Feedback (PIHF) and uses dynamic access to public biomedical tools. On two challenging benchmarks that provide only patient clinical features, LiteOdyssey achieved state-of-the-art performance, with an overall disease Recall@1 of 59.3% over the combined 1,243 cases of LIRICAL (n = 370) and the PhenoPacket Store (n = 873). Both benchmarks have a high proportion of ultra-rare disease (a prevalence below 1 in 1,000,000, with ultra-rare shares of approximately 45% and 52.8%, respectively). On the more difficult PhenoPacket subset, where causal diseases were not mapped to Orphanet in our rarity-mapping pipeline, LiteOdyssey achieved 60.7% Recall@1, compared with 10.7% for the same baseline model (GPT-5.4) without tools. This performance was achieved without fine-tuning, multi-agent ensembles, or a large case-retrieval database. Gains were also observed in the following: on cases never seen during development, on a private cohort of real-world rare disease patients, and on a smaller open-weights model. LiteOdyssey suggests a path toward rare-disease AI systems that are accurate, easier to deploy, and more transparent for physician review.

---


### 324. [GRACE: Step-Level Benchmark for Faithful Reasoning over Context](https://arxiv.org/abs/2606.16151)

**<font color=#1a73e8>作者：</font>** Hoang Pham, Dong Le, Anh Tuan Luu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many reasoning tasks require models to reason over input context, from document-grounded question answering to rule-based deduction. Chain-of-Thought (CoT) prompting produces traces that appear transparent, yet individual steps can silently deviate from the source evidence, even when the final answer is correct. Existing methods detect hallucinations at the response level but fail to identify where in the chain a failure occurs or what type it is. We introduce GRACE, the first human-annotated step-level faithfulness benchmark with a data-driven error taxonomy for context-grounded textual reasoning. GRACE covers CoT traces from 10 models across 4 source datasets, with each step annotated for faithfulness, error category, and natural language explanation. A data-driven taxonomy, discovered bottom-up via unsupervised clustering, organizes failures into two tracks: GRACE-Inference (deductive errors) and GRACE-Grounding (factual grounding errors), with four categories each. The evaluation set is human-annotated and challenging by design. Our experiments reveal substantial headroom for current models. In addition, integrating step-level faithfulness signals into reinforcement learning pipelines improves both downstream accuracy and reasoning reliability.

---


### 325. [A Comprehensive Survey of Medical Image Segmentation: Challenges, Benchmarks, and Beyond](https://arxiv.org/abs/2606.16153)

**<font color=#1a73e8>作者：</font>** Pengyu Zhu, Xiaojing Zhang, Kunbo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation plays a critical role in clinical diagnostics, treatment planning, disease monitoring, and neurological disorder identification. This article presents a comprehensive review of its systematic development, covering widely used public datasets, representative methods built on the U-Net, Transformer, and SAM architectures, and key evaluation metrics with their differences, followed by an analysis of major challenges from multiple perspectives. Unlike surveys that focus on a single model family or a specific clinical application, this review organizes U-Net-, Transformer-, and SAM-based methods within a unified analytical framework, with a particular focus on their effectiveness in improving segmentation accuracy and efficiency. This work aims to guide future research and support clinical translation of medical image segmentation, with all related resources publicly available in our GitHub repository: this https URL.

---


### 326. [A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/abs/2606.16154)

**<font color=#1a73e8>作者：</font>** Prasanth YSS, Zhichen Ren, Rasa Hosseinzadeh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but GRPO-style optimization remains prone to collapse. We analyse this instability through token-level gradient dynamics, deriving a taxonomy that predicts how updates affect next-token probabilities and entropy. The taxonomy shows that stability depends jointly on the advantage sign and token distribution under the current policy. Motivated by this finding, we propose Winner Advantage Policy Optimization (WAPO), a simple online clipped policy-gradient objective that updates only on positive-advantage completions. Across mathematical reasoning and multi-hop QA benchmarks, WAPO improves training stability and matches or outperforms baselines across multiple model families. Full code can be found at this https URL.

---


### 327. [Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Yicui Shi, Guofa Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement aims to recover clear images from low-illumination observations and is crucial for high-level downstream vision tasks. However, existing methods frequently encounter color distortion and structural artifacts when balancing global smooth illumination adjustment and local high-frequency detail recovery. To address these issues, we propose CGS-Retinex as the first low-light image enhancement framework based on explicit-implicit joint modeling. Our framework deeply integrates continuous Gaussian splatting with Retinex theory. Specifically, we represent the image grid as a continuous parameter field and propose a continuous Gaussian renderer to estimate the spatially continuous global illumination distribution. This approach fundamentally eliminates grid artifacts caused by discrete Gaussian sampling. Furthermore, we introduce an implicit neural representation to model reflectance independently. We leverage shallow high-frequency features to guide the network in accurately reconstructing degraded texture details. Within the Retinex framework, we incorporate physics-inspired brightness consistency constraints and illumination smoothness regularization to enable explicit illumination and implicit reflectance to maintain proper exposure and achieve high-fidelity recovery of high-frequency structures and colors. Extensive experiments demonstrate that CGS-Retinex significantly suppresses dark-region noise and overexposure while achieving exceptional high-frequency structural fidelity and color restoration by precisely decoupling illumination and texture. This work establishes a novel continuous physical representation paradigm for low-light image enhancement.

---


### 328. [A comparative and critical study of EEGNet for fNIRS-driven cognitive load classification](https://arxiv.org/abs/2606.16160)

**<font color=#1a73e8>作者：</font>** Mehshan Ahmed Khan, Houshyar Asadi, Li Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately classifying cognitive load from functional near-infrared spectroscopy (fNIRS) signals remains a significant challenge due to temporal variability, inter-subject differences, and sensitivity to preprocessing choices. This study provides a comprehensive evaluation of EEGNet for fNIRS-based cognitive load classification by systematically examining the effects of temporal segmentation strategies (overlapping vs. non-overlapping), window lengths (10s, 20s, 30s), feature extraction methods (Analysis of Variance (ANOVA), Principal Component Analysis (PCA), Fast Independent Component Analysis (FastICA)), learning rate configurations (fixed and adaptive), and evaluation protocols (random split vs. subject-independent (SI)). Results from random-split experiments show that overlapping segmentation, combined with smaller fixed learning rates (0.01-0.001), yields the highest accuracies, due to temporal redundancy and dense sampling of hemodynamic transitions. However, SI evaluation reveals a substantial drop in accuracy, demonstrating limited generalization to unseen participants. Under SI evaluation, non-overlapping segmentation outperformed overlapping windows, with the best accuracy of 56.11% achieved using PCA features with a 20-second window and a 0.1 learning rate. These findings indicate that eliminating temporal redundancy helps the model learn more robust and generalizable representations of cognitive load across individuals. Although adaptive learning rate strategy improved training stability, it did not surpass the performance of optimally selected fixed learning rates. The study highlights the critical role of segmentation strategy and learning rate selection in improving model generalization and identifies methodological considerations essential for developing reliable, real-time, and SI cognitive load classification systems using fNIRS.

---


### 329. [Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Wenxuan Yu, Guofa Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing single image dehazing methods are often constrained by computational redundancy in pixel-level optimization and the lack of physical interpretability in implicit neural networks. These limitations hinder the balance between representation efficiency and reconstruction fidelity. To address these issues, we propose Dehaze-GaussianImage, the first zero-shot framework that introduces 2D Gaussian Splatting (2DGS) into the image dehazing domain to break the traditional pixel-grid processing paradigm. Distinct from static convolutional neural networks (CNNs) or Transformers, our approach models hazy images as continuous and dynamically evolvable anisotropic Gaussian fields. Specifically, we propose a novel reconstruction-decoupling zero-shot learning strategy that embeds the atmospheric scattering model into the Gaussian parameter space. This strategy drives Gaussian primitives to adaptively split, clone, and prune during optimization, achieving geometric-level decoupling of the transmission medium and clear textures. Furthermore, explicit structure-preserving constraints are introduced to suppress artifacts commonly caused by traditional physical priors. Experimental results demonstrate that the proposed method achieves state-of-the-art (SOTA) performance in a fully unsupervised manner with minimal parameters, highlighting the potential of explicit Gaussian representation for low-level vision tasks.

---


### 330. [AI Pluralism and the Worlds It Misses](https://arxiv.org/abs/2606.16167)

**<font color=#1a73e8>作者：</font>** Rashid Mushkani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI pluralism is often framed as a problem of representing diverse values, preferences, users, or outputs. This paper argues that this framing is incomplete because AI systems also impose ontologies: they define what counts as an entity, relation, feature, harm, benefit, and valid form of evidence. We define ontological flattening as the conversion of situated, contested, and historically specific meanings into a restricted technical category, proxy, aggregation rule, or benchmark target that is treated as neutral and difficult to contest. The paper develops a bounded conceptual and qualitative synthesis across value pluralism, pluralistic alignment, participatory and democratic AI, procedural justice, science and technology studies, accountability research, aggregate themes from 11 expert interviews, and three urban AI companion cases. The cases illustrate how pluralistic methods can improve or structure model behavior while still compressing categories, proxies, aggregation rules, and revision rights before affected actors have procedural standing. We introduce Pluralistic Lifecycle Governance (PLG) as a preliminary qualitative audit scaffold for documenting ontological openness, epistemic inclusion, procedural authority, evaluation pluralism, and lifecycle accountability. PLG is not presented as a validated scoring instrument; it is a framework for making the evidence and governance conditions of pluralistic AI explicit.

---


### 331. [Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Ying Fang, Guofa Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single image dehazing continues to be hindered by the loss of high-frequency details and the difficulty of accurate physical scattering modeling. To address these issues, we propose Fi-Gaussian, a frequency-aware implicit Gaussian splatting network for single image dehazing. Unlike explicit rendering methods that rely on 3D point clouds, our method employs implicit Gaussian splatting to adaptively model the underlying distribution of clear images as a continuous representation in 2D feature space. The core of the network is a frequency-aware implicit Gaussian splatting module, which decouples low-frequency structural information and high-frequency texture information in the frequency domain and then performs adaptive Gaussian aggregation with complex-valued weights to recover fine details. In addition, a physics-driven scattering renormalization mechanism is introduced to estimate the transmission map and atmospheric light under the guidance of implicit Gaussian priors. Extensive experiments on multiple benchmark datasets demonstrate that Fi-Gaussian achieves state-of-the-art quantitative performance and produces visually superior dehazed results, validating the effectiveness of implicit Gaussian splatting for low-level vision tasks.

---


### 332. [PAL-Bench: Evidence-Grounded Profile Reconstruction from Longitudinal Personal Albums](https://arxiv.org/abs/2606.16175)

**<font color=#1a73e8>作者：</font>** Qiwei Yan, Zhiqiang Yuan, Zexi Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Longitudinal personal albums are weak-schema multimodal databases: noisy perceptual records whose key facts require joins across faces, text, timestamps, locations, and repeated events. Existing visual, video, document, and lifelog benchmarks test sub-problems, but not album-scale profile reconstruction with social identity binding and evidence citation. Benchmarking this task is difficult because the ground truth needed for evaluation--owner profiles, social graphs, face-name maps, and evidence provenance--is private state that real albums cannot safely release. We introduce PAL-Bench, a controlled benchmark for evidence-grounded reconstruction under a public-record contract. Its Evidence Compiler builds latent private worlds, programs target-level evidence paths, renders album pixels, re-measures them through perception pipelines, and exports audited public/private views. Agents receive only perception-derived public records; targets, identifier maps, and evidence paths remain hidden. PAL-Bench contains 50 synthetic users, 36,659 public photo records, and 2,799 targets over owner facts, identities, and relations. A privacy-preserving audit with 10 participants confirms that PAL-Bench evidence structures match real private albums, though equivalent releases remain privacy-prohibitive. Across seven systems and two compute-matched diagnostics, a seven-metric protocol reveals a gap between plausible profile summarization and faithful social reconstruction: systems recover some owner facts but struggle with recurring identities and evidence citation. PAL-TRACE, a reference framework that freezes identity bindings before owner-fact mining, performs best but leaves hard identity resolution far from solved. PAL-Bench provides a testbed for perceptual entity resolution, multimodal data integration, temporal evidence aggregation, and provenance-aware structured prediction.

---


### 333. [To forget is to preserve: Machine Unlearning for 3D medical image segmentation](https://arxiv.org/abs/2606.16180)

**<font color=#1a73e8>作者：</font>** Nitesh Kumar Singh, Akhilesh Singh, Arjun Arora  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With new data privacy laws such as the General Data Protection Regulation (GDPR) [1] that allow individuals to ask that any of their personal information be erased from trained machine learning models, there has been a push to investigate the unlearning of data from models as a way to comply with these laws. In this regard, based on four mechanics, we consider several approximate unlearning strategies applied to the MRBrainS18 dataset [2]. We use a 3D ResNet-50 [3] as a backbone architecture for segmentation that has been pre-trained with the Med3D framework [4]. Considering the pre-trained model as a baseline, we evaluate respective retention accuracy on 2 types of subjects, i.e., retain and forget. We assess these approaches through their Dice similarity coefficient and mean absolute error (MAE) values using two separate training horizons 20 and 50 epochs. The results show that the Noisy Label strategy had the best overall trade-off with a decrease of 93% in the forget set while maintaining 84% accuracy for the retained set after 50 epochs. All other strategies showed extreme levels of forgetting at higher epoch numbers while also demonstrating catastrophic degradation of their retain set performance. The results of this study provide a strict baseline of performance metrics for unlearning on a subject-specific level and provide practitioners with clear criteria for selecting the proper strategies.

---


### 334. [Closed-Loop Triplet Synergistic Generation for Long-Form Video](https://arxiv.org/abs/2606.16184)

**<font color=#1a73e8>作者：</font>** Xinlei Yin, Xiulian Peng, Xiao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-shot long-form video generation remains challenging due to identity drift and compounding inconsistencies across shots. While storyboard-driven pipelines improve controllability, they are often executed in a feed-forward manner, with limited mechanisms to incorporate generated visual evidence back into subsequent conditioning. We propose CoTriSyGen, an agentic framework that formulates multi-shot long video generation as a closed-loop visual-text-memory synergy process, where planned intent, persistent memory, and generated visuals are jointly leveraged for iterative correction and long-range coherence. A vision-language-model-based analyzer reasons over this triplet and produces updates to both prompts and memory along two pathways: (i) intra-shot refinement, which triggers targeted regeneration when semantic or compositional violations are detected and refines image-to-video prompt for coherent motions; and (ii) inter-shot refinement, which rewrites subsequent-shot prompts to propagate newly manifested entities or attributes and improve prompt quality (e.g., compositional grounding and cinematic fluency) based on generated evidence. The loop is grounded in an entity-centric memory modeled as a mutable visual state that evolves as the story progresses, which is continuously updated by both the generator and the analyzer by adding new and evolved entities to reflect appearance changes, accumulated multi-view evidence, and multi-entity compositions. Experiments on our curated StoryBench benchmark demonstrate substantial improvements in cross-shot consistency, prompt adherence, and cinematic continuity over representative methods.

---


### 335. [Learned JPEG Compression for DNN Vision](https://arxiv.org/abs/2606.16185)

**<font color=#1a73e8>作者：</font>** Kaixiang Zheng, Ahmed H. Salamah, Siyu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> JPEG, a lossy image compression technique designed for human viewers, has maintained its dominance for decades. However, in the era of artificial intelligence (AI), a substantial portion of image data, often compressed by JPEG, is and will continue to be consumed by deep neural networks (DNNs) instead of humans, thus creating a need to optimize JPEG for DNN inference performance. To this end, we propose learned JPEG compression for DNN vision (J4D), a novel training framework for determining JPEG encoding parameters to minimize compression rate while maximizing DNN inference performance. The major challenge of solving this optimization problem lies in representing the JPEG codec and compression rate in closed form. By incorporating a differentiable soft quantizer based on a probabilistic quantization scheme, we not only obtain a differentiable proxy for the JPEG codec, but are also able to compute the entropy of the coded source analytically, which is a close estimate of the actual compression rate. Equipped with both the differentiable JPEG codec and the information-theoretic rate estimator, we are then able to solve the aforementioned optimization problem with backpropagation. After training, the learned encoding parameters will be subsequently used in actual JPEG encoding based on probabilistic quantization. Extensive experimental results across multiple datasets and DNN architectures demonstrate that J4D consistently and significantly outperforms the default JPEG and other competitive JPEG codecs optimized for DNNs. Notably, compared to the default JPEG, J4D achieves an increase in accuracy by as much as 11.60% at the same rate, or a reduction of compression rate up to 80.05% at the same accuracy. Additionally, with the help of J4D, we show the potential to design universal JPEG encoding parameters for various DNN architectures for the first time.

---


### 336. [teasr: training-efficient any-step diffusion transformer for real-world image super-resolution](https://arxiv.org/abs/2606.16188)

**<font color=#1a73e8>作者：</font>** Xiang Gao, Chenxin Zhu, Yushun Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models excel in Real-World Image Super-Resolution (Real-ISR) due to their powerful generative priors but suffer from slow iterative sampling. Although existing one-step distillation methods accelerate inference, they typically require auxiliary teacher models that inflate training memory and restrict scalability to large-scale architectures. Furthermore, these fixed-step models lack the flexibility to trade off speed for quality. In this paper, we propose TEASR, a training-efficient any-step diffusion framework for Real-ISR that enables both one-step and multi-step restoration within a unified model. Our key idea is to perform self-adversarial distillation within a single diffusion model, eliminating the need for auxiliary teachers or discriminators. Specifically, we propose a timestep-aware rectification strategy that stabilizes one-step generation across noise levels. These two designs further enables the distillation of 20B-parameter diffusion models on a single GPU, significantly improving training efficiency. Moreover, we introduce a dual-branch diffusion transformer with decoupled timestep condition to separate the current noise state and the denoising target to enhance sampling quality. Extensive experiments demonstrate that TEASR supports seamless any-step sampling and consistently outperforms state-of-the-art methods across multiple datasets.

---


### 337. [Scalable Malware Family Classification Using Quantum Kernel Based Machine Learning](https://arxiv.org/abs/2606.16191)

**<font color=#1a73e8>作者：</font>** Ratun Rahman, Hassan Jalil Hadi, Christopher Gabriel Pedraza Pohlenz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The classification of malware families is a key challenge in cybersecurity, which enables threat attribution, analysis of attack operations, and the formulation of effective defense strategies. Emerging malware samples are becoming increasingly structurally similar and obfuscated, making accurate multiclass classification challenging for traditional machine learning models, especially when deployed at scale. In this research, we propose a scalable Quantum Kernel-based Machine Learning (QKML) framework for malware family classification that addresses both accuracy and efficiency constraints. The proposed framework extracts structural features from executable files and uses a supervised Linear Discriminant Analysis (LDA) projection to generate a compact, class-aware representation well suited for quantum processing. The nonlinear relationships among malware families are captured using a fidelity-based quantum kernel built from parameterized quantum circuits. We use the Nyström approximation method to obtain a low-rank approximation of the quantum kernel, which enables effective multiclass classification via ridge regression and enables learning from all available training samples without incurring the quadratic computational cost of kernel matrix construction. The proposed model achieves strong classification performance, with 80.88% accuracy, outperforming classical machine learning baselines under identical feature and data splits, according to experimental evaluation on a large-scale malware dataset that includes 18,836 samples across 23 malware families. These findings suggest that scalable quantum-kernel-based machine learning can offer measurable performance advantages for real-world malware family classification tasks.

---


### 338. [When Confidence Lacks Concepts: Interpretable OOD Detection via Representation Perturbations](https://arxiv.org/abs/2606.16196)

**<font color=#1a73e8>作者：</font>** Anju Chhetri, Pratik Shrestha, Ramesh Rana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have achieved remarkable performance across medical imaging tasks, yet their tendency to overgeneralize under distributional shifts poses a major obstacle to safe clinical deployment. Out-of-Distribution (OOD) detection methods aim to mitigate this risk, but most existing approaches rely on opaque internal signals with poorly understood semantic meaning, limiting trust in safety-critical settings. In this work, we propose an interpretable OOD detection framework that probes the stability of model predictions under class-conditioned semantic perturbations. Leveraging sparse autoencoders (SAEs), we learn class-specific concept vectors from in-distribution data that disentangle dense intermediate representations into sparse, semantically meaningful components. At inference, we perturb deeper-layer representations using the concept vectors associated with the model's predicted class and measure the class logits stability. We hypothesize that in-distribution samples exhibit low sensitivity to such perturbations, as their representations align with class-specific semantic directions, whereas OOD samples show amplified deviations due to representational misalignment. By framing OOD detection as a concept conditioned stability analysis, our approach provides both a discriminative OOD signal and an interpretable lens into the internal mechanisms driving model uncertainty, making it particularly suitable for high stakes medical applications.

---


### 339. [EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video](https://arxiv.org/abs/2606.16202)

**<font color=#1a73e8>作者：</font>** Hyunjin Kim, Ri-Zhao Qiu, Guangqi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans naturally understand object physics through everyday interactions, but faithfully predicting complex deformable dynamics, such as elastic materials and fabrics, remains a major challenge for computer vision and robotics. We present EgoPhys, a framework that constructs deformable physical digital twins from egocentric RGB-only video using generalizable priors. EgoPhys overcomes the limitations of existing methods to enable controllable deformable digital twin generation from egocentric videos by distilling per-object inverse-physics solutions into a compact codebook, enabling prediction of dense spring stiffness fields for unseen objects without per-spring test-time optimization. Trained with generalizable priors from diverse egocentric interactions, EgoPhys outperforms baselines in reconstruction, future prediction, and zero-shot generalization. To support training and evaluation, we curate an egocentric interaction dataset covering diverse deformable objects, scenes, and manipulation styles. We deploy EgoPhys on a real xArm6 robot, demonstrating that a digital twin initialized from a single egocentric human play video can serve as an internal world representation to aid in deformable-object planning, highlighting egocentric RGB observations as a scalable path toward real-to-sim pipelines.

---


### 340. [Sensor-Conditioned Representation Learning via Scene-Relevant Observation Quotients](https://arxiv.org/abs/2606.16210)

**<font color=#1a73e8>作者：</font>** Yan Jiao, Pin-Han Ho, Limei Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned representations in intelligent sensing systems are often evaluated by reconstruction fidelity or downstream prediction accuracy, but these criteria do not specify which latent distinctions are justified by the sensing process. In sensor-conditioned environments, nuisance factors can change measurements without changing the scene, while distinct scenes may be indistinguishable under limited sensing capability. This paper formulates sensor-conditioned representation correctness as preserving sensing-supported scene distinctions while suppressing nuisance-induced and sensor-unsupported variation. We introduce the scene-relevant observation quotient, a representation target induced by sensing-supported distinguishability after nuisance canonicalization, and develop Observation-Quotient Tucker-Structured Autoencoding (OQ-TSAE), a scene-nuisance factorized framework with diagnostics for false distinction, false merge, nuisance sensitivity, and latent ordering consistency. Experiments on a controlled benchmark show that quotient-consistent supervision improves representation-correctness diagnostics over reconstruction-oriented, metric-learning, and contrastive-learning baselines. Sensitivity, perturbation, and ablation studies show the importance of quotient-aligned supervision, reliable quotient relations, and quotient geometry. Complementary real-radar experiments show that a reconstruction-only OQ-TSAE variant retains competitive downstream utility, robustness under observation degradation, and low seed-to-seed variability. These results suggest that sensor-conditioned representations should be evaluated not only by predictive utility, but also by whether their latent geometry preserves sensing-justified scene distinctions.

---


### 341. [LUCID: Learned Undersampling-Adaptive Consistency-Guided Inference with Deterministic Flow Matching for Sparse-View CT Reconstruction](https://arxiv.org/abs/2606.16212)

**<font color=#1a73e8>作者：</font>** Jigang Duan, Jiayi Wang, Heran Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view CT reduces radiation dose and scanning time by acquiring fewer projection views, but angular undersampling makes reconstruction severely ill-posed, causing streak artifacts, structural blurring, and loss of fine details. Existing supervised methods are often tied to specific sampling settings, whereas generative methods may introduce anatomically inconsistent hallucination-like structures under severe undersampling. We propose Lucid, a sparsity-adaptive, consistency-guided reconstruction framework based on a Flow Matching generative prior for sparse-view CT. Lucid is trained only on high-quality CT images to learn a continuous transport between a Gaussian distribution and the high-quality CT image distribution, independent of view sampling. During inference, the sampling sparsity level is explicitly incorporated to adapt the generative trajectory of a single pretrained model. Specifically, Lucid constructs a degradation-matched initial state by sparsity-weighted fusion of the sparse-view FBP image and Gaussian noise, performs sparsity-modulated Flow Matching updates, and applies projection-domain data-consistency correction after each prior update. Experiments under multiple sparse-view settings show that Lucid achieves stable reconstruction performance across different sampling densities, improves image quality and structural fidelity, and reduces the risk of hallucination-like structures in generative sparse-view CT reconstruction.

---


### 342. [Calibrated Sampling-Free Uncertainty Estimation in Bayesian Deep Learning](https://arxiv.org/abs/2606.16214)

**<font color=#1a73e8>作者：</font>** Tobias Jan Wieczorek, Leon de Andrade, Thomas Möllenhoff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning models remain notoriously prone to overconfidence, limiting their reliability in high-stakes applications. Bayesian methods aim to counter this by learning a distribution over model parameters, and recent advances now make this feasible for large-scale architectures at costs comparable to AdamW. However, a challenge remains at test time: predictions must be averaged across many forward passes with weights sampled from the posterior, which is prohibitively expensive. Variance propagation offers an efficient alternative, computing layer-wise analytical approximations of uncertainty in a single forward pass. While such techniques are effective for MLPs, their extension to modern architectures remains challenging, due to increased depth and diversity of layer types. To fill this gap, we propose Calibrated Variance Propagation (CVP), which introduces a new propagation method for normalization layers, combines it with recent techniques for handling activation functions, and absorbs residual error through a light calibration step. CVP yields comparably accurate uncertainty estimates to MC sampling across transformers and CNNs, at a fraction of the cost. Against prior variance propagation work, CVP improves coverage at $0.5\%$ risk from $8.2\%$ to $14.6\%$ with BEiT-3 on Visual Reasoning (NLVR2) and from $2.6\%$ to $10.8\%$ with ViLT on VQAv2, with gains extending to convolutional architectures.

---


### 343. [PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents](https://arxiv.org/abs/2606.16215)

**<font color=#1a73e8>作者：</font>** Zhenbang Du, Jun Luo, Zhiwei Zheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn tool-use agents must reason, call tools, and adapt to observations across several interaction turns. Post-training such agents is challenging, as reinforcement learning often suffers from sparse rewards and weak credit assignment despite matching the prompt-only inference setting, while supervised fine-tuning on expert traces provides dense process supervision but can over-constrain the model to fixed trajectories. To tackle this, we propose PACT, a Privileged trAce Co-Training framework for multi-turn tool-use agents. The key idea is to use expert traces only as training-time optimization signals rather than rollout-time hints. PACT keeps rollout generation prompt-only, then uses expert traces to guide optimization through two complementary signals: a trace-conditioned RL surrogate that evaluates prompt-only rollouts under expert-trace context, and a component-aware SFT loss that supervises reasoning prefixes and tool-calls with annealed strength. To reduce over-reliance on the training-only trace context, PACT further introduces a prompt-only anchoring. We also provide a latent-trace view that connects the two trace-based objectives and explains how expert traces can guide optimization without being used during rollout generation. Experiments on FTRL, BFCL, and ToolHop show that PACT consistently improves over strong SFT- and RL-based baselines, highlighting the value of privileged trace co-training for multi-turn tool-use learning.

---


### 344. [did:crdt: Coordination-Free Decentralised Identifiers via Signed CRDTs](https://arxiv.org/abs/2606.16223)

**<font color=#1a73e8>作者：</font>** Hugo O'Connor, Claire Barnes  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing Decentralised Identifier (DID) methods require coordination, an agreed global order of operations, to update a DID document: blockchain-anchored methods incur fees and latency; lightweight peer methods (did:key, did:peer) offer no update mechanism; and Sidetree methods still require blockchain ordering for finality. We present did:crdt, a DID method that targets W3C DID Core and removes the need for coordination entirely: there is no ledger, no sequencer, and no global total order. Each DID document is composed of signed Conflict-Free Replicated Data Types (CRDTs), one per document field, each chosen so that concurrent edits merge deterministically. By the CALM Theorem, the state-merge path is then confluent: replicas that see the same updates reach the same document in any arrival order. The signed-delta path needs only causal delivery, applying an update after those it builds on, which is far weaker than the total ordering ledgers impose and needs no agreement protocol. We are explicit about scope: every untrusted-peer path is authenticated, so Byzantine fault tolerance (safety even when peers lie or send malformed data) holds for signed deltas and verified-bundle replay, while the unauthenticated state-merge path is a trusted-domain optimisation and key-compromise recovery is bounded by revocation semantics. We give the data and threat model, CRUD semantics, conflict resolution, and a Rust reference implementation with property-based convergence tests and microsecond-scale merge latency.

---


### 345. [Prediction of Runtime Parameters of Parallel Chemistry Applications via Active and Generative Learning](https://arxiv.org/abs/2606.16226)

**<font color=#1a73e8>作者：</font>** Tanzila Tabassum, Omer Subasi, Ajay Panyala 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we develop two main Machine Learning based approaches to predict the runtime parameters of highly scalable parallel chemistry this http URL approaches employ active and generative learning together with the empirically determined gradient boosted regression tree models chosen among a rich suite of machine learning models. When evaluated on Coupled-Cluster with Singles and Doubles computations, our models achieve a mean absolute error percentage (MAPE) as low as 0.023 and a coefficient of determination as high as 99.9%. Furthermore, when combined with active learning to mitigate the lack of large amounts of training data, our models score a MAPE about 0.2 with 20-25% of the original dataset.

---


### 346. [Propagating Structural Guidance: Synthesizing Fluorescein Angiography from Fundus Images and Sparse OCT Scans](https://arxiv.org/abs/2606.16234)

**<font color=#1a73e8>作者：</font>** Tengfei Ma, Ruiqi Wu, Chenran Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fundus fluorescein angiography (FFA) is critical for assessing retinal vascular abnormalities, but its acquisition is invasive and not always feasible. In contrast, color fundus photography (CFP) is non-invasive and widely accessible, which has motivated studies on CFP-to-FFA synthesis. However, prior works rely solely on CFP surface texture, fundamentally limiting the ability to reconstruct functional vascular information and subtle pathological changes. To address this, we propose a novel framework that synthesizes FFA from CFP with structural guidance provided by optical coherence tomography (OCT). We construct a multi-modal retinal imaging dataset with paired CFP, FFA, and OCT from 3,676 patient eyes--the first tri-modally aligned dataset in retinal imaging. To bridge the spatial gap between OCT and fundus modalities, we propose a Spatially Aligned Cross-Modal Fusion (SACMF) module that projects depth-resolved OCT features onto the fundus plane and injects them into the CFP encoder via adaptive layer normalization. Beyond feature fusion, we further introduce Token-wise Cross-Modality Alignment (TCMA), a token-level contrastive learning strategy that explicitly aligns CFP and FFA representations at corresponding spatial positions. Our method achieves superior synthesis performance compared to state-of-the-art methods. Moreover, extensive experiments demonstrate that the FFA images synthesized by our approach bring greater improvements in downstream disease diagnosis performance than existing methods, highlighting the clinical potential of our approach as a non-invasive decision-support tool in routine workflows. The code is available at this https URL.

---


### 347. [Evolutionary Bilevel Reward Shaping for Generalization in Reinforcement Learning](https://arxiv.org/abs/2606.16236)

**<font color=#1a73e8>作者：</font>** Ekasit Usaratniwart, Xilin Gao, Marc Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) often suffers from performance degradation when deployed in environments that differ from those encountered during training. Existing techniques such as domain randomization (DR) mitigate this, but require access to diverse training environments and full trajectory observability, assumptions that fail in privacy-preserving or restricted scenarios where only scalar performance metrics are available. We propose Generalization via Evolutionary Reward Shaping (GERS), a bilevel optimization approach to improve generalization on unseen test environments using only scalar feedback from validation environments. At the lower level, an RL agent guided via a reward function shaped by the upper level learns a policy on a limited set of training environments with accessible trajectory data; at the upper level, CMA-ES optimizes the reward shaping parameters to maximize the cumulative unshaped reward on separate validation environments for which trajectory access is unavailable. Results on continuous control tasks indicate that GERS outperforms the standard RL baseline on unseen test environments. GERS performance is comparable to DR, despite DR treating the combined set of training and validation environments of GERS as a single training set that requires trajectory access, whereas GERS cannot access validation trajectories. These results confirm that GERS effectively enhances generalization under restricted data access constraints.

---


### 348. [Structure-Semantic Co-optimized Latent Diffusion Model for Fast Visual Anagram Synthesis](https://arxiv.org/abs/2606.16241)

**<font color=#1a73e8>作者：</font>** Xiang Gao, Yunpeng Jia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual anagram is an intriguing form of art creation wherein a single image presents different conceptual interpretations under transformations such as flipping or rotation. Recent work has achieved visual anagram synthesis by leveraging pretrained text-to-image (T2I) diffusion models, yet still suffers from several key limitations including computational inefficiency, suboptimal aesthetic quality, and weak semantic fidelity and expressiveness. This work focuses on generating visual anagrams with substantially improved visual quality at minimal computational cost, thereby advancing intelligent creation of illusionary digital art. To increase image resolution while reducing time overhead, we adapt the cutting-edge parallel denoising algorithm from pixel-based T2I model to the adversarially distilled latent-based one, and accordingly propose a structure-semantic co-optimization (S2CO) framework to counteract the consequent visual degradation. As the core of our approach, S2CO framework comprises three key innovations: (\romannumeral1) null-text structure alignment optimization; (\romannumeral2) semantic enhancement optimization; (\romannumeral3) attention-guided noise fusion. Building upon these components, our method dubbed \textbf{S2CO-Anagram} is able to generate higher-resolution anagram images with noticeably superior visual harmony and semantic faithfulness than related SOTA approaches, all while achieving substantially faster inference speed. Code will be publicly available.

---


### 349. [Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework](https://arxiv.org/abs/2606.16242)

**<font color=#1a73e8>作者：</font>** David Huang, Jaewon Chang, Avidan Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Rapid Response (RR) framework, deployed in production systems, including Anthropic's ASL-3 safeguards, continuously improves jailbreak-detection classifiers. When new jailbreaks emerge that bypass these classifiers, Rapid Response generates synthetic variants for training, helping the model generalize from the new attacks and quickly adapt. We reveal that prompt injection can infiltrate this pipeline to deliver poisoned samples into the classifier's training set, enabling two attack objectives: (I) targeted poisoning attacks that create false positives on harmless samples by categorizing them as a jailbreak, with a specific desired feature (e.g., certain formatting, subject, or keyword), (II) concept-based backdoor attacks that induce false negatives on jailbreak inputs, generalizing even to jailbreaks from attack strategies the defender explicitly trained against, when the backdoor trigger is present. Importantly, our threat model restricts adversaries to modifying only jailbreak samples (not benign data or labels), a constraint unexplored by prior work that makes the second objective particularly challenging. We address this with Omission Attack, which exploits a new phenomenon: when training on concept-absent unsafe samples, the classifier misassociates that concept's presence with the safe label. Both attacks cause substantial and in some cases near-complete label flipping at only a 1% poisoning rate, achieving up to 100% false positive rates and up to 96% false negative rates.

---


### 350. [LiFT: Local Search via Linear Programming for Overfitting-Controlled Transformers](https://arxiv.org/abs/2606.16243)

**<font color=#1a73e8>作者：</font>** Abhishek Shukla, Anikeit Khanna, Ankur Sinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Linear Programming (LP)-based local search framework for fine-tuning pretrained transformer models with explicit control against overfitting. The approach formulates transformer fine-tuning as a bilevel optimization-based regularization problem, in which model parameters and regularization hyperparameters are jointly updated. Information collected during initial warm-up iterations, including validation gradients and training Hessian information, is used to construct a local descent direction by solving an LP that minimizes a scaled directional derivative while preserving training optimality. This validation-aware descent direction enables focused local updates of both parameters and regularization hyperparameters, reducing overfitting without requiring repeated full retraining cycles. The resulting method, termed Linear Programming-based Fine-Tuning (LiFT) for transformers, differs from conventional fine-tuning by systematically identifying task-specific updates rather than relying on heuristic or grid-based hyperparameter selection. Experiments on GPT-2 Small fine-tuned on WikiText-2 demonstrate that LiFT enables effective adaptation through selective tuning of transformer blocks and regularization parameters, yielding consistent improvements in test perplexity across multiple layer configurations and regularization settings, with particularly pronounced gains in overfitting-prone scenarios. Beyond empirical performance, LiFT establishes a principled connection between transformer fine-tuning, bilevel optimization, local search, and regularization theory.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
