# 🧠 大模型相关研究 | 2026年08月25日

> 本类共 **170** 篇论文：已确认 **154** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-170**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-170**

---

### 151. [Move by Move: Measuring and Steering How LLMs Conduct Psychotherapy](https://arxiv.org/abs/2608.21325)

**<font color=#1a73e8>作者：</font>** Afonso Baldo, Hugo Pitorro, Areti Vassilopoulos 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users increasingly turn to large language models for emotional support, yet little is known about how these models actually conduct a psychotherapy interaction. We introduce an ontology of ten therapeutic moves: compact, function-based categories grounded in the MULTI-60 inventory, validated through an annotation campaign with five licensed psychologists, and scaled with a judge-based approach that matches expert agreement. Applying it to real counseling transcripts and model-led sessions, we compare the move distributions between human clinicians and a panel of frontier models. Models over-use inquiry at up to three times the human rate, neglect psychoeducation, and are strongly context-anchored: they carry forward strategies initiated by a human clinician but rarely initiate them themselves. Exposing the ontology as a set of tools roughly halves the mean deviation from the human move distribution and improves turn-level alignment with human therapist by 7-9 percentage points, without any fine-tuning.

---


### 152. [Asymmetric Capacity Allocation in Self-Refinement Pipelines](https://arxiv.org/abs/2608.21345)

**<font color=#1a73e8>作者：</font>** Zhuoyi Yang, Ian G. Harris, Salar Hashemitaheri 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-refinement, typically structured as generation, critique, and revision, is a widely adopted paradigm for improving LLM generation and serves as a core mechanism in many LLM agents. While the three stages involve different cognitive demands, most existing approaches conveniently treat the model size as an implementation detail rather than a subject of study, which may lead to a waste of resources. Little work has systematically examined how model size affects each stage or whether effective self-refinement requires equally capable models for generation, critique, and revision. We present the first stage-wise model size study of the self-refinement pipeline on 5 benchmarks from different domains using 6 model sizes of Qwen3 and 4 model sizes of Gemma 3. We conclude that larger generators and refiners generally improve the pipeline, whereas an undersized refiner can even harm performance. Second, performance is highly insensitive to the size of the critic, although including even a small critic consistently outperforms omitting critique altogether. Our findings demonstrate that model capacity should not be allocated uniformly across self-refinement pipelines. Instead, different stages exhibit distinct size scaling characteristics, providing practical guidance for designing more computationally efficient multi-stage language model systems.

---


### 153. [VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences](https://arxiv.org/abs/2608.21357)

**<font color=#1a73e8>作者：</font>** Elaine Lau, Thanuka Udumulla, Lee Izhaki-Tavor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In professional life sciences workflows, scientists routinely interpret visual artifacts (gel blots, microscopy images, plasmid maps, flow cytometry plots, molecular structures, ...) to inform research decisions. We introduce VIALS, a visual question-answering benchmark with 161 such interpretation tasks, spanning the types of artifacts examined throughout experimental workflows in the biotech industry (rather than polished figures from publications and textbooks). While frontier vision-language models can now fluently describe natural images, we find that they are unable to accurately interpret these scientific images, reflecting limitations in domain knowledge and domain-specific visual reasoning capabilities. In contrast, scientists with relevant domain expertise find these visual interpretation tasks straightforward. AI that cannot similarly interpret such images will have limited utility in professional life sciences workflows, where such artifacts are central to how scientists reason, communicate, and make decisions.

---


### 154. [OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs](https://arxiv.org/abs/2608.21360)

