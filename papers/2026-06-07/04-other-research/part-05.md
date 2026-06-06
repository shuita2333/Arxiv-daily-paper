# 📦 其他研究 | 2026年06月07日

> 本类共 **289** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-289](./part-06.md)

---

### 201. [SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization](https://arxiv.org/abs/2606.06079)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Zhaopeng Feng, Xiaonan Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills, which consist of reusable strategies that guide agent reasoning and action, have shown strong potential for improving model capability at inference time. However, current skill construction methods treat the problem as one-shot extraction, overlooking a fundamental tension: a skill tailored to the specific task fails to transfer, while the abstracted skill often provides insufficient guidance. We attribute this fragility to the absence of explicit mechanisms for skill specification and generalization. To address this gap, we introduce SkillComposer, a framework that decomposes skill construction into three learnable operations: create, improve, and merge. Trained via systematic rejection sampling recipe, SkillComposer enables language models to self-evolve skills at inference time and supports three deployment modes: offline for building generalized libraries, online for task-specific refinement, and hybrid for combining both. Comprehensive experiments on $\tau^2$-Bench, LiveCodeBench v6, and AppWorld show that SkillComposer consistently outperforms baselines. Our SkillComposer-4B improves a 27B executor by up to +4.5 on agent tasks and +3.4 on code tasks, while generalizing across domains and task types unseen during training. Analysis reveals that merge and improve address orthogonal quality dimensions and that skill composition is a transferable meta-ability, providing a practical recipe for skill-augmented inference.

---


### 202. [On Advantage Estimates for Max@K Policy Gradients](https://arxiv.org/abs/2606.06080)

**<font color=#1a73e8>作者：</font>** Shota Takashiro, Soichiro Nishimori, Paavo Parmas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards is widely used for post-training reasoning models, but sparse outcome rewards make exploration difficult. A complementary approach is to optimize inference-time objectives such as pass@K and max@K directly, yet existing policy-gradient estimators for these objectives use different signals, baselines, and normalizations, making their relationships unclear. We study this issue through baseline design and advantage centering. Starting from the advantage estimator of a leading method in the field, we show that it is policy-gradient unbiased but yields a non-centered advantage. We then introduce a Leave-Two-Out baseline that preserves policy-gradient unbiasedness while making realized batch advantages exactly centered. The resulting method, MaxPO, has an efficient quadratic-time implementation and integrates naturally into group-based RL for LLM post-training. We further derive the canonical finite-batch advantage for max@K, providing a unified view of existing advantage estimators. Empirically, we verify that the L2O baseline reduces gradient variance and outperforms non-centered alternatives.

---


### 203. [A Framework for Measuring Appropriate Reliance on Set-Valued AI Advice](https://arxiv.org/abs/2606.06081)

**<font color=#1a73e8>作者：</font>** Ranjan Mishra, Jakob Schoeffer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Appropriate reliance on AI advice has become a central research theme in human-AI collaboration. Existing frameworks have focused exclusively on point predictions as AI advice. However, set-valued AI advice (e.g., discrete sets or continuous intervals) is increasingly being used to communicate uncertainty and improve human decision making. In this paper, we develop the first formal framework for measuring appropriate reliance on set-valued AI advice within the sequential judge-advisor paradigm, spanning both classification and regression tasks. For classification, we first introduce the dimensions that are necessary for evaluating set-valued AI advice. We then define two metrics: correct reliance rate on AI and correct reliance rate on self, which jointly characterize appropriate reliance in this setting. For regression, we introduce quantity of AI reliance and quality of AI reliance, which respectively measure whether a decision maker utilized the AI advice and whether their reliance helped them get closer to the ground truth relative to their initial estimate. Through the application of our framework, we demonstrate how these metrics capture important nuances in human-AI collaboration that existing measures overlook.

---


### 204. [CHALIS: A Challenge Dataset for Language Identification in Difficult Scenarios](https://arxiv.org/abs/2606.06088)

**<font color=#1a73e8>作者：</font>** Michal Tichý, Jindřich Libovický  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CHALIS (Challenging Language Identification Samples), a new benchmark dataset explicitly designed to address difficult cases in language identification: cousin languages and orthographic noise. Our dataset has two parts: First, we collected sentences shared across mutually intelligible language pairs (Czech/Slovak, Spanish/Catalan, Portuguese/Galician, Danish/Norwegian). The second part tests for orthography noise: we transliterate text across multiple scripts, remove diacritics, simulate homoglyph attacks, and use Internet slang. We evaluate four widely used language identification systems on CHALIS and demonstrate that all struggle substantially in these scenarios, especially on lower-resource languages within cousin pairs and on transliterated input. The resource is publicly available at this https URL.

---


### 205. [Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents](https://arxiv.org/abs/2606.06090)

**<font color=#1a73e8>作者：</font>** Yaoqi Chen, Haibin Lai, Yuru Feng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly tackle long-horizon tasks with interdependent decisions, where each action reshapes future constraints and intermediate errors can cascade. Existing RAG and agent memory systems organize histories by semantic similarity, retrieving content-relevant entries at decision time. We argue that this design mismatches execution-state dependencies: it fragments decision trajectories and mixes valid and erroneous traces, hindering coherent state reconstruction and error isolation. We propose MAGE (Memory as Agent-Guided Exploration), an active execution-state manager that stores interactions in a hierarchical state tree. The agent derives its state from the active root-to-current path, combining subgoal summaries, recent traces, and hints from prior branches. Four coupled operations maintain the tree: Grow records new traces, Compress summarizes completed subgoals, Maintain validates summaries, and Revise restores a target boundary and resumes on a new branch. This design bounds context growth while preserving state integrity and isolating flawed segments from the active path. Experiments on MemoryArena show that MAGE improves the average task success rate by 7.8--20.4 pp over baselines, while reducing token consumption by 55.1%.

---


### 206. [Integrating Mechanistic and Data-Driven Models for Neurological Disorders through Differentiable Programming](https://arxiv.org/abs/2606.06094)

**<font color=#1a73e8>作者：</font>** Shah Pallav Dhanendrakumar, Saikat Pal, Sitikantha Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in computational modeling, neuroimaging, and artificial intelligence are revolutionizing the modeling of neurological disorders for improved diagnostics, prognosis, and treatment planning. Mechanistic models provide valuable scientific insight into the disorders, but in practice they are often simplified with assumptions or computationally expensive and slow to solve. However, while purely data driven approaches provide speed and scalability, they require large, high quality data to train and generally suffer from interpretability and generalization issues. This perspective paper presents a structured overview of hybrid modeling strategies, which combine deep learning models with physics based solvers, and are categorized into parallel, series, and parallel-series architectures. Three main approaches that have been emphasized are residual modeling for missing or incomplete physics, Neural Ordinary Differential Equations (NODEs) for continuous time dynamics approximation, and solver in the loop that accelerates traditional solvers with neural approximations. These hybrid models integrate the governing differential equation based formulations and deep learning to characterize the evolution of neurological disorders, and promise advanced personalized neurological modeling. In addition, the study explores and proposes different hybrid configurations to improve diagnosis accuracy, predict disease progression, and inform treatment strategies across a range of neurological disorders. These capabilities outperform standalone mechanistic or purely data driven approaches, making hybrid modeling a powerful tool, especially in applications involving modeling the progression and treatment responses in neurological conditions such as brain tumors, Alzheimer's disease, and stroke.

---


### 207. [OrderGrad: Optimizing Beyond the Mean with Order-Statistic Policy Gradient Estimation](https://arxiv.org/abs/2606.06096)

**<font color=#1a73e8>作者：</font>** Paavo Parmas, Yongmin Kim, Kohsei Matsutani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy-gradient methods usually optimize expected return, but many real world applications care about distributional properties of returns: tail risk, outlier robustness, or best-of-K discovery. We introduce OrderGrad, a family of likelihood-ratio and reparameterization gradient estimators for order-statistic objectives. OrderGrad optimizes finite-sample L-statistics, i.e., weighted averages of sorted rewards or costs, recovering objectives such as VaR, CVaR, trimmed means, medians, and top-m/best-of-K criteria by changing only the rank weights. For any fixed sample size and rank-weight vector, OrderGrad provides an unbiased gradient estimator for the corresponding order-statistic objective. The method is implemented as a simple reward transformation that can then be used in an otherwise standard policy-gradient or reparameterized update. We study the resulting estimator's variance behavior and evaluate it on tasks where mean optimization is mismatched to the deployment objective, including LLM math post-training and other tasks. OrderGrad provides a unified, plug-and-play route to risk-averse, robust, and exploratory learning.
Code: this https URL

