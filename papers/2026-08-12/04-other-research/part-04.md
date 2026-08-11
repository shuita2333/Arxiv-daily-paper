# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

---

### 151. [PARAGraph: Pathology-Anatomy-Aware Hierarchical Graph for Diabetic Retinopathy Grading](https://arxiv.org/abs/2608.08368)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Yuankai Huo, Yalin Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy (DR) remains a leading cause of vision loss among working-age adults worldwide, making reliable severity grading clinically important. Despite strong performance, most deep models formulate DR grading as image-level classification and do not explicitly model clinically grounded evidence, such as lesion types and spatial relations. In this paper, we propose PARAGraph, a Pathology-Anatomy-Aware Hierarchical Graph framework for DR grading. PARAGraph represents each image as a three-level hierarchical graph with lesion-level nodes, intermediate category and region nodes, and global anatomical and semantic nodes. To incorporate medical priors into nodes, we construct an optic disc-fovea-anchored coordinate frame that provides a scale- and rotation-normalized retinal reference system. Within this frame, lesion nodes are encoded with category, normalized area, and anatomical coordinates. To mitigate noisy lesion segmentation, PARAGraph uses a dual-fusion strategy that introduces global visual context into a graph semantic node and a decision-level prediction branch, improving robustness when lesion evidence is unreliable. Extensive experiments on Messidor-2, APTOS, and DDR show that PARAGraph achieves consistent DR grading performance over state-of-the-art methods. Interpretability and robustness analyses further demonstrate that its predictions are clinically grounded, closely associated with lesion evidence and robust to lesion segmentation noise.

---


### 152. [Gated Spatial Redundancy Projection for Pathology Transformer Attentions](https://arxiv.org/abs/2608.08374)

**<font color=#1a73e8>作者：</font>** Zhiyuan Yang, Jiahao Cheng, Vincent Quoc-Huy Trinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer models are increasingly used for whole-slide image analysis in computational pathology. Yet, WSIs differ fundamentally from natural images: neighbouring patches often contain highly similar tissue type, stain, texture, and cellular composition. We identify this local spatial redundancy as a pathology-specific failure mode of self-attention, where dominant neighbourhood features can be repeatedly mixed into patch-tokens and weaken subtle diagnostic or prognostic deviations. We propose Gated Spatial Redundancy Projection (Gated SRP), a lightweight drop-in correction module for self-attention layers. For each patch token and attention head, Gated SRP estimates a local redundancy axis from neighbouring value vectors, projects the attention output onto this axis, and applies a learned signed gate to correct the redundancy-aligned component geometrically. Across five TCGA survival cohorts, Gated SRP obtains the highest mean C-index among the compared attention variants in all cohorts, with an average improvement over the base attention, while adding only +0.02% parameters. Across five slide-level classification datasets, it improves the base attention on 12 of 16 reported metrics and achieves the best AUC on three datasets. Code is publicly available at this https URL.

---


### 153. [DoRF++: Spherical Representation Learning over Doppler Radiance Fields for Robust Wi-Fi Sensing](https://arxiv.org/abs/2608.08381)

**<font color=#1a73e8>作者：</font>** Navid Hasanzadeh, Shahrokh Valaee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motivated by the IEEE 802.11bf effort to standardize advanced WLAN sensing, interest in Wi-Fi Channel State Information (CSI) for passive, device-free, and privacy-preserving activity and gesture recognition has grown rapidly. Recent studies have shown that Doppler velocity projections extracted from CSI, which directly reflect human-motion velocity, enable more robust human activity recognition (HAR) and stronger generalization across users and unseen conditions. Nevertheless, reliable generalization under real-world variability remains a major challenge, hindering the adoption of Wi-Fi sensing in real-world applications. To address this challenge, we introduce Doppler Radiance Fields (DoRF), bringing the concept of neural radiance fields (NeRF) from computer vision into Wi-Fi sensing. DoRF models Doppler velocity projections extracted from Wi-Fi CSI as sparse and diverse virtual-camera views of human motion. It then infers a latent 3D motion sequence whose projections along learned effective Doppler directions explain the CSI-derived Doppler observations. The recovered motion is subsequently projected onto an equiangular grid of directions on the unit sphere, producing a spherical representation of the underlying motion. Since DoRF naturally defines the Doppler representation on spheres, we further introduce DoRF++, a spherical-learning design that applies spherical Transformers for activity classification. Experiments on our collected hand-gesture dataset show that DoRF++ significantly outperforms state-of-the-art Wi-Fi-based HAR methods in cross-user generalization accuracy, especially for difficult gestures in settings with a single multi-antenna receiver access point (AP).

---


### 154. [FZ-VIS: A Visual Analytics Framework for Quantities-of-Interest-Aware Scientific Lossy Compression](https://arxiv.org/abs/2608.08386)

**<font color=#1a73e8>作者：</font>** Guoxi Liu, Yuxiao Li, Congrong Ren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern scientific simulations generate massive volumes of data, making lossy compression essential for efficient storage and transmission. However, preserving critical quantities of interest (QoIs) under lossy compression is inherently data- and task-dependent, requiring domain scientists to navigate complex trade-offs between compression ratio and data fidelity. Exploring these trade-offs often involves large design and evaluation spaces, motivating human-in-the-loop approaches that combine interactive exploration with quantitative analysis. To address this challenge, we present FZ-VIS, an interactive framework for human-in-the-loop feature-oriented lossy compression design and visual analytics. FZ-VIS provides a web-based interface for rapidly generating and comparing compression configurations, along with integrated visualization tools for assessing reconstruction fidelity and QoI preservation through both visual inspection and quantitative metrics. We demonstrate the utility of FZ-VIS through case studies involving three representative user groups: novice users selecting compression methods, compressor developers examining internal pipeline behavior, and domain scientists investigating feature preservation. The case studies show how FZ-VIS helps users efficiently navigate complex design spaces and make informed decisions that balance compression performance with application-specific QoI requirements.

---


### 155. [Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research Agents](https://arxiv.org/abs/2608.08389)

**<font color=#1a73e8>作者：</font>** Harshitha Kolukuluru, Reshma Ashok, Kirat Arora 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon research agents solve open-ended tasks through iterative retrieval, aggregation, and synthesis, but context grows rapidly while the marginal value of additional evidence often declines. This leads to unnecessary token cost, higher latency, and noisier inputs for final report generation. We study marginal value estimation for context management in deep research agents and present the first systematic stage-aware comparison of pruning strategies across the pipeline. We evaluate lightweight heuristic criteria and a learned value model at pre-retrieval, post-retrieval, and pre-synthesis stages. Our results show that pruning effectiveness depends more on where pruning is applied than on the specific scoring rule: early pruning yields the largest end-to-end savings, while later pruning mainly refines the final synthesis context. Lightweight heuristics reduce token usage by up to 73% with little quality degradation, learned pruning remains competitive on selected trade-offs, and no single method dominates across quality, efficiency, and faithfulness. These findings provide practical guidance for designing efficient long-horizon agentic systems.

---


### 156. [Estimating Uncertainty in Galaxy Morphology Classification](https://arxiv.org/abs/2608.08398)

**<font color=#1a73e8>作者：</font>** Kai Cheng, Ruoqi Wang, Qiong Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Astronomers classify galaxy morphology to investigate cosmic evolution. While deep foundation models are increasingly utilized in Galaxy Morphology Classification (GMC), little work has been done on evaluating the uncertainty of GMC results. Uncertainty evaluation is important because astronomical data are inherently noisy due to instrumental and environmental limitations. Also, the continuous evolution of galaxies creates intrinsic morphological ambiguity. However, current foundation models operate as deterministic point estimators, failing to quantify the uncertainty. To overcome this limitation, we propose UEGMC, a post-hoc framework of Uncertainty Estimation for Galaxy Morphology Classification. It categorizes uncertainty in GMC into distinct types by model parameters, astronomical data, reference standards, or intrinsic physical ambiguities, thereby facilitating better classification. Our framework can directly predict uncertainties from representations extracted from the frozen backbones of foundation models, without computationally expensive sampling, therefore enabling fine-grained uncertainty evaluations. Our experimental results demonstrate that UEGMC provides competitive uncertainty quantification performance compared with previous methods.

---


### 157. [Exact Rank and Convex Calibration Dimension Lower Bounds for the Multi-Label F1 Loss](https://arxiv.org/abs/2608.08399)

