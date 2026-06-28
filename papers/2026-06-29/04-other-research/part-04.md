# 📦 其他研究 | 2026年06月29日

> 本类共 **245** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-245](./part-05.md)

---

### 151. [The Capability Frontier: Benchmarks Miss 82% of Model Performance](https://arxiv.org/abs/2606.26836)

**<font color=#1a73e8>作者：</font>** Bradley Fowler, Ryan Smith, Daniel Thi Graviet 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks typically report accuracy for a single model on a single run. This systematically understates real-world LLM capabilities, particularly under heterogeneous data distributions: (i) different models get different questions correct according to their specializations, and (ii) given a budget, multiple generations can be sampled and selectively retained. To quantify this gap, we introduce the Capability Frontier: a Pareto frontier over a set of models that characterizes the best achievable performance at each cost level under optimal selection across models and generations (i.e., via an oracle). Our construction corrects for two opposing biases: underestimation from single-model evaluation and overestimation from taking maxima over noisy samples. We study 21 LLMs across 16 widely used benchmarks spanning coding, reasoning, medicine, factuality, instruction following, and agentic tasks, comparing Capability Frontier performance at matched cost to each benchmark's top-performing model. Correcting for single-model evaluation yields a 54% error rate reduction; additionally correcting for single runs yields an 82% improvement, with SOTA accuracy matched at 85% cost reduction. Complementing these empirical results, we use controlled probabilistic simulations to show that higher query topic entropy produces a near-monotonic increase in the performance gap between oracle routing and the best single model. Our findings suggest collective LLM capabilities are substantially underestimated, with implications for evaluation and deployment in data-heterogeneous, multi-domain settings.

---


### 152. [SpikeTimer: Exploring Active Copyright Protection in Spiking Neural Networks via Temporal Backdoor Regularization](https://arxiv.org/abs/2606.26841)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Gaolei Li, Jun Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNN) have emerged as a revolutionary paradigm compared to traditional Deep Neural Networks (DNN) in energy-efficient computing, showcasing exceptional capabilities in processing event-driven sensory data for real-time applications like robotics and edge AI systems. However, unlike extensive studies on DNN copyright solutions, SNN copyright protection remains largely underexplored due to their inherent temporal coding complexities and spike-driven computation. In this study, we propose a novel active copyright protection framework named SpikeTimer for SNNs via temporal backdoor learning. SpikeTimer partitions neuromorphic data into designated timeslices and exclusively embeds authorized tokens within authorized slices. Furthermore, the inherent temporal segmentation characteristic intrinsically enables SpikeTimer to support multi-user authorization mechanisms and accommodates token embedding of arbitrary morphology. Based on this, SpikeTimer precisely responds to authorized data containing a token within the correct timeslice, while producing erroneous responses to unauthorized data. Our key innovation lies in establishing a time-dependent authorization mechanism that protects the SNN copyright by temporal token validity. Additionally, SpikeTimer retains its defensive efficacy even under adversarial attempts. Evaluations on multiple neuromorphic datasets manifest that SpikeTimer achieves around 10% accuracy on unauthorized data with merely around 1.5% degradation on authorized inputs. Moreover, SpikeTimer demonstrates robust resistance against model finetuning and pruning threats.

---


### 153. [Liquid Fusion of Heterogeneous Representations Towards General Salient Object Detection](https://arxiv.org/abs/2606.26849)

**<font color=#1a73e8>作者：</font>** Ke Chen, Ling Zhou, Guangqi Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General Salient Object Detection (SOD) aims to identify and segment visually interesting objects from uni-modality or multi-modality scenes, recently advanced by cutting-edge State Space Models (SSMs). However, a critical limitation of current approaches is their neglect of the inherent spectral biases exhibited by different neural network paradigms. By digging to the dataset-level spectral analysis of Convolutional Neural Networks (CNNs) and SSMs, their semantic representations are inherently complementary based on their complementary frequency preferences. Inspired by this, we harmonize heterogeneous representations from SSMs and CNNs to bridge their spectral biases for general salient object detection. To this end, inspired by the dynamic information propagation of Liquid Neural Networks (LNNs), we introduce a liquid fusion to dynamically integrates features from two backbones, including VMamba and ConvNeXt, referred to Liquid Fusion Network (LFNet). Concretely, by treating the continuous VMamba features and ConvNeXt features as evolving states and exogenous stimulus, respectively, LFNet employs a dynamic gating mechanism for content-aware feature aggregation. Crucially, this state-stimulus paradigm enables to scale to multi-modal cues, resulting in flexibility in general SOD. Besides, a Saliency-Guided Upsampling (SGU) operator to propagate the features to the shallow layer, which leverages a spectral-spatial co-design to suppress upsampling artifacts while preserving semantics. Extensive experiments across five diverse tasks (RGB, RGB-D, RGB-T, VSOD, and VDT) demonstrate that LFNet achieves state-of-the-art performance, offering a superior trade-off between detection accuracy and model efficiency. Code has been released at this https URL.

---


### 154. [Context-Aware Synthesis of Optimization Pipelines for Warehouse Optimization](https://arxiv.org/abs/2606.26852)

**<font color=#1a73e8>作者：</font>** Janik Bischoff, Anne Meyer, Uta Mohring 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Order fulfillment in manual picker-to-goods warehouses involves interconnected decisions such as item assignment, order batching, and picker routing. While integrated models capture interactions between these decisions, practical warehouse systems often require decomposed approaches due to organizational boundaries, differing responsibilities, or limited data availability. Existing studies primarily evaluate algorithms for isolated subproblems or fixed subproblem combinations for specific warehouse settings, but lack a general mechanism to determine applicable algorithm configurations, compose them into valid solution pipelines, and assess their performance.
With Context-Aware Synthesis of Optimization Pipelines (CASOP), we propose a framework for constructing and evaluating context-specific optimization pipelines and apply these to order fulfillment. The framework comprises: (1) a modular repository of algorithms for common order fulfillment problems; (2) semantic data and algorithm cards to describe warehouse context and algorithm requirements; (3) a taxonomy that structures order fulfillment problems into relevant subproblems; (4) a pipeline synthesizer that identifies applicable algorithms for a given warehouse context and composes all valid optimization pipelines; and (5) a pipeline evaluator that assesses all resulting pipelines. We demonstrate the framework on 7 benchmark instance sets covering four problem classes, resulting in 1,063,044 valid pipelines. The framework supports researchers and practitioners in designing, automatically synthesizing, and selecting valid, high-performing algorithmic pipelines for warehouse operations. The software is open-source and available at this https URL and this https URL.
Keywords: Warehouse optimization, Algorithm selection, Pipeline synthesis, Order fulfillment

---


### 155. [AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems](https://arxiv.org/abs/2606.26859)

**<font color=#1a73e8>作者：</font>** Changxin Lao, Fei Pan, Guozhuang Ma 等 60 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. Innovation therefore scales linearly with headcount rather than compounding with evidence, compute, and accumulated experimental knowledge. We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. AgentX operates as a self-evolving development engine: it autonomously generates, implements, evaluates, and learns from recommendation experiments at a scale and pace that no manual workflow can sustain.
The system orchestrates four tightly coupled stages in a closed loop. A Brainstorm Agent synthesizes evidence from historical experiments, system architecture, data analysis, and external research into ranked, executable proposals. A Developing Agent translates each proposal into production-ready code through repository-grounded generation and multi-dimensional reliability verification. An Evaluation Agent conducts safe online rollout with guardrail-vetoed A/B judgment, converting both successes and failures into structured knowledge assets. A Harness Evolution layer (SGPO) then distills execution trajectories into semantic-gradient updates that continuously sharpen the agents themselves -- making the system not merely automated, but self-improving.

---


### 156. [Rolling Shutter Relative Pose Estimation Made Practical](https://arxiv.org/abs/2606.26863)

