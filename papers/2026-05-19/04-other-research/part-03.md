# 📦 其他研究 | 2026年05月19日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 101. [Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered](https://arxiv.org/abs/2605.15622)

**<font color=#1a73e8>作者：</font>** Sijia Liu, Yicheng Lang, Soumyadeep Pal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization, learning from finite differences of function evaluations without backpropagation, has recently regained attention in deep learning due to its memory efficiency and applicability to gray- or black-box pipelines. Yet, ZO methods are often dismissed as fundamentally unscalable because of estimator variance and unfavorable query complexity. We argue that this conclusion might be misguided: ZO optimization is underexplored, not underpowered. We show that many perceived limitations stem from myopic development practices, most notably full-space, element-wise, estimator-centric designs. We articulate six positions spanning the algorithmic, systems, and evaluation stack. First, we revisit the feasibility boundaries of estimator-centric ZO methods through variance control, variance-query tradeoffs, and directional-derivative lenses. Then, we identify three underexplored opportunities: (i) subspace and spectral views of ZO that enable interpretable variance reduction with graceful query scaling, (ii) the forward-only nature of ZO as a systems advantage for communication-efficient, pipeline-friendly, and resource-constrained training, and (iii) the need to de-obfuscate ZO evaluations from task complexity. We strongly advocate rethinking ZO optimization around its unique strengths and acting accordingly, opening a viable path toward large-scale, system-aware, and resource-efficient learning with ZO optimization.

---


### 102. [ColPackAgent: Agent-Skill-Guided Hard-Particle Monte Carlo Workflows for Colloidal Packing](https://arxiv.org/abs/2605.15625)

**<font color=#1a73e8>作者：</font>** Lijie Ding, Changwoo Do  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce ColPackAgent, an agent framework that autonomously runs Monte Carlo simulations of colloidal packing through a Model Context Protocol (MCP) tool server and an agent skill, whether as a standalone agent or inside an existing agent system. By harnessing the MCP server and agent skill, ColPackAgent executes a structured workflow for colloidal packing simulations, which are central to studies of phase behavior, self-assembly, and materials design. Without dedicated simulation tools and workflow instructions, general-purpose Large Language Model (LLM) agents tend to describe such workflows rather than execute them reliably. The MCP server exposes a custom-built colpack Python package that wraps HOOMD-blue hard-particle Monte Carlo, and the skill encodes a four-stage workflow contract. ColPackAgent can carry out the workflow interactively with human feedback, autonomously from an end-to-end prompt, or as autoresearch following a provided program file. We demonstrate the system in different modes with several colloidal packing simulation examples such as cube particles in 3D, a binary system of disks and capsules in 2D, and the 2D hard-disk freezing transition using autoresearch. We also compare model performance on this workflow across a panel of LLMs with 17 stage-specific prompts. This benchmark provides a stage-level check of how reliably different models follow the setup, planning, and analysis workflow. Together, these results show that pairing a domain Python package with MCP tools and a portable agent skill provides a practical route for turning a simulation toolkit into an agent-assisted research workflow.

---


### 103. [Learning Disentangled Representations for Generalized Multi-view Clustering](https://arxiv.org/abs/2605.15640)

**<font color=#1a73e8>作者：</font>** Xin Zou, Ruimeng Liu, Chang Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-View Clustering (MVC) has gained significant attention for its ability to leverage complementary information across diverse views. However, existing deep MVC methods often struggle with view-distribution entanglement during cross-view fusion, which hampers the quality of the shared latent space and leads to suboptimal Figures. To address this issue, we propose the Generalized Multi-view Auto-Encoder (GMAE), a framework designed to preserve cross-view complementarity through disentangled representation learning. Specifically, GMAE employs dual-path autoencoders to decouple source features into view-specific and view-common embeddings, facilitating the discovery of clearer clustering structures. We further construct cross-view adversarial discriminators to guide view-specific encoders in capturing more discriminative features. By strategically modulating mutual information, GMAE effectively aligns distributions and prevents representation collapse, ensuring the generation of robust, non-trivial embeddings. Comprehensive experiments on 13 benchmark datasets demonstrate that GMAE consistently outperforms state-of-the-art methods in both complete and incomplete MVC tasks. Our code implementation is available at the repository: this https URL.

---


### 104. [Perforated Neural Networks for Keyword Spotting](https://arxiv.org/abs/2605.15647)

**<font color=#1a73e8>作者：</font>** Vishy Gopal, Aris Ilias Goutis, Ralph Crewe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge machine learning presents a unique set of constraints not encountered in cloud-scale model deployment: strict memory budgets, limited compute, and non-negotiable accuracy thresholds must all be satisfied simultaneously. Existing compression and optimization techniques can trade one resource for another, but rarely improve both accuracy and model size at the same time. This paper presents the application of Perforated Backpropagation to keyword spotting on the Edge Impulse platform, an experiment that won the Best Model award at the Edge Impulse 2025 Hackathon in December 2025. By adding artificial Dendrite Nodes to a standard convolutional neural network trained on the Edge Impulse keyword spotting tutorial pipeline, we demonstrate that dendritic models outperform traditional architectures at every level of parameter count and at every accuracy threshold tested across 800 hyperparameter trials. The best dendritic model achieved a test accuracy of 0.933 with only 1,500 parameters, versus the baseline accuracy of 0.921 requiring approximately 4,000 parameters. These results suggest that Perforated Backpropagation is a powerful addition to the edge AI engineer's toolkit, offering simultaneous gains in both model quality and deployment efficiency.

---


### 105. [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/abs/2605.15648)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Shujie Cui, Hui Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially Private Stochastic Gradient Descent (DP-SGD) is widely used to protect training data in machine learning. Its privacy guarantee is commonly analyzed through a security game in which an adversary infers whether a target record is included in the training dataset from the mechanism output. The resulting privacy leakage is characterized by a privacy curve, which reports the false negative rate as a function of the false positive rate.
We identify a mismatch between this formal analysis and common DP-SGD implementations. Existing analyses often model DP-SGD and its variants as the Subsampled Gaussian Mechanism (SGM), where Gaussian noise is added to the sum of clipped gradients computed from a Poisson-sampled batch. In practice, however, many implementations apply an additional normalization step: the noisy gradient sum is divided either by the expected batch size or by the sampled batch size. These mechanisms are therefore better formalized as the Expected-Averaged SGM (EASGM) or the Batch-Averaged SGM (ASGM), respectively.
We re-analyze the privacy guarantees of DP-SGD under the EASGM and ASGM formulations. Our theoretical results show that these guarantees can be weaker than the standard SGM-based guarantee, implying that the true privacy leakage may exceed the reported guarantee in some regimes. We further audit four state-of-the-art DP-SGD implementations, including Meta's Opacus library, and observe empirical leakage beyond the SGM-based guarantees. Finally, we audit Opacus versions v0.9.0 to v1.5.4 and derive a corrected privacy guarantee for the latest implementation.

---


### 106. [Towards Code-Oriented LM Embeddings for Surrogate-Assisted Neural Architecture Search](https://arxiv.org/abs/2605.15649)

**<font color=#1a73e8>作者：</font>** Pranav Somu, Advay Balakrishnan, Stepan Kravtsov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing effective surrogates (performance predictors) for Neural Architecture Search (NAS) typically requires expensive fine-tuning or the engineering of complex representations. We propose a low-cost embedding strategy that leverages the inductive bias of Language Models (LMs) to eliminate these overheads. By representing architectures as PyTorch class definition text, we demonstrate that off-the-shelf LMs act as competitive feature extractors without NAS-specialized fine-tuning. The final predictor is constructed by passing the extracted Code-Oriented LM Embeddings (COLE) through a lightweight regression head. We also investigate strategies to improve embedding quality and utilization. Our experiments on the NAS-Bench-201 and einspace search spaces reveal that raw code inputs yield higher predictive performance than other text-based encodings (e.g., ONNX-to-text encodings) when using frozen LMs. We also observe COLE drives superior surrogate-assisted search using the BANANAS algorithm in NAS-Bench-201. When optimizing for CIFAR-100 performance, replacing structural path encodings with COLE for architecture representation allows for a 34% decrease in the evaluation budget required to reach within 1% of the fittest architecture in the search space (by test accuracy). As any neural architecture can be represented as code, these findings establish COLE as a versatile and efficient foundation for advancing NAS.

---


### 107. [Sharp Spectral Thresholds for Logit Fixed Points](https://arxiv.org/abs/2605.15651)

