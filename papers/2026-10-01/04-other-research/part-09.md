# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-447**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-447**

---

### 401. [Pattern Formation in Transformers](https://arxiv.org/abs/2609.37921)

**<font color=#1a73e8>作者：</font>** Erkan Turan, Gaspard Abel, Maks Ovsjanikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What are the inductive biases of a Transformer architecture? Existing theory on how the forward pass shapes representations either considers whether Transformers escape from rank collapse or demonstrates that self-attention drives tokens toward cluster patterns. The latter view arises from an elegant dynamical systems perspective, but relies on simplified architectural assumptions, and does not explain the rich structures observed in practice. This leaves a major open question: when a full Transformer escapes rank collapse, how does it structure token representations? Using pattern-formation theory, we show that the dynamical view of Transformers can account for Positional Encoding, Multi-Head Attention, and Output-Value geometry. We demonstrate that a full Transformer architecture imposes an inductive prior by selectively amplifying a rich set of previously unreported patterns, including traveling or rotating waves among others. We characterize the role of each architectural component in controlling which pattern is amplified, which ones stabilize, compete, or coexist. Finally, we show that these structures can act as a controllable dynamical prior that facilitates learning. By choosing both task-aligned positional encoding and weight initialization, we demonstrate improved data efficiency and accelerated optimization on controlled sequence tasks and with ConViT on CIFAR-10.

---


### 402. [EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory](https://arxiv.org/abs/2609.37923)

**<font color=#1a73e8>作者：</font>** Ziyun Zeng, Hang Hua, Shaden Alshammari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agents can learn from past executions, but enabling different agents to reuse and build on one another's experience remains challenging. We introduce EpiCon, a shared multimodal memory framework for agent collective learning without updating host model parameters. EpiCon links question-level memory evolution to a persistent experience bank through two independently trained 2B models: a memory controller and a tree self-organizer. The controller jointly refines textual guidance and visual evidence across attempts and selectively includes visual memory. The self-organizer consolidates lessons hierarchically and retrieves experience and rules for new problems. We evaluate EpiCon on eleven benchmarks spanning four multimodal task domains, using two harnesses and multiple backbones. A frozen bank improves other systems even with a single solving attempt. A second harness raises the original system's macro-average score by 2.6 points across eleven benchmarks. Across four host configurations, EpiCon improves macro-average scores by 1.7 to 4.9 points over No Memory and reduces memory-operation time by 67\% to 74\% relative to backbone-sized memory models.

---


### 403. [Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation](https://arxiv.org/abs/2609.37925)

**<font color=#1a73e8>作者：</font>** Chenjian Gao, Zhihao Hu, Jianqi Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion enables low-latency, streamable video generation, but prediction errors often accumulate over long rollouts. Training the generator on its own rollouts exposes it to these imperfect histories. However, existing video-level distribution matching distillation (DMD) scores the whole rollout jointly. Because a chunk is evaluated together with its past and future, its correction can favor matching artifacts in the surrounding context merely to preserve temporal consistency. To provide a clearer visual-quality signal, we introduce Rollout-Marginal Distillation (RMD). RMD retains the generated history for AR prediction but scores each chunk independently against a chunk teacher, ensuring its quality correction is not compromised by an imperfect temporal context. To compensate for the lack of temporal context in independent chunk scoring, RMD subsequently applies video-level DMD to restore temporal coherence. Extensive experiments demonstrate that RMD maintains high visual quality far beyond its training horizon and outperforms video-level DMD baselines. Code and video results are available at this https URL

---


### 404. [Learning When to Update: A Near-Optimal Timing Bandit Approach](https://arxiv.org/abs/2609.37932)

**<font color=#1a73e8>作者：</font>** Qiulin Lin, Junyan Su, Liyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Systems operating in dynamic environments require timely updates to sustain performance. For resource-intensive systems such as machine learning models and digital twins, strategically timing updates is essential. Updating too frequently wastes resources, while updating too infrequently leads to costly performance degradation. The problem is particularly challenging when the system's degradation pattern is unknown a priori, as is common in new operating environments. We formalize this challenge as a novel \emph{timing bandit} problem, where each arm represents a candidate update interval with a fixed update cost and an unknown, stochastic degradation cost. Three structural properties distinguish this setting from standard multi-armed bandits: selecting an interval commits the learner to multiple time slots before the next update; arm costs are composed of per-step degradation costs and a fixed update cost; and selecting a longer interval naturally reveals degradation at every intermediate step, providing consecutive feedback relevant to shorter intervals. By exploiting these structures, we develop Balanced Consecutive Arm Elimination (BCAE). BCAE achieves $\tilde{O}(\sqrt{T})$ regret, improving upon the $\tilde{\Omega}(K\sqrt{T})$ regret of standard bandit algorithms in this setting, where $K$ is the number of candidate update intervals. We further propose an Optimism-Enhanced variant (OE-BCAE) that integrates lower-confidence-bound principles to improve empirical adaptivity while preserving the same regret order. Moreover, the regret bound achieved by our algorithms matches the theoretical lower bound up to logarithmic factors. Simulation results demonstrate that our algorithms achieve low regret and remain stable as both the number of arms and the update cost vary.

---


### 405. [GRFBrain: Graph-Structured Rectified Flows for EEG Dynamic Modeling](https://arxiv.org/abs/2609.37934)

**<font color=#1a73e8>作者：</font>** Haohui Jia, Zheng Chen, Jathurshan Pradeepkumar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting time-varying functional connectivity from electroencephalography (EEG) requires modeling both history-dependent trends and structured variability across channels. Conditional flow matching provides a framework for distributional forecasting, yet it remains unclear whether graph-informed source distributions offer practical advantages over isotropic noise and strong deterministic predictors. We introduce a graph-structured residual flow framework that separates conditional mean prediction from stochastic residual transport. A history-only predictor estimates the future connectivity graph, while a graph Gaussian source encodes dependencies derived from past connectivity through a Laplacian-based covariance. A conditional velocity field transports source samples to future graph residuals, with transport time explicitly distinguished from physical EEG time. Our study identifies the conditions and controls needed to distinguish useful residual transport from improvements attributable to deterministic prediction, learned representations, and sampling effects.

---


### 406. [Look Closer: Patch-wise Supervision for AI-Generated Image Detection](https://arxiv.org/abs/2609.37937)

**<font color=#1a73e8>作者：</font>** Zhida Zhang, Tao Wu, Siyu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How much of an image does a detector need to see? Small RGB regions can retain useful evidence of image synthesis even when they reveal little of the full scene. Motivated by single-patch detection, we study patch-wise supervision: a shared backbone classifies explicit crops, each crop receives its own loss, and patch probabilities are averaged only at inference. The procedure requires neither handcrafted residual filtering nor a learned image-level fusion module. Experiments span single-patch selection, multiple generator collections, and four CNN and Transformer backbones. On GenImage, the reported patch-wise variants improve average accuracy over their whole-image counterparts across all four backbones. Comparisons of supervision granularity, source resolution, crop size, and inference coverage further characterize the approach, while post-processing tests and difficult-image evaluation reveal its limitations. The historical experiments include evaluation-based model selection, so their scores are not presented as a uniformly selected leaderboard comparison. Overall, the study identifies explicit local input and patch-level supervision as a simple, useful combination for investigating generalizable AI-generated image detection.

---


### 407. [An Efficient Machine Learning Approach for Degradation Forecasting in AEM Water Electrolysis](https://arxiv.org/abs/2609.37941)