**<font color=#1a73e8>作者：</font>** Mingyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The instance-wise $F_1$ measure is a central performance measure for multi-label classification. For a problem with $s$ labels, it defines a $2^s\times 2^s$ loss matrix. Previous work exhibited $s^2+1$-coordinate affine and shifted low-rank representations and used them to construct quadratic-dimensional convex calibrated surrogates. We determine the exact rank. Under the convention $F_1(\varnothing,\varnothing)=1$, the $F_1$ score matrix, the shifted loss matrix, and the unshifted loss matrix all have rank $s^2-s+2$, while the column-affine dimension of the loss is $s^2-s+1$. The proof factors the nonempty score matrix through subset-incidence matrices and a positive-definite Cauchy matrix.
Exact rank does not, by itself, lower-bound the dimension of an arbitrary convex calibrated surrogate. We therefore analyze the Bayes geometry of $F_1$ directly. We construct a distribution for which precisely all supersets of a fixed core label set are Bayes optimal, and show that the corresponding active loss columns, restricted to the witness support, have affine dimension $hn$, where $n=s-\lfloor s/3\rfloor$ and $h=\lceil(s\lfloor s/3\rfloor)^{1/2}\rceil-1$. Applying the feasible-subspace lower bound for convex calibration dimension gives \[
\operatorname{CCdim}(L^{F_1})
\ge \left(\frac{2}{3\sqrt{3}}-o(1)\right)s^2. \] Together with the quadratic upper bound, this establishes $\operatorname{CCdim}(L^{F_1})=\Theta(s^2)$.

---


### 158. [Anatomically Consistent Cross-Contrast Super-Resolution of Anisotropic Brain T2w MRI](https://arxiv.org/abs/2608.08401)

**<font color=#1a73e8>作者：</font>** Mengqi Shen, Haicheng Wang, Meghna Trivedi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> T2-weighted (T2w) brain MRI provides fluid-sensitive soft-tissue contrast that is important for neuro-oncology and radiotherapy planning. However, T2w scans are acquired with anisotropic voxels and appear blurred or stair-stepped on coronal and sagittal views, which obscures small structures and weakens any downstream 3D analysis. We propose VIPP-SR (View-Independent Patched Projection Super-Resolution), a cross-contrast guided super-resolution framework that restores the inter-plane resolution of an existing anisotropic T2w volume without an isotropic ground-truth T2w. VIPP-SR first trains a view-independent patched generator (VIP-GAN) to learn local T1c-to-T2w anatomical correspondence from high-resolution axial slices. The trained generator is then applied to axial, coronal, and sagittal views of the T1c volume to generate three orthogonal T2w estimates. Shape-preserving patching and deepest-skip removal reduce view-specific shortcuts, thereby constraining the generator to learn patch-local representations and enabling the zero-shot inter-plane transfer. Central to VIPP-SR, a projection-based optimization then enforces anatomical consistency across the three view-specific volumes, fusing them by balancing inter-plane self-consistency against per-view data fidelity. The generator is trained on BraTS-MET and evaluated on both the held-out BraTS-MET testing set and the BraTS-GLI cohort without retraining, assessing the cross-cohort generalizability. The results validate that VIPP-SR improves downstream segmentation over the real anisotropic T2w baseline, raising mean-label Dice from 0.330 to 0.465 on BraTS-MET and, zero-shot, from 0.473 to 0.563 on BraTS-GLI and ablation studies identify inter-plane self-consistency as the main source of the gain.

---


### 159. [Rethinking Learning-Based Influence Maximization: Simple Neural Surrogates and Native Discrete Search](https://arxiv.org/abs/2608.08406)

**<font color=#1a73e8>作者：</font>** Yiqiao Liao, Parinaz Naghizadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing learning-based influence maximization frameworks rely heavily on complex neural architectures and continuous optimization over seed representations. We challenge this paradigm with SIMBA, a diffusion-model-agnostic framework pairing a lightweight neural surrogate with direct discrete search. SIMBA introduces three key components: 1) uniformly anchored node embeddings that eliminate initialization noise and encourage learning driven by graph topology and diffusion pattern, 2) a shallow two-layer graph neural network surrogate predicting final infection states, and 3) batched multi-swap simulated annealing that explores combinatorial seed space without gradients or continuous relaxation. By shifting compute from complex representation learning to effective discrete search, SIMBA drastically cuts time-to-solution while achieving superior influence spread and data efficiency. Our code is available at this https URL.

---


### 160. [Constrained Learning with Universally Learnable Concept Classes](https://arxiv.org/abs/2608.08414)

**<font color=#1a73e8>作者：</font>** Herlock SeyedAbolfazl Rahimi, Spyridon Pougkakiotis, Dionysis Kalogerias  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study constrained statistical learning over infinite-dimensional hypothesis classes in the fully nonconvex setting, and establish universal PACC learnability of the solutions of dual algorithms: Probably Approximately Correct on Constraints, guaranteeing optimality and constraint satisfaction at once. This strengthens near-PACC results, whose feasibility residual no amount of data can remove. Optimality is caught between generalization, governed by Rademacher complexity and favoring small classes, and strong Lagrangian duality, which rests on Lyapunov convexity for vector measures and needs decomposability, a demand pulling the other way. We reconcile the two by posing the population problem over a universal RKHS $\mathcal{H}_K$, dense in a decomposable envelope, and learning over norm balls of growing radius. This yields the Tikhonov complexity $\mathfrak{T}^{\varepsilon}_{n}$, the least RKHS norm reaching an $\varepsilon$-optimal Lagrangian level set; we prove it finite, obtain exact learnability of the optimal value, and make the sample threshold explicit and polynomial in $1/\varepsilon$ under a source condition. Feasibility is harder: absent convexity the Lagrangian may not attain its infimum, and dual information pins down only an averaged constraint-risk vector, not the risks of any returned predictor. We introduce the closure-realization gap $\varepsilon^\star_\infty$, an index of how well $\mathcal{H}_K$ retrieves feasible solutions from dualization; it is a property of the problem, not of a modeling choice. Learnability is exact when $\varepsilon^\star_\infty=0$, in particular under dual differentiability, and near-PACC with residual exactly $\varepsilon^\star_\infty$ otherwise. Finally, no distribution-free threshold exists already in the unconstrained specialization, so universality is the canonical frame for dual algorithms over large hypothesis classes.

---


### 161. [Optimal Learning Under Tsybakov Noise](https://arxiv.org/abs/2608.08416)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Hongao Wang, Mingyue Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probably Approximately Correct (PAC) learning [Val84] is a fundamental learning model that has been extensively investigated. In this model, $\mathcal{H} \subseteq \{0,1\}^{\mathcal{X}}$ is a concept class, and $h^*\in\mathcal{H}$ is the target concept to be learned. Having access to i.i.d. labeled examples from a distribution $\mathcal{D}$ over $\mathcal{X}\times\{0,1\}$, which admits $h^*$ as the best concept in $\mathcal{H}$, the goal is to design a learning algorithm that outputs a hypothesis having low error competitive to $h^{*}$ with high probability.
This model was initially studied under the realizable setting, which assumes that $h^*$ has no error. A natural relaxation is to allow label noise, that is, the true label can be flipped with probability $\eta\in(0,1/2)$. In reality, certain labels might be extremely noisy, especially for those points near the decision boundary. Hence, it is natural to allow very noisy points, though only rarely. This is quantified by a noise model introduced by [MT99] and [Tsy04], now known as Tsybakov noise. For learning general concept classes, [MN06] gave the general upper and lower bounds for error guarantees under Tsybakov noise. However, their upper and lower bounds differ by a logarithmic factor. Resolving this gap has remained a well-known open question for the past twenty years.
In this work, we resolve this open question by improving the upper bound to match the best known lower bound, thus establishing the optimal error guarantee for learning under Tsybakov noise. Our learning algorithm operates by adaptively partitioning the instance space into regions, roughly corresponding to different noise levels, and returning a hypothesis in the concept class satisfying a specific error constraint for each region. Our technique shares a conceptual foundation with several recent advances in non-realizable learning, such as [HLZ24] and [Han25].

---


### 162. [Human-Guided Causal Knowledge Injection for Virtual Cells](https://arxiv.org/abs/2608.08430)

**<font color=#1a73e8>作者：</font>** Pengcheng Wang, Changjian Chen, Zhuo Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual cells employ machine learning models to simulate and predict cellular behaviors, serving as a critical computational framework for investigating health and disease. Injecting causal graphs into virtual cells can improve the interpretability, but such graphs are usually not available in real-world applications. Recently, many methods have been proposed to construct causal graphs from data, which group genes based on their similarities to form concepts and extract their causal relationships. However, since this automatic process is unsupervised, the causal graphs usually contain errors. In this paper, we propose a human-guided causal knowledge injection method for virtual cells. We developed a gene-similarity-aware causal graph visualization supported by a hybrid optimization algorithm to help explore both the causal relationships between concepts and the similarities between genes. Based on the exploration, we further developed a counterfactual analysis strategy supported by a counterfactual visualization and a causal path visualization to help validate and refine causal graphs. The effectiveness of our method is demonstrated through two real-world case studies, the extraction of scientifically meaningful causal insights, and positive feedback from domain experts.

---


### 163. [FreCast: Refining Radar Echo Intensity via Phase-Preserving Amplitude Residual Diffusion for Precipitation Nowcasting](https://arxiv.org/abs/2608.08436)

