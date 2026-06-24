# 📦 其他研究 | 2026年06月24日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-219](./part-05.md)

---

### 151. [Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation](https://arxiv.org/abs/2606.24464)

**<font color=#1a73e8>作者：</font>** Tianyu Zhu, Yingping Liang, Hesong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven Referring Video Object Segmentation (RVOS) aims to locate and segment target objects in videos given natural language. However, existing models are typically trained on 2D image or video datasets with naive segmentation losses, which overlooks the geometric consistency across frames and leads to weak spatial understanding. In this paper, we propose Geometry-enhanced Language-guided Video segmentation (GeoLaV), a two-stage framework that distills 3D geometric knowledge from images to enhance text-driven video segmentation. In the first stage, we perform monocular geometry pretraining with monocular novel-view synthesis, enabling the model to acquire geometry-consistent visual representations via spatial alignment on large-scale single-image datasets. In the second stage, we introduce geometry-aware distillation and fine-tune the model on video segmentation datasets, transferring 3D structural knowledge from a general 3D prior model. This process reinforces 3D awareness and improves both spatiotemporal coherence and language grounding in segmentation. Extensive experiments show that our method using only image segmentation data already provides notable zero-shot generalization in RVOS. When combined with geometry-aware distillation for fine-tuning on videos, our method achieves state-of-the-art performance across multiple RVOS benchmarks. The code is available at this https URL.

---


### 152. [The Latent Bridge: A Continuous Slow-Fast Channel for Real-Time Game Agents](https://arxiv.org/abs/2606.24470)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A real-time agent for general computer use - with games as the most demanding case - must act within tens of milliseconds while still planning over seconds. These two regimes sit at opposite ends of the latency-quality tradeoff. A reasoning VLM (Qwen3-VL-8B-Thinking) deliberates effectively but requires ~1.5 s per response - far too slow for a 15 Hz control loop. In contrast, a reactive VLM (MiniCPM-o 4.5) acts in milliseconds but underperforms on planning-heavy tasks. We couple two frozen models of matched scale (9B reactive, 8B reasoning), leaving the communication channel as the sole trainable component. The standard coupling is a Text Bridge (T): the slow model writes a suffix the fast model reads. We introduce a learned continuous Latent Bridge (L) that projects the slow model's residuals into the fast model's input-embedding space in a LLaVA-style manner, avoiding any text round-trip; both are compared against Fast-Only (F). On 7 Atari games and a driving domain (MetaDrive), tuning the action decoder per channel on held-out seeds, the Latent Bridge matches or beats the Text Bridge in every domain: it significantly improves two games (MsPacman +57%, RoadRunner +28%) and is a safe drop-in elsewhere. Combining both channels interferes destructively (RoadRunner -96%), so only one should be used. The benefit is highly predictable: the bridge helps if and only if slow reasoning already beats fast reaction (T > F) - the Latent and Text gains over Fast-Only move together at r=0.93. MetaDrive is the controlled negative, where the Latent Bridge is demonstrably inert because the Text Bridge adds no value. We release replay recordings and reproducible pipelines.

---


### 153. [MambaRaw: Selective State Space Modeling for Efficient 4K Raw Image Reconstruction](https://arxiv.org/abs/2606.24479)

**<font color=#1a73e8>作者：</font>** Peize Li, Fanhu Zeng, Tongda Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-camera JPEG previews are ubiquitous in raw image formats and provide an sRGB reference at negligible storage cost. Although existing metadata-based reconstruction frameworks can exploit this side information when recovering raw images, their context models often become computationally expensive especially at high resolution, eg, 4K raw image, given that attention mechanisms scale quadratically with feature maps, hindering its practical application. To address these limitations, we propose MambaRaw, a JPEG-conditioned metadata-based raw image reconstruction framework that uses State Space Models (SSMs) to estimate entropy parameters efficiently. Our key contribution comprises a Spatial-Energy Coupled Context Modeling mechanism with two lightweight modules: (1) TileMambaBlock, which performs Mamba-style selective scanning only on information-dense tiles to improve the efficiency; and (2) Energy-Aware Refinement (EAR), an identity-initialized residual module that enhance feature representation to match the long-tail energy distribution of raw signals. Extensive experiments on three camera datasets (Sony, Olympus, Samsung) show consistent improvements over strong metadata-based baselines and set a new state of the art for JPEG-guided raw reconstruction with great efficiency. Notably, at low metadata bitrates, MambaRaw increases PSNR by 1.2--1.4 dB and reduces end-to-end coding latency by about 9%. Code is released at this https URL.

---


### 154. [VistaRef: Boosting Visual Spatial Orientation Awareness for Pointing-to-Object Detection](https://arxiv.org/abs/2606.24498)

**<font color=#1a73e8>作者：</font>** Ling Li, Zhizhen Cai, Xinkun Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding deictic gestures in natural images is fundamental to AR and human-robot collaboration, providing a basis for seamless spatial interaction. While Transformer-based visual models have achieved significant progress in general object detection, their global attention mechanisms often neglect micro-geometric relationships, degrading orientation accuracy. In pointing tasks, this deficiency manifests as an inability to accurately capture the pointing ray implied by finger poses, which results in pointing drift and localization ambiguity when dealing with distant or densely packed objects. To address this, we propose VistaRef, a framework designed to explicitly enhance spatial orientation awareness. First, we develop the Local Hand Entity Modeling (LHEM) module, which incorporates hand-pose embeddings to strengthen the model's capability to capture subtle finger deviations. Second, drawing inspiration from multi-view geometry, we construct the Geometric Ray Modeling (GRM) module to transform implicit orientation information into explicit spatial geometric features, guiding feature aggregation and deep fusion via attention mechanisms. Furthermore, we introduce a novel Orientation-Consistent Alignment Loss (OCAL) to synergistically supervise hand presence and pointing consistency, ensuring that all architectural improvements collectively serve the core objective of spatial localization. Experimental results demonstrate that VistaRef significantly outperforms the baseline, achieving a 14-point absolute gain in grounding accuracy. Qualitative analysis further confirms that VistaRef effectively models the geometric correlation from hand to target, bridging the spatial perception gap inherent in traditional Transformers for complex scenarios. Code: this https URL.

---


### 155. [GeoIMO: Geometry-Driven Independent Motion Classification for Event Cameras](https://arxiv.org/abs/2606.24499)

**<font color=#1a73e8>作者：</font>** Anil Bayram Gogebakan, Filippo Marostica, Alessio Caviglia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing automotive event datasets rely on appearance-based annotations from frame pipelines, making them poorly suited for motion-aware event perception. We present a geometry-driven, annotation-free framework that classifies detected objects as static or independently moving by exploiting ego-motion structure directly from the event stream. A Focus of Expansion model with yaw compensation estimates global background motion, while objects are labeled as moving when local motion deviates from this prediction, as quantified by a scale-invariant residual. Temporal stabilization improves robustness across consecutive event windows. The method requires no learning, no manual motion labels, and works with any input bounding boxes. Experiments on MVSEC and the Prophesee 1 Megapixel Automotive Detection dataset demonstrate consistent performance across diverse driving scenarios, with yaw compensation improving results during turns and a simple translational local model offering a favorable accuracy-efficiency trade-off.

---


### 156. [UOL@IDEM at BEA 2026 Shared Task 1: Neural Fusion and Feature-Rich Modeling for L1-Aware Vocabulary Difficulty Prediction](https://arxiv.org/abs/2606.24501)

