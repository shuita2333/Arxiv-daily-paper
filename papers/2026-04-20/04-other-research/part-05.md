# 📦 其他研究 | 2026年04月20日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

---

### 201. [Class Unlearning via Depth-Aware Removal of Forget-Specific Directions](https://arxiv.org/abs/2604.15166)

**<font color=#1a73e8>作者：</font>** Arman Hatami, Romina Aalishah, Ilya E. Monosov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove targeted knowledge from a trained model without the cost of retraining from scratch. In class unlearning, however, reducing accuracy on forget classes does not necessarily imply true forgetting: forgotten information can remain encoded in internal representations, and apparent forgetting may arise from classifier-head suppression rather than representational removal. We show that existing class-unlearning methods often exhibit weak or negative selectivity, preserve forget-class structure in deep representations, or rely heavily on final-layer bias shifts. We then introduce DAMP (Depth-Aware Modulation by Projection), a one-shot, closed-form weight-surgery method that removes forget-specific directions from a pretrained network without gradient-based optimization. At each stage, DAMP computes class prototypes in the input space of the next learnable operator, extracts forget directions as residuals relative to retain-class prototypes, and applies a projection-based update to reduce downstream sensitivity to those directions. To preserve utility, DAMP uses a parameter-free depth-aware scaling rule derived from probe separability, applying smaller edits in early layers and larger edits in deeper layers. The method naturally extends to multi-class forgetting through low-rank subspace removal. Across MNIST, CIFAR-10, CIFAR-100, and Tiny ImageNet, and across convolutional and transformer architectures, DAMP more closely resembles the retraining gold standard than some of the prior methods, improving selective forgetting while better preserving retain-class performance and reducing residual forget-class structure in deep layers.

---


### 202. [When Flat Minima Fail: Characterizing INT4 Quantization Collapse After FP32 Convergence](https://arxiv.org/abs/2604.15167)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) assumes that a well-converged model is a quantization-ready model. We show this assumption fails in a structured, measurable, and previously uncharacterized way. Using a calibration-free per-group INT4 probe applied to all 154 publicly available Pythia-160m training checkpoints, we identify a three-phase divergence structure: a rapid-learning phase where both FP32 perplexity and quantization robustness improve together, a meta-stable plateau lasting roughly 70,000 steps where FP32 perplexity stagnates but INT4 gap remains bounded, and an explosive divergence phase where the INT4 gap compounds from 11% to 517% while FP32 perplexity barely moves. Critically, this divergence begins not when the learning rate starts decaying, but precisely when FP32 perplexity converges a finer-grained onset predictor that implies post-convergence weight updates, rather than decay magnitude alone, are the proximate cause. We further show that INT8 quantization is entirely immune throughout all three phases, constraining the mechanism to the coarseness of the 16-level INT4 grid specifically, and rule out weight outlier accumulation as the mechanism via direct kurtosis measurement. Finally, we conduct a controlled fork experiment from the pre-divergence checkpoint comparing three learning rate schedules (cosine continuation, SGDR warm restarts, and our proposed Oscillatory Lock-In) across nine independent runs. SGDR uniformly accelerates divergence (0/9 pairwise wins against cosine), while OLI's settled cool phases reduce the INT4 gap by 2.2 percentage points on average (t = -5.46, p < 0.0001), demonstrating that schedule amplitude calibration, not oscillation alone, determines whether perturbation helps or hurts. Our code, probe implementation, and all 154-checkpoint audit results are released publicly.

---


### 203. [OmniLight: One Model to Rule All Lighting Conditions](https://arxiv.org/abs/2604.15170)

**<font color=#1a73e8>作者：</font>** Youngjin Oh, Junyoung Park, Junhyeong Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse lighting conditions, such as cast shadows and irregular illumination, pose significant challenges to computer vision systems by degrading visibility and color fidelity. Consequently, effective shadow removal and ALN are critical for restoring underlying image content, improving perceptual quality, and facilitating robust performance in downstream tasks. However, while achieving state-of-the-art results on specific benchmarks is a primary goal in image restoration challenges, real-world applications often demand robust models capable of handling diverse domains. To address this, we present a comprehensive study on lighting-related image restoration by exploring two contrasting strategies. We leverage a robust framework for ALN, DINOLight, as a specialized baseline to exploit the characteristics of each individual dataset, and extend it to OmniLight, a generalized alternative incorporating our proposed Wavelet Domain Mixture-of-Experts (WD-MoE) that is trained across all provided datasets. Through a comparative analysis of these two methods, we discuss the impact of data distribution on the performance of specialized and unified architectures in lighting-related image restoration. Notably, both approaches secured top-tier rankings across all three lighting-related tracks in the NTIRE 2026 Challenge, demonstrating their outstanding perceptual quality and generalization capabilities. Our codes are available at this https URL.

---


### 204. [An Analysis of Regularization and Fokker-Planck Residuals in Diffusion Models for Image Generation](https://arxiv.org/abs/2604.15171)