**<font color=#1a73e8>作者：</font>** Tongxi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax feedback systems are a common mathematical core of entropy-regularized reinforcement learning, logit game dynamics, population choice, and mean-field variational updates. Their central stability question is simple: when does a self-reinforcing softmax system produce a unique and globally predictable outcome? Classical theory gives a conservative answer. By treating softmax as a unit-scale response, it certifies stability only in a strongly randomized regime.
We prove that the classical approach misses an entire stable regime and does not identify the point at which the qualitative change truly occurs. For finite-dimensional affine logit systems, the sharp dimension-free Euclidean threshold is $$\beta\|\Pi W\Pi\|_{\mathcal T\to\mathcal T}<2,$$ rather than the previously used condition, which certifies stability only while the softmax system remains safely over-regularized. Our theorem fills the previously missing pre-bifurcation regime, extending stability guarantees for affine softmax feedback systems to reward-responsive yet globally predictable systems. It enlarges the certified stability boundary for these systems and identifies where the model genuinely undergoes a phase transition.

---


### 108. [MaTe: Images Are All You Need for Material Transfer via Diffusion Transformer](https://arxiv.org/abs/2605.15660)

**<font color=#1a73e8>作者：</font>** Nisha Huang, Henglin Liu, Yizhou Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based methods for material transfer rely on image fine-tuning or complex architectures with assistive networks, but face challenges including text dependency, extra computational costs, and feature misalignment. To address these limitations, we propose MaTe, a streamlined diffusion framework that eliminates textual guidance and reference networks. MaTe integrates input images at the token level, enabling unified processing via multi-modal attention in a shared latent space. This design removes the need for additional adapters, ControlNet, inversion sampling, or model fine-tuning. Extensive experiments demonstrate that MaTe achieves high-quality material generation under a zero-shot, training-free paradigm. It outperforms state-of-the-art methods in both visual quality and efficiency while preserving precise detail alignment, significantly simplifying inference prerequisites.

---


### 109. [VAGS: Velocity Adaptive Guidance Scale for Image Editing and Generation](https://arxiv.org/abs/2605.15661)

**<font color=#1a73e8>作者：</font>** Yan Luo, Ahmadou Aidara, Jingyi Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is the primary control over how strongly text semantics move a flow-based sampler, yet standard practice holds its scale fixed across the entire ODE trajectory. This is a fundamental mismatch: early steps are noise-dominated and carry weak semantic signal, while late steps commit image structure and demand stronger directional commitment; more critically, the value of any guidance strength depends on whether the guided velocity is consistent with the model's current dynamics or working against them. We propose \textit{Velocity-Adaptive Guidance Scale} (VAGS), a training-free replacement that multiplies the nominal scale by a bounded factor combining a temporal signal-level term with the cosine similarity between task-relevant velocity fields. For inversion-free editing, VAGS measures the alignment between source- and target-guided velocities, so edit strength at each step reflects local compatibility between preservation and transformation. For generation, VAGS-Gen uses the alignment between unconditional and conditional velocities as the analogous signal. Neither variant requires fine-tuning, auxiliary networks, or extra forward passes, and fixed CFG is recovered as a special case. On PIE-Bench and DIV2K for editing, and COCO17, CUB-200, and Flickr30K for generation, VAGS consistently improves structural fidelity and generation quality over fixed CFG and recent training-free guidance variants. The code is publicly available at this https URL.

---


### 110. [On the Power of Adaptivity for $\varepsilon$-Best Arm Identification in Linear Bandits](https://arxiv.org/abs/2605.15663)

**<font color=#1a73e8>作者：</font>** Arnab Maiti, Yunbei Xu, Kevin Jamieson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the minimax sample complexity of $\varepsilon$-best arm identification in linear bandits. Given a compact action set $\mathcal{X}$ that spans $\mathbb{R}^d$ and an unknown reward vector $\theta\in\mathbb{R}^d$, the goal is to output an arm $\widehat{x}\in\mathcal{X}$ such that $\langle \widehat{x},\theta\rangle \ge \max_{x\in\mathcal{X}} \langle x,\theta\rangle - \varepsilon$ with probability at least $1-\delta$, using as few samples as possible.
First, we present a non-adaptive fixed-design method with sample complexity $\mathcal{O}\!\left(\frac{d\log(1/\delta)}{\varepsilon^2}+\frac{w(\mathcal{X})^2}{\varepsilon^2}\right)$, where $w(\mathcal{X})$ is a Gaussian width term dependent on $\mathcal{X}$, and we prove a matching lower bound $\Omega\!\left(\frac{d\log(1/\delta)}{\varepsilon^2}+\frac{w(\mathcal{X})^2}{\varepsilon^2}\right)$ for all non-adaptive fixed-design methods.
We then turn to adaptive sampling. We raise an important structural question: beyond the canonical basis, are there structured action sets for which adaptivity yields only logarithmic-factor improvements over the optimal non-adaptive rate? We answer in the affirmative for several natural action sets, namely the hypercube, the $\ell_2$ ball, $m$-sets, and multi-task multi-armed bandits.
Finally, we provide the first construction of an action set $\mathcal{X}$ for which adaptivity yields a polynomial-factor improvement over every non-adaptive algorithm. A key ingredient behind this separation is an $\ell_2$-norm estimation subroutine: we design an adaptive algorithm that uses $\mathcal{O}\!\left(\frac{d\log(1/\delta)}{\varepsilon^2}\right)$ samples from the unit $\ell_2$ ball in $\mathbb{R}^d$ and outputs an estimate $\widehat r$ satisfying $|\widehat r-\|\theta\|_2|\le \varepsilon$ with probability at least $1-\delta$, where $\theta$ is the unknown reward vector.

---


### 111. [PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI](https://arxiv.org/abs/2605.15665)

**<font color=#1a73e8>作者：</font>** Keshava Chaitanya, Jahnavi Gundakaram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language model (LLM)-driven conversational agents in enterprise settings requires prompts that are simultaneously correct at launch and resilient to the non-deterministic behavioral drift that characterizes production LLM deployments. Existing prompt optimization frameworks address prompt quality as a one-time compile-time problem, leaving open the equally critical question of how to detect and repair prompt regressions caused by silent LLM behavior changes over time. We present PRISM (Prompt Reliability via Iterative Simulation and Monitoring), a closed-loop framework that treats prompt engineering as a continuous reliability engineering problem rather than a one-time authorship task. PRISM takes as input plain-language agent requirements, a set of configured tools and memory variables, and an initial draft prompt. It automatically generates test cases from requirements, simulates full multi-turn conversations against a platform-faithful LLM environment, evaluates pass/fail using an LLM-as-judge, diagnoses root causes of failures, and surgically repairs the prompt -- iterating until all tests pass. Critically, PRISM is designed to run on a scheduled basis (daily), treating LLM behavioral drift as a first-class reliability concern. We evaluate PRISM across 35 enterprise conversational agents over a three-week deployment period on the this http URL V3 platform. PRISM reduces median prompt authoring time from 2 days to under 30 minutes, achieves 99% production reliability across all evaluated agents, and successfully identifies and repairs production regressions caused by LLM behavioral drift within a 24-hour detection window. Our results suggest that continuous, simulation-driven prompt optimization is both tractable and necessary for reliable enterprise conversational AI at scale.

---


### 112. [ChronoEarth-492K: A Large Scale and Long Horizon Spatiotemporal Hyperspectral Earth Observation Dataset and Benchmark](https://arxiv.org/abs/2605.15666)

**<font color=#1a73e8>作者：</font>** Haozhe Si, Yuxuan Wan, Yuqing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging (HSI) provides dense spectral information for the Earth's surface, enabling material-level understanding of land cover and ecosystem dynamics. Despite recent progress in hyperspectral self-supervised learning (SSL), existing datasets remain temporally shallow, limiting the development of long-horizon spatiotemporal modeling. To address this gap, we introduce ChronoEarth-492K, the first large-scale, temporally calibrated hyperspectral SSL dataset built upon NASA's EO-1 Hyperion mission, the world's longest continuous hyperspectral archive up to date (2001-2017). ChronoEarth-492K comprises 492,354 radiometrically harmonized patches across 185,398 global locations over 17 years, with 28,786 sites containing multi-temporal sequences ($\geq 3$ observations) that enable both short- and long-horizon temporal analysis. Building on this foundation, we establish the ChronoEarth-Benchmark, a unified evaluation suite spanning static, short-horizon, and long-horizon temporal tasks, constructed from six open-source geospatial products covering land cover, crop type, forest dynamics, and soil properties. We further introduce a standardized evaluation protocol and report extensive baseline results across state-of-the-art hyperspectral foundation models. Together, ChronoEarth and benchmark provide the first large-scale, temporally grounded platform for systematic spatiotemporal hyperspectral representation learning.

---


### 113. [VLMs Trace Without Tracking: Diagnosing Failures in Visual Path Following](https://arxiv.org/abs/2605.15672)

