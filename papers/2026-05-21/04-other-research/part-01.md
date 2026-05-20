# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

---

### 1. [OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments](https://arxiv.org/abs/2605.18758)

**<font color=#1a73e8>作者：</font>** Felix Henry, Xiaochen Lin, Jiangyou Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for graphical user interface (GUI) agents predominantly rely on static screenshots. However, real-world smartphone interaction routinely requires agents to process transient audio cues and temporal video dynamics that are tightly coupled with the moment of action. To bridge this gap, we introduce OmniGUI, the first step-level benchmark designed to evaluate GUI agents in omni-modal smartphone environments. OmniGUI provides continuous, interleaved multimodal inputs comprising static images, synchronous audio, and video clips at every action step. The dataset encompasses 709 expert-demonstrated episodes (2,579 action steps) across 29 applications, systematically annotated with objective multimodal dependency levels. Because dedicated omni-modal GUI agent frameworks are currently in their nascent stage, we select foundational omni-modal models capable of natively processing interleaved inputs to serve as agent proxies for our initial baselines. Our empirical evaluation reveals that while current models exhibit competency on visually static tasks, their action prediction performance degrades significantly in environments requiring synchronous temporal and auditory signals. Furthermore, ablation studies isolate specific operational bottlenecks, notably cross-modal interference when processing task-irrelevant environmental noise. The complete dataset, evaluation pipeline, and baseline prompts are provided in the supplementary material. Project page: this https URL.

---


### 2. [Balancing Teacher and Student Agency: Co-Orchestration Tool Design Supporting Real-Time Dynamic Pairing](https://arxiv.org/abs/2605.18761)

**<font color=#1a73e8>作者：</font>** Kexin Bella Yang, Menghan Liu, Liyi Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In human-AI interaction, respecting user agency is essential for fostering trust and sustaining effective use of technology. In educational settings, dynamically integrating individual and collaborative learning offers pedagogical value by supporting personalized, self-paced learning experiences. Prior research has demonstrated the feasibility of this approach through intelligent tutoring systems and human-AI co-orchestration tools. However, how to balance teacher and student control in this process remains largely unexplored. This work explores the design space of how control can be distributed between teachers and students across the orchestration process, using participatory speed dating and a mixed-method analysis. We focus on three stages of the pairing process: before, during, and after, taking context in designing classroom orchestration tools that support teachers in dynamically coordinating student transitions between individual practice and collaborative problem-solving. It contributes empirical insights to the fields of educational technology and HCI by framing these findings within a theoretical design space, emphasizing the balance of multi-stakeholder agency and control. We propose design recommendations for achieving hybrid-control in analytic-based orchestration tools in pairing contexts. We recommend ensuring structured teacher guidance in the beginning, while progressively increasing student autonomy over time as activities unfold.

---


### 3. [Decentralized autonomous organization and blockchain-based incentivization framework for community-based facilities management](https://arxiv.org/abs/2605.18773)

**<font color=#1a73e8>作者：</font>** Reachsak Ly, Alireza Shojaei, Xinghua Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional facility management often relies on centralized decision-making structures that limit stakeholder participation, leading to misalignment with occupant needs and reduced satisfaction. This paper proposes a novel blockchain- and Decentralized Autonomous Organization (DAO)-based framework for community-based facilities management in smart buildings. The framework comprises two key components: a decentralized governance platform that facilitates transparent collective decision-making through blockchain-based voting, and a maintenance management platform with an incentivization mechanism that encourages building occupants to actively contribute to facility upkeep through tokenized rewards. System evaluation includes cost analysis, scalability, data security considerations, usability testing, and semi-structured interviews with facility managers and researchers to assess the platform's usefulness, challenges, and adoption potential. The findings demonstrate the framework's potential as a viable incentivization solution for engaging stakeholders in the collective upkeep and improvement of building infrastructure.

---


### 4. [Dimensional Balance Improves Large Scale Spatiotemporal Prediction Performance](https://arxiv.org/abs/2605.18793)

**<font color=#1a73e8>作者：</font>** Jing Chen, Shixiang Pan, Yujie Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate spatiotemporal pattern analysis is critical in fields such as urban traffic, meteorology, and public health monitoring. However, existing methods face performance bottlenecks, typically yielding only incremental gains and often exhibiting limited cross-domain transferability. We analyze this bottleneck through spatial and temporal entropy measures, which are used as diagnostic indicators of spatiotemporal complexity mismatch rather than as guarantees that entropy alignment alone yields better forecasting. Empirically, larger mismatch is often accompanied by higher prediction uncertainty, especially under a fixed model-capacity budget. Guided by this diagnostic, we propose a scalable, adaptive framework that harmonizes spatial and temporal feature representations. Spatial dimensionality is compressed via low-rank matrix embedding to preserve essential structure, while an extended temporal horizon captures long-range dependencies and mitigates cumulative errors arising from temporal heterogeneity. Extensive experiments on urban traffic, meteorological, and epidemic datasets demonstrate substantial accuracy gains and broad applicability across the evaluated domains, suggesting that the framework is promising for a wide range of spatiotemporal tasks beyond the current study. The code is available on GitHub at this https URL.

---


### 5. [Robust Basis Spline Decoupling for the Compression of Transformer Models](https://arxiv.org/abs/2605.18794)

**<font color=#1a73e8>作者：</font>** Joppe De Jonghe, Van Tien Pham, Mariya Ishteva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoupling is a powerful modeling paradigm for representing multivariate functions as compositions of linear transformations and univariate nonlinear functions. A single-layer decoupling can be viewed as a fully connected neural network with a single hidden layer and flexible activation functions, providing a direct link with neural networks. Because of this, the use of decoupling methods has gained increasing attention in neural network domains, particularly compression, since it enables structured approximations with reduced parameter complexity. Existing tensor-based decoupling methods typically rely on polynomial or piecewise-linear parameterizations of the internal nonlinear functions, which can suffer from numerical instability or limited expressiveness. In this work, we introduce a B-spline-based decoupling framework that generalizes these existing approaches. By exploiting the local support and flexible smoothness control of B-splines, the proposed formulation yields a more numerically stable and expressive representation. We derive a constrained coupled matrix-tensor factorization and propose a robust alternating least-squares algorithm, called R-CMTF-BSD, incorporating normalization and Tikhonov regularization. The proposed method is validated through experiments on synthetic data and transformer model compression. Results on the Vision and Swin Transformer architectures demonstrate that B-spline decoupling enables substantial parameter reduction while maintaining competitive accuracy, making the R-CMTF-BSD algorithm a promising tool for structured neural network compression.

---


### 6. [Simply Stabilizing the Loop via Fully Looped Transformer](https://arxiv.org/abs/2605.18797)

**<font color=#1a73e8>作者：</font>** Rao Fu, Zixuan Yang, Jiankun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling model performance typically requires increasing model size. Looped Transformer offers a compelling alternative by iteratively reusing the same Transformer blocks, trading additional computation for improved performance without increasing parameter count or context length. Because the number of loop iterations can be adjusted at inference, it also provides a natural mechanism for balancing performance and test-time compute. However, Looped Transformer still suffers from training instability when the number of loop iterations increases. Our analysis reveals that this instability stems from two sources: gradient oscillation and residual explosion. To address these two problems, we propose the Fully Looped Transformer, which introduces two parameter-free modifications: (1) Fully Looped Architecture, which distributes inter-loop signals across all layers to mitigate residual explosion; (2) Attention Injection, which reuses the existing attention block to suppress gradient oscillation. These modifications stabilize training dynamics, enabling the Fully Looped Transformer to be trained stably up to 12 loop iterations, whereas other baseline looped models collapse in this regime. In milder settings where Looped Transformer does not collapse, Fully Looped Transformer still improves average downstream-task performance by up to 13.2\%. Overall, our experiments demonstrate that Fully Looped Transformer improves training stability, enhances downstream performance, and provides preliminary adaptability under different test-time compute budgets by varying loop iterations at inference.

---


### 7. [Accurate Evaluation of Quickest Changepoint Detectors via Non-parametric Survival Analysis](https://arxiv.org/abs/2605.18798)

**<font color=#1a73e8>作者：</font>** Taiki Miyagawa, Akinori F. Ebihara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose non-parametric estimators for the average run length (ARL) and average detection delay (ADD) in quickest changepoint detection (QCD) under finite and irregular sequence lengths. Although ARL and ADD are widely used as optimality criteria in theoretical and simulation studies, their application to real-world datasets is hindered by limited and irregular sequence lengths. To address this issue, we propose non-parametric estimators for the ARL and ADD, termed KM-ARL and KM-ADD, by drawing an analogy between QCD and survival analysis to model detection probabilities under sequence truncation. We derive estimation bias bounds and prove that they are asymptotically unbiased unless extrapolation is required. Experiments on simulated and real-world datasets demonstrate their practical utility, enhancing robustness against limited and irregular sequence lengths, improving interpretability, and facilitating empirical, intuitive model selection. Our Python code is provided at this https URL, offering ready-to-use implementations for practitioners.