**<font color=#1a73e8>作者：</font>** Xianyun Sun, Chaoyou Fu, Zhengye Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent omni-modal large language models (Omni-LLMs) show great potential as real-time video assistants, which continuously perceive environments and guide users to achieve specific goals. Unlike traditional passive video understanding, interactive assistants should actively combine visual states, user goals, and prior knowledge to provide effective help. Evaluating this is rather challenging, as the model's unpredictable response dynamically changes the user's subsequent actions, which static offline datasets cannot accommodate. To address this bottleneck, we introduce OmniAssistBench. To solve the issue of diverging interaction paths where the same user goal can be achieved through various methods, we provide models with predefined priors derived from the source video, requiring them to guide users along the exact same routes. Since real interaction videos are rare, we construct the dataset by reverse-engineering existing Internet videos. We deduce logical user goals and segment the videos into multi-turn clips to simulate continuous interactions. This rigorous pipeline required over 1000 expert person-hours to build the dataset. Results show that the proprietary Gemini-3-Pro reaches 66.4 out of the max point of 100, while the open-source Qwen3-Omni-Instruct achieves 51.2. Although current models generally understand user inputs, they frequently provide incorrect or incomplete answers. Specifically, they struggle with visual prompts (e.g., hand gestures), fail to maintain historical context during multi-turn interactions, and fail to delay response until the target event. Results indicate substantial room for improvement before models can become reliable assistants.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 155. [Who Delegates to AI? Evidence from 53,000 Agent Configurations](https://arxiv.org/abs/2608.20425)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hyeongjae Lee, Jihyang Cheon, Lanu Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A growing literature measures how far occupations are exposed to AI, but these measures capture where AI could perform tasks, not whether workers have adopted it. We propose a new layer of exposure, delegated exposure, which records whether a worker has committed a task to AI by building it into a workflow. We operationalize it as the Agentic Adoption Index (AAI), which measures how closely an occupation's tasks match the agentic routines practitioners have already built and shared. We embed roughly 53,000 agent skill specifications from the Manus Skills Marketplace, compute their semantic similarity to about 18,000 O*NET task statements, and aggregate to the occupation level. Three findings follow. First, the occupations where delegation concentrates differ sharply from those pre-AI frameworks identified as most at risk. Second, the AAI tracks what AI could do more closely than what workers currently use it for. Third, the AAI peaks below the top of the wage distribution and at the bachelor's level, declining at both extremes. Technical availability explains most of this variation, but not the shortfall among the most educated occupations, so feasibility alone cannot account for who adopts. That shortfall may reflect work that resists advance specification, or professional discretion over the pace of codification. Distinguishing the two, and tracking how these measures diverge over time, will require repeated measurement.

---


### 156. [Difficulty-Aware Semantic-ID Optimization for Generative Recommendation](https://arxiv.org/abs/2608.20611)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xin Yu, Stephen Li, Sina Aghaei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic-ID-based generative recommendation casts retrieval and ranking as autoregressive generation over hierarchical item identifiers. A common recipe is SFT followed by GRPO, yet vanilla GRPO is poorly matched to this tree-structured task. Under the frozen SFT checkpoint, the exact target is absent from the first 16 candidates of the 50-beam constrained ranking for many prompts, and in harder cases none of these candidates enters the target SID branch. This prompt-level diagnostic motivates a training concern: when on-policy GRPO groups are similarly target-missing, item-level rewards may produce weak or degenerate reward variation even if some candidates follow part of the target path. We propose Difficulty-Aware Semantic-ID Optimization (DASO), a tree-aware post-training method that addresses this failure mode as an online rollout-allocation problem. Instead of using fixed difficulty buckets or uniformly injecting ground-truth completions, DASO profiles each current rollout group by prefix-match depth, locates the bottleneck SID levels where candidates leave the target path, and reallocates a bounded portion of the group to prefix-guided completions while retaining raw rollouts for contrast. A SID-prefix reward provides graded credit, while an auxiliary SFT anchor mitigates regression on examples already solved by the SFT checkpoint. On the public benchmarks, DASO improves over MiniOneRec-style GRPO on 11 of 12 metrics and achieves the best result on 9 of 12 metrics; it also improves most level-wise recall metrics on the internal recommendation task.

---


### 157. [MV2GF: Multi-view Pedestrian Detection with a Visual Geometric Foundation Model](https://arxiv.org/abs/2608.20639)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taiga Yamane, Satoshi Suzuki, Ryo Masumura 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-View Pedestrian Detection (MVPD) aims to detect pedestrians in the form of a bird's eye view map from multi-view images. Recent MVPD methods adopt a unified framework that projects 2D image features into a 3D world space and aggregates them into a single feature. Although they are effective, they struggle to generalize to unseen camera configurations during training due to two main issues. First, they are difficult to capture accurate visual geometry across views in unseen camera configurations. Second, they make detection models highly dependent on distortion patterns during training arising from their image feature projection. To address these, we leverage a visual geometric foundation model and propose MV2GF. This foundation model has exhibited strong generalization in capturing visual geometry across views and predicting accurate 3D attributes in diverse camera configurations. MV2GF fuses task-specific features with general-purpose geometric features extracted by the foundation model to effectively capture the visual geometry even in unseen camera configurations. Furthermore, MV2GF projects each pixel in the image features to an appropriate 3D location using 3D pointmaps predicted by the foundation model, preventing the detection model from depending on distortion patterns during training. Our experiments demonstrate the effectiveness of leveraging a visual geometric foundation model for MVPD and that MV2GF generalizes better than existing methods.