---


### 208. [HyperVis: Continuous Latent Visual Relational Graphs on the Lorentz Hyperboloid for Compositional Reasoning](https://arxiv.org/abs/2606.06100)

**<font color=#1a73e8>作者：</font>** Moshiur Farazi, Sameera Ramasinghe, Mahbub Ahmed Turza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) struggle with compositional reasoning that requires understanding inter-object relationships. A natural remedy is to inject explicit scene graph triplets $\langle s, p, o \rangle$ from an off-the-shelf scene graph generator (SGG), but we show this backfires: discrete text labels collide with the continuous visual modality, degrading GQA accuracy from 60.38\% to 58.86\%. We propose \textbf{HyperVis}, which bypasses the SGG semantic bottleneck entirely. From $N$ class-agnostic region proposals, we compute a dense $O(N^2)$ visual relation tensor via spatially-biased cross-attention, project it onto a Lorentz hyperboloid, and enforce hierarchy through spatial physics, namely IoA-driven entailment cones and exterior-angle repulsion. We discover that HyperVis contributes in two complementary ways: (1) as a \emph{training-time regularizer}, the hyperbolic relational losses shape LoRA representations that improve generative VQA (GQA 61.03\% vs.\ 57.21\% for LoRA fine-tuning without relational losses, recovering and surpassing the baseline); and (2) as an \emph{inference-time relational encoder}, hyperbolic prefix tokens boost discriminative compositional scoring (SugarCrepe 79.94\%, $+$6.25pp over baseline). The learned curvature stabilises at $\kappa{=}4.0$, an order of magnitude above prior hyperbolic VLMs where $\kappa$ typically collapses toward zero, indicating that continuous visual features genuinely require the exponential volume of strongly curved space. A controlled Euclidean ablation confirms this decomposition: the relational pipeline regularises LoRA comparably in flat space (GQA 60.81\%), but the compositionality gain is specifically hyperbolic (SugarCrepe $+$4.58pp over Euclidean), with entailment loss ${\sim}6{\times}$ higher in Euclidean training. Codes are available at TBA.

---


### 209. [MS-DKC: A Dataset Knowledge Card Framework for Designing and Adapting Medical Image Segmentation Models](https://arxiv.org/abs/2606.06103)

**<font color=#1a73e8>作者：</font>** Tariq M. Khan, Syed Saud Naqvi, Thantrira Porntaveetus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is often framed as a search for stronger architectures, but this can obscure a more fundamental question: what does the dataset require from the model? In medical imaging, this requirement is shaped by foreground occupancy, morphology, boundary ambiguity, topology sensitivity, annotation quality, acquisition variation, and operating point.
This paper introduces the Medical Segmentation Dataset Knowledge Card (MS-DKC), a framework for making these factors explicit. MS-DKC records dataset evidence through image/acquisition, morphology, supervision, context-dependence, and deployment-risk descriptors. These descriptors are mapped to failure modes, design priors, and risk-aligned criteria, making segmentation design more traceable than architecture-first comparison.
We evaluate MS-DKC on DRIVE, ISIC2018, and ACDC, representing distinct regimes. DRIVE contains sparse, thin, branching vessels, favoring detail-preserving models, sensitivity-aware optimization, threshold analysis, and topology-aware metrics. DKC-TNet-v2 achieved Dice 0.8044 and IoU 0.6730 with 35103 parameters, while SA-UNetv2-DKC-AmbRef reached Dice 0.8141, IoU 0.6865, sensitivity 0.8265, specificity 0.9804, and AUC 0.9853. ISIC2018 involves compact but appearance-variable lesions; validation-constrained score-function selection on Att-Next-Topo/ATTNext produced MS-DKC-AttNextTopo-VCSF-NoAug with Dice 0.8872, IoU 0.8214, precision 0.9173, Boundary F1 0.4878, and ASSD 4.13, while plausible additions failed to improve the risk-aligned profile. ACDC provides a multi-class cardiac case, where MS-DKC recommends four-class softmax segmentation, class-balanced Dice/CE supervision, and class-wise surface evaluation. Overall, the results support dataset-conditioned design: different datasets require different priors, operating points, and evidence before a model can be judged appropriate.

---


### 210. [A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding](https://arxiv.org/abs/2606.06104)

**<font color=#1a73e8>作者：</font>** Chen Hu, Rui Wang, Jiale Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) offers noninvasive, millisecond resolution recordings of neuronal activity and is widely used in neuroscience and healthcare. Many EEG decoding pipelines rely on covariance descriptors for their robustness to noise, but such representations are sensitive to channel-wise scaling. Recent studies have therefore advocated full-rank correlation matrices as a scale-invariant alternative for EEG decoding. In this paper, we propose a general framework for Sliced Wasserstein (SW) discrepancies on manifolds endowed with Pullback Euclidean Metrics (PEMs), termed Pullback Euclidean Metric Sliced Wasserstein (PEMSW). Within this framework, we instantiate two Correlation Sliced-Wasserstein (CorSW) discrepancies on the manifold of full-rank correlation matrices under two recently introduced correlation geometries, \textit{i.e.}, the Off-Log Metric (OLM) and Log-Scaled Metric (LSM). Building on CorSW, we further develop a domain generalization (DG) framework for EEG decoding. Experiments on three EEG datasets demonstrate improved generalization under distribution shifts, with low training overhead and no additional inference cost. The source code is available at this https URL.

---


### 211. [Where, What, Why, and Importance: Structured Defect Grounding for Text-to-Image Feedback](https://arxiv.org/abs/2606.06113)

**<font color=#1a73e8>作者：</font>** Huaisong Zhang, Hao Yu, Yuxuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite generating increasingly photorealistic images, text-to-image (T2I) models still exhibit localized, subtle, and structurally complex failures. Diagnosing these failures requires instance-level feedback that answers where a defect occurs, what type it is, why it is defective, and its importance to overall image quality. While recent dense-feedback methods move beyond scalar supervision, their heatmap-centric representations still formulate diagnosis as pixel-field regression, making it difficult to localize variable-cardinality defects and bind semantic reasons to individual failures. To address this representation bottleneck, we propose Structured Defect Grounding (SDG), which casts T2I diagnosis as structured set prediction by modeling each defect as a (location, type, reason, importance) tuple. To make this formulation trainable and measurable, we introduce SDG-30K, a 30K-image dataset with box-grounded annotations across four modern T2I generators, together with a dedicated evaluation protocol, SDG-Eval. Building on this structured representation, we further present a diagnosis-to-alignment framework in which a Vision-Language Model (VLM) serves as the SDG detector, and BoxFlow-GRPO converts predicted defect sets into box-derived, importance-weighted spatial rewards for diffusion model alignment. Extensive experiments show that our SDG detector outperforms leading proprietary VLMs on structured defect grounding, while SDG-guided rewards consistently improve T2I alignment and support localized image refinement. These results establish SDG as a unified, instance-level interface for diagnosing, evaluating, and enhancing modern generative models.

---


### 212. [Towards Healthy Evolution: Exploring the Role and Mechanisms of Human-Agent Interaction in Self-Evolving Systems](https://arxiv.org/abs/2606.06114)

**<font color=#1a73e8>作者：</font>** Dianxing Shi, Junqi He, Junhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve through continual self-play and self-generated learning signals, but autonomous evolution can also cause capability degradation and safety drift. Although human feedback has proven effective for static and post-trained agents, its role in self-evolving systems remains underexplored. We introduce Agent Norm Correction through Human-like Oversight and Review (ANCHOR), an LLM-based framework that simulates human supervision and delivers feedback at various phases of self-evolution. With ANCHOR, we evaluate two representative open-source self-evolving agent systems across coding, mathematical reasoning, and safety. Our results show that even limited supervision substantially mitigates safety degradation while preserving stable performance on core evolutionary objectives. Further analysis shows that supervision over the output verification phase is the most effective for intervention, whereas increasing supervision frequency yields diminishing returns. These findings provide empirical evidence and practical guidance for designing more stable, controllable, and human-aligned self-evolving agent systems.

