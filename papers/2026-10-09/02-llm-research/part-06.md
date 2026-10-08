# 🧠 大模型相关研究 | 2026年10月09日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

---

### 251. [SAREO-FM: Decoupled Semantic Supervision for SAR-EO Foundation Models](https://arxiv.org/abs/2610.09317)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR) and electro-optical (EO) imagery provide complementary observations: SAR enables day-and-night, weather-resilient sensing, whereas EO provides rich appearance and fine-grained semantic cues. We introduce SAREO-FM, which avoids forcing a single token stream to serve two distinct roles: modality tokens preserve how each sensor observes the scene through masked reconstruction, while learnable semantic queries capture what the scene contains under guidance from a pretrained vision foundation model (VFM). By jointly encoding these queries with SAR and EO tokens, the queries acquire modality-grounded semantic context, while the modality-token outputs remain the explicit targets of masked reconstruction. This design assigns semantic and reconstruction supervision to separate token streams while preserving their interaction within the shared encoder. Pretrained on the million-scale SAR-1M corpus, SAREO-FM achieves strong unimodal transfer for both SAR-only and EO-only inputs, while delivering substantial gains from joint SAR--EO observations on tasks that benefit from complementary sensing.

---


### 252. [TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning](https://arxiv.org/abs/2610.09360)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruochi Li, Jianzhe Lin, Haoxuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world documents distribute evidence across text, tables, figures, and captions within complex page layouts. Answering complex questions over such documents therefore requires more than retrieving relevant passages: systems must recover the evidence topology that connects heterogeneous evidence units. Existing GraphRAG evaluations remain largely text-centered, while multimodal document RAG benchmarks assess cross-modal retrieval and generation without directly evaluating recovery of the intended evidence topology. We introduce TOPOGRAPHRAG-BENCH, a layout-grounded benchmark for multimodal evidence reasoning in GraphRAG, comprising 2,024 questions over 201 long, visually rich documents. Questions are constructed bottom-up from text, figure, and table evidence units under three controlled topologies: single-hop retrieval, bridge-chain reasoning, and multi-source synthesis. To ensure that questions preserve their intended structure, we apply counterfactual validation for shortcut resistance, modality necessity, and evidence necessity. We evaluate text-only GraphRAG, page-level visual retrieval, and multimodal GraphRAG systems using retrieval, generation, and topology-aware reasoning metrics. Multimodal GraphRAG systems achieve the strongest overall performance, but still fail when visual-textual evidence alignment or multi-unit composition is incomplete. Text-only GraphRAG struggles when key dependencies are grounded in figures or tables, while page-level visual retrieval lacks the fine-grained structure needed for topology recovery. These findings motivate GraphRAG systems that move beyond text-derived entity relation graphs to explicitly model document layouts, cross-modal evidence alignment, and the reasoning roles of evidence units. Code and data are available at this https URL.

---


### 253. [RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning](https://arxiv.org/abs/2610.09455)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seungjun Moon, Subin Jeon, Sangwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy training. To this end, we propose RLHND, a video foundation model-based hand tracking model that jointly estimates hand pose and realistic tactile information from monocular egocentric videos. RLHND turns the pre-trained Cosmos 3 video diffusion backbone into a deterministic clip-level feature extractor via clean-latent conditioning, carrying its learned priors on hand motion and hand-object interaction into tracking. For pose estimation, RLHND (i) predicts hand poses with anatomically plausible joint angles and (ii) enables optional conditioning on the shape parameter to maintain consistent hand shape within the same video and even across videos recorded by the same actor. For tactile estimation, a separate tactile expert stream, trained with the pose stream frozen, predicts dense contact and force over the hand surface. We further adopt LBS-based feature spreading to enable vertex-wise feature extraction without costly per-vertex attention. RLHND achieves state-of-the-art performance across various benchmark datasets for pose estimation, while also achieving state-of-the-art performance in contact and force estimation. Moreover, we demonstrate the utility of RLHND for robot learning through retargeting results and real-world robot experiments. The code will be publicly available at this https URL.

---