---


### 8. [Adaptive Multi-Scale Goodness Aggregation for Forward-Forward Learning](https://arxiv.org/abs/2605.18804)

**<font color=#1a73e8>作者：</font>** Salar Beigzad, Vansh Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Adaptive Multi-Scale Goodness Aggregation (AMSGA), a novel extension of the Forward-Forward (FF) algorithm designed to improve stability, robustness, and generalization in local-learning neural networks. AMSGA addresses several limitations of the original FF framework by introducing multi-scale goodness aggregation across local, intermediate, and global representations; adaptive curriculum-guided hard negative mining; layer-dependent adaptive thresholds; and a warm-up cosine annealing learning-rate schedule for improved optimization stability. Together, these modifications strengthen the FF paradigm while preserving its biologically plausible and memory-efficient properties. Experiments on MNIST and Fashion-MNIST demonstrate consistent performance improvements over the baseline FF algorithm, achieving up to +1.45% improvement on MNIST and +1.50% improvement on Fashion-MNIST without significant computational overhead. Our results suggest that local learning methods can become substantially more competitive when goodness estimation and training dynamics are carefully designed.

---


### 9. [Block-Based Double Decoders](https://arxiv.org/abs/2605.18807)

**<font color=#1a73e8>作者：</font>** Asher Labovich, Benjamin Bradley, Vanessa Alexander 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encoder-decoder models offer substantial inference-time savings over decoder-only models, but their pretraining objectives suffer from sparse supervision and dynamic sequence lengths, keeping them out of practice at scale. We propose block-based double decoders, a novel transformer architecture that utilizes doubly-causal block-based attention masks to train with full loss supervision and static sequence packing, combining decoder-only training efficiency with encoder-decoder inference efficiency. In scaling law experiments, block-based double decoders strongly outperform encoder-decoders and closely track decoder-only models across scales. At inference time, they cut KV-cache memory and per-token compute by at least 2/3 without sacrificing prefill caching or other existing inference optimizations available to decoder-only models.

---


### 10. [Metric-Gradient Projection for Stable Multi-Agent Policy Learning](https://arxiv.org/abs/2605.18809)

**<font color=#1a73e8>作者：</font>** Zuyuan Zhang, Sizhe Tang, Mahdi Imani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-sum multi-agent learning is often governed by a stacked update field in which each agent's policy update changes the optimization landscape faced by the others. This coupling can entangle an integrable component of collective improvement with cyclic interaction dynamics, leading to slow or unstable multi-agent learning. Existing approaches, such as regularization, credit assignment, and consensus methods, stabilize MARL through local or algorithmic modifications; HPML complements them by projecting the joint update field onto a metric-gradient component. We introduce \textbf{HPML} (\textbf{H}odge-\textbf{P}rojected \textbf{M}ulti-agent \textbf{L}earning), which views the joint update field of a multi-agent system as an element of an $L^2$ space of vector fields and computes a Hodge-type projection onto the closest metric-gradient potential flow. HPML follows the projected component as the update direction, yielding the closest metric-gradient field under the chosen metric and sampling measure. The projection is defined variationally, characterized by a Poisson-type equation, and implemented through graph-based and amortized neural realizations that recover projected directions from samples. We show that the projected dynamics admit a Lyapunov potential and yield equilibrium-gap bounds with an explicit additive non-potentiality term. Controlled experiments validate the geometric mechanism, and CTDE benchmarks show improved stability and normalized return when HPML is used as a plug-in projection layer in MARL pipelines.

---


### 11. [D-PACE: Dynamic Position-Aware Cross-Entropy for Parallel Speculative Drafting](https://arxiv.org/abs/2605.18810)

**<font color=#1a73e8>作者：</font>** Tianyu Wu, Yu Yao, Zhenting Qi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by having a small drafter propose tokens that a larger target model verifies in parallel. Recent diffusion-based parallel drafters such as DFlash predict the full B-token block in one forward pass, enabling deeper drafters and longer accepted blocks. However, existing multi-token drafter objectives often use fixed position-dependent weighting schedules, such as head-dependent weights or block-position decays, which do not adapt as the positions limiting acceptance change during training. To address this, we derive per-position training weights from a differentiable surrogate of expected accepted draft length, matching the weight of each position to its log-probability gradient contribution. The resulting loss, D-PACE (Dynamic Position-Aware Cross-Entropy), shifts training signal toward positions that currently limit acceptance as the drafter improves. Across six benchmarks, two Qwen3-4B draft depths, two decoding temperatures, and two additional target models, D-PACE consistently improves both wall-clock speedup and average emitted length, with 2.3\% measured training-time overhead and no changes to the drafter architecture or inference procedure.

---


### 12. [How Faithful Is Trajectory-Based Data Attribution? Error Sources, Remedies, and Practical Guidelines](https://arxiv.org/abs/2605.18814)

**<font color=#1a73e8>作者：</font>** Junwei Deng, Pingbang Hu, Suliang Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory-based data attribution methods estimate the influence of training samples on model predictions by unrolling the training trajectory. They are widely used in applications such as data selection, data valuation, and model diagnosis, but there is a lack of comprehensive error analysis of these methods, raising concerns about method faithfulness and hindering reliable deployment. In this work, we provide the first systematic analysis of error sources in trajectory-based data attribution, together with concrete remedies to mitigate them and practical guidelines for downstream use. We organize the total error into three categories, config-level, algorithm-level, and system-level. We make three contributions. First, we identify optimizer mismatch as the dominant config-level error: existing methods derive their attribution under the assumption of SGD, even for models trained with the modern de facto optimizer AdamW. We propose AdamW-influence to fully account for AdamW's optimization dynamics, yielding improvements from 10% to over 300% in Spearman correlation between estimated and ground-truth influence across four settings spanning MLP, CNN, GPT-2, and Llama 3.2-1B. Second, we isolate the remaining algorithm-level error arising from the first-order Taylor approximation, identify the learning rate and trajectory length as factors governing the error magnitude, and derive a closed-form error proxy that can be evaluated along the original trajectory without retraining. Third, we translate these insights into practical guidelines for data selection by unifying offline and online strategies under a K-step look-ahead framework. Under this framework, online selection with a short horizon often matches or exceeds offline, and the optimal horizon can be tuned jointly with the learning rate. Together, these results turn the framework into an actionable selection recipe for practitioners.

---


### 13. [Symmetry in the Wild: The Role of Equivariance in Neural Fluid Surrogates](https://arxiv.org/abs/2605.18816)

**<font color=#1a73e8>作者：</font>** Patryk Rygiel, Julian Suk, Kak Khee Yeung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates enable orders-of-magnitude acceleration of computational fluid dynamics (CFD) simulations, with the potential to transform engineering and healthcare workflows. Neural surrogate use in real-world applications requires addressing scalability to large, high-resolution surface and volume meshes, as well as to bespoke architectures, and accounting for limited training data through the use of inductive biases. Group-equivariant architectures are a principled way to introduce such bias, yet they can be detrimental when the learning problem itself breaks symmetry, for example, due to strong distributional alignment in the dataset. In this work, we investigate under which conditions equivariance improves generalization in neural CFD surrogates across tasks with increasing levels of distributional alignment and realism, covering automotive aerodynamics and blood flow (hemodynamics). To systematically assess the added value of equivariance at the limit of problem scaling, we introduce the Anchored-Branched Geometric Algebra Transformer (AB-GATr), a neural surrogate that integrates scalability and symmetry preservation to efficiently model coupled surface and volume quantities in an $E(3)$-equivariant manner. We find that on strongly aligned aerodynamics datasets, i.e., those that break symmetry, enforcing equivariance can degrade in-distribution performance. In contrast, across hemodynamic benchmarks with diverse geometries and varying alignment, equivariance is consistently beneficial. Moreover, across all benchmarks, the explicit equivariance of AB-GATr reliably outperforms implicit symmetry learning through data augmentation. Our findings showcase that equivariance is not universally beneficial across domains, yet it brings tangible advantages in problems lacking strong data regularities.

---


### 14. [Multi-Token Residual Prediction](https://arxiv.org/abs/2605.18817)