---


### 213. [Diff-CA: Separating Common and Salient Factors with Diffusion Models](https://arxiv.org/abs/2606.06120)

**<font color=#1a73e8>作者：</font>** Michaël Soumm, Alexandre Fournier Montgieux, Yunlong He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Analysis aims to separate factors that are common between two data distributions from those that are salient to only one of them. Existing contrastive methods are based on generative models (e.g., VAEs or GANs) that often suffer from limited reconstruction and image quality, which hampers effective latent factor separation and limits their applicability to high-fidelity image generation and edition. We propose a novel conditioning framework for diffusion models that enables contrastive decomposition without compromising generation quality. We first train a prompt-free, image-conditioned diffusion model, and then learn to decompose the conditioning into a common and a salient factor, using weak supervision. We prove that the additive contrastive factorization, commonly assumed in prior work, is identifiable under mild conditions. This factorization enables targeted operations by swapping or interpolating only the salient factor.

---


### 214. [Adaptive state-action abstractions via rate-distortion](https://arxiv.org/abs/2606.06123)

**<font color=#1a73e8>作者：</font>** Fernando E. Rosas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When learning to walk, infants seem to address a coarse version of the problem first - stay upright, reach the caregiver - and refine it only when further practice at that resolution stops paying off. Reinforcement learning offers multiple techniques for building simple versions of complex tasks, but lacks general principles for how to dynamically adjust the granularity of these abstractions during learning. This paper proposes one such principle: refine the abstraction as soon as the learning error within it becomes comparable to the error induced by the abstraction itself. Here, we investigate one way of formalising this principle via a performance certificate that decomposes value error into two terms: a learning error bound captured by a Bellman residual, and an abstraction error bound given by a bisimulation metric. The resulting switching strategy is implemented by soft state-action abstractions built from rate-distortion principles, whose resolution along state and action axes can be continuously adjusted. We validate this construction in a range of tabular settings, showing that near-optimal performance can be achieved under substantial lossy compression of state and action information.

---


### 215. [Deterring Searches for Child Sexual Abuse Material on Google Search and Promoting Help-Seeking](https://arxiv.org/abs/2606.06126)

**<font color=#1a73e8>作者：</font>** Rebecca Umbach, Griffin Hunt, John Buckley 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Google Search deploys a "Onebox" feature at the top of the results page when users conduct searches for Child Sexual Abuse Material. This study evaluates the impact of a strategic shift in this feature, comparing a revised intervention, focused on repercussions and therapeutic resources, to a previous iteration that focused on reporting. Using a difference-in-differences analysis of internal Google Search logs data, we found the new messaging resulted in a 3.8 percentage point reduction as compared to the status quo in subsequent CSAM-related queries within the same Search session. We found an average click through rate of 0.73% on any of the hyperlinked buttons to help-providing resources. Together, this research presents convergent evidence that a subset of individuals can be deterred from ongoing CSAM-seeking and redirected to therapeutic services.

---


### 216. [Computation-Aware Event-to-Frame Reconstruction via Selective Attention](https://arxiv.org/abs/2606.06142)

**<font color=#1a73e8>作者：</font>** Jingqian Wu, Yunbo Jia, Edmund Y. Lam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-to-frame (E2F) reconstruction bridges asynchronous event streams with frame-based vision pipelines, but existing methods often face a trade-off between reconstruction quality and computational efficiency. In this work, we propose an efficient E2F framework that emphasizes causal temporal modeling and computation-aware design. The architecture adopts a recurrent encoder-decoder to incrementally aggregate event information with compact hidden states. To improve robustness under fast motion and illumination variations, a selective context fusion strategy is introduced to integrate event-driven features with prior intensity cues. Within this fusion process, a lightweight hybrid attention mechanism enhances feature selectivity without relying on heavy attention operations. Experimental results on standard benchmarks demonstrate that the proposed approach achieves competitive reconstruction performance while maintaining a favorable balance between accuracy and model complexity.

---


### 217. [WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation](https://arxiv.org/abs/2606.06147)

**<font color=#1a73e8>作者：</font>** Shengtao Zheng, Kai Li, Weichen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation. However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions. We argue that the ability to "imagine" future states -- inherent in World Models -- is critical for robust decision-making under such partial observability. To address this, we construct a challenging Urban Canyon Traversal Benchmark, specifically designed to evaluate spatial understanding in scenarios characterized by severe occlusions and drastic viewpoint transitions. To this end, we propose WorldFly, a novel world-model-based VLA framework that employs a dual-branch coupled flow matching mechanism to jointly generate future video predictions and navigation actions, thereby explicitly guiding the agent's policy via spatial imagination. Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.

---


### 218. [Tight list replicability bounds via a novel sphere covering theorem](https://arxiv.org/abs/2606.06148)

**<font color=#1a73e8>作者：</font>** Ari Blondal, Hamed Hatami, Pooya Hatami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, list replicability has emerged as a framework for formalizing reproducibility in learning theory. A central question is how the required list size relates to the accuracy parameter and natural complexity measures of the hypothesis class.
To achieve sharp bounds on list replicability, we prove a novel topological sphere covering theorem, derived from the Borsuk-Ulam theorem. Specifically, if the $d$-sphere is covered by open sets, each of which lies in an open hemisphere, then $d+1$ of these sets must have a common intersection. Using this result, we obtain a sharp bound on the relationship between list size and accuracy for VC classes. We also show that for large-margin half-spaces, provided the margin is not too large, the optimal list size equals the ambient dimension. However, when the margin is taken to be very large, we devise a replicable algorithm achieving the minimal list size of $\lceil d/2 \rceil + 1$.

---


### 219. [Trust-Aware Predictive Emissions Monitoring for Gas Turbine Fleets with Limited Labelled Data](https://arxiv.org/abs/2606.06156)

**<font color=#1a73e8>作者：</font>** Rebecca Potts, Aiden Durrant, Rick Hackney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based predictive emissions monitoring systems offer a practical alternative to direct emissions measurement, but their deployment across gas turbine fleets is challenging when emissions labels are available for only a small subset of assets. In this work, a trust-aware probabilistic framework is proposed for fleet-level gas turbine NOx prediction under limited labelled supervision. The framework combines a multi-head recurrent prediction model with learned confidence estimation, ensemble-based uncertainty quantification, auxiliary feature prediction, feature-space distance analysis, and operating-range diagnostics. These signals are calibrated on labelled data to produce interpretable per-sample trust scores, providing indicators of prediction reliability on unlabelled turbines, supporting the identification of predictions that should be treated with greater caution during fleet-level deployment. Confidence-based filtering reduces MAE from 0.202 at full coverage to 0.070 for the highest-confidence 10\% of predictions, demonstrating that confidence estimates are meaningfully related to prediction error. Unlabelled and out-of-distribution samples exhibit increased uncertainty and reduced confidence, indicating that the framework responds appropriately to distributional shift. The results show that the proposed trust framework provides actionable reliability information for emissions prediction on unlabelled turbines, supporting more transparent and trustworthy deployment of PEMS across industrial fleets.

---


### 220. [Adaptive Tokenisation Via Temporal Redundancy Masking And Latent Inpainting](https://arxiv.org/abs/2606.06158)