---


### 158. [Lift, Associate, and Fuse: A Decision-Centric Framework for 2D-to-3D Foundation Model Transfer](https://arxiv.org/abs/2608.20659)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wentao Sun, Yiping Chen, John S. Zelek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methods that transfer predictions from two-dimensional foundation models into three-dimensional segmentation are commonly grouped by task or representation. Those groupings obscure the decisions that determine whether a system remains coherent across views: where image evidence is grounded, when observations become one identity, how semantic and granularity conflicts are handled, which information is fused, and what state survives for later queries. We introduce \textbf{Lift, Associate, and Fuse (LAF)}, a decision-centric framework that represents a transfer system as five operators: \textbf{Generate, Associate, Reconcile, Fuse, and Persist/Query}. LAF defines an explicit contract for the persistent carrier---its spatial support, semantic state, identity state, uncertainty, provenance, and supported operations---and identifies the first stage at which discarded evidence becomes unrecoverable. We operationalize the framework as a structured audit protocol and apply it to 161 systems available through 7 August 2026, spanning point-, field-, Gaussian-, object-, graph-, and memory-based carriers. Representation, temporal, relational, and feed-forward stress tests required no additional analytical stage after the final confirmation pass. The resulting decision traces expose four recurring properties: association does not establish identity; carrier design fixes both the query interface and correction boundary; rendered-view, native-3D, and proposal-level evaluations are not interchangeable; and qualifiers such as \emph{training-free}, \emph{real-time}, \emph{open-vocabulary}, and \emph{generalizable} are meaningful only when attached to a stage and a complete cost ledger. LAF therefore supplies a representation-neutral method for comparing existing systems, diagnosing irreversible failures, and specifying revisable 3D perception for future agents.

---


### 159. [DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents](https://arxiv.org/abs/2608.20664)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sarthak Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> DreamBench-SWE is a multi-session benchmark for software-agent memory hygiene in which later software tasks depend on non-inferable evidence from earlier sessions and are scored by executable hidden oracles. We report the original scaled v2 fold and a separately preregistered v2.1 successor audit designed after that study but frozen before successor outcome inspection. The successor run completed 360/360 work units and 720/720 S3 cells across four conditions. In the original fold, the primary DF-hybrid--B5 contrast was null (95/180 versus 89/180; clustered p=.518, Holm p=1), not evidence of equivalence, and C9/C10 retained B0-headroom limitations. In the successor, no external memory achieved 21/180 passes (rate 0.1167), deterministic verbatim event memory 82/180 (rate 0.4556), the typed-plus-raw reference probe 83/180 (rate 0.4611), and one pinned hosted Mem0 literal-storage configuration 97/180 (rate 0.5389). The registered six-slot Family A retained unavailable slots at p=1; all three available comparisons against no memory rejected after Holm correction. Both preregistered mechanism contrasts were unavailable after pre-evaluation conformance rejection. The secondary literal-storage-versus-verbatim comparison was nonconfirmatory and sensitivity-dependent, while the comparison with the reference probe did not reject. The audit therefore supports DreamBench-SWE as a discriminating executable profile benchmark and characterizes one exact hosted-memory configuration, but it does not establish an external-system mechanism, superiority among memory-bearing conditions, equivalence, or broad product generality. The original v2.0.5 findings and artifacts remain unchanged.

---


### 160. [CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting](https://arxiv.org/abs/2608.20771)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zixi Zhu, Jiayuan Su, Jian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search Agents face a severe reliability crisis during reinforcement learning (RL) fine-tuning. Heuristic Top-K retrieval often causes critical evidence loss or noise inclusion, while over-confidence induced by progressive RL leads to hallucinated answers and redundant searches.
To build highly reliable agents, we introduce Conformal Prediction (CP) and propose Conformalized Agentic Search (CAS). This framework establishes reliability guarantees on both the retrieval and training sides: on the retrieval side, an Adaptive Prediction Set (APS), a specific CP realization, translates statistical coverage into dynamic document truncation to construct prediction sets that are adaptive in size; on the training side, Adaptive Conformal Inference (ACI), a dynamic CP algorithm, dynamically constructs prediction sets with controllable coverage to quantify answer confidence, which is then used to penalize low-confidence trajectories within the Group Relative Policy Optimization (GRPO) objective, ensuring the model learns only from reliable ones.
Experiments across single-hop and multi-hop QA datasets demonstrate that our framework significantly improves reasoning accuracy while drastically reducing redundant tool invocations, establishing a highly reliable and efficient agent paradigm. Our code is available at this https URL.