**<font color=#1a73e8>作者：</font>** Marco Veneriano, Ani Gjergji, Sebastiano Bellani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study provides a data-driven analysis of a novel dataset of single-cell Anion Exchange Membrane water electrolyzers (AEMWE), operated under constant current load across multiple heterogeneous experimental campaigns. We train and evaluate a range of machine learning models with different complexity, including linear baselines, LSTMs and CNNs, to perform medium-term forecasting of the cell voltage degradation curve. The models are assessed within a rigorous training and evaluation framework specifically designed for heterogeneous industrial data.

---


### 408. [Scene-Consistent Illumination Transfer for Inserted Advertising Graphics](https://arxiv.org/abs/2609.37951)

**<font color=#1a73e8>作者：</font>** Rameshwar Mishra, Bishshoy Das, A. V. Subramanyam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Replacing a visible advertisement in a broadcast frame is geometrically straightforward but photometrically delicate. A pasted graphic can have the correct perspective and still appear detached when its brightness, shading, or shadow disagrees with the surface beneath it. This paper presents Ad-Relight, an inference-only procedure for transferring scene illumination to a supplied advertising graphic without collecting a banner-specific training set. The procedure first separates slowly varying shade from graphic structure, then probes a pretrained diffusion relighter with two nearly identical backgrounds to isolate the contribution of the target region. A final pass combines this residual with a smoothed luminance field and a soft attenuation mask. Across 560 generated placements, the approach improves structural similarity, perceptual distance, and illumination agreement over geometric compositing and direct relighting baselines. Human judgments and an automated preference study show the clearest gains on floor-mounted graphics with nonuniform lighting. The current study is image based; temporal stabilization remains an open extension.

---


### 409. [Towards the Threshold: A Fall-Risk Anchored Pareto Framework for Virtual Reality Gait Feedback Selection for Individuals with Multiple Sclerosis](https://arxiv.org/abs/2609.37952)

**<font color=#1a73e8>作者：</font>** Nafisa Anjum, John Quarles, M. Rasel Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reduced walking speed in people with multiple sclerosis (MS) is associated with an increased risk of falls. However, virtual reality (VR)-based rehabilitation studies often emphasize performance improvements without considering the cognitive and physical effort required to achieve them. This study introduces a threshold-anchored efficiency framework that jointly evaluates gait performance and overall effort. A normative walking-velocity target of \(T=1.29\) m/s was derived from the mean walking speed of non-fallers in an independent MS gait dataset and used as a clinically motivated reference point. Thirty-four adults with MS were evaluated across eight VR feedback conditions spanning unimodal, bimodal, and multimodal feedback. For each condition, we quantified the proportion of the velocity gap to the target that was closed and the associated cognitive and physical burden. Pareto efficiency analysis identified five non-dominated conditions: Static Visual, Spatial Auditory, Auditory+Visual, Auditory+Vibrotactile, and Multimodal, whereas Spatial Vibrotactile and Vibrotactile+Visual were dominated. Spatial Auditory showed a favorable performance-effort trade-off, closing 72.7% of the velocity gap while maintaining below-average burden. Multimodal feedback achieved the greatest gap closure (95.6%) but also imposed the highest burden. These findings demonstrate that greater gait improvement does not necessarily correspond to greater rehabilitation efficiency and provide a quantitative framework for comparing VR feedback strategies according to both performance gains and participant burden.

---


### 410. [Topological Coherence for Self-evolving Multi-agent Systems](https://arxiv.org/abs/2609.37953)

**<font color=#1a73e8>作者：</font>** Sen Zhao, Ruiqi Kong, Zuyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex tasks inherently couple workflow structure, agent responsibility, collaboration, and memory access: task regions delimit responsibility and tool scope, cross-region dependencies give rise to handoffs, and ownership boundaries delimit private and selectively shared memory. Existing methods can jointly optimize agent and communication structures, yet such optimization does not by itself require responsibility, handoff, and memory boundaries to remain consistent with task dependencies. We term this requirement topological coherence. We introduce TOCOMAS, a Topology-Coherent Multi-Agent System. TOCOMAS grounds a task graph in tool interfaces, organizes compatible task nodes into reusable responsibility domains, and derives dependency-induced and profile-conditioned collaboration together with boundary-regulated memory visibility. During online self-evolution, TOCOMAS proposes coupled changes to agent, collaboration, and memory policies, retaining for subsequent tasks only candidates that satisfy structural constraints and improve evaluated reward. Across BBEH, WorkBench, SWE-Bench-Verified, and CoMemBench, TOCOMAS improves task success over baselines across backbones. CoMemBench also shows gains over the self-evolving baseline in verified progress, handoffs, and memory isolation.

---


### 411. [Kolmogorov-Arnold Classifier Systems as Universal Approximators](https://arxiv.org/abs/2609.37958)

**<font color=#1a73e8>作者：</font>** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the input dimension $n$ grows, rule-based machine learning, such as Learning Classifier Systems (LCSs), faces a fundamental scalability bottleneck for function approximation: both rule count and parameter count grow exponentially with $n$. Traditional LCSs partition the $n$-dimensional input space directly, requiring $\mathcal{O}(m^n)$ rules for adequate coverage, where $m$ is the per-variable resolution. This article breaks from this paradigm by reorganizing rules dimension-wise, guided by the Kolmogorov-Arnold representation theorem: any continuous $n$-dimensional function can be expressed as a finite superposition of one-dimensional functions. The proposed Kolmogorov-Arnold Classifier System (KACS) decomposes the target function into one-dimensional subproblems and assigns a dedicated ruleset to each, reducing the worst-case rule count from $\mathcal{O}(m^n)$ to $\mathcal{O}(mn^2)$ and replacing $n$-dimensional local models with one-dimensional models requiring only two parameters per rule, independent of $n$. We also provide the first constructive proof that an LCS, namely KACS, is a universal approximator for continuous functions on compact domains. Evaluated against a direct $n$-dimensional input space partitioning approach under otherwise identical conditions, KACS achieves competitive accuracy in many settings while using only 2\% to 40\% of the parameters. Our implementation is available at this https URL.

---


### 412. [A Task-Driven Framework for Multiscale Ocean Flow Dynamics through Integrated Simulation and Visualization](https://arxiv.org/abs/2609.37964)

**<font color=#1a73e8>作者：</font>** James Kress, Jithendra Nadimpalli, Shehzad Afzal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Internal waves are large-amplitude gravity waves that occur below the ocean surface and propagate along interfaces separating water layers of different densities. Understanding their generation, propagation, and evolution is essential, as these waves play a vital role in the ocean system by contributing to nutrient transport, biological productivity, and the transfer of energy across the ocean and continental shelf. Domain scientists use high-resolution numerical ocean models, to study internal-wave dynamics and associated coastal and nearshore processes on hybrid computational grids. These models generate large-scale, three-dimensional spatiotemporal datasets that capture internal wave flow behavior and interactions with multiple ocean variables. These datasets are generally analyzed using command-line tools with limited interactivity. To address these challenges, we in collaboration with domain scientists designed a task-driven visualization methodology for analyzing multiscale, multivariate flow data on hybrid grids. The framework incorporates a hybrid-grid volumetric reconstruction method, enabling continuous 3D analysis and a coordinated multi-view design that supports interactive exploration of complex flow structures. An insight-based evaluation with domain experts demonstrates that the system enables the identification of previously difficult-to-observe phenomena, including transverse wave propagation, energy transport pathways, and shoaling-driven mixing. Beyond the application domain, our contributions provide generalizable techniques and design principles for visual analysis of multiscale, multivariate flow data on irregular grids.

---


### 413. [SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video](https://arxiv.org/abs/2609.37969)