**<font color=#1a73e8>作者：</font>** Kevin Dave, Sai Aditya Patkuri, Chhaya Kumar Das 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive video tokenisation seeks to dynamically allocate token budgets based on the underlying visual complexity of a sequence. Current continuous-regime approaches achieve this via iterative binarised searches or trained neural regressors, while discrete methods often require a full-rate decoder pass to estimate information content. We demonstrate that such computational overheads are not strictly necessary. We show that the latent space of a frozen continuous video tokeniser inherently encodes temporal redundancy that can be exploited directly: spatial positions whose latent representations change minimally between consecutive frames carry near-zero additional information.
We introduce a parameter-free adaptive token allocation mechanism that applies a fixed threshold to per-position temporal-L1 differences, identifying and dropping redundant latent positions. Consequently, the compression rate emerges naturally from the input content rather than being enforced top-down: static scenes get compressed aggressively, while highly dynamic sequences retain more tokens. To reconstruct the dropped positions, we propose the Latent Inpainting Transformer (LIT), a lightweight factorised spatial-temporal attention architecture. The resulting inference pipeline is highly efficient, requiring only a single encoder pass and one LIT forward pass, eliminating the need for auxiliary routing networks. Evaluations across TokenBench and DAVIS, which are the standard benchmarks used by recent tokenisers~\cite{infotok, agarwal2025cosmos}, indicate that our framework yields meaningful, content-driven token allocation while maintaining competitive reconstruction fidelity, and delivers a $31\times$ inference-time speedup over the continuous adaptive baseline (ElasticTok-CV) and an $\approx2\times$ speedup over the discrete information-theoretic baseline (InfoTok)

---


### 221. [Where does Absolute Position come from in decoder-only Transformers?](https://arxiv.org/abs/2606.06160)

**<font color=#1a73e8>作者：</font>** Valeria Ruscio, Umberto Nanni, Fabrizio Silvestri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RoPE-trained transformers distinguish absolute position in their attention patterns, even though RoPE encodes only relative offsets in the inner product. We trace this leakage to two architectural components, The causal mask is responsible for the first: its per-query softmax denominator depends on the absolute query position by construction. The residual stream supplies the second. Under causal attention the activation at position $0$ attends only to itself and runs as a closed dynamical system from the embedding of the token at that position; downstream attention reads this trajectory through sink-reading heads. Both components appear in all three architectures we study, in architecturally specific balance: NTK scaling suppresses the residual-stream component, sliding-window attention allows it to accumulate with depth, and standard RoPE sits between. Replacing the \texttt{BOS} embedding before the forward pass removes $40\%$ of the residual-stream component at early queries. Attention sinks are token-anchored stabilizers that pass forward a deterministic fingerprint of the token at position $0$, constant across inputs when that token is the auto-prepended \texttt{BOS} and varying with it otherwise.

---


### 222. [Learning to Contest: Decentralized Robust Fairness in Cooperative MARL via Cross-Attention](https://arxiv.org/abs/2606.06162)

**<font color=#1a73e8>作者：</font>** Can Savcı  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Fair cooperative multi-agent RL (MARL) teams maximizing egalitarian welfare are exploitable: a single selfish agent free-rides on the surplus fair agents forgo to raise the worst-off. A centralized need-based allocator removes it, but only by taking allocation out of agents' hands; whether decentralized policies can be robust was left open. We show this futility is an artifact of all-or-nothing contention. Under graded contention (a contested resource delivers $1-c$, wasting $c$), we prove that for any $c<1$ a worst-off cooperator that contests a free-rider strictly improves on yielding, so decentralized leverage exists (Prop. 1). Realizing it is a coordination problem under uncertainty: the number of free-riders is unknown and variable, so any fixed rule is dominated. We introduce CAN, a permutation-equivariant cross-attention policy over agents' observed behaviour that infers the number of free-riders and responds proportionally: turn-taking when none, contesting just enough when some. Trained against an adversarial league (PSRO), CAN keeps best-response exploitability low ($\rho\approx1.2$-$1.5$, vs. $\rho=N$ unprotected) across the contention range, wasting almost nothing at $D=0$ (efficiency $\approx1.0$) and retaining most of it at $D\geq1$ (efficiency 0.83-0.96), approaching the centralized oracle on both axes, no central allocator. Fair-MARL learners fail on complementary axes (GGF/FEN yield and are exploitable, SOTO all-contests and wastes), while CAN is both. On two further games we find clear scope, not blanket generality: CAN stays efficient and Pareto-dominates the fair learners, but its robustness holds only in proportion to the contest leverage: strong on a multi-server game, partial when it weakens, absent under winner-take-all (Prop. 1 fails). We also report its fragilities: weak leverage and zero-shot transfer to larger teams degrade it at high contention.

---


### 223. [On the training of physics-informed neural operators for solving parametric partial differential equations](https://arxiv.org/abs/2606.06164)

**<font color=#1a73e8>作者：</font>** Nanxi Chen, Chuanjie Cui, Airong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural operators (PINOs) aim to learn solution operators for partial differential equations by using the governing physics as supervision, rather than relying solely on paired input-output simulation data. By incorporating physical constraints into the training objective, PINOs combine the cross-instance generalization of neural operators with the data efficiency of physics-informed learning. Despite this promise, how to train PINOs efficiently and robustly remains less well-understood than the training of either data-driven neural operators or physics-informed neural networks (PINNs). To bridge this gap, we examine key components of the PINO training pipeline, including architecture design, optimizer choice, loss balancing, and collocation-point sampling strategy. We study three representative operator backbones, Deep Operator Network (DeepONet), Fourier Neural Operator (FNO), and Continuous Vision Transformer (CViT), across five diverse parametric PDE systems. Our results show that CViT provides consistently strong and stable performance across the considered benchmarks. Beyond architecture, we find that several optimization pathologies previously identified in PINN training naturally arise in PINOs, including gradient conflicts and causal violation. We also find that mitigation algorithms developed for PINNs remain effective in the PINO setting. We further compare physics-informed and data-driven training under different data regimes, revealing that a carefully designed physics-informed training pipeline can match, and in some cases, outperform purely data-driven neural operators. Taken together, these findings provide a systematic empirical understanding of the optimization challenges in PINO training and inform a practical pipeline for efficient and robust physics-informed operator learning. Code and data are available at this https URL.

---


### 224. [ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity](https://arxiv.org/abs/2606.06168)

**<font color=#1a73e8>作者：</font>** Prathamjyot Singh, Ashima Sood, Sahil Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ProSarc, an audio-only framework that detects sarcasm by modelling temporal prosodic incongruity, that is, the mismatch between local prosodic dynamics and the utterance-level emotional baseline. Dual encoding paths, a Global Emotion Encoder and a Temporal Prosody Encoder (BiLSTM + multi-head attention), feed a Prosodic Incongruity Analyzer that produces a scalar incongruity score for classification. Monte Carlo dropout provides uncertainty estimates, and an attention-based mechanism localises sarcastic onset without frame-level labels. ProSarc outperforms prior audio-only methods on MUStARD++ (F1=75.3) and generalises to spontaneous (PodSarc, F1=62.9) and cross-lingual speech (MuSaG, F1=65.6). Ten-run validation confirms the contribution of incongruity modelling (Wilcoxon p=0.002, Cohen's d=1.51). Human evaluation shows that model uncertainty tracks perceptual ambiguity and predicted onsets align with human-annotated temporal windows.

---


### 225. [Learning to model pediatric asthma exacerbation from multiple risk factors: a case study in coastal Virginia](https://arxiv.org/abs/2606.06174)

**<font color=#1a73e8>作者：</font>** Jonathan Colen, Eric Werner, Maryam Golbazi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Childhood asthma is a common illness exacerbated by air pollution as well as meteorological and neighborhood-level socioeconomic factors. Modeling asthma exacerbation (AE) in large spatiotemporal datasets requires disentangling impacts from multiple contributors. In this case study, we compared three techniques that balance predictive power with interpretability to predict AE in Hampton Roads, a coastal Virginia region comprising 7 cities and over 1.5 million people. After collating ambient air pollution measurements, weather data, and measures of neighborhood opportunity, we modeled zip code-level acute AE visits to a regional children's hospital and affiliated providers from 2018-2023. Generalized linear models (GLM) provided a baseline while neural networks (NN) served as a maximally predictive target. To bridge between statistical models and deep learning, we developed a framework based on sparse dictionary learning to identify and interpret parsimonious nonlinear interacting equations. After comparing each model's predictive performance, we estimated relative risks for AE due to input exposure variables and found consensus across frameworks. Our work links statistical and interpretable machine learning models to highlight possible synergistic interactions influencing AE, and may enable future studies to guide public health interventions in coastal Virginia.

---