**<font color=#1a73e8>作者：</font>** Yufeng Xu, Zishuo Bao, Qian Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) generate text by iteratively denoising masked token sequences, offering a tradeoff between parallelism and quality compared to autoregressive models. In current practice, the number of tokens decoded per step is controlled by a confidence threshold, and quality degrades monotonically as more tokens are denoised per step. We introduce Multi-token Residual Prediction (MRP), a lightweight module that enables dependency-aware multi-token denoising within a single backbone forward pass. MRP exploits a key property of the denoising process: the logit distributions at adjacent denoising steps are remarkably similar. Rather than running the backbone a second time to obtain the next-step logits, MRP predicts the residual between steps from the backbone's hidden states, effectively denoising more tokens per backbone forward at a fraction of the cost. We deploy MRP in two inference modes: direct decoding, which uses the corrected logits without verification for a tunable quality--speed tradeoff; and speculative decoding, which verifies MRP's proposals against the backbone for lossless acceleration. Experiments on SDAR models at the 1.7B, 4B, and 8B scales across reasoning and code generation benchmarks demonstrate up to $1.42\times$ lossless speedup in SGLang.

---


### 15. [Efficient Conditioning Why Pseudo Observation Batch Bayesian Optimization Works When It Does not](https://arxiv.org/abs/2605.18819)

**<font color=#1a73e8>作者：</font>** Kumbha Nagaswetha, Rabi Pathak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constant Liar (CL), Kriging Believer (KB), and fantasy models are widely used for batch selection in parallel Bayesian Optimization, yet a unified theory explaining their effectiveness and conditions under which they fail has been lacking. We identify efficient conditioning as the key surrogate property the ability to update predictions in closed form when data is augmented. We prove that Gaussian Processes satisfy this requirement, producing provably distinct batch points with separation of order l, and that this holds for any acquisition function monotonically non decreasing in posterior uncertainty (EI, UCB, PI), with qualitatively similar behavior for Thompson Sampling. We unify CL, KB, and fantasy models as instances of a single conditioning mechanism differing only in the lie value distribution, and draw quantitative connections to Local Penalization (LP) and qualitative connections to Determinantal Point Processes (DPPs). To disentangle model structure from optimizer randomness, we introduce the Structural Diversity Diagnostic (SDD), a reusable methodology for testing surrogate compatibility. Experiments on Hartmann6D, Ackley 8D, Levy10D, and SVM hyperparameter tuning validate all theoretical predictions: CL or KBs implicit penalty matches or outperforms explicit LP greedy conditioning achieves convergence on par with joint qEI efficient conditioning extends to Multiquadric RBF networks; and parametric surrogates produce degenerate batches even when fully retrained (random forests), while neural networks regain diversity only at 15x the wall clock cost of GP conditioning. Robustness is confirmed across multiple initial datasets and under observation noise.

---


### 16. [Emergence of Frontier Superposition: Möbius attractor and Cascade Supervision](https://arxiv.org/abs/2605.18820)

**<font color=#1a73e8>作者：</font>** Hongyu Gu, Jingwen Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Superposition allows Transformers to reason in depth, carrying an entire reasoning frontier in parallel through a bounded-depth forward pass instead of unrolling serial chain-of-thought tokens. While Zhu et al. (2025) hand-crafted an equal-weight breadth-first frontier in a single residual stream for graph reachability, it remained open whether gradient descent could ever find this target amidst permutation-symmetric saddles.
We close this gap on Reachability-by-Superposition over Erdős-Rényi graphs by isolating architectural and supervisional contributions. Architecturally, we identify a Möbius attractor: under $S_n$-symmetry in the tree regime, layerwise dynamics reduce to a 1D Möbius map whose zero set is a codimension-one manifold of global optima containing the equal-weight superposition state.
On the supervision side, we identify Cascade Supervision: a loss class whose backward pass simultaneously delivers (A) selectivity bootstrap, (B) gradient persistence across depth, and (C) per-step discrimination (e.g., \mathcal{L}_{sup} and \mathcal{L}_{node}). End-to-end supervision fails condition (B) and is provably insufficient: internal gradients at layer c decay as (np)^{-(D-c-2)/2} in the graph fan-out and stall before the manifold is reached.
Our thesis: Möbius attractor + Cascade Supervision = emergence of superposition reasoning. The parameter-free decay law predicts a final-step cosine of 0.35 vs. 0.71 (end-to-end vs. cascade) at depth D=3; experiments confirm 0.37 vs. 0.69, matching within 0.02 at every step.

---


### 17. [Quantum Adversarial Machine Learning: From Classical Adaptations to Quantum-Native Methods](https://arxiv.org/abs/2605.18821)

**<font color=#1a73e8>作者：</font>** Roozbeh Razavi-Far, Mohammad Meymani, Erfan Mahmoudinia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has revolutionized numerous industrial domains. Despite recent advances, machine learning models remain vulnerable to adversarial threats. Adversarial machine learning is a field that studies these vulnerabilities to build robust machine learning models. Quantum machine learning is an interdisciplinary field that bridges quantum computing and classical machine learning. While quantum machine learning shows potentials to outperform classical machine learning in complex tasks such as regression, classification, and generative modeling, it remains vulnerable to adversarial attacks. Given the recent advancements in quantum computing and machine learning, the quantum adversarial machine learning field has emerged to study the vulnerabilities of quantum machine learning, possible attacks, and novel quantum-enhanced defense strategies. In this survey, we provide a detailed overview on quantum adversarial machine learning and explore the existing attacks and countermeasures. We also review the theoretical underpinnings of this area, emerging trends, and critical challenges.

---


### 18. [Multi-Pedestrian Safety Warning at Urban Intersections Use Case of Digital Twin](https://arxiv.org/abs/2605.18823)

**<font color=#1a73e8>作者：</font>** Yongjie Fu, Qi Gao, Mahshid Ghasemi Dehkordi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital twins (DTs) for urban transportation systems have gained increasing attention; however, their systematic evaluation in safety-critical scenarios remains limited. This paper presents a multi-pedestrian safety warning system at urban intersections enabled by a tightly coupled physical-digital twin framework. Built upon the COSMOS city-scale wireless testbed in New York City, the proposed system integrates camera and ultra-wideband (UWB), edge-cloud computing, predictive trajectory modeling, and MQTT-based communication to deliver real-time safety alerts to vulnerable road users (VRUs). The system is evaluated through both field deployment and virtual reality (VR) experiments. Results demonstrate high warning generation accuracy, localization accuracy, efficient end-to-end latency under different model configurations, and significant reductions in user response time when warnings are issued. The proposed DT framework provides a scalable, modular, and generalizable solution for real-time multi-pedestrian safety enhancement at complex urban intersections.

---


### 19. [The Routing and Filtering Structure of Attention](https://arxiv.org/abs/2605.18826)

**<font color=#1a73e8>作者：</font>** Shafayeth Jamil, Rehan Kapadia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The attention interaction matrix $QK^{\top}$ contains two entangled computations: a skew-symmetric component that redistributes information between positions (routing) and a symmetric component that scales mutual relevance (filtering). We decompose 1776 heads across five pretrained transformers and find routing operating at low rank, well below the routing capacity allocated by the weight kernel. We introduce $S$-$D$ attention as a diagnostic parameterization that disentangles routing from filtering by construction with guaranteed stability ($\mathrm{Re}(\lambda) \le 0$) and trains stably without layer normalization. When disentangled and unnormalized, routing self-organizes into a spectral cascade, effective rank $2$ at the first layer, expanding with depth across six scales from 7M to 355M parameters. The cascade predicts where attention can be simplified: linearizing the first seven layers of 125M $S$-$D$ attention costs ${<}5\%$ perplexity, whereas standard attention collapses under the same intervention. The linearizable region widens with depth. Replacing the first four layers with ELU+1 linear attention reaches within $1.4\%$ of baseline at full head dimension. Cascade-allocated architectures trade attention parameters for perplexity ($47\%-65\%$ fewer attention parameters at $+3.9\%$ to $+8.4\%$ PPL). The routing-filtering decomposition makes the spectral budget legible; the cascade makes it actionable.

---


### 20. [Lossless Anti-Distillation Sampling](https://arxiv.org/abs/2605.18829)

**<font color=#1a73e8>作者：</font>** Zibo Diao, Jingchu Gai, Xinyue Ai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier commercial generative models face a growing threat from distillation, whereby a distiller harvests generated responses and trains a competing model of its own at drastically lower cost. Existing defenses either rely on modifying the models outputs, thereby sacrificing response quality for benign users, or on behavioral detection methods, which can be readily circumvented by distributing queries across multiple accounts. In this work, we propose Lossless Anti-Distillation Sampling (LADS), a novel sampling scheme specifically designed to counter multi-account distillation while maintaining a lossless experience for benign users. Concretely, LADS derives the randomness underlying each generation from a private seed determined by the semantic content of the query and the number of times the user has queried the model. By construction, every benign user receives a response independently sampled from the original model at each visit, and thus experiences no distortion. In contrast, for a distiller, different accounts share latent randomness whenever their queries fall in the same semantic bucket. As a result, the harvested data becomes correlated, potentially reducing sample diversity and degrading generalization. Using uniform convergence theory, we show that LADS provably degrades the convergence rate of the distillers generalization gap relative to standard i.i.d. sampling in both unconditional and conditional generation settings. Experiments on image generation, mathematical reasoning, and code generation confirm that LADS substantially degrades the performance of distilled students while preserving exact statistical fidelity for individual users.