**<font color=#1a73e8>作者：</font>** Haozhe Liu, Tian Ye, Shuchen Xue 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution video generation is expensive, as its cost grows rapidly with the number of spatiotemporal tokens. A practical alternative first generates a lower-resolution video and then applies a refiner, but conventional multi-step refinement introduces a second sampling bottleneck. We present SoL-Refiner, a one-step video refiner that transforms low-resolution model outputs into 4K videos with a single denoising step. Our three-stage recipe combines high-resolution continual training, reinforcement learning (RL) post-training, and a final one-step distillation. We introduce Refiner-Bench, a video refinement benchmark constructed from the outputs of different video generators, and use a shared-input protocol to compare refiners at approximately 2K output resolution. At 2K, the one-step SoL-Refiner outperforms all external refiners on the VBench and UniPercept averages, while at $3840\!\times\!2176$ it improves both metrics over the three-step LTX-2.3 Refiner. With the complete acceleration stack, SoL-Refiner achieves an $8.91\times$ speedup in refinement latency over the same baseline in our 2K latency setting.

---


### 414. [Dagger: Decoupling-based Model Stealing Attack against Graph Neural Networks](https://arxiv.org/abs/2609.37972)

**<font color=#1a73e8>作者：</font>** Ying Song, Xiaowei Jia, Balaji Palanisamy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Graph Neural Networks (GNNs) are widely deployed as Machine Learning-as-a-Service (MLaaS) APIs, model stealing attacks have emerged as a critical security threat. By querying a victim model's black-box API, an adversary can construct a functionally equivalent surrogate model, compromising proprietary intellectual property and downstream security. Existing GNN stealing attacks, however, rely on overly permissive assumptions, such as soft-label outputs, large query budgets, full-graph query access, and prior knowledge of victim backbones that rarely hold in real-world deployments. In this work, we formalize a strictly constrained black-box, hard-label and backbone-agnostic threat model for GNN stealing attacks under a tight query budget. Given these realistic restrictions, we identify four fundamental challenges: sparse local structures and isolated nodes that degrade victim label quality, insufficient supervision signals, systematic imbalance with incomplete class coverage, and backbone mismatch. To address these interlocking barriers, we propose Dagger, a novel two-phase decoupling-based attack framework. Specifically, in Phase 1, Dagger pre-trains a surrogate using decoupled information propagation to preserve structural context over sparse local subgraphs while handling isolated nodes, combined with manifold-level node mixup to synthesize continuous supervision signals and smooth decision boundaries. In Phase 2, Dagger freezes the encoder and fine-tunes the classifier head via class-balanced sampling paired with logit adjustment to rectify severe query imbalance without requiring extra victim queries. Extensive experiments across four benchmark graphs and four GNN backbones demonstrate that Dagger consistently outperforms state-of-the-art GNN stealing attacks, achieving up to 18.16\% higher fidelity while only utilizing 12.23$\times$ fewer queries than the strongest baseline.

---


### 415. [ORMA: Optimization-based Monocular 4D Reconstruction of Articulated Animals](https://arxiv.org/abs/2609.37986)

**<font color=#1a73e8>作者：</font>** Xuyi Hu, Francesco Palandra, Shangzhe Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering articulated 4D representations of animals from monocular videos remains challenging due to the large diversity of quadruped morphologies and lack of animal 4D supervision data. Existing learning-based reconstruction methods operate on individual images and rely on synthetic or model-fitted 3D supervision, which inherits the constraints of strong parametric priors and limits generalization to out-of-distribution species. When applied to out-of-distribution animals, they often recover a plausible pose while producing inaccurate geometry because the underlying shape model cannot faithfully represent the observed instance. We present ORMA, a training-free reconstruction framework that decouples articulation from shape, using the predicted pose as reference for optimization while leveraging generative 3D priors for accurate shape reconstruction. Given a reference image, we reconstruct the animal geometry and register it to the parametric model SMAL+, yielding an articulated shape adapted to the observed instance. We then combine per-frame articulated pose estimates with globally consistent camera poses to recover animal motion in a shared world coordinate frame, and further refine the reconstruction using self-supervised DINO correspondences and temporal consistency. To enable quantitative evaluation, we introduce PAW4D, a synthetic multi-species benchmark with ground-truth 3D geometry and camera motion. Experiments on PAW4D, PFERD, and challenging in-the-wild videos demonstrate that ORMA improves reconstruction accuracy while recovering globally consistend animal motion across diverse quadruped species.

---


### 416. [No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection](https://arxiv.org/abs/2609.38004)

**<font color=#1a73e8>作者：</font>** Jiaheng Guo, Haochen Zhang, Yu-Chao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series anomaly detection (TSAD) plays a crucial role in healthcare, finance, industrial monitoring, and other sectors. Within and between these settings, anomalies span vastly different temporal scales, from sub-second point spikes to multi-hour drift patterns. However, most existing TSAD methods commit to a single temporal granularity, and multi-scale designs either analyze different scales in isolation or are constrained to a predefined coarse-to-fine hierarchy, both failing to sufficiently capture multi-scale interactions. To resolve this limitation, we propose Multi-Scale Autoencoder with Cross-Scale Attention for TSAD (MSCAD), a simple yet powerful semi-supervised TSAD framework founded on parallel autoencoder branches corresponding to different patch sizes. A stack of symmetric bidirectional cross-scale attention blocks enables every pair of scales to exchange information before reconstruction without allowing any single scale to be privileged. On the comprehensive TSB-AD benchmark (40 datasets, 530 series), MSCAD achieves large performance gains against 50 baselines across multiple metrics, with VUS-PR of 0.57(+9.6%) on the univariate split and 0.47(+9.3%) on the multivariate split compared to the state-of-the-art.

---


### 417. [From Unity Simulation to Diffusion-Based Augmentation: Quantifying Dataset Balance for Robust Object Detection](https://arxiv.org/abs/2609.38010)

**<font color=#1a73e8>作者：</font>** Mohamed Benkedadra, Aissa Saoudi, Maxime Gloesener 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern computer vision models achieve high accuracy when trained on large-scale annotated datasets. In critical domains such as construction safety monitoring, data collection is costly, hazardous, and ethically constrained. This paper presents a systematic study comparing two complementary data generation paradigms, (1) Unity Simulation-based rendering and (2) Controllable Diffusion-based generation (CIA), for object detection under real data-scarce conditions. A unified experimental framework enables controlled dataset mixing across real, simulated, and generative sources, while maintaining identical model and training settings. Quantitative evaluation using Precision, Recall, mAP, and custom $\Delta$-metrics, reveals that neither simulation nor generative augmentation alone achieves optimal transferability. Unity-only training yields an mAP@0.5 drop of $-50\%$ relative to real data, while CIA-only training shows a milder $-16.5\%$ degradation. Hybrid compositions significantly improve performance, with the 90\% real + 10\% Unity configuration achieving the best overall mAP@0.5 of $62.68\%$ ($+7.64\%$ over baseline), and the 90\% real + 10\% CIA configuration maximizing precision at $74.45\%$. Results demonstrate that limited synthetic inclusion enhances generalization, while excessive substitution induces domain drift.

---


### 418. [A Function-level Dataset of Vulnerable and Fixed Source Code in JavaScript and TypeScript](https://arxiv.org/abs/2609.38012)