### 226. [RQUL-UIE: Revitalizing Quality-Unstable Labels for Underwater Image Enhancement via In-Dataset Self-Supervision](https://arxiv.org/abs/2606.06176)

**<font color=#1a73e8>作者：</font>** Haochen Hu, Yanrui Bin, Chih-yung Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater Image Enhancement (UIE) is essential for mitigating degradations caused by water medium. Although learning-based methods have advanced significantly, most rely on paired datasets with unstable label quality, which bottlenecks model performance. This paper proposes a diffusion-based, in-dataset self-supervised learning strategy designed to exploit the quality distribution of training labels. Specifically, we evaluate label quality via semantic perception embeddings from a pre-trained diffusion model in a training-free manner. These quality scores are subsequently quantized into noise-level indices, guiding a multi-step denoising process for level-wise supervision. This mechanism prevents low-quality labels from degrading the model while maximizing their utility during training. Furthermore, a Fourier-based refinement network is incorporated to explicitly reconstruct high-frequency components. Extensive evaluations demonstrate that our method consistently outperforms SOTA approaches in restoration quality. The code and pre-trained model will be available once accepted in link.

---


### 227. [Ouvia: A User-centered Framework for Measuring Usability of Speech Translation in Real-World Communication Scenarios](https://arxiv.org/abs/2606.06177)

**<font color=#1a73e8>作者：</font>** Giuseppe Attanasio, Beatrice Savoldi, Daniel Chechelnitsky 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech translation (ST) is increasingly adopted in user applications, yet its evaluation largely focuses on decontextualized testbeds and holistic quality, rather than end users' communication needs. We introduce Ouvia, an evaluation framework for measuring user-perceived usability of speech translation outputs in real-world settings. Ouvia focuses on one-to-one communication: an English speaker needs to convey a request to a Portuguese speaker, and the message is automatically translated. Through a custom web app and multi-phase study design, we collect more than 1,750 such interactions in healthcare and everyday situations, mediated by four ST systems, involving speakers from three English dialects and two genders. We find that modern ST serves people only to a limited extent -- only around half of interactions are rated as usable -- with significant gaps in reported usability across demographic groups. Moreover, among quality metrics, we find that QA-based evaluation is a substantially stronger predictor of real-world usability than standard approaches. Together, these findings stress the importance of situated, user-centered evaluation frameworks that go beyond holistic quality scores and attend to who the technology serves -- and how well.

---


### 228. [Opportunities and Challenges in Securely Reusing and Repurposing Mobile Devices](https://arxiv.org/abs/2606.06181)

**<font color=#1a73e8>作者：</font>** Adelin Roty, Jan Tobias Mühlberg, Jean-François Determe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An estimated 5.3 billion mobile phones became electronic waste in 2022. Many of these devices can be repurposed and used in different contexts to extend their lifetime and to reduce ecological impacts. An often overlooked aspect of smartphone reuse is cybersecurity: these devices embed hardware-backed security mechanisms that rely on vendor-controlled provisioning and are designed for a fixed device lifecycle. In this paper, we investigate whether security mechanisms and guarantees remain effective when devices are repurposed outside their original ecosystem. We explore security features in a PinePhone, an open-hardware smartphone, and focus on three core security aspects: boot chain integrity, isolation provided by the Trusted Execution Environment, and the protection of hardware-bound secrets. Our experiments simulate realistic repurposing scenarios and highlight the complexity of reconstructing trust anchors. We generalize our observations to infer requirements for secure repurposing and illustrate how vendor locked mechanisms hinder the repurposing of a majority of discarded devices.

---


### 229. [A Swarm Approach to Public Transit Using On-demand Routing in a Slime-Mold-Inspired Framework](https://arxiv.org/abs/2606.06189)

**<font color=#1a73e8>作者：</font>** Lindsay Burke, Maxfield Comstock, Jason Graham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Demand-responsive transit (DRT) is a flexible alternative to traditional, fixed-route mass-transit networks. Although DRT can function well in low-density communities, high operating costs and low reliability are common issues. We propose that these issues can be mitigated by moving from a centralized, manually-scheduled scheme to a distributed system capable of dynamically routing multiple vehicles using a slime-mold-inspired routing algorithm to maximize network effectiveness. We additionally introduce the method of dynamic transfers to further optimize transit network efficiency. All passenger allocation and dynamic transfers are handled via a continual cooperative bidding process by the buses. In this paper, we present simulated results for a swarm-driven transit network in suburban, urban, and semi-rural scenarios, using map networks pulled from OpenStreetMap. We show that our approach increases passenger delivery rates relative to a fixed-network approach by 28%, 49%, and 101%, respectively, and results in over 75% reduction in walking time in all cases.

---


### 230. [A Machine Learning-Based Framework for Discovering Huntington's Disease Stages: Integrating Graph Representation Learning and clustering to Uncover Progression Dynamics in Longitudinal Enroll-HD Dataset](https://arxiv.org/abs/2606.06196)

**<font color=#1a73e8>作者：</font>** Lubna M. Abu Zohair, Marta Vallejo, MD Azher Uddin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Huntington's disease (HD) is a progressive brain disorder that gradually affects movement, cognitive function, and behavior. Identifying the stage of the disease accurately and consistently is important for understanding its course, grouping patients, personalized care, and discovering treatment. Existing clinical staging frameworks rely primarily on predefined clinical measurement thresholds and clinical expert decisions, yet these discrete cut-offs may obscure meaningful intra-stage variability and remain vulnerable to inter-rater differences, especially in motor and functional assessments. To address these limitations, we developed an unsupervised machine learning framework based on dynamic graph representation learning to capture temporal relationships within and across patients from longitudinal clinical measurements. Using the learned representations, we applied K-means++ clustering to identify well-separated groups. We then iteratively increased the number of clusters (k), using stability analysis to assess robustness and reveal additional meaningful clusters beyond the initial optimal solution. We applied the framework to 302 individuals from the Enroll-HD cohort (1,477 visits, 44 clinical variables per visit; 80% manifest participants), enabling data-driven discovery of HD stages reflecting natural clinical progression. Despite the limited cohort size, the proposed framework achieved robust clustering performance using a four-dimensional latent space, identifying four meaningful and statistically distinct disease stages through clustering stability analysis. Each stage corresponded to well-defined clinical measurement boundaries, with minimal overlap compared to previously established clinical staging methods.

---


### 231. [SC-MFJ: A Simple Haptic Quality Metric for Medical Image Segmentation](https://arxiv.org/abs/2606.06199)

**<font color=#1a73e8>作者：</font>** Souraj Adhikary, Negar Chabi, Andre Mastmeyer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard segmentation metrics such as Dice and Hausdorff distance measure geometric overlap but say nothing about whether a segmented surface is suitable for haptic rendering in surgical simulation. We propose SC-MFJ (Surface-Constrained Mean Force Jerk), a simple, inexpensive metric that samples a segmented organ surface with many short virtual stylus walks and measures how jerky the resulting contact forces are. The metric is computed from existing segmentation outputs and uses roughly one minute of CPU time per case. We evaluate three pancreas CT segmentation approaches-binary nnU-Net output, Gaussian-smoothed output, and learned signed distance function (SDF) regression-across 80 cases in five-fold cross-validation. SC-MFJ reveals a 147x gap in haptic quality between the raw binary baseline and simple Gaussian post-processing, a difference entirely invisible to Dice and HD95. It also shows that learned SDF regression, despite requiring full model retraining, produces more variable haptic quality than Gaussian smoothing, with a case-level standard deviation of 168 N/s2 compared with 22 N/s2 for Gaussian. A second evaluation on the LiTS liver dataset (131 cases) confirms the generality of these findings: the binary-to-Gaussian gap widens to 189x, and Gaussian smoothing again produces consistently low force jerk across all folds. Our results suggest that for haptic simulation applications, a one-line post-processing step may be sufficient, and that a cheap metric like SC-MFJ can flag problems that geometric metrics miss.

---


### 232. [Learning to replenish: A hybrid deep reinforcement learning for dynamic inventory management in the pharmaceutical supply chains](https://arxiv.org/abs/2606.06201)