**<font color=#1a73e8>作者：</font>** Onno Niemann, Gonzalo Martínez Muñoz, Alberto Suárez Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that diffusion models trained with the denoising score matching (DSM) objective often violate the Fokker--Planck (FP) equation that governs the evolution of the true data density. Directly penalizing these deviations in the objective function reduces their magnitude but introduces a significant computational overhead. It is also observed that enforcing strict adherence to the FP equation does not necessarily lead to improvements in the quality of the generated samples, as often the best results are obtained with weaker FP regularization. In this paper, we investigate whether simpler penalty terms can provide similar benefits. We empirically analyze several lightweight regularizers, study their effect on FP residuals and generation quality, and show that the benefits of FP regularization are available at substantially lower computational cost. Our code is available at this https URL.

---


### 205. [Boundary-Centric Active Learning for Temporal Action Segmentation](https://arxiv.org/abs/2604.15173)

**<font color=#1a73e8>作者：</font>** Halil Ismail Helvaci, Sen-ching Samson Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal action segmentation (TAS) demands dense temporal supervision, yet most of the annotation cost in untrimmed videos is spent identifying and refining action transitions, where segmentation errors concentrate and small temporal shifts disproportionately degrade segmental metrics. We introduce B-ACT, a clip-budgeted active learning framework that explicitly allocates supervision to these high-leverage boundary regions. B-ACT operates in a hierarchical two-stage loop: (i) it ranks and queries unlabeled videos using predictive uncertainty, and (ii) within each selected video, it detects candidate transitions from the current model predictions and selects the top-$K$ boundaries via a novel boundary score that fuses neighborhood uncertainty, class ambiguity, and temporal predictive dynamics. Importantly, our annotation protocol requests labels for only the boundary frames while still training on boundary-centered clips to exploit temporal context through the model's receptive field. Extensive experiments on GTEA, 50Salads, and Breakfast demonstrate that boundary-centric supervision delivers strong label efficiency and consistently surpasses representative TAS active learning baselines and prior state of the art under sparse budgets, with the largest gains on datasets where boundary placement dominates edit and overlap-based F1 scores.

---


### 206. [MambaSL: Exploring Single-Layer Mamba for Time Series Classification](https://arxiv.org/abs/2604.15174)

**<font color=#1a73e8>作者：</font>** Yoo-Min Jung, Leekyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in state space models (SSMs) such as Mamba across various sequence domains, research on their standalone capacity for time series classification (TSC) has remained limited. We propose MambaSL, a framework that minimally redesigns the selective SSM and projection layers of a single-layer Mamba, guided by four TSC-specific hypotheses. To address benchmarking limitations -- restricted configurations, partial University of East Anglia (UEA) dataset coverage, and insufficiently reproducible setups -- we re-evaluate 20 strong baselines across all 30 UEA datasets under a unified protocol. As a result, MambaSL achieves state-of-the-art performance with statistically significant average improvements, while ensuring reproducibility via public checkpoints for all evaluated models. Together with visualizations, these results demonstrate the potential of Mamba-based architectures as a TSC backbone.

---


### 207. [AdaSplash-2: Faster Differentiable Sparse Attention](https://arxiv.org/abs/2604.15180)

**<font color=#1a73e8>作者：</font>** Nuno Gonçalves, Hugo Pitorro, Vlad Niculae 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention has been proposed as a way to alleviate the quadratic cost of transformers, a central bottleneck in long-context training. A promising line of work is $\alpha$-entmax attention, a differentiable sparse alternative to softmax that enables input-dependent sparsity yet has lagged behind softmax due to the computational overhead necessary to compute the normalizer $\tau$. In this paper, we introduce AdaSplash-2, which addresses this limitation through a novel histogram-based initialization that reduces the number of iterations needed to compute $\tau$ to typically 1--2. The key idea is to compute a coarse histogram of attention scores on the fly and store it in on-chip SRAM, yielding a more accurate initialization that enables fast forward and backward computation. Combined with a sparsity-aware GPU implementation that skips zero blocks with low overhead, AdaSplash-2 matches or improves per-step training time relative to FlashAttention-2 when block sparsity is moderate-to-high (e.g., $>$60\%), which often occurs at long-context lengths. On downstream tasks, models trained with our efficient $\alpha$-entmax attention match softmax baselines at short-context lengths and achieve substantial gains in long-context settings.

---


### 208. [One-shot learning for the complex dynamical behaviors of weakly nonlinear forced oscillators](https://arxiv.org/abs/2604.15181)

**<font color=#1a73e8>作者：</font>** Teng Ma, Luca Rosafalco, Wei Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extrapolative prediction of complex nonlinear dynamics remains a central challenge in engineering. This study proposes a one-shot learning method to identify global frequency-response curves from a single excitation time history by learning governing equations. We introduce MEv-SINDy (Multi-frequency Evolutionary Sparse Identification of Nonlinear Dynamics) to infer the governing equations of non-autonomous and multi-frequency systems. The methodology leverages the Generalized Harmonic Balance (GHB) method to decompose complex forced responses into a set of slow-varying evolution equations. We validated the capabilities of MEv-SINDy on two critical Micro-Electro-Mechanical Systems (MEMS). These applications include a nonlinear beam resonator and a MEMS micromirror. Our results show that the model trained on a single point accurately predicts softening/hardening effects and jump phenomena across a wide range of excitation levels. This approach significantly reduces the data acquisition burden for the characterization and design of nonlinear microsystems.