**<font color=#1a73e8>作者：</font>** Heping Fang, Zihuai Yin, Kaicheng Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting predicts the spatiotemporal evolution of future radar echoes from historical radar echo sequences, thereby estimating the occurrence, development, and movement of precipitation over the near term. In recent years, deep learning has become an important approach to precipitation nowcasting. Although state-of-the-art models can generally capture the overall spatial distribution of future precipitation, their predictions still exhibit substantial biases in radar echo intensity at individual locations. This observation motivates a more targeted strategy for reducing forecast errors. Instead of regenerating an entire radar echo sequence without spatial constraints, the predicted precipitation structure can be used to guide the refinement of echo intensities at individual locations. This structure-guided refinement directly targets echo intensity biases. Accordingly, we propose FreCast, a two-stage framework for radar echo prediction. The first stage generates an initial forecast of future radar echoes. The second stage uses the spatial structure of the initial forecast as a constraint to further correct intensity biases at individual locations in the first-stage prediction. Experiments on three datasets demonstrate that FreCast achieves consistent improvements across forecast skill metrics. Qualitative results further show that FreCast better preserves rainband continuity and intense precipitation structures at longer lead times.

---


### 164. [FSTC-Encoder: Feature--Spatial--Temporal Correlation Learning for Generalizable RF Sensing](https://arxiv.org/abs/2608.08439)

**<font color=#1a73e8>作者：</font>** Jing Wang, Zhu Wang, Changlong Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous RF sensing differs substantially in feature structure, spatial layout, and temporal scale, making existing models difficult to reuse across devices, environments, and RF modalities. We propose FSTC-Encoder, which unifies heterogeneous RF representation learning through feature, spatial, and temporal correlation modeling. Structure-aware feature encoding accommodates different signal structures, set-based spatial encoding aggregates variable observations, and hierarchical temporal encoding jointly captures local variations and long-range dependencies. Across sensing tasks and modalities, FSTC-Encoder retains the same spatial--temporal backbone architecture while varying only the feature configuration and task head. Across Widar3.0, CSI-Bench, and XRF55, FSTC-Encoder achieves 92.15% mean Accuracy under multi-factor cross-domain protocols, ranks first on three of four additional sensing tasks, remains consistently strong across WiFi, millimeter-wave radar, and RFID, and reduces the cross-modality performance gap from 18.85% to 12.93% through cross-RF learning. These results demonstrate that FSTC-Encoder achieves high domain robustness, task generality, and modality extensibility.

---


### 165. [MGMCL: Multi-Granularity Manifold Contrastive Learning With Neural ODEs for Cross-Subject EEG Emotion Recognition](https://arxiv.org/abs/2608.08440)

**<font color=#1a73e8>作者：</font>** Xiang Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject electroencephalogram (EEG)-based emotion recognition remains challenging due to substantial inter-individual variability and discrete formulation that overlooks affective continuity. Existing methods operate in Euclidean space and focus on marginal distribution alignment, failing to preserve the semantic structure of emotions across subjects. This article proposes MGMCL, reconceptualizing emotion recognition as learning continuous representations on symmetric positive definite (SPD) Riemannian manifolds. The frame?work introduces multi-granularity manifold contrastive learning at instance, emotion, and trajectory levels while preserving semantic ordering. Neural ordinary differential equations on manifolds model continuous emotion dynamics. Cross-subject generalization employs Gromov-Wasserstein manifold alignment. Weakly-supervised learning enables continuous valence-arousal-dominance prediction from discrete labels. Extensive experiments on three public datasets demonstrate state-of-the-art performance: 91.23% accuracy on SEED, 73.82% on SEED-IV, and 76.38% on DEAP, achieving consistent improvements of 1.89%, 1.66%, and 1.28% over previous best methods, respectively.

---


### 166. [InstructionCrafter: Generating Consistent and High-Fidelity Visual Instructions](https://arxiv.org/abs/2608.08460)

**<font color=#1a73e8>作者：</font>** Shun Okamoto, Satoshi Iizuka, Kazuhiro Fukui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given textual task instructions, generating step-by-step visual instructions as an image sequence requires the simultaneous satisfaction of multiple properties, specifically step faithfulness, cross-image consistency, and per-frame visual quality. Existing text-to-image generation approaches rarely meet all three properties, owing to independent sampling that breaks consistency, finetuning on low-quality video that degrades per-frame quality, and frozen backbones that lack multi-step understanding. In this work, we propose InstructionCrafter, a diffusion-based framework with the key idea of separating the optimization of temporal and instructional alignment from per-frame visual quality via (1) spatial-freeze training and (2) instruction-aware adapters. Built on a pretrained video diffusion backbone, InstructionCrafter freezes the spatial layers that control per-frame detail and updates only temporal and text-conditioning pathways to learn instruction semantics and inter-step relations, which preserves the generative prior for per-frame quality and reduces trainable parameters by about 50 percent compared with full finetuning. We also introduce two lightweight adapters that enhance the model's understanding of instructional context. The Consistent Adapter aggregates textual cues from the entire instruction sequence and from neighboring steps to keep object identity and attributes consistent across frames, and the Context-Aware Temporal Adapter converts cross-attention outputs into biases for temporal self-attention, explicitly propagating inter-frame relations. Extensive experiments on two benchmark datasets demonstrate state-of-the-art overall performance on step faithfulness, cross-image consistency, and per-frame visual quality while significantly reducing noise, blur, and spurious subtitles. Our code and trained models will be publicly available.

---


### 167. [Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses](https://arxiv.org/abs/2608.08466)

**<font color=#1a73e8>作者：</font>** Tailin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents are often improved by modifying prompts, tools, or workflows manually, while the executable scaffold surrounding the model---the \emph{harness}---is typically treated as a fixed artifact after deployment. This work studies an alternative where the harness is \emph{task-specific and continuously evolvable}: each task family maintains its own harness, which is hot-swapped across iterations through a fixed task-injection seam and rewritten using environment feedback. We introduce \textbf{Hierarchical Self-Improvement (HSI)}, a framework in which a single frozen LLM $M$ operates across three hierarchical scopes: a task harness $H$ that executes tasks, an evolver that rewrites $H$, and a meta-evolver that rewrites the evolver's strategy code under a frozen outer anchor. A thinking-on/off design isolates the contribution of harness evolution by disabling reasoning during task execution while enabling it during self-modification. HSI is bounded by two factors: a \emph{feedback-fidelity bound}, since evolution requires informative reward signals to guide selection, and a \emph{backbone capability bound}, since harness redesign cannot overcome limitations of the frozen model. On BALROG with DeepSeek-V4-Flash-Preview as the frozen backbone, HSI achieves consistent gains over the initial harness on moderate-difficulty tasks ($+39.3$ on BabyAI, $+33.0$ on Crafter, $+25.0$ on TextWorld, and $+15.0$ on MiniHack, all in raw \% Progress), while obtaining strong held-out generalization on BabaIsAI sub-suites ($0.98$ best-test on BreakStop and $1.00$ on GoTo from a $20\%$ unseen split). On tasks beyond the backbone's capability (NLE), harness evolution provides no improvement. These results demonstrate task-specific harness evolution as a viable axis for improving frozen LLM agents under clear empirical limits. Code is available at this https URL.

---


### 168. [RayLift: Lifting Complementary Ray-Wise Evidence with 3D Geometry Priors for Semantic Scene Completion](https://arxiv.org/abs/2608.08476)

**<font color=#1a73e8>作者：</font>** Meng Wang, Hongxia Yu, Wenzhe He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 3D semantic scene completion (SSC) provides comprehensive scene understanding for autonomous driving and robotics. However, existing methods often treat stereo depth estimates as deterministic geometric constraints, causing depth uncertainty and local correspondence errors to propagate directly into voxel representations. To address this issue, we propose RayLift, a framework that uses stereo geometry as a metric reference while incorporating complementary ray evidence to recover reliable 3D structures adaptively. RayLift first employs a Complementary Context Encoder that extracts geometry-aware priors from a frozen 3D vision foundation model, thereby enriching the scene context. It then introduces a Depth Ray Evidence Lifter module that jointly models geometric dissimilarity, depth confidence, and spatial uncertainty to adaptively sample and weight candidate surface locations along each camera ray. Finally, a Semantic-Aware Voxel Integrator injects the resulting ray evidence into voxel features by explicitly modeling their spatial support. Extensive experiments on SemanticKITTI and SSCBench-KITTI-360 demonstrate that RayLift achieves competitive performance and consistently outperforms existing methods.

---


### 169. [RenderMatte: Exact-Alpha Rendering and Group-Relative Alignment for Image Matting](https://arxiv.org/abs/2608.08487)

