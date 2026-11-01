# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 251. [CASE: Concept-Aware Segmentation from Positive and Negative Visual Exemplars](https://arxiv.org/abs/2610.39396)

**<font color=#1a73e8>作者：</font>** Yi-Jen Tsai, Yen-Yu Lin, Chien-Yao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot semantic segmentation typically identifies target objects based on positive support examples of a single semantic class. In practice, however, positive cues alone are often underspecified: for instance, "red cars" may be confused with cars of all colors, "vehicles" may include cars that should be excluded, and "material-defined objects" may span multiple categories. Fulfilling precise requests requires positive exemplars to provide inclusion evidence and negative exemplars to act as intent-defining constraints for exclusion and disambiguation. We formulate this setting as Specified Visual Prompt Segmentation (SVPS), where the target concept is specified by both positive and negative visual prompts. In this work, visual exemplars refer to support-image regions specified by bounding-box prompts. To study SVPS, we introduce CASE (Concept-Aware Segmentation from Positive and Negative Visual Exemplars), a benchmark built on COCO and PACO. CASE encompasses six category- and attribute-level task families: exclusion, isolation, union, attribute exclusion, attribute isolation, and attribute union. We evaluate SAM 3 under this setting and find that, despite its powerful positive-only few-shot segmentation capability, frozen SAM 3 does not consistently treat negative visual prompts as exclusion evidence. To address this, we present Concept Prompt Adaptation (CPA), a conservative LoRA-based adaptation baseline that improves positive-negative prompt interpretation on CASE while remaining competitive under positive-only few-shot segmentation. Code is available at this https URL.

---


### 252. [ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.39399)

**<font color=#1a73e8>作者：</font>** Houqiang Zhong, Tianchi Zhu, Qiang Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a powerful paradigm for real-time photorealistic novel view synthesis. However, its training-time densification remains largely heuristic, often resulting in redundant Gaussian proliferation and inaccurate geometric reconstruction. Existing methods predominantly rely on first-order screen-space gradients to trigger cloning and splitting, which fail to distinguish true geometric discontinuities from high-frequency textures or noisy residuals. To address this limitation, we propose ACD-GS, an Asymmetric Curvature-aware Densification framework for compact and geometry-aware 3D Gaussian optimization. Our key insight is that second-order depth responses provide a more reliable structural prior for density control, enabling asymmetric regulation of cloning and splitting to better capture geometric discontinuities. Building on this, we introduce a multi-view photometric consistency constraint to suppress transient single-view errors, together with a capacity-aware adaptive regulation strategy that balances densification and pruning during training. Unlike post-hoc compression or quantization-based approaches, ACD-GS directly prevents redundant Gaussian generation during training, yielding inherently compact representations. Extensive experiments demonstrate that our method reduces nearly 60% of Gaussian count and storage while maintaining competitive rendering fidelity, consistently outperforming existing methods across multiple datasets. Our code is available in this https URL.

---


### 253. [SymKL: A Unified Representation-Space Measure of Signal Degradation](https://arxiv.org/abs/2610.39403)

**<font color=#1a73e8>作者：</font>** Dhananjaya Jayasundara, Sudarshan Rajagopalan, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying degradation between a pristine signal and its degraded observation is fundamental to signal processing, yet existing full-reference measures are inherently modality-specific. We introduce SymKL, a unified full-reference degradation measure based on implicit neural representations (INRs). An INR is fitted once to the pristine reference and characterized by its diagonal Fisher information, which captures the local information geometry of the learned representation. Evaluating the Fisher information with the pristine reference and a degraded observation yields two parameter-sensitivity profiles whose symmetric KL divergence defines the degradation score. The proposed formulation requires only the reference and degraded observation, without knowledge of the corruption process or degradation severity, making it applicable across images, audio, and 3D data. We further derive an exact closed-form expression for the diagonal Fisher of SIREN, enabling efficient computation. Experiments on image, speech, and volumetric 3D benchmarks demonstrate that SymKL accurately tracks degradation severity, remains monotonic where conventional metrics saturate or fail, and provides a unified modality-agnostic measure of signal degradation. Code will be made publicly available after the review process.

---


### 254. [YOLOF-MLD: A Multi-Level Distillation Framework for Efficient Object Detection](https://arxiv.org/abs/2610.39408)

**<font color=#1a73e8>作者：</font>** Xiaolong Wu, Liming Zheng, Zitong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient object detection on resource-constrained edge devices is essential for safety-critical applications such as fire-smoke monitoring. However, current lightweight frameworks, such as YOLO26, still rely on the parameter-dense multi-branch Feature Pyramid Network (FPN), preventing full exploitation of their lightweight advantage. Replacing FPN with YOLOF's single-input-single-output (SiSo) neck is a promising solution but causes substantial accuracy loss. To alleviate this, we propose YOLOF-MLD, a CPU-efficient multi-level distillation (MLD) framework that combines a YOLO26n backbone, a SiSo neck, and MLD. It aligns features at the backbone via sliced-semantics matching, neck with receptive-field matching, and response levels. On D-Fire and Annotated Fire-Smoke (AFS) datasets, YOLOF-MLD reduces the parameter count of YOLO26n by 35.7\% and achieves a 62.3\% speedup on Raspberry Pi 5, attaining 71.6% and 59.9% mAP@50, respectively, compared with 75.5% and 60.0% for YOLO26n. These results demonstrate a competitive accuracy--latency trade-off for edge deployment. Our code is available at this https URL.

---


### 255. [Safe Multi-Objective Reinforcement Learning: Zero Constraint Violation and Primal-Averaging Convergence](https://arxiv.org/abs/2610.39409)

**<font color=#1a73e8>作者：</font>** Chenxi Li, Yao Shu, Siyang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many applications of multi-objective reinforcement learning (MORL) require policies that balance conflicting objectives while satisfying safety constraints. We study safe MORL with zero constraint violation throughout learning, covering both cumulative and stepwise constraints. A key challenge is to explore sufficiently under unknown dynamics and constraint costs without violating the constraints. For a given preference over objectives, we develop an algorithm to learn a safe Pareto optimal policy by combining optimistic reward estimates with pessimistic cost bounds. With high probability, every policy executed over $T$ episodes incurs zero constraint violation. The algorithm returns a safe Markov policy induced by the averaged occupancy measure and achieves an $\widetilde{O}(1/\sqrt{T})$ suboptimality gap under smooth Tchebycheff scalarization. We further develop a preference-free algorithm that first explores safely without a prespecified preference and then computes a safe policy for any given preference without further interaction. Over $T$ exploration episodes and $K$ planning iterations, it retains the same safety guarantee and achieves an $\widetilde{O}(1/\sqrt{T}+1/\sqrt{K})$ suboptimality gap. Both algorithms require knowledge of a policy that strictly satisfies the constraints and its costs. We then relax these requirements, incurring at most constant cumulative violation. To our knowledge, we provide the first sample-efficient MORL algorithms that guarantee safety for every executed policy.

---


### 256. [How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents](https://arxiv.org/abs/2610.39413)

**<font color=#1a73e8>作者：</font>** Yi Wen, Xiangjue Dong, Bingxuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents (DRAs) conduct long-horizon reasoning, search, and literature synthesis to provide long-form answers to complex, domain-specific questions. These agents are typically trained and evaluated on fully specified user queries. However, real-world user queries can often be underspecified. We introduce UNDERSPEC-DR, a framework for systematically evaluating how underspecified queries affect agents' final answer quality and intermediate search behavior. Across three DRAs we evaluated, underspecification substantially reduces how well DRA's answers fulfill users' information needs, even though they remain grounded in cited evidence. Our analysis of intermediate search behavior suggests a possible explanation: DRAs conduct broader searches that draw less on the original user query but rely more on their learned prior during training, which can be misaligned with users' intent. Our findings reveal the vulnerability of current DRAs to underspecified user queries and inform future efforts to build DRAs that proactively recognize when additional user input is needed to reliably complete deep research tasks.

---


### 257. [Anatomical Prior-Guided Routing for 3D Lung Tumor Segmentation](https://arxiv.org/abs/2610.39414)