**<font color=#1a73e8>作者：</font>** Hyesoo Hong, Minsoo Kim, Wonje Jeung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong performance on multimodal benchmarks, but may still lack robust control over basic visual operations. We study \textit{line tracing}, where a model must follow a selected visual path through successive local continuations. To isolate this ability, we design controlled tracing tasks that introduce nearby competitors while reducing semantic and topological ambiguity such as crossings and overlaps. Across these tasks, even state-of-the-art VLMs frequently lose the target path and switch to nearby alternatives, especially when those alternatives look locally similar to the target. Behavioral interventions and internal analyses indicate that these failures arise from local competition: nearby similar distractors pull the model away from the true continuation. Standard remedies do not remove this bottleneck: model-size scaling provides only limited gains, reasoning partially compensates through costly substitute strategies, and explicit tracing instructions fail to recover stable path following. Finally, tests on tangled-cable scenes and metro maps with richer visual complexity show that the same path-switching failure persists beyond our controlled settings.

---


### 114. [Interaction-Aware Influence Functions for Group Attribution](https://arxiv.org/abs/2605.15675)

**<font color=#1a73e8>作者：</font>** Jaeseung Heo, Kyeongheung Yun, Youngbin Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Influence functions approximate how removing a training example changes a quantity of interest, called the target function, such as a held-out loss. To estimate the influence of a group of examples, the standard practice is to sum the individual influences of its members. However, this sum does not capture how examples jointly affect the target: a pair of examples may be redundant or complementary, but the sum cannot distinguish these cases. We propose an interaction-aware influence function that characterizes how interactions between examples influence the target. By expanding the target to second order around the trained parameters, we obtain an estimator that augments the standard sum with a pairwise interaction term that captures the alignment between two examples' effects on the target. We empirically evaluate our estimator in two settings. First, on six dataset-model pairs spanning logistic regression, MLPs, and ResNet-9, our estimator tracks leave-group-out retraining substantially better than first-order influence across all settings. Second, when used as a greedy selection rule for instruction-tuning data on Llama-3.1-8B, it beats prior influence-based and representation-similarity baselines on five of seven downstream tasks, in a regime where standard influence-based selection underperforms random selection.

---


### 115. [VCG-Bench: Towards A Unified Visual-Centric Benchmark for Structured Generation and Editing](https://arxiv.org/abs/2605.15677)

**<font color=#1a73e8>作者：</font>** Xiaoyan Su, Peijie Dong, Zhenheng Tang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancements in Vision-Language Models (VLMs), a critical gap remains in their ability to handle structured, controllable diagrammatic tasks essential for professional workflows. Existing methods predominantly rely on pixel-based synthesis, which operates in probabilistic pixel spaces and is inherently limited in editability and fidelity. Instead, we propose a new Diagram-as-Code paradigm with symbolic logic that leverages mxGraph Extensible Markup Language (XML) for precise diagram generation and editing. We present VCG-Bench, a unified benchmark for visual-centric \texttt{mxGraph} tasks. VCG-Bench comprises: (1) a taxonomized dataset of 1,449 diverse diagrams spanning 6 domains and 15 sub-domains, (2) a paradigm definition that integrates Generation (Vision-to-Code) and Editability (Code-to-Code), (3) a Tailored Evaluation Protocol employing multi-dimensional metrics such as \texttt{mxGraph} Execution Success Rate, Style Consistency Score (SCS), etc. Experimental results highlight the challenges faced by current State-of-the-Art (SOTA) VLMs in structured fidelity and instruction compliance, reflecting their vision and reasoning capabilities.

---


### 116. [DreamSR: Towards Ultra-High-Resolution Image Super-Resolution via a Receptive-Field Enhanced Diffusion Transformer](https://arxiv.org/abs/2605.15682)

**<font color=#1a73e8>作者：</font>** Qingji Dong, Hang Dong, Mingqin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-trained diffusion models have been extensively adopted for real-world image Super-Resolution because of their powerful generative priors through textual guidance. However, when super-resolving high-resolution images with patch-wise inference strategy, most existing diffusion-based SR methods tend to suffer from over-generation, due to the misalignment between the global prompt from LR image and the incomplete semantic information of local patches during each inference step. On the other hand, most existing methods also failed to generate detailed texture in local patches due to the overemphasis on global generation capabilities in network designs and training strategies. To address this issue, we present DreamSR, a novel SR model that suppresses local over-generation and improves fine-detail synthesis, thereby achieving visually faithful results with ultra-high-quality details. Specifically, we propose a dual-branch MM-ControlNet, where the ControlNet generates local textual feature with patch-level prompts while the pre-trained DiT provides global textual feature with global prompts, thereby mitigating over-generation and ensuring semantic consistency across patches. We also design a comprehensive training strategy with stage-specific data processing pipelines and a Receptive-Field Enhancement strategy, enhancing the model's capability to capture patch information and effectively restore local textures. Extensive experiments demonstrate that DreamSR outperforms state-of-the-art methods, providing high-quality SR results. Code and model are available at this https URL.

---


### 117. [ElasticDiT: Efficient Diffusion Transformers via Elastic Architecture and Sparse Attention for High-Resolution Image Generation on Mobile Devices](https://arxiv.org/abs/2605.15684)

**<font color=#1a73e8>作者：</font>** Kunpeng Du, Haizhen Xie, Sen Lu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Diffusion Transformer (DiT) architecture is the state-of-the-art paradigm for high-fidelity image generation, underpinning models like Stable Diffusion-3 and FLUX.1. However, deploying these models on resource-constrained mobile devices entails prohibitive computational and memory overhead. While efficiency-driven approaches like Linear-DiT and static pruning alleviate bottlenecks, they often incur quality degradation. Unlike cloud environments, mobile constraints require a single-model paradigm that dynamically balances fidelity and latency. We introduce ElasticDiT, which achieves this dynamic trade-off by adjusting spatial compression ratios and DiT block depths. By integrating Shift Sparse Block Attention (SSBA) and a Tiny DWT-Distilled VAE (T-DVAE), ElasticDiT reduces inference latency and memory footprint while maintaining image quality. Experiments confirm that ElasticDiT effectively covers a wide range of fidelity-latency trade-offs within a single set of parameters. By jointly adjusting compression and depth, a single ElasticDiT model can be reconfigured on-the-fly to outperform task-specific baselines. Specifically, our flex lite variant achieves an HPS of 32.87, surpassing the Flux model, while maintaining competitive quality at 84.16 percent average sparsity through SSBA. Furthermore, the plug-and-play T-DVAE provides SD3-level reconstruction with only 1/8x the computational cost of standard VAEs, and Flow-GRPO boosts semantic alignment (GenEval: 66.93 to 73.62). These results demonstrate that ElasticDiT offers a versatile, hardware-adaptive solution that eliminates the need for multiple specialized models, providing a promising path for future high-resolution image generation on mobile devices.

---


### 118. [How to Choose Your Teacher for Fine Grained Image Recognition](https://arxiv.org/abs/2605.15689)

**<font color=#1a73e8>作者：</font>** Oswin Gosal, Edwin Arkel Rios, Augusto Christian Surya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image recognition classifies subcategories such as bird species or car models. While state-of-the-art (SOTA) models are accurate, they are often too resource-intensive for deployment on constrained devices. Knowledge distillation addresses this by transferring knowledge from a large teacher model to a smaller student model. A key challenge is selecting the right teacher, as it heavily impacts student performance. This paper introduces a teacher selection metric, \textbf{Ratio 1-2}, based on teacher prediction ratios. Extensive analysis of over one thousand experiments across 3 students, 8 teachers, and 8 datasets under 4 training strategies demonstrates that our metric improves teacher selection by 18\% over previous methods, enabling small student models to achieve up to 17\% accuracy gains. Experiment codebase is available at: \href{this https URL}{this https URL}.

---


### 119. [FRWKV+: Adaptive Periodic-Position Branch Interaction for Frequency-Space Linear Time Series Forecasting](https://arxiv.org/abs/2605.15690)