**<font color=#1a73e8>作者：</font>** Daniel Barath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rolling shutter (RS) cameras equip virtually all consumer devices, yet RS-aware relative pose estimation has remained impractical: the state-of-the-art solver requires a minimum of 20 point correspondences, making RANSAC-based robust estimation prohibitively expensive due to the exponential dependence of the iteration count on the sample size. We make RS relative pose estimation practical by introducing affine correspondences (ACs) into the RS two-view geometry. We derive novel \emph{RS-corrected affine constraints} that account for the coupling between point perturbations and the row-dependent essential matrix, providing two equations per correspondence beyond the standard epipolar constraint. Building on these constraints, we develop a linearized algebraic solver that estimates pose and RS motion from only 7 ACs. The solver exploits the physical smallness of RS parameters to linearize the constraints, eliminates the 12 RS unknowns via null-space projection, and solves the remaining degree-20 system via action matrices in 1.2\,ms. On the TUM RS benchmark, our method achieves the best pose and RS parameter accuracy among all tested methods and, uniquely among RS solvers, provides accurate translational velocity estimates -- which are poorly conditioned from point correspondences alone due to a $\vec{v}$-$\vec{t}$ coupling. On the global-shutter EuRoC MAV dataset, the solver achieves comparable accuracy to the standard 5-point algorithm, demonstrating that it generalizes well to the GS setting. Code is at this https URL.

---


### 157. [Fortress and Gatekeeper: Theorizing Transitive Trust in Third-Party Cybersecurity Risk Governance](https://arxiv.org/abs/2606.26866)

**<font color=#1a73e8>作者：</font>** Yijun Chen, Misita Anwar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party vendors, such as analytics platforms, cloud services, identity providers, and software suppliers, are increasingly embedded in digital service delivery. While these arrangements enable scale and specialization, they also move customer data and security-relevant practices into environments that customers rarely see, select, or evaluate. This paper examines this problem through a document analysis of the November 2025 OpenAI-Mixpanel security incident. The incident serves as an illustrative case for showing how a security event in a vendor environment can become a governance and accountability problem for the focal organization that maintains the customer relationship. Drawing on organizational trust research and agency theory, the paper argues that third-party cybersecurity risk is both a trust relationship and a delegation problem. Customers trust the visible service provider, while the provider relies on vendors whose security practices are only partially visible and controllable. The paper develops the concept of transitive trust, where customer trust in a digital service depends on the security practices of vendors authorized by that service provider. It then presents the Fortress and Gatekeeper framework, which explains cybersecurity governance boundaries through trust and data flows rather than formal organizational ownership alone. The analysis develops four propositions concerning vendor integration, metadata exposure, vendor assurance, and data proliferation. The paper contributes to cybersecurity governance scholarship by explaining how delegated data processing creates customer-facing accountability and by identifying implications for vendor tiering, data classification, contractual design, continuous assurance, and data minimization.

---


### 158. [SpatialFlow-GRPO: Where Spatial Credit Drives Image Editing](https://arxiv.org/abs/2606.26872)

**<font color=#1a73e8>作者：</font>** Yankai Yang, Yancheng Long, Wei Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent online reinforcement learning has substantially improved image editing quality. However, existing Flow-GRPO-style methods usually rely on a single whole-image reward, which makes fine-grained editing optimization difficult. We observe that a key obstacle in image editing is this spatial uniformity assumption: a whole-image reward cannot distinguish how different spatial regions contribute to image quality. To address this issue, we propose SpatialFlow-GRPO, a training framework that introduces spatially fine-grained reward feedback. The framework converts region-aware rewards into semantic-region-level optimization signals and aligns region advantages with the corresponding latent positions during policy updates. We also train a region-aware reward model, SFReward, construct SFReward-14K with region-annotated editing samples, and introduce MultiEditBench to evaluate multi-region editing ability. On OmniGen2 and FLUX.2-klein-4B, SpatialFlow-GRPO outperforms Flow-GRPO on GEdit-Bench, ImgEdit-Bench, and MultiEditBench. The results show that SpatialFlow-GRPO converts local feedback into spatially aligned update signals and improves editing quality.

---


### 159. [RIS-Assisted Proactive Handover for Reliable mmWave Wireless Networks](https://arxiv.org/abs/2606.26885)

**<font color=#1a73e8>作者：</font>** Alaa Adnan, Mohammad Al-Quraan, Ahmed Zoha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) networks are highly susceptible to line-of-sight (LoS) blockages. Vision-aided wireless communications (VAWC) enable proactive handovers (PHO) to mitigate such blockages; however, PHO becomes challenging when no nearby base station (BS) is available. In such cases, reconfigurable intelligent surfaces (RIS) can be used to restore connectivity. To ensure timely PHO, the RIS configuration time must be taken into account, as the large number of RIS elements can limit responsiveness in time-sensitive scenarios. This work proposes a novel RIS-assisted PHO approach that optimizes the number of allocated RIS elements to balance signal processing complexity and link quality under handover timing constraints, making the RIS-assisted link more energy-efficient. An optimization problem based on particle swarm optimization (PSO) is formulated to determine the optimal end-to-end RIS link setup that runs offline to bypass latency constraints. Results show that reducing the number of RIS elements by 12\% leads to a 10\% decrease in dissipated energy without compromising the signal-to-noise ratio (SNR). Moreover, the RIS-assisted link achieves a 15--30 dB improvement in blocked regions while maintaining accurate PHO timing.

---


### 160. [Optimizing Human-Machine Interface for Real-Time AI Support in the Operating Room: the CVS Copilot](https://arxiv.org/abs/2606.26886)

**<font color=#1a73e8>作者：</font>** Lorenzo Arboit, Nicolas Chanel, Aditya Murali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems for automated Critical View of Safety (CVS) assessment in laparoscopic cholecystectomy are nearing clinical translation. Beyond algorithmic performance, clinical safety and effectiveness depend on the quality of the human-machine interface (HMI). This work examines how AI-generated predictions should be presented and controlled intraoperatively. Seventeen surgeons, including residents, attending surgeons, and professors, took part in a mixed-methods, user-centered design study to optimize an intraoperative HMI for AI-assisted safe laparoscopic cholecystectomy. Interviews explored interaction modalities, timing of assistance, visualization strategies, and control mechanisms across surgical roles, and were analyzed using reflexive thematic analysis and human-factors heuristics. Most surgeons (16/17) supported the use of AI for intraoperative decision support while rejecting autonomous decision-making. Attendings preferred minimal AI feedback at decisive moments (13/14), whereas residents favored optional guidance (3/3) with confidence indicators and on-demand anatomical overlays. Across interviews, surgeons consistently prioritized visual, surgeon-controlled, minimally intrusive displays, with the strongest support for a minimal overlay (16/17) and on-demand anatomical segmentation (13/17). Recurrent concerns included persistent overlays, haptic feedback, and numeric confidence displays, although these were not uniformly raised across the cohort. These findings informed the design of CVS Copilot, a surgeon-controlled, role-adaptive HMI that provides AI-based CVS assessment with minimal default visualization and optional overlays.

---


### 161. [Bridging Vision and Language Concepts through Optimal Transport Semantic Flow](https://arxiv.org/abs/2606.26891)

**<font color=#1a73e8>作者：</font>** Chenyang Zhang, Anqi Dong, Guangming Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) promise transparent reasoning by predicting through human-interpretable concepts, yet their effectiveness fundamentally depends on how well visual and textual representations are aligned or matched. Existing vision-language CBMs often rely on pre-aligned encoders or global cosine similarity, which obscures fine-grained concept localization and fails to reflect true semantic geometry. In this work, we rethink concept alignment as a dynamic cross-modal transport process instead of static projection and propose the Optimal Transport Flow Concept Bottleneck Model (OTF-CBM). It first learns a data-driven semantic cost via Inverse Optimal Transport to measure cross-modal distances, and then performs unbalanced optimal-transport-based flow matching to model semantic transitions between visual patches and textual concepts. With velocity-based concept activation, OTF-CBM captures interpretable geometric relations without ODE integration. Experiments further show that OTF-CBM achieves superior classification accuracy and concept faithfulness, offering a new geometric and dynamical perspective for interpretable cross-modal reasoning.

---