**<font color=#1a73e8>作者：</font>** Uihyeon Maeng, Jonghun Kim, Hyunjin Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lung tumor segmentation in computed tomography (CT) is essential for treatment planning, response assessment, and quantitative imaging analysis. However, 3D lung tumor segmentation remains challenging because tumors occupy only a small portion of the whole volume and exhibit heterogeneous appearances across anatomical locations. In patch-based training and sliding-window inference for 3D medical image segmentation, location-dependent heterogeneity is further amplified because cropped image patches provide limited global anatomical context, making it difficult for a model to adapt its feature processing according to the anatomical region from which each patch is extracted. To address this limitation, we propose an Anatomical Prior-guided Routing Module (APRM) for lung tumor segmentation. For each image patch, we obtain anatomical prior information of regional occupancy and deterministically select an anatomical routing gate. The selected gate then performs sparse feature routing over a shared expert adapter pool, enabling anatomy-specific feature adaptation while sharing expert capacity across regions. We evaluate APRM on two datasets with various backbone networks and demonstrate consistent improvements over baseline models. Furthermore, feature visualizations show that APRM produces different feature responses depending on patch location, indicating that the proposed routing mechanism effectively adapts feature processing according to anatomical context.

---


### 258. [FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss](https://arxiv.org/abs/2610.39423)

**<font color=#1a73e8>作者：</font>** Hina Otake, Shinei Arakawa, Keitaro Tanaka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Formula-Driven Supervised Learning (FDSL) enables vision pre-training without real images, but existing methods cast pre-training as classification on discretized labels, discarding continuity in the generative process. We propose Formula-Driven Supervised Metric Learning (FDSML), which derives relational supervision from image-generation parameters beyond discrete class labels. FDSML combines FineFractalDB, our refined fractal dataset with higher intra-class variation and more stable structures, with a Parameter-Aware Triplet (PA-Triplet) Loss that assigns positives and negatives according to distances in the underlying Iterated Function System parameter space. This objective trains embeddings to respect parameter-derived relative similarity orderings. Experiments show that FDSML improves transferability to image retrieval while remaining competitive on downstream classification and improving robustness under several corruption settings. On ResNet-50, Recall@1 improves from 65.6% to 74.0% on Stanford Online Products and from 56.2% to 78.4% on Stanford Cars over FDSL pre-training. These results suggest that parameter-derived relational supervision provides a stronger synthetic pre-training signal than label-based classification for transfer beyond recognition.

---


### 259. [End-to-End Guarantees for Masked Diffusion Models under Conditional Mixing](https://arxiv.org/abs/2610.39444)

**<font color=#1a73e8>作者：</font>** Fareed Sheriff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models train a denoiser on masked cross-entropy and generate by unmasking many positions in parallel. Existing MDM sampling bounds assume an exact denoiser or leave its error uncontrolled while training bounds cover only the masking distribution on which the model was trained. We present an end-to-end guarantee for a learned denoiser under conditional mixing (CM): stationary sources (e.g. floored order-$r$ Markov and two-sided-Doeblin hidden-Markov sources) for which revealing distant visible tokens moves a masked token's posterior on average exponentially little in the distance with correlation length $\tau_c$. We show the empirical risk minimizer trained under any masking distribution attains per-token excess $\varepsilon'$ on that distribution from $\varepsilon'^{-\mathcal{O}(\tau_c\log|\mathcal{V}|)}$ training sequences, independent of sequence length $N$ -- one sample budget serves every decoding schedule when each schedule's denoiser is trained under its own weighting. We further show that the exponent's order $\Theta(\tau_c\log|\mathcal{V}|)$ is minimax-optimal up to constants; more efficient rates require added structure. With this, we bound the end-to-end KL as $\mathrm{KL}(\pi\Vert p_{\mathrm{alg}})\leq \varepsilon+N\varepsilon'$ under a dilated schedule of $T=\mathcal{O}(\tau_c\log(N|\mathcal{V}|/\varepsilon))$ denoising steps versus $\Omega(N)$ steps for a fixed random order on an explicit CM source. Finally, we show that block-autoregressive samplers chain across blocks with no added error and that a $\Lambda$-looped order-$r$ message-passing class on order-$r$ sources achieves polynomial sample complexity, with approximation error improving per loop until saturation at $\Lambda r\approx \tau_c\log(1/\varepsilon')$. Experiments on released and retrained models support our results' qualitative predictions.

---


### 260. [Kairos: Semantics-Aware Orchestration of Planning Engines across Classical, Numeric, Temporal and Hybrid PDDL](https://arxiv.org/abs/2610.39454)

**<font color=#1a73e8>作者：</font>** Francisco Martín Rico, Esther Aguado González, Francisco Miguel Moreno Olivo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning at run time, as in robots that re-plan while they act, needs a planner that reads the PDDL its users write (durative actions, numeric resources, time windows, continuous change), answers quickly, and delivers only validated plans. Specialised planners are strong on individual fragments of PDDL, but they differ in coverage, latency and in what their failures mean. We study whether selecting heterogeneous engines from the semantics of each task can give broad coverage of PDDL, from STRIPS to PDDL+, while remaining competitive with specialised planners and making explicit what each answer guarantees. Kairos profiles each task to decide which of five engines apply (ground heuristic search, compressed and snap-action temporal search, time steps for hybrid dynamics, lifted search) and schedules them under one budget of time and memory. Every candidate plan is checked by a validator independent of the planner's transformations, and "unsolvable" is reported only when a search whose exhaustion is a proof exhausts its space. On 1,756 tasks from nine comparative suites, Kairos solves more tasks at the full limits than the strongest evaluated planner of each suite, with the largest differences on numeric, temporal, PDDL3 and PDDL+ planning, and it also solves the most tasks at 100 ms and 1 s. Resampling over domains, the gain is above zero in six of the nine suites, while on classical planning against LAMA it is within the noise. A further 450 feature-oriented tasks and 26 one-feature probes show that Kairos handles all seventeen features probed, where no other planner evaluated handles more than eight. Ablations identify compressed temporal search and the novelty fallback as major contributors, and a comparison with VAL traces every disagreement to a PDDL+ convention or to a documented VAL defect. Planner and benchmark are open source.

---


### 261. [Sparse Fine-Tuning for Parameter-Efficient Adversarial Training](https://arxiv.org/abs/2610.39455)

**<font color=#1a73e8>作者：</font>** Zhaoxin Wang, Zihang Ding, Handing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve strong performance across many tasks but remain vulnerable to adversarial perturbations. Adversarial training (AT) is one of the most effective defenses, yet it suffers from high memory cost on large models and the persistent clean-robust accuracy trade-off. Recent work introduces parameter-efficient fine-tuning, such as LoRA, into AT, but this constraint induces a notable robustness gap relative to full-parameter AT. In this work, we revisit parameter-efficient adversarial fine-tuning from a parameter space perspective. Through gradient analysis, we find that adversarial optimization is highly concentrated on a small subset of parameters, which we call Robustness-Critical Parameters (RCPs), suggesting that robustness is encoded in a sparse subspace. Building on this observation, we propose Sparse Adversarial Fine-Tuning (SAFT), which identifies RCPs via adversarial gradient saliency and performs AT by updating only these parameters while freezing the rest. Across architectures and datasets, SAFT outperforms LoRA-based methods in both clean and robust accuracy with fewer trainable parameters, and approaches or surpasses full parameter AT in robustness while updating only about 5\% of parameters.

---


### 262. [Achieving Minimax-Optimal First-Order and Best-of-Both-Worlds Regret Simultaneously in Multi-Armed Bandits](https://arxiv.org/abs/2610.39457)

**<font color=#1a73e8>作者：</font>** Mengxiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study first-order and best-of-both-worlds regret guarantees in multi-armed bandits. Pogodin and Lattimore (2019) proposed an algorithm that combines minimax-optimal worst-case regret with a first-order guarantee whose loss-dependent term is $\mathcal{O}(\sqrt{K L^\star}\log T)$, where $T$ denotes the horizon, $L^\star$ denotes the smallest expected cumulative loss among fixed arms, and $K$ denotes the number of arms. However, a logarithmic gap remains between this loss-dependent term and the optimal first-order scale. In this paper, we remove this logarithmic factor by proposing an efficient and parameter-free algorithm that achieves the minimax optimal first-order regret guarantee $\mathcal{O}(\sqrt{K L^\star})$. Technically, our algorithm is built upon FTRL with a Tsallis entropy regularizer (Zimmert and Seldin,2021), with a learning rate adapted to the learner's cumulative loss and a sampling distribution determined by a scalar fixed point. This construction controls the combined estimation and stability cost in terms of the learner's loss. Moreover, we show that the same algorithm achieves a best-of-both-worlds guarantee, with $\mathcal{O}(\sum_{i\ne i^\star}\frac{\log T}{\Delta_i})$ regret for i.i.d. losses with a unique best arm $i^\star$, where $\Delta_i$ denotes the suboptimality gap of arm $i$.

---


### 263. [GraspPressure: Understanding Pressure Input With Busy Hands](https://arxiv.org/abs/2610.39459)