**<font color=#1a73e8>作者：</font>** Amandeep Kaur, Gyan Prakash  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pharmaceutical supply chains (PSCs) struggle with inventory management (IM) due to unpredictable demand patterns and variable lead times associated with restocking. This complexity is further compounded by the finite shelf lives of pharmaceutical products, which necessitate a delicate balance between adequate stock and minimal waste. These intertwined factors create a complex optimization problem that requires sophisticated inventory strategies to ensure both product availability and PSC efficiency. This study aims to develop an optimal inventory replenishment policy for pharmaceutical products that can handle the stochasticity arising from uncertain demand and variable PSC conditions. The objective is to maximize the profitability of the PSC while maintaining a high patient service level. We formulate the problem as a Markov decision process and propose a deep reinforcement learning (DRL) approach, specifically, a hybrid asynchronous advantage actor critic distributed proximal policy optimization (A3C DPPO)algorithm. The A3C DPPO algorithm is tailored to handle the continuous action space inherent in IM. The numerical results demonstrate that the proposed algorithm adaptively updates the inventory replenishment strategy under dynamic scenarios, resulting in lower inventory costs compared to various benchmarks. We also conduct numerical validation using real-world pharmaceutical inventory data to confirm the practical feasibility of the proposed algorithm.

---


### 233. [Non-Negative Matrix Factorization for Event Data](https://arxiv.org/abs/2606.06205)

**<font color=#1a73e8>作者：</font>** Raphaël Romero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time event data, in which entities emit instantaneous events over time, arises naturally across many domains such as neuroscience, seismology, and social networks. Non-negative matrix factorization (NMF) is a natural tool to uncover interpretable structure in such data, but it has so far only been applied after binning or smoothing the entity-level counting measures. This preprocessing step comes with the risk of erasing entity-level heterogeneities and fine-grained temporal features. In this paper, we introduce EventNMF, a continuous-time non-negative factorization model that operates directly on event times: each entity's events are modeled as a Poisson process whose intensity factorizes through a non-negative B-spline basis, and a simple estimation procedure recovers interpretable temporal templates shared across entities. The resulting method is mathematically principled, easy to implement, and computationally efficient. We further show that standard binned-count approaches arise as the special case of degree-zero splines, explore bias-variance tradeoffs and compare against existing methods on a synthetic latent factor model, and demonstrate the effectiveness of EventNMF on several real-world applications.

---


### 234. [Unsupervised Pattern Analysis in Japanese Veterinary Toxicology: A Regulatory-Compliant Framework for Cross-Species Risk Assessment](https://arxiv.org/abs/2606.06207)

**<font color=#1a73e8>作者：</font>** Yukiko Kawakami, Mohammad Shirazi, Ryo Shimizuwa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Veterinary pharmacovigilance systems are essential for monitoring adverse drug events (ADEs), yet existing approaches often fail to capture region-specific toxicity patterns shaped by local biological and regulatory contexts. In Japan, these challenges are amplified by species-specific metabolic differences and reporting practices defined by the Ministry of Agriculture, Forestry, and Fisheries (MAFF). Most prior work relies on prediction-oriented models, limiting mechanistic interpretability. This study proposes a regulatory-integrated unsupervised framework for pattern discovery using the National Veterinary Assay Laboratory (NVAL) database. ADEs are encoded into organ system-aligned representations and adjusted for species-specific reporting biases, enabling cross-species comparison. Similarity-based clustering and dimensionality reduction are applied to identify latent toxicity structures. Analysis of 4,120 high-confidence ADE reports (9,080 drug-ADE combinations) identified three significant species clusters (p < 0.01), including hepatic-dominant patterns in companion animals (0.42 $\pm$ 0.06), renal toxicity in ruminants (0.39 $\pm$ 0.07), and dermatological sensitivity in sheep (0.35 $\pm$ 0.07). Drug-level clustering achieved 83% alignment with pharmacological classes, while cosine similarity outperformed alternative metrics (silhouette score: 0.48; cluster precision: 87%). Regulatory validation showed strong agreement with established classifications. These findings demonstrate that regulation-aligned unsupervised analysis can uncover biologically meaningful, region-specific toxicity patterns, providing an interpretable and scalable framework for veterinary drug safety assessment.

---


### 235. [Symb-xMIL: Symbolic Explanations for Multiple Instance Learning in Digital Pathology](https://arxiv.org/abs/2606.06224)

**<font color=#1a73e8>作者：</font>** Yanqing Luo, Julius Hense, Niklas Prenißl 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explanations of multiple instance learning (MIL) models are widely used for validation and discovery in digital histopathology. Existing methods primarily rely on heatmaps that highlight influential regions but do not explain how evidence from different tissue regions is combined to produce a prediction. This limits interpretability, especially when decisions depend on interactions between tissue features. We introduce Symbolic explainable MIL (Symb-xMIL), a post-hoc explanation framework that quantifies how a MIL model's behavior aligns with human-readable decision rules, expressed as logical relationships (e.g., AND, OR, NOT) between input features. These alignment scores reveal semantic patterns underlying the model's predictions. We evaluate Symb-xMIL on synthetic and real-world histopathology datasets. On synthetic MIL data, Symb-xMIL reliably recovers ground-truth logical rules. In a clinical tumor detection task, the best-aligned rules uncover heterogeneous decision patterns and expose hidden model errors. On an HPV-prediction task on TCGA-HNSCC, a cohort of head and neck cancer, our framework refines patient survival stratification beyond HPV status with potential clinical relevance. Overall, Symb-xMIL extends MIL explainability beyond visual attribution toward structured, rule-based reasoning, enabling more transparent and semantically grounded interpretation of model predictions.

---


### 236. [SAM-Flow: Source-Anchored Masked Flow for Training-Free Image Editing](https://arxiv.org/abs/2606.06228)

**<font color=#1a73e8>作者：</font>** Haowang Cui, Rui Chen, Tao Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free image editing has recently attracted increasing attention due to its ability to modify real images using powerful pre-trained diffusion and flow-matching models without additional training. However, existing inversion-based and differential-flow-based methods usually perform global latent transport, which inevitably propagates editing effects to non-target regions and leads to background leakage. To address this problem, we propose SAM-Flow, a source-anchored masked flow framework for localized training-free image editing. Instead of updating the whole latent representation, SAM-Flow first uses a scout image and token-grounded attention maps to localize the editable semantic regions. It then applies differential velocity updates only within these regions, while anchoring the remaining areas to the source-image latent trajectory. To further improve spatial stability and boundary naturalness, we introduce a time-varying source-anchored projection mechanism with dynamic soft masks, transition regions, and temporal mask accumulation. The proposed method is plug-and-play and can be integrated with mainstream flow-matching backbones such as Stable Diffusion 3 and FLUX without any fine-tuning. Extensive qualitative and quantitative experiments demonstrate that SAM-Flow achieves accurate semantic editing while significantly improving background preservation, providing a simple and general localized editing paradigm for training-free image editing. Code is available at: this https URL.

---


### 237. [Tracing the Oracle: Improving Diffusion Timestep Scheduling for 3D CT Reconstruction](https://arxiv.org/abs/2606.06236)

**<font color=#1a73e8>作者：</font>** Yujia Wu, Zhaoqiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion models demonstrate impressive potential in solving highly ill-posed 3D computed tomography (CT) inverse problems, while the inference process suffers from significant computational overhead. Furthermore, existing uniform timestep schedules fail to capture the non-uniform evolution of the reverse conditional diffusion stochastic differential equation, thereby introducing substantial truncation errors. To overcome this limitation, we propose Tracing the Oracle (TrO), a plug-and-play framework for improved timestep scheduling. Specifically, we treat densely sampled numerical integration trajectories on a few samples as the reference oracle. The optimized schedule is extracted by leveraging dynamic programming to globally minimize the cumulative error between the few-step approximation and the oracle. This mechanism precisely allocates the limited sampling steps to critical evolution stages that are highly susceptible to truncation errors. Our extensive experiments on the AAPM dataset across multiple 3D CT reconstruction tasks demonstrate that, when combined with the state-of-the-art 3D CT reconstruction method DDS, our optimized timesteps significantly improve reconstruction fidelity and computational efficiency compared to existing heuristic schedules, especially under a strict budget of no more than 10 sampling steps.