**<font color=#1a73e8>作者：</font>** Qingyuan Yang, Dongyue Chen, Da Teng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting is essential for decision making in energy, finance, transportation, and healthcare systems. Recent lightweight forecasting models improve efficiency by operating in transformed or linearized spaces, but two challenges remain in frequency-space forecasting. The real and imaginary streams of complex spectra contain complementary information that is often weakly exchanged, and periodic-position cues can help recurring patterns only when they are reliable for the current dataset and prediction horizon. To address these challenges, we propose FRWKV+, an enhanced FRWKV forecasting model for selective periodic-position branch interaction. FRWKV+ first introduces cross-branch gates that exchange compact contexts between the real and imaginary frequency streams, allowing each stream to modulate the other. It then uses the Adaptive PhaseGate mechanism to extract periodic-position context and generate signed corrections to these gates. An adaptive trust mechanism controls the correction strength at the sample, variable, and channel levels, so periodic-position information is admitted as a reliable correction signal while preserving the efficiency of the FRWKV backbone. External benchmark tables report a separately labeled FRWKV-family selected system for manuscript-level comparison, while mechanism-level claims are based on strict matched-seed FRWKV-family ablations and representative component-level ablations. Under this matched protocol, FRWKV+ achieves the largest MSE winner coverage among the family variants and provides clear gains in selected periodic regimes. Component analysis further supports the usefulness of periodic-position context, signed correction, and adaptive trust in these regimes, while revealing boundary cases where simpler correction rules remain preferable.

---


### 120. [SEED: Targeted Data Selection by Weighted Independent Set](https://arxiv.org/abs/2605.15691)

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Lifeng Guo, Junwen Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection seeks to identify a compact yet informative subset from large-scale training corpora, balancing sample quality against collection diversity. We formulate this problem as a Weighted Independent Set (WIS) on a similarity graph, where nodes represent data samples weighted by influence, and edges connect semantically redundant pairs. This formulation naturally yields subsets that are simultaneously high-quality and diverse. However, two challenges arise in practice: naive node weights fail to distinguish informative signals from gradient noise, and edge construction under heterogeneous domain distributions produces structurally imbalanced graphs that bias selection toward sparse regions. To address these issues, we introduce two principled refinements from a unified graph perspective: (1) \textit{node value calibration} that restricts influence estimation to the bilateral salient subspace to ground node importance in task-relevant signals rather than surface-level statistics; (2) \textit{local scale normalization} that adapts edge thresholds to local neighborhood density, mitigating graph imbalance induced by cross-domain distribution shifts. Together, these components yield a robust and scalable data selection pipeline dubbed SEED. We further construct \texttt{Honeybee-Remake-SEED-200K}, a compact multimodal dataset curated by SEED. Extensive experiments show that SEED consistently outperforms state-of-the-art methods on instruction tuning, visual instruction tuning, and semantic segmentation across diverse model families.

---


### 121. [Tighter Regret Bounds for Contextual Action-Set Reinforcement Learning](https://arxiv.org/abs/2605.15692)

**<font color=#1a73e8>作者：</font>** Zijun Chen, Zihan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study episodic reinforcement learning with fixed reward and transition functions, but with episode-dependent admissible action sets that are observed at the start of each episode. Performance is measured by cumulative regret against the episode-wise optimal value, $\sum_{k=1}^K [V^{*,M^k} - V^{\pi^k,M^k}]$, where $M^k$ represents the action context in the $k$-th episode. We show that the MVP algorithm naturally extends to this framework and enjoys strong theoretical guarantees. In particular, we establish a minimax regret bound of $\widetilde{O}(\sqrt{SAH^3K\log L})$ for adversarial contexts, where $L$ denotes the number of possible contexts. This result implies a regret bound of $\widetilde{O}(\sqrt{SAH^3K})$ for stochastic contexts. We further translate the stochastic regret guarantee into a sample complexity bound of $\widetilde{O}(SAH^3/\epsilon^2)$ for a fixed context distribution.
In addition, we derive a gap-dependent regret bound of \[ \widetilde O\left( \inf_{p\in [0,1)} \left( \frac{1}{\Delta_{\min}^{p}} + pK\Delta_{\min}^{p} \right)\log K \cdot \mathrm{poly}(S,A,H) \right), \] where $\Delta_{\min}^{p}$ is the global $p$-trimmed positive-gap floor over suboptimal $(h,s,a)$ triples. This bound can substantially improve upon the minimax rate when the relevant suboptimality gaps are large.

---


### 122. [Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices](https://arxiv.org/abs/2605.15694)

**<font color=#1a73e8>作者：</font>** Alexander Gräfe, Ding Huo, Johannes Berger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer models are rapidly becoming a cornerstone of modern Internet of Things (IoT) applications, yet their computational and memory demands far exceed the capabilities of a single typical ultra-low-power IoT device. We present CATS, a framework for distributed transformer inference on ultra-low-power wireless devices, enabling multiple devices to collaboratively execute models far larger than what a single device can sustain. At its core, CATS is a communication-aware distributed transformer inference scheme co-designed across transformer partitioning, wireless communication and training. It employs SomeGather, a new pruned communication primitive that selectively broadcasts activation columns to reduce communication bandwidth and RAM usage without sacrificing model accuracy. Building on SomeGather, we design a partitioning method that exploits this primitive for efficient model parallelism. To cope with unreliable wireless communication, CATS employs message-dropout during training, which mimics packet losses and yields models that are robust to message loss during inference. In real-world experiments, we show that CATS brings distributed transformer inference to ultra-low-power wireless devices for the first time, with deployments on up to 16 devices that collaboratively execute transformer models up to 14 times larger than what a single device can run.

---


### 123. [Distributed Zeroth-Order Policy Gradient for Networked Multi-agent Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2605.15697)

**<font color=#1a73e8>作者：</font>** Pengcheng Dai, He Wang, Dongming Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study a networked multi-agent reinforcement learning (NMARL) problem with human feedback in an infinite-horizon setting, where agents interact over an underlying network with localized state dependencies and aim to collaboratively maximize the average discounted return. Existing approaches with preference feedback are primarily developed for single-agent settings and rely on centralized training, which limits their scalability and applicability to large-scale networked multi-agent systems. To address this, we introduce a novel human feedback mechanism based on spatiotemporally truncated trajectories, defined as $H$-horizon trajectory pairs aggregated over each agent's $\kappa$-hop neighborhood. Building on this, we develop a distributed zeroth-order policy gradient algorithm, where each agent estimates its local policy gradient using human preference feedback generated from both the current joint policy and a perturbed joint policy drawn from zero-mean Gaussian distribution. Specifically, the algorithm is fully distributed, as the feedback received by each agent depends solely on the state-action information within its $\kappa$-hop neighborhood and does not require explicit reward signals or centralized control. We further rigorously establish that the proposed algorithm converges to an $\epsilon$-stationary point with polynomial sample complexity. Finally, simulation results in a stochastic GridWorld environment and a predator-prey environment further demonstrate that the effectiveness and scalability of the proposed algorithm in achieving collaborative optimization based solely on human preference feedback.

---


### 124. [AGOP-IxG: A Gradient Covariance Filter for Local Feature Attribution on Tabular Data, with a Controlled Benchmark](https://arxiv.org/abs/2605.15700)

**<font color=#1a73e8>作者：</font>** Raj Kiran Gupta Katakam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated machine learning pipelines increasingly produce models whose predictions must be explained to end users, auditors, and downstream decision systems. The most widely used feature attribution methods (SHAP, Integrated Gradients, LIME) are typically chosen by convention rather than measured fidelity, because rigorous evaluation is impeded by the absence of ground-truth attribution on real data. We propose AGOP-IxG, a fast per-sample attribution method for tabular classifiers that pre-multiplies the per-sample gradient by a top-$K$ rank-truncated Average Gradient Outer Product matrix, and evaluate it against four widely-used baselines on a controlled tabular benchmark designed for AutoML practitioners. In Part 1, we construct three synthetic multi-class tabular tasks (linear, sparse nonlinear, interaction-based) where ground-truth attribution per sample is analytically or numerically derivable, and compare five methods: AGOP-IxG, SHAP (DeepExplainer), Integrated Gradients, InputXGradient, and LIME. AGOP-IxG leads on Spearman rank correlation and noise feature mass on all three synthetic datasets, and on top-$k$ precision on the interaction dataset. Across all settings, AGOP-IxG is approximately $350\times$ to $1{,}650\times$ faster than SHAP. In Part 2, we evaluate global faithfulness on Adult Income and Credit Card Default using the ROAR protocol; the methods cluster within $\sim 1.7\%$ relative AUC, consistent with AGOP-IxG being optimized for per-sample local attribution rather than global feature ranking.

---


### 125. [H-Mem: A Novel Memory Mechanism for Evolving and Retrieving Agent Memory via a Hybrid Structure](https://arxiv.org/abs/2605.15701)