**<font color=#1a73e8>作者：</font>** Nouran Khallaf, Serge Sharoff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes UOL@IDEM's closed-track submission to the BEA 2026 shared task on L1-aware vocabulary difficulty prediction. We model the task as regression and train separate systems for Spanish, German, and Mandarin Chinese\footnote{Below we use \emph{Chinese} for brevity.}. Our system combines multilingual contextual representations with engineered features capturing frequency, surface form, retrieval evidence, semantic alignment, cognate similarity, and masked-language-model predictability. Development results show consistent gains over the official closed-track baselines, with sentence-embedding encoders such as BGE-M3, multilingual E5, and LaBSE performing best. Official submissions achieve RMSE scores of 1.132, 1.037, and 0.891 for Spanish, German, and Chinese, respectively. Feature analysis identifies frequency as the most stable predictor, while contextual predictability, form similarity, retrieval, and semantic features provide complementary L1-sensitive signals. Error analysis shows strong ranking performance but weaker calibration for the easiest items, which are often overpredicted. See this https URL

---


### 157. [What Do Flow-Based Inverse Solvers Approximate? A Posterior-Transport View](https://arxiv.org/abs/2606.24516)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A growing family of training-free solvers -- FlowDPS, FLOWER, PnP-Flow and their diffusion ancestors (DPS, DAPS) -- repurpose a pretrained flow-matching prior to solve imaging inverse problems by adding a measurement-guidance term to the deterministic probability-flow ODE. Despite strong empirical results, what these per-step corrections actually approximate -- and how far the resulting samples are from the true posterior $p(x\mid y)$ -- has not been characterized. We give a posterior-transport account of flow-based inverse problem solving. Our starting point is a simple but consequential fact: for a \emph{deterministic} flow prior, Bayesian conditioning is realized entirely by a \emph{reweighting of the source distribution}, not by a drift correction; pushing the reweighted source through the \emph{unmodified} velocity field yields exact posterior samples. From this we show that trajectory-guidance solvers can be read as the minimum-kinetic-energy \emph{correction} field needed to morph the unconditional source into the posterior, and that FlowDPS / FLOWER / PnP-Flow correspond to distinct zeroth-order / Gaussian / proximal approximations of this single object; we bound the resulting posterior bias in Wasserstein distance. A controlled $2$D study with a closed-form posterior confirms the theory decisively: source reweighting matches the true posterior to the Monte-Carlo floor on every metric, whereas trajectory guidance incurs $200$--$800\times$ larger error and collapses posterior modes, \emph{regardless of guidance strength}. Guided by the analysis we propose a cheap, principled velocity-correction solver that is competitive across two in-domain priors (AFHQ, CelebA) and two out-of-distribution settings while, unlike point-estimate source-space optimizers, producing diverse posterior samples with uncertainty that correlates with reconstruction error.

---


### 158. [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525)

**<font color=#1a73e8>作者：</font>** Jiachen Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents powered by vision-language models show strong potential for automating digital tasks, yet frequently fail in long-horizon scenarios due to the absence of step-level verification. Existing process reward models verify actions through textual reasoning alone, missing the visual nature of GUI state changes. We introduce VisCritic, a visual process reward framework that verifies agent actions by directly comparing pre-action and post-action screenshots in visual feature space. VisCritic employs a Siamese vision transformer to extract change-aware representations, coupled with an Action-Aware Critic Head that jointly evaluates action success, task progress, and error type. A critic-training data construction pipeline generates weakly supervised samples from existing trajectories without additional human labels for critic training. Experiments and offline analyses across five benchmarks demonstrate that VisCritic serves as a plug-and-play enhancement for diverse GUI agents, generally improving benchmark metrics while providing visual diagnostic cues.

---


### 159. [NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](https://arxiv.org/abs/2606.24530)

**<font color=#1a73e8>作者：</font>** Yuru Wang, Lejun Cheng, Yuxin Zuo 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce NatureBench, a cross-discipline benchmark of 90 tasks distilled from peer-reviewed Nature-family publications, designed to evaluate whether AI coding agents can move beyond reproduction toward discovery on real scientific problems. NatureBench is built on NatureGym, an automated pipeline that constructs a standardized, per-task containerized environment from a source paper, addressing the environment-fragmentation problem that has limited the credibility of prior agent-on-research benchmarks. Evaluating ten frontier agent configurations under a strict web-search-disabled protocol, we find that the strongest model surpasses SOTA on only 17.8% of tasks under the g>0.1 criterion. Analysis of method pathways reveals that agents succeed primarily through methodological translation, converting scientific tasks into familiar supervised prediction problems, rather than through genuine scientific invention. Failures are dominated by wrong method choice and insufficient compute budget, not by task misunderstanding. We release the benchmark, the NatureGym pipeline, and a public leaderboard with maintainer-side reproduction. Code: this https URL

---


### 160. [Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization](https://arxiv.org/abs/2606.24543)

**<font color=#1a73e8>作者：</font>** Kanishk Awadhiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are traditionally viewed as autoregressive generators. However, from the perspective of collective computation, they function as high-dimensional Dense Associative Memories that store complex reasoning patterns as latent attractors. In this work, we investigate the energy landscape of mathematical reasoning. We posit that correct reasoning chains correspond to deep, wide attractor basins ("flat minima") in the model's output distribution, whereas hallucinations manifest as sharp, unstable local minima. To exploit this geometry, we introduce a retrieval mechanism based on a Gibbs measure of the trajectory's spectral entropy. By sampling multiple reasoning paths and weighting them by their inverse energy ($P \propto e^{-\beta E}$), we approximate the equilibrium distribution of the associative memory, effectively ``relaxing'' the system into a robust solution. Empirically, this physics-inspired mechanism improves Microsoft Phi-3.5 performance on GSM8K by 5.38\% (84.7\% $\to$ 90.1\%), demonstrating that inference is better modeled as a dynamic settling process into an attractor basin rather than greedy next-token prediction.

---


### 161. [Are Text-to-Image Models Inductivist Turkeys? A Counterfactual Benchmark for Causal Reasoning](https://arxiv.org/abs/2606.24548)

**<font color=#1a73e8>作者：</font>** Jiayi Lei, Yuandong Pu, Xingyu Han 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generation models have achieved remarkable progress in producing visually realistic images from natural language prompts. Yet it remains unclear whether their success reflects genuine causal understanding or sophisticated pattern matching over visual-textual correlations. Inspired by Russell's inductivist turkey, we introduce Counterfactual-World (CF-World), a counterfactual benchmark designed to investigate whether text-to-image models can generate images under rules that systematically contradict real-world priors. CF-World organizes each scenario into three progressive levels: factual generation under ordinary world knowledge, explicit counterfactual generation with direct visual instructions, and implicit counterfactual generation requiring causal deduction from altered rules. We evaluate both open-source and closed-source T2I models using a Vision Language Model (VLM)-based evaluator (CF-Eval). Furthermore, we introduce two metrics: Prior Resistance Rate (PRR), which measures a model's ability to overcome entrenched real-world priors, and Reasoning Retention Rate (RRR), which assesses whether models can maintain reasoning-dependent counterfactual generation without explicit visual cues. Experiments show that all models exhibit sharp degradation from factual to counterfactual settings. Further analyses suggest that these failures arise because current T2I models encode world knowledge and visual appearances as tightly coupled patterns. Consequently, their heavy reliance on frequent visual co-occurrences within the training data forces them to default to familiar commonsense priors when tasked with rendering counterfactual worlds.

---


### 162. [FirmCure:Towards Autonomous and Adaptive Rehosting of Linux-Based Firmware](https://arxiv.org/abs/2606.24549)