**<font color=#1a73e8>作者：</font>** Anand Kumar, Aditya Shekhar Nittala  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In many real-world scenarios, users interact with digital systems while their hands are partially occupied, such as when holding tools or everyday objects. Prior work on busy-hand interaction has focused on microgestures and motion-based techniques, which rely on finger articulation or relative movement. In situations where a stable grasp is required, such as handling fragile, heavy, or precision objects, such motion can be undesirable or impractical. Pressure-based input offers a complementary modality that enables interaction without changing finger pose, yet its use while holding objects has received limited empirical attention. To explore this, we conducted two within-subject experiments examining users' ability to perform controlled pressure selections and analyzing finger-specific performance across different grasps and geometries. Results indicate that participants can reliably perform pressure-based selections in these conditions, achieving high success rates (92.7% on average) with low selection times (1.74s on average). Our findings characterize the potential of pressure input as a complementary microinteraction modality under grasp-constrained, busy-hand scenarios.

---


### 264. [CBE: A Complexity-adaptive Boundary-aware Ensemble Method for Imbalanced Data](https://arxiv.org/abs/2610.39466)

**<font color=#1a73e8>作者：</font>** Xun Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world classification tasks, datasets exhibit class imbalance, which can degrade the generalization performance of conventional learning algorithms. Data complexity has recently been recognized as a more objective indicator of learning difficulty than the imbalance ratio alone, because class overlap and complex decision boundaries often impair classifiers more severely than imbalance itself. Samples near the decision boundary are inherently difficult to classify, which has motivated many researchers to focus on such instances to improve classifier performance. However, most under-sampling approaches fail to differentiate their sampling of boundary samples across datasets of varying complexity. To overcome this limitation, we propose a complexity-adaptive boundary-aware ensemble (CBE) framework that links the sampling weight distribution to data complexity and dynamically adjusts the boundary preference of under-sampling accordingly. We also introduce an overall complexity measure that combines metrics at multiple levels and use it to divide imbalanced datasets into three categories. Extensive experiments on 24 benchmark datasets from UCI and KEEL show that the proposed method outperforms many existing methods in terms of F-measure and G-mean on Easy and Median datasets, without degrading performance on hard cases.

---


### 265. [Calibrating Attention-Based Token Pruning for Efficient Multi-Image Synthesis in UMMs](https://arxiv.org/abs/2610.39467)

**<font color=#1a73e8>作者：</font>** Zimeng Wu, Qijian Tian, Penghui Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) enable powerful multi-image synthesis but incur substantial computation from long visual contexts. While token pruning offers a direct route to accelerating inference, existing methods are primarily adapted from understanding tasks, suffering from insufficient reference image exploration, confused conditional guidance, and pooling-induced ambiguity that degrades generation quality. To address these issues, we propose CATP, the first training-free context-compression method tailored to UMM generation, which \textbf{C}alibrates the discrepancies of general \textbf{A}ttention-based \textbf{T}oken \textbf{P}runing for better quality-efficiency trade-off. Concretely, building on independent layer-wise pruning during denoising, we introduce Guidance-Consistent Pruning (GCP) to synchronize pruning decisions across conditioning branches, and a Taylor-Calibrated Attention Metric (TCAM) that derives a theoretically grounded second-order correction for pooling-induced bias. In addition, a Fast Scoring Operator (FSO) fuses the calibration into tiled online Softmax to reduce pruning cost. Extensive experiments across representative UMMs and benchmarks demonstrate that CATP consistently outperforms state-of-the-art token-reduction methods, achieving up to 2.09$\times$ attention-core speedup.

---


### 266. [Topology Survives Shuffling: Robust Long-Context Memory Access Prediction for Graph Analytics](https://arxiv.org/abs/2610.39477)

**<font color=#1a73e8>作者：</font>** Dongyan Sun, Neelesh Gupta, Rajgopal Kannan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph analytics generates irregular, topology-dependent memory-access streams via indirect traversals, limiting data prefetching. Accurate prediction enables timely prefetches that hide memory latency. However, ML predictors couple short histories with fixed horizons, fitting the training trace's node layout rather than learning transferable graph patterns. We propose LoCoMAP, a long-context representation-learning framework for memory-access prediction with independently controlled observation history and prediction horizon. We evaluate Connected Components (CC), PageRank (PR), and Single-Source Shortest Paths (SSSP) on six synthetic graph families, with Erdos-Renyi (ER) and Grid as random and deterministic controls. We test two interventions: same-family regeneration changes connectivity, while node shuffling disrupts layout but preserves connectivity. Across 18 graph-workload pairs, extending history from 8 to 128 accesses improves F1 by 7.8%, while extending prediction horizon from 8 to 512 improves F1 by 88.3%. For CC, regeneration is less disruptive than shuffling: without retraining, long context retains 95.4% of original F1 and outperforms short context in six families. Under full shuffle, long context improves CC F1 by 33.6% across ER, Barabasi-Albert, Copying Model, and Stochastic Block Model (SBM), with a 2.06x gain on SBM, but not on Watts-Strogatz or Grid, where near-zero delta mass shifts into heavy tails beyond the predictor's range. Long context outperforms short context on six real-world CC graphs. At full shuffle, long-context PR retains 57.6% of original F1 and averages 11.0% above short context. Both SSSP models retain about 30% of original F1 under full shuffle as distance updates access vertex data in a new order. Within these bounds, long-context predictors are robust across related graphs and layouts without retraining, enabling a generalizable graph prefetcher.

---


### 267. [Regional Anchor Routing for Multi-Object Motion Transfer](https://arxiv.org/abs/2610.39478)

**<font color=#1a73e8>作者：</font>** Yuze Li, Fuchen Long, Xinlong Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional motion transfer requires a model to extract motions from multiple reference videos, and apply each motion to a user-specified object in one target scene. Existing methods normally struggle to reliably assign different reference motions to the correct target objects, thus a motion intended for one object may affect another. Meanwhile, some motion-specific tuning approaches are still facing another issue: they must run a new optimization whenever the reference video changes, making repeated transfers inefficient. To address these limitations, we propose RART, a framework that unifies object-wise motion extraction, target-region anchoring, and frame-aligned injection into a frozen video Diffusion Transformer for multi-object motion transfer. For each reference motion, RART extracts temporally ordered features from the masked reference video, and then conditions them on the target first-frame mask to form mask-anchored motion tokens. Frame-aligned motion cross-attention allows each generated frame to read only the motion tokens at the corresponding time slots, composing all object motions in one denoising process. During training, a motion-attention routing loss encourages each target region to attend to its corresponding motion tokens and reduces interference between objects. Therefore, RART can handle novel reference-target combinations without per-video optimization. Experiments show that RART achieves accurate motion preservation, efficient inference, and strong compositional generalization.

---


### 268. [Does Federated Training Degrade Explainability? A Comparative Analysis of Grad-CAM Faithfulness in Centralized vs. Federated Deepfake Detection](https://arxiv.org/abs/2610.39483)

**<font color=#1a73e8>作者：</font>** Muhammad Uzair Shahid, Muhammad Zabil Mehboob  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated detection has become the essential safeguard against realistic synthetic media, but deploying it at scale requires training on sensitive data from multiple organizations, putting privacy and the transparency demanded by forensic review in direct conflict. Federated learning resolves the privacy side by sharing only model updates rather than raw data, but whether this comes at the cost of trustworthy gradient-based explanations, which analysts rely on to decide whether or not to trust a flagged clip, has not been studied. We present the systematic study of Grad-CAM explanation faithfulness under federated deepfake detection, evaluating an EfficientNet-B4 detector on FaceForensics++ across five federated clients under varying degrees of data heterogeneity. We find that the relationship between federation and explanation quality is non-monotonic: at near-IID (Independent and Identically Distributed Data) and moderate heterogeneity, federated models match or exceed the faithfulness of a centralized baseline, but at extreme heterogeneity, explanations break down entirely, becoming spatially incoherent and, on average, causally misleading. This degradation is not a general cost of federated training but a threshold effect tied to client heterogeneity, and we offer practical guidance for identifying when privacy-preserving deepfake detection can be deployed safely and when its explanations can no longer be trusted. Code and data partitions are available for reproducibility.

---


### 269. [Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?](https://arxiv.org/abs/2610.39497)

**<font color=#1a73e8>作者：</font>** Qi Wang, Yun Qu, Lizhou Cai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with System-1, a lightweight, semantically aware predictor that evaluates candidate interactions before execution, so that System-2 acts only on those worth their cost. Our answer is a qualified yes. We study \textit{conditional interaction}, a predict--gate--execute--update loop: System-1 estimates each candidate's utility, System-2 executes those admitted by an adaptive threshold, and the outcomes update System-1. The loop spans training, test-time reasoning, adaptive decision-making, and agentic tool use, with utility and cost defined by the application. Under ideal screening and equal execution costs, execution compute falls by a factor approaching $1/\rho_u$, where $\rho_u$ is the density of utility-relevant interactions (cost-weighted when costs differ); prediction errors, exploration, and distribution shift reduce the saving. We bound selection regret by predictor error and the utility margin. These results motivate our central hypothesis: $\rho_u$ is a measurable coordinate of scaling efficiency and makes informative compute a better description of scaling than total compute.