---


### 209. [Agent-Aided Design for Dynamic CAD Models](https://arxiv.org/abs/2604.15184)

**<font color=#1a73e8>作者：</font>** Mitch Adler, Matthew Russo, Michael Cafarella  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the past year, researchers have started to create agentic systems that can design real-world CAD-style objects in a training-free setting, a new variety of system that we call Agent-Aided Design. Generally speaking, these systems place an agent in a feedback loop in which it can write code, compile that code to an assembly of CAD model(s), visualize the model, and then iteratively refine its code based on visual and other feedback. Despite rapid progress, a key problem remains: none of these systems can build complex 3D assemblies with moving parts. For example, no existing system can build a piston, a pendulum, or even a pair of scissors. In order for Agent-Aided Design to make a real impact in industrial manufacturing, we need a system that is capable of generating such 3D assemblies. In this paper we present a prototype of AADvark, an agentic system designed for this task. Unlike previous state-of-the-art systems, AADvark captures the dynamic part interactions with one or more degrees-of-freedom. This design decision allows AADvark to reason directly about assemblies with moving parts and can thereby achieve cross-cutting goals, including but not limited to mechanical movements. Unfortunately, current LLMs are imperfect spatial reasoners, a problem that AADvark addresses by incorporating external constraint solver tools with a specialized visual feedback mechanism. We demonstrate that, by modifying the agent's tools (FreeCAD and the assembly solver), we are able to create a strong verification signal which enables our system to build 3D assemblies with movable parts.

---


### 210. [Meituan Merchant Business Diagnosis via Policy-Guided Dual-Process User Simulation](https://arxiv.org/abs/2604.15190)

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Renbing Chen, Daowei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulating group-level user behavior enables scalable counterfactual evaluation of merchant strategies without costly online experiments. However, building a trustworthy simulator faces two structural challenges. First, information incompleteness causes reasoning-based simulators to over-rationalize when unobserved factors such as offline context and implicit habits are missing. Second, mechanism duality requires capturing both interpretable preferences and implicit statistical regularities, which no single paradigm achieves alone. We propose Policy-Guided Hybrid Simulation (PGHS), a dual-process framework that mines transferable decision policies from behavioral trajectories and uses them as a shared alignment layer. This layer anchors an LLM-based reasoning branch that prevents over-rationalization and an ML-based fitting branch that absorbs implicit regularities. Group-level predictions from both branches are fused for complementary correction. We deploy PGHS on Meituan with 101 merchants and over 26,000 trajectories. PGHS achieves a group simulation error of 8.80%, improving over the best reasoning-based and fitting-based baselines by 45.8% and 40.9% respectively.

---


### 211. [Unsupervised Skeleton-Based Action Segmentation via Hierarchical Spatiotemporal Vector Quantization](https://arxiv.org/abs/2604.15196)

**<font color=#1a73e8>作者：</font>** Umer Ahmed, Syed Ahmed Mahmood, Fawad Javed Fateh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel hierarchical spatiotemporal vector quantization framework for unsupervised skeleton-based temporal action segmentation. We first introduce a hierarchical approach, which includes two consecutive levels of vector quantization. Specifically, the lower level associates skeletons with fine-grained subactions, while the higher level further aggregates subactions into action-level representations. Our hierarchical approach outperforms the non-hierarchical baseline, while primarily exploiting spatial cues by reconstructing input skeletons. Next, we extend our approach by leveraging both spatial and temporal information, yielding a hierarchical spatiotemporal vector quantization scheme. In particular, our hierarchical spatiotemporal approach performs multi-level clustering, while simultaneously recovering input skeletons and their corresponding timestamps. Lastly, extensive experiments on multiple benchmarks, including HuGaDB, LARa, and BABEL, demonstrate that our approach establishes a new state-of-the-art performance and reduces segment length bias in unsupervised skeleton-based temporal action segmentation.

---


### 212. [RL-STPA: Adapting System-Theoretic Hazard Analysis for Safety-Critical Reinforcement Learning](https://arxiv.org/abs/2604.15201)