**<font color=#1a73e8>作者：</font>** Chuan Hong, Zheng Zhang, Lei Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Full-system rehosting plays a critical role in the security analysis of Linux-based firmware. It matches commonly deployed firmware with sufficient background knowledge. However, for custom devices, existing approaches struggle to handle initialization and runtime obstacles in the rehosting process caused by specialized architectures and hardware-dependent configuration, which heavily rely on expert intervention. This ultimately creates fundamental bottlenecks and results in low rehosting efficiency. To address the above challenges, we propose FirmCure, the first LLM-driven full-system rehosting framework designed for autonomous and adaptive rehosting of Linux-based firmware. FirmCure develops an Adaptive Perception Inference mechanism to extract firmware structural dependencies via static analysis, followed by a Reflective Synthesis module for iterative configuration optimization, and finally an Autonomous Runtime Intervention module for real-time error remediation through runtime fault diagnosis and monitoring. We evaluated 21 IoT firmware images from 10 vendors across 5 architectures, while FirmCure achieved a 100% network port opening rate and 90.5% service interactivity, substantially outperforming state-of-the-art baselines. Our experiments confirm that FirmCure's intervention strategies generalize across heterogeneous firmware. The framework successfully reproduces known vulnerabilities and discovers new security flaws.

---


### 163. [GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/abs/2606.24551)

**<font color=#1a73e8>作者：</font>** Xiao Zhou, Siyue Zhang, Yilun Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. These results suggest that GUI and CLI expose different execution bottlenecks: GUI agents are limited by reliable grounded interaction over long-horizon workflows, whereas CLI agents are limited by the coverage and scalability of their skill interfaces.

---


### 164. [Heterogeneous Knowledge Distillation via Geometry Decoupling and Momentum-Aware Gradient Regulation](https://arxiv.org/abs/2606.24557)

**<font color=#1a73e8>作者：</font>** Wuming Yang, Xiang Zhang, Hongmin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Knowledge Distillation (HKD) aims to transfer knowledge across varying architectures (e.g., from Transformer to CNN) but inherently suffers from severe training instability. We reveal that this instability stems from two highly coupled challenges: massive feature norm discrepancies that cause optimization drag, and severe gradient conflicts between the primary and distillation objectives arising from distinct inductive biases. To achieve stable distillation, we propose SPOFA, a framework built upon a novel Feature and Gradient Dual Stabilization mechanism. Specifically, at the feature level, we introduce a LayerNorm-based decoupling projector that explicitly decouples feature magnitude from direction, creating a bounded and stable space for semantic alignment. At the gradient level, we propose a momentum-driven Exponential Moving Average (MEMA) dynamic scaler. By establishing a robust historical baseline of the optimization trajectory, MEMA actively evaluates instantaneous gradient conflicts and adaptively penalizes harmful distillation signals, guaranteeing stable convergence. Importantly, SPOFA achieves this dual stabilization with an extremely lightweight parameter footprint. Extensive experiments on two mainstream benchmarks demonstrate that SPOFA achieves state-of-the-art accuracy, significantly outperforming computationally expensive methods while introducing only minimal computational overhead compared to standard baselines.

---


### 165. [Quantum CT via Dynamic Interval Encoding and Prior-Balanced QUBO Reconstruction](https://arxiv.org/abs/2606.24561)

**<font color=#1a73e8>作者：</font>** Ao Wang, Yikuang Yuluo, Yujie Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quadratic unconstrained binary optimization (QUBO)-based quantum computed tomography (CT) casts reconstruction as a binary quadratic problem for quantum annealing and hybrid quantum--classical solvers. For grayscale CT, however, image encoding is constrained by the binary-variable budget: fixed global bit-plane encodings increase QUBO size and coupling complexity as gray-level precision improves, whereas low-bit encodings introduce quantization error. We propose a QUBO-based grayscale CT reconstruction framework that combines dynamic interval encoding with prior-balanced optimization. Each refinement round encodes active pixels only within local gray-level intervals around the current estimate, and a boundary-hit-guided update rule adaptively switches between search expansion and local refinement. To improve optimization stability, the method balances projection-domain data consistency and an edge-preserving quadratic prior before forming the final QUBO. Sparse-view and limited-angle fan-beam CT experiments show that the proposed method recovers structures and gray-level distributions more faithfully than the evaluated analytic, iterative, variational, and representation-based baselines. Expressivity analysis and ablation studies further indicate that the improvement mainly arises from effective gray-level representation through dynamic local encoding and more stable data-fidelity--prior coupling. Experiments on the D-Wave hybrid binary quadratic model (BQM) solver further demonstrate that the formulation is executable on a hardware-backed hybrid quantum--classical backend.

---


### 166. [PatternGSL: A Structured Specification Language for Template-Free and Simulation-Ready 3D Garments](https://arxiv.org/abs/2606.24564)

**<font color=#1a73e8>作者：</font>** Zhenyang Li, Lutao Jiang, Yizhou Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing realistic, physically plausible garments from a single image remains a fundamental challenge. Template-free methods capture surface geometry but lack explicit sewing structure for simulation; while programmatic systems are simulation-ready but constrained by predefined templates. This reveals a fundamental representation gap between geometric reconstruction and structured garment construction. We present PatternGSL, a structured garment representation in the form of a template-free and learnable specification language that encodes complete sewing patterns, including panel boundaries, parameterized seams, and explicit stitch topology, in a compact and standardized form. PatternGSL preserves the physical rigor of pattern-based models while removing template dependence, elevating sewing structure as a first-class target for generative modeling. We further propose a vision-language framework that predicts PatternGSL specifications directly from a single image and decodes them into garments using lightweight deterministic validity handling, without optimization-based refinement or manual cleanup. In addition, we introduce PatternGSLData, the first large-scale image-to-GSL paired dataset comprising 300K samples with complete sewing pattern annotations, enabling supervised VLM training for structured garment reconstruction. Experiments demonstrate improved pattern accuracy over prior baselines, explicit sewing-structure recovery, reliable cloth simulation, and pattern-level editing through the same deterministic decoding pipeline. Code and data-processing scripts will be released at this https URL.

---


### 167. [Generating Realistic Individual Activity Schedules via Activity Location Allocation Based on Simulated Travel Times](https://arxiv.org/abs/2606.24566)

**<font color=#1a73e8>作者：</font>** Tatsuya Mitomi, Yahya Gamal, Esra Suel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Individual level daily activity schedules are essential for a wide range of applications, including infectious disease control, urban transportation planning, and policy design. In practice, such schedules are typically generated by combining population data with travel survey data. These data sources are used because they are often publicly available, whereas observed individual activity schedules are difficult to obtain due to privacy concerns. However, because of the complexity of mobility modelling, it is difficult to generate realistic activity schedules that also preserve travel times consistent with those reported in travel surveys. To address this issue, we propose a framework for generating activity schedules that iteratively applies a dynamic programming method to allocate activity locations based on simulated travel times. Numerical experiments with dummy data show that the proposed method reduces the discrepancy between simulated travel times and those reported in travel surveys by 52.2% relative to the first iteration through iterative refinement.

---


### 168. [Multilevel Stochastic Plug-and-Play for Sparse-View CT Reconstruction](https://arxiv.org/abs/2606.24567)

**<font color=#1a73e8>作者：</font>** Antoine De Paepe, Alexandre Bousse, Dimitris Visvikis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view computed tomography (SVCT) reduces radiation exposure and acquisition time, but the limited number of projection views makes the reconstruction problem severely ill-posed and leads to streak artifacts when analytical methods are used. Plug-and-Play (PnP) methods provide an effective way to combine data fidelity with learned image priors, while stochastic PnP methods further improve robustness by matching the denoiser input distribution through re-noising. However, these methods often require many iterations to converge, which limits their practical efficiency. In this work, we propose a multilevel (ML) stochastic PnP method for SVCT that accelerates stochastic PnP reconstruction. We highlight that, in the stochastic setting, directly enforcing prior coherence across levels would require accurately estimating fine-level prior gradients through multiple denoiser function evaluations, which substantially increases the computational cost. Motivated by this observation, we perform the multilevel steps in multiresolution analysis (MRA) approximation spaces. This choice is supported by the structure of the wavelet decomposition, which causes the prior-coherence correction to vanish in expectation, thereby avoiding costly estimation of fine-level stochastic prior gradients for the coarse-level corrections. Experiments on SVCT reconstruction show that our method, called Multilevel Stochastic Plug-and-Play (ML-SPnP), achieves reconstruction quality comparable to state-of-the-art methods while substantially reducing runtime.