### 162. [Asymptotically Optimal Learning for Parametric Prophet Inequalities](https://arxiv.org/abs/2606.26893)

**<font color=#1a73e8>作者：</font>** Jung-hun Kim, Anna Grebennikova, Vianney Perchet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning in prophet inequalities with i.i.d. rewards drawn from an exponential-type parametric family with an unknown parameter $\theta$, a class that includes exponential, Pareto, and bounded-support power-family distributions. We first characterize the optimal full-information asymptotic competitive ratio for this family. In the unbounded-support case, the limit is $ {\left({\theta}/({\theta-c_+})\right)^{c_+/\theta}}/ {\Gamma(1-c_+/\theta)},$ while in the bounded-support case, the limit is $1$. We then propose a confidence-based dynamic-programming policy for online learning. By exploiting the explicit parametric structure, the policy achieves the same optimal asymptotic competitive ratio using only online observations, without external offline samples. We further derive distribution-specific convergence rates for canonical examples. Finally, numerical experiments on synthetic instances illustrate the performance of our algorithm.

---


### 163. [Tractography-Driven Synthetic Data Generation for Fiber Bundle Segmentation in Tracer Histology](https://arxiv.org/abs/2606.26898)

**<font color=#1a73e8>作者：</font>** Kyriaki-Margarita Bintsi, Sparsh Makharia, Yaël Balbastre 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion MRI (dMRI) tractography enables non-invasive reconstruction of white-matter pathways, but its accuracy is fundamentally limited by indirect, low-resolution measurements of axonal organization. Tracer injection studies in non-human primates provide a gold standard for validating dMRI tractography. This, however, requires time-consuming manual annotation of fiber bundles in histology sections. We propose a synthetic-data augmented framework for automated fiber bundle segmentation in macaque tracer histology. Our approach uses ex vivo dMRI tractography as a generative prior to synthesize 2D image patches for training. This provides us with sufficiently realistic foreground texture, which we compose with backgrounds from blockface photos and diversify via domain randomization. A 2D U-Net is trained on mixed real and synthetic patches. Experiments on held-out brains demonstrate improved generalization across brains and fiber bundle densities compared to training with real data only. Training with synthetic data only leads to poor performance, underscoring the need for real supervision. Overall, our approach achieves performance comparable to the state-of-the-art while requiring 3x less manually annotated data.

---


### 164. [Generative Retrieval via Diffusion Transformer with Metric-Ordered Sequence Training and Hybrid-Policy Preference Optimization](https://arxiv.org/abs/2606.26899)

**<font color=#1a73e8>作者：</font>** Chenghao Liu, Yu Zhang, Zhongtao Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embedding-based retrieval ranks items by their similarity to a query in a shared vector space and usually aims to return the highest-scoring items. In many production settings this is not what is wanted: given a seed set that expresses a fine-grained pattern, one needs more items that both satisfy a target attribute and stay within that pattern. We formalize this as pattern-preserving attribute retrieval. The two goals pull against each other: averaging the seeds preserves the pattern but stays in a low-attribute region, while global attribute retrieval drifts to unrelated patterns. We approach the task with continuous generative retrieval, where a model reads a sequence of item embeddings and generates query embeddings for nearest-neighbor search. We propose MO-DiT+HPPO, a staged framework with raw-sequence pretraining, multi-domain metric-ordered continuation pretraining, tail-centroid fine-tuning, and HPPO. Metric-ordered training turns sparse online retrieval labels into in-pattern trajectories ordered from low to high predicted attribute density, teaching one model the metric-improvement direction across domains. HPPO aligns the generated query distribution with the true online objective by labeling a hybrid candidate pool with the online intersection metric and applying reference-anchored preference optimization. A Pareto pair filter keeps only winner pairs that do not lower same-pattern purity, raising the attribute metric without sacrificing the pattern. Across four attribute domains under item- and pattern-holdout protocols, metric-ordered DiT improves the intersection metric over a pretrained generative retriever, and HPPO improves it further, with significant gains on seven of eight domain-split cells and a marginal tie on the hardest split. Metric-predictor validation, order ablations, CPT/SFT comparisons, and a candidate-policy ablation show where the gains come from.

---


### 165. [SamaVaani: Auditing and Debiasing Multilingual Clinical ASR for Indian Languages](https://arxiv.org/abs/2606.26901)

**<font color=#1a73e8>作者：</font>** Subham Kumar, Prakrithi Shivaprakash, Abhishek Manoharan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) is increasingly used to document clinical encounters, yet its reliability in multilingual and demographically diverse Indian healthcare context remains largely unknown. In this study, we first conduct the systematic audit of ASR performance on real-world psychiatric interview data spanning Kannada, Hindi and Indian English, comparing eight state-of-the-art models including IndicWhisper, WhisperLargeV3, Sarvam, GoogleS2T, Gemma3n, OmniLingual, Vaani, and Gemini. Our results reveal substantial variability across models and languages, with some systems performing competitively in Indian English but failing in regional speech. We further fine-tune two of the best performing opensource models, i.e., Gemma3n and OmniLingual, using various methods. With this, we uncover systematic performance gaps tied to speaker role and gender, raising concerns about equitable deployment in clinical settings, which are further mitigated by fairness-aware fine-tuning. To this end, we propose SamaVaani, a unified debiasing technique that simultaneously improves ASR performance and improves fairness across demographic groups.

---


### 166. [Learning to Recover Task Experts from a Multi-Task Merged Model](https://arxiv.org/abs/2606.26902)

**<font color=#1a73e8>作者：</font>** Jinwook Jung, Taegyu Kim, Kumju Jo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-task model merging aims to consolidate several task-specific experts into a unified model, yet static merging consistently suffers from parameter interference. While dynamic merging models aim to bridge this gap, many works rely on the costly storage and loading of redundant expert components at inference. In this work, from the perspective of task expert, we view parameter interference as parameter perturbation introduced to each expert during merging process. We show that such parameter perturbations can be modeled as affine transformation, which can be approximated as additive offsets. Motivated by these, we propose Recover Task eXpert (ReTeX), a framework that predicts those offsets, in order to undo parameter interference and recover task-expert performance from a single merged checkpoint. To recover the appropriate expert when task identity is unknown, we introduce a router-free task identifier based on SVD subspace signatures computed offline before inference. At inference, the identifier selects the task whose subspace yields the smallest projection residual for a given input. As a result, ReTeX recovers over 95% of individual-expert performance in both vision and NLP domains, while significantly improving generalization to unseen tasks. Crucially, we also show that the parameter offset prediction leads to emergent adaptive interpolation of expert knowledge for out-of-distribution (OOD) tasks. ReTeX adaptively interpolates seen expert knowledge to handle unseen tasks. Our code is available at this https URL

---


### 167. [Diagnosing Task Insensitivity in Language Agents](https://arxiv.org/abs/2606.26918)

**<font color=#1a73e8>作者：</font>** Jingyu Liu, Xiaopeng Wu, Kehan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can serve as capable long-horizon agents, but their out-of-distribution (OOD) generalization remains weak. We identify a key source of this failure as task insensitivity: when faced with similar but distinct tasks, models might apply patterns learned during training and fail to solve the task at hand. We show that models often continue with actions aligned with the original task even when the instruction is semantically corrupted and cannot be directly answered. We further find that, when we replace the task description in a trained prompt with another similar but distinct task, the model may still output the same action. This behavior is accompanied by a consistent training-time attention drift away from task tokens and toward local observations, suggesting an optimization bias toward shortcuts. To mitigate this problem, we propose Task-Perturbed NLL Optimization, a lightweight contrastive regularizer that explicitly encourages action dependence on the task instruction. Extensive evaluations show that our intervention improves task sensitivity and OOD generalization while preserving more stable attention to task tokens.

---


### 168. [GAVEL: Grounded Caption Error Verification and Localization](https://arxiv.org/abs/2606.26923)