**<font color=#1a73e8>作者：</font>** Tamás Viszkok, Péter Hegedűs  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> JavaScript and TypeScript are widely used in modern web development, making their security critical; however, automated vulnerability detection is often constrained by the availability of high-quality training data. Here we present JsVul, a dataset curated from seven major sources. Unlike generic multi-language datasets that may retain noise -- such as minified code and cosmetic edits -- JsVul utilizes a language-specific pipeline. We collected pre-fix and post-fix versions of files around security fixes and, by filtering irrelevant artifacts and applying automated syntax normalization, isolated security-related changes. We ensured data integrity through multi-stage deduplication and heuristic-based labeling. Provided in a time-ordered JSONL format, JsVul supports robust model training in the JavaScript and TypeScript ecosystem and demonstrates the importance of language-aware preprocessing in building vulnerability datasets.

---


### 419. [Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy](https://arxiv.org/abs/2609.38016)

**<font color=#1a73e8>作者：</font>** Huan Rong, Chao Yin, Anouar Imel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is often defined as static state-to-cost mapping, and the safe-action projection in hard-constrained methods relies on the static projection with the fixed feasible region boundary estimated from offline demonstrations. The above drawback tightly couples the imposed constraints to the training scenarios, leaving the AD policy hard to handle different interaction scenarios, due to the improper state-level action-cost and the static projection boundary. Consequently, in this paper, we propose Brain-SAD, a brain-inspired safe autonomous driving control framework with dynamic fear-oriented constraints. By perceiving the current vehicle-interaction scene, Brain-SAD generates dynamic fear signal as fear reaction to online decide long-term policy for regular interaction or short-term policy for urgent-collision defense. In such two policy, the above fear-reaction will be constructed as the dynamic fear constraints, respectively reflecting the overall fear cost directly coupled with action-impact, and the dynamic fear boundary of the feasible region derived from different risky neighbors, both of which will in turn serve for the online policy optimization. Experimental results show that Brain-SAD outperforms existing methods, achieving higher success rate in shorter task-completion and collision-recovery time, and exhibits stronger reliability across continuous intersections of fluctuating complexity.

---


### 420. [Beyond Lip Sync: Reference-Grounded Oral Refinement for Audio-Driven Portrait Animation](https://arxiv.org/abs/2609.38019)

**<font color=#1a73e8>作者：</font>** Bangxun Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RGOR (Reference-Grounded Oral Refinement), an audio-driven lip-sync framework that renders the mouth of the specific person being dubbed rather than a generic one. Existing lip-sync systems follow the audio closely and keep the face recognizable, yet the mouth they render is an average mouth: the shape and texture of the lips, the arrangement of the teeth, and how much of them shows as the mouth opens are not that person's. The problem persists because nothing in current training or evaluation asks for the person's own mouth: perceptual losses accept any plausible mouth, face identity is carried mostly by the skin around it, and the released inference code of inpainting systems uses the unmasked target frame as the reference, which hides the gap. To address this, RGOR conditions every generated frame on frames from separate enrollment recordings of the same person and on HD patches of the mouth that bypass the VAE, and trains the generator against a paired judge that compares each rendered mouth with the person's reference and learns to reject a realistic mouth of someone else. We further build an evaluation protocol and use it to compare open-source and commercial lip-sync systems on held-out identities. Experiments show that RGOR achieves the best or second-best result on most metrics, and preserves the person's own lip and dental detail while keeping synchronization and the rest of the face intact.

---


### 421. [PE-EK-PINN: Physics Embedding with Evolving Kernel for Scalable Physics-Informed Neural Networks](https://arxiv.org/abs/2609.38023)

**<font color=#1a73e8>作者：</font>** Huiwen Zhang, Feng Ye, Chu Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) embed governing equations into deep learning, but enforce them only through loss residuals, leaving highly oscillatory wave behavior to be discovered by optimization. As a result, methods that achieve relative $L_2$ errors below $10^{-3}$ on standard manufactured Helmholtz benchmarks can fail on practical radiation problems involving singular excitations, absorbing boundaries, and wave fields spanning tens of wavelengths. Architectural physics embedding addresses this limitation by factorizing the field into analytically derived oscillatory kernels and learnable envelopes. However, the kernel dictionary must be manually constructed and scales with the number of elementary units, growing exponentially with the depth of hierarchically structured systems such as antenna arrays and metasurfaces. We propose PE-EK-PINN (Physics Embedded with Evolving Kernels), which treats physics kernels as reusable learned representations rather than fixed analytical inputs. A converged subsystem field is frozen and promoted to an evolved kernel, whose transformed copies are reused to represent higher-level configurations without deriving new governing equations. The resulting hierarchy makes the peak number of active kernels independent of system size and reduces cumulative training cost from $O(N)$ to $O(\log N)$. Experiments on dipole arrays, composite line-source geometries, and cross arrays demonstrate the dramatic training cost reduction, while achieving a reduced or comparable relative $L_2$ error. One notable example is PE-EK-PINN solves a $256$-dipole array more than 30 times faster than direct PE-PINN.

---


### 422. [Improving Function Space Flow Matching with Kernel Optimal Transport](https://arxiv.org/abs/2609.38049)

**<font color=#1a73e8>作者：</font>** Fred Xu, Thomas Markovich, Barbora Barancikova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for function-valued data, such as time series and solutions of partial differential equations, must learn distributions over infinite-dimensional spaces. Functional Flow Matching (FFM) extends Flow Matching to this setting, learning a velocity field whose flow transports a Gaussian prior to the data distribution, but it inherits the independent endpoint pairing of standard Flow Matching: in each batch, prior and data samples are matched arbitrarily, so the conditional bridge must traverse both the shared global structure of the dataset and instance-specific residuals. In function space this is harder to fix than in finite dimensions, since optimal transport (OT) on function spaces is delicate to formulate and a flat Euclidean surrogate ignores the geometry that distinguishes function-valued data. We propose kernel Functional Flow Matching (kFFM), which replaces the independent pairing by entropic OT under a kernel-induced cost, the coupling underlying the Hilbert Sinkhorn Divergence (HSD), leaving the FFM neural-operator architecture unchanged. We prove that the kernel cost and the HSD objective are uniformly bounded and well-posed on Banach ambient spaces, derive an error decomposition against quadratic-cost OT on compact metric spaces that isolates an irreducible kernel-cost mismatch term, and prove a discretization-invariance bound whose rate is governed by Sobolev regularity. Empirically, kFFM improves distributional matching over FFM, diffusion, adversarial, and finite-dimensional OT baselines on time-series and PDE benchmarks, with significant paired-seed gains over FFM and improvements that persist under non-kernel and physics-based diagnostics, including a turbulent Navier-Stokes benchmark. Bounded kernel costs already outperform raw $L^2$ Sinkhorn, and function-space-aware kernels (signature, Sobolev RBF) give further gains on rough or path-valued data.

---


### 423. [Jaxolotl: A Unified High-Performance Benchmark Suite for LTL-Based Multi-Task RL](https://arxiv.org/abs/2609.38065)

**<font color=#1a73e8>作者：</font>** Mathias Jackermeier, Jacques Cloete, Alessandro Abate  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training agents to follow arbitrary instructions is an important goal of multi-task reinforcement learning (RL). Linear temporal logic (LTL) provides a precise and structured formalism for specifying instructions to agents, and has been successfully adopted for training generalist multi-task policies. However, differences in implementations, task distributions, and evaluation protocols make existing methods difficult to compare, while high computational costs limit the scale and statistical reliability of experiments. We introduce Jaxolotl, a unified high-performance benchmark suite for multi-task LTL-RL to address these concerns. Jaxolotl provides a modular, end-to-end JAX implementation of six representative algorithms and four environments, together with newly curated task suites and a standardised, statistically robust evaluation protocol. By precompiling symbolic task representations into static arrays, Jaxolotl enables fully JIT-compiled training and evaluation, achieving end-to-end speedups of up to $220\times$ and supporting controlled comparisons at substantially greater experimental scale. We use this framework to systematically evaluate existing approaches, revealing complementary strengths and limitations: general methods capable of non-myopic reasoning struggle as the number of propositions grows, while methods with stronger scaling rely on environment-specific assumptions and suffer from myopia.