---


### 169. [Quant Convergence: Bridging Classical Value Investing and Modern Factor Models for Systematic Equity Selection](https://arxiv.org/abs/2606.24575)

**<font color=#1a73e8>作者：</font>** Augusto Eiji Yamazaki, Hugo Garrido-Lestache Belinchon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern finance relies heavily on complex machine learning models to find patterns in the stock market. However, as these AI models get more complicated, they often memorize short-term market noise instead of finding companies with real, lasting value. We designed this research to test if Benjamin Graham's classic value investing rules could act as a mathematical "low-pass filter" to keep these modern models in check. We built three different sets of features - pure Graham rules, modern market factors, and a mix of both - and tested them against highly complex models (XGBoost and AutoGluon) using 20 years of S&P 500 data. By applying a strict buy-and-hold strategy over a four-year test period (March 2022 to March 2026), the results showed that more complex algorithms do not always win. While the AutoGluon model captured high returns (222.68%), it suffered a substantial 39.78% drop because it bought volatile tech stocks right before the market crashed. On the other hand, the pure Graham Random Forest achieved the highest overall return (232.13%) with much less risk (1.38 Calmar Ratio). Furthermore, the Combined Random Forest successfully mixed momentum with Graham's rules, making a 202.91% return while keeping the lowest maximum drop (34.53%) of any model tested. Ultimately, this research proves that Graham's "margin of safety" isn't outdated; it is actually a highly effective way to prevent modern AI from taking on too much risk.

---


### 170. [Cross-Lingual Exploration for Parametric Knowledge](https://arxiv.org/abs/2606.24579)

**<font color=#1a73e8>作者：</font>** Elisha Diskind, Itamar Trainin, Uri Shaham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parametric knowledge in Large Language Models is not equally accessible across languages. As a result, standard inference techniques often struggle to surface localized facts, leading to failures in cross-lingual knowledge transfer and consistency. In this work, we investigate techniques for accessing hidden factual knowledge by exploring cross-lingual prompting strategies. We identify four inherent dimensions of cross-lingual exploration that directly govern parametric knowledge retrieval and evaluate them on multilingual factual benchmarks covering 17 typologically diverse languages. Our results demonstrate that cross-lingual exploration significantly improves knowledge transfer and factual recall, representing a more efficient compute Pareto frontier than native-language scaling. Furthermore, we observe corresponding improvements in cross-lingual consistency, exceeding what can be explained by accuracy gains alone. Overall, our work establishes multilingual prompt exploration as a highly effective inference-time strategy for unlocking latent parametric knowledge.

---


### 171. [EERLoss: A Novel Loss Function for Training Deep Biometric Models. A Case Study in Keystroke Dynamics](https://arxiv.org/abs/2606.24586)

**<font color=#1a73e8>作者：</font>** Nahuel Gonzalez, Marta Robledo-Moreno, Ivan DeAndres-Tame 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning approaches to biometric verification are commonly trained by optimizing indirect objectives, creating a misalignment between the optimization process and the primary evaluation metric, typically the Equal Error Rate (EER). This paper introduces EERLoss: a subdifferentiable, arbitrarily accurate approximation to EER for training deep biometric models. Furthermore, this framework has the potential to be adapted to optimize any specific operating point on the DET curve, enhancing its generalizability. To validate this approach, EERLoss is evaluated on a particularly demanding behavioral biometric modality: keystroke dynamics verification. This task is characterized by its high intra-class and low inter-class variability. Experiments are conducted on the large-scale KVC-onGoing benchmark, incorporating data from over 185,000 subjects across different scenarios. A comprehensive ablation study initially demonstrates the superiority of EERLoss in comparison to existing state-of-the-art loss functions. It also converges substantially faster compared to other losses, reducing the overall training cost. Additionally, a comparison is made between the proposed loss and the KVC-winning architecture by re-training it with EERLoss, demonstrating that the proposed approach significantly outperforms the original SoTA, achieving a relative EER reduction of up to approx. 30\%. This improvement on a challenging, large-scale benchmark validates the effectiveness of EERLoss as a task-aligned training objective specifically suited for high-variance biometric traits.

---


### 172. [MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery](https://arxiv.org/abs/2606.24595)

**<font color=#1a73e8>作者：</font>** Enze Ma, Yufan Zhou, Wei-Chieh Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interaction artifact: after ordinary assistance, what structured user state can be reconstructed from the memory the agent leaves behind? We instantiate this view in MEMPROBE, a benchmark in which a memory-equipped agent assists simulated users, each carrying a hidden, taxonomy-anchored user-state bank, across a trajectory of leak-controlled tasks, after which that bank is reconstructed from the agent's resulting memory under both full-store and top-k access. Built on synthetic ground truth for efficient, scalable measurement, MEMPROBE spans 50 simulated users with 31 hidden dimensions each (1,550 recovery targets) and tests 5 representative memory systems. Testing state-of-the-art memory agents, we find that successful assistance and recoverable memory behave as distinct capabilities. Task completion nearly saturates, even for a memoryless baseline, while category-balanced recovery stays moderate (about 0.6) and drops further under top-k retrieval. MEMPROBE is the first benchmark to study memory recovery directly, reconstructing the user state a system retains and scoring it against ground truth. We see recovery as a concrete objective for future memory agents to optimize, and MEMPROBE as a step toward an environment where agents are trained to remember their users, growing more faithful the longer they know them.

---


### 173. [To Compare, or Not to Compare: On Methodological Practices in Evaluating Social Bias](https://arxiv.org/abs/2606.24596)

**<font color=#1a73e8>作者：</font>** Federico Marcuzzi, Xuefei Ning, Roy Schwartz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models are increasingly deployed in critical applications, robustly evaluating their social biases is paramount. However, the current literature suffers from widespread methodological fragmentation, which yields contradictory conclusions. This stems largely from ignoring the structural framing of benchmark-level evaluations. To resolve this, we introduce a unified and controllable framework that standardizes heterogeneous benchmarks to systematically contrast isolated demographic assessments with forced-choice comparative settings. Crucially, this allows us to disentangle the confounding effects of Chain-of-Thought reasoning, neutral fallback options, and other structural artifacts in social bias evaluations. Our evaluation across multiple model families reveals a massive, systematic paradigm gap: while isolated assessments limit prejudice activation, comparative settings act as aggressive catalysts for latent discrimination, a shift primarily driven by underspecified contexts. Alarmingly, CoT reasoning exacerbates social biases under comparative settings, and this systemic bias persists as a deterministic prejudice even when models are provided neutral fallback options or claim to answer randomly. Finally, we demonstrate that this comparative prejudice is a generalized phenomenon that scales positively with model size. Ultimately, we offer a crucial methodological guideline: while researchers must leverage comparative settings to robustly audit hidden biases, practitioners cannot safely rely on comparative deployments in ambiguous real-world tasks.

---


### 174. [Uncertainty-Aware Longitudinal Forecasting of Alzheimer's Disease Progression Using Deep Learning](https://arxiv.org/abs/2606.24604)