---


### 161. [Foundation Models for Partial Causal Identification](https://arxiv.org/abs/2608.20841)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexis Bellot, Anish Dhir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates the development of causal foundation models for bounding the effect of interventions and counterfactuals from observational data. We show that a canonical prior can be defined with full support over the space of structural causal models with discrete observables. With this canonical prior, we translate the problem of bounding counterfactuals into that of learning distributions over functions that map data (and possibly structural assumptions) to a causal query of interest. This extends the promising causal foundational modelling paradigm to the estimation of partially-identifiable causal effects, i.e., under unobserved confounding, where multiple values are equally compatible with the observed data and prior structural assumptions.

---


### 162. [EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking](https://arxiv.org/abs/2608.20886)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Enjun Du, Siyi Liu, Zirong Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image search queries are multimodal and compositional: ``find this shirt in pink'' specifies an entity to retain, an attribute to modify, and context to ignore. Yet existing re-rankers either compress such multifaceted relevance into an opaque embedding or rely on free-form chain-of-thought that easily omits or hallucinates fine-grained constraints. Drawing on rubric- and checklist-based evaluation from NLP, we recast multimodal image re-ranking as a semantic constraint satisfaction problem and propose EviRank, which parses any query - text-only, image-only, or composed - into a unified evidence package: typed criteria across six semantic slots (e.g., entities, attributes, relations), each labelled required, forbidden, or ignorable. Re-ranking then reduces to evidence-conditioned verification, combining deterministic rubric scoring and evidence-grounded listwise comparison in a single training-free procedure. The explicit evidence can further serve as structured supervision for optionally distilling a lightweight student. Across five benchmarks spanning text-to-image, image-to-image, and composed image retrieval, EviRank achieves state-of-the-art performance, and the distilled student preserves over 90% of the teacher's capability at substantially lower cost.

---


### 163. [Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models](https://arxiv.org/abs/2608.20916)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qifeng Zhang, Ting Xiang, Zeyuan Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) offer strong generalization capabilities for domain-adaptive object detection (DAOD). However, existing VFM-based methods overlook the spatial-scale discrepancy between teacher and student feature maps, resulting in semantic incompatibility that weakens both feature alignment and pseudo-label learning. Moreover, domain shift can cause source-trained VFM teachers to miss target-domain objects, limiting the quality of their pseudo-labels. To address these issues, we propose the Semantic Localization-Enhanced Teacher (SLE-T), a semantically compatible knowledge-distillation framework built around a lightweight SLE Adapter for DINOv2. SLE Adapter injects pretrained local-texture priors into DINOv2 to improve cross-domain recognition and reformulates its features into dense representations that are spatially and semantically compatible with the student detector. SLE-T transfers the resulting teacher knowledge through either pseudo-label learning or feature alignment. We instantiate SLE-T with DINOv2-B and DINOv2-L (the ViT-B and ViT-L variants) and compare them with the larger DINOv2-G teacher. Extensive experiments on three DAOD benchmarks demonstrate that our method achieves state-of-the-art performance, and ablation studies confirm the importance of teacher-student semantic compatibility. Notably, SLE-T with DINOv2-B produces competitive or superior pseudo-labels using approximately one-quarter of the training time of DINOv2-G and substantially less GPU memory, demonstrating efficient VFM knowledge transfer under limited computational resources.

---


### 164. [MentorPulse: Refreshing Cross-Model Latent Guidance for Long-Form Generation](https://arxiv.org/abs/2608.20927)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziwu Liu, Guozhong Li, Chen Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-model latent guidance lets a frozen large mentor encode an input once and a frozen small student generate from the resulting signal. Existing methods keep this signal fixed, assuming it stays useful as the output grows; we show this fails in long-form generation. On multi-turn instruction following, static guidance pushes a 4B student's constraint satisfaction 2.5 points below its no-guidance baseline; a training-free refresh every 16 tokens changes only the memory content and restores a 2.0-point gain over that baseline. We propose MentorPulse to keep guidance fresh at practical cost: it compresses mentor states into a capped slot memory, incrementally processes newly generated tokens, and updates the memory that the student reads through gated cross-attention without resetting the student's KV cache. Windowed Refresh Training exposes the bridge to prefix-conditioned memory. Across thirteen datasets, MentorPulse closes 52.2% of the mentor-student gap on macro average, outperforming C2C, T2T, and equal-budget LoRA, with the largest gains on long outputs. It performs best on all eleven mentor-student pairs from three model families, with margins that narrow as the capability gap grows, and a lightweight read-pattern check predicts the gain before deployment. Measured costs identify refresh intervals that dominate text guidance on long outputs.