---


### 424. [RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA](https://arxiv.org/abs/2609.38072)

**<font color=#1a73e8>作者：</font>** Chengjie Jiang, Yunqi Zhou, Jiafeng Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires models to resolve small visual evidence within extremely large images. Existing approaches typically rely on token pruning, visual search, or tool-augmented reasoning at inference time. We instead investigate whether the benefit of zoom-in visual privilege can be internalized into the model. We introduce RS-OPSD, a reliable privileged on-policy self-distillation (OPSD) framework for UHR remote sensing VQA. To provide high-quality privileged information with explicit question-relevant evidence, we construct GeoEvidence-6K, containing 6,750 VQA samples across seven task categories with evidence-region annotations, and develop Human Feedback-Guided Skill Refinement (HF-SR) for scalable annotation. To address context loss from tight crops and conflicting signals from imperfect teachers, RS-OPSD introduces Context-Preserving Visual Privilege (CPVP) and Correctness-Aligned Distillation (CAD). Without any additional visual search or tool calls at inference time, RS-OPSD achieves state-of-the-art (SOTA) performance on XLRS-Bench, MME-RealWorld-RS, and LRS-VQA, outperforming pervious SOTA models of comparable scale by an average of 4.0 percentage points. Moreover, our 2B variant, RS-OPD-Lite, surpasses most 8B-scale models while achieving the fastest measured inference speed. Our Code, GeoEvidence-6K, and the model weights for RS-OPSD and RS-OPD-Lite are publicly available.

---


### 425. [MUGEN: Interactive Panoramic World Exploration via Camera Control](https://arxiv.org/abs/2609.38077)

**<font color=#1a73e8>作者：</font>** Jiaming Tan, Zhen Li, Shuwei Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive panoramic video generation aims to synthesize immersive 360\textdegree{} videos that remain visually coherent while following user-specified camera trajectories during exploration. However, progress is limited by a coupled data-and-model gap: existing panoramic video datasets are often short, weakly annotated, or lack camera trajectories, while existing camera-controlled video generation models are designed for perspective videos and do not directly support panoramic geometry. In this paper, we introduce MUGEN and Wan360 to address these limitations. MUGEN is a large-scale real-world panoramic video dataset tailored to interactive 360-degree world exploration, comprising over 1,300 hours of at least 4K panoramic videos with rich semantic and geometric annotations. Built on MUGEN, we further present Wan360, a camera-controllable interactive panoramic video generation model. Panoramic videos are commonly represented by EquiRectangular Projection (ERP), which unfolds a spherical 360-degree view into a rectangular frame with cyclic longitude seams and pole distortions. To this end, Wan360 introduces three parameter-free ERP-aware components: periodic longitude RoPE for seam-consistent positional encoding, ERP-aware padding for reducing boundary artifacts, and random roll yaw for consistent learning. For camera control, Wan360 uses a panoramic Plücker embedding that represents camera motion with ERP rays rather than perspective pinhole rays. Experiments show that MUGEN serves as a data foundation for panoramic world exploration, and that Wan360 enables high-quality, temporally coherent, camera-controllable 360-degree video generation.

---


### 426. [OmniTaskonomy: When Does Visual Generation Improve Visual Understanding?](https://arxiv.org/abs/2609.38079)

**<font color=#1a73e8>作者：</font>** Jiaxin Ge, Yiming Qin, Ji Xie 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training a model to generate visual content can encourage it to learn rich perceptual capabilities related to geometry, spatial relationships, and objectness; yet, its benefits for visual understanding remain unclear. We ask: when and how does visual generation supervision improve visual understanding? We study controlled pairs of image-to-image (I2I) generation and image-to-text (I2T) understanding tasks that express the same underlying problem in different output modalities. We find that under the correct recipe, I2I training improves downstream I2T performance, with larger gains as the amount of I2I training data increases. We next ask which generation tasks benefit which understanding capabilities. To study transfer beyond paired tasks, we introduce OmniTaskonomy, a unified taxonomy spanning 19 I2I generation tasks and 25 I2T understanding capabilities. The resulting transfer map reveals selective, task-dependent benefits. Some follow intuitive correspondences, e.g., depth prediction improving metric 3D reasoning, object pointing improving counting, and jigsaw reconstruction improving 2D ordering. Interestingly, we also uncover surprising connections: 2.5D segmentation improving category recognition and Z-depth prediction improving localization. To probe these patterns, we analyze gradient alignment between generation and understanding tasks and find that stronger alignment is associated with larger downstream transfer gains. Together, our results highlight visual generation as a rich source of supervision for visual understanding and provide a roadmap for unlocking its benefits through the right training curriculum and task selection. Project page: this https URL.

---


### 427. [Traversing the solution space of neural networks with Hessian Null Space Continuation](https://arxiv.org/abs/2609.38081)

**<font color=#1a73e8>作者：</font>** Ann Huang, Mitchell Ostrow, Zhouyang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. However, it is unclear how these solutions are related in weight space. We unify these subfields and show for the first time that many different internal mechanisms exist within a local mode-connected region in weight space. To do so, we introduce Hessian Null Space Continuation (HNC), a scalable method that uses local curvature to traverse regions of weight space that preserve network function, and can be steered toward solutions with specified properties. In RNNs trained on a memory task, HNC reaches drastically different representations and dynamics with maintained behavior. In ImageNet-trained Vision Transformers, HNC finds representations that differ more from the original network than any independently trained model with a different architecture or objective. In reinforcement-learning agents, HNC uncovers a distinct navigation strategy at comparable return and exposes reward hacking in an AI Safety Gridworld. Finally, HNC measures the local geometry of the solution set, showing how model size and task complexity shape its dimension and functional sensitivity. Our results show that a surprisingly large amount of representational diversity exists near a single trained solution, unseen by standard gradient-based optimization. HNC identifies and quantifies this diversity, opening new possibilities for mechanistic understanding of solution spaces and for model merging, editing, and fine-tuning.

---


### 428. [Dimensionally consistent surrogate modelling through dimensional analysis and harmonic expansions](https://arxiv.org/abs/2609.38094)

**<font color=#1a73e8>作者：</font>** Ernest Tarrus, Hector Gisbert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensional homogeneity is a fundamental constraint on physically meaningful models, requiring invariance under changes of units. We present a data-driven method for constructing surrogate models that satisfy this constraint at the level of the hypothesis class. Starting from a dimension matrix of measured variables, the method derives Buckingham $\Pi$-groups, constructs admissible dimensional prefactors, and approximates the remaining dimensionless dependence using truncated harmonic expansions on normalized invariant domains. Once the prefactor and dictionary are fixed, the coefficients are obtained from a regularized linear regression problem. We test the approach on the simple pendulum, Planck's black-body law, the double-pendulum Lyapunov field, and an experimental COBE/FIRAS black-body spectrum dataset. The results show that dimensional constraints improve conditioning, robustness to noise, and sample efficiency relative to unconstrained baselines, while the choice of dictionary becomes important in non-periodic or multi-invariant settings. The learned expressions are explicit and inexpensive to evaluate, which makes them useful as surrogate models for structured physical problems.

---


### 429. [How Local Mixing Encodes Relative Position in Global NoPE Attention](https://arxiv.org/abs/2609.38109)