**<font color=#1a73e8>作者：</font>** Zecheng Ren, Yafei Hu, Jianing Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image matting is an essential enabling technology for modern visual content production, where foreground extraction determines the realism and editability of downstream creation workflows. However, precise alpha estimation in open-world scenes remains challenging because real foregrounds exhibit highly diverse appearances and opacity patterns. This makes existing methods struggle with semantic ambiguity and fine-grained opacity variation, especially in sparse boundary regions that are fragile and difficult to supervise. To address this gap, we present RenderMatte, a trimap-guided matting framework that adapts FLUX.1 Kontext through full-parameter fine-tuning, leveraging image editing priors for structure-preserving alpha prediction. During supervised adaptation, an alpha-edge objective preserves the latent flow-matching signal while strengthening pixel-space boundary supervision. We further introduce group-relative alpha alignment for post-training. It compares multiple mattes sampled under the same trimap condition using matting-specific rewards for alpha accuracy, boundary fidelity, trimap compliance, and compositional consistency. To overcome the lack of precise edge annotations, we construct the RenderMatte dataset, a large-scale synthetic dataset combining 3D-rendered RGBA foregrounds with diverse multi-source assets. It features exact strand-level alpha annotations and diverse background composites. Experiments show state-of-the-art performance across all benchmarks, demonstrating a scalable path toward high-fidelity matting in open-world scenes.

---


### 170. [No Unique Minimizer, No Problem: On the Consistency of Robust Neural Classifiers](https://arxiv.org/abs/2608.08489)

**<font color=#1a73e8>作者：</font>** Subhabrata Majumdar, Anand Deo, Partha Pratim Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network classifiers trained by cross-entropy minimization are highly sensitive to label noise and adversarial contamination. While robust alternatives offer bounded influence and resistance to corruption, their statistical foundations in the deep learning setting are insufficient due to a fundamental difficulty: neural parameterizations are non-identifiable, so the population loss minimizer is an equivalence class of parameters, not a unique point. We develop a consistency theory for robust neural classifiers based on the S-divergence family that requires no identifiability assumption. Casting training as stochastic optimization over a non-identifiable parameter space, we prove that empirical S-divergence minimizers converge to the population-optimal equivalence class under mild regularity conditions, and verify these conditions for three architecture choices. We further establish that limit points of the robust training algorithm are stationary points of the empirical objective. Experiments on vision and language benchmark datasets confirm that S-divergence training maintains clean-data accuracy while exhibiting performance competitive with existing robust methods.

---


### 171. [Linguistically-Aligned and Visually-Grounded Preference Optimization for Clinically-Augmented Medical Report Generation](https://arxiv.org/abs/2608.08494)

**<font color=#1a73e8>作者：</font>** Qiang Hu, Yuxuan Luo, Yingjie Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in Medical Report Generation (MRG), the reliability remains constrained by the prevalence of factual errors. While Direct Preference Optimization (DPO) has emerged as a promising post-training paradigm to enhance the performance of Supervised Fine-Tuned (SFT) MRG models, existing DPO-based MRG methods typically adopt a naive preference construction that directly pairs model-generated reports with ground truth reports. This strategy inadvertently entangles critical clinical findings with clinically irrelevant linguistic characteristics, and fundamentally lacks explicit vision-language alignment. To address these challenges, we propose DPO-Clin, a novel post-training framework that focuses preference optimization on clinical findings and cross-modal alignment. First, we introduce the Entity-level Clinical Diagnostic (ECD) module to perform a precise entity-level factual diagnosis. ECD guides the generation of linguistically-aligned report preference pairs, isolating clinical discrepancies from linguistic variations. Second, to achieve fine-grained cross-modal alignment, we develop M$^2$DPO, a retrieval-augmented multi-modal DPO variant that enforces textual preference inversion triggered by visual context switches. Third, we locate correct yet highly uncertain predicted entities and apply counterfactual modifications to construct targeted preference data for latent risk mitigation, thereby further enhancing the model reliability. Extensive experiments on two public chest X-ray datasets (MIMIC-CXR and IU X-Ray) and an in-house endoscopy dataset demonstrate that DPO-Clin significantly improves the SFT baselines on clinical-aware metrics. Furthermore, it achieves superior performance over existing DPO-based MRG methods, exhibiting robust generalizability across distinct baseline architectures and diverse medical imaging modalities.

---


### 172. [Towards Adaptive Super-Resolution and Quality Assessment via Test-Time Adaptation](https://arxiv.org/abs/2608.08508)

**<font color=#1a73e8>作者：</font>** Ajeet Kumar Verma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents doctoral research on adaptive video super-resolution and perceptual quality modeling under real-world conditions. Existing video super-resolution (VSR) methods struggle to generalize under unknown degradations arising from heterogeneous devices, codecs, and network environments. We address this challenge through test-time adaptation (TTA), a unified paradigm that improves robustness and perceptual quality without retraining or high-quality supervision. Specifically, we: 1) propose a TTA-based framework for no-reference video quality assessment (VQA), where adapted quality predictions provide perceptual guidance for VSR under unseen distortions; 2) develop a transformer-based architecture for screen-content super-resolution that preserves text clarity and structural fidelity; and 3) introduce a region-aware TTA strategy that selectively refines text and non-text regions without requiring high-resolution ground truth. Experimental results across diverse benchmarks demonstrate consistent improvements in perceptual quality and readability. We also outline ongoing work toward fully adaptive video enhancement systems capable of generalizing across unseen domains.

---


### 173. [Fluid Structure, Rigid Record: A Layered Organizational Design Framework for Agent-Native Organizations](https://arxiv.org/abs/2608.08516)

**<font color=#1a73e8>作者：</font>** Lucian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An agentic organization should not be a set of model instances with corporate titles, despite most MAS still operationalizing organization as a conversational topology, a role prompt, or a fixed workflow. This paper develops an agent-native organizational structure framework that separates the persistent and dynamic layers of operations. The persistent layer consists of a four-store record architecture and a pool of resident specialization agents. A coordination layer defines Permission as the boundary of the operational world available to an agent, and Privilege as the set of organizational state changes that the agent is authorized to initiate. Together, these mechanisms compile task-specific operational worlds. A runtime layer combines an external Workflow Protocol with an isolated runtime store to dynamically assemble Task Groups. A human-interaction layer exposes the organization through a Control Plane mediated by a non-decision-making Translation Agent. Three orthogonal Role Groups further separate Operation, Review, and Supervision. Operators execute within narrowly scoped leases; reviewers receive elevated but demand-activated authority to modify organizational state; supervisors retain broad observational access while holding limited modification authority. The resulting architecture is fluid at the execution surface but structurally rigid underneath: tasks and events may alter team composition, topology, views, tools, and workflows, while records, write constraints, authority boundaries, and separation of powers remain persistent. The architecture has been implemented as a prototype and evaluated in small-sample experiments. Large-scale empirical validation remains incomplete, therefore no general performance claimed is made yet. Instead, the contribution is a coherent and falsifiable framework for designing, governing, recovering, and evaluating agent-native organizations.

---


### 174. [eBIRD: Event-based Intensity Image Reconstruction Using Controllable Diffusion Models](https://arxiv.org/abs/2608.08519)

**<font color=#1a73e8>作者：</font>** Ignacio Bugueno-Cordova, Fabian Valderrama, Rodrigo Verschae  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intensity-image reconstruction from event streams remains a challenging problem due to the binary, sparse, and asynchronous nature of event data. This work proposes eBIRD, an event-guided reconstruction framework that combines a DDPM with ControlNet-based conditioning. We analyze generic and specialized diffusion learning strategies for handwritten digit (N-MNIST) and face (RGBE-Gaze) reconstruction using 33ms event windows. On N-MNIST, the general model achieves the best reconstruction quality (MSE 0.0052, SSIM 0.8982, PSNR 23.34dB), whereas the specialized model performs best on RGBE-Gaze (MSE 0.0161, SSIM 0.7605, PSNR 19.08dB). These preliminary results suggest that controllable diffusion models are a promising approach for event-guided intensity-image reconstruction, while highlighting that the preferred learning strategy depends on the reconstruction domain.

---


### 175. [A Combined Feature-Based Framework for Disguise and Spoofing Detection in Face Recognition Systems](https://arxiv.org/abs/2608.08521)

**<font color=#1a73e8>作者：</font>** Sangiya Pararajasingham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems face two distinct, commonly-separated failure modes: spoofing, where an impostor presents a photograph or video of an authorized user, and disguise, where a legitimate user is rejected because their appearance differs from their enrolled template due to accessories, facial hair, illumination, or pose. This paper proposes and compares five combined feature-extraction and classification pipelines that address both problems within a single framework: PM (PCA and Minimum Euclidean Distance, MED), LPM (Local Binary Patterns with PCA and MED), HPM (Histogram of Oriented Gradients with PCA and MED), SM (Speeded-Up Robust Features with MED), and HM (Harris corner features with MED). Each pipeline follows a common two-phase process comprising pre-processing, feature extraction, feature filtering, and classification. The methods were trained on 115 subjects drawn from the FEI, Disguised Faces Database, and NUAA databases and evaluated on six test conditions covering mixed appearances, frontal faces, dark illumination, left- and right-turned poses, and photo-spoofing attempts. The HOG-based pipeline (HPM) achieved the most consistent performance across conditions, with 94.59% accuracy on mixed-appearance disguise, 81.5-93.2% across pose and illumination variants, and 91.67% on spoofing, while the LBP-based pipeline (LPM) achieved the highest spoofing-detection accuracy (93.2%) but weaker robustness to pose change. These results reveal a measurable trade-off between spoof sensitivity and disguise robustness among classical feature representations, motivating the deep-learning and cross-database extensions discussed in the concluding sections.