**<font color=#1a73e8>作者：</font>** Arya Hariharan, Shreyank N Gowda, Anala M R  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Longitudinal modelling of Alzheimer's disease progression is clinically useful only if it can describe not just the most likely next diagnosis, but how a patient may evolve over time and how reliable that forecast is. Most deep learning approaches reduce this problem to single-step classification, treating cognitively normal, mild cognitive impairment, and dementia as flat categories while providing limited insight into how uncertainty accumulates across future visits. We propose a probabilistic framework that combines ordinal diagnosis prediction, multi-horizon trajectory generation, and decomposed uncertainty estimation. A Temporal Fusion Transformer encoder is adapted with a CORAL ordinal output layer, asymmetric loss weighting, and converter oversampling to respect disease-stage ordering and improve sensitivity to MCI-to-dementia transitions. Conditioned on the learned patient-context representation, an autoregressive Mixture Density Network generates five-year probabilistic trajectories for diagnosis state, CDR Sum of Boxes, MMSE orientation, and hippocampal volume. On ADNI, the model outperforms linear, recurrent, and transformer baselines for next-visit diagnosis prediction, with the strongest gains on MCI-versus-dementia discrimination. Generated trajectories achieve near-nominal 90% credible interval coverage, widening uncertainty across the forecast horizon, and biomarker dynamics consistent with expected Alzheimer's disease progression. We further separate aleatoric from epistemic uncertainty using analytic mixture variance and a five-member bootstrap ensemble, which provides the strongest encoder diversity and output-level epistemic signal. Epistemic uncertainty is higher for rare progression archetypes, MCI and dementia patients, and under external evaluation on OASIS-3, where it increases alongside prediction error.

---


### 175. [Abstractions of Queries in Ontology-Based Data Access](https://arxiv.org/abs/2606.24618)

**<font color=#1a73e8>作者：</font>** Michel Leclère, Marie-Laure Mugnier, Guillaume Pérution-Kihli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In ontology-based data access (OBDA), multiple data sources are integrated via mappings to an ontology. We consider an OBDA setting based on existential rules and the certain answer semantics. We address the recent issue of query abstraction, which consists of abstracting data queries by translating them to the ontology layer. Since a perfect abstraction may not exist, the notions of minimally complete and maximally sound abstractions have been introduced.
We study abstractions within an extension of UCQs with a limited form of inequality and a special predicate marking database constants. While this extension does not lead to an increased complexity of the problems of interest, it is able to express minimally complete abstractions, hence perfect abstractions when they exist. We also characterize maximally sound abstractions by making a new connection with the notion of maximum recovery stemming from data exchange.

---


### 176. [When CQs Go Wrong: Challenges in CQ Verification with OE-Assist](https://arxiv.org/abs/2606.24619)

**<font color=#1a73e8>作者：</font>** Anna Sofia Lippolis, Mohammad Javad Saeedizade, Robin Keskisärkkä 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Competency Questions (CQs) are the central component of CQ-verification, an established process in which an ontology is evaluated against a set of natural language questions to determine whether the intended purpose of the ontology has been properly modelled. However, CQ-verification is often time-consuming and error-prone, as it requires careful interpretation of linguistic nuances and precise alignment with formal ontology constructs. Ambiguities and complexity in CQs can further complicate this process, leading to inconsistent modelling decisions and verification outcomes. In this paper, we investigate what makes a CQ challenging and possible solutions to enhance the users' performance in the CQ-verification process. We experimented with the data of 19 participants who performed CQ-verification on 20 tasks using an LLM assistant to support ontology evaluation. The results show the necessity of a tool to refine CQs before publishing them to avoid ambiguity or excessive complexity in later phases of the ontology engineering process.

---


### 177. [Themis: An explainable AI-enabled framework for Reinforcement Learning with Human Feedback](https://arxiv.org/abs/2606.24622)

**<font color=#1a73e8>作者：</font>** Andreas Chouliaras, Luke Connolly, Dimitris Chatzpoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training safe Reinforcement Learning (RL) systems is inherently challenging, with no guarantee of avoiding unwanted behaviors. The most effective defenses against this are (i) transparency through explainability and (ii) alignment via human feedback. While both show promising results, no publicly available framework currently combines them. To address this, we introduce Themis, an XAI-enabled testing and evaluation framework for Reinforcement Learning from Human Feedback. Themis supports over 200 widely used environments and is easily configurable for experiments in RL, transparency, and alignment. Our results show that Themis can train reward models that match or outperform the environment's true reward signal using human preferences. We also provide a cloud-based platform for collecting human feedback and managing experiments. It is user-friendly, auto-scalable, and supports large participant groups across multiple experiments without extra development overhead. Tests show Themis can support one thousand users in back-to-back experiments on a modest commercial machine.

---


### 178. [QC-SMOTE: Quality-Controlled SMOTE for Imbalanced Classification](https://arxiv.org/abs/2606.24625)

**<font color=#1a73e8>作者：</font>** Parth Upman, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class imbalance poses a significant challenge in classification, where existing methods such as SMOTE often generate low-quality synthetic samples in regions with noise or class overlap. We propose QC-SMOTE, a quality-controlled oversampling framework that estimates minority sample reliability using a composite neighbourhood trustworthiness score combining local density, safe-level, and isolation from the majority class. Synthetic candidates are generated using an IPQ-guided best-of-K strategy that evaluates midpoint purity and, when required, majority clearance, with allocation guided by sample reliability and boundary informativeness. Generation behaviour adapts across overlap--imbalance regimes, adjusting interpolation range and selection criteria to match local data geometry. Low-quality synthetic samples are replaced with original minority duplicates when neighbourhood purity falls below an adaptive threshold, providing graceful degradation by reverting to duplication in severely noisy regions. Experiments on 30 imbalanced datasets using repeated stratified cross-validation show that QC-SMOTE achieves the strongest average AUC-ROC and Macro F1 among the compared oversampling methods, with particularly clear gains under moderate and severe imbalance. These results demonstrate the importance of quality-aware, geometry-adaptive synthetic sampling for robust imbalanced classification.

---


### 179. [The Warrant Gap: Claim-Conditioned Re-scoring for Fact-Checking](https://arxiv.org/abs/2606.24627)

**<font color=#1a73e8>作者：</font>** Arka Ujjal Dey, John Collomosse  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fact-checking systems built on LLMs achieve high verdict accuracy on standard benchmarks, yet routinely output Supports labels whose cited evidence does not license the claim. Structured decomposition is the natural way to inspect those warrants, but rigid extraction protocols strip the full-claim context that facets need. We introduce SIFT -- claim-conditioned re-scoring of extracted evidence spans against the full claim -- paired with WSP (Warranted Supports Proportion), an automatic NLI check that the cited warrant entails the claim. We evaluate on FEVER, SciFact, 5PILS, and DP across four open-source backbones. SIFT recovers accuracy on cells where naive decomposition costs up to 27.6 points, while raising WSP above direct prompting; WSP itself calibrates against human gold evidence at AUC 0.92 and precision 0.98.

---


### 180. [Visualizing "We the People": Bridging the Perception Gap through Pluralistic Data Storytelling](https://arxiv.org/abs/2606.24635)

**<font color=#1a73e8>作者：</font>** Lisa Schirch, Beth Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional visual data storytelling relies on binary graphics that depict two simplified groups in conflict. This can increase political polarization by oversimplifying intra-group disagreements and erasing ambiguity and shared ideas or values. This can inadvertently foster "us versus them" thinking. Intentional, pluralistic design choices for AI-enabled digital platforms can produce visualizations that emphasize nuance, opinion distribution, and intergroup commonalities. To demonstrate this potential, we examine deliberative technologies that map high-dimensional opinion spaces and highlight areas of both consensus and dissensus. The paper highlights the We the People deliberation conducted by Jigsaw and the Napolitan Institute in September 2025, which engaged over 2,400 Americans across all 435 congressional districts in an AI-supported, asynchronous dialogue regarding freedom and equality. By utilizing AI to synthesize long-form, text-based participant inputs into interactive "opinion landscapes," the initiative provided an alternative format for pluralistic data storytelling that humanized diverse viewpoints and revealed hidden areas of substantial broad consensus. The paper concludes that shifting from divisive, contrast-heavy visual frameworks to distribution-focused, interactive models represents a highly scalable, low-cost intervention capable of bridging perceptual gaps and cultivating a more resilient, collaborative democratic culture.

---


### 181. [Measuring User's Mental Models of Speech Translation in Human-AI Collaboration](https://arxiv.org/abs/2606.24644)