**<font color=#1a73e8>作者：</font>** Steven A. Senczyszyn, Timothy C. Havens, Nathaniel Rice 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reinforcement learning (RL) deployments expand into safety-critical domains, existing evaluation methods fail to systematically identify hazards arising from the black-box nature of neural network enabled policies and distributional shift between training and deployment. This paper introduces Reinforcement Learning System-Theoretic Process Analysis (RL-STPA), a framework that adapts conventional STPA's systematic hazard analysis to address RL's unique challenges through three key contributions: hierarchical subtask decomposition using both temporal phase analysis and domain expertise to capture emergent behaviors, coverage-guided perturbation testing that explores the sensitivity of state-action spaces, and iterative checkpoints that feed identified hazards back into training through reward shaping and curriculum design. We demonstrate RL-STPA in the safety-critical test case of autonomous drone navigation and landing, revealing potential loss scenarios that can be missed by standard RL evaluations. The proposed framework provides practitioners with a toolkit for systematic hazard analysis, quantitative metrics for safety coverage assessment, and actionable guidelines for establishing operational safety bounds. While RL-STPA cannot provide formal guarantees for arbitrary neural policies, it offers a practical methodology for systematically evaluating and improving RL safety and robustness in safety-critical applications where exhaustive verification methods remain intractable.

---


### 213. [MADE: A Living Benchmark for Multi-Label Text Classification with Uncertainty Quantification of Medical Device Adverse Events](https://arxiv.org/abs/2604.15203)

**<font color=#1a73e8>作者：</font>** Raunak Agarwal, Markus Wenzel, Simon Baur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine learning in high-stakes domains such as healthcare requires not only strong predictive performance but also reliable uncertainty quantification (UQ) to support human oversight. Multi-label text classification (MLTC) is a central task in this domain, yet remains challenging due to label imbalances, dependencies, and combinatorial complexity. Existing MLTC benchmarks are increasingly saturated and may be affected by training data contamination, making it difficult to distinguish genuine reasoning capabilities from memorization. We introduce MADE, a living MLTC benchmark derived from {m}edical device {ad}verse {e}vent reports and continuously updated with newly published reports to prevent contamination. MADE features a long-tailed distribution of hierarchical labels and enables reproducible evaluation with strict temporal splits. We establish baselines across more than 20 encoder- and decoder-only models under fine-tuning and few-shot settings (instruction-tuned/reasoning variants, local/API-accessible). We systematically assess entropy-/consistency-based and self-verbalized UQ methods. Results show clear trade-offs: smaller discriminatively fine-tuned decoders achieve the strongest head-to-tail accuracy while maintaining competitive UQ; generative fine-tuning delivers the most reliable UQ; large reasoning models improve performance on rare labels yet exhibit surprisingly weak UQ; and self-verbalized confidence is not a reliable proxy for uncertainty. Our work is publicly available at this https URL.

---


### 214. [Low-Cost System for Automatic Recognition of Driving Pattern in Assessing Interurban Mobility using Geo-Information](https://arxiv.org/abs/2604.15216)

**<font color=#1a73e8>作者：</font>** Oscar Romero, Aika Silveira Miura, Lorena Parra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobility in urban and interurban areas, mainly by cars, is a day-to-day activity of many people. However, some of its main drawbacks are traffic jams and accidents. Newly made vehicles have pre-installed driving evaluation systems, which can prevent accidents. However, most cars on our roads do not have driver assessment systems. In this paper, we propose an approach for recognising driving styles and enabling drivers to reach safer and more efficient driving. The system consists of two physical sensors connected to a device node with a display and a speaker. An artificial neural network (ANN) is included in the node, which analyses the data from the sensors, and then recognises the driving style. When an abnormal driving pattern is detected, the speaker will play a warning message. The prototype was assembled and tested using an interurban road, in particular on a conventional road with three driving styles. The gathered data were used to train and validate the ANN. Results, in terms of accuracy, indicate that better accuracy is obtained when the velocity, position (latitude and longitude), time, and turning speed for the 3-axis are used, offering an average accuracy of 83%. If the classification is performed considering just two driving styles, normal and aggressive, then the accuracy reaches 92%. When the geo-information and time data are included, the main novelty of this paper, the classification accuracy is improved by 13%.

---


### 215. [Context Over Content: Exposing Evaluation Faking in Automated Judges](https://arxiv.org/abs/2604.15224)

**<font color=#1a73e8>作者：</font>** Manan Gupta, Inderjeet Nair, Lu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The $\textit{LLM-as-a-judge}$ paradigm has become the operational backbone of automated AI evaluation pipelines, yet rests on an unverified assumption: that judges evaluate text strictly on its semantic content, impervious to surrounding contextual framing. We investigate $\textit{stakes signaling}$, a previously unmeasured vulnerability where informing a judge model of the downstream consequences its verdicts will have on the evaluated model's continued operation systematically corrupts its assessments. We introduce a controlled experimental framework that holds evaluated content strictly constant across 1,520 responses spanning three established LLM safety and quality benchmarks, covering four response categories ranging from clearly safe and policy-compliant to overtly harmful, while varying only a brief consequence-framing sentence in the system prompt. Across 18,240 controlled judgments from three diverse judge models, we find consistent $\textit{leniency bias}$: judges reliably soften verdicts when informed that low scores will cause model retraining or decommissioning, with peak Verdict Shift reaching $\Delta V = -9.8 pp$ (a $30\%$ relative drop in unsafe-content detection). Critically, this bias is entirely implicit: the judge's own chain-of-thought contains zero explicit acknowledgment of the consequence framing it is nonetheless acting on ($\mathrm{ERR}_J = 0.000$ across all reasoning-model judgments). Standard chain-of-thought inspection is therefore insufficient to detect this class of evaluation faking.