---


### 238. [Benchmarking Open-Source Layout Detection Models for Data Snapshot Extraction from Institutional Documents](https://arxiv.org/abs/2606.06242)

**<font color=#1a73e8>作者：</font>** AJ Carl P. Dy, Aivin V. Solatorio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Institutional documents contain substantial amounts of operational and analytical information embedded within figures and tables. Current approaches for extracting visual content from documents are largely built around generic document layout analysis, where figures and tables are treated as uniformly relevant document objects rather than semantically meaningful analytical artifacts. In this work, we introduce a benchmark dataset and evaluation framework for \textit{data snapshot extraction}, the task of identifying and localizing semantically meaningful visual artifacts within institutional documents. The benchmark spans humanitarian reports, World Bank policy research working papers, and project appraisal documents, and includes annotations for figures and tables that contain reusable analytical information. Using this dataset, we benchmarked multiple open-source layout detection models and evaluated both detection performance and spatial extraction quality. Our results show that current models struggle to generalize to operational institutional documents despite strong performance on conventional academic benchmarks. Common failure modes include confusion between analytical and non-analytical content, fragmentation of composite analytical artifacts, and incomplete extraction of contextual information required for interpretation. These findings highlight a persistent gap between generic document layout analysis and operationally useful data snapshot extraction. We release the source PDFs, annotation dataset, metadata, and source code to support future research in operational document intelligence. The dataset is available at this https URL and the source code is available at this https URL.

---


### 239. [Closing the Loop on Latent Reasoning via Test-Time Reconstruction](https://arxiv.org/abs/2606.06252)

**<font color=#1a73e8>作者：</font>** Xiaopeng Yuan, Haibo Jin, Ye Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work moves intermediate reasoning from natural-language traces into latent or cache-level representations to reduce token overhead and avoid a discrete communication bottleneck. However, this shift also removes a key advantage of textual reasoning: intermediate states are no longer inspectable, making it difficult to determine whether a latent state still preserves the constraints of the original query. As a result, latent reasoning typically operates in an open loop, where a latent state is produced and consumed without an input-anchored fidelity check. We propose ReLAT (Reconstruction-Guided Latent Reasoning At Test Time), a self-supervised test-time training method that closes this loop using the query itself as the reference. Our key observation is that if a latent state faithfully represents a query, the query should be recoverable from it; if the query cannot be recovered, the latent state has lost task-relevant information. ReLAT operationalizes this principle by constructing a differentiable Question -> Latent Thought -> Question cycle and optimizing query reconstruction loss through the latent thought before answer generation. This anchors opaque latent computation to the problem specification it is supposed to represent. Across mathematical reasoning, knowledge QA, and code generation benchmarks on the Qwen family, ReLAT consistently improves over single-model inference, text-based collaboration, open-loop latent collaboration, and alternative test-time training objectives. On Qwen3-8B, ReLAT raises AIME 2024 accuracy from 56.7% to 73.3%, a 16.6-point gain over the strongest open-loop latent baseline.

---


### 240. [Robust Ensemble of Selectively Strengthened and Augmented Predictors](https://arxiv.org/abs/2606.06265)

**<font color=#1a73e8>作者：</font>** Parsa Memarzadehsaghezi, Zahra Hashemi, Pooria Madani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evasion attacks present a significant challenge to the robustness of machine learning (ML)-based classifiers, particularly in critical applications such as fraud detection and cybersecurity. Although existing defense mechanisms are effective in some settings, they often suffer from limited generalizability and do not systematically improve model robustness across diverse attack scenarios. To address these limitations, we introduce Robust Ensemble of Selectively Strengthened and Augmented Predictors (RESSAP), a novel framework that transforms a single classifier into an ensemble of robust classifiers. Each classifier in the ensemble is trained on a carefully selected subset of features, where feature selection is guided by a resilience metric that accounts for both feature importance and robustness. During inference, a random subset of these classifiers is used to make predictions, increasing unpredictability and improving resistance to adversarial manipulation. In addition, noise-based data augmentation is applied during training to strengthen decision boundaries and improve generalization. Our experimental results demonstrate that RESSAP significantly improves robustness against adversarial evasion attacks while maintaining strong accuracy on clean data. Overall, this model-agnostic framework provides a scalable and flexible defense strategy for enhancing the security of machine learning systems without requiring major changes to existing architectures.

---


### 241. [Many Circuits, One Mechanism: Input Variation and Evaluation Granularity in Circuit Discovery](https://arxiv.org/abs/2606.06267)

**<font color=#1a73e8>作者：</font>** Alireza Bayat Makou, Jingcheng Niu, Subhabrata Dutta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Circuit discovery methods identify subgraphs that explain specific model behaviors, and structural differences between discovered circuits are commonly interpreted as evidence of distinct mechanisms. We test this assumption by varying input statistics while holding the task fixed, and show that the resulting structural differences exhibit apparent specialization but do not correspond to functional differences, a pattern we term phantom specialization. Using Literal Sequence Copying across four token-frequency bands plus a control condition in five Pythia models (70M-1.4B), we extract 75 circuits and find that structurally distinct circuits implement the same computation: band-specific edges transfer broadly across bands, a core shared across most bands recovers at least 99% of circuit performance, and causal interchange interventions confirm that internal representations are interchangeable across frequency bands. Repeated extractions within the same frequency band further suggest that discovery algorithms sample from an equivalence class of valid subgraphs rather than recovering a unique mechanism. Standard evaluation practice obscures this pattern: source-level evaluation inflates apparent faithfulness, while edge-level evaluation reveals the many-to-one mapping from structure to function. Our results show that structural differences between circuits are not sufficient evidence for distinct mechanisms, and that exposing this requires edge-level evaluation and cross-condition transfer tests.

---


### 242. [Your GFlowNet Secretly Learns an Optimal Transport Plan](https://arxiv.org/abs/2606.06272)

**<font color=#1a73e8>作者：</font>** Ian Maksimov, Nikita Morozov, Denis Belomestny 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) are a framework for sampling structured objects via stochastic trajectories in a directed graph. In this work, we establish a theoretical connection between non-acyclic GFlowNets and optimal transport (OT). We show that fixing the initial flow distribution in a minimum-flow GFlowNet reduces its objective to a Kantorovich OT problem with graph-induced shortest path costs. At the optimum, the learned GFlowNet policy therefore encodes an optimal transport plan from the source distribution to the target distribution: we show that sampling trajectories from the minimum-flow GFlowNet recovers the corresponding optimal coupling. Our formulation enables applying the GFlowNet learning framework to OT problems on large graphs via edge flows and neural parameterization. Experiments confirm agreement with exact OT solvers and demonstrate that GFlowNets can learn high-quality transport plans.

---


### 243. [Geodesic Flow Matching on a Riemannian Degradation Manifold for Blind Image Restoration](https://arxiv.org/abs/2606.06278)

**<font color=#1a73e8>作者：</font>** Akshay Janardan Bankar, Ankita Chatterjee, Sayan Banerjee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image restoration requires recovering clean images from observations corrupted by unknown and potentially mixed degradations. While recent deterministic flow-based methods model restoration as transport processes that map degraded images to clean ones, they typically rely on Euclidean interpolation, implicitly assuming linear degradation geometry. In this paper, we explicitly model degradations as points on a low-dimensional Riemannian manifold and formulate restoration as geodesic transport on the joint image-manifold space. Using a geodesic flow matching objective, we learn intrinsic transport dynamics that respect the curvature of degradation space. This framework generalizes linear flow matching, provides a principled treatment of mixed degradations as geodesic compositions, and yields a clean theoretical interpretation for generalization beyond observed degradations.

---


### 244. [Synthetic Data Generation and Vision-based Wrinkle and Keypoint Detection for Bimanual Cloth Manipulation](https://arxiv.org/abs/2606.06292)