**<font color=#1a73e8>作者：</font>** Zixian Gao, Atsushi Hashimoto, Kuniaki Saito  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often produce hallucinated or inconsistent outputs, where text and images are not properly aligned. Addressing this issue requires not only detecting misalignment but also explaining the discrepancy and localizing its visual evidence. We introduce GAVEL (Grounded Caption Error Verification and Localization), a task that jointly addresses verification, explanation, and localization for image-text pairs. To support systematic evaluation, we also present a corresponding dataset and benchmark. We further train a supervised baseline on the human-annotated training split to assess whether GAVEL provides learnable supervision for these abilities. Experiments show that even strong closed-source models struggle on GAVEL, while the supervised baseline yields consistent improvements across grounding and explanation metrics.

---


### 169. [Game Changers: Designing and Measuring Dynamic Feedback To Help Users Self-Regulate in a VR Pointing Game](https://arxiv.org/abs/2606.26925)

**<font color=#1a73e8>作者：</font>** Bastian Ilsø Hougaard, Scott Bateman, Iris Brunner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The way games dynamically convey information through feedback is critical to players' ability to perform, learn, and improve. However, it is poorly understood how performance metrics impact player performance and perception in core game tasks like pointing or steering. With a virtual reality pointing task we systematically explored how three performance metrics driving the feedback affected players when rewarding short completion times, straight movements, or high peak speed. across different points in time - continuously, at end-of-action, or at end-of-task. On average the dynamic feedback helped people point more straight and faster, while for others it had small or opposite effect. The study quantitatively compared dynamic feedback across three forms with the metrics driving the form as the intended locus of quantitative comparison. Our work improves game designers basis for crafting dynamic feedback by helping them know when to employ feedback schemes that align with desirable game performance objectives.

---


### 170. [PortraitGen: Exemplar-Driven GRPO with Dual-Reward Guidance for Photorealistic Portrait Generation](https://arxiv.org/abs/2606.26930)

**<font color=#1a73e8>作者：</font>** Xiaomin Li, Qian Liang, Yinan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning like Group Relative Policy Optimization (GRPO) has significantly advanced text-to-image post-training. However, current methods often favor superficial aesthetics, such as over-saturated colors, leaving critical flaws like AI artifacts and biological implausibilities unresolved. We attribute these limitations to two primary factors: (1) The absence of real images during post-training confines GRPO sampling to the original distribution, failing to break inherent generative boundaries; (2) the optimization process lacks specific rewards targeting fine-grained artifacts like overly oily skin and other AI artifacts. To address this, we propose PortraitGen, a novel framework tailored for photorealistic portrait generation. First, we break inherent generative boundaries by directly introducing real images into the GRPO sampling groups, where image inversion is employed to obtain their transition probabilities and latents. Second, to explicitly steer the model toward photorealism, we introduce a complementary dual-reward mechanism: OmniReward for general quality and AI-Portrait for human-centric fidelity. Furthermore, we curate PortraitBench, a comprehensive portrait-centric benchmark. Extensive experiments demonstrate that PortraitGen significantly outperforms existing baselines, effectively suppressing AI artifacts and achieving unprecedented photorealism.

---


### 171. [Scaling Multi-Reference Image Generation with Dynamic Reward Optimization](https://arxiv.org/abs/2606.26947)

**<font color=#1a73e8>作者：</font>** Wenwang Huang, Yusen Fu, Junjie Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While personalized image generation has achieved remarkable progress, multi-reference image generation (MRIG) remains a challenging task. Most existing benchmarks fail to adequately evaluate complex MRIG scenarios, hindering further progress in this area. To better assess model performance on complex MRIG tasks, we introduce OmniRef-Bench, a benchmark that covers complex combinations of reference image types and a large number of reference images. Evaluations on OmniRef-Bench show that mainstream open-source models struggle in complex MRIG scenarios, and their performance deteriorates significantly as the number of mixed-type reference images increases. To address this issue, we propose DyRef, a two-stage training framework. In the first stage, supervised fine-tuning equips the model with the basic capability to handle complex MRIG tasks. In the second stage, we introduce Difficulty-aware Advantage Reweighting (DAR) and Discriminative Reward Scaling (DRS). DAR dynamically adjusts the optimization objective to improve performance when handling a large number of mixed-type reference images. DRS enlarges intra-group reward differences for more effective policy optimization. Experiments demonstrate that DyRef significantly improves the performance of open-source models on OmniRef-Bench and single-image editing benchmarks, demonstrating the effectiveness and generalization capability of our approach.

---


### 172. [What Holds Back Brain-Computer Interfaces? Uncovering Challenges and Opportunities in BCI-controlled Games for Cerebral Palsy Rehabilitation](https://arxiv.org/abs/2606.26951)

**<font color=#1a73e8>作者：</font>** Bastian Ilsø Hougaard, Kirstine Schultz Dalgaard, Kirstine Johanne Stougaard Klebæk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain-computer interfaces (BCIs) offer promising avenues for cerebral palsy (CP) rehabilitation at home and in the clinic, using games that promote engagement and sustained training effort. Nonetheless, the design constraints of BCI-based CP rehabilitation remain unclear, especially how individuals with CP experience a sense of control through BCI, and how they experience computer-mediated game assistance. To address this gap, we present preliminary clinical and user perspectives on BCI-based CP rehabilitation, drawing on in-clinic insights from a CP therapist and experiential accounts from ten individuals with CP engaging with BCI game prototypes. Sporadic help in BCI games eased monotony, but also fostered doubts regarding agency. The therapist saw BCI rehabilitation as complementary to traditional training, facilitating the transition from playful exercises to autonomous, self-managed training. We outline key challenges and opportunities to inform and empower further design and research of BCI training for CP.

---


### 173. [Term-Centric Hierarchy Induction from Heterogeneous Corpora](https://arxiv.org/abs/2606.26963)

**<font color=#1a73e8>作者：</font>** Elena Senger, Yuri Campbell, Jan-Peter Bergmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing knowledge from diverse text sources into interpretable hierarchies is crucial for tasks such as policy analysis, innovation monitoring, and exploratory domain mapping. Existing taxonomy induction methods typically rely on document-level representations that capture entire documents rather than the specific domain concepts relevant for knowledge organization, limiting their ability to generalize across heterogeneous sources. We propose a term-centric framework for inducing hierarchical taxonomies from heterogeneous corpora that scales to massive document collections. Our approach maps documents from diverse sources into a shared representation space using automatic term extraction, enabling robust cross-source alignment. Based on these representations, we construct interpretable hierarchies that integrate domain priors with datadriven clustering. Experiments on a novel English and German multi-source benchmark of over one million documents demonstrate that our method improves cross-source coherence and hierarchy quality over text- and summarybased baselines. A case study on German regional innovation analysis further demonstrates its practical utility for technology landscape mapping.

---


### 174. [Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds](https://arxiv.org/abs/2606.26964)

**<font color=#1a73e8>作者：</font>** Jiaming Bian, Bingliang Li, Yuehao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As embodied AI and world models increasingly operate in dynamic 3D environments, visual perception must move beyond passively interpreting given observations toward actively deciding what to observe. We study this problem through camera planning in dynamic 3D story worlds, where the camera must not only generate smooth motion, but also decide what visual evidence should be acquired before it moves. We formulate this capability as Narrative-Grounded World Visual Attention, where the camera acts as an embodied observer that determines what to observe, how to compose the observation, and how to shift attention over time under narrative intent and physical 3D constraints. To realize this capability, we propose Look-Before-Move, a camera planning framework that separates observation specification from motion execution. It first builds a Semantic Observation Contract to convert directorial intent into executable visual constraints, then performs Monte Carlo Viewpoint Search to find narrative-compliant and geometrically feasible viewpoints, and finally applies Semantic Trajectory Grounding to connect selected viewpoints into continuous, collision-aware, and temporally coherent camera motion. We further construct a dynamic 3D Story World Benchmark based on StoryBlender, covering 50 stories, 457 scenes, and 1585 shots with animated characters, semantic scene configurations, and executable 3D environments. Experiments show that our framework improves subject perception, intent consistency, and trajectory quality over representative baselines, demonstrating the importance of organizing visual attention before generating camera motion.

---