---


### 21. [Automated Big Data Quality Assessment using Knowledge Graph Embeddings](https://arxiv.org/abs/2605.18833)

**<font color=#1a73e8>作者：</font>** Hadi Fadlallah, Rima Kilany, Mitri Haber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated data quality assessment is crucial for managing big data, but existing solutions face challenges in achieving accurate context-aware assessment. This paper presents a novel knowledge-based approach to enhance automated data quality assessment. Our approach utilizes knowledge graph embeddings to predict missing edges between the input dataset's context representation and the relevant quality rules and dimensions within a knowledge graph representing contextual data characteristics and the required quality assessment operations. We surpass conventional practices by integrating diverse representations within the knowledge graph, drawing insights from contextual information from a thorough literature investigation. This integration allows us to develop a comprehensive and context-specific data quality assessment plan tailored to each context. Leveraging the knowledge graph improves our understanding of the input dataset's context, overcoming the limitations of traditional methods that rely solely on strict matching and overlook contextual characteristics. By injecting numerical edge attributes, we assign corresponding weights to each predicted quality measurement, providing a comprehensive data quality assessment plan for the input dataset.
To evaluate our approach, we leverage AmpliGraph, a framework developed and benchmarked by AccentureLabs. The evaluation involves employing a real-world radiation sensors dataset provided by the Lebanese Atomic Energy Commission (LAEC-CNRS). The results obtained from this evaluation demonstrate the capability of our solution to generate a comprehensive data quality assessment plan for the given input dataset.

---


### 22. [Spectral Gradient Surgery for Domain-Generalizable Dataset Distillation](https://arxiv.org/abs/2605.18836)

**<font color=#1a73e8>作者：</font>** Minyoung Oh, Najeong Chae, Jae-Young Sim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dataset Distillation (DD) synthesizes a compact synthetic dataset that preserves the training utility of a full dataset. However, its standard formulation assumes that test data follow the same distribution as training data, an assumption that rarely holds in practice. A straightforward extension-applying post-hoc Domain Generalization (DG) techniques to distilled data-is ill-suited because existing DG methods rely on the natural diversity of real datasets, which compact synthetic sets inherently lack, while also incurring substantial augmentation overhead that conflicts with the efficiency objective of dataset distillation. To address this limitation, we introduce Domain Generalizable Dataset Distillation (DGDD), a new problem setting that explicitly targets out-of-distribution (OOD) generalization of distilled datasets. We study this problem through a widely adopted DD baseline of Distribution Matching (DM). We attribute the OOD vulnerability of DM to the entanglement of class-discriminative and domain-specific information within the compressed synthetic set, and propose Spectral Gradient Surgery (SGS) to disentangle the two. The key insight of SGS is that cross-domain agreement among domain-wise gradients in the spectral domain reveals which gradient components are shared across source domains-and are therefore class-discriminative-and which are domain-specific. Based on this observation, SGS augments the standard DM update with two complementary gradients: one that reinforces cross-domain shared components and another that explicitly promotes diversity within the distilled dataset. Extensive experiments on diverse-scale benchmarks demonstrate that SGS substantially improves OOD generalization while remaining plug-and-play compatible with existing DM methods.

---


### 23. [VCR: Learning Valid Contextual Representation for Incomplete Wearable Signals](https://arxiv.org/abs/2605.18837)

**<font color=#1a73e8>作者：</font>** Yuxuan Weng, Wenhan Luo, Qijia Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable devices enable continuous health monitoring from multimodal signals, but real-world deployment is hindered by limited labeled data and pervasive sensor incompleteness. While large-scale self-supervised pretraining reduces label dependence, most existing methods assume full modality availability. Current approaches for handling modality missingness often reconstruct entire absent signals, which can encourage hallucinating modality-specific details that are not inferable from the observed sensor signals and degrade robustness. We propose VCR, a self-supervised framework that learns to extract valid representations robust to modality missingness. VCR employs an orthogonal tokenizer to enforce strict orthogonal disentanglement by rectifying latent manifolds and applying a geometric projection, separating each modality into shared semantics and modality-specific residuals. This design preserves complete information integrity while serving as a structural foundation for robust learning under modality missingness. The resulting tokens are processed by a missing-aware mixture-of-experts backbone that adapts to varying patterns of modality availability. By constraining the objective to reconstruct only the shared components of missing modalities, VCR effectively mitigates hallucinations of non-inferable modality-specific details. Across multiple health monitoring tasks, VCR consistently improves performance and robustness under full, single-missing, and multiple-missing modality settings compared with strong supervised and self-supervised baselines.

---


### 24. [An Integrated Forecasting Prototype for Emergency Department Boarding Time to Support Proactive Operational Decision Making](https://arxiv.org/abs/2605.18839)

**<font color=#1a73e8>作者：</font>** Orhun Vural, Abdulaziz Ahmed, Ferhat Zengul 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overcrowding in emergency departments (ED) remains a persistent operational challenge worldwide, causing delays in care delivery and downstream congestion. ED boarding time, defined as the duration admitted patients remain in the ED while awaiting inpatient bed placement, is a key indicator of this congestion. Predicting ED boarding time in advance enables proactive operational decision making before congestion escalates. We developed and evaluated a multi-horizon time series forecasting framework to predict ED boarding time at 6, 8, 10, 12, and 24-hour horizons. Real-world data from a university-affiliated urban hospital in the United States were utilized and integrated with external contextual data sources, including weather, holidays, and major local events. Decomposition-based Linear (DLinear) and Normalization-based Linear (NLinear) time series forecasting deep learning models showed superior performance across multiple horizons. Models were also evaluated under extreme congestion scenarios characterized by elevated boarding times. In addition, a Machine Learning Operations (MLOps) web application prototype was developed to support translation of the forecasting framework into practice through integrated data ingestion, forecast visualization, experimentation, and retraining.

---


### 25. [The Growing Pains of Frontier Models: When Leaderboards Stop Separating and What to Measure Next](https://arxiv.org/abs/2605.18840)

**<font color=#1a73e8>作者：</font>** Adil Amin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leaderboards rank frontier models on independent axes but do not reveal whether capabilities reinforce or trade off across releases -- and at the frontier, this interaction is the more informative signal. We decompose paired SWE-bench and GPQA Diamond scores into a population coupling trend and per-release residual ($h$-field) that diagnoses capability emphasis and identifies which measurement or stress test is most informative next. Across 34 models from 10 labs (2024--2026), capabilities cooperate ($r = +0.72$, $p < 10^{-6}$), but cooperation varies by lab and over time: DeepSeek reversed from reasoning-rich to coding-first ($h$: $+11.2 \to -4.7$, 15.9-pp swing); Google maintains consistent reasoning emphasis; Anthropic oscillates between coding excursions and recovery. Cooperation is not static -- it cascades. Six open-weight architectures confirm a second capability transition at 30--72B, and SWE-bench is now saturating while HLE and instruction-following retain discriminatory spread -- signaling the next axis rotation. We provide a three-level playbook (locate, diagnose, rotate), a per-lab measurement-priority table, and seven falsifiable predictions with timestamped criteria for the next 12 months of frontier releases. Per-lab coupling slopes vary $5\times$ (Google $1.15$ vs. DeepSeek $0.23$), quantifying how efficiently each recipe converts coding gains into reasoning. Five April 2026 releases confirm the diagnostic out of sample ($r$ rises from $+0.72$ to $+0.75$). An interactive dashboard provides phase classification with actionable recommendations, $h$-field diagnostics, per-lab coupling trajectories, ODE-based scaling predictions, benchmark rotation guidance, self-steering demo, and live tracking of all seven predictions: this https URL.

---


### 26. [From Cumulative Constraints to Adaptive Runtime Safety Control for Nonstationary Reinforcement Learning](https://arxiv.org/abs/2605.18841)