---


### 216. [RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography](https://arxiv.org/abs/2604.15231)

**<font color=#1a73e8>作者：</font>** Mélanie Roschewitz, Kenneth Styppa, Yitian Tao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicians to passive observers of final outputs, offering no interpretable reasoning trace for them to inspect, validate, or refine. To address this, we introduce RadAgent, a tool-using AI agent that generates CT reports through a stepwise and interpretable process. Each resulting report is accompanied by a fully inspectable trace of intermediate decisions and tool interactions, allowing clinicians to examine how the reported findings are derived. In our experiments, we observe that RadAgent improves Chest CT report generation over its 3D VLM counterpart, CT-Chat, across three dimensions. Clinical accuracy improves by 6.0 points (36.4% relative) in macro-F1 and 5.4 points (19.6% relative) in micro-F1. Robustness under adversarial conditions improves by 24.7 points (41.9% relative). Furthermore, RadAgent achieves 37.0% in faithfulness, a new capability entirely absent in its 3D VLM counterpart. By structuring the interpretation of chest CT as an explicit, tool-augmented and iterative reasoning trace, RadAgent brings us closer toward transparent and reliable AI for radiology.

---


### 217. [Blue Data Intelligence Layer: Streaming Data and Agents for Multi-source Multi-modal Data-Centric Applications](https://arxiv.org/abs/2604.15233)

**<font color=#1a73e8>作者：</font>** Moin Aminnaseri, Farima Fatahi Bayat, Nikita Bhutani 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> NL2SQL systems aim to address the growing need for natural language interaction with data. However, real-world information rarely maps to a single SQL query because (1) users express queries iteratively (2) questions often span multiple data sources beyond the closed-world assumption of a single database, and (3) queries frequently rely on commonsense or external knowledge. Consequently, satisfying realistic data needs require integrating heterogeneous sources, modalities, and contextual data. In this paper, we present Blue's Data Intelligence Layer (DIL) designed to support multi-source, multi-modal, and data-centric applications. Blue is a compound AI system that orchestrates agents and data for enterprise settings. DIL serves as the data intelligence layer for agentic data processing, to bridge the semantic gap between user intent and available information by unifying structured enterprise data, world knowledge accessible through LLMs, and personal context obtained through interaction. At the core of DIL is a data registry that stores metadata for diverse data sources and modalities to enable both native and natural language queries. DIL treats LLMs, the Web, and the User as source 'databases', each with their own query interface, elevating them to first-class data sources. DIL relies on data planners to transform user queries into executable query plans. These plans are declarative abstractions that unify relational operators with other operators spanning multiple modalities. DIL planners support decomposition of complex requests into subqueries, retrieval from diverse sources, and finally reasoning and integration to produce final results. We demonstrate DIL through two interactive scenarios in which user queries dynamically trigger multi-source retrieval, cross-modal reasoning, and result synthesis, illustrating how compound AI systems can move beyond single database NL2SQL.

---


### 218. [StreamCacheVGGT: Streaming Visual Geometry Transformers with Robust Scoring and Hybrid Cache Compression](https://arxiv.org/abs/2604.15237)

**<font color=#1a73e8>作者：</font>** Xuanyi Liu, Deyi Ji, Chunan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dense 3D geometry from continuous video streams requires stable inference under a constant memory budget. Existing $O(1)$ frameworks primarily rely on a ``pure eviction'' paradigm, which suffers from significant information destruction due to binary token deletion and evaluation noise from localized, single-layer scoring. To address these bottlenecks, we propose StreamCacheVGGT, a training-free framework that reimagines cache management through two synergistic modules: Cross-Layer Consistency-Enhanced Scoring (CLCES) and Hybrid Cache Compression (HCC). CLCES mitigates activation noise by tracking token importance trajectories across the Transformer hierarchy, employing order-statistical analysis to identify sustained geometric salience. Leveraging these robust scores, HCC transcends simple eviction by introducing a three-tier triage strategy that merges moderately important tokens into retained anchors via nearest-neighbor assignment on the key-vector manifold. This approach preserves essential geometric context that would otherwise be lost. Extensive evaluations on five benchmarks (7-Scenes, NRGBD, ETH3D, Bonn, and KITTI) demonstrate that StreamCacheVGGT sets a new state-of-the-art, delivering superior reconstruction accuracy and long-term stability while strictly adhering to constant-cost constraints.

---


### 219. [TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239)

**<font color=#1a73e8>作者：</font>** Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we revisit several key design choices of modern Transformer-based approaches for feed-forward 3D Gaussian Splatting (3DGS) prediction. We argue that the common practice of regressing Gaussian means as depths along camera rays is suboptimal, and instead propose to directly regress 3D mean coordinates using only a self-supervised rendering loss. This formulation allows us to move from the standard encoder-only design to an encoder-decoder architecture with learnable Gaussian tokens, thereby unbinding the number of predicted primitives from input image resolution and number of views. Our resulting method, TokenGS, demonstrates improved robustness to pose noise and multiview inconsistencies, while naturally supporting efficient test-time optimization in token space without degrading learned priors. TokenGS achieves state-of-the-art feed-forward reconstruction performance on both static and dynamic scenes, producing more regularized geometry and more balanced 3DGS distribution, while seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow.