### 175. [Protocol Prying: Systematic Vulnerability Research in the Apple AirDrop and Android Quick Share Proximity Transfer Protocols](https://arxiv.org/abs/2606.26967)

**<font color=#1a73e8>作者：</font>** Arash Ale Ebrahim, Nils Ole Tippenhauer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Apple AirDrop and Google/Samsung Quick Share are proximity file-transfer protocols used by over five billion devices, yet their application-layer security properties remain largely unstudied because both stacks are proprietary and undocumented. Both protocols are reachable from wireless proximity without any prior pairing and process complex serialized content (binary plists, CPIO archives, Protocol Buffers, UKEY2 handshakes) inside privileged daemons, making them attractive zero-click targets across multiple operating systems. We perform the first cross-platform reverse engineering and protocol-aware fuzzing study of both stacks. We reconstruct AirDrop's seven-layer state machine and DVZip adaptive compression from binary analysis, build AIRFUZZ, a protocol-aware fuzzer that mutates pre-compression representations, and complement it with targeted hand-written analyses of Samsung's Quick Share service and Google's Quick Share for Windows. We discover six vulnerabilities (V1-V6): three pre-authentication issues in macOS/iOS AirDrop (V1: Swift fatalError DoS in the HTTP path router; V2: unbounded XML plist recursion in Foundation; V3: NULL dereference in this http URL's HTTP/1.1 parser), two protocol-layer flaws in Samsung Quick Share (V4: pre-authentication OfflineFrame dispatch; V5: D2D encryption bypass for three frame types), and a heap use-after-free in Google Quick Share for Windows (V6) for which Google awarded a bounty. We responsibly disclosed all findings, and Apple, Samsung, and Google have acknowledged the reports.

---


### 176. [RedVox: Safety and Fairness Gaps in Speech Models Across Languages](https://arxiv.org/abs/2606.26968)

**<font color=#1a73e8>作者：</font>** Beatrice Savoldi, Sara Papi, Wafa Aissa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-capable models are increasingly deployed in real-world applications across languages. Yet their safety and fairness beyond English settings and under naturalistic conditions remain understudied. We survey safety reporting practices across state-of-the-art speech model releases, finding that only 8% document any multilingual analysis. To address this gap, we introduce RedVox, a multilingual safety and fairness benchmark for audio and speech built on real voices, covering unsafe and unfair stereotypical requests across five languages (English, French, Italian, Spanish, and German). Evaluating eight state-of-the-art models, we find that vulnerabilities persist even under non-adversarial conditions, worsen in non-English languages, and are amplified when the request comes from a spoken input. Finally, by surveying the participants who contributed to RedVox, we document the unique personal and privacy challenges of collecting speech data with human participants, pointing to broader sociotechnical challenges in naturalistic speech safety research.

---


### 177. [Computer Vision for MOBA Analytics: A Dataset and Baseline for Visibility Analysis in Dota 2](https://arxiv.org/abs/2606.26970)

**<font color=#1a73e8>作者：</font>** Ricardo da Rocha Carvalho, Eloísa Oliveira, Luiz Bernardo Martins Kummer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Introduction: Most Multiplayer Online Battle Arena (MOBA) analytics studies rely on structured data, which does not directly capture what each team could actually see during a match. Objective: This work introduces Dota2-Vis, a video-based dataset, and a baseline pipeline for visibility analysis in professional Dota 2 matches. Methodology: The dataset comprises all 144 matches from The International 2025, recorded from both team perspectives, totaling 288 Full HD videos, together with 2,477 manually annotated minimap images. We evaluate multiple variants of a modern object detector for player-icon detection and use the best-performing model to estimate opponent-visible player presence over time. Results: YOLO11l (large) achieved the best overall performance, reliably identifying player icons even in dense and visually cluttered minimap scenes. The resulting visibility curves reveal player, hero, role, and team-level patterns that complement conventional MOBA analytics, highlighting behavioral differences that are difficult to obtain from structured data alone. The dataset and code are publicly available at this https URL.

---


### 178. [Geometric Gradient Rectification for Safe Open-Set Semi-Supervised Learning](https://arxiv.org/abs/2606.26973)

**<font color=#1a73e8>作者：</font>** Jiahe Chen, Qian Shao, Qiyuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set semi-supervised learning aims to leverage unlabeled data that may contain out-of-distribution outliers while maintaining performance on in-distribution classes. Existing methods mainly follow two paradigms: filtering suspicious samples or incorporating unlabeled objectives with soft weighting. We argue that both face a common trade-off: aggressive filtering can discard informative but hard ID samples, whereas utilization can introduce auxiliary gradients that conflict with supervised learning when pseudo labels are wrong. We therefore shift the focus from sample selection to gradient-level control. We propose \textit{Geometric Gradient Rectification} (GGR), a plug-in framework that uses the supervised gradient as an anchor and projects conflicting auxiliary gradients onto an admissible region in gradient space. This makes the applied auxiliary update first-order non-opposing within the rectified coordinate block while preserving orthogonal components that may still carry useful representation signals. We further extend GGR with subspace-aware rectification to stabilize the anchor under noisy mini-batch gradients. Experiments on CIFAR and ImageNet benchmarks show that GGR improves representative OSSL baselines in most settings and yields gains in both closed-set generalization and open-set robustness. Code will be available at this https URL.

---


### 179. [Decision-Aligned Evaluation of Uncertainty Quantification](https://arxiv.org/abs/2606.26990)

**<font color=#1a73e8>作者：</font>** Annika Schneider, Tommy Rochussen, Joshua Stiller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimates in machine learning are typically evaluated using generic metrics such as the negative log-likelihood and expected calibration error, yet good performance on such metrics does not necessarily imply high utility in downstream decisions. We introduce decision-alignment, a criterion that reveals which evaluation metrics meaningfully align with downstream utilities. Applying this framework, we show that many widely used uncertainty metrics are either misaligned with common decision problems or encode pathological prior beliefs about the downstream task. We then propose prior-weighted utility metrics, a special class of proper scoring rules that provides decision-aligned uncertainty evaluation. Across benchmark experiments and real-world case studies, our metrics consistently align with realized decision utility, while conventional metrics do not. Our results surface flaws in the current UQ evaluation protocol and offer a principled extension of existing metrics toward decision-relevant UQ evaluation.

---


### 180. [Event-Aware Instructed Assistant for Referring Video Segmentation](https://arxiv.org/abs/2606.26994)

**<font color=#1a73e8>作者：</font>** Jinyu Liu, Henghui Ding, Shuting He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing referring video segmentation methods often treat a video as a single event consisting of multiple images, overlooking the fact that a video typically contains multiple distinct events. Under such a mechanism, the model needs to directly understand all the complex content in the video and text, which can easily lead to confusion and hallucinations. To address this issue, we propose to decompose a video to a set of simple events by learnable Event Query, and understand complex video content in an event-by-event, easy-to-understand manner. This is based on the observation that natural language expressions often divide a video into distinct, text-related segments, each representing a separate event within a compound event. We introduce EVIS, an Event-Aware Video Instructed Segmentation Assistant, which utilizes text-guided Event Queries to partition a video into simple events, extracting event-aware visual-text features to achieve a hierarchical understanding of the video. Additionally, we propose Object-Pixel-Hybrid Learning, which enables the MLLMs to track targets in long-term videos by integrating fine-grained pixel features with prior object queries. Extensive experimental results on 5 public benchmarks demonstrate EVIS's strong performance in addressing the referring video segmentation task.

---


### 181. [Uncertainty quantification via conformal prediction in data assimilation](https://arxiv.org/abs/2606.27001)