**<font color=#1a73e8>作者：</font>** Timofey Tomashevskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety in reinforcement learning is often specified through cumulative cost constraints, but these trajectory-level guarantees do not directly prevent unsafe individual decisions, especially under nonstationarity. In continual and nonstationary settings, the difficulty is amplified because the risk associated with the same action can vary across contexts, while a fixed state-level threshold may be either too conservative or too weak. We propose Constraint Projection Safety Shield (CPSS), a runtime mechanism that converts a cumulative safety budget into adaptive state-level control constraints during execution. CPSS tracks the remaining safety budget, projects it into a time-varying admissible risk threshold, and filters policy actions whose predicted safety cost exceeds the active threshold. The threshold is adjusted online using contextual signals so that enforcement becomes stricter in more demanding or rapidly changing regimes and less restrictive when the available safety budget is sufficient. We analyze the resulting shielded policy and show that the mechanism guarantees per-state threshold satisfaction for executed actions, induces finite-horizon cumulative cost bounds, and yields a performance degradation bound in terms of intervention frequency and per-step reward distortion. We evaluate CPSS in nonstationary highway merging scenarios using highway-env. Across multiple seeds, CPSS substantially reduces proximity-based safety violations and increases separation margins while intervening selectively rather than dominating the learned policy. These results support adaptive budget-to-threshold projection as a practical way to transform cumulative safety specifications into effective local safety control for continual reinforcement learning systems.

---


### 27. [Safe Continual Reinforcement Learning under Nonstationarity via Adaptive Safety Constraints](https://arxiv.org/abs/2605.18842)

**<font color=#1a73e8>作者：</font>** Timofey Tomashevskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning in nonstationary environments requires safety mechanisms that adapt as environmental conditions change. Standard safe reinforcement learning methods often assume fixed constraints or stable environmental conditions, which can become inadequate under distribution shift. We propose LILAC+, a framework for safe continual reinforcement learning under nonstationarity that combines three adaptive safety mechanisms: context-based safety constraints, adaptation-speed constraints, and budget-to-state safety enforcement. Context-based constraints adjust safety requirements using inferred and predicted environmental context. Adaptation-speed constraints tighten safety requirements when the rate of environmental change exceeds the agent's ability to adapt safely. Budget-to-state enforcement converts cumulative safety requirements into local state-level control constraints that can be enforced at decision time. Together, these mechanisms provide a unified approach for proactive and reactive safety adaptation in continual reinforcement learning. We evaluate the framework in simulated driving environments under stationary, seen nonstationary, and unseen nonstationary conditions. The results show that adaptive safety constraints substantially reduce safety violations under distribution shift while maintaining competitive task performance compared with unconstrained and fixed-constraint baselines. These findings suggest that safe continual reinforcement learning requires adaptive constraint mechanisms that respond not only to current state information but also to predicted environmental context, adaptation demand, and remaining safety budget.

---


### 28. [Graph-Driven Cross-Industry Real-Time Monitoring Framework for Anti-Money Laundering Detection in Converged Mobility-Energy Supply Chain Networks](https://arxiv.org/abs/2605.18844)

**<font color=#1a73e8>作者：</font>** Rong Liu, Xiaojun Xiao, Zhanqing Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the deep integration of the travel and energy industries, cross-industry supply chain finance has gradually become a high-risk field of hidden money laundering incidents. For this reason, this work proposes a graph-driven cross-industry real-time anti-money laundering monitoring framework (GCRMF) for integrated travel - energy supply chain networks. First, a cross-industry heterogeneous graph (CIHG) covering new energy vehicle rental platforms, energy suppliers, fintech institutions, etc., is constructed, and industry semantics are integrated through temporarily Dual-GAT (Temporal Dual-Graph Attention Network), dynamically encoding capital flow paths and evolution features over time. Subsequently, in order to identify the structural fraud behavior together produced by colluding subjects, a meta-path subgraph reasoning module based on contrastive learning and hierarchical graph sampling is proposed to enhance the discrimination capability of cross-industry recurring money laundering behavior. Meanwhile, a self-supervised online learning mechanism is adopted for real-time adaptation and continuous optimization to new money laundering strategies. The experimental results show that compared with existing graph neural network methods in cross-industry scenarios, GCRMF improves the performance by more than 17.8% of F1 score and greatly reduces the false positive rate.

---


### 29. [First-Passage Prediction of Grokking Delay: ACalibrated Law under AdamW with Causal Validation](https://arxiv.org/abs/2605.18845)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give the first quantitative prediction of grokking delay under AdamW. Treating the delay as a first-passage time, we derive a closed-form law T_grok - T_mem = (1 / 2 kappa_LL eta lambda) log(V_mem / V_star), where V_t = ||theta_t||^2 is the squared parameter norm, V_star is an architecture-dependent threshold, and kappa_LL absorbs the AdamW correction to the clean-SGD contraction rate 2 eta lambda. Calibrating (kappa_LL, V_star) on a single hyperparameter cell predicts grokking delays on 26 held-out runs with MAPE 17.7% over a 41x delay range; the law generalises to MLPs (MAPE 18.0%, N=34) and degrades to 23.3% on cross-task extension (N=46, 43.5x range), with a structured residual in which V_star / V_mem stays comparatively stable within architecture (CV about 14% on the 1L transformer).
First-passage of V_t is necessary but not sufficient. A quantile-margin theorem establishes that positive delay requires both norm separation V_mem > V_post and angular reachability of a threshold alpha_star = arcsin(C / V_T_mem^(1/2)), where C is computable from the empirical NTK feature map and the validation-margin quantile. Calibrating C on modulus p=89 predicts alpha_star = 47.2 degrees at p=97 (observed 47.8 degrees, error 1.3%) as a prior cross-cell prediction. Causal interventions that freeze the norm or remove weight decay at memorisation eliminate grokking (0/6 vs. 3/3 baseline), trapping the angular displacement near 12 degrees.
kappa_LL is empirically measured per architecture rather than derived from (beta_1, beta_2, epsilon); within-architecture CV stays at most 15% across four architectures, but values differ by about 2x between architectural variants beyond depth alone. Empirical scope is algorithmic tasks (modular arithmetic, sparse parity) under AdamW; whether the law transfers to natural-language scale models is open.

---


### 30. [Lost and Found in Translation: Variational Diagnostics for Neural Codebook Channels](https://arxiv.org/abs/2605.18846)

**<font color=#1a73e8>作者：</font>** Yusuke Hayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical communication systems fail not only through random noise but also when transmitter and receiver use incompatible operational codebooks. Variational autoencoders (VAEs) train an encoder $q_\phi$ and decoder $p_\theta$ jointly, and practitioners treat the resulting latent space as a discrete code -- for clustering, conditional generation, and mechanistic interpretability. Yet standard VAE diagnostics -- ELBO, active units, mutual information, and code histograms -- certify only whether this code is used, never whether the decoder reads each latent under the encoder's code.
We close this gap with the neural codebook channel $K_{e\to d}(j\mid i)$, a coupled encoder-decoder diagnostic whose off-diagonal mass is bounded by an architecture-free Bernoulli-KL certificate $d_{\mathrm{bin}}(1-\mathcal{A} \,\|\, \bar\eta_p) \le \bar\Delta$ controlled by the variational gap. The certificate is the operational specialization of the classical KL chain rule under disintegration to the encoder-decoder disagreement event, complemented by a constructive marginal-impossibility result: no combination of marginal histograms, entropies, active-code counts, or mutual information determines $K_{e\to d}$.
We audit the certificate on four sklearn datasets (finite-grid exact, 5/5 seeds, 20/20 pairs satisfy the bound), a 2D model where the bound is non-vacuous at $2.71\times$ the observed disagreement and the four-term identity closes within $10^{-4}$, MNIST under importance-sampling control, and a VQ-VAE attaining the predicted limit $\hat{\mathcal{A}}=1.000$. The package $(K_{e\to d}, \mathcal{A}, R_{\mathrm{eff}}, R, \mathrm{AU})$ is an audit-ready reporting unit. More broadly, the framework makes mismatched decoding -- a failure mode classical communication theory named decades ago -- visible inside a single deep generative model.

---


### 31. [Exact Linear Attention](https://arxiv.org/abs/2605.18848)

**<font color=#1a73e8>作者：</font>** Weinuo Ou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Exact Linear Attention (ELA), a mechanism that achieves linear computational complexity for Transformer attention by leveraging the exact decomposition property of kernel functions, without any approximation error. It identifies and addresses gradient explosion and token attention dilution in prior linear attention methods by imposing kernel constraints that ensure non-negativity, discriminability, and geometric interpretability. Several kernel functions are proposed, including the Hadamard Exp Kernel, Summation Squared Euclidean Distance Kernel, and Subtraction Squared Euclidean Distance Kernel. Beyond the core attention formulation, the paper presents three engineering innovations: a Hyper Link structure that replaces traditional residual connections to mitigate gradient degradation, a Memory Lobe module based on bidirectional linear attention that captures transformation flow across layers to implement qualitative memory and an implicit reinforcement learning paradigm, and a routing score based bias mechanism for Mixture of Experts to improve interpretability and semantic alignment.

---