---


### 270. [Integrated Feature Selection for classification and Representation Learning with Group-Lasso Siamese Networks](https://arxiv.org/abs/2610.39499)

**<font color=#1a73e8>作者：</font>** Nisargo Ranjan Pal, Pradeep Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Least Absolute Shrinkage and Selection Operator (Lasso) has been widely employed for feature selection in linear models and has also been extended to multi-layer perceptron (MLP) networks for both feature and group feature selection. Group-Lasso has also been used in feature selection using feed-forward neural networks. To the best of our knowledge, this is the first study to incorporate the Group-Lasso principle into a Siamese network architecture for feature selection. Unlike existing approaches that primarily optimize classification accuracy, the proposed method aims to identify a compact subset of features that simultaneously preserves the intrinsic representation of the input data (the goal of Siamese network) and is expected to achieve high classification performance. Two variants of the proposed framework are developed: one based on the Euclidean distance and the other on a modified Jaccard similarity measure for real-valued vectors. The latter is specifically designed to improve feature selection for high?dimensional sparse data. The effectiveness of the proposed approach is demonstrated on 12 benchmark datasets with feature dimensions ranging from 6 to 7070 using eight different classifiers. Experimental results demonstrate that the proposed Siamese Lasso framework consistently identifies compact and discriminative feature subsets maintaining competitive or superior classification performance, although the loss function used explicitly did not consider any regularizer to learn classification. In addition, the quality of the embeddings produced by these networks is assessed using manifold learning techniques such as UMAP and t-SNE.

---


### 271. [Agent-Wise Test-Time Normalization for Camera-Based Cooperative Perception with Corrupted Collaborators](https://arxiv.org/abs/2610.39505)

**<font color=#1a73e8>作者：</font>** Yu Wang, Shaohua Wang, Yicheng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intermediate-fusion cooperative perception lets a vehicle detect objects beyond its own field of view by fusing features shared by nearby agents. When only a collaborator's cameras are degraded by fog, motion blur or exposure errors, the features it shares drift away from the training distribution while the ego input stays clean, and cooperation can become worse than not cooperating at all. Test-time batch-normalization adaptation, the standard training-free remedy, estimates statistics over the pooled batch of all agents and therefore normalizes both the clean ego and the corrupted collaborator with a mixture of two distributions. We show that this mixing harms even the clean ego: when the ego shares BN statistics with a corrupted collaborator, its detection from its own features drops by 3.58 to 6.68 AP@0.5 points although its cameras are untouched. We propose AgentNorm, an agent-wise test-time normalization that i) estimates the normalization statistics of every collaborator from its own current observation and ii) anchors the ego to its source statistics, so that the ego path remains exactly the original model. AgentNorm has no learnable parameters, needs no gradients or labels, is independent of the order of test frames, and runs locally on each agent without changing the transmitted features. On camera-based OPV2V with four fusion checkpoints and collaborator-only corruptions, AgentNorm raises AP@0.5 under severity-5 fog from 29.42-37.25 to 43.32-58.86 and outperforms pooled normalization by 5.53-12.94 points under fog and motion blur, at an extra latency of 2.3 ms per frame. On the real-world DAIR-V2X-C dataset, it outperforms pooled normalization in all ten infrastructure-corruption settings. We also report the cases it does not fix: occlusion, which removes image content rather than shifting feature statistics, and the case in which all agents share the same shift.

---


### 272. [DEG: Diffusion-Enhanced GFlowNet for Solving Vehicle Routing Problems](https://arxiv.org/abs/2610.39512)

**<font color=#1a73e8>作者：</font>** Ni Zhang, Zhiqin Zhang, Ling Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional neural solvers for solving vehicle routing problems (VRPs) often suffer from limited solution diversity, motivating the development of Generative Flow Network (GFlowNet)-based models. However, the effectiveness of these models is frequently constrained by insufficient flow expansion in high-reward regions, limiting their ability to distribute probability across promising solution routes. Deeper exploration could yield superior results. Diffusion models, in contrast, provide stronger structural guidance for exploration. These two paradigms are naturally complementary: GFlowNet can supply edge-level signals for diffusion to embed, while diffusion can guide broader exploration. Leveraging this synergy, we propose Diffusion-Enhanced GFlowNet (DEG), a novel framework that integrates GFlowNet with a diffusion model to encourage richer flow expansion toward high-reward regions and derive higher-quality solutions. Specifically, DEG exploits GFlowNet's inherent diversity to generate edge-specific backward signals, applies the stochastic noise schedule of diffusion to perturb these signals, and then denoises them within the GFlowNet paradigm. To further improve scalability, we introduce a specialized decoder capable of dynamically adapting to diverse problem scales. Extensive experimental evaluations on synthetic and real-world datasets, including instances with up to 10,000 nodes, demonstrate that DEG consistently achieves favorable performance compared to baseline methods.

---


### 273. [Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion](https://arxiv.org/abs/2610.39516)

**<font color=#1a73e8>作者：</font>** Christoph B Rist, Larissa T Triess, Markus Enzweiler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study domain generalization for LIDAR semantic segmentation. Deep neural networks achieve strong performance on 3D point clouds, yet real-world LIDAR exhibits sensor-specific sampling patterns that hinder transfer across datasets. In many applications, performance on completely unseen sensors is crucial. A model should preferably work on a new setup without prior access to its data or labels. To this end, we introduce a source-only training scheme that adds an occupancy prediction auxiliary objective. We aggregate source-domain scans into a simple world model and use it as the supervision signal, replacing single-scan standard segmentation training.
A key property of our approach is that it does not alter the input scan. During training and testing the network consumes the same single-frame LIDAR input, only the supervision signal is enriched via the occupancy objective. At deployment, there is no runtime overhead as the auxiliary head can be dropped for pure segmentation, or kept to obtain scene completion alongside semantic segmentation. In an experimental evaluation across distinct LIDAR datasets, we demonstrate that a model's generalization to new domains can be significantly affected by how it is supervised. In certain setups, performance on unseen domains improves without any explicit domain adaptation (no target scans, no target labels, no sensor priors) and without prediction refinement. At the same time, our method maintains competitive source-domain segmentation performance and incurs no additional inference cost.

---


### 274. [FFAI: Flow Matching with Feedback Training and Adaptive Initialization for CT Reconstruction](https://arxiv.org/abs/2610.39517)

**<font color=#1a73e8>作者：</font>** Jigang Duan, Heran Wang, Genwei Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although low-dose, sparse-view, and limited-angle CT involve distinct degradation mechanisms, all three pose reconstruction challenges due to limited measurement information and can therefore be addressed within a unified framework. In iterative image restoration with flow matching, prediction errors may cause inference states to deviate from the prescribed training path, while a fixed initialization may be unsuitable for inputs with varying degradation severity. We propose a unified conditional flow matching method that conditions on the initial reconstruction and combines feedback-aware training with degradation-adaptive initialization. During training, a teacher network simulates inference updates to generate shifted states, from which a student network learns to recover high-quality reference images, improving its ability to handle prediction errors. During inference, the starting time is selected based on the noise level or extent of missing projection data, and the noise added to the initial state is adjusted accordingly to adapt the starting point to the input. Experiments on public benchmark datasets show that the proposed method achieves better quantitative results than the compared methods across all three reconstruction tasks, effectively suppressing noise and artifacts while preserving anatomical structures and details.

---


### 275. [Last-Iterate Convergence for Constrained MDPs: From Dual Descent to Primal-Dual](https://arxiv.org/abs/2610.39524)

**<font color=#1a73e8>作者：</font>** Michael Lu, Max Qiushi Lin, Mo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study policy optimization for infinite-horizon, discounted constrained Markov decision processes. While primal-dual ($\texttt{PD}$) methods are widely used in practice, their theoretical guarantees typically hold for an impractical mixture policy. In contrast, dual descent ($\texttt{DD}$) methods output a single policy ("last iterate") with guarantees on its performance. However, such methods require iteratively solving entropy-regularized MDPs in an inner-loop, limiting their practical effectiveness. Moreover, existing analyses rely on strong coverage assumptions that are difficult to satisfy in practice. Consequently, we first provide a new analysis of $\texttt{DD}$ methods that does not require coverage assumptions. We then employ entropy-regularized natural policy gradient and dual regularization to eliminate the inner loop, resulting in an efficient $\texttt{PD}$ algorithm. We develop a novel tracking analysis which shows that, compared to existing methods, the proposed algorithm achieves improved last-iterate convergence guarantees. Furthermore, our theoretical framework allows us to analyze a truncated bilevel method that interpolates between $\texttt{DD}$ and $\texttt{PD}$ methods. Finally, we generalize our analysis to handle linear function approximation. Compared to prior last-iterate methods, we prove stronger guarantees under less restrictive assumptions.