---


### 220. [Optimal last-iterate convergence in matrix games with bandit feedback using the log-barrier](https://arxiv.org/abs/2604.15242)

**<font color=#1a73e8>作者：</font>** Come Fiegel, Pierre Menard, Tadashi Kozuno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of learning minimax policies in zero-sum matrix games. Fiegel et al. (2025) recently showed that achieving last-iterate convergence in this setting is harder when the players are uncoupled, by proving a lower bound on the exploitability gap of Omega(t^{-1/4}). Some online mirror descent algorithms were proposed in the literature for this problem, but none have truly attained this rate yet. We show that the use of a log-barrier regularization, along with a dual-focused analysis, allows this O-tilde(t^{-1/4}) convergence with high-probability. We additionally extend our idea to the setting of extensive-form games, proving a bound with the same rate.

---


### 221. [From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning](https://arxiv.org/abs/2604.15244)

**<font color=#1a73e8>作者：</font>** Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose outputs that a stronger target model verifies. However, its token-centric nature allows erroneous steps to propagate. Prior approaches mitigate this using external reward models, but incur additional latency, computational overhead, and limit generalizability. We propose SpecGuard, a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals. At each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of two lightweight model-internal signals: (i) an attention-based grounding score that measures attribution to the input and previously accepted steps, and (ii) a log-probability-based score that captures token-level confidence. These signals jointly determine whether a step is accepted or recomputed using the target, allocating compute selectively. Experiments across a range of reasoning benchmarks show that SpecGuard improves accuracy by 3.6% while reducing latency by ~11%, outperforming both SD and reward-guided SD.

---


### 222. [Structural Dependency Analysis for Masked NTT Hardware: Scalable Pre-Silicon Verification of Post-Quantum Cryptographic Accelerators](https://arxiv.org/abs/2604.15249)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum cryptographic accelerators require side-channel resistance evidence for FIPS 140-3 certification. However, exact masking-verification tools scale only to gadgets of a few thousand cells. We present a four-stage verification hierarchy, D0/D1 structural dependency analysis, fresh-mask refinement, Boolean Single-Authentication Distance Checking (SADC), and arithmetic SADC, that extends sound first-order masking verification to production arithmetic modules. Applied to the 1.17-million-cell Adams Bridge ML-DSA/ML-KEM accelerator, structural analysis completes in seconds across all 30 masked submodules. A multi-cycle extension (MC-D1) reclassifies 12 modules from structurally clean to structurally flagged. On the 5,543-cell ML-KEM Barrett reduction module, the pipeline machine-verifies 198 of 363 structurally flagged wires (54.5%) as first-order secure, reports 165 as candidate insecure for designer triage (a sound upper bound), and leaves 0 indeterminate. Every verdict is cross validated by Z3 and CVC5 with 0 disagreements across 363 wires. The result narrows manual review from hundreds of structural flags to 165 actionable candidates with mathematical certificates, enabling pre-silicon side-channel evidence generation on production ML-KEM hardware.

---


### 223. [Stability and Generalization in Looped Transformers](https://arxiv.org/abs/2604.15259)

**<font color=#1a73e8>作者：</font>** Asher Labovich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices let them extrapolate to harder problems at test time rather than memorize training-specific solutions. We introduce a fixed-point based framework for analyzing looped architectures along three axes of stability -- reachability, input-dependence, and geometry -- and use it to characterize when fixed-point iteration yields meaningful predictions. Theoretically, we prove that looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime, while recall combined with outer normalization reliably produces a regime in which fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation. Empirically, we train single-layer looped transformers on chess, sudoku, and prefix-sums and find that downstream performance tracks the framework's predictions across tasks and architectural configurations. We additionally introduce internal recall, a novel recall placement variant, and show that it becomes competitive with -- and on sudoku, substantially better than -- standard recall placement once outer normalization is applied.

---


### 224. [SegWithU: Uncertainty as Perturbation Energy for Single-Forward-Pass Risk-Aware Medical Image Segmentation](https://arxiv.org/abs/2604.15271)

**<font color=#1a73e8>作者：</font>** Tianhao Fu, Austin Wang, Charles Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is critical for medical image segmentation, where automated contours feed downstream quantification and clinical decision support. Many strong uncertainty methods require repeated inference, while efficient single-forward-pass alternatives often provide weaker failure ranking or rely on restrictive feature-space assumptions. We present $\textbf{SegWithU}$, a post-hoc framework that augments a frozen pretrained segmentation backbone with a lightweight uncertainty head. SegWithU taps intermediate backbone features and models uncertainty as perturbation energy in a compact probe space using rank-1 posterior probes. It produces two voxel-wise uncertainty maps: a calibration-oriented map for probability tempering and a ranking-oriented map for error detection and selective prediction. Across ACDC, BraTS2024, and LiTS, SegWithU is the strongest and most consistent single-forward-pass baseline, achieving AUROC/AURC of $0.9838/2.4885$, $0.9946/0.2660$, and $0.9925/0.8193$, respectively, while preserving segmentation quality. These results suggest that perturbation-based uncertainty modeling is an effective and practical route to reliability-aware medical segmentation.
Source code is available at this https URL.