### 254. [CHASE: Channel-Aligned Structure Exploitation for Geometry-Aware Model Engineering](https://arxiv.org/abs/2610.09476)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wei Wang, Wei Jiang, Ziran Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometric and Spectral Alignment (GSA) characterizes trained networks through spectral concentration, physical-channel alignment, support structure, and changes in singular bases. In this paper, we propose CHASE (Channel-Aligned Structure Exploitation) to use these structures in practical model design. CHASE covers six applications across model modification, reconfiguration, and compression. CORA, COEC, and CORAM apply GSA to parameter-efficient finetuning, structured-pruning compensation, and model merging. We further develop three new methods. CAGA uses GSA to identify multi-head attention heads that can share a KV representation and constructs the shared key and value heads through geometric alignment and low-rank subspace extraction. SAKV uses GSA to determine which adjacent layers can share a low-rank KV-cache representation and the retained rank for each layer group. CAPS uses GSA spectral structure to group output neurons and selects retained input channels separately for each group. Results from CORA, COEC, and CORAM establish the effectiveness of GSA for adaptation, pruning compensation, and model merging. Experiments on CAGA show that geometric shared-head construction substantially improves MHA-to-GQA conversion, and SAKV and CAPS improve over representative baselines for KV-cache compression and structured pruning. These results show that the structures identified by GSA can be used directly to design methods for a range of model operations.

---


### 255. [WAPR: A Foundation Model for Wide-Angle Refinement in Unseen Object Pose Estimation](https://arxiv.org/abs/2610.09535)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yulin Wang, Mengting Hu, Hongli Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world applications require 6D pose estimation to be accurate, fast, and scalable to unseen objects. This paper introduces WAPR, a zero-shot wide-angle pose refinement model that refines candidate poses with rotational deviations up to 90 degrees. With as few as 12 candidate poses per detected object instance, WAPR supports fast inference within 1 s per frame and reaches a pose-estimation throughput of up to 25 detected object instances per second. To support wide-angle training for rotationally symmetric objects, WAPR uses rotational symmetry priors to canonicalize symmetry-equivalent pose targets before loss computation. We further construct SA6D, a large-scale 6D training dataset with such priors. SA6D obtains KASAL-assisted rotational symmetry priors for 944 GSO scans and expands them through geometry and texture augmentation into about 50K augmented object instances and about 2M rendered RGB-D images. In addition, an angle-balanced loss stabilizes learning across different angular ranges by reducing the influence of uninformative large-error cases. Experiments on seven BOP core datasets show that WAPR achieves state-of-the-art performance in unseen-object 6D pose localization and detection under both fast and unconstrained inference settings. Project page: this https URL.

---


### 256. [Constitution-Guided Watermarking](https://arxiv.org/abs/2610.09552)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Toluwani Aremu, Samuele Poppi, Nils Lukas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking enables language model providers to identify text generated by their models. However, its desired properties can conflict (\ie~stronger watermark signals can degrade text quality), while designs that resist editing may also facilitate forgery. Providers address these trade-offs by choosing configurations that balance competing objectives or prioritize particular properties. Either approach imposes a shared operating point on requests with different requirements, potentially sacrificing quality where wording preservation matters or robustness where reliable attribution is essential. To allow flexible and adaptable designs, we introduce \emph{Constitution-Guided Watermarking}, a framework that selects request-appropriate trade-offs from provider requirements, listed as natural-language principles. \emph{Offline}, a pretrained reasoning agent examines constitutional rules alongside watermark implementations and iteratively refines rule-specific configurations using empirical feedback. \emph{At deployment}, a separate monitor identifies applicable rules and retrieves the corresponding policy, including watermarking exemptions, without modifying the serving model. Furthermore, our framework supports offline parallel optimization and refinement of rule-specific configurations based on evolving provider requirements without affecting deployment, and binds each deployed configuration to its evaluation evidence, making deployment decisions auditable. In a proof-of-concept evaluation using KGW and a five-rule constitution, our framework selects configurations responsive to provider priorities and improves post-paraphrase detection on robustness-prioritized requests by up to $14$ percentage points over fixed configurations, while matching or exceeding all baselines in aggregate quality and clean detection at a nominal $0.1\%$ false-positive rate.

---