---


### 276. [MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530)

**<font color=#1a73e8>作者：</font>** Hailong Yan, Yongrui Zhang, Xiangtao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose MorphSIG, a training-free framework that reformulates subject-driven image generation (SIG) as pseudo-video feature transport. MorphSIG contains two core modules: Progressive Decoupled Anchoring, which uses frequency-domain decoupling and structural scrambling during early denoising to break structural locking and enable a gradual transition from free composition to identity alignment; and Pseudo-flow Guided Feature Transport, which constructs a latent-space pseudo-flow field to mimic Image-to-Video temporal coherence and transport subject semantics precisely. To address stylistic homogeneity and the lack of ground truth in existing benchmarks, we further introduce a benchmark with diverse stylized subjects. Extensive experiments show that MorphSIG significantly improves pose diversity and subject fidelity over baselines without additional training. Overall, MorphSIG bridges static generation and dynamic propagation, providing a cost-effective paradigm for high-fidelity subject consistency.

---


### 277. [MOSAIC-Flow: Orthogonal-Axis and Status-Conditioned Fusion for Missing-Sequence Completion in Brain Tumor MRI](https://arxiv.org/abs/2610.39534)

**<font color=#1a73e8>作者：</font>** Pengli Zhu, Zhihao Peng, Yixuan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Missing-sequence completion is important for comprehensive brain tumor characterization, but cross-modal fusion can obscure sequence-specific contrast and lose fine-grained three-dimensional tumor detail. To address this challenge, we introduce Modality-aware Orthogonal-axis Status-conditioned Attentive Integration for Completion (MOSAIC-Flow), a unified framework for missing-sequence completion that learns a target-conditioned velocity field while keeping the seven acquired volumes fixed throughout the transport. Specifically, modality-aware stems independently encode each sequence, and orthogonal-axis refinement captures axial, coronal, and sagittal dependencies while retaining the three-dimensional representation. Status-conditioned prototype fusion uses compact modality and availability tokens to route and modulate pooled queries from the fused visual representation, enabling target-adaptive conditioning without dense voxel-to-voxel attention. A conditional flow matching objective transports target-channel noise toward the single missing sequence, while four Heun trajectories are averaged to produce the completion. Evaluation across structural, diffusion, and contrast-enhanced MRI in UCSF-PDGM demonstrates consistent whole-brain and tumor-region fidelity across all eight single-target completion tasks, with the strongest performance on structural sequences. Code is available at this https URL.

---


### 278. [ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale](https://arxiv.org/abs/2610.39539)

**<font color=#1a73e8>作者：</font>** Xiaoou Li, Shan You, Tao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step distillation turns pretrained diffusion models into fast generators, but strong results often require substantial training machinery and compute. Pure adversarial distillation offers a simpler route, yet has struggled at modern text-to-image scale. To address this limitation, we propose ROAD (Representation-grounded One-step Adversarial Distillation), a one-stage framework that distills text-to-image models with one adversarial objective and a lightweight representation-space critic. First, we replace the classical convolutional head with a Lipschitz-controlled Transformer head with token-level text conditioning, which matches the semantic tokens of modern visual encoders. Second, we observed a fixed random feature mixing leads to long-horizon degradation. We attribute it to generator-critic co-adaptation around one realization-specific view, and periodically re-draw the mixing to keep the randomization effective. Third, for our dense and vector-valued logits, we introduce Jacobian R1 which penalizes the full input-logit Jacobian, overcoming pooled R1's limitation of neglecting most of logit sensitivities. A single adversarial objective then suffices: in one step, ROAD reaches 11.03 FID on SDXL and 13.73 on SD3.5-M on COCO-10K, surpassing the multi-step teachers at a fraction of distribution matching's training compute.

---


### 279. [Comprehensive empirical evaluation of feature extractors in computer vision](https://arxiv.org/abs/2610.39551)

**<font color=#1a73e8>作者：</font>** Murat Isik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature detection and matching are fundamental components in computer vision, underpinning a broad spectrum of applications. This study offers a comprehensive evaluation of traditional feature detections and descriptors, analyzing methods such as Scale Invariant Feature Transform (SIFT), Speeded-Up Robust Features (SURF), Binary Robust Independent Elementary Features (BRIEF), Oriented FAST and Rotated BRIEF (ORB), Binary Robust Invariant Scalable Keypoints (BRISK), KAZE, Accelerated KAZE (AKAZE), Fast Retina Keypoint (FREAK), Dense and Accurate Invariant Scalable descriptor for Yale (DAISY), Features from Accelerated Segment Test (FAST), and STAR. Each feature extractor was assessed based on its architectural design and complexity, focusing on how these factors influence computational efficiency and robustness under various transformations. Utilizing the Image Matching Challenge Photo Tourism 2020 dataset, which includes over 1.5 million images, the study identifies the FAST algorithm as the most efficient detector when paired with the ORB descriptor and Brute-Force (BF) matcher, offering the fastest feature extraction and matching process. ORB is notably effective on affine transformed and brightened images, while AKAZE excels in conditions involving blurring, fisheye distortion, image rotation, and perspective distortions. Through more than 2 million comparisons, the study highlights the feature extractors that demonstrate superior resilience across various conditions, including rotation, scaling, blurring, brightening, affine transformations, perspective distortions, fisheye distortion, and salt-and-pepper noise

---


### 280. [BEACON: Distilled Begin/End-Aware Structured Decoding for Continuous Sign Language Segmentation](https://arxiv.org/abs/2610.39553)

**<font color=#1a73e8>作者：</font>** Guohou Zhang, Kalin Stefanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In segmentation-based continuous sign language recognition, an untrimmed video is first partitioned into lexical units; segmentation is therefore a means to an end---downstream recognition. However, segmenters are usually judged by local boundary detection rather than by the quality of the lexical segments and the recognition they enable. We present BEACON, a begin/end-aware segmenter that combines four-class Outside/Begin/Inside/End (BIOE) labeling, constrained Viterbi decoding over eight legal transitions, and boundary knowledge distilled from a binary teacher into a shared student. Under strict no-cut evaluation with validation-based model selection, BEACON improves segment-F1 by 14.58/14.59 points and boundary-F1 by 2.17/1.22 points, and reduces the downstream word error rate (WER) by 9.10/4.15 points relative to the state-of-the-art in the PHOENIX-14/BSL Corpus. To examine which segmentation metric better reflects downstream recognition, we evaluated five distinct architecture families. Segment-F1 aligns more consistently with lower WER than boundary-F1 in both corpora (Spearman $\rho=-1.0/-0.9$ versus $-0.9/-0.8$). These results support evaluating sign language segmentation in terms of segment quality and downstream recognition utility rather than local boundary accuracy alone.

---


### 281. [Explainable and Adaptive Machine Learning for Fraud Risk Detection in Bangladesh's Digital Banking Ecosystem](https://arxiv.org/abs/2610.39556)

**<font color=#1a73e8>作者：</font>** Md Najmus Swaqeeb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of digital banking and mobile financial services creates growing challenges for fraud detection, particularly under severe class imbalance and operational constraints. This study presents an explainable and adaptive machine-learning framework integrating chronological evaluation, leakage-conscious feature engineering, probability calibration, SHAP-based explainability, and adaptive risk prioritization. Experiments use the synthetic PaySim mobile-money benchmark and compare Logistic Regression, Random Forest, XGBoost, and LightGBM. XGBoost achieved the strongest fixed-threshold performance, with PR-AUC of 0.5658, ROC-AUC of 0.9068, and F1-score of 0.5369. Platt calibration reduced the test Brier score from 0.1141 to 0.0245, improving probability reliability. SHAP analysis identified temporal, destination-account, transaction-type, and amount features as important model drivers. An adaptive top-1% policy reduced false positives from 192 to 117, but recall declined from 0.4236 to 0.2122, demonstrating a clear alert-capacity trade-off. The results provide a reproducible methodological framework rather than evidence of deployment performance in Bangladesh, since PaySim is synthetic. Validation using governed real-world financial data is therefore an important direction for future research.

---


### 282. [Generative artificial intelligence prompting strategies among Chinese university students across academic tasks](https://arxiv.org/abs/2610.39571)