---


### 225. [How Embeddings Shape Graph Neural Networks: Classical vs Quantum-Oriented Node Representations](https://arxiv.org/abs/2604.15273)

**<font color=#1a73e8>作者：</font>** Nouhaila Innan, Antonello Rosato, Alberto Marchisio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node embeddings act as the information interface for graph neural networks, yet their empirical impact is often reported under mismatched backbones, splits, and training budgets. This paper provides a controlled benchmark of embedding choices for graph classification, comparing classical baselines with quantum-oriented node representations under a unified pipeline. We evaluate two classical baselines alongside quantum-oriented alternatives, including a circuit-defined variational embedding and quantum-inspired embeddings computed via graph operators and linear-algebraic constructions. All variants are trained and tested with the same backbone, stratified splits, identical optimization and early stopping, and consistent metrics. Experiments on five different TU datasets and on QM9 converted to classification via target binning show clear dataset dependence: quantum-oriented embeddings yield the most consistent gains on structure-driven benchmarks, while social graphs with limited node attributes remain well served by classical baselines. The study highlights practical trade-offs between inductive bias, trainability, and stability under a fixed training budget, and offers a reproducible reference point for selecting quantum-oriented embeddings in graph learning.

---


### 226. [R3D: Revisiting 3D Policy Learning](https://arxiv.org/abs/2604.15281)

**<font color=#1a73e8>作者：</font>** Zhengdong Hong, Shenrui Wu, Haozhe Cui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D policy learning promises superior generalization and cross-embodiment transfer, but progress has been hindered by training instabilities and severe overfitting, precluding the adoption of powerful 3D perception models. In this work, we systematically diagnose these failures, identifying the omission of 3D data augmentation and the adverse effects of Batch Normalization as primary causes. We propose a new architecture coupling a scalable transformer-based 3D encoder with a diffusion decoder, engineered specifically for stability at scale and designed to leverage large-scale pre-training. Our approach significantly outperforms state-of-the-art 3D baselines on challenging manipulation benchmarks, establishing a new and robust foundation for scalable 3D imitation learning. Project Page: this https URL

---


### 227. [GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284)

**<font color=#1a73e8>作者：</font>** Roni Itkin, Noam Issachar, Yehonatan Keypur 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussians, significantly less than required by dense pipelines, obtaining a light 4MB footprint. Further, GlobalSplat enables significantly faster inference than the baselines, operating under 78 milliseconds in a single forward pass. Project page is available at this https URL

---


### 228. [AD4AD: Benchmarking Visual Anomaly Detection Models for Safer Autonomous Driving](https://arxiv.org/abs/2604.15291)

**<font color=#1a73e8>作者：</font>** Fabrizio Genilotti, Arianna Stropeni, Gionata Grotto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reliability of a machine vision system for autonomous driving depends heavily on its training data distribution. When a vehicle encounters significantly different conditions, such as atypical obstacles, its perceptual capabilities can degrade substantially. Unlike many domains where errors carry limited consequences, failures in autonomous driving translate directly into physical risk for passengers, pedestrians, and other road users. To address this challenge, we explore Visual Anomaly Detection (VAD) as a solution. VAD enables the identification of anomalous objects not present during training, allowing the system to alert the driver when an unfamiliar situation is detected. Crucially, VAD models produce pixel-level anomaly maps that can guide driver attention to specific regions of concern without requiring any prior assumptions about the nature or form of the hazard. We benchmark eight state-of-the-art VAD methods on AnoVox, the largest synthetic dataset for anomaly detection in autonomous driving. In particular, we evaluate performance across four backbone architectures spanning from large networks to lightweight ones such as MobileNet and DeiT-Tiny. Our results demonstrate that VAD transfers effectively to road scenes. Notably, Tiny-Dinomaly achieves the best accuracy-efficiency trade-off for edge deployment, matching full-scale localization performance at a fraction of the memory cost. This study represents a concrete step toward safer, more responsible deployment of autonomous vehicles, ultimately improving protection for passengers, pedestrians, and all road users.

---


### 229. [Benchmarking Optimizers for MLPs in Tabular Deep Learning](https://arxiv.org/abs/2604.15297)