### 32. [INSIGHTS: Demonstration-Based Summaries of Time Series Predictors](https://arxiv.org/abs/2605.18849)

**<font color=#1a73e8>作者：</font>** Bar Eini Porat, Rom Gutman, Uri Shalit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainability methods have progressed rapidly, but global explanations for time-series models remain underdeveloped, with most approaches focusing on local, instance-level attributions. We introduce INSIGHTS, a model-agnostic, user-centric approach for providing global explanations of time series models. Our approach prioritizes simplicity, efficiency, and transparency in its design, ensuring that stakeholders can readily adopt its outputs. While current methods focus on local explanations, INSIGHTS generates sample summaries that offer a comprehensive overview of model behavior. It balances the importance and diversity of time series samples to create informative subsets using utility functions that capture domain-specific aspects of time series behavior, such as exceeding domain norms. We evaluate INSIGHTS through experiments, interviews, and a user study. Our results indicate INSIGHTS effectively constructs comprehensive, diverse time series subsets, producing summaries manageable for individual evaluation. It is preferred by domain experts for its ability to provide a stable understanding of model behavior and the quality of the samples identified. Moreover, user study participants presented with INSIGHTS-based summaries exhibit an enhanced understanding of the model's overall behavior.

---


### 33. [INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference](https://arxiv.org/abs/2605.18853)

**<font color=#1a73e8>作者：</font>** Ahmed Šabanović, Paul Joe Maliakel, Ivona Brandić  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge deployment of Vision-Language Models (VLMs) faces a tradeoff between latency and accuracy: cloud execution provides high-quality predictions but incurs communication delay and energy cost, while edge-only execution is faster but less accurate due to limited model capacity. This trade-off is further complicated by heterogeneity in image quality and reasoning complexity, making static placement suboptimal. We present INAR-VL, a lightweight edge-cloud routing system for multimodal inference in a two-tier deployment. INAR-VL maintains complementary VLMs across edge and cloud and uses lightweight image and text complexity signals to guide routing and model selection, executing simple queries locally while offloading complex ones when beneficial. Evaluation on visual question answering shows that INAR-VL executes 36% of requests on the edge, reduces latency by 24%, lowers energy by 26%, and preserves 97% of cloud-level accuracy.

---


### 34. [Evaluating Memory Condensation Strategies for Coding Agents in Data-Driven Scientific Discovery](https://arxiv.org/abs/2605.18854)

**<font color=#1a73e8>作者：</font>** Renuka Chintalapati, Sid Raskar, Anurag Acharya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents accumulate extensive context during long-running tasks, yet fixed context windows force practitioners to choose between truncation and task failure. While numerous memory condensation strategies have been proposed, from simple sliding windows to LLM-generated summaries, no systematic comparison exists to guide strategy selection, especially in scientific discovery tasks. We evaluate eight memory condensation strategies using GPT-4o on sixty DiscoveryBench tasks spanning six scientific domains (480 total evaluations). We find that no condenser significantly alters hypothesis quality, while LLM-based condensers increase token costs by 24-94 percent, and masking tool-call outputs achieves an 8.6 percent net savings. We also observe that the optimal condenser for data-driven scientific discovery varies by scientific domain and task length.

---


### 35. [Delta Attention Residuals](https://arxiv.org/abs/2605.18855)

**<font color=#1a73e8>作者：</font>** Cheng Luo, Zefan Cai, Junjie Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention Residuals replace standard additive residual connections with learned softmax attention over previous layer outputs, enabling selective cross-layer routing. However, standard Attention Residuals still attend over cumulative hidden states in previous layers, which are highly redundant. We show that this redundancy leads to routing collapse in deeper layers: attention weights become low-contrast and closer to uniform (max weight ${\approx}$0.2), limiting the model's ability to select informative states in previous layers. This raises a key but underexplored design question: what layer-wise representations should be routed in Attention Residuals? To answer this question, we propose Delta Attention Residuals, which attend over deltas -- the change introduced by each sublayer ($\mathbf{v}_i = \mathbf{h}_{i+1} - \mathbf{h}_i$) -- instead of cumulative states. Delta representations are structurally diverse and yield higher-contrast attention distributions (max weight ${\approx}$0.6), enabling more selective and effective routing across layers. This principle applies at both per-sublayer and block granularity. Across all tested scales (220M--7.6B), Delta Attention Residuals consistently outperform both standard residuals and Attention Residuals, with 1.7--8.2\% validation perplexity gains. Delta Attention Residuals also enables converting pretrained checkpoints into Delta Attention Residuals via standard fine-tuning. Code is available at this https URL.

---


### 36. [SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference](https://arxiv.org/abs/2605.18856)

**<font color=#1a73e8>作者：</font>** Anay Chauhan, Gurucharan Marthi Krishna Kumar, Arion Das 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context inference is increasingly constrained by the KV cache: resident memory grows with context length, and decoding becomes limited by repeated High Bandwidth Memory (HBM) streaming rather than arithmetic. Existing methods such as eviction, windowing, quantization, and offloading reduce footprint, but often leave the critical-path bottleneck only partially addressed, especially when compressed states must still be reconstructed into dense vectors during decoding.
We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding. The method is built on two ideas: (i) represent directional information cheaply in the decode hot loop, and (ii) allocate retention and precision according to estimated future utility. Its first component, Angle-Domain Attention (ADA), stores keys in a spherical parameterization consisting of a scalar radius and compact angle codes, and computes attention logits directly from these codes without reconstructing dense keys. This preserves a paged, block-local, fusion-friendly decode path and directly targets HBM traffic in realistic serving settings. Its second component, Rate-Distortion Retention (RDR), jointly chooses keep/drop decisions and precision tiers per token and head under a fixed budget, producing tier-homogeneous pages with lightweight metadata and coalesced reads. Together, ADA and RDR provide a deployment-oriented mechanism for reducing KV residency while preserving decode efficiency.

---


### 37. [When Individually Calibrated Models Become Collectively Miscalibrated](https://arxiv.org/abs/2605.18858)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic prediction systems often aggregate probability estimates from multiple models into a single decision. A common assumption is that if each model is individually calibrated, the aggregate prediction will also be well calibrated. We show that this assumption fails in multi-agent settings: individually calibrated predictors can become collectively miscalibrated when their predictions interact strategically, in the game-theoretic sense of Brier-optimal local response, even without deliberate coordination.
This phenomenon arises naturally when agents are independently trained on overlapping data. We prove that under Brier-score-based aggregation with positively correlated beliefs, each agent's individually optimal report systematically underestimates the positive-class probability, yielding a Price of Anarchy greater than one whenever Cov(b_i, b_j) > 0.
In a canonical setting (n = 5 agents, pairwise correlation = 0.5, base rate = 0.3), the empirically measured PoA in false-negative rate reaches 7.25x. In contrast, VCG-based aggregation aligns incentives by rewarding marginal contribution, achieving dominant-strategy incentive compatibility and near-optimal performance.
Experiments on three real-world datasets (NSL-KDD, UNSW-NB15, Credit Card Fraud) show that VCG provides strong robustness while maintaining comparable accuracy. It performs particularly well in data-sparse and adversarial settings, and adaptive weighting further improves performance under distribution shift.

---


### 38. [Towards Family-Grouped Hierarchical Federated Learning on Sub-5KB Models: A Feasibility Study of Privacy-Preserving ECG Monitoring for Ultra-Resource-Constrained Wearables](https://arxiv.org/abs/2605.18862)

**<font color=#1a73e8>作者：</font>** Hangyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiovascular disease remains the leading cause of death worldwide, and early detection of arrhythmias through continuous ECG monitoring on wearable devices can prevent life-threatening events. Federated Learning (FL) enables privacy-preserving collaborative training by keeping raw ECG data on device, yet standard FL incurs prohibitive communication overhead and standard deep learning models cannot fit on ultra-low-power microcontrollers. We propose Family-Grouped Hierarchical Federated Learning (Family-FL), a three-tier architecture that uses the family as a natural privacy boundary for intra-family aggregation before global synchronization. We further design a hardware-constrained Tiny CNN-LSTM architecture with only 669 parameters, INT8-quantized to occupy merely 4.65KB Flash and 2.95KB RAM, meeting the constraints of STC32G12K128-class microcontrollers. Experiments on the MIT-BIH Arrhythmia Database (mean of 5 independent runs with different seeds) demonstrate that Family-FL reduces communication volume by 76.7% compared to FedAvg while maintaining comparable accuracy. Family-FL-Tiny achieves 91.9 +/- 1.2% accuracy with macro-F1 of 0.483 +/- 0.031, reducing total communication to 0.31% of FedAvg. The model achieves reliable ventricular arrhythmia detection (per-class F1 = 0.80), the most clinically critical abnormality for home-based preliminary screening. These results demonstrate the technical feasibility of privacy-preserving federated learning on ultra-resource-constrained microcontrollers through simulation-based evaluation. We honestly discuss limitations: no hardware deployment, single-dataset validation (MIT-BIH, 47 subjects), reduced rare-class sensitivity, and absence of formal differential privacy guarantees.