---


### 176. [Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization](https://arxiv.org/abs/2608.08523)

**<font color=#1a73e8>作者：</font>** Pengfei Xu, Yong Liu, Xiaoya Nan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal embodied agents are increasingly required to solve long-horizon tasks by integrating visual observations, textual goals, and interaction history into closed-loop decision making. However, state-of-the-art large-model-based planners often rely on a single dominant planning style during execution. Once this execution mode becomes ineffective, the agent may remain stalled for many steps, repeatedly interacting with the environment without making meaningful progress. We address this limitation by proposing a Quality-Diversity (QD) framework for discovering diverse planning policies for multimodal embodied agents. The proposed method treats planning-policy templates as evolvable individuals and organizes them into a behavior-indexed archive rather than collapsing search to a single prompt style. In the offline stage, rollout trajectories are summarized into structured success and failure experiences, which guide policy variation through recombination and experience-guided mutation. The resulting policies are mapped into a behavior space defined by interaction intensity and goal-directedness, and the highest-quality policy in each niche is retained in the archive. In the online stage, the agent executes one policy at a time while monitoring task progress. When persistent stall is detected, the system rolls back to the latest checkpoint and switches to a behaviorally distinct archive policy to resume execution. Experiments on the ThreeDWorld transport benchmark show that the proposed framework improves both task success and interaction efficiency over representative baseline planners. These results suggest that discovering diverse policy repertoires is an effective way to support adaptive multimodal planning and online failure recovery.

---


### 177. [Out-of-Distribution Federated Distillation with Domain-Aware Proxy](https://arxiv.org/abs/2608.08525)

**<font color=#1a73e8>作者：</font>** Jiahao Xiao, Jiangming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning is a distributed machine learning paradigm that trains a global model by aggregating local clients without sharing private data of each client. Federated Distillation (FD) builds upon this paradigm by leveraging knowledge distillation to exchange soft predictions on proxy data instead of model parameters, enabling more efficient communication and supporting heterogeneous model collaboration. However, FD models trained on In-Distribution data are hardly adapted to Out-of-Distribution (OOD) scenarios. In this paper, we propose a domain-aware proxy selection framework to better adopt proxy data for OOD problems. The experimental results show that the proposed models effectively address the challenges of distribution shifts under OOD with and without proxy data by achieving average 82.9\% and 80.6\% over existing works on standard benchmarks. The codes and data are released in this https URL.

---


### 178. [ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints](https://arxiv.org/abs/2608.08531)

**<font color=#1a73e8>作者：</font>** Xiaoyang Bai, Zhenyang Li, Weiwei Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-driven representations such as neural radiance fields (NeRFs) and 3D Gaussian splatting (3DGS) have revolutionized the field of dynamic 3D scene reconstruction with improved visual precision and scalability. However, the reconstruction of fast-moving objects remains a challenge; existing methods based on conventional frame-based videos often struggle in scenarios such as sports events and animal videography. We propose an event-RGB fusion Gaussian splatting (ERF-GS) framework that integrates event information into both optimization and densification stages of the Gaussian splatting pipeline, taking advantage of novel event sensors with high frame-rate. Unlike many other event-assisted scene reconstruction methods, ERF-GS was developed using realistic simulation settings and realizes event-based learning detached from RGB inputs. This design enables its application beyond straightforward synthetic data into the realm of natural video with complex layout, low frame rates and severe motion blur. Our experiments show that ERF-GS outperforms both the 4DGS baseline and the concurrent E-D3DGS on different variants of the Neu3D and Nvidia datasets which include blurry RGB frames and disjoint RGB-event viewpoints. Our code is available at this https URL.

---


### 179. [Can Graph Learning Learn Circuits?](https://arxiv.org/abs/2608.08536)

**<font color=#1a73e8>作者：</font>** Chester Tan, Moritz Lampert, Courtney Maynard 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit localization is a mechanistic interpretability task whose goal is to identify a sparse subgraph of a transformer's computation graph sufficient to reproduce a particular behavior. Most established methods localize circuits independently for each model--task pair. We instead frame circuit localization as a graph machine learning problem in which the edges of a computation graph represent computational pathways, and graph neural networks (GNNs) model interactions among these pathways. We introduce Graph Circuit Learning (GCL), a supervised, amortized framework that trains a GNN across multiple model--task pairs and applies it to unseen cases. To provide sufficient data, we augment the InterpBench benchmark with additional cases derived from the TracrBench programs. Of the 14 evaluated GCL configurations, the highest scored a median edge AUROC of $0.902$ (interquartile interval $[0.861, 0.942]$) on the 16 original held-out InterpBench cases. This is close to the published InterpBench median of $0.910$ for EAP-IG while remaining below ACDC's $0.959$. Removing all message-passing edges reduces the median to $0.825$. We also adapt PGExplainer, a GNN explainability method, to circuit localization, obtaining a median edge AUROC of $0.858$ on the same cases. These preliminary results suggest that graph machine learning offers a natural and potentially powerful perspective on circuit localization, and we hope this perspective encourages closer exchange between the two communities.

---


### 180. [Rethinking Attention Locality in Spiking Transformers](https://arxiv.org/abs/2608.08541)

**<font color=#1a73e8>作者：</font>** Zeqi Zheng, Zizheng Zhu, Yuping Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking Transformers provide a promising paradigm for efficient visual processing with spike-driven computation, yet their Softmax-free Spiking Self-Attention (SSA) struggles to establish spatially localized token interactions. Although existing locality-enhanced SSA methods improve accuracy, it remains unclear whether they consistently induce spatial locality across layers and different Spiking Transformer architectures. Through Mean Attention Distance (MAD) analysis, we reveal that computational locality does not necessarily translate into spatial locality and show that uniformly applying the same locality enhancement overlooks architecture-dependent deployment requirements. Motivated by these observations, we propose Spatially Contiguous Local Attention with Boundary Continuity Pathway (SCLA-BCP). SCLA computes attention within non-overlapping regions of spatially adjacent tokens, while BCP facilitates cross-boundary information exchange through a lightweight convolutional pathway. Furthermore, we develop a hierarchical locality deployment strategy to effectively apply SCLA-BCP across the two major Spiking Transformer architectures. Extensive experiments on seven static and neuromorphic datasets covering classification, detection, and segmentation demonstrate consistent improvements with limited parameter and energy overhead. Notably, our approach improves mAP@50 by up to 9.50% on COCO 2017 and mIoU by up to 3.42% on ADE20K. Visualizations, MAD analysis, and ablation studies further validate its effectiveness.

---


### 181. [MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling](https://arxiv.org/abs/2608.08553)

**<font color=#1a73e8>作者：</font>** Rong Fu, Chunlei Meng, Yangchen Zeng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video super-resolution (VSR) aims to recover high-fidelity high-resolution videos from low-resolution inputs and is central to applications ranging from mobile capture to streaming and archival restoration. Existing approaches trade off among local-detail fidelity, long-range spatio-temporal modeling, perceptual realism, and efficiency: convolutional alignment techniques preserve local structure but suffer when motion is large or degradations are complex; transformer-based methods capture long-range dependencies yet require architectural or algorithmic adaptations to remain computationally feasible; and recent latent or diffusion-based generators synthesize rich texture but require specialized temporal constraints to maintain coherence. We present MotionCraft, a controllable VSR framework that formulates restoration as motion-aware latent state prediction inspired by world models and integrates adaptive sparse attention with an explicit user-accessible control interface. MotionCraft combines robust motion fusion, a Latent World Transformer that balances locality and targeted non-local interactions, and a compact conditional decoder to deliver temporally consistent, high-quality reconstructions under streaming constraints. Empirical evaluations show that MotionCraft achieves strong reconstruction and perceptual performance while enabling predictable trade-offs between temporal smoothness and reconstruction fidelity.

---


### 182. [SC-Diff: Semantically Calibrated Diffusion for Visible-to-Infrared Image Translation](https://arxiv.org/abs/2608.08555)