**<font color=#1a73e8>作者：</font>** Jiawei Yu, Yixiang Fang, Xilin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory data are ubiquitous in Large Language Model (LLM)-based agents (e.g., OpenClaw and Manus). A few recent works have attempted to exploit agents'memory for improving their performance on the question-answering (QA) task, but they lack a principled mechanism for effectively modeling how memory data evolves over time and retrieving memory data effectively, leading to poor performance in memory utilization. To fill this gap, we present H-Mem, a novel memory mechanism via a hybrid structure that can not only effectively model the evolution of agent memory over a long period of time, but also provide an efficient memory retrieval approach. Particularly, H-Mem builds a temporal and semantic tree structure that allows the short-term memory data to evolve progressively into long-term memory data, where the latter provides summarized information about the former, while simultaneously constructing a knowledge graph to capture the relationships between entities in memory. Moreover, it offers an effective memory retrieval approach by exploiting the hybrid structure of the tree and graph structures. Extensive experiments on three agent memory benchmarks show that H-Mem achieves state-of-the-art performance on the QA task.

---


### 126. [3D Segmentation Using Viewpoint-Dependent Spatial Relationships](https://arxiv.org/abs/2605.15708)

**<font color=#1a73e8>作者：</font>** Ayaka Nanri, Klara Reichard, Mert Kiray 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D datasets and multimodal models have greatly improved natural language 3D scene understanding. However, most 3D referring segmentation methods do not explicitly represent the observer viewpoint, making spatial relations such as "left," "right," "front," and "behind" ambiguous and difficult to evaluate. We introduce a viewpoint-aware 3D referring segmentation dataset containing 220k benchmark samples, and scalable to tens of millions of viewpoint-conditioned samples through dense viewpoint sampling. In this dataset, target objects can only be identified through observer-centric spatial relations, making viewpoint-conditioned grounding necessary. We construct the benchmark by leveraging camera poses to automatically annotate observer-centric relations (left/right, front/behind) together with viewpoint-independent relations (above/under). Using this benchmark, we evaluate several existing 3D large multimodal models in a zero-shot setting and find that current models struggle with viewpoint-dependent spatial instructions. We further study how explicit viewpoint information can be incorporated into 3D large multimodal models. We introduce a viewpoint representation that encodes camera poses and conditions the model on the observation viewpoint, improving segmentation accuracy on viewpoint-dependent relations and increasing mIoU from 0.30 to 0.47 compared to a model without viewpoint conditioning. The dataset, code, and trained models will be made publicly available upon acceptance.

---


### 127. [Bidirectional Fusion Guided by Cardiac Patterns for Semi-Supervised ECG Segmentation](https://arxiv.org/abs/2605.15722)

**<font color=#1a73e8>作者：</font>** Jeonghwa Lim, Minje Park, Sunghoon Joo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate delineation of electrocardiogram (ECG), the segmentation of meaningful waveform features, is crucial for cardiovascular diagnostics. However, the scarcity of annotated data poses a significant challenge for training deep learning models. Conventional semi-supervised semantic segmentation (SemiSeg) methods primarily focus on consistency from unlabeled data, underutilizing the information exchange possible between labeled and unlabeled sets. To address this, we introduce CardioMix, a framework built on a bidirectional CutMix strategy guided by cardiac patterns for ECG segmentation. This approach enriches the labeled set with realistic variations from unlabeled data while simultaneously applying stronger supervisory signals to the unlabeled set, as the cardiac pattern-guided mixing ensures all augmented samples remain physiologically meaningful. Our framework is designed as a plug-and-play module, demonstrating high compatibility with various SemiSeg algorithms. Extensive experiments on SemiSegECG, a public multi-dataset benchmark for ECG delineation, demonstrate that CardioMix consistently outperforms existing CutMix-based fusion strategies across diverse datasets and labeled ratios as a plug-and-play module compatible with various SemiSeg algorithms.

---


### 128. [Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR](https://arxiv.org/abs/2605.15726)

**<font color=#1a73e8>作者：</font>** Chanuk Lee, Sangwoo Park, Minki Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable paradigm for improving the reasoning capabilities of large language models. However, its effectiveness is fundamentally limited by exploration: the policy can only improve on trajectories it has already sampled. While increasing the number of rollouts alleviates this issue, such brute-force scaling is computationally expensive, and existing approaches that modify the optimization objective provide limited control over what is explored. In this work, we propose NudgeRL, a framework for structured and diversity-driven exploration in RLVR. Our approach introduces Strategy Nudging, which conditions each rollout on lightweight, strategy-level contexts to induce diverse reasoning trajectories without relying on expensive oracle supervision. To effectively learn from such structured exploration, we further propose a unified objective, which decomposes the reward signal into inter- and intra-context components and incorporates a distillation objective to transfer discovered behaviors back to the base policy. Empirically, NudgeRL outperforms standard GRPO with up to 8 times larger rollout budgets, while outperforming oracle-guided RL baseline on average across five challenging math benchmarks. These results demonstrate that structured, context-driven exploration can serve as an efficient and scalable alternative to both brute-force rollout scaling and feasibility-oriented methods based on privileged information. Our code is available at this https URL.

---


### 129. [DecomPose: Disentangling Cross-Category Optimization Contention for Category-Level 6D Object Pose Estimation](https://arxiv.org/abs/2605.15728)

**<font color=#1a73e8>作者：</font>** Yifan Gao, Lu Zou, Zhangjin Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level 6D object pose estimation is typically formulated as a multi-category joint learning problem with fully shared model parameters. However, pronounced geometric heterogeneity across categories entangles incompatible optimization signals in shared modules, resulting in gradient conflicts and negative transfer during training. To address this challenge, we first introduce gradient-based diagnostics to quantify module-level cross-category contention. Building on results of diagnostics, we propose DecomPose, a difficulty-aware decomposition framework that mitigates optimization contention via: (1) difficulty-aware gradient decoupling, which groups categories using a data-driven difficulty proxy and routes each instance to a group-specific correspondence branch to isolate incompatible updates; and (2) stability-driven asymmetric branching, which assigns higher-capacity branches to structurally simple categories as stable optimization anchors while constraining complex categories with lightweight branches to suppress noisy updates and alleviate negative transfer. Extensive experiments on REAL275, CAMERA25, and HouseCat6D demonstrate that DecomPose effectively reduces cross-category optimization contention and delivers superior pose estimation performance across multiple benchmarks.

---


### 130. [BARRIER: Bounded Activation Regions for Robust Information Erasure](https://arxiv.org/abs/2605.15737)

**<font color=#1a73e8>作者：</font>** Jan Miksa, Patryk Krukowski, Przemysław Spurek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has reached a critical bottleneck. As traditional weight-space interventions focus primarily on erasing targeted concepts, they often fail to prevent the unintended suppression of other significant representations. This leads to substantial collateral damage, with essential knowledge being forgotten, because these methods lack formal mathematical guarantees for the preservation of neutral concepts. To avoid degradation, they are frequently forced into conservative updates. We propose BARRIER (Bounded Activation Regions for Robust Information Erasure), a paradigm-shifting framework that shifts the locus of intervention from static model weights to the dynamic geometry of hidden-layer activations. Unlike existing methods, BARRIER employs Interval Arithmetic (IA) on SVD-based projections of the activation space to encapsulate the specific target region within a bounding hypercube. By driving unlearning updates exclusively within this forget interval and mathematically bounding the model response on the complement, we ensure rigorous protection of the retain distribution. This geometric construction transforms the preservation of knowledge from an empirical heuristic into a formal optimization target with a probabilistic tail bound on functional drift. Crucially, this stability permits highly aggressive unlearning updates within the forget region. Empirical evaluations demonstrate that BARRIER matches state-of-the-art trade-offs across classifiers and diffusion models, maximizing targeted concept erasure while safeguarding the integrity of all other representations. Our code is available at this https URL.

---


### 131. [HyperDiT: Hyper-Connected Transformers for High-Fidelity Pixel-Space Diffusion](https://arxiv.org/abs/2605.15741)

**<font color=#1a73e8>作者：</font>** Yu He, Lichen Ma, Zipeng Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models bypass the reconstruction bottleneck of Variational Autoencoders (VAEs) but face a fundamental "granularity dilemma": capturing global semantics favors large patch scales, while generating high-fidelity details demands fine-grained inputs. To address this issue, we propose HyperDiT, a unified framework establishing Hyper-Connected Cross-Scale Interactions to bridge the semantic and pixel manifold. Diverging from injecting semantics by AdaLN, HyperDiT utilizes Cross-Attention mechanisms, enabling fine-grained tokens to query multi-level semantic anchors globally. To resolve the spatial mismatch during multi-scale interactions, we introduce Scale-Aware Rotary Position Embedding (SA-RoPE) to ensure precise geometric alignment among tokens of varying patch sizes. Furthermore, we incorporate Registers to learn the dense semantics from a pretrained Visual Foundation Model (VFM), effectively reducing generation hallucination and artifacts. Extensive experiments demonstrate that HyperDiT achieves state-of-the-art (SoTA) FID of $\mathbf{1.56}$ on ImageNet $256\times256$ directly within the pixel space. By combining the fine-grained stream with semantic guidance, HyperDiT offers a superior paradigm for high-fidelity pixel generation.