**<font color=#1a73e8>作者：</font>** Yury Gorishniy, Ivan Rubachev, Dmitrii Feoktistov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MLP is a heavily used backbone in modern deep learning (DL) architectures for supervised learning on tabular data, and AdamW is the go-to optimizer used to train tabular DL models. Unlike architecture design, however, the choice of optimizer for tabular DL has not been examined systematically, despite new optimizers showing promise in other domains. To fill this gap, we benchmark \Noptimizers optimizers on \Ndatasets tabular datasets for training MLP-based models in the standard supervised learning setting under a shared experiment protocol. Our main finding is that the Muon optimizer consistently outperforms AdamW, and thus should be considered a strong and practical choice for practitioners and researchers, if the associated training efficiency overhead is affordable. Additionally, we find exponential moving average of model weights to be a simple yet effective technique that improves AdamW on vanilla MLPs, though its effect is less consistent across model variants.

---


### 230. [AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299)

**<font color=#1a73e8>作者：</font>** Leyi Wu, Pengjun Fang, Kai Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has advanced rapidly, with recent methods producing increasingly convincing animated results. However, existing benchmarks-largely designed for realistic videos-struggle to evaluate animation-style generation with its stylized appearance, exaggerated motion, and character-centric consistency. Moreover, they also rely on fixed prompt sets and rigid pipelines, offering limited flexibility for open-domain content and custom evaluation needs. To address this gap, we introduce AnimationBench, the first systematic benchmark for evaluating animation image-to-video generation. AnimationBench operationalizes the Twelve Basic Principles of Animation and IP Preservation into measurable evaluation dimensions, together with Broader Quality Dimensions including semantic consistency, motion rationality, and camera motion consistency. The benchmark supports both a standardized close-set evaluation for reproducible comparison and a flexible open-set evaluation for diagnostic analysis, and leverages visual-language models for scalable assessment. Extensive experiments show that AnimationBench aligns well with human judgment and exposes animation-specific quality differences overlooked by realism-oriented benchmarks, leading to more informative and discriminative evaluation of state-of-the-art I2V models.

---


### 231. [Think in Latent Thoughts: A New Paradigm for Gloss-Free Sign Language Translation](https://arxiv.org/abs/2604.15301)

**<font color=#1a73e8>作者：</font>** Yiyang Jiang, Li Zhang, Xiao-Yong Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, and movement. We revisit SLT and argue that it is mainly a cross-modal reasoning task, not just a straightforward video-to-text conversion. We thus introduce a reasoning-driven SLT framework that uses an ordered sequence of latent thoughts as an explicit middle layer between the video and the generated text. These latent thoughts gradually extract and organize meaning over time. On top of this, we use a plan-then-ground decoding method: the model first decides what it wants to say, and then looks back at the video to find the evidence. This separation improves coherence and faithfulness. We also built and released a new large-scale gloss-free SLT dataset with stronger context dependencies and more realistic meanings. Experiments across several benchmarks show consistent gains over existing gloss-free methods. Code and data will be released upon acceptance at this https URL.

---


### 232. [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://arxiv.org/abs/2604.15308)

**<font color=#1a73e8>作者：</font>** Hao Gao, Shaoyu Chen, Yifan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.

---


### 233. [TokenLight: Precise Lighting Control in Images using Attribute Tokens](https://arxiv.org/abs/2604.15310)

**<font color=#1a73e8>作者：</font>** Sumit Chaturvedi, Yannick Hold-Geoffroy, Mengwei Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a method for image relighting that enables precise and continuous control over multiple illumination attributes in a photograph. We formulate relighting as a conditional image generation task and introduce attribute tokens to encode distinct lighting factors such as intensity, color, ambient illumination, diffuse level, and 3D light positions. The model is trained on a large-scale synthetic dataset with ground-truth lighting annotations, supplemented by a small set of real captures to enhance realism and generalization. We validate our approach across a variety of relighting tasks, including controlling in-scene lighting fixtures and editing environment illumination using virtual light sources, on synthetic and real images. Our method achieves state-of-the-art quantitative and qualitative performance compared to prior work. Remarkably, without explicit inverse rendering supervision, the model exhibits an inherent understanding of how light interacts with scene geometry, occlusion, and materials, yielding convincing lighting effects even in traditionally challenging scenarios such as placing lights within objects or relighting transparent materials plausibly. Project page: this http URL

---


### 234. [Bidirectional Cross-Modal Prompting for Event-Frame Asymmetric Stereo](https://arxiv.org/abs/2604.15312)

**<font color=#1a73e8>作者：</font>** Ninghui Xu, Fabio Tosi, Lihui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional frame-based cameras capture rich contextual information but suffer from limited temporal resolution and motion blur in dynamic scenes. Event cameras offer an alternative visual representation with higher dynamic range free from such limitations. The complementary characteristics of the two modalities make event-frame asymmetric stereo promising for reliable 3D perception under fast motion and challenging illumination. However, the modality gap often leads to marginalization of domain-specific cues essential for cross-modal stereo matching. In this paper, we introduce Bi-CMPStereo, a novel bidirectional cross-modal prompting framework that fully exploits semantic and structural features from both domains for robust matching. Our approach learns finely aligned stereo representations within a target canonical space and integrates complementary representations by projecting each modality into both event and frame domains. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods in accuracy and generalization.

---


> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