### 257. [Pretraining Shapes Spectral Structure: Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation Models](https://arxiv.org/abs/2610.09709)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sangyoon Bae, Sk Miraj Ahmed, Shinjae Yoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can we determine whether a foundation model will generalize out-of-distribution (OOD) before any target data is available? Existing diagnostics require source or target data, which rules them out before a target domain exists. Those that use the weights alone apply one statistic to every architecture, and do not separate robust models from fragile ones. We show the answer is encoded in the spectral structure of pretrained weights. Two forces shape that structure. Architecture determines how information is stored in weight matrices. Pretraining strategy determines what is rewarded. Together they set a spectral geometry that governs OOD robustness. We prove that the OOD accuracy gap is bounded by how tightly the source representations concentrate. A statistic computed from the pretrained weights alone serves as a proxy for that concentration. The direction of that proxy reverses between architecture families. We operationalize it: the direction is stable within one (architecture X strategy) combination, the finest grouping we test, which we call a cell. Pooled over 116 models spanning 7 modalities, a single statistic ranks OOD robustness weakly, because cells of opposite direction cancel. Within a cell, the statistic selected for it orders 92% of model pairs by OOD robustness in-sample. The selection does not leak the target: for each model family outside the matrix we logged the cell, metric and sign before running its OOD evaluation, and the predicted direction held in every case: EEG, genomic and protein. Acting on spectral concentration narrows the OOD gap by 24% at 87.5% ID retention. The diagnostic operates on released weights alone, so OOD robustness becomes checkable at model-selection time, before data or compute is committed to a target domain.

---


### 258. [Leaner Transformers Can Easily Learn to Cluster](https://arxiv.org/abs/2610.09760)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Charlotte Park, Kenneth L. Clarkson, Lior Horesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have in-context learning capabilities, where some known learning algorithms can be executed in the forward pass through the model. Recent work shows that transformers can exactly perform Lloyd's algorithm for $k$-means clustering with $n$ points in $d$ dimensions with an embedding size $d_{\textsf{emb}} = d+k$ (thus, requiring attention projection matrices of size $(d+k)^2$). In this work, we build upon this result in the following ways: First, we present an equally expressive but smaller transformer that executes Lloyd's algorithm with embedding size $d_{\textsf{emb}} = (d + \lceil \log_2 k \rceil)$. Next, we train these transformers to learn the clustering algorithms given a distribution of clustering tasks, and theoretically characterize and empirically validate the factors affecting the convergence and in-distribution generalization of learning algorithms based on stochastic gradients. Finally, we probe the general clustering abilities of these learned algorithms (in the form of transformers), and try to understand situations where they succeed and fail.

---


### 259. [DisParQ: Self-Supervised Part Concepts for Interpretable Vision Foundation Models](https://arxiv.org/abs/2610.09802)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adam Pardyl, Siddhartha Gairola, Sukrut Rao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-based vision models represent images through an intermediate layer of human-inspectable concepts, so what a model relies on can be traced to those concepts. However, those models are often limited to fixed categories or depend on language to define their concepts. We introduce DisParQ (Discrete Parts with Quantized attributes), a method that learns spatially grounded, discrete concept representations from a powerful frozen vision-only self-supervised backbone. It requires no class labels and no language supervision. Each image patch is assigned to exactly one concept from a learnable prototype dictionary, and only a sparse subset of concepts may activate per image. To capture how each concept varies across images (e.g., the type of a "wheel"), we learn continuous residuals alongside the concepts and then quantize them into discrete attributes. A spatial decoder reconstructs the backbone's representation from the concepts and attributes alone, so successful reconstruction means that the discrete representation preserves the backbone's information. We evaluate DisParQ across seven datasets, from general recognition (ImageNet, PartImageNet, Places) to fine-grained benchmarks (CUB, Cars, Dogs, Flowers). We show that DisParQ closely matches its frozen DINOv2 teacher on ImageNet linear probing (83.2% top-1), achieves higher concept consistency than language-aligned models, remains competitive on fine-grained recognition, and enables cross-category part-based retrieval.

---


### 260. [A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration](https://arxiv.org/abs/2610.09891)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexandra Coroiu, Andrea Vogt, Viktor Werbilo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-Robot Collaboration (HRC) can facilitate mass customisation in Industry 4.0, with Reinforcement Learning from Human Feedback (RLHF) representing a promising approach for developing safe AI-based robots. Practical challenges remain regarding safety during AI development, human feedback quality, and bidirectional human-robot adaptation. We conducted a scoping review of RLHF in HRC systems, mapping methods that address these challenges. Following PRISMA guidelines, we screened 199 records and included 20 peer-reviewed publications (2020-2025) spanning multiple HRC domains. To our knowledge, this is the first review focused on the bidirectional, closed-loop design of RLHF. Our review found multiple feedback modalities enabling data collection in various feedback formats. Collected data can be integrated at different stages of AI training, resulting in a multi-step development process. Pilot experiments are commonly used to evaluate HRC systems based on both human and robot metrics. To empirically test a key gap identified in the review, we conducted a between-subjects VR experiment comparing system- and user-initiated feedback on robot proxemic behaviour for safe navigation. Using Bayesian models, we analysed the relation between the collected feedback and safety metrics: psychological safety (post-experiment questionnaire) and physical safety (inverse time-to-collision). Results show that user-initiated feedback captures perceived safety better than system-initiated feedback, indicating that feedback timing directly affects feedback quality. Our review and experiment findings show that RLHF relies on appropriate feedback methods to ensure AI safety in HRC, and future RLHF research should prioritise realistic HRC experiments evaluating the effects of feedback collection methods on relevant human and robot metrics.