---


### 132. [Separating Acute Psychological Stress from Physical Exertion in Biometric Signals](https://arxiv.org/abs/2605.15756)

**<font color=#1a73e8>作者：</font>** Esther Bosch  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Acute psychological stress occurs in a wide range of everyday contexts, including transportation, occupational settings, and physical activity, where its reliable detection could enable adaptive system responses and support human well-being. A persistent challenge in automated stress recognition is disentangling the biometric signatures of acute psychological stress from those of concurrent physical exertion. This study examined how five physiological signals (tonic electrodermal activity, trapezius electromyography, heart rate, heart rate variability, and respiration rate) respond to cognitive stress and physical activity, independently and in combination. Nineteen participants completed a 2x3 within-subjects design in which acute psychological stress was induced via an n-back arithmetic task combined with social pressure and financial reward, across three activity conditions: idle sitting, walking, and stationary cycling. Multilevel linear mixed models and repeated-measures ANOVA were used to decompose main effects and interactions for each sensor. Tonic electrodermal activity showed a robust, additive response to both cognitive stress (r=0.48) and physical exertion (r=0.67), with no interaction, making it the most promising candidate for stress detection during physical activity. Heart rate and trapezius electromyography were driven almost exclusively by physical exertion, with no reliable sensitivity to the stress task. RMSSD was strongly suppressed by physical activity and showed only marginal sensitivity to cognitive load. Respiration rate was dominated by physical activity, with no reliable stress effect in the primary analysis. These findings provide a sensor-specific hierarchy for real-world stress detection and highlight tonic electrodermal activity as the most informative channel when cognitive stress must be identified in physically active populations.

---


### 133. [Learn2Splat: Extending the Horizon of Learned 3DGS Optimization](https://arxiv.org/abs/2605.15760)

**<font color=#1a73e8>作者：</font>** Naama Pearl, Stefano Esposito, Haofei Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) optimization is most commonly performed using standard optimizers (Adam, SGD). While stable across diverse scenes, standard optimizers are general-purpose and not tailored to the structure of the problem. In particular, they produce independent parameter updates that do not capture the structural and spatial relationships within a scene, leading to inefficient optimization and slow convergence. Recent works introduced learned optimizers that predict correlated updates informed by inter-parameter and inter-Gaussian dependencies. However, these methods are trained for a fixed number of optimization iterations and rely on manually scheduled learning rates to avoid degradation. In this paper, we introduce a learned optimizer for 3DGS that avoids degradation over extended optimization horizons without auxiliary mechanisms. To enable this, we propose a meta-learning scheme that extends the optimization horizon via a checkpoint buffer and an optimizer rollout strategy, combined with an architecture that encodes gradient scale information in its latent states. Results show improved early novel view synthesis quality while remaining stable over long horizons, with zero-shot generalization to unseen reconstruction settings. To support our findings, we introduce the first unified framework for training and evaluating both learned and conventional optimizers across sparse and dense view settings. Code and models will be released publicly. Our project page is available at this https URL .

---


### 134. [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](https://arxiv.org/abs/2605.15761)

**<font color=#1a73e8>作者：</font>** Hosna Oyarhoseini, Jimmy Lin, Amir-Hossein Karimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluation leaderboards such as LMArena play a central role in benchmarking large language models by aggregating pairwise human preferences into model rankings, yet the robustness of these rankings remains poorly understood. We present a unified perturbation framework for analyzing Bradley-Terry leaderboards under structured data modifications using influence-based approximations. Our framework studies three match-level perturbations -- Drop, Add, and Flip -- together with player removal, and evaluates their effects on top-k membership, global ranking consistency via Kendall's tau, and confidence-interval-based uncertainty. Across Chatbot Arena and six additional pairwise-comparison datasets, we show that modern leaderboards are non-robust across all three objectives: sub-1% targeted perturbations can change the top-ranked model, degrade Kendall's tau, and alter confidence intervals. Beyond robustness auditing, we show that the same influence scores enable efficient targeted perturbations, promoting or demoting specific models and reducing target-model uncertainty with fewer actions than previous manipulation and active-sampling baselines. By summarizing these effects with normalized dataset-level robustness scores, our framework provides a practical and helpful tool for auditing leaderboard stability and motivating more robust evaluation protocols.

---


### 135. [ALSO: Adversarial Online Strategy Optimization for Social Agents](https://arxiv.org/abs/2605.15768)

**<font color=#1a73e8>作者：</font>** Xiang Li, Liping Yi, Mingze Kong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social simulation provides a compelling testbed for studying social intelligence, where agents interact through multi-turn dialogues under evolving contexts and strategically adapting opponents. Such environments are inherently non-stationary, requiring agents to dynamically adjust their strategies over time. However, most Large Language Model (LLM) based social agents rely on static personas, while existing approaches for enhancing social intelligence, such as offline reinforcement learning or external planners, are ill-suited to these settings, typically assuming stationarity and incurring substantial training overhead. To bridge this gap, we propose \textbf{ALSO} (\textbf{A}dversarial on\textbf{L}ine \textbf{S}trategy \textbf{O}ptimization), the first framework for online strategy optimization in multi-agent social simulation. ALSO advances social adaptation through two key contributions. (1) ALSO formulates multi-turn interaction as an adversarial bandit problem, where combinations of static personas and dynamic strategy instructions are treated as arms, providing a principled solution to non-stationarity without relying on environmental stability assumptions. (2) To predict rewards and generalize sparse feedback in multi-turn dialogues, ALSO introduces a lightweight neural surrogate to predict rewards from interaction histories, enabling sample-efficient exploration and continuous online adaptation. Experiments on the Sotopia benchmark demonstrate that ALSO consistently outperforms static baselines and existing optimization methods in dynamic environments, validating the effectiveness of adversarial online strategy optimization for building robust social agents.

---


### 136. [Beyond Controlled Noise: Achieving Symmetric FHE through Dynamic Position Shifting](https://arxiv.org/abs/2605.15774)

**<font color=#1a73e8>作者：</font>** Mostefa Kara  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional Fully Homomorphic Encryption (FHE) schemes often suffer from prohibitive computational overhead and complex noise management. In this paper, we propose a novel symmetric FHE through a mechanism of plaintext fragmentation and dynamic interposition. Our approach is built upon a modular encryption foundation, c = mk + rp, which is naturally additive but typically limited by exponential noise growth during multiplication. To resolve this, we introduce an interposition framework where the plaintext is partitioned into multiple fragments across distinct logical positions. We introduce a dual-regulator system to govern the multiplication process; exponent regulators (t_i) redirect the product of fragments to a new target position, preventing the accumulation of secret key exponents, while coefficient regulators (d_i) normalize the resulting scalars. Security is established through a binding mechanism where exponents and coefficients are mutually dependent, shielding the secret key k from algebraic manipulation and substitution attacks.

---


### 137. [Continual Learning of Domain-Invariant Representations](https://arxiv.org/abs/2605.15775)

**<font color=#1a73e8>作者：</font>** Pascal Janetzky, Tobias Schlagenhauf, Stefan Feuerriegel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) aims to train models sequentially over multiple domains without forgetting previously learned knowledge. However, existing CL methods optimize for in-domain performance and are therefore prone to learning spurious, domain-specific cues (``shortcut learning''), which limits generalization to unseen domains after deployment. In this paper, we address this limitation through continual learning of domain-invariant representation. We introduce a broad class of CL methods that sequentially learn representations capturing invariant structures across domains. Our methods are motivated by the observation that such invariant structures often preserve the underlying causal mechanisms, which can reduce the risk of overfitting to domain-specific cues and thus offer better out-of-domain generalization. Our proposed CL methods combine replay-based training with a tailored sequential invariance alignment to learn -- and preserve -- invariant structures over time. We evaluate our methods under a deployment-oriented protocol that measures performance on unseen target domains. Across six benchmark and real-world datasets spanning vision, medicine, manufacturing, and ecology, our methods consistently outperform existing CL baselines in terms of generalization to unseen target domains. As an ablation, we further show that naïve extensions of sequential training with existing domain-invariant representation learning (DIRL) methods provide only limited benefits. To the best of our knowledge, this is the first work to develop domain-invariant representation methods for CL.

---


### 138. [Grokking as Structural Inference: Transformers Need Bayesian Lottery Tickets](https://arxiv.org/abs/2605.15787)