---


### 165. [TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming](https://arxiv.org/abs/2608.20958)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yibo Hu, Yu Qian, Mao Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios. It maps image, video, audio, and text inputs into a unified representation space. For long-form live streaming analysis, we introduce Per-vGrid, a timestamped token organization that groups each video grid with its temporally corresponding audio within explicit boundary tokens to facilitate temporal alignment. We design a three-stage supervised training recipe that progressively develops live-commerce understanding, from omni-modal perception to instruction-following responses. We then propose Faithful-RFT, a reinforcement fine-tuning stage that further improves answer faithfulness and expression quality while meeting real-time demands, scoring final responses directly with task-verifiable feedback rather than optimizing for reasoning-style exploration during rollout. Moreover, TLive-Omni is supported by a scenario-oriented atomic capability taxonomy and a compact data production engine that converts live-commerce audio, image, and video streams into training signals for speech recognition, speaker analysis, product visual grounding, text recognition, temporal grounding, video dense caption, and omni-modal QA, etc. For scalable training, a synchronized length-grouped sampler reduces padding while preserving comparable workloads across workers, while a lightweight dynamic sampling strategy regenerates rollout groups with near-zero reward variance to maintain meaningful relative advantages for GRPO. Experiments on e-commerce live streaming benchmarks demonstrate strong performance across live-commerce domain tasks, together with excellent generalization on general benchmarks.

---


### 166. [Trojaning the Alignment: Stealthy Backdoor Attacks against Graph Foundation Models](https://arxiv.org/abs/2608.20991)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minhua Lin, Zhicheng Gao, Yilong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Foundation Models (GFMs) on text-attributed graphs (TAGs) align graph representations with language semantics to support transferable graph learning. Despite these advantages, the backdoor vulnerability of GFMs on TAGs remains insufficiently understood, especially under graph-language alignment, where graph and text representations are trained to constrain each other in a shared semantic space. Existing backdoor attacks mainly target either the graph side or the text side, treating the two modalities independently. This makes direct adaptation ineffective: graph-only triggers can be constrained by clean text semantics, while text-only triggers alter the language view but do not directly shift the graph representation being aligned and scored. TAGs also impose a stealth challenge because triggers are exposed as both node text and local graph structure, making incoherent trigger attributes or anomalous subgraphs easy to inspect or filter. In this paper, we propose STAG, a stealthy trojan attack framework designed for the graph-language alignment interface of GFMs on TAGs. STAG coordinates a graph-trigger generator with a text-side soft prompt so that trigger-attached graph representations and triggered text representations move toward the same target-class text region. To address TAG-specific stealthiness, STAG realizes trigger nodes as readable text through candidate retrieval and regularizes the trigger-attached subgraph so that its local structure remains close to the original subgraph. Extensive experiments on multiple TAG datasets and representative GFMs demonstrate the effectiveness and stealthiness of STAG. Our code is available at this https URL.

---


### 167. [CellPath-Bench: A Multidimensional Benchmark for Whole-Slide Cellular Representations in Pathology Foundation Models](https://arxiv.org/abs/2608.21060)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bokai Zhao, Yiyang Zhang, Hanqing Chao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) are increasingly used as general-purpose backbones, yet existing benchmarks cannot systematically diagnose their whole-slide cellular representation capabilities, including the decodability of cell-type information and the transferability of such information across tissue sections, datasets, and anatomical organs. We introduce CellPath-Bench, a cellular-resolution benchmark that evaluates frozen PFMs themselves. Following quality control of 52 candidate Xenium datasets, we construct a panel of 25 spatially aligned H\&E--Xenium tissue sections spanning 11 organs and 7,079,283 cells, harmonized into fine- and coarse-grained taxonomies. CellPath-Bench samples frozen WSI feature maps at registered nuclear coordinates and evaluates them using standardized multiclass linear probes. Cell Representation Advantage (CRA) measures the within-section advantage of nucleus-anchored representations over patch-level mean pooling, while Cell Representation Transferability (CRT) characterizes the generalization of cell-type decodability across tissue sections, datasets, and organs. We benchmark 30 pathology-specific and general-purpose foundation models through 304,920 runs across spatial readouts, magnifications, taxonomic granularities, and evaluation protocols. The results reveal substantial model-dependent differences in cell-type decodability and its cross-domain generalization, yielding distinct multidimensional capability profiles. CellPath-Bench provides a standardized framework for auditing cellular information in frozen PFM representations.