**<font color=#1a73e8>作者：</font>** Junyin Zhang, Siyu Huang, Jianxiong Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-to-infrared image translation provides a practical way to expand infrared training data using abundant visible images. Diffusion models are promising for this task because of their strong generative performance. However, existing diffusion-based methods typically use semantic priors only as external conditions, without explicitly regulating token interactions within the denoising network. Consequently, they struggle to preserve object locations, shapes, and semantic layouts required for reliable annotation reuse. We propose SC-Diff, a semantically calibrated latent diffusion framework that uses semantic priors for both conditional guidance and internal self-attention calibration. A pretrained SAM3 model with predefined text prompts first extracts category-specific semantic masks from visible images. These masks are merged into a semantic map and fused with the visible image as the input condition. The same map is converted into token-level semantic labels to calibrate self-attention in the denoising network. Based on these labels, we introduce Semantic-Guided Self-Attention Calibration (SGSC), which adaptively applies positive biases to query-key pairs of the same category. The query-wise calibration strength depends on the dispersion of attention across semantic categories and the attention assigned to the query's own category. The original attention scores further modulate the bias, giving greater calibration to same-category keys with stronger responses. This soft calibration reduces cross-category interference while retaining global contextual interactions, thereby improving semantic consistency in generated infrared images. Extensive experiments show that SC-Diff improves perceptual quality and produces more effective synthetic training data for downstream infrared object detection.

---


### 183. [OpenVisTool: An Open Recipe for Synthesizing Instructive Visual Tool-Use Trajectories](https://arxiv.org/abs/2608.08557)

**<font color=#1a73e8>作者：</font>** Changhao Xiang, Shilin Zhang, Zheng Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual tool use has emerged as a fundamental capability for multimodal agents to actively acquire evidence beyond a fixed image encoding. The prevailing recipe learns this capability from teacher-generated trajectories filtered for answer correctness, implicitly assuming that every successful demonstration provides effective supervision. We argue this assumption is flawed: a strong teacher often reaches the correct answer without needing its tool calls, and imitating such trajectories teaches a student that tool calls accompany correct answers, not that tool observations ground them. We present OpenVisTool, an open framework for constructing instructive visual tool-use trajectories that provide effective supervision for tool learning. The key insight is that a trajectory should be retained only if its answer is correct (outcome validity) and its tool observations causally contribute to that answer (causal utility). The framework operates in three stages: difficulty screening to select queries that are not reliably answerable without tools, domain-specific trajectory synthesis to elicit coherent tool-use trajectories, and supervision verification to jointly test both conditions. Rather than encouraging models to imitate tool calls, the resulting supervision teaches when and how visual evidence should be acquired. Using this framework, we construct OpenVisTool-42K, a dataset spanning five visual reasoning domains, together with OpenVisTool-Bench, a benchmark covering the same domains. Across four backbones (4B-27B), fine-tuning on OpenVisTool-42K consistently improves visual tool-use performance and yields gains on two out-of-distribution benchmarks; the larger models approach leading closed-source systems. The evidence suggests that effective visual tool use is learned from causally grounded supervision rather than tool-calling patterns.

---


### 184. [Deep probabilistic logic programming for diagnostic reasoning from incomplete information: A case study in stroke detection](https://arxiv.org/abs/2608.08561)

**<font color=#1a73e8>作者：</font>** Felix Weitkämper, Monchito Avila, Elizabeth Nanjala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In medical applications, raw data is frequently associated with significant privacy concerns, lending particular importance to the encoding of summary statistics from the literature. On the other hand, deep learning has become an invaluable tool for assessing symptoms based on visual or auditory sensor data. DeepProbLog allows for an extensible neuro-symbolic approach that accommodates connectionist components to analyse patient images within a transparent and rigorous probabilistic framework, namely probabilistic logic programming under the distribution semantics. Framed as a case study in stroke detection from multimodal data, this contribution explores the pathway from summary statistics available in the literature to a DeepProbLog-based diagnostic system. It suggests a workflow using established maximum entropy techniques to complete available probabilistic information and the probabilistic logic programming system ProbLog 2 to move from the entropy-maximising causal model to a discriminative neuro-symbolic model expressible within DeepProbLog. The relative performance of models derived from less complete data is analysed alongside the potential of the probabilistic inductive logic programming system ProbFOIL 2 for compressing large discriminative models, and the perspectives and implications of using DeepProbLog for diagnostic reasoning are discussed.

---


### 185. [On-Device Multi-Species Malaria Detection with Uncertainty-Calibrated Slide-Level Aggregation](https://arxiv.org/abs/2608.08566)

**<font color=#1a73e8>作者：</font>** Idaya Seidu, Ahmed Tahiru Issah, Charles B. Delahunt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Malaria remains a leading cause of mortality in resource-limited settings, where expert microscopists are scarce. Automated diagnosis based on microscopy images thus has strong potential to improve care delivery. But for an algorithm to deploy, a necessary requirement is that it meet a suite of non-obvious (from a machine learning (ML) perspective) clinical constraints. Therefore, in close consultation with a national health center we developed a malaria diagnosis pipeline which addresses key requirements listed by the health care center but typically ignored in the ML malaria literature. In particular, it includes: (i) stopping criteria (to reduce image acquisition and time-to-result); (ii) human-in-the-loop functionality (for review and accountability); (iii) multi-species discrimination (since treatment varies by species); (iv) thick film detection (standard for microscopy); (v) computationally-efficient uncertainty calculations (to aid clinician review); and (vi) an edge device platform (since internet can be spotty in this catchment area). The mobile system performs all inference on-device using YOLOv13n deployed via TensorFlow Lite. It detects four species and white blood cells from Giemsa-stained thick blood smear images, aggregating per-image detections into slide-level parasitemia with World Health Organization (WHO)-standard quantification. This paper highlights these various clinical constraints and offers methods to address them. Evaluated on 2,739 annotated images across all four species, the system achieves mAP@0.5 of 0.863, per-image parasite count correlation of r = 0.812, slide-level r = 0.951 (soft counting, 10 images/slide), and runs entirely offline with a pipeline time of 10.27 +- 1.65 s per image.

---


### 186. [Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks](https://arxiv.org/abs/2608.08567)

**<font color=#1a73e8>作者：</font>** Omer Yom Tov, Avigdor Gal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central obstacle in building graph foundation models is the input heterogeneity in terms of feature space dimensionality, semantics, and structure. Such heterogeneity limits the capability of graph neural networks to generalize to new graphs with unseen feature spaces. We address the transferability challenge with SIGIL, a framework that maps any attributed graph to a unified representation space of fixed dimension. Given a graph, SIGIL lifts it to a structural interaction graph, where nodes are the input feature dimensions and weighted, typed edges encode feature alignment across multiple orders of the graph's connectivity. A relational message-passing network embeds each feature dimension into a shared space, transforming the original node features, of arbitrary dimensionality, into representations transferable to any downstream graph. By construction, SIGIL is equivariant to permutations of nodes, feature dimensions, and labels. Additionally, when the input features are one-hot indicators of discrete relations, SIGIL recovers and strictly generalizes existing foundation models for knowledge graph reasoning. A single SIGIL model, pretrained on one graph, delivers strong fully-inductive link prediction. Also, SIGIL can be used to implement existing knowledge graph foundation models. As such, SIGIL unifies several existing regimes in graph foundation model design under a single framework

---


### 187. [Robust Reputation-Driven Crowdsourced Federated Learning](https://arxiv.org/abs/2608.08574)

**<font color=#1a73e8>作者：</font>** Mouhamed Amine Bouchiha, Gregory Blanc  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crowdsourced Federated Learning (CrowdFL) extends traditional federated learning by enabling open and heterogeneous participation through a crowdsourcing paradigm. In this setting, reputation-driven incentive mechanisms are commonly employed to guide worker selection and enhance trustworthiness. While such approaches improve participant reliability, existing frameworks largely overlook the quantification of their robustness against stealthy adversaries, particularly those capable of evading standard detection mechanisms. To fill this gap, this paper proposes R2CFL, a robust reputation-driven CrowdFL framework. R2CFL introduces a robust reputation model coupled with a nearest neighbor mixing (R2-NNM) defense mechanism that links reputation evolution with the filtering of updates during aggregation. The proposed mechanism prevents stealthy attackers from gradually accumulating trust and influencing future tasks. Experimental results demonstrate that R2-NNM matches or surpasses state-of-the-art Byzantine-robust and backdoor defense mechanisms against adaptive attackers. Furthermore, when integrated with existing detect-and-filter defenses, the proposed reputation model faithfully captures the statistical robustness of the underlying defense by producing reputation scores that closely reflect its true positive and false positive characteristics.

---


### 188. [CDGC-Net: 3D Medical Image Segmentation with Cooperative Dual-Scale Self-Attention and Grouped Channel Modeling](https://arxiv.org/abs/2608.08575)