**<font color=#1a73e8>作者：</font>** Kai Hidajat, Solden Stoll, Joseph An  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why does a Transformer that has memorized its training set wait thousands of steps before it generalizes? Existing accounts locate this delay in norm minimization, feature emergence, or the late discovery of sparse subnetworks. These explanations capture important parts of the transition, but ignore a constraint unique to attention-based models: if attention discards an informative token, no bounded downstream computation can recover it. We formalize attention as an implicit Bayesian posterior over the task dependency graph and prove that generalization requires two separable conditions: a familiar Goldilocks bound on MLP capacity, coinciding with norm-based theories of grokking, and a novel Bayesian structural condition requiring attention to place sufficient mass on every informative token. This decoupling explains delayed generalization as delayed structural inference. Early in training, the MLP memorizes through unaligned features, drives the cross-entropy loss near zero, and thereby starves attention of structural gradient. Weight decay must then erode memorization before the missing graph becomes learnable, yielding the known inverse-weight-decay delay, which we derive as a structural waiting time. We then prove that this explaining-away delay can be bypassed by a KL-based structural intervention, yielding an inverse-intervention-strength scaling law for the grokking time. Experiments on algorithmic sequence tasks isolate structure from capacity and show that this Bayesian ticket matches or outperforms lottery-ticket transfer.

---


### 139. [Learning Context-conditioned Gaussian Overbounds for Convolution-Based Uncertainty Propagation](https://arxiv.org/abs/2605.15789)

**<font color=#1a73e8>作者：</font>** Ruirui Liu, Xuejie Hou, Yiping Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is essential in safety-critical settings--from autonomous driving to aviation, finance, and health--where decisions must rely on conservative bounds rather than point estimates. Predictor-level intervals (e.g., from quantile regression, conformal prediction, variance networks, or Bayesian models) generally do not compose: adding two per-variable intervals need not yield a valid interval for their sum or preserve coverage. In aviation, Gaussian overbounding replaces complex error distributions with a conservative Gaussian whose tails dominate the truth, so conservatism propagates through linear operations. Yet classical overbounds are global, often overly conservative, and hard to adapt to feature-conditioned errors. We propose a unified learning framework that trains neural networks to produce context-aware Gaussian overbounds--mean and scale--with provable conservatism on a finite quantile grid and, under three explicit regularity assumptions, continuous-tail conservatism on a certified interval. Our overbounding loss enforces conservativeness at selected quantiles while penalizing distributional distance with a Wasserstein-style term. The learned bounds support conservative linear-combination and convolution analysis on the enforced grid, and on the certified interval when assumptions hold, while being less redundant than traditional methods. We provide a scoped analysis of discrete-to-continuous conservatism and compact-domain objective regularity, and validate on synthetic data and real-world datasets, including multipath, ionospheric, and tropospheric residual errors. Across these settings, the method yields tighter bounds while maintaining conservatism on the enforced grid and in experiments. The framework is modality-agnostic and applicable to learning systems that require conservative, feature-conditioned uncertainty estimates in dynamic environments.

---


### 140. [ForMaT: Dataset for Visually-Grounded Multilingual PDF Translation](https://arxiv.org/abs/2605.15794)

**<font color=#1a73e8>作者：</font>** Michał Ciesiółka, Dawid Wiśniewski, Adrian Charkiewicz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ForMaT (Format-Preserving Multilingual Translation), a parallel corpus of 3,956 PDFs across 15 language pairs that preserves original layout metadata proposed for multimodal machine translation. To ensure structural diversity in the dataset, we employ K-Medoids sampling over 45 geometric features, capturing complex elements like nested tables and formulas to focus only on visually diverse PDF documents. Our evaluation reveals that current MT systems struggle with spatial grounding and geometric synchronization, often losing the link between text and its visual context. ForMaT provides a benchmark for developing layout-aware translation models that integrate visual and textual context for high-fidelity document reconstruction.

---


### 141. [Cross-Modal Registration Between 3D and 2D Fingerprints via Pose-Aware Unwrapping and Point-Cloud Fusion](https://arxiv.org/abs/2605.15796)

**<font color=#1a73e8>作者：</font>** Xiongjun Guan, Jianjiang Feng, Jie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) fingerprints preserve global finger geometry and local ridge structure while avoiding contact-induced deformation, but they remain difficult to integrate with legacy two-dimensional (2D) fingerprint systems. This paper addresses the intermediate stage between 3D acquisition and cross-modal matching, and presents a unified framework for 3D fingerprint preprocessing and registration across contactless and contact-based 2D modalities. The framework combines four components: 1) a nonparametric visualization and unwrapping method that converts a 3D fingerprint point cloud into a rolled-equivalent 2D representation without relying on a global finger-shape model; 2) a point-cloud fusion pipeline that registers and mosaics multiple partial 3D captures into a more complete fingerprint model; 3) an ellipse-based pose normalization method for canonical finger alignment; and 4) a pose-aware cross-modal registration strategy that improves compatibility between 3D fingerprints and both contactless and contact-based 2D fingerprints. Experiments on a self-collected multimodal fingerprint database containing 150 fingers show that the proposed framework achieves ridge-level 3D registration accuracy, robust pose estimation, and consistent gains in 2D compatibility. In particular, the 3D fusion error is concentrated around 0.09 mm, contactless 2D--3D registration reaches ridge-scale projection accuracy, and pose-aware unwrapping improves genuine matching scores relative to generic 3D unwrapping. These results support the use of 3D fingerprints as an effective geometric bridge across heterogeneous fingerprint modalities.

---


### 142. [From Gridworlds to Warehouses: Adapting Lightweight One-shot Multi-Agent Pathfinding for AGVs](https://arxiv.org/abs/2605.15799)

**<font color=#1a73e8>作者：</font>** Hiroki Nagai, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent pathfinding (MAPF) under one-shot planning is a core component of warehouse automation, yet classical formulations typically assume four-connected 2D grids with unit-time moves in four directions. To fill reality gaps while still being trackable with discrete combinatorial search, this work proposes a more practical counterpart tailored to differential-drive AGVs. We term this multi-agent warehouse pathfinding (MAWPF), featured with four constraints: (i) agent actions are restricted to straight motion and in-place rotation; (ii) rotations require multi-step costs; (iii) acceleration and deceleration are considered, and; (iv) follower collisions are prohibited to prevent rear-end crashes. To solve MAWPF efficiently, we adapt representative suboptimal MAPF algorithms-PP, LNS2, PIBT, and LaCAM-and conduct comprehensive benchmarking. Our experiments reveal that PP and LNS2 struggle to solve instances with many agents, while PIBT-based approaches achieve preferable scalability with increased solution cost. We believe that these constitute an important step toward adapting classical gridworld MAPF to operational warehouse setups.

---


### 143. [Embedding-perturbed Exploration Preference Optimization for Flow Models](https://arxiv.org/abs/2605.15803)

**<font color=#1a73e8>作者：</font>** Sujie Hu, Chubin Chen, Jiashu Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements have established Reinforcement Learning (RL) as a pivotal paradigm for aligning generative models with human intent. However, group-based optimization frameworks (e.g., GRPO) face a critical limitation: the rapid decay of intra-group variance. As the distinctiveness among samples within a group diminishes, the variance approaches zero. This eliminates the very learning signal required for optimization, rendering the process unstable and forcing the policy into premature stagnation or reward hacking. Existing strategies, such as varying the initial noise or increasing group sizes, often fail to address this fundamental issue, resulting in training instability or diminishing returns. To overcome these challenges, we propose $\textbf{Embedding-perturbed Exploration Preference Optimization (}E^2\textbf{PO)}$, a novel framework that sustains optimization through embedding-level perturbation. Our method introduces structured, embedding-level perturbations within sample groups, guaranteeing a robust variance that preserves the discriminative signal throughout the training process. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art baselines, achieving a more faithful alignment with human preference.

---


### 144. [Security Analysis of a Communication Protocol: MQTT](https://arxiv.org/abs/2605.15804)

**<font color=#1a73e8>作者：</font>** Ricardo Venâncio, Clarisse Sousa, Filipe Duarte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper analyzes the security of the Message Queuing Telemetry Transport (MQTT) protocol in the context of the Internet of Things (IoT). The main objective consists of identifying vulnerabilities and proposing security improvements. Adopting a hybrid methodology, a theoretical review was combined with an experimental demonstration in a simulated Smart Home environment. Eavesdropping, Tampering, Denial of Service (DoS), and Brute Force attacks were executed and analyzed. The results evidenced critical risks due to the absence of robust encryption and authentication. Finally, mitigation strategies and best practices are proposed to strengthen MQTT implementations.

---


### 145. [Martingale Neural Operators: Learning Stochastic Marginals via Doob-Meyer Factorization](https://arxiv.org/abs/2605.15806)