---


### 168. [Tydra: An Efficient Hybrid Model for Tabular Data](https://arxiv.org/abs/2608.21199)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based tabular foundation models such as TabPFN achieve strong predictive performance but incur quadratic computational cost with context length. On the other hand, subquadratic SSM-based alternatives such as Hydra trade away accuracy for efficiency. To balance both, we introduce Tydra, a hybrid Transformer-State Space Model (SSM) architecture for tabular in-context learning that interleaves attention and SSM layers. Across 30 OpenML datasets, Tydra reduces inference time by 30% relative to TabPFN while retaining much of its predictive performance. Tydra also outperforms an approximately ten-times-larger Hydra model while providing faster inference. The results indicate that hybrid architectures are a promising direction for tabular foundation models.

---


### 169. [Anchoring Instruction Outside Mask: Exact Reference Caching for Efficient In-Context Diffusion Transformers](https://arxiv.org/abs/2608.21229)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yangshuai Liu, Zheming Li, Jiaao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal generation is central to a wide range of content creation and editing applications. In-context conditioning is essential to this paradigm. It allows diffusion transformers to process text instructions and visual references in a shared attention sequence. However, each reference image introduces thousands of tokens. Computation therefore grows rapidly with the number of references. Existing methods reduce computation through structured sparse attention, which limits interactions between reference and target tokens. This structure also makes the reference K and V independent of the denoising target, allowing them to be computed once and reused across steps. However, it blocks visual references from attending to the text instruction. This substantially degrades instruction following and reference fidelity in multi-reference editing. To resolve this conflict, we jointly redesign the token sequence and attention mask. Our beyond-mask design uses static text anchors to connect the instruction to the reference branch. It preserves exact K and V reuse without adding parameters. However, this direct architectural conversion degrades generation quality. We recover the lost performance through teacher-forced velocity distillation, followed by a short on-policy stage in which the teacher supervises student-visited states. To our knowledge, this is the first use of on-policy distillation for architectural recovery in diffusion models. Across three image-editing benchmarks, our method matches full-attention generation quality. With five reference images, it accelerates the complete 40-step denoising process by 3.92x, while static text anchors introduce negligible runtime overhead; the speedup reaches 5.47x at ten references in our scaling study.

---


### 170. [Prompt-Model Interaction Reaches the Fixed Points: A deterministic, task-free structural readout -- and the factorizations of it that failed](https://arxiv.org/abs/2608.21315)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> That a prompt's effect is not a property of the prompt is established: prompts optimised for one model degrade on another, and rankings reorder under neutral reformatting. That evidence is about task accuracy, which cannot say whether the interaction is a fact about task machinery or about the conditional distribution itself. We ask on a readout with no task in it: the fixed-point structure of the short-window argmax map x_{t+1} = argmax_x p(x | x_{t-1}, x_t), censused from 96 starts. It is deterministic, so nothing can be helped or hurt, and it exists only at short windows -- four of six models lose it entirely by window 16 -- so everything here concerns how a model reads a fragment. Two results. First, the interaction reaches this readout at full magnitude: nine tokens of conditioning move the fixed-point fraction across most of its range, change a four-way structural class, and reorder models, while instruction tuning worth 60.5 IFEval points moves the class by zero. Second, nothing we proposed carries it. Prefix length fails: the effect is not monotone. Four phenomenological factors -- prose-versus-markup, a universal direction, bidirectionality, instruct-resistance -- were each withdrawn within one run of being proposed, dissolved by widening the sample. And the nearest mechanistic account, attention-sink dominance of early tokens, predicts the sign of the shift on 2 of 5 models -- chance -- while a length-by-content cross shows it holds on real text and fails on our probe's uniformly random input, so we are outside its regime, not against it. One fixed nine-token prefix drives four models toward 0 and two toward 1; the bidirectionality survives in-distribution starts. On this readout the unit of explanation is the prompt-model pair. The recurring error it caught in us has a name: a criterion with a shape applied to a quantity with no room to vary.

---


> [!TIP]
> 当前位于：**151-170**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-170**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