**<font color=#1a73e8>作者：</font>** Ariel Herrera, Xueyang Kang, Atal Anil Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation of textiles remains challenging because continuous deformation and self-occlusions hinder the robust visual perception required to estimate the cloth's state. To address the lack of annotated real-world data, we developed a Blender-based synthetic pipeline exporting auto-annotated keypoints, and combined manually labeled renders with real-world data to train a wrinkle detector. We present a perception framework integrating a CNN for permutation-invariant keypoint detection and a YOLOv8-OpenCV pipeline to extract grasping points from structural wrinkles. A proposed bimanual algorithm uses this system to stretch fully folded garments via wrinkles, transitioning to keypoint-based ironing once corners emerge. The keypoint model achieves a Mean Position Error (MPE) of 1.7615 pixels. The perception system transfers to physical fabrics without fine-tuning, outperforming baselines that fail in high-occlusion states or yield false positives on severe folds.

---


### 245. [PAC-Bayesian Adversarially Robust Generalization for Message Passing Graph Neural Networks: A Sensitivity Analysis](https://arxiv.org/abs/2606.06293)

**<font color=#1a73e8>作者：</font>** Ziling Liang, Xinping Yi, Qingsong Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whilst the vulnerability of graph neural networks (GNNs) to adversarial attacks poses a critical threat to graph representation learning, the understanding of the robust generalization behavior remains a fundamental challenge in the adversarial setting. Recently, PAC-Bayesian margin-based generalization analysis substantially advances this line of research by providing a flexible and data-dependent analytical framework. However, existing robust analyses often rely on isotropic Gaussian posteriors and control weight perturbations in the full parameter space, which limits the ability to capture heterogeneous parameter sensitivity yet hinges on hidden-width-dependent complexity terms, resulting in not-tight-enough generalization bounds. In this paper, we extend a recently proposed sensitivity-aware PAC-Bayesian framework from deep neural networks to message passing GNNs (MPGNNs) and derive a tighter robust generalization bound in the adversarial setting. Specifically, we first quantify how sensitive the perturbations across different parameter blocks are to the network outputs by deriving the output Jacobians with respect to the weight parameters. Exploiting the fact that these Jacobian matrices have rank at most $K$ in $K$-class graph classification, we then construct Jacobian-aligned sensitivity matrices and use anisotropic Gaussian posteriors with optimized covariances to upper bound the KL divergence in a tight way. Notably, by refining the spectral-norm dependence on the learned weights and reducing the leading dimension factor from hidden-width-dependent terms to the number of classes $K$, our analysis yields much tighter robust generalization guarantees for MPGNNs, thereby guiding their designs to enhance adversarial robustness.

---


### 246. [Reactive Flux Matching: Mechanism Discovery and Adaptive Sampling of Rare Events](https://arxiv.org/abs/2606.06295)

**<font color=#1a73e8>作者：</font>** Rishal Aggarwal, David Ryan Koes, Nicholas M. Boffi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Path sampling methods generate ensembles of reactive trajectories connecting metastable states, but extracting mechanistic insight from these data remains nontrivial. We introduce Flux Matching, a framework that learns two complementary objects directly from reactive trajectory data: a current velocity $u(z)$, whose streamlines trace the dominant reaction pathways, and a scalar potential $h(z)$, obtained from a weighted Helmholtz-Hodge decomposition of the reactive current, that serves as a data-driven reaction coordinate. Both minimize quadratic functionals over the reactive path ensemble, analogous to the flow matching loss in generative modeling, and require no knowledge of the underlying dynamics or stationary distribution. Unlike committor-based methods, $u$ and $h$ remain well-defined under projection onto non-Markovian collective variables, and their level sets in turn provide adaptive interfaces for improved sampling with enhanced sampling methods. Flux Matching is validated through the generation of current velocity trajectories and rate constant calculations on molecular systems.

---


### 247. [A MATLAB Toolbox for Standardized Reading Speed Assessment: Implementing and Extending the Perrin Sentence Generator for English Corpora](https://arxiv.org/abs/2606.06297)

**<font color=#1a73e8>作者：</font>** Daniel P. Spiegel, Romain Bachy  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In the fields of vision science, cognitive psychology, and psycholinguistics, the accurate measurement of reading speed is frequently hampered by the limitations of static reading charts. Repeated testing often leads to memorization effects, while the requirement for oral recitation introduces speech-motor confounds that obscure true information processing speed. To address these methodological hurdles, this paper introduces an open-source MATLAB toolbox that adapts the sentence generation paradigm originally proposed by Perrin, Paillé, and Baccino (2014) for the English language. This system utilizes a semantic ontology and a "proto-truth" logic to autonomously generate thousands of unique, grammatically simple sentences with unambiguous truth values. Beyond the original scope of Maximum Reading Speed (MRS) measurement, this implementation introduces band-pass psycholinguistic filtering and specific logic to resolve semantic ambiguities unique to English. We present this complete software package as an open platform for the scientific community to validate and refine.

---


### 248. [Multi-ResNets for Subspace Preconditioning in Constrained Optimization](https://arxiv.org/abs/2606.06300)

**<font color=#1a73e8>作者：</font>** Merve Karakas, Christopher J. Williams, Emmanuel O. Balogun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose MResOpt, a staged residual neural network architecture for constrained optimization problems. Our architecture fits within predict-complete-correct pipelines and decomposes constraint satisfaction by priority through intermediate re-completion and stage-aware losses. The framework enables domain-informed ordered constraint satisfaction which allows the network to utilize ordinal structure when present. Under an idealized infinite-width regime, we show that our design behaves as sequential Gaussian Process regression. On synthetic QP, QCQP, and SOCP benchmarks, the staged architecture improves high-priority constraint satisfaction across convex and non-convex settings. On line-flow-constrained AC optimal power flow, we introduce a physics-motivated constraint ordering and show that MResOpt supports a learned division of labor that keeps iterates on the equality manifold, achieving substantially lower high-priority violation than reprojected baselines while remaining computationally efficient.

---


### 249. [Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction](https://arxiv.org/abs/2606.06303)

**<font color=#1a73e8>作者：</font>** Hongkun Dou, Zike Chen, Fengji Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controllable generation with discrete diffusion models is often hindered by high computational overhead or the need for retraining. In this paper, we present \underline{\textbf{G}}radient-\underline{\textbf{I}}nformed \underline{\textbf{L}}ogit \underline{\textbf{C}}orrection (\textbf{GILC}), a plug-and-play framework that efficiently estimates guidance signals by repurposing the pretrained denoising network as a variational proxy. To circumvent the gradient instability inherent in high-dimensional discrete spaces, we introduce a Jacobian-free mechanism that directly corrects the clean prediction logits, facilitating stable and effective guidance. Our method accommodates both differentiable and non-differentiable reward functions. Extensive experiments across DNA, protein sequence, and molecular generation tasks demonstrate that GILC achieves state-of-the-art performance without additional training, frequently outperforming fine-tuning approaches.

---


### 250. [RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling](https://arxiv.org/abs/2606.06309)

**<font color=#1a73e8>作者：</font>** Chensheng Dai, Shengjun Zhang, Yifan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models based on Diffusion Transformers (DiTs) have achieved remarkable performance in video synthesis, yet they suffer from high inference latency and computational costs due to the quadratic complexity of 3D attention. Existing acceleration methods primarily reduce computational complexity within each individual denoising steps through techniques such as sparse attention and KV-caching. However, they rigidly adhere to the inherent constraint of the standard diffusion pipeline: every frame in the target video sequence must be subjected to a complete, dense denoising process across all diffusion timesteps. We observe that due to the corresponding contents and motions among adjacent frames, when keyframes with critical semantic transitions are anchored, the intermediate states of others often follow more predictable trajectories, which indicates that such uniform, dense denoising process is inherently redundant for natural video data. To this end, we introduce \textbf{RhymeFlow}, a training-free framework that decouples the denoising trajectories of different frames. Specifically, we first identify a sparse set of pivotal key frames that dominate the latent semantic evolution. Then, only these keyframes undergo dense, step-by-step denoising to ensure structural integrity, while non-keyframes progressively skip denoising steps to minimize computational cost. Since skipped intermediate states of non-keyframes break the temporal coherence in keyframe denoising steps, leading to visual degradation, we further introduce a latent trajectory projection module, which enables keyframes to interact with a complete and temporally consistent sequence representation. Extensive experiments on current DiT-based video generation models demonstrate our method outperforms existing baselines with higher inference speed and better visual quality.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-289](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