**<font color=#1a73e8>作者：</font>** Cutter Dawes, Nick Alonso, Tom Figliolia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in global attention layers has recently been shown to be successful at scale. How and why this approach works is not well-understood. In this paper, we develop an explanation of how hybrid models of this sort can implicitly encode position at global NoPE layers. Supported by both theoretical and empirical evidence, our central argument is that SWA and gated linear attention induce a recency bias in the residual stream that propagates to, and is selected by, the global attention logits. Moreover, in contrast to the implicit position encodings found in models with only global NoPE attention, in which positional information arises solely from the causal mask, the recency bias in hybrid models can be maintained across long sequences. In addition to deepening our understanding of how hybrid models encode position, these findings may provide insights for how to encode position in a way that can extrapolate to longer sequence lengths indefinitely.

---


### 430. [IMPACT: Modeling Socially Interdependent Movement in a Generative Multi-Agent Simulation of a Pompeian Household](https://arxiv.org/abs/2609.38113)

**<font color=#1a73e8>作者：</font>** Tianqi Liu, Nayoung Kim, Julia Sebastien 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Simulations of archaeological sites can make interpretations of past cultural practices observable and examinable. Generative multi-agent simulations offer a bottom-up approach to modeling how people collectively moved through and used historical spaces. However, current agents designed to simulate everyday life often plan and act independently, limiting their ability to capture how movement depends on others' actions. We introduce IMPACT (Interdependent Movement Planning through Inter-Agent Constraints and Triggers), an architecture that uses culturally specific roles and obligations to define dependencies among agents' activities and guide coordination. IMPACT connects socially gated milestone planning, wait-or-prompt resolution, structured directive issuance, and directive integration. These mechanisms determine whether and when activities can begin or change as social conditions evolve, producing socially constrained and prompted movement as their primary observable outcome. We instantiate IMPACT in a five-hour simulation of a Pompeian dinner involving ten agents across interdependent roles. Analysis of five simulation runs shows how social roles, responsibilities, and status relations shape household activities and spatial practices, as reflected in patterns of co-location, asymmetric waiting, co-movement, and social directives. In a controlled ablation evaluation, thirty-seven participants rated the complete architecture's behavior as more socially coherent and believable than that of two reduced architectures. Interviews with six archaeology experts highlighted historically plausible movement patterns and the simulation's potential to support archaeological interpretation, while identifying areas requiring stronger historical grounding for future work.

---


### 431. [Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History](https://arxiv.org/abs/2609.38114)

**<font color=#1a73e8>作者：</font>** Weiqiang Wang, Zhuokun Chen, Yusheng Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion enables interactive streaming generation, but suffers from error accumulation over long rollouts. Self-rollout training reduces exposure bias, yet finite rollouts leave long-range drift unresolved. We observe that the noise level of the history key-value (K/V) representations trades visual quality against motion, and that restoring gradients through the history aligns causal training far more closely with bidirectional training. Motivated by these observations, we introduce Self-Aligned Forcing (SAF), a training scheme that aligns the history of each block with the noise level of the block being denoised. Specifically, the history is the K/V produced by preceding blocks at the same denoising stage, so all blocks at a stage can be denoised in a single forward pass under a causal mask. This keeps the noisy history differentiable, allowing future losses to optimize how it is encoded. SAF therefore avoids a separate no-gradient rollout and per-block timestep-zero recaching, training up to 1.8x faster than prior methods with lower memory. At inference, SAF achieves the highest single-GPU throughput among existing methods and keeps one history bank per stage for a multi-GPU pipeline, reaching 49.1 FPS on 4 GPUs. Experiments show superior long-horizon generation with a better balance between visual quality and motion. Project page: this https URL.

---


### 432. [GA-EIRFS: A Geometry-Augmented Repeat-Factor Sampling Method for Long-Tailed LiDAR 3D Object Detection](https://arxiv.org/abs/2609.38116)

**<font color=#1a73e8>作者：</font>** Taufiq Ahmed, Constantino Álvarez Casado, Daniel Herrera Castro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed 3D object detection is treated as a class-frequency problem, but LiDAR supervision quality depends on object observability: similar frequencies can hide different geometric evidence. We introduce Geometry-Augmented Exponentially Weighted Instance-Aware Repeat Factor Sampling (GA-EIRFS), a detector-agnostic method that modulates a frequency-based repeat factor with a fixed geometry score combining point count, surface-normal entropy, and surface coverage. GA-EIRFS changes only frame-sampling probabilities, leaving the detector and inference unchanged. On nuScenes it improves mean average precision (mAP) and the nuScenes detection score (NDS) in four converged experiments with CenterPoint and PointPillars over two seeds; for CenterPoint at seed 666, mAP rises from 0.552 to 0.563 and bicycle AP from 0.306 to 0.359. Per-class gains correlate with the class sampling-weight increase (Spearman rho=0.70, p=0.025) but not with geometry score alone (rho=0.32, p=0.37), so geometry amplifies frequency-driven need. KITTI results vary across seeds, most for the rarest class. Code: this https URL.

---


### 433. [Stochastic World Models for Verifying Vision-Based Neural Feedback Systems](https://arxiv.org/abs/2609.38120)

**<font color=#1a73e8>作者：</font>** I. Samuel Akinwande, Mykel J. Kochenderfer, Clark Barrett  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying a vision-based neural feedback system requires a model of the observations its controller acts upon. Such a model must capture the variation the sensor produces, while remaining tractable for closed-loop analysis. Generative adversarial networks (GANs) have served as perception surrogates, but they are large, reproduce complex scenes poorly, and are hard to verify. We explore stochastic world models as a richer class of perception surrogates. We train a world model with physically grounded latents, built from operations that standard verifiers bound. It reproduces held-out frames more faithfully than GAN surrogates with up to 130 times as many parameters. To verify these surrogates, we develop a procedure that combines falsification, adaptive refinement, symbolic, and backward analyses. On an emergency braking benchmark with a GAN surrogate, our procedure resolves the entire state space, 38% of which the state-of-the-art verifier left unresolved. On the RGB version of the benchmark, where no verification results have previously been reported, our procedure resolves over 80% of the state space with a world model surrogate.

---


### 434. [HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123)

**<font color=#1a73e8>作者：</font>** Lei Ke, Jiahao Pan, Zeyue Tian 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time. Yet prevailing interactive world models remain strictly silent, focusing exclusively on visual rendering and control while overlooking the acoustic dimension. We present HelixWorld, a real-time interactive audio-visual world model where visual scenes and camera-grounded spatial stereo sound co-evolve natively under user interaction. We curate a high-fidelity spatial audio-visual dataset with true stereo acoustics and metric camera poses, upon which we pre-train a bidirectional teacher conditioned on 6-DoF camera trajectories and user actions. To enable low-latency causal interaction, we distill the teacher into a few-step streaming student via an online trajectory distillation loss, sustaining drift-free joint audio-visual rollouts at 24 FPS on a single GPU. Furthermore, we formalize spatial-acoustic consistency and introduce HelixBench to evaluate whether synthesized sound fields faithfully track dynamic viewpoint motion. Extensive experiments demonstrate that HelixWorld matches state-of-the-art silent world models in visual fidelity and responsiveness, while significantly surpassing existing baselines in camera-aligned spatial-acoustic immersion.

---


### 435. [Achieving an $O(1/N)$ Optimality Gap in Average-Reward Weakly-Coupled MDPs](https://arxiv.org/abs/2609.38132)