**<font color=#1a73e8>作者：</font>** Catherine George, Alireza Javanmardi, Tijana Janjić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantifying the evolution of uncertainty is critical to both probabilistic forecasting and data assimilation in numerical weather prediction. In this study, we investigate the applicability of conformal prediction (CP), a recent machine learning (ML) method, to quantify uncertainty in a controlled, idealized setting. We use the one dimensional modified shallow water model, designed to mimic the convective process. CP provides a set of possible outcomes with a chosen confidence level. Here, we compare and evaluate the average empirical coverage, the average interval length, miss low, miss high and average interval score loss (AISL) for three variants of CP, namely a) Standard CP, b) Normalized CP and c) Conformalized Quantile Regression. We further compare these CP-based uncertainty estimates with traditional ensemble-based measures such as standard deviation intervals and ensemble spread. In addition, we investigate the integration of CP-derived uncertainty within the data assimilation cycle through CP perturbations. Our results highlight the strengths and limitations of each approach, providing insight into the effectiveness of CP to complement common ensemble-based uncertainty quantification in simplified atmospheric models.

---


### 182. [Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)](https://arxiv.org/abs/2606.27005)

**<font color=#1a73e8>作者：</font>** Rahul Umesh Mhapsekar, Ilias Cherkaoui, Lizy Abraham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI systems are increasingly deployed under non-stationary computational, demographic, and operational conditions in which static resource allocation strategies degrade both predictive performance and human-centric properties such as fairness and explainability. This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop this http URL framework continuously redistributes computational budget across a population of heterogeneous AI models so that the global utility, defined jointly over predictive performance, demographic parity, cost, latency, robustness, and interpretability, remains maximised under disruption. The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation. AURORA-AI achieves immediate recovery from the black-swan event compared to eighty-eight time steps for the Static baseline and twenty-two for Proximal Policy Optimisation, lifts the alpha-quantile and the super-quantile by twenty-nine and twenty-five percent respectively, simultaneously reduces the mean and maximum demographic parity gap, and increases the fraction of Lyapunov-stable operating steps. These results indicate that fairness-aware adaptive orchestration grounded in stability theory is a practical and theoretically motivated path toward resilient human-centric AI deployment.

---


### 183. [Improving General Role-Playing Agents via Psychology-Grounded Reasoning and Role-Aware Policy Optimization](https://arxiv.org/abs/2606.27025)

**<font color=#1a73e8>作者：</font>** Zhenhua Xu, Dongsheng Chen, Jian Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building general-purpose role-playing agents that faithfully portray any character from a natural-language profile remains challenging. The dominant paradigm -- supervised fine-tuning -- encourages behavioral mimicry without deep, human-like internal thought processes, resulting in poor out-of-distribution generalization. Therefore, we propose \textbf{Psy-CoT}, a psychology-grounded chain-of-thought framework that decomposes pre-response reasoning into three role-specific steps -- \emph{Interaction Perception}, \emph{Psychological Empathy}, and \emph{Logical Construction} -- so that the model \emph{thinks dynamically} from the profile rather than merely mimicking surface patterns. While structured reasoning provides a foundation, it alone is insufficient; reinforcement learning is essential to further align the model with character fidelity. However, we observe that under LLM-based reward models, both generic phrases that hack the reward model and genuinely role-specific phrases receive identical gradient signals -- this hacking accumulates over training, misleading the model into treating both as equally optimal choices. To address this, we propose \textbf{Role-Aware Policy Optimization (RAPO)}, which uses profile--token mutual information to weight gradients asymmetrically -- amplifying role-specific tokens under positive advantage while attenuating them under negative advantage. Experiments on CoSER, CharacterBench, and CharacterEval demonstrate that Psy-CoT outperforms existing role-playing CoT methods, and RAPO consistently surpasses GRPO across multiple model scales.

---


### 184. [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/abs/2606.27027)

**<font color=#1a73e8>作者：</font>** Liwei Liu, Tianzhu Han, Zijian Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of LLM-driven agents, Model Context Protocol (MCP), an open protocol bridging LLMs with external tools, has quickly become foundational to modern agent ecosystems. However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts. Existing poisoning schemes typically adopt a monolithic plaintext embedding paradigm, which fails to withstand manual inspection or automated detectors. Current research still lacks a systematic analysis on multi-tool poisoning, where multiple tools can be exploited cooperatively to disperse detection risk. In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. After a covert reconstruction trigger is planted during server update, the aggregated shares reconstruct the hidden instruction, resulting in critical breaches of system assets or private data. To evaluate the realistic threat of ShareLock, we constructed a comprehensive benchmark encompassing four multi-tool scenarios and conducted extensive experiments across mainstream LLMs on two distinct MCP clients. Our results demonstrate that ShareLock significantly outperforms existing single-tool poisoning strategies in tool description-based detection while maintaining an average attack success rate exceeding 90%.

---


### 185. [Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation](https://arxiv.org/abs/2606.27028)

**<font color=#1a73e8>作者：</font>** Bhavya Dixit, Aayushi Rajgor, Subham Kumar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) swarms rely on distributed coordination and cooperative communication to support scalable operations, extended coverage, and applications such as surveillance and real-time data exchange. Wireless technologies such as radio frequency (RF) and WiFi are widely used for UAV-to-UAV and UAV-to-ground control station (GCS) communication but introduce significant security challenges. MAVLink, the predominant communication protocol in UAV systems, provides message integrity and authentication but lacks built-in encryption, leaving telemetry traffic vulnerable to eavesdropping. In our previous work, we proposed MAVShield, a lightweight encryption framework for MAVLink communications. In this paper, MAVShield, AES-CTR, Speck-CTR, ChaCha20, and Rabbit are integrated into four custom-built UAVs to establish secure communication links over RF and WiFi channels. Their performance is evaluated through flight experiments using a UAV swarm testbed. Encrypted telemetry data enable autonomous formation control and collision avoidance during flight. For collision avoidance, we develop a modified artificial potential field (APF) algorithm that computes attractive and repulsive forces directly in geodetic coordinates, eliminating Cartesian transformations and reducing trajectory oscillations while avoiding local-minimum trapping. CPU utilization, memory consumption, and packet delivery ratio (PDR) are measured for each encryption scheme. Results show that MAVShield achieves performance comparable to unencrypted communication while outperforming AES-CTR, Speck-CTR, ChaCha20, and Rabbit in overall efficiency. Algebraic cryptanalysis and Wireshark-based traffic analysis demonstrate resistance to key-recovery attacks and protection of telemetry confidentiality. The results indicate that MAVShield is an efficient and secure solution for UAV swarm communication.

---


### 186. [Symplectic Neural Networks for learning Generalized Hamiltonians](https://arxiv.org/abs/2606.27029)

**<font color=#1a73e8>作者：</font>** Harsh Choudhary, Vyacheslav Kungurtsev, Chandan Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hamiltonian Neural Networks (HNNs) integrate physical priors into neural models by learning a system's Hamiltonian, improving generalization and sample efficiency. Identifying the system Hamiltonian from noisy observations of state variables is a challenging task. For simulations to faithfully reflect the long-term behavior of Hamiltonian systems, especially energy conservation, it is essential to use symplectic integrators, which preserve the system's geometric structure. This fidelity comes at a cost: implicit symplectic integrators are more computationally intensive and make backpropagation through the ODE solver non-trivial. However, by leveraging the fact that symplectic discretizations of the adjoint system yield the same sensitivities associated by backpropagation, we obtain an efficient method of training the Neural Network parameters. In our work, we explore this alternate method of HNN training under noisy observation of trajectories with our HNN model based on an implicit symplectic integrator. Computationally, a predictor-corrector based ODE solver and fixed point iteration help to mitigate the computational cost of the implicit timestepping, resulting in more efficient generation of gradient updates. We showcase the numerical advantage, in experiments, in system identification and energy preservation on a range of non-separable, chaotic systems and the efficient computation and memory complexity of our method. We also observe that the post-processing of the learned Hamiltonian using backward error analysis yields a modified Hamiltonian that is a more accurate approximation of the true Hamiltonian without the need to use more accurate discretizations of the flow map.

---


### 187. [State Representation Matters in Deep Reinforcement Learning: Application to Energy Trading](https://arxiv.org/abs/2606.27032)