**<font color=#1a73e8>作者：</font>** HyoJung Han, Nishant Balepur, Jordan Boyd-Graber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Millions of people use machine translation (MT) tools daily, yet little is known about their perception of what systems can and cannot do. This paper studies users' mental models of speech translation systems through a new framework based on cross-lingual question answering, where users either accept MT output or request professional re-translation to answer questions based on the information presented in a foreign language. By analyzing user behavior and accuracy trends across varying translation qualities, we examine to what extent they can predict where the system is likely to be wrong, and how this mental model evolves. Users develop stronger mental models with practice, especially when they have some knowledge of the source language, primarily by relying on surface-level error cues. Moreover, providing speech transcriptions can help users develop better mental models. Our results show the promise of cross-lingual question answering as a downstream task for studying MT mental models and advancing our understanding of human-AI collaboration.

---


### 182. [DREAM: Dense Retrieval Embeddings via Autoregressive Modeling](https://arxiv.org/abs/2606.24667)

**<font color=#1a73e8>作者：</font>** Yixuan Tang, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense retrieval embedding models are a fundamental component of modern retrieval-based AI systems. Most dense retrievers are trained with contrastive objectives, which require labeled positive and negative document pairs that are often costly and difficult to obtain. In this work, we investigate whether the autoregressive next-token prediction objective of a large language model (LLM) can provide supervision for dense retrieval. The intuition is simple: if a document contains information relevant to a query, conditioning on that document should make the target output easier for the LLM to predict. A key challenge is that the next-token prediction loss is computed inside the LLM, while the retriever is a separate embedding model. To address this challenge, we propose DREAM (Dense Retrieval Embeddings via Autoregressive Modeling), which injects retriever-generated query-document similarity scores into selected attention heads of a frozen LLM. During training, these scores determine how much attention each candidate document receives while the LLM predicts the target output. The resulting prediction loss provides gradients for retriever training through the attention mechanism. We evaluate DREAM on retrieval benchmarks BEIR and RTEB using embedding backbones ranging from 0.5B to 3B parameters. DREAM consistently outperforms existing baselines across different model scales. These results demonstrate that DREAM provides a promising approach for training dense retrievers through autoregressive modeling.

---


### 183. [Cost-Optimal Decision Diagrams for Stochastic Boolean Function Evaluation](https://arxiv.org/abs/2606.24672)

**<font color=#1a73e8>作者：</font>** Xia Zong, Tuomo Lehtonen, Jussi Rintanen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In many decision-making scenarios, acquiring information incurs different costs. We consider the problem of constructing a deterministic evaluation strategy that minimizes the expected cost of evaluating a propositional formula under variable costs and a probability distribution over truth assignments. We present a branch-and-bound algorithm with variable-selection heuristics, pruning, and caching. To the best of our knowledge, it is the first practical exact algorithm for this level of generality. Experiments on random instances demonstrate scalability and quantify the efficiency-quality trade-off of a greedy beam-search variant. We additionally evaluate a structured heart-disease diagnosis instance. Finally, we prove that the problem is $\#P$-hard and contained in $\mathrm{PSPACE}$.

---


### 184. [PowerFuzz: Power-Based Black-Box Firmware Fuzzing](https://arxiv.org/abs/2606.24692)

**<font color=#1a73e8>作者：</font>** Dakshina Tharindu, Sahan Sanjaya, Philip Baptist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzzing is widely used for software and hardware verification, offering an effective alternative to random testing. While gray-box fuzzers benefit from full visibility into the system under test and can leverage execution feedback such as branch coverage, these approaches are not applicable when verifying systems whose firmware or binaries are not publicly available. In such scenarios, obtaining coverage information for guiding the fuzzer becomes infeasible. In this paper, we introduce PowerFuzz, a statistical black-box fuzzing framework that leverages power side-channel measurements as a substitute for binary instrumentation, requiring no internal visibility into the target firmware. A central challenge in black-box firmware fuzzing is determining the executed branches during test execution. To address this challenge, we use power traces to identify branches utilizing a sliding window followed by a growing window full-trace correlation method. This approach also enables the construction of a high-level control-flow graph of the black-box firmware, which we utilize to drive the fuzzer to unexplored execution paths. Extensive evaluation using three embedded hardware platforms and ten firmware benchmarks demonstrates that PowerFuzz can provide branch coverage comparable (within 13.5%) to gray-box fuzzers while significantly outperforming (up to 22%) state-of-the-art black-box fuzzers.

---


### 185. [SupplyNet: Supporting Visual Exploratory Learning in Supply Chain via Contextual Multi-Agent Simulation](https://arxiv.org/abs/2606.24694)

**<font color=#1a73e8>作者：</font>** Yanjia Li, Kelcy Kexin Han, Tianrui Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simulation has long supported supply chain management instruction by letting learners observe network behavior and test decision strategies. Recent progress in LLM-driven agents opens new possibilities for richer, more adaptive simulations, but many existing systems still present abstract, opaque data that overwhelms learners and discourages active exploration. We introduce \textit{SupplyNet}, a gamified visual simulation system built on a contextual graph-based LLM multi-agent framework that models interdependent supply chain dynamics and provides responsive feedback through tiered challenges. \textit{SupplyNet} turns the simulation into a manipulable decision space by integrating an interactive network view of system state, a branching timeline for "what-if" exploration and comparison, and a task-oriented analysis console for structured performance breakdowns. Together, these visual components support counterfactual exploration, causal tracing, and comparative reasoning about outcomes. A user study suggests that \textit{SupplyNet} increases engagement and supports users' perceived understanding of supply chain dynamics, highlighting the potential of pairing contextual multi-agent simulation with visualization to advance operational comprehension.

---


### 186. [CN-NewsTTS Bench: a target-level automatic benchmark for raw-input Chinese news TTS pronunciation](https://arxiv.org/abs/2606.24714)

**<font color=#1a73e8>作者：</font>** Shijun Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese news text contains dense written forms such as scores, hyphenated model names, ranges, unit symbols, percentages, English abbreviations, and mixed Chinese-Latin-digit names. These forms are frequent in real listening workflows, and a text-to-speech (TTS) system can preserve the written string while changing the spoken meaning. We introduce CN-NewsTTS Bench v0.1, an open target-level benchmark for evaluating whether Chinese news TTS products pronounce such targets correctly from raw text, without user-side rules, LLM rewriting, SSML hints, or manual edits. The release contains a 200-record development set, an 800-record public test set, 992 public auto-evaluable targets, fixed transcripts from a three-ASR ensemble, an automatic target scorer, and initial results for seven product TTS systems. We additionally report ASR-route diagnostics, ASR-subset ablations, category-level results, confidence intervals, and provider configuration metadata. The best system reaches 0.879 strict accuracy, while several systems remain below 0.60.

---


### 187. [Evaluating the Interpretability of Sparse Autoencoders with Concept Annotations](https://arxiv.org/abs/2606.24716)

**<font color=#1a73e8>作者：</font>** Jonas Klotz, Cassio F. Dantas, Pallavi Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are increasingly used to extract interpretable concepts from vision and vision language models, yet existing evaluation methods largely rely on proxy metrics or qualitative inspection rather than measuring semantic correspondence. We present a human-grounded evaluation framework that quantifies alignment between SAE latents and human-annotated concepts, without requiring user studies, and validate this matching through targeted attribute perturbations. To enable this intervention-style evaluation in vision, we construct synCUB and synCOCO, synthetic benchmarks of paired images that differ in exactly one attribute. We introduce Fully-Binary Matching Pursuit (FBMP), a coalition-based matching procedure that supports many-to-one mappings between SAE latents and annotated concepts, and consistently outperforms one-to-one baselines. For functional validation, we propose a Targeted Attribute Perturbation Alignment Score (TAPAScore), which tests whether matched concepts respond selectively and in the expected direction under targeted image-level attribute perturbations. Under sanity checks, our matching and TAPAScore are the only evaluated metrics that reliably distinguish trained SAEs from untrained ones. Across SAEs trained on CLIP and DINOv2 embeddings, we find that increased overcompleteness can reduce perturbation alignment, indicating a reduction in interpretability. Our evaluation framework suggests that moderate dictionary sizes provide the best trade-off, yielding the most interpretable SAEs. Code and datasets are available at this https URL.