**<font color=#1a73e8>作者：</font>** Yige Hong, Xiangcheng Zhang, Qiaomin Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study average-reward weakly-coupled Markov decision processes (WCMDPs), where a WCMDP consists of $N$ smaller MDPs, called arms, that share multiple per-step budget constraints. We consider the setting where the arms have identical model parameters, multiple actions, and state- and action-dependent costs. For restless bandits (RBs), a well-studied special case of WCMDPs, prior work has developed policies that achieve an $O(1/\sqrt{N})$ optimality gap under general conditions, and has further identified conditions under which policies can achieve a better-than-$1/\sqrt{N}$ optimality gap. However, for general WCMDPs, no prior result achieves an optimality gap better than $1/\sqrt{N}$. In this paper, we identify conditions analogous to those for RBs under which a better-than-$1/\sqrt{N}$ optimality gap is achievable, and design a policy that attains an $O(1/N)$ optimality gap. Notably, unlike prior approaches based on generalizing priority orderings, our policy is not priority-based but rather is designed to induce locally linear mean-field dynamics.

---


### 436. [Multi-Agent Flow Matching with Decoupled Generative Guidance](https://arxiv.org/abs/2609.38133)

**<font color=#1a73e8>作者：</font>** Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling is widely used for producing diverse objects from complex, multimodal distributions. However, its expressivity does not, in general, come with formal guarantees that the generated objects satisfy hard constraints or requirements. In multi-agent generation, this problem becomes more challenging because a hard requirement can depend on multiple agents, while each agent may need to determine its own guidance input without relying on the simultaneously computed guidance inputs of other agents. To this end, we introduce DeGG-Flow, a general framework for multi-agent flow matching with decoupled generative guidance. By representing the generative process as a control-affine dynamical system, we develop guidance conditions for two classes of coupled requirements: shared requirements whose satisfaction depends on multiple agents together, and private requirements associated with each individual agent dependent on its neighbors. For both classes, we establish feasibility conditions and finite-horizon convergence guarantees. We further derive a Wasserstein bound that characterizes the distributional deviation induced by the guidance. We demonstrate DeGG-Flow on multi-robot collaboration for crossing a spatial gap by reconfiguring the environment, and on multi-object scene generation with affordance requirements. Across both applications, DeGG-Flow directly generates objects that satisfy all corresponding hard requirements, including at team sizes unseen during training.

---


### 437. [LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146)

**<font color=#1a73e8>作者：</font>** Shengxiang Ji, Boyang Wang, Haiyang Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LIFT, a unified image-to-video generation framework that complements camera control with Layout-In-FuTure control, enabling users to specify what should appear in a future view and where it should appear. This addresses a practical need in controllable video generation: given an initial image, users often care not only about how the camera moves, but also about what the scene should look like at key future moments, especially the final frame. Existing camera controls specify viewpoint trajectories, while text prompts provide only coarse semantic guidance; neither precisely determines the content and spatial layout of future views. This limitation becomes particularly pronounced under large viewpoint changes, where the camera reveals regions that are not visible in the first frame. LIFT therefore uses the last-frame layout as an explicit control signal for the desired future scene. Since learning from such sparse layout guidance is substantially more challenging than conditioning on dense per-frame layouts, we introduce on-policy self-distillation (OPSD) to transfer the control capability of a dense-layout teacher to a last-frame-layout student. We further curate LIFT-Vista, a dataset featuring large viewpoint changes with camera and temporally consistent layout annotations. Experiments show that LIFT improves video quality, future-layout controllability, and camera controllability over other methods.

---


### 438. [FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152)

**<font color=#1a73e8>作者：</font>** Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce FracGen, a fracture-aware video generation model that produces plausible, controllable fracture dynamics from a single image of an intact object, conditioned on physics signals. To train FracGen, we build FracSim, a fracture-aware simulation framework that augments material point method (MPM) simulation with a continuum damage model, producing paired fracture videos and dense, pixel-aligned physical fields at no additional cost beyond standard rendering. FracGen leverages these maps in two ways: it is trained to jointly predict them alongside RGB video, encouraging the model to capture physical state rather than surface appearance; and it is supervised with physics-informed losses that encourage consistency among the predicted maps. As a result, FracGen captures distinct material-specific fracture behavior without expensive test-time simulation or per-scene tuning, while offering fine-grained control over where an object tears, how fast the crack propagates, and how much deformation precedes failure. We further introduce a benchmark for evaluating the physical plausibility of generated fracture video, and show through extensive experiments that FracGen outperforms existing video generation baselines in both physical and visual fidelity. Results are best viewed in our project website: this https URL.

---


### 439. [PowerSim: Differentiable Physics Simulation and Rendering with Power Diagrams](https://arxiv.org/abs/2609.38153)

**<font color=#1a73e8>作者：</font>** Trong-Tung Nguyen, Anand Bhattad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PowerSim, a method to bring physically grounded, differentiable dynamics to PowerFoam's power diagram based 3D representation. PowerSim directly couples a pre-trained PowerFoam scene to the Material Point Method (MPM) by exploiting a natural alignment between the two: the geometric and appearance properties of each primitive correspond closely to the quantities MPM already tracks as an object deforms. Consequently, simulated motion can drive the scene's geometry and appearance directly, without an auxiliary representation in between. Built on this framework, we enable a range of applications on real and synthetic scenes: (1) simulating a static scene under user interaction, (2) recovering spatially varying material fields, (3) compositing primitives from independently captured scenes into a single simulation-ready scene and (4) ray-tracing reflections that update consistently as the object deforms. Our results suggest that PowerSim excels over previous frameworks for physically grounded dynamics, while unlocking unique advantages-such as secondary ray lighting effects on dynamic scenes. Results are best viewed on our project website: this https URL.

---


### 440. [LongLive-Plug: Once-for-All Distillation for Video Generation](https://arxiv.org/abs/2609.38154)

**<font color=#1a73e8>作者：</font>** Shuai Yang, Luozhou Wang, Wei Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or to improve long-video generation. This stage is typically repeated for every specialized model. We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs on a base model for training-free, plug-and-play deployment to compatible downstream models. These capabilities include single-pass classifier-free guidance, few-step sampling, and long-context error correction for autoregressive generation. The adapters remain reusable even when downstream models add conditioning branches, expand output channels. Despite training at a fixed guidance scale, our dedicated CFG LoRA provides text guidance control through its inference weight. Combining it with a few-step LoRA simultaneously preserves few-step generation and CFG controllability on downstream tasks. We verify training-free deployment on 54 downstream models across three backbone families and eight task categories, including world modeling, robotics, editing, and multimodal generation. The approach may support additional compatible models. Each capability can thus be distilled once per backbone family and reused without per-target retraining.

---


### 441. [Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies](https://arxiv.org/abs/2609.38155)

**<font color=#1a73e8>作者：</font>** Hui Ren, Lei Fan, Henry Pao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Entity Biographies (GEB), a long-video memory framework that groups visually grounded observations of the same physical instance across clips into retrievable biographies while preserving the context of each moment. During question answering, the biography is retrieved alongside episodic evidence, allowing the model to follow an entity through events using identity links established during memory construction. Evaluations across four benchmarks, including day-long and week-long recordings, demonstrate improvements over prior memory frameworks in both multiple-choice and open-ended question answering. On EgoLifeQA, GEB achieves 72.0% accuracy, 4.4 percentage points above the best published result. Ablations show that grounded identity association and biography reading both contribute to the gains, which additional descriptions alone do not fully recover.

---


### 442. [DMA$^2$: Pixel-space Distribution Matching with Adversarial and Anchor Losses](https://arxiv.org/abs/2609.38156)