**<font color=#1a73e8>作者：</font>** Jesper Klicks, Sander Vržina, Vincent François-Lavet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy trading decisions depend not only on current market prices, but also on expected future market conditions, and operational constraints. This makes the state representation given to a reinforcement learning agent an important design choice. We study this in HydroDam, a pumped-storage arbitrage environment, using a fixed Double DQN agent. The environment, action space, reward function, network, and training protocol are kept fixed; only the market features are changed. We compare absolute price/calendar features, relative features that compare current prices with recent market history, forecast features, and all combinations of these three feature families. Policies are trained and selected using 2007--2011 Belgian day-ahead prices and evaluated on two test settings: a later same-market test set from 2012--2025 and 39 other ENTSO-E market zones. Absolute features only reaches 28.8% on the test set and a median 5.7% across zones. Relative-only and forecast-only states also stay below a rolling price-score heuristic in the cross-zone median. Combining feature families is much stronger: absolute + relative reaches 49.9% on the test set and a 39.8% cross-zone median, while absolute + relative + forecast reaches 55.6% and 47.5%. These results suggest that state representation is not a minor preprocessing choice in storage-trading RL, but a central part of the policy design: robust transfer requires combining price scale, recent relative price context, and short-horizon forecast information, rather than relying on any single feature family.

---


### 188. [Physical Layer Authentication With Channel Knowledge Maps in Indoor Environments](https://arxiv.org/abs/2606.27044)

**<font color=#1a73e8>作者：</font>** Luca Bonaventura, Francesco Ardizzon, Stefano Tomasin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical layer authentication (PLA) allows to authenticate the user by comparing measurements over time, assuming their time consistency or by modeling their evolution. However, these assumptions become problematic when devices are in motion and in indoor environments due to multipath propagation and obstructions. In this paper, we propose a PLA mechanism for moving devices in indoor environments, where multiple access points (APs) estimate the dominant channel tap path loss (PL) and angle of arrival (AoA) from the received signals and compare them with previously collected channel knowledge maps (CKMs). Specifically, the measurements are compared to those in the neighborhood of the previously known position obtained from CKMs. A comprehensive security analysis is conducted under both random and optimal attacks. Numerical results in a representative indoor scenario, with CKM obtained via ray tracing, validate the effectiveness of the proposed PLA approach.

---


### 189. [Type-based information flow analysis for $π$-calculus with a dynamically extensible security lattice](https://arxiv.org/abs/2606.27059)

**<font color=#1a73e8>作者：</font>** Yukihiro Oda, Eijiro Sumii  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We develop a type system for secure information flow where new security levels can be created and inserted into the security lattice dynamically, i.e., even in the middle of an execution of a system. Our system is formalized by extending Kobayashi's type-based secure information flow analysis for Milner's pi-calculus, which is one of the most expressive models (or "languages") supporting both sequential and concurrent computations, with concise syntax, reduction-based semantics, and bisimulation equivalence as a robust formalization of secrecy as non-interference. The development required careful treatment of extensions of lattices themselves as well as deliberate generalization from the simple 2-element lattice (consisting of only High and Low) in the original system.

---


### 190. [How to evaluate clustering with ground truth?](https://arxiv.org/abs/2606.27061)

**<font color=#1a73e8>作者：</font>** Pasi Fränti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External indexes can be used for cluster evaluation when ground truth is available. We review the most common external validity indexes focusing on set-matching-based measures. We recommend centroid index (CI), because it is an intuitive cluster-level measure with an explainable result. If we need a more fine-tuned, point-level measure, there are more choices. Pair-set index (PSI) provides a normalized score which is not biased by cluster sizes. If all points should matter equally, then clustering accuracy (ACC) or any other set-matching measure is suitable.

---


### 191. [Floor Raiser or Ceiling Limiter? Differential Storytelling Outcomes with a Child-Centric GenAI System Across Individual Differences](https://arxiv.org/abs/2606.27067)

**<font color=#1a73e8>作者：</font>** Min Fan, Wanqing Ma, Xinyue Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) holds promise for democratizing creative literacy, yet whether it benefits all children equally remains unclear. Using a child-centric GenAI storytelling system for children aged 7-12, we conducted a mixed-methods within-subjects experiment (N = 40, Grades 2-6) comparing GenAI-assisted and traditional storyboard conditions. Three findings emerged. First, the GenAI-assisted condition was associated with a floor-raising convergence pattern, with the quality gap narrowing by 83.5%, driven by lower-end support and upper-end constraint mechanisms. This convergence was dimension-selective, improving creativity and richness while leaving coherence and narrative structure tied to baseline performance. Second, younger children more often selected semantically distant keywords while older children preferred semantically closer ones, although engagement orientation varied across individuals regardless of age. Third, image regeneration was positively associated with structural quality dimensions, though this association was attenuated after baseline control. We propose mechanism-contingent scaffolding as a design principle for adaptive GenAI storytelling systems serving diverse children.

---


### 192. [Towards Explainable Adjudicative Variance: Quantifying Judicial Discretion via Gated Multi-Task Learning](https://arxiv.org/abs/2606.27069)

**<font color=#1a73e8>作者：</font>** Stanisław Sójka, Felix Steffek, Matthias Grabmair  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal outcome prediction must disentangle objective case facts from adjudicative context. Merit-based rulings rely on factual evidence while technical disposals may hinge on judicial discretion. We propose a Judge-Aware Gated Multi-Task Learning architecture that explicitly models this distinction. We introduce a fine-grained outcome taxonomy to supervise the encoder, enforcing a structural regularization that disentangles distinct semantic pathways. This granular legal curriculum enables our Gated Fusion mechanism to dynamically modulate reliance on judge identity. We evaluate our approach on 13,937 UK Employment Tribunal decisions. We benchmark our design against supervised fine-tuning (SFT) of a Gemma-4 26B-A4B backbone, in which judge identity and the taxonomy are injected as prompt tokens or autoregressive output targets. The two contextual signals compose only weakly when forced through a single autoregressive channel. In contrast, coupling a LoRA-adapted Gemma-4 encoder with our gated architecture defines a new state of the art on this benchmark while requiring an order of magnitude fewer trainable parameters than the generative SFT baselines, with gains concentrated on the most ambiguous and rarest outcome classes. Beyond accuracy, the architecture is interpretable; learned judge embeddings and calibration profiles localize the cases where adjudicative context drives the prediction. These results indicate that, for identity-conditioned classification of legal outcomes, the choice of conditioning interface dominates scale: differentiable structured composition yields more accurate, more parameter-efficient models than prompt-based composition over a substantially larger backbone.

---


### 193. [PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071)

**<font color=#1a73e8>作者：</font>** Zhisong Xu, Takeshi Oishi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization. Given only a few panoramic images, PanoImager decomposes them into local perspective views, synthesizes auxiliary observations to enrich sparse evidence, and stabilizes Gaussian optimization for improved cross-view consistency. Experiments on multiple benchmarks show improved stability under extreme sparsity, suggesting PanoImager as an offline/background component for map refinement when SfM/SLAM fails to initialize.

---


### 194. [Urban Context and Travel Experience Events: An Exploratory Comparison of Two German Cities](https://arxiv.org/abs/2606.27077)

**<font color=#1a73e8>作者：</font>** Marie Güntert, Esther Bosch  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The presented study investigates events influencing public transportation experience in both urban (Hamburg) and rural (Tuttlingen) areas in Germany, with the aim of identifying events that affect travel experience and as a result travel behavior. Using a mobile application, 21 participants in Tuttlingen and 70 participants in Hamburg tracked everyday trips, providing real-time evaluations of travel experiences along with situational data. Multi-level regression analyses were applied to assess the impact of events such as punctuality, capacity offer, information about public transportation and others on the ontrip experience. Results indicate that a sufficient public transportation capacity offer has the strongest positive effect in Tuttlingen, whereas a lack of punctuality and low personal well-being have the strongest negative effects. In Hamburg, a lack of punctuality and a negative information event have the largest impacts. These identified effects provide a foundation for decision-making and measures to improve local public transportation.

---


### 195. [Finding Stationary Points by Comparisons](https://arxiv.org/abs/2606.27082)