**<font color=#1a73e8>作者：</font>** Zheyang Jing, Qin Lu, Jianwang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D medical image segmentation requires the integration of long-range anatomical context with fine boundary detail. Existing methods often model global and local features in separate modules or feature levels and perform channel recalibration independently. This may cause semantic mismatch between global context and local boundaries, insufficient channel relationship modeling, weak spatial-channel interaction, and redundant representations. We propose CDGC-Net, a 3D medical image segmentation network that combines cooperative dual-scale spatial attention with grouped hierarchical channel modeling. With-in each CDGC block, Cooperative Dual-Scale Self-Attention (CDSA) assigns attention heads to parallel local-window and global-sparse branches. The two branches capture fine spatial details and long-range anatomical context at the same feature level. Their outputs are concatenated into an $N\times C$ spatial representation and directly passed to Grouped Hierarchical Channel Attention (GHCA). GHCA organizes the channels into $r$ groups and models both within-group and cross-group dependencies. CDSA and GHCA reuse a shared key projection to maintain a consistent feature reference. Residual feature alignment subsequently integrates the refined features with the original representation. On the Synapse, ACDC, BraTS, and LA datasets, CDGC-Net achieved mean DSC values of 86.96\%, 92.91\%, 82.56\%, and 93.52\%, respectively, exceeding the next-highest reported values by 0.39, 0.47, 0.17, and 0.32 percentage points. CDGC-Net contains 25.83M parameters and 28.62G FLOPs for an input size of $64\times128\times128$, reducing these quantities by 39.87\% and 40.30\%, respectively, relative to UNETR++. These results indicate a favorable trade-off between segmentation accuracy and computational complexity.

---


### 189. [When Can Fraud Operations Authorize Automation? A Decision-Support Framework for Fresh Audit Evidence and Review Workload](https://arxiv.org/abs/2608.08577)

**<font color=#1a73e8>作者：</font>** Jie Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fraud operations must allocate events among automatic approval, analyst review, and automatic blocking even though the labels needed to evaluate these actions are selective and delayed. Predictive scores order cases, but they do not show whether the evidence is current and representative enough to delegate an action to the model. We develop freshness-constrained audit capacity (FCAC), a decision-support framework that treats automation as an authorization decision constrained by action risk, evidence freshness, and shared review capacity. It evaluates candidate action regions from mature randomized audits and a prespecified temporal allowance. Supported regions are automated; unsupported regions remain in review. The resulting decision record reports evidence age, audit demand, total review workload, value exposure, and compatible temporal change. We show that current action risk is unidentified without restricting unobserved label evolution. Under representative randomized audits, label-independent evidence windows, and a prespecified condition linking historical and current action risk, we derive simultaneous finite-sample control of unsafe authorization. Chronological evaluations with simulated audits on IEEE-CIS, ULB-Worldline, and Elliptic++ yield zero-drift automation rates of 84.4%, 67.4%, and 81.3%, with total review workloads of 24.1%, 46.0%, and 43.1%. The experiments reveal an audit-capacity trade-off: sparse auditing delays authorization, whereas intensive auditing eventually increases workload. A separately specified BAF stress test further indicates that fallback thresholds must reflect candidate-specific evidence rather than a common fraction of the risk limit. These findings identify audit freshness and analyst capacity as joint design considerations for fraud decision support.

---


### 190. [Where Is the Bee? Detecting Tiny Pollinators with a Single Collaborative-Head Transformer](https://arxiv.org/abs/2608.08580)

**<font color=#1a73e8>作者：</font>** Junsu Kim, Seungryul Baek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The CVPPA@ECCV 2026 BuzzSpot Challenge asks us to detect bees, bumblebees, hoverflies, and moths in 1920x1080 field keyframes. Its annotations carry 2 difficulties: the median box occupies 0.16% of a frame, and bees account for 80% of the labels. To cope with the small boxes, we compare 10 recorded detector configurations on held-out keyframes; plain Co-DINO with a Swin-L backbone has the highest mAP in this comparison, so we select it. Training then addresses the bee dominance in 2 ways: fine-tuning on a crop-mosaic pool in which the combined annotation share of the 3 rare classes rises from 19.9% to 55.1%, and a class-weighted simplex equiangular tight frame (ETF) loss that pulls the projected states of matched decoder queries toward fixed class directions. The full schedule spans 12+3+2 epochs. Without inference-time ensembling or test-time augmentation, we rank first on FinalTest at 0.5062 mAP@[.5:.95].

---


### 191. [EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585)

**<font color=#1a73e8>作者：</font>** Zixuan Chen, Jiakai Zhang, Junhao Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras, with high temporal resolution, high dynamic range, and asynchronous sensing characteristics, have shown great potential for dense 3D reconstruction. Traditional reconstruction methods based on off-the-shelf pose estimates achieve high efficiency but produce low-fidelity results, as inaccurate pose initialization introduces cumulative reconstruction errors. In contrast, recent SLAM-style methods stabilize joint pose-scene optimization through incremental tracking and mapping, yielding higher reconstruction fidelity at the expense of considerable computational overhead. To address this trade-off, this paper presents EvTrajGS, an accurate and efficient 3D Gaussian Splatting framework for unposed event streams. Our method enables reliable joint pose-scene optimization initialized from coarse pose priors, eliminating the need for computationally expensive SLAM-style pipelines. EvTrajGS parameterizes camera motion as a continuous-time trajectory initialized from discrete camera poses, providing a unified representation for pose refinement. We then aggregate adjacent trajectory states into a temporally coupled pose, promoting temporally consistent pose updates during joint optimization. Additionally, we introduce a loss-reweighted event sampling strategy to adaptively emphasize temporally under-reconstructed intervals. Extensive experiments on both synthetic and real-world datasets demonstrate that EvTrajGS outperforms state-of-the-art methods in terms of both geometric reconstruction quality and pose estimation accuracy, achieving 3.8 dB higher PSNR, 0.1 higher SSIM, and over 40\% lower ATE RMSE while retaining high computational efficiency.

---


### 192. [SDDBMs: Soft Denoising Diffusion Bridge Models](https://arxiv.org/abs/2608.08594)

**<font color=#1a73e8>作者：</font>** Shiyi Qi, Kun He, Mingmou Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion bridge models leverage Doob's \(h\)-transform to construct stochastic transports between arbitrary endpoint distributions, and have shown strong potential in image-to-image translation and restoration. However, most existing bridge models rely on hard endpoint conditioning, which forces the terminal state to match a prescribed target exactly. This hard constraint induces terminal-boundary singularities: the terminal law collapses to a Dirac measure, and the resulting drift coefficients become ill-conditioned near the endpoint. In this paper, we propose Soft Denoising Diffusion Bridge Models (SDDBMs), a generalized framework that regularizes diffusion bridges directly at the level of their terminal constraints. Instead of imposing an exact endpoint, SDDBMs prescribe a non-degenerate Gaussian terminal marginal under the transformed path measure, with a flexible terminal center and variance. Starting from this prescribed marginal, we develop a complete closed-form construction of the soft bridge, including the Gaussian terminal reweighting and soft \(h\)-function, the induced Gaussian forward marginals and \(\mathbf{x}_0\)-free dynamics. Theoretically, SDDBMs provide a unified probabilistic perspective that encompasses existing diffusion bridge models, including DDBMs, GOUB, and UniDB, as special cases under specific parameter choices. Extensive experiments on image restoration tasks demonstrate that SDDBMs achieve improved numerical stability and superior generation quality over existing bridge-based methods.

---


### 193. [Population-Scalable Multi-Agent World Modeling](https://arxiv.org/abs/2608.08600)

**<font color=#1a73e8>作者：</font>** Renjie Zhao, Yuxiang Wu, Mingyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models have recently achieved impressive progress in visual prediction and interactive generation, but extending them to multi-agent environments introduces a fundamental scalability challenge. Existing methods generally assume a fixed number of agents during training and inference, which ties the model to a pre-determined agent population and limits inference-time scalability. Our key insight is that cross-view consistency should arise from a shared world state whose evolution does not assume a predefined number of agents, while agent-specific observations should be generated by querying this state through a unified rendering interface. Based on this insight, we propose Khora, a scalable multi-agent world model that supports inference-time expansion to arbitrary numbers of agents without retraining. Our framework decouples world-state evolution from visual rendering and introduces a population-agnostic rendering mechanism for incorporating other agent information. This design maintains cross-view consistency through the shared world state rather than through dense interactions among observation streams inside the expensive video generator, enabling approximately linear practical scaling with the number of queried views. Qualitative experiments demonstrate that our approach generalizes to unseen numbers of agents while maintaining visual quality and multi-agent consistency. We further implement a real-time interactive system to demonstrate scalable open-world simulation.

---


### 194. [Multi-Agent Reinforcement Learning via Agent-Specific Preference](https://arxiv.org/abs/2608.08604)