**<font color=#1a73e8>作者：</font>** Lei Fan, Fangxue Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) is increasingly embedded in university learning, yet effective human-GenAI interaction depends not only on access to these tools but also on students' ability to formulate, evaluate, and refine prompts for academic tasks. This study examined university students' perceived GenAI prompting capability and reported prompting strategies. Questionnaire data from 234 students were analyzed using descriptive statistics, measurement modelling, scenario comparisons, structural associations, and qualitative coding of optional comments. Students reported using GenAI across diverse academic activities and generally expressed confidence in their prompting capabilities, particularly in providing relevant context and refining prompts following initial outputs. However, prompting strategies showed limited sensitivity to task types: specifying output format was more strongly endorsed in a creative workshop preparation scenario than in a research-oriented assignment, whereas other matched strategies showed no adjusted differences. Students also commonly endorsed both concise instructions and providing all relevant information at the outset, suggesting that effective brevity may depend more on selecting and organizing task-relevant information than on prompt length alone. By contrast, fixed prompt templates received lower endorsement than other prompting strategies. In the adopted factor model, perceived cognition showed the clearest unique association with perceived prompting capability, while open-ended responses highlighted prompt-intent alignment as a common challenge.

---


### 283. [RV2GC: Reconstructing the Garbling Boundary in a RISC-V Garbled Processor](https://arxiv.org/abs/2610.39572)

**<font color=#1a73e8>作者：</font>** Zixiao Feng, Xiaolin Li, Chenglu Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Programmable garbled-circuit execution must balance the benefits of cross-program reuse against the cost of repeated work during secure execution. A complete garbled processor provides a fixed circuit for many programs, but its evaluator repeatedly visits processor-wide structures even when only a small part performs the current protected computation. We present RV2GC, which reconstructs the garbling boundary around a fixed library of RISC-V instruction circuits. Public scheduling and operand routing operate outside the circuit topologies; persistent label-encoded state connects independently invoked garbled instruction circuits and instruction-specific garbling-free paths through a common interface. A Conditional-execution Stack and protected commits support secret-dependent branches, bounded loops, and secret-indexed memory access under public scheduling, keeping instruction and memory-address sequences independent of private inputs. Across nine benchmarks, measured ARM2GC-to-RV2GC runtime ratios range from 12.81 to 4,043. In terms of circuit size, the largest listed instruction circuit has 3,386 gates, corresponding to 2.044% and 0.393% of the 256-byte and 4,096-byte Amber processors, respectively. Additional comparisons quantify schedule storage, communication, and the cost of secret-dependent execution.

---


### 284. [Cybersecurity Practices in Industrial Automation and Control Systems: a Study of Croatian System Integrators](https://arxiv.org/abs/2610.39573)

**<font color=#1a73e8>作者：</font>** Filip Katulić, Damir Sumina, Stjepan Groš 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Given the increasing frequency of industrial cybersecurity incidents, governments, industry, and the research community are all working to find ways to protect industrial automation and control systems (IACSs). A key regulatory effort in the European context is the EU's Network and Information Security Directive 2 (NIS2), which aims to strengthen cybersecurity requirements and improve resilience across critical and important sectors. Nevertheless, translating cybersecurity requirements into practical engineering remains challenging within IACS environments. This paper explores how Croatian IACS system integrators perceive cybersecurity requirements, implementation challenges, and current practices in the industrial environments in which they operate. The findings are based on three focus groups with system integrators working with clients in the energy, chemical and pharmaceutical, and food and beverage sectors. Participants reported limited cybersecurity awareness among IACS owners, as well as perceived differences in practices between smaller and larger companies and between domestic and foreign firms. Participants were divided in their expectations regarding regulatory pressure: while some believed it could improve cybersecurity, others expected only minimal compliance focused on cost reduction. The results of this study provide a basis for developing more practical cybersecurity practices and offer a deeper understanding of the key challenges faced by IACS system integrators and owners when dealing with cybersecurity.

---


### 285. [Bayesian Offline Multi-Agent Reinforcement Learning with Latent World Models](https://arxiv.org/abs/2610.39576)

**<font color=#1a73e8>作者：</font>** Xi Xiong, Lu Liu, Yiming Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Model-based offline multi-agent reinforcement learning (MARL) provides a promising approach to multi-agent decision-making under partial observability, where the global state is unavailable from offline data. However, limited dataset coverage can lead to substantial out-of-distribution (OOD) model errors, which may mislead policy optimization and degrade downstream performance. Existing model-based offline MARL methods typically rely on access to global states or mitigate model errors through pessimistic or conservative policy optimization, leaving the reliability and refinement of learned world models less explored. We propose a Bayesian offline MARL framework that infers latent global states from decentralized observation-action histories and iteratively refines a posterior world model using only offline data. Building on posterior information loss, we extend this criterion to the multi-agent setting as multi-agent posterior information loss (MPIL), which provides a reliability measure for world model refinement and offline evaluation. Theoretically, we establish an upper bound on policy regret that is monotonic in MPIL and further characterize its dependence on the size and state-joint-action coverage of the offline dataset. Experiments on partially observable multi-agent variants of D4RL MuJoCo tasks demonstrate competitive policy performance across diverse offline data conditions, while MPIL-guided refinement improves world model prediction and downstream policy performance. These results support a principled connection between world model reliability, offline data coverage, and policy performance in partially observable offline MARL.

---


### 286. [DOSE: Dominance-Guided Ordinal Severity Estimation from Sparse Relative Annotations](https://arxiv.org/abs/2610.39584)

**<font color=#1a73e8>作者：</font>** Tushir Sahu, Hideaki Hayashi, Hajime Nagahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical severity estimation commonly relies on absolute grade annotations, which are fundamentally ordinal, yet existing methods often treat the grades as independent categories. Learning-to-rank methods, which can be trained using relative annotations based on severity comparisons of image pairs, can provide continuous severity rankings but cannot directly predict discrete severity grades. We propose Dominance-guided Ordinal Severity Estimation from Sparse Relative Annotations (DOSE), a framework for learning ordinal medical severity from sparse pairwise comparisons without using absolute annotations. DOSE aggregates the observed comparisons through a global comparison graph to estimate a dominance score for each image. Differences between dominance scores set cumulative margins in the embedding space, so that pairs with larger estimated severity differences are separated more strongly, and also generate pseudo-pairs that supervise a scalar severity head alongside the observed comparisons. The learned continuous severity axis is converted into discrete grades via label-free score calibration, with tie-anchored segmentation as the main calibration method. In the experiment, DOSE consistently outperformed pairwise-ranking baselines on ACNE04, IDRiD, and LIMUC under different pair budgets. Code is available at this https URL

---


### 287. [TactoHand: Learning Geometry-Based Dense Hand-Surface Interaction Fields from Video](https://arxiv.org/abs/2610.39585)

**<font color=#1a73e8>作者：</font>** Ziheng Xi, Weibo Li, Jiayi Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how humans interact with the world requires a representation of physical interactions at the hand surface. Tactile sensing captures these interactions, but collecting tactile data at scale requires specialized hardware. We introduce TactoHand, a model that predicts three dense hand-surface interaction fields---contact, proximity, and 3D force---from monocular video. We derive geometry-based contact and proximity labels and motion-derived force labels from eligible training data within a curated collection spanning approximately 50 million source frames. TactoHand uses a temporal transformer to aggregate visual evidence across frames, while three learned queries decode the corresponding hand-surface fields. A differentiable physics layer further constrains force predictions using observed object motion. Across in-domain and out-of-domain benchmarks, TactoHand improves contact and proximity estimation over prior methods. In addition, physics supervision reduces position and rotation errors in motion rollouts, and the predicted contact and proximity fields improve downstream hand-object reconstruction. Together, these results show a scalable, low-cost path to learning hand-surface interaction fields without collecting tactile measurements. Code will be released at this https URL.

---


### 288. [Operator-Aware Posterior Sampling for Multivariate Weather Downscaling](https://arxiv.org/abs/2610.39592)

**<font color=#1a73e8>作者：</font>** Carlo Saccardi, Rudolf Saathof, Geethu Joseph 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Statistical downscaling is the task of reconstructing high-resolution meteorological fields from coarse inputs. A principled approach formulates downscaling as a Bayesian inverse problem, using a diffusion prior over high-resolution fields and incorporating the coarse field only at inference through a likelihood. This decouples the prior from the coarse source, allowing one pretrained model to adapt to different sources. However, two challenges limit this flexibility: (1) when coarse and target fields come from different reanalysis systems, no fixed coarsening operator can capture their relationship; and (2) guidance gradients can differ by orders of magnitude across variables, making a single guidance strength ineffective. This paper addresses both challenges within the guidance loop, leaving the prior unchanged. We learn the forward operator from paired data and normalize the gradient per channel. We show that this normalization corresponds to steepest descent under a block-max norm, allowing a single guidance strength across variables. Our code is publicly available at this https URL.