**<font color=#1a73e8>作者：</font>** Xin Lin, Zhifei Zhang, Yuqian Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution matching distillation (DMD) provides a general framework for few-step diffusion generation, but its modern text-to-image instantiations have been developed primarily around latent diffusion. It therefore overlooks key properties and design opportunities of native RGB. We revisit two DMD interfaces for pixel-space teachers. On the teacher-matching side, diagnostics show low-noise RGB matching is dominated by a local-texture cue, motivating a fixed high-noise matching band. On the real-data side, native clean-RGB outputs allow guidance from an external visual representation without traversing a decoder or sharing the heavy fake-score critic. DINO-Adv removes this critic from the adversarial gradient path and supplies local parametric patch guidance. For distribution-level guidance, we introduce AF-Loss, a parameter-free auxiliary semantic distribution-field objective designed for text-to-image DMD. It operates on detached rolling real and generated supports in the shared DINOv2 space while preserving prompt-conditioned teacher supervision. AF-Loss adds no learnable parameters or inference-time computation. Together these designs form DMA$^2$. Across DPG-Bench, GenEval, VQAScore, and COCO30K, the four-step DMA$^2$ student performs better than the 25-step teacher and evaluated few-step distillers.

---


### 443. [Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163)

**<font color=#1a73e8>作者：</font>** Haoyi Jiang, Liu Liu, Xinjiang Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction. We study the design of this space through controlled comparisons, finding that neither reconstruction fidelity nor pre-trained perceptual features alone ensure effective policy learning. These findings motivate ReWAM, a representation-centric world-action model built on pre-trained DINO features. Feature Calibration and a Temporal Representation Bottleneck organize these features into compact world states suited to dynamics modeling. Action-Grounded Representation Shaping routes only action-loss gradients to the bottleneck, thereby letting the policy shape what the representation encodes while the world model learns how it evolves. Without generative video pre-training, ReWAM achieves 93.6% success on RoboTwin 2.0. On RoboDojo, it achieves an average score of 12.29 and a success rate of 8.28% using approximately 600 hours of embodied pre-training data.

---


### 444. [Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data](https://arxiv.org/abs/2609.38165)

**<font color=#1a73e8>作者：</font>** Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The landscape of satellite imagery time series datasets and boundary-pushing architectures for cropland segmentation has never been richer. However, in this gold rush, important truths are being missed on both fronts, as a drive for the most novel concepts or the largest datasets pushes finer details to the side. In this paper, we present our hybrid transformer-convolutional model, Cropland Parallel Attention and Refinement Network for Segmentation (PAtteRNS), the first model to use self-attention mechanisms separately for each of the temporal, spectral, and spatial aspects of Sentinel-2 multispectral SITS data. To achieve fully-factorised attention in our proposed model, we introduce a novel parallel transformer architecture which significantly reduces the computational complexity of triple-factorised self-attention. We validate our architecture with an in-depth ablation study, and analyse the performance of our model against state-of-the-art crop segmentation models on multiple tile-size variants of the popular PASTIS and MTLCC datasets. Our findings show our model to outperform all others in the task of crop class segmentation, verified across multiple important segmentation metrics, with especially strong performance against compared models seen in the often under-reported parcel delineation quality, for which we use the Boundary IoU metric. We also find that flawed class groupings within datasets can have a significant negative impact on model performance, and report that alternate tile-size variants of crop segmentation datasets produce results incomparable to one-another, invalidating fair comparison between model performance when trained on different tile-sizes. Based on these findings, we suggest further work is required to standardise best practices when constructing SITS crop segmentation datasets, and to enable future dynamic-tile-sizing for ideal model performance.

---


### 445. [Adversarial Training for Pixel Diffusion](https://arxiv.org/abs/2609.38170)

**<font color=#1a73e8>作者：</font>** Xin Lin, Zhifei Zhang, Yuqian Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel diffusion models generate RGB images directly, avoiding the bottleneck of an autoencoder, yet their outputs still systematically underrepresent fine-scale natural-image statistics. We show that adversarial learning provides an effective post-training correction for this deficiency. Starting from a pretrained model, we retain its original diffusion or flow-matching objective and add an adversarial loss to the predicted output at non-high-noise timesteps, leaving the model architecture and sampling procedure unchanged. To our knowledge, this is the first systematic study of adversarial post-training for pixel diffusion. Across two pixel backbones, the method jointly improves distribution fidelity, coverage, prompt alignment, and perceptual quality. We further investigate why it works. Frequency-band and power-law analyses show that the original models systematically underproduce natural-image high-frequency content, while adversarial post-training restores this missing spectral power. In contrast, perceptual loss also increases high-frequency content but sacrifices distribution fidelity and prompt alignment. Nearest-neighbor, recall, and matched no-GAN SFT controls further rule out memorization, mode dropping, and additional optimization as simple explanations. Finally, we examine the boundary of this effect. Under the tested latent diffusion configurations, the same procedure does not produce comparable joint gains and adds almost no decoded high-frequency power. These results identify direct output access to the image statistics being corrected as a key factor governing when adversarial post-training succeeds.

---


### 446. [Breakdown of Local Denoising as Semantic Speciation](https://arxiv.org/abs/2609.38176)

**<font color=#1a73e8>作者：</font>** Guangkuo Liu, Mert Okyay, Yifan F. Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dynamics of generative models exhibit two apparently distinct temporal windows: a speciation window, in which a sample commits to a semantic class, and a nonlocality window, in which local context windows become insufficient for generation. Motivated by evidence of their near-concurrence in a variety of frontier models, we investigate their relationship through the spatial distribution of semantic information. Under a "common cause" hypothesis, we prove that the nonlocality window must lie in the speciation window. This hypothesis postulates that semantic labels explain a fraction of the correlations between distant tokens, a condition that is natural for many real datasets. We further give conditions under which both windows shrink to a single limiting time as system size grows, defining a "phase transition", and verify this behavior analytically in Gaussian mixtures. Together, these results identify conditions under which semantic information explains the concurrence of speciation and nonlocality, connecting two complementary perspectives on the emergence of semantic structure in generative modeling.

---


### 447. [Point2Part: Unified 3D Partitioning from Point Prompts](https://arxiv.org/abs/2609.38180)

**<font color=#1a73e8>作者：</font>** Hao-Tang Tsui, Yu-Rou Tuan, Xiaoxuan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D part decomposition methods do not necessarily partition the original shape into non-overlapping parts that collectively cover the entire shape, allowing overlaps or gaps that hinder downstream part-level applications. We instead formulate part decomposition as a joint partitioning of the entire shape, where the predicted parts are non-overlapping and jointly recover the entire shape. Our key insight is that part decomposition should consider all desired parts jointly, rather than modeling each part independently. To this end, we develop a promptable model for 3D part decomposition from images or meshes. Users can specify desired parts through 3D point prompts for controllable decomposition. Given one point prompt per desired part, our model produces the corresponding parts as a complete partition of the entire shape. We build on a pretrained 3D generation model and first obtain a shape latent from either an input image or mesh. We then introduce a prompt encoder that maps each 3D point prompt to a part token while attending to the shape latent. To decode the desired parts, we propose a novel part decoder jointly scoring the entire shape against all part tokens in a coarse-to-fine manner, assigning every position within the shape volume to exactly one part. We perform part decomposition in this shared shape latent space, enabling a unified model for image-to-part generation, mesh-to-part generation, and part segmentation. Our method outperforms existing works on all part-quality metrics across all three tasks, and improves compatibility among parts by an order of magnitude over previous SOTA methods. Code and models will be released.

---


> [!TIP]
> 当前位于：**401-447**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-447**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