---


### 188. [Decentralised AI Training and Inference with BlockTrain](https://arxiv.org/abs/2606.24722)

**<font color=#1a73e8>作者：</font>** Peter Toth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI training is increasingly shaped by access to dense, centrally controlled accelerator clusters. This creates a structural advantage for hyperscalers and large centralized laboratories, and makes open or independent AI efforts depend on scarce capital, privileged infrastructure, and data-center geography. We present Spheroid BlockTrain, a decentralized training protocol in which a model is partitioned into independently trainable blocks, each optimized on a local objective derived from the same global target and composed at inference into one model. On byte-level WikiText, BlockTrain reaches cross entropy 1.359 (perplexity 3.89), within about 0.04 CE of a same-setup end-to-end Transformer reference, while each active worker trains only one block and avoids full-model optimizer state. A shared six-worker block training run reaches CE 1.385 by averaging same-block updates into one assembled model. HTTP/TCP transport experiments move real serialized checkpoints and updates, including a public-IP three-host run that improves CE from 5.580 to 1.811 while moving 15.22 GB. For inference, the current BlockTrain path uses one block-stack traversal per full output and serves over direct TCP across three public-network GPU hosts up to a 75.80B-parameter logical fp16 shape, outperforming a matched plain-autoregressive TCP pipeline baseline because it emits a full sequence per WAN pipeline traversal rather than one token per traversal.

---


### 189. [SER: Learning to Ground Video Reasoning with Semantic Evidence Rewards](https://arxiv.org/abs/2606.24726)

**<font color=#1a73e8>作者：</font>** Sheng Xia, Zhengqin Lai, Tianxiang Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video MLLMs often struggle with fine-grained spatio-temporal reasoning, sometimes generating correct answers based on irrelevant frames or objects. Although outputting spatio-temporal evidence during reasoning is a promising direction, existing RL frameworks typically rely on geometry-only (IoU) rewards, which can be sensitive to boundary perturbations and overlook semantic alignment. To address this, we propose Semantic Evidence Reward (SER), which reformulates spatio-temporal evidence grounding as a constrained verification task. Instead of computing pixel-level overlap, SER uses a referee VLM as a local checker to evaluate model-generated evidence claims across two dimensions: relevance and localization quality, combined with a temporal penalty. This design reduces the reliance on dense box annotations and enables training directly on standard video QA data. On the V-STAR benchmark, SER achieves 49.6% mLGM, improving by 3.0 points over the strong evidence-grounded baseline Open-o3-Video, demonstrating its potential in enhancing both answer accuracy and evidence grounding.

---


### 190. [SciFi-VIS: Way Out There -- How SciFi and Visualization Influence Each Other](https://arxiv.org/abs/2606.24731)

**<font color=#1a73e8>作者：</font>** Ulrik Günther, Julián Méndez, Gabriela Molina León 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose a hybrid half-day workshop at IEEE VIS 2026, calling for participation from visualization researchers and science fiction creators in order to develop a systematic understanding of the two-way relationship these communities have long shared. We invite submissions of creative formats showcasing connections and inspiring future research. Our workshop plan includes a keynote, lightning talks, brainstorming, cross-community critique, affinity mapping, and discussion around identified themes.

---


### 191. [Task Decomposition for Efficient Annotation](https://arxiv.org/abs/2606.24734)

**<font color=#1a73e8>作者：</font>** Nupoor Gandhi, Emma Strubell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality annotations of structured representations are expensive to collect over large corpora. Manual annotation of structure is laborious, and model-based annotation, although cheaper to generate, requires expensive validation and potentially significant supervision to ensure that the annotation quality is strong enough to be useful downstream. In traditional annotation workflows, annotation of each complete example is performed end-to-end by a single annotator. However, structured annotation is complex, and each aspect of the task represents a unique challenge with an associated inferential load for a given annotator. Modern annotation projects can incorporate heterogeneous groups of annotators, including both models and human annotators with varying domain and linguistic expertise. It remains unclear, however, how to redesign annotation tasks in this setting, where efforts are discriminately allocated across heterogeneous annotators with respect to distinct annotation challenges.
We propose to decompose annotation tasks into sub-tasks in order to reduce the aggregate inferential load of annotation projects. Inspired by the notion of centers from centering theory, we introduce a formal model of inferential load based on the degrees of freedom in the space of valid annotations. Using this model, we show that identifying these centers (i.e. salient anchor entities realized by annotation sub-tasks) constrains the output space complexity, and decompositions which isolate and advance center identification reduce the aggregate inferential load. We provide guidelines for decomposing complex structured annotation tasks, supported by examples demonstrating improved cost-efficiency from our prior work. Finally, we present a procedure for allocating sub-tasks across annotators to maximize quality under a fixed budget.

---


### 192. [VSANet: View-aware Sparse Attention Network for Light Field Image Denoising](https://arxiv.org/abs/2606.24737)

**<font color=#1a73e8>作者：</font>** Gargi Panda, Soumitra Kundu, Saumik Bhattacharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light field (LF) image denoising is challenging due to the high-dimensional structure of LF data. While noise is independent across sub-aperture images, scene content exhibits strong cross-view correlations. We introduce VSANet, a view-aware sparse attention network for LF denoising. Specifically, we propose a view-aware sparse attention (VSA) block that represents the 4D LF feature map as a unified spatial-angular token space and performs cross-view aggregation via locality-sensitive hashing-based sparse attention. This enables global feature interactions with linear complexity, effectively exploiting LF correlations across views and spatial locations. In addition, we design a feature refinement (FR) block to emphasize informative features in spatial, angular, and epipolar subspaces. The VSA and FR blocks are integrated within a sequential attention refinement module, forming the core of VSANet. Experiments demonstrate VSANet outperforms stateof-the-art LF denoising methods.

---


### 193. [Adaptive Hebbian Memory Routing in Vision Transformers for Few-Shot Learning](https://arxiv.org/abs/2606.24756)

**<font color=#1a73e8>作者：</font>** Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot image recognition requires models to adapt to new classes from a small labeled support set. Hebbian fast-weight memory can provide temporary associative information during an episode, but fixed memory behavior may not be appropriate for every few-shot task. In this work, we propose Adaptive Hebbian Routing for few-shot Vision Transformers. The method uses a lightweight MLP router to control the contribution of Hebbian memory, the strength of memory updates, and the retention of previous memory from support-set features. We study Adaptive Placement, Adaptive Plasticity, and Fully Adaptive Hebbian Routing. Experiments use ViT-Small, DeiT-Small, and Swin-Tiny under 5-way 1-shot evaluation on Omniglot, CIFAR-FS, and cross-domain transfer from CIFAR-FS to Omniglot. In the direct Swin comparison, fixed and adaptive Hebbian variants use the same memory location. Adaptive Plasticity improves the fixed Hebbian result from 96.74\% to 96.92\%, while Fully Adaptive Routing achieves the best result at 96.94\%. The fully adaptive Swin model also reduces inference time from 16.51 ms to 14.05 ms relative to fixed Hebbian Swin. On CIFAR-FS, adaptive variants improve performance across all three backbones, and the multi-shot evaluation shows that these gains remain useful as the number of support examples increases. These results show that adaptive plasticity and adaptive memory activation can improve few-shot Transformer representations beyond fixed Hebbian behavior.

---


### 194. [CANDLE: Character-level Arabic Noise Deduplication using Lightweight Encoder](https://arxiv.org/abs/2606.24758)