---


### 39. [From Sparsity to Simplicity: Enabling Simpler Sequential Replacements via Sparse Attention Distillation](https://arxiv.org/abs/2605.18865)

**<font color=#1a73e8>作者：</font>** Yuxin Ren, Maxwell D Collins, Miao Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention serves as the core foundation of large-scale transformer pretraining, but its quadratic token interaction cost makes inference expensive. Replacing attention with simpler sequential modules is appealing, yet naive substitution is often lossy, especially at larger scales. This paper revisits attention replacement through the lens of sparsity. Based on the observation of diverse sparsity patterns across transformer layers, we posit that pretrained transformers decompose the complex token dependency across tokens into various sequence-to-sequence mappings of diverse complexities, where some layer functionalities can be approximated and replaced with much simpler sequential modules without loss. We evaluate this premise using a plug-and-play layer-wise distillation framework to approximate and replace attention functionalities in pretrained vision transformer models. Controlled group-wise replacements under a fixed training budget reveal a clear pattern: substituting layers with sparser attention incurs substantially smaller accuracy drops than replacing denser ones. We further impose explicit attention sparsity on the pretrained ViT via AViT-style token retention and perform sparsity-guided distillation for sequential replacing models, where we see increasing teacher sparsity consistently reduces the student-teacher gap. The proposed method achieves efficient attention replacement for reduced parameter size and latency through the guidance of attention sparsity.

---


### 40. [FLUIDSPLAT: Reconstructing Physical Fields from Sparse Sensors via Gaussian Primitives](https://arxiv.org/abs/2605.18866)

**<font color=#1a73e8>作者：</font>** Huaxi Huang, Meng Li, Zhengqing Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous flow fields from sparse surface-mounted sensors is central to aerodynamic design, flow control, and digital-twin instrumentation. Existing neural methods for this task typically encode sensor readings into implicit latent codes with little spatial interpretability and limited formal guidance on how representational capacity should scale with observation count. Inspired by 3D Gaussian Splatting, we introduce FLUIDSPLAT, a sensor-conditioned model that predicts K anisotropic Gaussian primitives forming a partition-of-unity scaffold, a spatially explicit and interpretable intermediate representation of the flow. For an idealized Gaussian primitive estimator, we prove an $O(K^{-s/d})$ approximation rate for fields with Sobolev smoothness $s$; incorporating $N$ noisy observations yields a squared-risk decomposition with bias $O(K^{-2s/d})$ and variance $O(\sigma^{2}K/N)$.Balancing the two yields $K^{*}\!\sim\!(N/\sigma^{2})^{d/(2s+d)}$: primitive count cannot grow freely under sparse sensing, revealing a variance bottleneck that motivates complementing the scaffold with a state-conditioned residual decoder. On a standard cylinder-flow benchmark, FLUIDSPLAT achieves the best mean error across all surface-sensor layouts; on AirfRANS with 8 surface-pressure sensors, it reduces error by 11-23% over the strongest baseline across three standard splits.

---


### 41. [EVA-0: Test-Time Model Evolution with Only Two Forward Passes per Sample](https://arxiv.org/abs/2605.18867)

**<font color=#1a73e8>作者：</font>** Guohao Chen, Shuaicheng Niu, Geng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time model evolution offers a promising way for deployed models to improve from unlabeled test-time experience, yet most existing methods depend on backpropagation (BP), which incurs substantial memory overhead and makes them difficult to deploy on edge devices, quantized models, specialized accelerators, or black-box models. In this work, we study test-time model evolution under a strict two-forward budget, a setting that pushes adaptation toward highly efficient real-world deployment. We reveal three key obstacles in zeroth-order test-time optimization: susceptibility to shortcut solutions, uncontrolled weight drift, and ineffective update direction estimation. To overcome them, we propose EVA-0, a minimal zeroth-order adaptation framework that: 1) keeps the loss scale-invariant to prevent shortcut solutions; 2) devises an anchor-guided optimization strategy to alleviate weight drift; 3) uses sample-wise symmetric two-sided perturbation for update direction estimation and inference. EVA-0 requires no BP and performs both inference and adaptation within only two forward passes per sample. Results on ImageNet-C & ViT-Base show that EVA-0 outperforms both BP-based DeYO and BP-free FOA, while achieving a 14x speed-up over FOA. Code will be released.

---


### 42. [Multi-Headed Transformer Architectures as Time-dependent Wasserstein Gradient Flows](https://arxiv.org/abs/2605.18870)

**<font color=#1a73e8>作者：</font>** Alex Massucco, Leonardo Del Grande, Marcello Carioni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, transformer architectures have revolutionized the field of language processing, opening the door to previously unforeseen possibilities. However, from a theoretical point of view, the mathematical models proposed in the literature often lack direct contact with the actual architectures and depend on strong simplifying assumptions. In this paper, we reduce this gap by modelling the data flow in multi-headed transformer architectures as time-dependent gradient flows for a suitable interaction energy capturing the design of the attention mechanism. The explicit dependence on time allows us to consider different weights for each head and for each layer, without imposing constraints on the initialization method. Moreover, we prove that, under a suitable integrability assumption on the evolution of the weights, each element of the $\omega$-limit set of the gradient flows is a stationary point of the interaction energy at a limiting weight distribution. Finally, we analyse the stability of the gradient flows considering perturbations of both the initial data and the weights. Specifically, on the one hand, we study the robustness of the proposed models with respect to noisy inputs, establishing a continuous dependence of the gradient flows on the initial data and uniqueness of the flows. On the other hand, we prove the $\Gamma$-convergence of the perturbed interaction energy to the unperturbed one, leading to the convergence of the corresponding gradient flows. We complement these theoretical results with numerical experiments that confirm the predicted energy-dissipation identity and clarify the asymptotic behavior of the dynamics in both the autonomous-like (Ornstein--Uhlenbeck) and the genuinely non-autonomous (oscillating-weights) regimes.

---


### 43. [EUPHORIA: Efficient Universal Planning via Hybrid Optimization for Robust Industrial Robotic Assembly](https://arxiv.org/abs/2605.18872)

**<font color=#1a73e8>作者：</font>** Shih-Yu Lai, Chia-Ching Yen, Yang-Ting Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robotic assembly in architectural construction faces a persistent bottleneck: existing planners are either highly specialized, requiring prohibitive retraining for every new geometric design, or operationally inefficient, treating structural sequencing and kinematic motion as disjoint processes. We present EUPHORIA, a unified framework that achieves universal few-shot adaptability and dynamic efficiency through a hybrid optimization strategy. To overcome the retraining bottleneck, we propose a Meta-Geometric Encoder based on Graph Hypernetworks: unlike standard contrastive learning, which performs only feature-level recognition, our hypernetwork dynamically generates policy parameters from a minimal support set, enabling parameter-level adaptation to complex topologies (e.g., domes, arches) without gradient-based retraining. For structural reasoning, we introduce a Physics-Informed Graph Transformer trained via Soft Actor-Critic (SAC), with a Physics-Bias Attention mechanism that modulates attention scores using contact forces from Discrete Element Model (DEM) simulations, guiding the planner toward structurally critical connections. We further ensure operational efficiency through Kinematics-Aware Sequencing, where the SAC objective penalizes high-energy transitions. Finally, we bridge the Sim2Real gap via Residual Stability Correction, a differentiable optimization layer that fine-tunes coarse assembly actions by minimizing a joint energy-stability cost prior to execution. Experiments show that EUPHORIA significantly reduces energy consumption over decoupled baselines and achieves state-of-the-art success rates on unseen, non-standard geometries with minimal few-shot examples, fusing meta-learning, physics-informed attention, and residual optimization into a cohesive, generalized planner.

---


### 44. [GenAI-FDIA: Physics-Informed Generative Models for False Data Injection Attacks](https://arxiv.org/abs/2605.18873)