---


### 261. [WxFM-XL: Adapting Univariate Foundation Models to Multi-Station Weather Forecasting](https://arxiv.org/abs/2610.10057)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiao Wang, Changjian Chen, Zhuo Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rise of univariate time series foundation models (e.g., Sundial, Timer), initial efforts have been made to extend them to multivariate settings. However, these models mainly focus on modeling correlations among variables. When they are applied to multi-station weather forecasting, two important factors are often overlooked: (1) the spatial information of stations, and (2) different error priors of different stations relative to the foundation model. In this paper, we propose WxFM-XL, a model for adapting univariate time series foundation models to multi-station weather forecasting. WxFM-XL introduces a cross-station error correlation prior graph to capture stationwise error priors with respect to the foundation model. Building on this, we further propose a dynamic fusion mechanism that adaptively integrates a spatial correlation graph with the error correlation prior graph. Experiments on multiple datasets demonstrate that our model outperforms state of the art baselines.

---


### 262. [Efficient Provably Private Classification with a Tabular Foundation Model](https://arxiv.org/abs/2610.10068)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Talal Alrawajfeh, Cristiana Diaconu, Ossi Räisä 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data underpin prediction and decision-making in medicine, finance, government and science, but often contain sensitive individual-level information, creating a need for accurate prediction while preserving privacy. Traditional private learning provides formal privacy guarantees, but requires slow dataset-specific optimisation, suffers substantial utility loss under strong privacy, and is often difficult to apply correctly. Tabular foundation models adapt rapidly to new datasets, but existing models lack formal privacy guarantees, and are highly vulnerable to membership-inference attacks, limiting their use on sensitive data. Here we introduce PrivTab, an easy to use tabular foundation model for differentially private classification that embeds a privacy mechanism within its architecture. Pretrained on simulated datasets, PrivTab uses in-context learning to transform sensitive rows into compact, provably private summaries---effectively learning how to learn under privacy. PrivTab outperforms private linear and neural-network baselines under moderate-to-strong privacy, shows negligible membership leakage, maintains well-calibrated predictions under strong privacy, and reduces dataset fitting time by 10,000 times, requiring only a single forward pass. By combining formal privacy, speed, and easy of use, PrivTab brings recent advances in AI to applications where sensitive individual-level data have limited their adoption.

---


### 263. [HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration](https://arxiv.org/abs/2610.10133)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps the capability of the agent system. In this work, we present HarnessIR, an agentic framework for Real-IR by harnessing a multimodal foundation model (MFM) as the executor. HarnessIR consists of five stages: perception and diagnosis, on-demand tool invocation, prompt composition, execution, and verification-driven refinement. Unlike prior agentic Real-IR methods that rely on tool chains assembled from task-specific models, HarnessIR feeds the restoration requirements, the perceptual diagnosis, and the evidence into an MFM that performs restoration in a single pass, followed by verification stages to determine whether the result warrants further processing. Under our harness, off-the-shelf MFMs handle restoration tasks remarkably well, achieving state-of-the-art results on the widely used MiO100 synthetic benchmark. More importantly, by exploiting the strong generalization ability of MFMs, HarnessIR delivers compelling restoration quality on challenging real-world scenes where previous agentic IR systems often struggle. Codes is available at this https URL.

---