**<font color=#1a73e8>作者：</font>** Ni Mu, Yao Luan, Yiqin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) is a powerful framework for solving complex collaborative tasks, but it relies heavily on well-defined global reward functions. Designing such rewards is challenging, especially in systems with heterogeneous agents, where a single scalar objective may fail to capture diverse behaviors. In this paper, we introduce Multi-AGent Preference-Integrated lEarning (MAGPIE), which addresses these challenges through agent-specific preference modeling. Each agent is evaluated by a dedicated expert through preference signals, eliminating the need for global evaluation. We theoretically prove that optimizing these decentralized preferences converges to a Nash equilibrium policy. To integrate local preferences into a coherent global objective, we construct agent-specific reward models from preference data and combine them via a monotonic aggregation mechanism. We further prove that optimizing this aggregate reward model is equivalent to training the Nash equilibrium policy. Extensive experiments on benchmark multi-agent tasks and a sequential production line task show that MAGPIE achieves performance comparable to reward-engineered baselines, demonstrating its potential to facilitate policy learning in scenarios where precise reward engineering is impractical.

---


### 195. [North Africa's Missing Framework: NLP-Driven Mental Healthcare in Algeria and Implications for Low-resource Settings](https://arxiv.org/abs/2608.08607)

**<font color=#1a73e8>作者：</font>** Meriem Laifa, Abdallah Bengueddoudj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health disorders are a leading cause of disability worldwide, yet Natural Language Processing (NLP) research for mental healthcare has remained concentrated in high-income, English-language settings. North Africa, and Algeria in particular, is largely absent from this literature despite its unique linguistic, historical, and healthcare context. We present the first conceptual framework examining the potential role of NLP within Algeria's mental healthcare system. Drawing on narrative synthesis of global NLP mental health research, Algerian healthcare literature, and low-resource NLP methodologies, we identify four structural barriers to mental healthcare: the language-of-care gap, geographic inequities in access, stigma-related barriers to help-seeking, and the absence of research and digital infrastructure. We then map existing NLP capabilities to each barrier, outlining their potential applications, implementation constraints, and the technical, institutional, and governance requirements necessary for deployment. Based on this analysis, we propose a research and policy roadmap that prioritizes data resources, multilingual language technologies, evaluation frameworks, and regulatory capacity. Although grounded in the Algerian context, the framework addresses challenges common to many multilingual, low-resource, and post-colonial settings. This work provides a foundation for future research on culturally and linguistically appropriate NLP for mental healthcare and offers a practical roadmap for developing responsible AI-enabled mental health systems in underrepresented regions.

---


### 196. [REVEAL: A Rubric-Guided Agent for Explicit Evidence Sufficiency Verificationin Long-Video Question Answering](https://arxiv.org/abs/2608.08612)

**<font color=#1a73e8>作者：</font>** Caijun Yan, Yang Zhou, Meixing Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, retrieval-augmented and memory-augmented methods have emerged as two promising paradigms for long-video question answering. However, existing methods typically rely on rigid, fixed-length temporal chunking (e.g., 10s) and static offline memory banks, which not only fragment coherent continuous events but also fail to adapt during real-time reasoning. Moreover, whether using multi-scale summaries or multimodal knowledge graphs, current approaches prioritize retrieval relevance while overlooking evidence sufficiency, often stopping to answer once only semantically relevant clues are retrieved, even when key temporal, causal, or fine-grained action evidence is still missing. To tackle these challenges, we propose REVEAL, a rubric-guided agent framework. As a foundation, we introduce an adaptive visual-similarity-based preprocessing pipeline that groups visually coherent adjacent frames into natural event units to construct an offline-online video memory---capturing global video context offline while dynamically maintaining question-conditioned memory online. Built upon this structured memory, REVEAL uses an automatically constructed rubric library to explicitly verify whether retrieved evidence satisfies sufficiency criteria, pinpoints missing clues upon verification failure, and directs targeted re-retrieval for complementary information. Without any extra training, REVEAL consistently outperforms both closed-source and open-source state-of-the-art methods across extensive experiments. These results show that explicitly verifying evidence sufficiency, rather than stopping at semantic relevance, retrieves the decisive clues that prior methods miss and yields more reliable long-video reasoning.

---


### 197. [Walking through Discussions: A Mobile Visual Analytics System for In-Situ Group Discussion Analysis](https://arxiv.org/abs/2608.08617)

**<font color=#1a73e8>作者：</font>** Yiping Sun, Ziyao Kang, Wei Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group discussion-based teaching is widely used to foster collaborative learning, yet teachers in physical classrooms often struggle to simultaneously monitor multiple groups and quickly diagnose a target group before intervening. Existing visual analytics tools primarily support post-hoc analysis on desktop, providing limited support for in-situ walk-around teaching. To address this gap, we present MobileGroupVis, a mobile visual analytics system for in-situ analysis of classroom group discussions. MobileGroupVis integrates multi-group monitoring, single-group diagnosis, and instructional intervention into a concise analytical workflow tailored for small-screen touch interaction. The system is powered by a lightweight streaming analysis pipeline that converts group audio into structured discussion data and further extracts interaction patterns, topic progression, and topic deviation through a dialogue analysis module. To enable both glanceable overview and traceable diagnosis, we design six coordinated views, including a compact glyph that visually encodes word count, interaction intensity, and topic deviation for efficient cross-group comparison and anomaly localization, along with detailed views for opinion evolution, interaction dynamics, topic coverage, and dialogue records. We evaluate MobileGroupVis through two case studies and expert interviews. The results provide preliminary evidence that MobileGroupVis supports teachers in understanding discussion processes, identifying groups in need of attention, and facilitating in-class intervention.

---


### 198. [MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning](https://arxiv.org/abs/2608.08623)

**<font color=#1a73e8>作者：</font>** Haotian Wang, Lian Yan, Xingzhi Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Reinforcement Learning with Verifiable Rewards (RLVR) frameworks for mathematical reasoning tasks, floating-point results are typically evaluated using a tolerance-based reward. However, this strategy suffers from challenges such as difficulty in threshold calibration, unstable training dynamics, and limited accuracy, especially in clinical scenarios. To address these limitations, we propose a knowledge-guided hybrid reward framework (\textsc{MedCalc-R1}). Specifically, we introduce a knowledge verification reward mechanism that enforces explicit generation of computational formulas, which are further validated by an external verifier to enhance interpretability and reasoning reliability. Furthermore, we design a hybrid soft-hard reward scheme combining a hard constraint based on clinical safety thresholds with a soft, precision-sensitive reward that progressively guides learning within the acceptable range. Experimental results demonstrate that our method significantly outperforms existing baselines in both reasoning accuracy and generalization capability, validating the effectiveness and applicability in safety-critical domains.

---


### 199. [Domain-Aware Pruning: Sparsity and Domain Generalization via Regularized Probabilistic Masking](https://arxiv.org/abs/2608.08624)

**<font color=#1a73e8>作者：</font>** Parham Sazdar, Mostafa Tavassolipour, Reshad Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) and neural network pruning are conventionally treated as distinct objectives, targeting out-of-distribution (OOD) robustness and model efficiency, respectively. In this work, we bridge this gap by introducing Domain-Aware Pruning (DAP), a framework that leverages network sparsity as a mechanism to implicitly enhance generalization to unseen domains. Diverging from standard binary mask optimization, DAP learns a continuous parameter retention probability $p \in [0, 1]$, framing network compression as a continuous probabilistic masking problem. By introducing a regularization objective that actively penalizes the retention of domain-sensitive weights during the mask training, DAP identifies a domain-invariant subnetwork. Empirical results across five DG benchmark datasets demonstrate that DAP achieves significant sparsity while consistently matching or exceeding the OOD performance of its dense counterparts. Crucially, DAP is an algorithm-agnostic framework that integrates seamlessly with existing DG pipelines without necessitating post-hoc fine-tuning. Beyond efficiency and generalization, we show that DAP natively provides increased robustness to adversarial perturbations and yields highly interpretable models, where the retained weights reliably encapsulate the most domain-invariant and task-critical representations.

---


### 200. [Trajectory Design and Budgeted Querying for Digital Twin Calibration](https://arxiv.org/abs/2608.08631)

**<font color=#1a73e8>作者：</font>** Vladyslava Spitkovska, Dmytro Kuzmenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital-twin calibration requires interaction data that is expensive to collect. We study two acquisition decisions: which trajectories to generate, and when to spend a limited budget on privileged parameter measurements. Our framework couples an excitation-oriented reinforcement learning controller, a recurrent parameter estimator with predictive uncertainty, and a budgeted query policy. In Pendulum, a Random Forest diagnostic recovers gravity only weakly from task-oriented trajectories and does not recover mass or length, while a GRU trained on excitation-oriented trajectories reaches a mean absolute error of 0.0066 with no queries. We then withdraw continuous oracle access partway through an episode, so that the twin must run on the estimator's output for the remainder. The estimator-plus-policy pipeline achieves a terminal error of 0.0092 under a three-query budget, against 0.2031 for an uncalibrated twin. In partially observable Waterworld, five controllers produce different observed error profiles across three hidden parameters, and an estimator trained on a five-controller mixture reaches online normalized errors of roughly 4-5%. These exploratory case studies are not controlled ablations, but they motivate treating trajectory design and query allocation as explicit design variables in data-scarce calibration.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