---


### 289. [Improving the Intrinsic Interpretability of Differentiable Decision Trees through Euclidean Feature-Concentration Regularisation](https://arxiv.org/abs/2610.39596)

**<font color=#1a73e8>作者：</font>** Qiqi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable decision trees (DDTs) support end-to-end optimisation and explicit decision paths, but dense oblique splits can obscure the role of individual input features. We propose the Euclidean-Concentrated Differentiable Decision Tree (EU-DDT), which regularises the relative absolute feature weights at each internal node using their normalised squared Euclidean distance from the uniform distribution. This encourages dominance by a small number of features while retaining probabilistic soft routing. Across five matched random seeds, EU-DDT reduces the mean effective number of features from 8.94 to 1.54 on Wine and from 45.28 to 9.06 on Digits. Mean test accuracy changes from 100.0% to 93.9% on Wine and from 92.3% to 94.6% on Digits, illustrating the dataset-dependent trade-off between concentration and predictive performance. We also use EU-DDT to parameterise a PPO actor with an MLP critic. Two random-seed runs per environment show a consistent qualitative increase in concentration while preserving effective task performance. In representative CartPole-v1 and MiniPacman runs, EU-DDT reaches 100% final evaluation success, while mean node concentration increases from 0.1272 to 0.7179 and from 0.0437 to 0.7237, respectively. These results support EU regularisation as a mechanism for reducing node-level feature complexity; the reinforcement-learning evidence remains preliminary because only two seeds are evaluated.

---


### 290. [DiFuse: Fusing Native Diffusion Representations for Spatial Reasoning in Unified Multimodal Models](https://arxiv.org/abs/2610.39609)

**<font color=#1a73e8>作者：</font>** Ruixin Fan, Weining Wang, Jiahui Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) jointly support visual understanding and image generation, yet information flow between these two capabilities remains largely asymmetric: understanding representations routinely condition generation, whereas generative representations are rarely reused for multimodal reasoning. In this work, we investigate whether intermediate representations from a UMM's native diffusion branch can enhance spatial reasoning without compromising general multimodal understanding. We propose DiFuse, which selectively incorporates intermediate diffusion representations into the understanding pathway of UMMs. Through systematic layer-wise analysis, we identify which diffusion representations are most informative and where they can be integrated with minimal interference to semantic processing. Guided by these findings, DiFuse spatially aligns diffusion features with visual tokens and injects them into selected multimodal decoder layers via residual fusion. Extensive experiments on UniWorld-V1 show that, DiFuse consistently improves spatial reasoning over a matched SFT baseline while maintaining broadly comparable performance on general multimodal benchmarks. Further analyses show that these gains depend critically on the choice of diffusion representations, injection positions, and the preservation of spatial correspondence between diffusion features and visual tokens. Results on OmniGen2 further demonstrate the transferability of DiFuse across unified multimodal architectures. Overall, our findings show that native diffusion representations can provide complementary spatial cues for multimodal reasoning when selectively integrated in a structure-preserving manner.

---


### 291. [Emergence of the transformer architecture as the score of entropic laws of random measures](https://arxiv.org/abs/2610.39614)

**<font color=#1a73e8>作者：</font>** Giacomo Greco  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We show that the transformer architecture emerges as the score of last-token laws in a natural statistical model of language, where sentences are empirical measures of tokens, a language is a law on $P(S^d)$, and our prior belief is that sentences carry no structure at all. By the maximum-entropy principle, we select the law closest to this prior in relative entropy among those reproducing an observed sentence-level statistic. We discuss the relevance of the statistic in the posterior interaction between tokens and we build a statistic, able to capture that interaction, with Luce's choice axiom truncated at the lowest relational order. This procedure gives the softmax choice rule, with the attention cross-moment as its mean parameter. The query--key matrix is then the Lagrange multiplier of a maximum-entropy problem inside each sentence, and the value matrix the multiplier of the constraint over the language, so that the two are untied. Under the optimal entropic law we then show that a transformer head appears in the score of the last-token law. For ordered sentences, causal masking follows from the masked reference choice rule, and with a next-token cross-moment the score equals one causally masked attention head. We also discuss multi-head attention, weight-tied unembedding, and a heuristic reading of residual blocks as projected Langevin steps.

---


### 292. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](https://arxiv.org/abs/2610.39619)

**<font color=#1a73e8>作者：</font>** Guangyuan Li, Kelu Yao, Shuolin Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models aim to follow user actions while maintaining scene consistency over extended interactions. History-based methods reuse generated latents to preserve scene content, but three limitations of this reuse contribute to error recirculation. 1) The latent generated at each interaction is retained as history, potentially containing blurred details, geometric distortions, or semantic drift. 2) Although retrieved historical content matches the current scene, it can still contain errors that are carried into the next chunk. 3) New outputs then become history for later interactions, potentially reinforcing the same errors through repeated reuse. To limit this cycle, we aim to predict the future scene state from the current generated latent and the next action before generating the next interaction's video chunk. This future-state prior provides guidance for the next chunk, with the aim of reducing the errors carried forward from history. To this end, we propose a plug-and-play Causal Next-Chunk Predictor (C-NCP) with cross-model adaptability and prediction-guided modulation. We integrate C-NCP into four base generators and evaluate the augmented models across three benchmarks for interactive long-video generation and action-conditioned world modeling. Extensive experiments demonstrate reduced error accumulation and improved long-horizon consistency across diverse generation settings. The project page is at this https URL.

---


### 293. [FlexTry-On: A Time-Efficient Framework for Multi-Scenario Virtual Try-on](https://arxiv.org/abs/2610.39646)

**<font color=#1a73e8>作者：</font>** Phuong Dam, Quyen Nguyen Duc, Son Hoang Minh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on has achieved remarkable progress in recent years, yet most existing methods are designed for a specific scenario, such as cloth-to-person or person-to-person try-on, and often require separate conditioning strategies and processing pipelines for different settings. We present FlexTry-On, a unified and time-efficient diffusion-based framework for diverse virtual try-on scenarios, including cloth-to-person, person-to-person, cross-domain, and in-the-wild settings. FlexTry-On adopts a common conditioning formulation, where a text-aware condition extraction strategy converts heterogeneous garment sources into a unified representation, and a dual-conditioning diffusion transformer jointly models garment appearance and person identity. Extensive experiments demonstrate competitive performance on both cloth-to-person and person-to-person benchmarks while maintaining fast inference. Moreover, the same framework can be directly applied to unseen cross-domain scenarios without requiring separate architectures or scenario-specific processing pipelines. These results highlight the potential of unified and efficient virtual try-on frameworks as a practical step toward more flexible and widely applicable virtual try-on systems.

---


### 294. [Annotation-Free Representation Learning for Polyp Retrieval in Colonoscopy Videos](https://arxiv.org/abs/2610.39648)

**<font color=#1a73e8>作者：</font>** Luca Parolari, Lamberto Ballan, Carlo Biffi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Colonoscopy is inherently comparative: reliable visual assessment of polyps often depends on complementary views acquired under different viewpoints and imaging conditions. Retrieving such views requires polyp tracklet representations, which recent contrastive methods learn from temporal cues but still build from manually annotated bounding boxes. We propose an annotation-free framework that constructs tracklet views directly from raw colonoscopy videos, enabling temporal self-supervised learning on full-procedure videos, including frames without visible polyps. On REAL-Colon, our method achieves state-of-the-art results on tracklet retrieval and re-identification, outperforming both self-supervised and supervised baselines. We then introduce few-shot polyp retrieval, a task closer to clinical use, where a few observations of a target polyp are used to retrieve its remaining tracklets: with only two examples, our method surpasses most competing methods given ten. Finally, we show that a modest number of unlabeled procedures suffices for competitive performance, making on-site model development more practical. Code is available at this https URL.

---


### 295. [Towards Audience-Driven Real-Time Data Storytelling](https://arxiv.org/abs/2610.39658)

**<font color=#1a73e8>作者：</font>** Angelica Lo Duca  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces the concept of Audience-Driven Real-Time Data Storytelling (ADRDS), a framework that utilizes participatory and social sensing to enable audiences to actively shape the presentation of data stories. At its core, ADRDS employs a pre-authored decision tree, where the presenter defines the data story through a branching three-act arc (setup, conflict, and resolution). Each node contains a question, branching rules, thresholds for coverage, consensus, and confidence intervals, as well as one or more potential calls to action (CTAs). Audience members connect to the ADRDS framework via a URL on their mobile devices and answer questions in real time. ADRDS evaluates responses against the decision tree in real-time, following strong branches when thresholds are satisfied or activating fallback paths when signals are inconclusive. ADRDS then selects the final action consistent with the traversed path and the audience's demonstrated readiness, subject to fairness safeguards. ADRDS transforms presentations of data stories into audience-shaped decision processes, where live data actively drives the narrative. This work paves the way towards a new form of data storytelling, where the final data story depends on the audience's background and interests.