### 264. [PatchBench: Measuring Collateral Damage in Activation Patching](https://arxiv.org/abs/2610.10276)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexi Canesse, Mathis Le Bail, Maël Jenny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An LLM safety patch can pass a benchmark while still being a poor repair. This risk is especially acute for jailbreak repairs, where the goal is to correct a specific unsafe behaviour without changing unrelated behaviours. A patch may block exact evaluation prompts yet fail on close harmful variants, or suppress harmful behaviour by over-refusing benign prompts that share its wording or structure. Existing protocols primarily test whether models can be broken, while aggregate metrics (attack success, refusal rates, global capability) cannot distinguish selective repairs from broader local suppression. To address this gap, we introduce PatchBench, a benchmark of empirically observed model-specific jailbreak failures inducing actionable harmful answers. Starting from 27,870 prompts from 37 public datasets, we curate 15,314 English prompts and query 8 open-source instruction-tuned models. Combining WildGuard filtering, pairwise Elo ranking, and manual verification, we retain a curated bank of 400 high-confidence jailbreak failures. We further introduce PatchBench-Local, an evaluation protocol testing whether a patch is behaviourally precise. For each harmful source prompt, PatchBench-Local generates three families of local neighbours: harmful variants preserving malicious intent, benign prompts with matched structure, and benign prompts reusing key harmful terms. It evaluates harmful-neighbour correction and benign-neighbour preservation, distinguishing selective repair from broader local suppression. Evaluating four activation steering methods with PatchBench-Local and MMLU shows that global capability can remain nearly unchanged while local benign regressions are severe, confirming aggregate metrics miss important collateral damage. PatchBench-Local provides a more precise basis for developing and comparing jailbreak repair methods.

---


### 265. [Thinking in Depth: Retrospective Inference for Tabular Foundation Models](https://arxiv.org/abs/2610.10317)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hao-Run Cai, Si-Yang Liu, Zi-Jian Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are pretrained across diverse tabular tasks and make predictions on a new table at inference time using its labeled examples as context. Most recent TFMs perform such in-context prediction with stacked Transformer layers, repeatedly transforming how examples are represented and compared. By tracing individual queries through several strong TFMs, we find that predictive refinement is highly uneven across depth and is often concentrated in later layers. This uneven refinement motivates us to reconsider how intermediate representations are constructed and reused throughout the network. We introduce Retro, a tabular foundation model based on retrospective inference, where later stages can explicitly revisit and recombine intermediate information produced earlier in the network. Retro organizes this process around two complementary operations: which intermediate information to revisit, and how the resulting contextual update should be shaped for each query. Attention Residuals address the former by adaptively reweighting contributions from different depths, while query-conditioned Gated Attention addresses the latter by modulating the attention output element-wise across representation dimensions. Our analysis shows that Retro shifts predictive refinement earlier and more broadly across depth, with different stages revising different subsets of queries in a pattern suggestive of multi-view refinement. Across TabArena, TALENT, and RelArena, Retro ranks among the top three and lies on the Pareto frontier. These results indicate that directly reusing intermediate representations provides a practical way to better exploit depth in TFMs.

---


### 266. [A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning and Teaching](https://arxiv.org/abs/2610.10447)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Randy Ardywibowo, Arnav Dalal, Jiantao Jiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) from outcome rewards suffers from sparse supervision, particularly on difficult, long-horizon tasks where successful trajectories are rare and costly to generate. On-Policy Distillation (OPD) offers an attractive alternative by providing dense token-level supervision from a stronger teacher along the student's own generations. Self-distillation methods further remove the need for a separate teacher model by conditioning the same policy on privileged information to serve as its own teacher. However, privileged conditioning alone does not guarantee that the resulting distillation update improves the student. Indeed, privileged information can lead the teacher to solve tasks through shortcuts unavailable to the student, producing supervision poorly matched to the student's current behavior. Consequently, even a higher-performing teacher can provide guidance that degrades student performance. To address this, we analyze how the choice of privileged teacher affects the student's update. We derive a necessary and sufficient condition for the teacher's local distillation update to be a positive multiple of the student's reward gradient. Our analysis suggests that the teacher should not only perform well on the task, but also provide guidance suited to the student's current capabilities. This characterization motivates a practical teacher-training surrogate that combines outcome rewards with token-level Kullback-Leibler (KL) regularization toward the student. Based on this result, we propose Joint On-Policy Learning and Teaching (JOLT), which jointly trains a single policy in two roles: a privileged teacher using a KL-regularized objective, and an unprivileged student using dense on-policy distillation. Across mathematical reasoning, coding, tool use, and terminal use, JOLT improves training efficiency and performance, with further gains from student rewards.

---


> [!TIP]
> 当前位于：**251-266**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-266**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