**<font color=#1a73e8>作者：</font>** Mohammad A. Razzaque, Muta Tah Hira  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Training and evaluating false data injection attack (FDIA) detectors for power systems is constrained by data scarcity. Operational grid measurements are commercially sensitive, and hand-crafted attacks fail to capture complex distributional structures imposed by network physics. We present \textsc{GenAI-FDIA}, a framework benchmarking a pool of $P{=}20$ architectures for physics-compliant FDIA synthesis, spanning Wasserstein GANs, MMD-VAEs, normalising flows, diffusion models, and cross-family hybrids. These are evaluated across three IEEE testbeds (14-bus DC, 30-bus DC, and 14-bus AC) under a 60/20/20 chronological split using data-driven Bad Data Detection (BDD) threshold calibration. Our empirical results verify that these models generate high-fidelity attacks, with all architectures achieving evasion rates of $\epsilon_{\text{BDD}} \ge 86.6\%$ on the 14-bus network; additionally, limiting an attacker's topological knowledge induces a measurable degradation in stealthiness ($p \le 0.0022$). Crucially, we identify a previously unreported failure mode: applying affine physics projections directly in normalised feature spaces critically displaces the attack vector, collapsing BDD evasion from ${\sim}55\%$ to $<\!2\%$ on the 30-bus testbed. We resolve this via a novel inference-time harmoniser, restoring full stealthiness ($\epsilon_{\text{BDD}}{=}100\%$) across all physics-informed variants without retraining. Finally, we isolate a covariance-collapse phenomenon ($\kappa \approx {-}0.076$) within advanced hybrid architectures and rectify it through 50-epoch warm-up schedules ($\kappa \to 0.785$, $\Delta\text{MMD}={-}3.1\%$). Ultimately, \textsc{GenAI-FDIA} delivers a robust recovery blueprint applicable to any physics-constrained generative model deployed for power-system security.

---


### 45. [A Multi-Dimensional Clustering Approach for Identifying Inborn Errors of Immunity](https://arxiv.org/abs/2605.18880)

**<font color=#1a73e8>作者：</font>** Nishad Kulkarni, Alexandra K. Martinson, Nicholas L. Rider 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rare diseases such as inborn errors of immunity (IEI) require early diagnosis to prevent end organ damage and improve quality of life. Hurdles in accessing and curating large scale electronic health record (EHR) data limit routine data driven analyses to remain on the forefront of IEI and other rare disease trends. Development of machine learning (ML) algorithms in IEI for pattern recognition as well as published methodology examining how to systematically process and integrate complex medical data is limited. Our proposed pipeline, including data curation and ML clustering algorithms, is designed to recognize novel rare disease patterns and extract IEI- associated features from a national data registry. Our methodology for EHR data formatting and processing presents the pipeline that transforms raw immunologic lab data into vectors. This is further combined with hyperparameter tuning for diseases pattern recognition via clustering. This study refines IEI feature awareness, develops data tool kits for rare disease populations analysis, and expands on transforming complex medical records in data structures interpretable by unsupervised ML.

---


### 46. [Emergence of a Flow-Assisted Casting Strategy for Olfactory Navigation via Memory-Augmented Reinforcement Learning](https://arxiv.org/abs/2605.18881)

**<font color=#1a73e8>作者：</font>** Changxu Zhao, Dongxiao Zhao, Xin Bian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In dynamic flow fields, various animals exhibit remarkable odor search capabilities despite relying on stochastic detections. Interestingly, there exists an optimal time window for integrating these detections that maximizes search efficiency. To understand the underlying mechanism, we investigate the navigation performance of Reinforcement Learning (RL) agents in unsteady flows under varying memory lengths and flow conditions. Without any predefined models, the agents develop a flow-assisted casting strategy and adaptively adjust both the geometry of their search trajectories and the concentration threshold for initiating casting to maximize the success rate. The agent's average speed toward the odor source exhibits a non-monotonic dependence on memory length, which can be explained by the "sector-search" model.

---


### 47. [Prediction Is Not Physics: Learning and Evaluating Conserved Quantities in Neural Simulators](https://arxiv.org/abs/2605.18883)

**<font color=#1a73e8>作者：</font>** Andrew Bukowski, Aditya Kothari, Simba Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A diffusion model trained on Hamiltonian trajectories can achieve rollout MSE near $10^{-3}$, but the standard deviation of its energy over time is between 7500 and 36000 times larger than the ground-truth energy standard deviation, indicating a failure to preserve conservation laws. This gap motivates our central question of whether neural networks can learn or select globally conserved quantities from physical trajectories. We investigate this across three Hamiltonian systems: projectile motion, pendulum, and spring-mass. We use a structured $T(v)+V(q)$ energy model, a black-box Conservation Discovery Network (CDN), a polynomial CDN, and a conditional diffusion baseline. The structured network reaches $R^2 \geq 0.9999$ against analytical energy on clean data, while the black-box CDN reaches $R^2 \geq 0.996$ when trained with temporal consistency plus a small alignment loss to analytical energy at $t=0$ ($\lambda_{\mathrm{align}}=0.2$). With $\lambda_{\mathrm{align}}=0$, CDN Pearson $R^2$ collapses on pendulum and spring-mass ($< 10^{-3}$), showing that temporal consistency alone is not enough to reliably identify the true energy. Under $1\%$ additive Gaussian noise, the CDN outperforms the structured model on the projectile and spring-mass systems, suggesting that the CDN may be more robust to noisy inputs in this setting. However, the polynomial CDN is sensitive to training configuration: it achieves $R^2=0.78$ under a short training schedule on the pendulum system, but reaches $R^2=0.9998$ with more training time and data, regardless of whether noise is added.

---


### 48. [Soft Learning](https://arxiv.org/abs/2605.18889)

**<font color=#1a73e8>作者：</font>** Mohammed Aledhari, Ali Aledhari, Fatimah Aledhari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning forces practitioners to choose between powerful but expensive deep networks and fast but limited classical algorithms. Here we introduce Soft Learning, a framework that maintains a library of heterogeneous specialists -- spanning linear models, tree ensembles, kernel machines, and neural networks -- and discovers provably optimal combination weights through cross-validated non-negative least squares. Soft Learning is guaranteed to match or exceed the best weighted combination of its specialists, trains over two orders of magnitude faster than deep networks on CPU alone (72-435x faster across tested configurations), provides inherent interpretability through learned weights that reveal which algorithmic paradigm best fits the data, and is future-proof: adding specialists is mathematically guaranteed to maintain or improve performance. Across 37 datasets (25 classification, 12 regression) against nine methods including CatBoost and tuned deep networks, Soft Learning ranks first on 70% of tasks, achieves the best mean rank (Friedman test, p = 1.12 x 10^-12), and is the only method to simultaneously excel at both classification and regression -- all without GPU hardware or hyperparameter tuning. These results suggest a paradigm shift from "which algorithm is best?" to "what is the provably optimal combination?" -- a question Soft Learning answers with formal guarantees for any data modality.

---


### 49. [Auditing Reasoning-Trace Memorization Claims after Unlearning with Head-Conditioned Canaries](https://arxiv.org/abs/2605.18891)

**<font color=#1a73e8>作者：</font>** Yanhang Li, Zhichao Fan, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluations of unlearning on reasoning models sometimes show a bypass pattern. The answer side looks unlearned, but the model's own thinking trace keeps emitting the forgotten content, and the gap is taken as evidence that the weights still remember. We audit this reading on DeepSeek-R1-Distill-Qwen-7B with LoRA-memorized fictional authors and NPO unlearning, conditioned on a six-token canary head. On one seed, swapping the thinking trace for a short non-canary prefill on the same weights drops the answer rate by as much as the bypass gap itself, whether the prefill mimics the training template or not. On a second seed the bypass gap shrinks rather than vanishing, and the prefill swap reverses direction and brings the answer rate to ceiling. A positive parser-split bypass gap thus does not by itself identify hidden weight-level memorization, and does not rule it out either. On a different distillate the same metric flips sign because the parser cannot find the closing tag. We recommend a decode-time template swap as a cheap sanity check alongside the canonical audit.

---


### 50. [Data-Free Client Contribution Estimation via Logit Maximization for Federated Learning](https://arxiv.org/abs/2605.18892)

**<font color=#1a73e8>作者：</font>** Asim Ukaye, Nurbek Tastan, Mubarak Abdu-Aguye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative learning of computer vision models, where privacy and regulatory constraints prevent centralizing data across devices or organizations. However, practical FL deployments often exhibit severe class imbalance and label skew, causing standard aggregation protocols to overfit dominant clients and degrade minority-class performance. We propose a data-free, class-wise contribution estimation and aggregation framework based on logit maximization (CELM) that does not require sharing raw data, client metadata, or auxiliary public datasets. The FL server probes client updates to obtain class-wise evidence scores and assembles a cross-client evidence matrix, which quantifies both per-class competence and class coverage. Using this matrix, we compute contribution weights that upweight clients providing strong, discriminative evidence for underrepresented classes. The resulting aggregation is stable due to simplex constraints and momentum smoothing, and it remains compatible with standard FL training pipelines. We evaluate the approach on representative vision benchmarks under controlled non-IID and pathological label splits, demonstrating that CELM-based aggregation improves robustness to imbalance and statistical heterogeneity, while yielding better performance without requiring any additional data exchange.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