---


### 296. [AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers](https://arxiv.org/abs/2610.39663)

**<font color=#1a73e8>作者：</font>** Bin Xu, Mo Zhang, Zhengfeiyang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers generate high-quality videos, but the quadratic cost of 3D full attention dominates their inference. Dynamic block-sparse attention reduces this cost by computing exact attention only on key/value blocks selected from current activations. However, its fidelity degrades under aggressive sparsity: blocks are scored from coarse summaries or formed by costly global clustering, pruned blocks vanish from the softmax, and whole tiles are kept or dropped even when only a few of their keys matter. To address these limitations, we propose Accurate Block Attention (AB-Attention), a training-free method that accurately approximates dense attention at high sparsity. Its Intra-Block Clustering Selector (IBCS) estimates block importance faithfully yet cheaply by clustering queries only within each query block, without permuting tokens. Sampling with Inclusion-Probability Weighting (SIP) then samples blocks in proportion to these estimates and reweights them by inverse inclusion probability, so that one pass estimates dense attention rather than truncating it. Finally, its kernel gathers key/value blocks much smaller than a tile into full tensor-core tiles, refining selection at no extra tensor-core cost. On Wan2.1 and HunyuanVideo, AB-Attention skips 89--92\% of attention, whereas the baselines compute 1.8--3.6$\times$ as much, yet it still improves PSNR by up to 4.4~dB over the strongest baseline and achieves up to 2.23$\times$ end-to-end speedup. Our code is available at this https URL.

---


### 297. [A New AFIB Detection Method with Deep Neural Networks](https://arxiv.org/abs/2610.39665)

**<font color=#1a73e8>作者：</font>** Sara Gjorgjieva, Ana Angjelevska, Dimitar Trajanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early detection of atrial fibrillation (AFIB), characterized by irregular heart rhythms, can potentially save thousands of lives annually [20]. Numerous studies have attempted to address this challenge using various algorithms and methodologies. This paper introduces a novel and robust method that enhances the precision of AFIB detection. Neural Networks (NN) are widely recognized for their ability to identify complex electrocardiogram (ECG) patterns, facilitating the accurate detection of irregular heart rhythms. This study explores multiple conventional machine learning algorithms alongside neural network approaches to develop a robust AFIB detection system. To evaluate the effective- ness and robustness of the proposed method, the MIT BIH arrhythmia database (MITDB) and the Long-term Atrial Fibrillation Database (LTAFDB), both available on the Physionet site. Our approach presents a novel feature engineering technique, employing specific features such as a time series of the differences in successive heart rates (dBPM) rather than traditional inter-beat intervals. The model analyzes inputs labeled into five distinct classes, using only clean intervals identified through a new labeling method for training while treating others as outliers. This strategy ensures a more accurate and reliable AFIB detection process. The best-performing model, a Deep Neural Network (DNN), achieved an F1 score of 95.18% for binary atrial fibrillation classification on a benchmark dataset distinct from the training set. Models trained using our approach have demonstrated superior performance than previously published models.

---


### 298. [Event-SAMA: Language-Grounded Video Object Segmentation on Neuromorphic Event Streams](https://arxiv.org/abs/2610.39676)

**<font color=#1a73e8>作者：</font>** Sergei Fedorchenko, Max Zehnder, Nikola Zubić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event cameras offer microsecond temporal resolution, high dynamic range and no motion blur, but referring video object segmentation (RVOS) lacks event-stream datasets and models. We introduce Event-SAMA-239K, a synthetic-event conversion of the SAMA-239K grounded video-chat corpus and all additional SAMA training data: 30,650 video clips and 392,162 images. Optical-flow, FILM or saccade upsampling followed by a linear event generator preserves all mask, referring-expression and dialogue annotations. We also introduce Event-SAMA, adapting SAMA-4B with a two-channel polarity patch embedding initialised from pretrained RGB weights and a zero-initialised event adapter. End-to-end training yields 24.37 $\mathcal{J}\&\mathcal{F}$ on MeViS valid_u and 22.33 $\mathcal{J}\&\mathcal{F}$ on the converted ReVOS valid subset, establishing the first event-native RVOS baseline (RGB SAMA-4B: 55.4 on MeViS). Frozen RGB SAMA-4B with pseudo-RGB renderings or E2VID reconstructions of the same events scores 13.23 and 15.94 $\mathcal{J}\&\mathcal{F}$. Without retraining, Event-SAMA works on real event-camera recordings when the accumulation window matches their event density. A seed-controlled ablation with a measured noise floor of 0.47 $\mathcal{J}\&\mathcal{F}$ finds gains from diverse training sources over MeViS alone (+4.99), RGB-mean event-stem initialisation (+4.33), and a trainable SAM2 mask decoder (+2.76); the event adapter, partial ViT unfreezing and event polarity are within noise at this budget. An earlier, partially converted corpus snapshot trained with the identical recipe scores 1.38 $\mathcal{J}\&\mathcal{F}$ higher on MeViS and 1.12 higher on ReVOS. Both are single runs that also differ in schedule length, so we draw no conclusion about corpus scale.

---


### 299. [PairWatch: Pair-Aware Anomaly Transformer for Detecting Adversarial Rendezvous in Public Satellite Catalogs](https://arxiv.org/abs/2610.39679)

**<font color=#1a73e8>作者：</font>** Young Eun Kwon, Ji Won Yoon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Documented adversarial rendezvous and proximity operations (RPO) appear in the public TLE catalog, yet existing TLE-based maneuver detectors treat each satellite in isolation - mistaking routine station-keeping for adversarial behavior and missing RPO entirely when the target stays passive. We argue that the right unit is the satellite pair and the right inductive bias is the kinematic symmetry between approach and recede. We instantiate both with PairWatch, a pair-aware AnomalyTransformer whose attention prior is augmented with a sign-symmetric geometric similarity over relative-motion features, and release an open benchmark of 359 windows from public Space-Track data spanning 11 documented RPO events, 100 Clohessy-Wiltshire synthetic adversarial windows, and a five-class hard-negative set culminating in the TerraSAR-X / TanDEM-X helix formation. Under the deployment-relevant criterion of a single threshold separating real RPO from operational negatives - a necessary property for catalog-scale screening - PairWatch is the only model that succeeds, with the property holding in 100% of bootstrap resamples versus 0-19.5% for three neural baselines and under 0.1% for four physics-informed detectors. A per-source analysis exposes a shortcut-learning failure mode of single-number AUROC: simpler baselines attain higher overall AUROC by shortcutting a synthetic-vs-formation contrast with no operational meaning; removing this single cell flips the test ranking entirely (LSTM-AD), and these baselines fail the security-relevant task the benchmark was built to measure.

---


### 300. [Hardware-Aware Model Inversion in Memristive Spiking Neural Networks](https://arxiv.org/abs/2610.39688)

**<font color=#1a73e8>作者：</font>** Pablo Sorrentino, Fernando M. Quintana, Erika Covi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware-accelerated spiking neural networks (SNNs) implemented on memristive crossbar arrays offer significant gains in energy efficiency, while device variability and analog noise are sometimes assumed to hinder information extraction. However, whether these hardware effects improve, preserve, or degrade privacy after deployment remains largely unexplored. Therefore, we ask whether model-inversion leakage characterized on an SNN remains representative after the same model is mapped to a non-ideal memristive substrate, and how hardware non-idealities and reliability faults affecting synapses, neuron thresholds, and spike processing reshape that leakage. To study this problem, we introduce Spiking Domain Model Inversion (SDMI), an inversion method that combines Expectation over Transformation (EOT) with surrogate gradients to optimize inputs through stochastic analog behavior and non-differentiable spiking dynamics. We use SDMI consistently across the SNN model, its memristive SNN, and the same memristive SNN under additional hardware perturbations.
Across four datasets, reconstruction leakage does not vary monotonically with model accuracy or hardware variability. At comparable accuracy levels, neuron-threshold perturbations increase reconstruction fidelity, measured by SSIM, by up to 51.8%, whereas spike-level perturbations primarily degrade utility without consistently improving reconstruction. Weight noise, in contrast, reduces leakage under the same inversion procedure. These results show that hardware variability is not inherently privacy-preserving: model inversion leakage in memristive SNNs depends on the hardware state and cannot be inferred from model accuracy alone.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