**<font color=#1a73e8>作者：</font>** Kai Hidajat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators excel as deterministic surrogates, but inevitably collapse to the conditional mean when applied to stochastic PDEs, discarding the variance and tail structure upon which uncertainty quantification depends. Recovering this structure typically requires Monte Carlo rollouts or grafted generative models, both of which surrender the one-shot efficiency and resolution invariance that define the operator paradigm. To resolve this, we draw on the Doob-Meyer theorem, which establishes that any semimartingale fundamentally decomposes into a predictable drift and an unpredictable, zero-mean martingale. Translating this theorem into an architectural prior, we introduce the Martingale Neural Operator (MNO). MNO maps an initial condition directly to the conditional mean and covariance of the terminal law, parameterized by a drift-like mean and a low-rank factor $B_\phi$ with $B_\phi^\top B_\phi$ positive semi-definite by construction. For our experiments, we use a Gaussian residual instantiation. Across 1D SPDEs, rough volatility, and 2D operator tasks, MNO reduces Wasserstein distance by up to $120\times$ on $\phi^4$ field theory and $68\times$ on stochastic Burgers, evaluating $\sim 3\times$ faster than a conditional diffusion baseline at matched wall-clock training budgets. On 2D tasks, MNO is comparable to FNO on zero-shot resolution transfer and turbulent flow, while quasi-deterministic systems such as Gray-Scott remain a failure mode.

---


### 146. [Toward Natural and Companionable Virtual Agents via Cross-Temporal Emotional Modeling](https://arxiv.org/abs/2605.15812)

**<font color=#1a73e8>作者：</font>** Feier Qin, Xiao Li, Yi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in foundation models have enabled conversational agents that aim for sustained companionship rather than mere task completion. Yet most still remain unable to support natural, long-term companion-like interactions, resulting in experiences that feel episodic and inauthentic. We argue that current agents overlooked cross-temporal modeling of agents' social behaviors and internal emotions: generated behaviors rarely influence an agent's emotional state, and emotional states seldom shape subsequent behaviors. We present Cross-Temporal Emotion Modeling (CTEM), a framework that links long-term behavioral history to moment-to-moment emotional expression. CTEM establishes a closed loop where past experiences update an evolving emotional state; this state conditions immediate interactions; and user feedback continually revises both memory and emotional state, enabling reflection and anticipation. We instantiate CTEM as Auri, a companion agent on an instant-messaging platform, and report a 21-day in-the-wild study showing that CTEM shows improvements in perceived naturalness, coherence, and emotional harmony.

---


### 147. [Which Moments Matter? Heuristics of Remembered Travel Experience in Public Transport](https://arxiv.org/abs/2605.15817)

**<font color=#1a73e8>作者：</font>** Esther Bosch, Klas Ihme, Stefan Bohmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how travelers form overall evaluations of public transport journeys is critical for improving travel satisfaction and encouraging sustainable mode choice. While travel satisfaction is discussed to influence attitudes and future behavior, the cognitive rules by which moment-to-moment experiences are aggregated into retrospective evaluations remain poorly understood in transport research. Drawing on psychological theories of experienced and remembered utility, this study investigates which temporal aggregation heuristics best predict post-trip travel satisfaction.
Using a smartphone-based experience sampling approach, we collected high-frequency on-trip experience ratings and post-trip evaluations for 2576 real-world public transport trips across three German cities. Travel experience was assessed every five minutes during trips using a multi-item scale, allowing direct comparison of competing aggregation rules, including mean experience, peak-end, minimum-end, final moment, and trip duration. Multilevel regression models were estimated to evaluate the explanatory power of each heuristic.
Results show that retrospective travel satisfaction is best predicted by a Minimum-End heuristic, combining the most negative moment of the journey and the final experience. Models based on mean experience, peak-end rules, final moment alone, or trip duration performed substantially worse. This pattern indicates that both negative extremes and the final phase of a journey independently contribute to remembered evaluations, rather than overall satisfaction reflecting an average of momentary experiences.
The results have important implications for theory and practice, suggesting that targeted interventions at critical negative moments and at trip endings may yield substantial improvements in remembered satisfaction and, ultimately, support shifts toward sustainable mobility.

---


### 148. [Intrinsic Wasserstein Rates for Score-Based Generative Models on Smooth Manifolds](https://arxiv.org/abs/2605.15822)

**<font color=#1a73e8>作者：</font>** Guoji Fu, Taiji Suzuki, Wee Sun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based generative models are trained in high-dimensional ambient spaces, yet many data distributions are supported on low-dimensional nonlinear structures. We prove that, for compact $d$-dimensional smooth manifolds $\mathcal{M} \subset [0,1]^D$ with $d > 2$ and $\beta$-Hölder densities strictly positive on $\mathcal{M}$, a variance-preserving SGM estimator attains the intrinsic Wasserstein--1 sample exponent $\tilde{\mathcal{O}}(D^{\mathcal{O}_\beta(d)}n^{-(\beta+1)/(d+2\beta)})$, up to logarithmic factors and explicit geometry and density factors. The full nonasymptotic bound explicitly isolates the finite-order geometry envelope, Hölder radius, density lower bound, ambient dependence, and finite-order correction terms. The analysis separates score approximation into a large-noise tangent-cell regime and a small-noise projection-centered, de-Gaussianized Laplace regime. The key technical ingredient is a ReLU implementation of nearest-projection coordinates via finite intrinsic anchors and Gauss--Newton iterations, rather than approximating the manifold projection as a black-box high-dimensional smooth map. Consequently, for families with polynomially controlled geometry and density lower bounds, the constructed score-network parameters have polynomial ambient dependence.

---


### 149. [FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization](https://arxiv.org/abs/2605.15824)

**<font color=#1a73e8>作者：</font>** Quanjian Song, Yefeng Shen, Mengting Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-centric video customization, particularly at the garment level, has shown significant commercial value. However, existing approaches cannot support low-latency and interactive garment control, which is crucial for applications such as e-commerce and content creation. This paper studies how to achieve interactive multi-garment video customization while preserving motion coherence using only single-garment video data. We present FashionChameleon, a real-time and interactive framework for human-garment customization in autoregressive video generation, where users can interactively switch garment during generation. FashionChameleon consists of three key techniques: (i) Instead of training on multi-garment video data, we train a Teacher Model with In-Context Learning on a single reference-garment pair. By retaining the image-to-video training paradigm while enforcing a mismatch between the reference and garment image, the model is encouraged to implicitly preserve coherence during single-garment switching. (ii) To achieve consistency and efficiency during generation, we introduce Streaming Distillation with In-Context Learning, which fine-tunes the model with in-context teacher forcing and improves extrapolation consistency via gradient-reweighted distribution matching distillation. (iii) To extend the model for interactive multi-garment video customization, we propose Training-Free KV Cache Rescheduling, which includes garment KV refresh, historical KV withdraw, and reference KV disentangle to achieve garment switching while preserving motion coherence. Our FashionChameleon uniquely supports interactive customization and consistent long-video extrapolation, while achieving real-time generation at 23.8 FPS on a single GPU, 30-180$\times$ faster than existing baselines.

---


### 150. [Not All Tasks Quantize Equally: Fisher-Guided Quantization for Visual Geometry Transformer](https://arxiv.org/abs/2605.15828)

**<font color=#1a73e8>作者：</font>** Yipu Zhang, Jintao Cheng, Weilun Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models, represented by Visual Geometry Grounded Transformer (VGGT), jointly predict multiple visual geometry tasks such as depth estimation, camera pose prediction, and point cloud reconstruction in a single forward pass. They have been widely adopted in 3D vision applications, but their billion-scale parameters bring substantial memory and computation overhead, posing challenges for on-device deployment. Post-Training Quantization (PTQ) is an effective technique to reduce this overhead. Existing PTQ methods for feed-forward 3D models mainly focus on handling heavy-tailed activation distributions and constructing diverse calibration datasets. However, we observe that feed-forward 3D models predict multiple geometric attributes through a shared backbone, where different transformer blocks and hidden channels contribute distinctly to each task, resulting in substantially different sensitivities to quantization errors across tasks, blocks, and channels. Consequently, treating all tasks equally over-emphasizes insensitive tasks and causes significant accuracy loss on the sensitive ones. To address this issue, we propose Fisher-Guided Quantization (FGQ) for feed-forward 3D reconstruction models. Specifically, FGQ uses the diagonal Fisher information matrix to quantify the different sensitivities across tasks, blocks, and channels, and incorporates these sensitivities into the Learnable Affine Transformation during calibration to better preserve the channels and blocks most critical to each task. Extensive experiments across camera pose estimation, point map reconstruction, and depth estimation show that FGQ consistently outperforms state-of-the-art quantization baselines on VGGT, achieving up to 39% relative improvement under the 4-bit quantization.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