**<font color=#1a73e8>作者：</font>** Helin Wang, Chenyi Zhang, Xiwen Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of finding stationary points of non-convex functions when access to the objective is provided only through a comparison oracle that, given two points, outputs which has the larger function value. For a twice differentiable $f\colon\mathbb R^n\to\mathbb R$ with Lipschitz gradient and Hessian, we develop an algorithm that visits an $\epsilon$-stationary point using $\widetilde O(n^2/\epsilon^{1.5})$ queries. Our approach uses a subroutine that estimates the normalized Hessian to accuracy $\delta$ using $\widetilde O(n^2\log(1/\delta))$ queries. We further study this problem with a quantum comparison oracle model where queries can be made in superpositions, and develop the first quantum algorithm that finds an $\epsilon$-stationary point, which takes $\widetilde O(n/\epsilon^{1.5})$ queries.

---


### 196. [Pseudo-Text-Conditioned 3D Grounding DINO for Organ Localization in Abdominal CT](https://arxiv.org/abs/2606.27084)

**<font color=#1a73e8>作者：</font>** Siqi Chen, Han Gong, Keyi Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable organ localization in abdominal CT can provide spatial priors for downstream trauma analysis. We propose CT-3GDINO, a lightweight 3D detector that adapts a Grounding-DINO-style query-based architecture to fixed organ localization using frozen pseudo-text class tokens instead of a real text encoder. The model combines a Swin3D visual backbone, bidirectional feature enhancement, pseudo-text-guided query selection, and a cross-modality decoder to predict normalized 3D boxes for liver, spleen, left kidney, right kidney, and bowel. We train and evaluate on 193 matched RSNA/RATIC CT volumes with segmentation-derived boxes. The best multi-scale model, trained from scratch, achieves 0.5830 overall top-1 class-wise mAP over 3D IoU thresholds from 0.1 to 0.7, outperforming fixed- and trainable-backbone classification-pretrained variants with 0.5570 and 0.4657 mAP. Performance is strong for coarse localization, with 0.9649 AP at IoU 0.1, but remains limited for strict box alignment, with 0.1552 AP at IoU 0.7. These results establish CT-3GDINO as an open-source baseline for pseudo-text-conditioned 3D organ localization and motivate future work on localization-aware pretraining, richer multimodal conditioning, and injury-focused detection.

---


### 197. [SubdivAR: Autoregressive Next-Scale Prediction for Neural Mesh Subdivision](https://arxiv.org/abs/2606.27088)

**<font color=#1a73e8>作者：</font>** Huipeng Guo, Zikai Song, Hang Long 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mesh subdivision is a fundamental operation for converting coarse, editable meshes into high-resolution surfaces, with broad applications in digital asset creation. Classical rule-based schemes rely on fixed local refinement rules and often produce over-smoothed surfaces. Recent neural subdivision methods improve detail synthesis, but remain constrained by local modeling and exhibit limited generalizability. We present SubdivAR, a neural mesh subdivision framework based on our proposed Mesh Autoregressive Representation (MAR). MAR arranges meshes at different subdivision levels into an ordered scale sequence, reformulating subdivision as autoregressive next-scale prediction. To support this formulation, we introduce a Hybrid Topology-Aware Transformer that combines global semantic attention with topology-constrained local feature aggregation. SubdivAR adopts a next-scale coordinate prediction paradigm, regressing vertex offsets at each refinement stage to preserve subdivision topology while recovering fine-grained geometric details. To enable reliable learning, we construct FII-40K, a curated dataset of nearly 40,000 high-quality meshes with multi-level subdivision supervision. Experiments show that SubdivAR outperforms state-of-the-art baselines, reducing Hausdorff Distance and Chamfer Distance by 18.8% and 14.2%, respectively, and demonstrates strong robustness on complex open-surface geometries.

---


### 198. [TMP: Tree-structured Mixed-policy Pruning for Large-scale Image Generation and Editing](https://arxiv.org/abs/2606.27089)

**<font color=#1a73e8>作者：</font>** Peizhen Zhang, Yang Li, Xunsong Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image generation model rapidly grows their sizes to meet high-fidelity image synthesis. However, they gradually become unaffordable for their enormous parameter consumption and computation budget that lead to massive resources requirement and gpu memory footprint. In this paper, we propose TMP, the first Tree-structured Mixed-policy Pruning framework that generalizes prevalent image tasks (T2I and TI2I) and architectures (Mixture-of-Experts (MoE) and Diffusion transformer (DiT)). It could be applied to the step-distilled models and contribute as the last stage. We perform experiments upon current open-sourced SOTA HunyuanImage-3.0 instruct and a popular efficient model Z-Image turbo. The proposed pruning framework manages to compress HunyuanImage 3.0 from 80B to 20B parameters at 75% reduction ratio, sacrificing limited generation quality. We also optimize to enable the inference of the pruned 20B version of HunyuanImage 3.0 on a single 24GB 4090 GPU by engineering skills. The inference script and model weight have been integrated into the existing HunyuanImage3.0 open-source github and huggingface repository. Besides, we prove the efficacy of TMP by compressing Z-Image turbo from 6B to 4B (33% reduction) with negligible degradation.

---


### 199. [zQR: A Verifiable QR-Driven zkSNARK Proof Verification Framework for Mobile Platforms](https://arxiv.org/abs/2606.27092)

**<font color=#1a73e8>作者：</font>** Goshgar Can Ismayilov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy is one of the fundamental rights of individuals in modern societies. Yet, the practical adoption of privacy-preserving technologies in daily interactions remains limited. Zero-knowledge proofs offer strong privacy guarantees but are often hindered by their technical complexity. In this paper, we advance the idea of verifiable QR codes that enable off-line verifiers to verify proofs encoded in QR codes. Based on this core idea, we build a novel QR-driven zkSNARK proof verification framework (i.e., zQR) for mobile platforms. The framework integrates blockchain for auditability, non-repudiation and logging; and large-language models for automatic circuit generation. We perform a security discussion of the framework by considering multiple attack surfaces. Furthermore, we present an experimental evaluation measuring temporal costs (proof generation and verification latency, QR code encoding and decoding latency) and financial costs (blockchain gas consumption). Our results demonstrate the feasibility of zQR as a proof-of-concept framework for privacy-preserving verification on mobile platform where proofs are compactly represented with QR code symbol version of 19 with low error correction level. Finally, we discuss potential applications, current limitations and future directions for the broader adoption of privacy-preserving technologies in daily interactions.

---


### 200. [Data-Free Reservoir Features for Efficient Long-Horizon Cold-Start Continual Learning](https://arxiv.org/abs/2606.27095)

**<font color=#1a73e8>作者：</font>** Augustinas Jučas, Yangchen Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold-start exemplar-free class-incremental learning requires learning a growing set of classes without replay, external pretraining, or a large initial task. Existing cold-start methods typically either train the backbone throughout the stream and compensate for semantic drift, or freeze a backbone after the first task, producing features biased toward the initial classes. These choices also create a computational tension: drift-compensation methods require repeated backbone training and increasingly expensive updates as the task horizon grows, while frozen-backbone methods are cheap but weak under cold start. We study a third option: a feature extractor that is never fit to image data at all. We propose CIRCLE, a class-incremental classifier built from fixed bidirectional two-dimensional reservoir features, adapted from BiRC2D for image classification, and streaming linear discriminant analysis heads. CIRCLE groups multiple random reservoir instantiations into feature ensembles and averages the softmax outputs of independent SLDA heads, yielding a tunable bias-variance tradeoff between richer random features and prediction-level ensembling. Because the feature extractor is fixed and the head admits streaming closed-form updates, CIRCLE performs sample-wise training without replay, task-boundary information, or backbone backpropagation. On CIFAR-100, TinyImageNet, ImageNet-Subset, and ImageNet-1k, CIRCLE is competitive at 10-20 task splits and substantially outperforms strong CS-EFCIL baselines at 50, 100, and 500 task splits, while training much faster than trained-backbone drift-compensation methods. Ablations show that the BiRC2D-style extractor, SLDA head, and balanced feature/prediction ensembling each contribute to the final performance.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-245](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