**<font color=#1a73e8>作者：</font>** Faris Alasmary, Taif Nono, Orjuwan Zaafarani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Handling repeated characters in text can be tricky, since they can represent either the correct spelling of a word or informal character elongation often seen in social media posts. We present CANDLE, a lightweight system for character-level Arabic noise deduplication that addresses this challenge without relying on handcrafted rules, dictionaries, or morphological analyzers. At the heart of CANDLE is a novel application of Connectionist Temporal Classification (CTC) to this task, a formulation not previously explored for character deduplication, which frames normalization as a sequence alignment problem over a character-based encoder. Evaluated on three benchmarks spanning clean newspaper, manually curated ambiguous cases, and real-world social media text, the CTC model achieves a Sentence Error Rate (SER) as low as $5.37\%$ and consistently outperforms a classification-based baseline by a large margin. To reduce inference overhead, we distill the 6-layer CTC model into a 2-layer student, achieving a $3\times$ depth reduction with minimal performance degradation. Beyond deduplication accuracy, normalization yields a practical downstream benefit: a relative reduction in tokenizer fertility of up to $12.8\%$ across a diverse set of Arabic LLM tokenizers, directly lowering inference costs and improving context window utilization. We release all code and models publicly to support reproducibility and advance future research\footnote{this https URL}.

---


### 195. [Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](https://arxiv.org/abs/2606.24767)

**<font color=#1a73e8>作者：</font>** Zhaopeng Cui, Jiarui Hu, Jingbo Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability. In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured map representation, thereby utilizing object units exclusively to drive the camera relocalization task. To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities. Leveraging recent foundation models, we first introduce a multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective 2D-3D object matching. Additionally, we design object-oriented reference frames as position priors, paired with a reference frame selection strategy based on the Distance-IoU (DIOU), enabling extension to scalable scenes. Moreover, to ensure stable and accurate pose optimization, we also propose a dual-path 2D Iterative Closest Pixel loss guided by object shape. Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets. Our source code will be released upon acceptance.

---


### 196. [Posterior Refinement: Fast Language Generation via Any-Order Flow Maps](https://arxiv.org/abs/2606.24773)

**<font color=#1a73e8>作者：</font>** Manan Agarwal, Sheel Shah, Chanhyuk Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-autoregressive generation offers a powerful paradigm for iterative refinement, allowing models to recursively critique, erase and regenerate arbitrary subsets of tokens. However, existing non-autoregressive models fail to realize this potential. Masked Diffusion Models (MDMs) suffer from factorization error, causing sample quality to collapse when generating multiple tokens simultaneously. Flow Map Language Models (FMLMs) circumvent this bottleneck via joint sequence transport for excellent few-step generation, but sacrifice the inference-time flexibility of MDMs. We introduce FMLM+, a framework that bridges this gap by equipping FMLM with masking-style noise schedules. While generating the full sequence in a single step, FMLM+ simultaneously scores the global consistency of each token a posteriori. We leverage this to introduce Posterior Refinement, a novel inference-time refinement strategy that enables the model to adaptively self-correct its outputs, matching the performance of discrete baselines with 32x fewer NFEs. Across diverse benchmarks, we demonstrate that FMLM+ with Posterior Refinement improves the speed--quality tradeoff over both MDM and FMLM families, providing a scalable foundation for high-fidelity language modeling.

---


### 197. [Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients](https://arxiv.org/abs/2606.24774)

**<font color=#1a73e8>作者：</font>** Zhihao Zhu, Hongyi Tang, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. These concerns are particularly acute in healthcare, where patient medical images paired with clinical reports demand rigorous privacy safeguards. However, existing training data detection methods either fail in cross-modal scenarios or rely on superficial output signals with insufficient discriminative power. We introduce GradAudit, a gradient-based auditing framework that examines internal optimization dynamics rather than treating VLLMs as black boxes. Our approach builds on a key observation: model parameters converge to regions where gradients on training samples become stable and well-aligned, whereas gradients on non-training samples remain noisy and inconsistent. By analyzing these gradient signatures, GradAudit achieves strong separability and detects genuine image-text associations learned during training, not merely individual modality membership. Empirically, across both medical and general-domain datasets, GradAudit substantially outperforms state-of-the-art baselines in both pretraining and fine-tuning VLLMs. In a case study employing copyrighted content, we show that existing training data detection methods not only underestimate the extent of unauthorized data usage, but that this underestimation becomes more pronounced as models become more recent and more advanced.

---


### 198. [Burnyard: Future of Malware Analysis](https://arxiv.org/abs/2606.24778)

**<font color=#1a73e8>作者：</font>** Rama Ramana Sharma Parnandi, Carter Yagemann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware analysis is a critical aspect of modern cybersecurity. The prevailing industry practice, sandboxing, involves executing suspicious binaries within isolated virtual machines in large-scale data centers. However, this approach can unintentionally expose samples to public platforms such as VirusTotal and MalwareBazaar, and it is both resource-intensive and time-consuming.
Burnyard addresses these limitations through a lightweight binary emulation platform that captures observable runtime behavior and records it as structured CSV event traces.

---


### 199. [BluTrain: A C++/CUDA Framework for AI Systems](https://arxiv.org/abs/2606.24780)

**<font color=#1a73e8>作者：</font>** Adhitya Charan, Adwaid Suresh, Anuj Kumar 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress in deep learning is, at scale, more a matter of systems engineering than of modelling: the behaviour of a model in training (its throughput, its memory footprint, and the numerical fidelity of the result) is determined less by the architecture itself than by how that architecture is expressed on the hardware. To achieve absolute control over this hardware expression while abstracting away systems complexity to make modelling seamless and eliminating the need for repetitive orchestration logic, BluTrain was architected from first principles as a robust, lightweight, and architecture-general training framework in standard C++ and the core CUDA programming model. Every layer is implemented natively: a typed tensor module with reverse-mode autograd, a linear-algebra library, a caching allocator, a multi-mode distributed-execution module, and an MLIR-based deep-learning compiler. In formal evaluations training a 124M-parameter GPT-2 baseline in FP32 on an 8-GPU 6000 Ada system, BluTrain outperforms industry-standard baselines in both throughput (sustaining an average of 407K tokens/s versus PyTorch's 395K tokens/s) and memory efficiency (achieving up to a 22% footprint reduction), while strictly preserving numerical fidelity and converging to a marginally lower final validation loss. With every layer explicitly open to native tuning, the performance ceiling is the framework's own to raise.

---


### 200. [Assessing Distribution Shift in Human Activity Recognition for Domain Generalization](https://arxiv.org/abs/2606.24781)

**<font color=#1a73e8>作者：</font>** Rebecca Adaimi, Edison Thomaz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the field of Human Activity Recognition (HAR) continues to draw interest from researchers and advance in important ways, some key challenges remain. One of the most difficult aspects of building HAR models that show good performance in real-world settings is dealing with data diversity from device and sensor heterogeneity, and contextual changes that are intrinsic to real-world applications. While data diversity in HAR has been well-acknowledged in the literature, there remains a gap in understanding the effect of various types of distribution shifts on HAR models and the domain generalization problem that arises. Towards that end, this paper systematically evaluates 4 different types of distribution shifts, including variations in device type, sensor placement, sampling rate, and user behavior. Quantifying their effects, we illustrate that diversity shifts predominantly define all types of shifts, indicating the existence of unique features that are not shared across different domains. We then introduce a uniform HAR-based distribution shift benchmarks and conduct a comprehensive evaluation of up to 28 domain generalization methods. Our analysis exposes the limitations of current domain generalization algorithms in achieving model generalizability, marginally outperforming the empirical risk minimization baseline. This work represents the first systematic exploration of domain generalization and adaptation concerning specific distribution shifts in sensor-based HAR, offering an open-source benchmark platform and datasets to spur further research.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
