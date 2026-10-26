# 🧠 大模型相关研究 | 2026年10月27日

> 本类共 **204** 篇论文：已确认 **185** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

---

### 151. [IGG: A Benchmark for Interactive GUI Grounding under Visibility Constraints](https://arxiv.org/abs/2610.32536)

**<font color=#1a73e8>作者：</font>** Kyeongseon Kim, Jiyeon Son, Tae-Hyun Oh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI grounding benchmarks ask whether an agent can localize a target that is already visible in a static screenshot. Real interfaces often violate this assumption: a target may be off-screen, appear only after a state change or hover, remain occluded, or become actionable after a delay. This leaves the ability to recover target visibility unevaluated. To measure this reveal step, we introduce Interactive GUI Grounding (IGG), a benchmark in which an agent must first make the target visible through interaction and then click it. IGG contains 601 tasks across 16 controllable GUI environments and seven visibility-constraint sub-types, with a compact action space of scrolling, moving, dragging, waiting, and clicking. In our human study, participants achieve 94.6% accuracy, while GPT-5.5 reaches 79.4% and the strongest evaluated open-source VLM reaches only 31.6%. To identify the source of this gap, we conduct two controlled interventions. Telling Qwen3-VL which interaction to perform raises its accuracy only from 30.8% to 33.9%, whereas performing the interaction for the model raises it to 81.9%. The bottleneck is executing the reveal interaction, not recognizing the target once it is exposed. We further show that this capability is learnable, demonstrating that visibility recovery can be strengthened consistently across model families.

---


### 152. [PHYRD: A Living Benchmark for Reproducing and Extending Theoretical Physics Research](https://arxiv.org/abs/2610.32575)

**<font color=#1a73e8>作者：</font>** Qituan Zhang, Guo Chen, Linfeng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models and agents have shown significant power in advanced physical research. In this paper, We introduce PHYRD, a living benchmark for theoretical-physics reasoning with 63 Reproduce and 43 Discover problems. Reproduce tests derivation of published results; Discover tests consequences of modified theoretical conditions. FormulaForest constructs the tasks with reference solutions and subquestion-level rubrics. Across five models, whole-problem accuracy ranges from 49.21% to 68.25% on Reproduce and from 18.60% to 74.42% on closed-book Discover. With tools, four models complete more Discover problems, but conceptual errors and missing arguments persist. Besides, our experimental results demonstrate the value of FormulaForest as synthetic data. On FrontierScience, a benchmark developed by OpenAI, it raises the accuracy of a Qwen-35B-A3B model from 61% to 72%.

---


### 153. [From Parameter Rebasin to Functional Transfer Across Heterogeneous Transformers](https://arxiv.org/abs/2610.32581)

**<font color=#1a73e8>作者：</font>** Filippo Rinaldi, Aniello Panariello, Giacomo Salici 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pretrained Transformers to downstream tasks produces task-specific updates that are expensive to reproduce for every model variant. Reusing these updates across different depths and widths is challenging because their parameters have incompatible shapes and do not share a canonical coordinate system. We introduce Ariadne, a training-free method that transfers task-specific behavior across heterogeneous Transformers without resizing the source model or transporting its parameters. Rather than treating the source task vector, i.e. the difference in parameter space between the fine-tuned and the base models, as the object to move, Ariadne characterizes fine-tuning by the activation changes it induces at matched blocks. First, it aligns these effects to a target base through local Procrustes maps. Then, it directly synthesizes a native target update by closed-form ridge regression. Across Transformer expansion, reduction and language-model transfer, Ariadne improves target-model performance while substantially reducing the time and memory required to construct an update relative to previous cross-architecture rebasin approaches. These results show that local functional effects provide an efficient alternative to parameter transport.

---


### 154. [Political sense-making in "individual" human-technology-world relations: the case of LLM-generated autobiographies](https://arxiv.org/abs/2610.32594)

**<font color=#1a73e8>作者：</font>** Anthony Longo, Olya Kudina  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI systems increasingly mediate how people describe, recognize, and present themselves, their politics cannot be reduced to what remains hidden inside the "black box." This chapter argues that AI's political significance emerges within technologically, intersubjectively, and temporally mediated interpretive practices. Bringing Arendt's political philosophy into conversation with Gadamerian hermeneutics, the chapter develops a postphenomenological relational-temporal account of political sense-making across Human-Technology-World relations. Against the charge that postphenomenology remains individualistic and using the case of LLM-generated biographies, the chapter shows how seemingly private human-LLM encounters are worldly and collective. When users ask systems such as ChatGPT to describe them, they do not simply receive algorithmic representations. They interpret, contest, edit, share, and publicly test these descriptions. In doing so, people move interpretively among affective resonance, friction, public re-articulation, and the sedimentation of meaning. This means that the so-called "micro-level" of postphenomenological analysis is already saturated with publicity: affective uptake becomes communicable, reflection becomes accountable, and uses sediment into shared standards of appearance. Simultaneously, we show that once mediation is treated as relational and temporal, the political is not an add-on at the "macro" level; it is intrinsic to the very movement through which technologies amplify and reduce, stabilize and unsettle, and thereby compose a shared world in which judgment can take place. The chapter finishes by discussing several design and policy implications for AI of such political foregrounding in postphenomenology.

---


### 155. [LLaCO: Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling](https://arxiv.org/abs/2610.32604)

**<font color=#1a73e8>作者：</font>** Zijian Jia, Peixuan Zhang, Genying Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion models have emerged as a promising non-autoregressive paradigm for text generation over continuous embedding spaces. Along the continuous trajectory, the residual token identity directly shapes the denoising objective. However, the geometric trajectory misaligns with temporal progression, triggering severe temporal compression. In this paper, we show that embedding norm decay causes Euclidean distance to yield spurious overtaking, indicating that token competition must be evaluated directionally. In this space, a candidate overtakes the source token only when the effective noise magnitude surpasses their semantic separation. We formalize these pairwise dynamics as the Competition Threshold Theory (CTT). Crucially, high-dimensional overtaking requires extreme noise levels, causing standard trajectories to concentrate identity decay into a narrow window near the noisy endpoint. To resolve this, we propose Semantic Retention Scheduling (SRS) to align time allocation with the progression of identity decay, and demonstrate that existing token identity metrics are fundamentally statistical aggregations of these pairwise crossings. Building on these theoretical insights, we introduce LLaCO, a generative framework powered by competition-aware semantic scheduling. LLaCO adapts a pretrained backbone to continuous representations via an embedding directional adapter and timestep-conditioned modulation. To operate within the directional space, LLaCO employs a spherical noising process formulated as a geodesic interpolation toward a mask-biased endpoint, eliminating norm decay while preserving accurate token competition. Guided by SRS, LLaCO reallocates the denoising trajectory proportionally to the logarithmic rank decay. Instantiated as an 8B model, LLaCO outperforms previous continuous diffusion baselines and rivals discrete diffusion models of comparable scale.

---


### 156. [What Transfers Across Protein Pockets? Experience Reuse in Molecular Optimization for Agentic Structure-Based Drug Design](https://arxiv.org/abs/2610.32620)

**<font color=#1a73e8>作者：</font>** Zaifei Yang, Weiyu Chen, Yaqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents optimize a ligand in a protein pocket by editing it step by step and docking each edit. Recent agents first spend extra dockings probing the complex with controlled edits; guidance induced from these probes is reported to help more than the chemical knowledge the model already carries. The probes are then discarded with the instance that produced them, so the obvious next step is to keep them in an experience base, letting a new pocket inherit what earlier ones already paid for. Such a base is read through a \emph{key}: the record properties under which past edits are pooled and a new one is looked up. Using the full log of one such run over the CrossDocked2020 test-set pockets, we ask whether its keys recur on a pocket the base has never seen and still separate improving from worsening edits. \crchange{Using} the contacts at the site being edited, the action, and the round as \crchange{a} key, the base separates them sharply. Within our analysis, this separation is largely explained by how much the edit changed the molecule's size, the action, and the round, none of which describes the target. That is not because the target is irrelevant: naming it outright separates them several times more sharply. For a pocket absent from the base, transfer must rely on a description rather than its identity. Among the exact-match descriptions we evaluate, the more specific ones rarely recur, whereas the coarser ones provide little separation; the signals that do transfer primarily describe the edit and the molecule it produced rather than the target. Under the representations and lookup scheme studied here, an experience base may be more useful for prioritizing an agent's own proposals for docking than for directly prescribing what to build.

---


### 157. [LGMT: A Tool for Testing the Logical Reasoning Reliability of LLMs](https://arxiv.org/abs/2610.32627)

**<font color=#1a73e8>作者：</font>** Zenghui Zhou, Xiaoke Fang, Zheng Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly serve as reasoning components in modern software systems, yet a model that answers a logical query correctly can contradict itself when the same problem is restated in an equivalent form. Static benchmarks evaluate queries in isolation and therefore fail to expose such inconsistencies. To address this limitation, we present LGMT, an open-source tool that detects reasoning inconsistencies through metamorphic relations grounded in first-order logic. Given a source test case in premise-conclusion form, LGMT generates logically equivalent follow-up cases and checks whether the model's entailment predictions agree across the pair, without ground-truth labels. The tool provides 20 built-in metamorphic relations, supports custom ones verified by the Z3 theorem prover, and runs from a CLI or a web studio, including an offline mock mode requiring no API key. Across six widely used LLMs on a bundled benchmark of 3,091 metamorphic groups, LGMT reveals inconsistency rates ranging from 20.84% to 29.44%. LGMT is publicly available on GitHub at this https URL, with a demonstration video at this https URL.

---


### 158. [The Answer Knows Where to Look: Zooming before MLLMs Answer under Visual-Token Budgets](https://arxiv.org/abs/2610.32664)

**<font color=#1a73e8>作者：</font>** Zhensheng Hu, Guanglong Xu, Guanqiang Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) read images through visual tokens, and under the small per-image budgets that efficient deployment requires, the fine text of documents, charts and infographics becomes illegible. Zooming in recovers the evidence, but the region must be chosen before the model answers. We find that MLLMs know where the evidence is, but not in a form that can be read before they answer: the answer tokens localize it from the middle layers on, whereas the attention available before answering does so only in the top layers, at a depth that varies across models, and diffusely. Supervising the pre-answer attention to point degrades reading, and the benefit of zooming is governed by each image's information gap. Building on these findings, we introduce ours, which lets an MLLM look where its answer would. A dedicated look token, processed in a single prefill and kept out of the answering pass, learns in hindsight to attend as the model's own correct answers do, extracting this knowledge into a concentrated pointer before any answer exists. Its hidden state then selects how to look, from no zoom to crops, square windows, windows that adapt to the pointer and foveated warps, supervised by the counterfactual outcome of every view. ours needs no box annotations, per-model layer search, external localizers or generation before the answer. On Qwen3-VL at three scales and five text-rich benchmarks, it surpasses the strongest baseline by 4.8-9.1 points at 98 visual tokens per view and attention-guided zooming by 11.1-17.0 points, while running faster than attention-guided and grounding-based zooming.

---


### 159. [Do Language Models Trust Their Own Justifications? A Study on Functional Consistency](https://arxiv.org/abs/2610.32665)

**<font color=#1a73e8>作者：</font>** Alisson Rosa Pereira, Bruno Iochins Grisci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been widely adopted in text classification tasks, where they not only output class predictions but also generate explanations that highlight the tokens deemed most relevant for reaching the predicted label. Yet it remains unclear whether these highlighted elements are behaviorally consistent with the model's own predictions under targeted interventions, which we refer to as functional auto-consistency. While much of the literature evaluates the textual plausibility of such explanations, few studies assess their functional consistency with the model's actual behavior. In this work, we propose an experimental framework based on the principle of auto-consistency: if a model identifies certain tokens as decisive, then isolating, removing, or semantically inverting them should produce systematic and interpretable changes in its predictions. We operationalize this evaluation through sufficiency, comprehensiveness, and counterfactuality metrics, and conduct experiments on IMDB and Steam reviews across both closed-source (GPT-4o-mini) and open-source LLMs (Gemma3, Granite8B, DeepSeek). Results show that GPT-4o-mini follows the expected progression across all metrics, Gemma3 and Granite8B maintain coherence under sufficiency but lose consistency under more demanding interventions, while DeepSeek variants display structural deviations, either failing to preserve sufficiency or overreacting under comprehensiveness and counterfactuality. These findings show that explanation reliability varies across LLM families and scales, with smaller models displaying contradictions and larger ones exhibiting over-sensitivity. By combining sufficiency, comprehensiveness, and counterfactuality, our approach provides a systematic methodology for assessing the functional consistency of LLM self-explanations.

---


### 160. [CounselPlex: A Stressor-Aware Full-Duplex Counseling Model](https://arxiv.org/abs/2610.32702)

**<font color=#1a73e8>作者：</font>** Yeonju Kim, Bella Godiva, Yong Man Ro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models can listen and speak at the same time, enabling natural, low-latency interaction. In counseling, however, these models often focus on the latest utterance and lose track of the seeker's underlying problem. We call this failure Stressor Blindness. We propose CounselPlex, a stressor-aware full-duplex framework that uses two operations. CounselPlex updates a short stressor state during seeker silence and injects this state into <PAD> positions while listening. We also introduce RoPE Position Shift Augmentation (RPSA), which broadens positional coverage during training and improves performance at longer turn depths in our evaluation. LLM-judge evaluations show improved counseling quality and stressor grounding over strong baselines.

---


### 161. [Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications](https://arxiv.org/abs/2610.32725)

**<font color=#1a73e8>作者：</font>** Aayush Acharya, Qi Zhang, Eduard Dragut 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of scientific literature far outpaces the speed of manual curation, creating a fundamental bottleneck in extracting structured knowledge from scientific texts. To address this, we introduce an agentic, ontology-guided framework for knowledge graph (KG) construction. Our framework utilizes specialized agents for document understanding, information extraction, ontology conformance, and entity linking. First, an LLM extracts factual knowledge in the form of triples with explicit textual evidence from research papers. Then the triplets undergo a multistage verification process to ground the triplets in the ontology. By enforcing schema constraints and requiring evidence in the form of text fragments, we ensure the data is both semantically consistent and traceable. In an agreement study over 1,000 extracted triplets, Gemini-2.5-flash achieves Cohen's $\kappa$ scores of 0.640--0.700 against three human annotators, matching the human--human agreement range of 0.616--0.689. We applied this framework to 2,000 scientific publications and construct a novel, ontology-grounded KG for climate science with 133,990 nodes and 755,308 relations; of the 23,327 triplets that the publications contribute after validation, 98.96\% are judged correct. The pipeline code and KG is publicly available this https URL.

---


### 162. [ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](https://arxiv.org/abs/2610.32752)

**<font color=#1a73e8>作者：</font>** Navyansh Mahla, Sashank Vandrangi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. We evaluate ActionRAG on MemoryAgentBench (MAB), which tests accurate retrieval, conflict resolution, long-range understanding, and test-time learning. Across its eight deterministic-scoring columns, ActionRAG achieves 55.1 average accuracy, improving over the strongest retrieval-based memory baseline by 5.4 points. Under MAB's query-time cost accounting, mean synthesis cost stays below \$0.001 per query on the four reported cost columns, and the sum of separately measured retrieval-side p99 components is 440.7 ms on our consumer Apple Silicon setup.

---


### 163. [On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models](https://arxiv.org/abs/2610.32770)

**<font color=#1a73e8>作者：</font>** Leon Sick, Lukas Hoyer, Yannick Strümpler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation enables post-training foundation models without relying on stronger external teachers. However, existing approaches rely on ground-truth question-answer pairs, human-curated problem sets, or other supervised signals. In this work, we reformulate on-policy self-distillation as a self-training framework, driven by self-generated question-answer pairs and privileged reasoning demonstrations. We push supervision to the limit: guided solely by coarse, high-level topic descriptions, the model synthesizes its own curriculum of queries and privileged reasoning traces without access to any human-curated prompts or answers. We find that self-distillation on fully synthetic privileged information enables a model to improve across multiple domains while retaining its capabilities on domains it is not self-trained on. We demonstrate the generality of this framework across text and multimodal domains, achieving consistent self-improvement on standard language benchmarks and Visual Question Answering. Our findings demonstrate that foundation models possess rich latent capabilities that can be amplified without external task supervision or curated problem distributions.

---


### 164. [Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents](https://arxiv.org/abs/2610.32781)

**<font color=#1a73e8>作者：</font>** Juan Felipe Duran, Arthur Tobler, Martin Vallières  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hospitals regularly buy software that clinicians and patients depend on. Because these purchases are costly, hard to reverse and can affect patient care, buyers look for evidence of which peer institutions already use a product and which systems it connects to. This evidence is public but scattered across vendor websites, press releases and third-party pages. Language-model agents can now collect it at low cost, but the correctness of the extracted claims is difficult to establish, and a wrongly listed customer can mislead buyers and misrepresent an organisation. We present a pipeline that builds a knowledge graph of customer and integration relations from the open web under one rule: every edge must be supported by a verbatim quote from its source page. Pages come from a deterministic crawl of each vendor's site and a budgeted ReAct agent that searches the rest of the web. A permissive extractor proposes relations with quotes, and a layered grounding stage decides which to keep, using a referent step that reads the whole page when a quote names only one side, deterministic checks, and a panel of five model calls voting on nine criteria. On 61 vendors, the pipeline reaches 0.94 precision and 0.71 recall against a page-level key covering the 6,428 candidate relations proposed by its extractor, whose verdicts were drafted by one model and re-checked with a second. Against the golden reference, the marketplace's own curated list, it scores lower, but 89% of the relations it keeps that the reference lacks are stated on a page. A confidence score built from the panel's votes keeps more correct relations than the fixed rule at the same precision, and reaches 0.90 precision at 0.90 recall. We also discuss how narrow, bounded model calls, string-matched evidence and voting address long-context degradation and run-to-run variance.

---


### 165. [Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding](https://arxiv.org/abs/2610.32784)

**<font color=#1a73e8>作者：</font>** Yonghui Niu, Yuhao Ji, Chang Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of video data has created an urgent need for efficient video understanding systems that can handle long and continuous visual inputs, posing significant challenges for Multimodal Large Language Models (MLLMs) due to severe memory bottlenecks. Moreover, existing compression methods often overlook the explosive accumulation of approximation errors. To address this issue, we propose Video-MemComp, a training-free and sensitivity-aware context management framework for memory-constrained streaming video understanding. Our method theoretically decomposes compression error into orthogonal local approximation error and layer-wise structural sensitivity via a first-order Taylor expansion. To minimize local approximation error, we perform token aggregation in a pre-RoPE safe zone with an attention-conserving logit bias, mitigating geometric distortions caused by RoPE rotations. To manage layer-wise structural sensitivity, we dynamically allocate the KV cache budget based on offline gradient priors and online context entropy, prioritizing high-sensitivity layers. Video-MemComp outperforms or achieves performance comparable to full-cache and state-of-the-art compression methods on benchmarks including MLVU, VideoMME, and EgoSchema. Notably, it improves the overall accuracy of Qwen2.5-VL-3B from 62.3% to 64.1% while reducing the KV cache to an equivalent of 6,000 tokens per layer, saving over 90% of KV memory.

---


### 166. [SREdit: Scene Response Guided Appearance Editing for Projection Mapping](https://arxiv.org/abs/2610.32792)

**<font color=#1a73e8>作者：</font>** Yuqiao Xia, Yuchen Deng, Ziheng Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Projection-based appearance editing changes selected visual attributes of a physical object through projection mapping (PM). To display a desired appearance, PM typically uses projector compensation, which computes a projector input that counteracts the geometric and photometric distortions of the scene. Compensation can only approximate this appearance within the available projection range, and it cannot revise the appearance itself. Pretrained LLM-based image editors provide a direct way to produce the desired appearance from a text prompt or reference image; projector compensation can then attempt to reproduce the edited result through projection. However, these editors do not have an accurate measure of the scene geometry or scene response. Therefore, their outputs may contain geometric misalignment, inconsistent shading, or changes outside the available projection range, which downstream projector compensation cannot correct. To address this problem, we introduce SREdit, an efficient response-guided framework for projection-based appearance editing. SREdit estimates a scene response map from the reconstructed scene that reflects how strongly projected illumination can affect different surface regions. SREdit uses the source appearance to constrain the early sampling process and preserve registration with the fixed physical object, while the scene response map adapts the amount of editing across surface regions. Experiments across two pretrained image editors show that SREdit improves projected appearance quality and reproduction fidelity. It adds less than one second per image with negligible VRAM overhead. Participants also consistently preferred the results produced with SREdit in our user study.

---


### 167. [HarnessMM: Recursive Self-Improvement for Harness Token Efficiency](https://arxiv.org/abs/2610.32813)

**<font color=#1a73e8>作者：</font>** Yuhua Jiang, Chang Xu, Feifei Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action. We introduce HarnessMM (Harness Minus Minus), a method for improving harness token efficiency through guarded decision reuse and recursive self-improvement (RSI). RSI iteratively refines companion harness configurations from training feedback, with validation selecting the configuration for deployment. A controller at the model-tool boundary reuses resolved decisions to replace later reasoning callbacks while actor weights remain fixed. Executable Decision Graphs store exact actions, literal arguments, causal dependencies, and public guards. Guarded Decision Reuse activates these persistent decisions from observed receipts; Certified Callback Substitution executes them through the native interface and records removal of the registered slow callback. New semantic decisions, unsupported evidence, and selector abstention invoke the original actor again. The representation restricts what feedback may change, while complete-task measurements establish quality and cost. On HumanEval, HarnessMM preserves Codex success at 90.82\% while reducing Tokens/task (k) from 66.72 to 47.02 (29.54\% saving). For DeepSeek Harness, success rises from 71.43\% to 85.71\% while Tokens/task (k) fall from 96.28 to 11.62 (87.93\% saving). A separate MBPP ablation measures 26.91\% lower cost than single-use graphs and 19.52\% lower cost than retained callbacks. These results establish guarded decision reuse as a practical way to reduce repeated reasoning in existing harnesses.

---


### 168. [Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves](https://arxiv.org/abs/2610.32851)

**<font color=#1a73e8>作者：</font>** Garima Agrawal, Prasun Das, Akshay Sarvade 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocabulary, related in name but operationally distinct, so one end-to-end journey implicates over a thousand near-identical rules that must not be conflated. Flat vector retrieval fails, returning an identical rule from the wrong service at high similarity with no signal of error. Content-level ontology, the traditional remedy, did not exist, and relating every occurrence of recurring entities would have cost more than the engagement and not survived a release cycle. We place the ontology at the artifact level. In this machine-generated corpus, each artifact retains its producer, component, service, domain and type, provenance that disambiguates before content is read. We present a knowledge layer that organizes before retrieving: a self-describing catalog, a sparse metadata registry, and a navigation hypergraph defined over artifacts rather than extracted entities. Queries resolve to artifact identifiers that constrain vector search, so the competing rule from another service is absent rather than outranked, making disambiguation structural, not statistical. Built in under a week and admitting new services by convention, the layer serves SDLC agents, developers, quality engineers and analysts. It supported root-cause analysis and resolution of 100+ production defects with developer verification and attributed 35 release regression failures to specific rules and services.

---


### 169. [Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery](https://arxiv.org/abs/2610.32866)

**<font color=#1a73e8>作者：</font>** Marek Masiak, Andrzej Szablewski, Nicola Cancedda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced during training, they are not easily interpretable. We present the full method of TopKLoRA, extending the preliminary proposal of Masiak et al. (2025), an interpretable-by-design LoRA variant in which only the $k$ largest adapter latents are active at each token. Unlike SAEs, TopKLoRA is trained purely on downstream loss, where optimisation pressure incentivises learning functionally causal latents. We demonstrate this sparse LoRA adapter in a sleeper-agent backdoor case study where we create model organisms by fine-tuning gemma-2-2b, Qwen2.5-1.5B, and Qwen2.5-7B on a poisoned instruction-following dataset. For each organism, we identify and ablate a circuit that is both necessary and sufficient to implement the backdoor. Furthermore, our new fine-tuning method produces sparse circuits that are up to an order of magnitude smaller than a dense LoRA baseline, allowing surgical ablation of the malicious capability without sacrificing instruction-following performance. Finally, we propose a technique to construct model organisms with localised circuits using TopKLoRA latents and gradient-routing, which we use to validate the findings of our circuit search algorithm. We consider these findings as a step toward interpretable-by-design architectures that provide faithful units of analysis without compromising model performance. We share our code: this https URL.

---


### 170. [Beyond pass or fail: an information-processing account of the Turing Test](https://arxiv.org/abs/2610.32868)

**<font color=#1a73e8>作者：</font>** Qiwei Zhao, Oriana Pansardi, James W. Strachan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Turing Test is passed when a human interrogator cannot distinguish machine-generated responses from human ones. Yet behavioral indistinguishability can reflect two fundamentally different failures: a failure of encoding, in which machine and human output distributions overlap so closely that source information is effectively absent; or a failure of readout, in which source information is present but the interrogator fails to extract it. To dissociate these possibilities, we inverted the Turing Test, placing humans and AI systems in symmetrical interrogator roles. Using a quantitative information-processing framework, we separated encoding, the information contained in the text; readout, the extraction of that information by an interrogator; and meta-readout, the interrogator's explicit access to the features guiding its own judgments. Across two series of experiments involving more than 3800 human interrogators and two generations of GPT models (GPT-4 and GPT-5), we found a striking dissociation across processing levels and interrogator types. As AI-generated responses became more human-like from GPT-4 to GPT-5, source information became more difficult for human interrogators to extract. GPT-5 interrogators, by contrast, read out source-discriminating information more accurately than GPT-4 interrogators. This improvement, however, came with a specific limitation: GPT-5 explanations only partially aligned with the feature weightings that actually predicted their judgments. Human interrogators showed the complementary pattern, with modest readout alignment but comparatively higher meta-readout alignment. Together, these findings suggest a double dissociation between readout and meta-readout across human and GPT interrogators.

---


### 171. [From Deliberately Constructed Systemic Representations of the World of Activity to Dialogue: A Five-Level Communication Architecture for Strong Language-Based ASI](https://arxiv.org/abs/2610.32869)

**<font color=#1a73e8>作者：</font>** Maxim Osovsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a five-level organization of message formation and understanding within thinking and activity in which ASI participates. Its central thesis is that a language model's context is fundamentally incapable of presenting the foundations of utterance formation for examination and verification. These foundations are established in advance by acquired schemas, systemic representations of the world of activity, and connections accepted as true within them. Neither context nor trained LLM weights, in themselves, attest to the presence of deliberately constructed systemic representations. The five levels distinguish systemic representations of the world of activity, a particular situation cut out from those representations, its narrative description, the full sense of a message, and text. A situation's schema-model is not identical to a story about it. A recipient reconstructs the full sense from an abbreviated text through jointly constructed and agreed-upon representations and joint activity. Reverse work proceeds from the full sense through an extended description and the situation's schema-model to the reconstruction of systemic foundations. The theoretical foundations draw on the systems methodology of G. P. Shchedrovitskiy, the structural differential of A. Korzybski, and the Meaning-Text theory of I. A. Mel'chuk. The contribution is a specific systemic-activity organization of content for examining and adjusting message foundations and controlling the consequences of their transformation. Further research concerns large graphical models of activity on reconstructible systemic foundations, distinct from text generation from context.

---


### 172. [J-Comm: Jacobian-Guided Latent Communication between LLM Agents](https://arxiv.org/abs/2610.32871)

**<font color=#1a73e8>作者：</font>** Xiangwei Wang, Wei Wang, Sachith Seneviratne 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent communication requires both an effective continuous reasoning process and an interface through which an external model can leverage its intermediate computation. We present J-Comm, a framework comprising two core components. First, a training-free Geometric Agreement for Latent Reasoning (GEAR) reweights token candidates over existing model embeddings, which monotonically optimizes geometric consensus among candidate tokens in embedding space at each step. Second, we introduce an H+J (Hidden-and-Jacobian) communication interface that gives the Receiver two complementary views of the Sender's reasoning. The H channel supplies continuous inputs derived from feedback distributions, while the J channel conveys intermediate-state cues in vocabulary-indexed Jacobian-lens coordinates. Intuitively, H provides inputs for the Receiver to reason from, while J offers additional guidance within its computation. The Receiver reconstructs these cues using its own dictionary and injects them into intermediate layers during prefill, enabling communication without sharing key-value caches or requiring identical model widths. In Qwen3-8B to Qwen3-4B communication, J-Comm achieves the highest mean score across seven benchmarks, including 94.80% on MATH500, 54.55% on GPQA-Diamond, 73.33% on AIME2024+2025, and 62.93% success on ALFWorld. Compared with TextMAS, it improves performance by 1.29-8.59 percentage points and reduces generated text tokens by 19.2-74.8%.

---


### 173. [Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations](https://arxiv.org/abs/2610.32874)

**<font color=#1a73e8>作者：</font>** Anouar Imel, Jin Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In LLM-agent opinion simulations, each agent reports the probability that a claim is true after seeing its own previous probability and the probabilities reported by its neighbors, and that number becomes its state in the next round. If the number describes the agent's position rather than the sentence it was shown, then rewriting the claim as its complement and replacing every probability p with 1 - p should return the complementary answer, so the two reports should sum to one. We test this with three small open models: Qwen3-4B, Llama-3.2-3B and Gemma-3-4B. On 2,304 agent states taken from a running network simulation, Qwen's paired reports sum to 1.18 on average, and on 48 real fact-checking claims from AVeriTeC they again exceed one. A controlled benchmark of 24 worlds, each with exactly two possible outcomes, shows the same failure in all three models. The discrepancy is two to ten times larger than the change produced by a same-meaning paraphrase, and it persists under repeated sampling and across peer group sizes and report strengths. When the reports are fed back into two populations that start from complementary states, the populations do not remain mirror images: their divergence is positive after five rounds for every model. Averaging each answer with the complement of its paired answer restores consistency by construction and lowers Brier loss averaged over the two wordings, but at the final round it beats the better of the two original wordings for only one of the three models. A schedule-by-targeting experiment on the same model gives a small, stable interaction because such sweeps keep the claim wording fixed. Consistency under rewording therefore needs its own test before simulated probabilities are read as beliefs

---


### 174. [Advancing SVD-based LLM Compression via Layer-Wise Error Model Search](https://arxiv.org/abs/2610.32878)

**<font color=#1a73e8>作者：</font>** Moritz Thoma, Maximilian Groezinger, Maximilian Forstenhäusler 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-rank SVD-based compression offers a powerful strategy to reduce the computational costs of LLMs. However, existing methods face two key limitations: (i) global rank allocation, where uncalibrated error proxies fail to capture complex error propagation, and (ii) decomposition quality, where Fisher-based estimators suffer from severe rank collapse. In this work, we address these limitations by introducing Layer-wise Error Modeling Search (LEMS) and KFAC-SVD. LEMS advances rank allocation by introducing a layer-wise error surrogate that integrates local and global layer importance alongside a propagation bias, enabling effective global rank allocation via an ILP formulation. KFAC-SVD improves decomposition quality by utilizing token-wise statistics, mitigating the rank deficiency observed in prior Fisher-based SVD approaches. Across Mistral, Qwen3, and Llama 3 model families, we show that LEMS consistently outperforms existing search strategies, delivering significant zero-shot accuracy gains of up to 4.8 p.p. that generalize to model sizes of 70B parameters, while KFAC-SVD achieves an average perplexity improvement of 15%. Project page and code: this https URL

---


### 175. [Multimodal Generative AI Assists Comprehensive Echocardiographic Interpretation](https://arxiv.org/abs/2610.32880)

**<font color=#1a73e8>作者：</font>** Yi Qin, Marawan Elbatel, Shanshan Song 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is the cornerstone of cardiovascular diagnostics, yet its global utility is constrained by a critical shortage of experienced interpreters. Current artificial intelligence (AI) solutions remain limited, typically operating as opaque "black boxes" or focusing on narrow tasks that fail to capture the holistic, guideline-driven reasoning of a clinician. Here we introduce EchoChat, a generative multimodal vision-language model that performs comprehensive echocardiographic analysis to support clinician interpretation. By emulating the cognitive workflow of a cardiologist, EchoChat integrates vast medical knowledge with a chain-of-thought reasoning mechanism to explicitly ground its conclusions in visual evidence. Trained on echocardiography-instruction pairs from 46,358 examinations, our model establishes a new state-of-the-art across diverse cohorts from six international medical centers. It supports the broadest diagnostic scope of 33 cardiac conditions and findings, including 15 newly added conditions for which it achieves an average F1 of 73.7% across available external evaluations. It surpasses existing best-performing foundation models in cardiac condition recognition (improving average recall by 13.54% on shared tasks) and quantification (average R2 score increase of 0.275 on shared tasks). Furthermore, in a source-blinded echocardiographer reader study, echocardiography reports co-generated with EchoChat were rated higher in diagnostic accuracy and completeness by two senior echocardiographers, and improved diagnostic performance from 72.78% to 82.75% in terms of F1 score over routine-reader only reports. These results demonstrate that integrating clinical reasoning into multimodal AI can democratize specialist expertise and transform the standard of cardiovascular care.

---


### 176. [NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding](https://arxiv.org/abs/2610.32881)

**<font color=#1a73e8>作者：</font>** Nilesh Prasad Pandey, Jangseon Park, Jason Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but its cost is dominated by autoregressive rollout generation, which can exceed 70% of training time. Existing speculative-decoding methods are poorly suited to this setting: model-based drafters consume scarce GPU memory and may become misaligned as the policy evolves, while existing model-free methods do not explicitly exploit repetition across training epochs. We observe that recent rollouts of the same prompt provide a high-quality, self-updating draft source. Based on this insight, we propose NgramRL, a per-prompt n-gram drafter constructed from bounded recent rollout history. NgramRL requires no auxiliary model, drafter training, or persistent GPU-resident drafter state, while target-model verification preserves the rollout distribution. To hide CPU cache lookup and scheduling, we further introduce an adaptive fan-out prefetcher that predicts likely verification outcomes (j, b), consisting of the accepted draft length j and target-emitted continuation token b. A causal budget allocator concentrates prefetches on high-probability outcomes, while uncovered outcomes fall back to sequential lookup without changing committed tokens. Across two model families and three reasoning and structured-generation workloads, NgramRL commits 3.60-7.77 tokens per target-model forward in the warm-cache regime, up to 1.99x more than SuffixDecoding and 7.0x more than prompt-lookup decoding. On Spider, the prefetcher covers 96.6% of Qwen3-8B outcomes at a candidate budget of 16 and improves measured rollout throughput by 1.38x over synchronous NgramRL, approaching its 1.40x overlap ceiling.

---


### 177. [When Should I Trust This? Designing and Evaluating Factuality Indicators for LLM-based Chatbots](https://arxiv.org/abs/2610.32883)

**<font color=#1a73e8>作者：</font>** Greta Warren, Jessica Heal, Sila Eser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems increasingly mediate how people seek information, yet communicating AI factuality to laypeople remains challenging. Through a mixed-methods investigation involving interviews (N=8), a survey (N=1,000), and an experiment (N=5,151), we examine how people evaluate AI-generated information for gardening, mathematical, and medical queries, and how factuality indicators (confidence and sources) shape perceptions. Our interviews and survey show people selectively verify AI responses using external and AI-provided evidence, moderated by contextual factors. Although confidence-indicators affected trust and accuracy perceptions, people hold diverse, ambiguous interpretations of AI confidence. Sources were viewed as crucial, yet users raised concerns about source reliability and verification effort. Our experiment showed that confidence and source-based indicators influenced initial perceptions, but effects disappeared once participants learned the response's correctness. Medical queries elicited skepticism regardless of indicator. Findings motivate helping users interpret model confidence and integrating source information into the interface to support calibrated trust in AI-supported information-seeking.

---


### 178. [SemantEq: Faithful Bidirectional Equivalence of Formal Statements](https://arxiv.org/abs/2610.32919)

**<font color=#1a73e8>作者：</font>** Xinrui Li, Pawan Sasanka Ammanamanchi, Siddharth Bhat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Statement autoformalization translates mathematics from natural language into a proof assistant such as Lean 4, and models now do it at scale. As provers get stronger, the burden of correctness shifts from the proof to the statement, that is, to whether the formal statement faithfully translates its source. Given a trusted reference formalization, the natural test is logical equivalence, and it proves too much. $P \leftrightarrow Q$ holds trivially for any two statements $P$ and $Q$ that the library proves, because a prover can prove each separately and pass through $P \leftrightarrow \mathrm{True} \leftrightarrow Q$. The stronger the prover, the more unrelated pairs pass. Earlier methods restrict the prover and check that each proof names the other statement. We introduce SemantEq, a more principled relation that instead requires each statement to turn into the other only through a chain of allowed steps, such as logical rearrangement and rewriting with the library's own equations. Our programs judge a proof by the proof term Lean checks, not by its tactic script. SemantEq-Eval, a search without a model, reaches 100% precision and 65.6% recall on the ProofNetVerif test split under our adjudicated labels, against 95.8% and 61.8% for BEq+, and an 8.9-fold increase in its CPU time adds at most three pairs. A language model finds more proofs, but under two of four prompts it proves both directions of about two in five of the non-equivalent pairs. SemantEq-ProofAudit audits each model-written proof under a policy derived from the relation and accepts none of the 104 non-equivalent pairs, and it raises recall on 407 equivalent pairs from 65.4% to 81.1% under the best prompt. Separating the generation of equivalence proofs from their acceptance lets a stronger prover raise recall without changing what an acceptance means. We release code and data at: this https URL

---


### 179. [Adaptive Frequency Threshold Byte Pair Encoding for Mixed Natural Language and Structured Symbolic Corpora](https://arxiv.org/abs/2610.32921)

**<font color=#1a73e8>作者：</font>** Pietro Di Nicco, Lucio La Cava, Andrea Tagarelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models rely on subwording tokenization to define the discrete units of input processing, typically using methods like Byte Pair Encoding (BPE) that treat whitespace as a fixed semantic boundary. This design is inherently limited, as many meaningful concepts---including multiword expressions and the structured environments of formal languages like LaTeX---frequently span across whitespaces. While recent superword tokenization methods attempt to address this by relaxing whitespace constraints, they often rely on greedy frequency-driven merging that fails to account for token length or the specific needs of underrepresented domain-specific languages. In this paper, we introduce Adaptive Frequency Threshold Byte Pair Encoding (AdaBPE), a new tokenization method that leverages an adaptive frequent-pattern mining approach. AdaBPE features a twofold dynamicity: it adapts minimum frequency thresholds based on both the length of a candidate token, to prevent favoring frequent short patterns, and its type, to distinguish between general and formal language patterns, using LaTeX as case in point. This allows the model to efficiently allocate vocabulary capacity to domain-specific notations, such as LaTeX, even when they represent a small fraction of the training data. We evaluate AdaBPE across five datasets spanning LaTeX and natural language, showing consistent gains in encoding efficiency and downstream language-model performance on domain-specific content without compromising general-language performance.

---


### 180. [Yalda-Embedding: Open Development of a Competitive Persian Retrieval Model](https://arxiv.org/abs/2610.32933)

**<font color=#1a73e8>作者：</font>** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in multilingual text representations, effective dense retrieval for Persian remains constrained by the limited availability of language-specific training resources and compact embedding models. We present Yalda Embedding, a 595.8-million-parameter Persian retrieval model adapted from Qwen3-Embedding-0.6B using more than one million query-document pairs. On eight Persian retrieval tasks from FaMTEB, the model achieves the highest macro-average among the evaluated 0.6B models, scoring 0.5488 and outperforming Qwen3-Embedding-0.6B and F2LLM-v2-0.6B on every task. It also approaches Qwen3-Embedding-4B, winning on four tasks, tying on one, and trailing by 0.0075 in macro-average. An incremental ablation study examines contrastive batch size, optimization stabilization, and relational knowledge distillation from F2LLM-v2-8B. Under the one-epoch training setup, contrastive fine-tuning alone yields a modest mean improvement over initialization and regressions on two tasks. The final distilled configuration improves all eight tasks over the non-distilled model, raising the mean from 0.4813 to 0.5488 without increasing inference-time model size. These gains include hard-negative evaluation tasks despite training without explicitly mined or supplied hard negatives. We release model weights, training and evaluation code, the pairwise dataset, and its teacher-embedded counterpart, enabling inspection of data composition and training procedures, independent evaluation, and reuse without repeating expensive teacher inference.

---


### 181. [Beyond Discrete Tokens: Preserving Numerical Continuity in Medical Vision-Language Models](https://arxiv.org/abs/2610.32948)

**<font color=#1a73e8>作者：</font>** Dianye Huang, Jiamei Guo, Yue Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: To develop a unified vision-language model for prompt-conditioned quantitative ultrasound measurement that addresses the mismatch between continuous measurement targets and discrete token-based numerical prediction. Methods: This article presents HAD-VLM, a hybrid autoregressive-diffusion framework that combines autoregressive text generation with continuous measurement prediction within a shared backbone. Visual prompt tuning adapts the vision encoder to ultrasound images. A diffusion process predicts a five-component representation comprising caliper endpoint coordinates and measurement length. A post-processing strategy combining the proposed coordinate-length consistency mechanism with ensemble prediction is introduced to refine measurement estimates. We evaluate four echocardiographic measurement tasks on EchoNet-LVH, with additional assessments of medical question answering and X-ray vertebral measurement. Results: HAD-VLM achieves mean absolute errors of 1.36, 2.77, 3.05, and 1.16 mm for IVSd, LVIDd, LVIDs, and LVPWd, respectively, reducing errors by 21.4-37.6\% relative to the Vicuna-based autoregressive baseline. It also outperforms fine-tuned Qwen3-VL and direct MLP regression across all four tasks. Medical question answering performance is preserved on the evaluated dataset. For X-ray vertebral measurement, HAD-VLM reduces mean absolute error from 11.4 to 6.7 pixels. Conclusion: Integrating autoregressive language generation with diffusion-based continuous prediction improves quantitative medical image measurement while retaining prompt-conditioned task flexibility. Significance: HAD-VLM provides a unified approach to combining language interaction with anatomically grounded numerical prediction for quantitative medical image analysis.

---


### 182. [Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning](https://arxiv.org/abs/2610.32951)

**<font color=#1a73e8>作者：</font>** Yijing Ke, Tianle Cai, Ruosong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for large language models often uses separate systems for inference and training. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the entire inference and training stacks, change global precision, or modify the learning algorithm. We ask whether aligning selected parts of the execution stack can stabilize BF16 RL while other implementation differences remain. We align training-side rounding locations with inference in three regions---RoPE, SwiGLU, and residual RMSNorm---by retaining selected intermediates in FP32 until their BF16 outputs. Across four Qwen-family models, aligning all three regions prevents the collapse observed under the default BF16 baseline; RoPE-path alignment alone also suffices in the studied runs, despite remaining numerical discrepancies. The interventions keep the inference engine, matrix-multiplication and attention kernels, and learning objective unchanged.

---


### 183. [Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox](https://arxiv.org/abs/2610.32955)

**<font color=#1a73e8>作者：</font>** Federico Lucca  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered hypotheses, human labels in the agent's review loop) that yields ground truth before any training. On 739 real Italian/English emails labelled by the owner (231 unbiased, 500 adversarially sampled), we compare nine systems under thread-grouped cross-validation: the production keyword rules, a TF-IDF + logistic-regression baseline, local typed decision models (Tev1, Nimble), a hosted decision model (Nimble v4-max), and hosted generative LLMs (Qwen2.5-7B, Gemma 4 26B/31B). Four results. The production rules score 28% on message type against a 58% majority class: the field shown most prominently carried no information. With ~200 labels, logistic regression has the highest accuracy on every field (type 0.79, urgency 0.74, needs-reply 0.83, is-noise 0.90), though it never predicts the two rarest classes and is statistically tied with Gemma 4 on type; few-shot prompting does not close the gap. The sender's relationship (client, supplier, service) is recovered from other emails of the same contact with 98.6% accuracy where the contact has been seen, and is not inferable from a single message by any model: it belongs in the contact graph, not the prompt. Finally, accuracy is not the product metric: composed into actions, the most accurate system most often ignores emails needing action (18% vs 4% for the best LLM); a cost-chosen threshold on its noise probability halves that rate and makes it the cheapest system.

---


### 184. [MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption Pairs](https://arxiv.org/abs/2610.32967)

**<font color=#1a73e8>作者：</font>** Tarunya Prasad, Bharatesh Chakravarthi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic misinformation can arise when an authentic image is paired with a caption that changes or distorts its narrative. Because the image itself may contain no visible signs of manipulation, methods designed to detect pixel-level artifacts can miss these misleading image-caption pairs. We study this problem using DGM4+, a dataset designed to evaluate the detection of global scene and semantic inconsistencies. We propose a multimodal model that combines image-text representations from SigLIP with visual scene features from DINOv2 through a projection MLP, and adapts Qwen2-VL-7B using LoRA. The model jointly predicts whether an image-caption pair is authentic, identifies the manipulation type, and grounds the misleading caption tokens. On the DGM4+ validation split, the model achieves an F1 score of $0.9679$ for binary authenticity classification. These results suggest that parameter-efficient adaptation of vision-language models is promising for detecting semantic inconsistencies, while also motivating further work on precise token-level grounding.

---


### 185. [The Language of Instruction: Genre and Generative AI](https://arxiv.org/abs/2610.32982)

**<font color=#1a73e8>作者：</font>** James E. Dobson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article argues that instruction-fine-tuned language models should be understood as implementing a genre, what is proposed as the instructional-conversational genre. This genre is an amalgamation of discursive language from prior conversations between generative models and humans recursively run through these massive neural networks. It is instantiated in applications through instruction fine-tuning, the inclusion of a pretext known as a system prompt, and the formalization of inputs in mark-up languages characterized by the use of special tokens and role assignment in turntaking structures.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 186. [PaperScorer: How Predictable Is Paper Acceptance?](https://arxiv.org/abs/2610.31791)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sachin Konan, Jonathan Liu, Zhuang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated research is largely evaluated by benchmark performance, but the value of research rarely reduces to a single score. Humans judge a work's holistic contribution through peer review, which is hard to model because it is noisy and depends on many factors. However, what if, given only the paper, we could predict its peer-review decision directly? We introduce PaperScorer, a family of models that predict a paper's accept or reject decision from its extracted text or page screenshots, training only on the decision after removing author identity and formatting shortcuts. Vision models are the most predictive (68% accuracy on ICLR papers and 77% on ML papers from arXiv), beating text-only and frontier reasoning models. Unlike plain text, page images retain figures, layout, and presentation. This signal is robust, surviving smaller models and even compressing the whole paper into a single image. But accurate predictions are not evenly spread. PaperScorer is strongest on the lowest and highest rated papers, while papers rated in the middle stay unpredictable for our models and frontier systems alike. Additionally, its confidence is calibrated, so its most confident predictions are also its most accurate. Overall, PaperScorer shows how much of the decision a paper carries on its own, marking a first step toward AI-driven research evaluation.

---


### 187. [Rethinking Multi-View Fusion for Urban Representation Learning](https://arxiv.org/abs/2610.31850)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sean Bin Yang, Zongyi Xu, Jilin Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban region representation learning encodes heterogeneous urban signals, such as mobility flows, points of interest, and land-use patterns, into unified embeddings for downstream tasks, including check-in prediction, crime forecasting, and service demand estimation. Existing approaches rely on globally shared fusion and joint optimization, implicitly assuming uniform modality importance and naturally balanced multi-objective training. However, urban data is inherently heterogeneous. Our empirical analysis reveals two structural issues: (i) modality utility varies markedly across regions, causing static fusion to overemphasize signals from certain modalities; and (ii) heterogeneous objectives exhibit persistent gradient imbalance, causing representational bias and unstable training. We present PRISM, a self-adjusting framework for adaptive multi-view learning. PRISM adapts sparse MoE routing to learn region-specific view allocations, while a PID (Proportional Integral Derivative)-inspired regulation mechanism mitigates gradient conflicts during optimization. Experiments on three large-scale urban datasets show that PRISM achieves competitive performance compared with strong multi-view baselines, while providing more stable optimization behavior and more balanced region representations.

---


### 188. [Forecasting Associations, Not Interventions: A Preregistered Causal Audit of Covariate-Aware Time Series Foundation Models](https://arxiv.org/abs/2610.31869)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zong-Han Bai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Covariate-aware time series foundation models (TSFMs) accept a future path for a control variable and return a forecast, inviting what-if queries. The query is interventional; the models are trained on observational data. We determine whether their answers are the conditional slope $\partial E[Y|X]$ or the interventional effect $\partial E[Y|do(X)]$, at three levels. Theory: a Bayes-optimal observational predictor answers interventional queries associationally unless the adjustment set is available and used; for in-context least squares we derive the resulting confounding gap -- a model's effect estimate under an observational minus under a randomized context -- in closed form, a parameter-free reference line. Behaviour: on a preregistered grid with exact counterfactual ground truth, Chronos-2, TiRex-2, TabPFN-TS and TimesFM-2.5 all track this line ($R^2$ 0.90-1.00) and respond more confounded than regression itself (slopes 1.3-1.8), on linear and nonlinear structural models. Pairs of models with identical observational laws prove this is not an identifiability limit: when the effect is identifiable, least squares recovers 100% of the true effect difference, Chronos-2 75%, TiRex-2 34%. Representation: linear probes decode the data-generating regime (94-96%) and the true effect ($R^2$ 0.7-0.9) from embeddings that the forecasts ignore. On two physical systems with randomized actuators, pretrained models under-respond by 2-5x and ignore in-window confounding. Minutes of interventional post-training on 3,000 synthetic series cut the gap by up to 83% and transfer outside the training prior. Its forecasting cost is a replay-distribution effect: replaying the model's own pretraining prior cuts it from +47% to +10% MASE, and with low-rank adaptation yields a recipe meeting the preregistered criterion over three seeds (52-61% gap reduction at +1-3% cost) while improving the DoTime benchmark.

---


### 189. [Beyond Local Accuracy: Benchmarking the Rollout Reliability of PDE Foundation Models](https://arxiv.org/abs/2610.31935)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jaewan Park, Seid Koric, Giri Krishnan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PDE foundation models enable data-efficient adaptation but are deployed autoregressively, so short-horizon accuracy need not imply reliable simulation. We ask whether the short-horizon advantage of a foundation-model recipe persists when its predictions are repeatedly fed back as inputs for a long horizon. We define error amplification as G=E(H_f)/E(H_s), which measures full-horizon error relative to short-horizon error. We evaluate seven models on seven two-dimensional time-dependent PDE datasets: scratch-trained FNO and DeepONet; fine-tuned DPOT, GPhyT, Poseidon, and Walrus; and frozen in-context VICON. We report VRMSE, relative L_2, and relative MAE. Six datasets provide paired short- and full-horizon scores, while CE-RM contributes short-rollout sweeps only. At least one fine-tuned foundation model outperforms both scratch baselines in 26 of 30 short-rollout dataset--budget cells under every metric. Nevertheless, full-horizon VRMSE exceeds short-horizon VRMSE in 140 of 144 paired trained configurations, with a median error amplification of $2.04$. The count below VRMSE one falls from 104 to 53, and 12 full rollouts exceed ten although none does at the short horizon. Walrus achieves the lowest full-horizon VRMSE in 16 of 24 cells, yet its median error amplification is $2.70$. Relative L_2 and relative MAE show the same qualitative pattern. These results show that favorable short-horizon rankings can coexist with substantial error amplification. PDE foundation-model benchmarks should therefore report horizon-resolved absolute errors, amplification statistics, and failure incidence rather than a single local forecast score.

---


### 190. [Kolibri: A Sovereign European Model on the Pareto Frontier](https://arxiv.org/abs/2610.31945)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aleph Alpha, Moritz Althaus, Artur Baranowski 等 67 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This report introduces Kolibri, an English-German mixture-of-experts transformer with 78.1B total parameters and 3.46B active parameters per token, released as open weights under the Apache 2.0 licence. We built Kolibri for sovereign and specialised deployment, with a particular focus on German and on regulated domains such as public administration, industry, and aerospace. To support these settings, we control the full model-development process, including data, architecture, training infrastructure, post-training, and evaluation.
We train Kolibri on 24T tokens across pre-training, mid-training, and long-context extension, with German accounting for more than 20% of the data mix by bytes. To reach this share, we complement German datasets with more than 2T German tokens that we curate from the web with our own pipeline and generate synthetically. Post-training combines supervised fine-tuning on curated German and English data with reinforcement learning on more than 1.2M internally curated tasks, which cover reasoning, tool use, instruction following, code, and retrieval. The model activates 4.4% of its parameters per token, and among the open models evaluated in this report, it lies on the Pareto frontier of quality and serving cost in English and German.
Kolibri builds on Kolibri Origin, an earlier iteration that validated our full pipeline at scale. Both models come from our Model Factory, which connects data, experimentation, training, evaluation, and deployment through version-controlled workflows.

---


### 191. [Agentic AI Defense: Decode-Time Provenance Binding for MCP](https://arxiv.org/abs/2610.31974)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Eric Yocam, Varghese Vaidyan, Paris Kalathas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems using the Model Context Protocol (MCP) are vulnerable to indirect prompt injection through untrusted tool outputs. We demonstrate cross-modal trust laundering, in which instructions concealed in an email-signature image using least-significant-bit (LSB), discrete cosine transform (DCT), or metadata steganography bypass text scanners and enter a multi-agent workflow when decoded by a tool. To counter this threat, we propose decode-time provenance binding, which combines HMAC-authenticated trust labels with an MCP-maintained provenance ledger and context-taint tracking. The mechanism labels decoded content as untrusted and blocks critical tool calls influenced by that content, even when a compromised agent substitutes a valid trusted label. We evaluate the approach using a real MCP testbed with three steganographic carriers and 24 adaptive payloads. The undefended pipeline exhibits 100% attack success, while keyword and regex defenses each permit 62.5% of attacks. Our mechanism blocks all attacks (0% success), including adversarial label substitution across mediated agent boundaries. A four-component ablation validates the roles of decode marking, cryptographic authentication, lineage tracking, and sink enforcement. An audited trusted-promotion mechanism increases legitimate-task completion from 67% to 100% without compromising protection. The approach provides carrier-independent containment within fully mediated MCP execution environments. Code and data are publicly available.

---


### 192. [Controlled Evaluation of EEG Foundation Models: Random Initialisation, Band-Power and Validation-Selected Probes](https://arxiv.org/abs/2610.32067)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingyu Jeon, Suwan Cho, Jae Young Suh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models report downstream gains, yet their protocols seldom include three controls. These are the same encoder untrained, spectral features fitted on the same data, and a layer picked without looking at test scores. We therefore evaluate five publicly released EEG foundation models and an in-house JEPA-style model under one protocol with all three controls and several seeds, on five benchmarks and four added task families. The controls change the reading in three ways. First, picking the probed layer by its test score raises the layer-wise peak by an average of +0.034 and reverses the peak-versus-output gap in 9 of 36 cells. Second, with the layer picked on validation, random initialisation matches or beats pretraining for half of the models on sleep and emotion, and no model beats a five-band log-power baseline on emotion or motor imagery. Third, after full fine-tuning only 5 of 30 pairs gain beyond twice their seed spread, and the one clear loss of -0.290 AUROC persists under matched learning rates. From these results we draw four reporting practices, and we release every cell for re-analysis.

---


### 193. [EDWARD-NMT: Elastic Dimensions With Adaptive Routing and Dual-consistency for Neural Machine Translation](https://arxiv.org/abs/2610.32115)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Edward Nguyen, Thai Tran, Kiet Anh Hoang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) is a powerful paradigm for scaling Neural Machine Translation (NMT) and managing language heterogeneity. However, practical limitations hinder its deployment on resource-constrained devices: the entire expert pool must remain in memory, and the per-token compute budget is statically fixed during training by rigid top-k routing. We introduce EDWARD-NMT (Elastic Dimensions With Adaptive Routing and Dual-consistency for NMT), a novel MoE encoder-decoder architecture designed for a train once, deploy anywhere paradigm that exposes a family of deployable sub-networks at inference time. EDWARD-NMT integrates three key innovations: (i) Matryoshka-style elastic dimensions to flexibly reduce the memory footprint; (ii) an adaptive sigmoid router with a learned, task-conditioned threshold, allowing each token to dynamically determine its active expert count; and (iii) a dual-consistency objective to maximize the performance of the extracted sub-networks. Extensive experiments on PhoMT (En-Vi), WMT-14 (En-De), multilingual OPUS-16, and a multi-domain De-En benchmark validate our approach. The full-capacity architecture matches or exceeds strong MoE baselines with improved parameter efficiency. Furthermore, the sub-networks seamlessly extracted from a single checkpoint consistently outperform comparably sized dense Transformers without any retraining.

---


### 194. [ImageRSI: Verification-Driven Recursive Self-Improvement for Agentic Image Generation](https://arxiv.org/abs/2610.32120)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuo Han, Zhilin Wang, Peng Ling 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex text-to-image requests remain difficult to satisfy reliably. Verifying and repairing an image can fix an individual output, but a successful repair does not necessarily carry over to other requests. We present ImageRSI, a framework that keeps the image generator frozen and combines three components: five-dimensional verification and repair within each task, an experience library shared across tasks, and offline updating of the judge. Candidate experiences enter the library only after paired A/B validation, and the judge is updated with supervised fine-tuning and GRPO on accumulated image-judgment records and evaluated before reuse. We also introduce ImageReq-Bench, a benchmark of 961 requests built around hard cases in real-world image-generation requests, each paired with an evaluation checklist. ImageRSI achieves a Checklist Strict Accuracy (CSA) of 52.6% on MindBench (with Nano Banana Pro as the generator) and 65.66% on ImageReq-Bench, and we compare system outcomes across judge-training configurations.

---


### 195. [MS-TTRL: Breaking the Frequency Conflict in Multiple-Solution Test-Time Reinforcement Learning](https://arxiv.org/abs/2610.32234)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhixia Zhang, Binqian Xu, Huaiyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific, engineering, and mathematical reasoning tasks can admit multiple valid solutions, while exhaustive annotation of the full solution set is often prohibitively costly. Test-time reinforcement learning (TTRL) applies reinforcement learning to unlabeled test instances, offering a label-free approach to multiple-solution reasoning. In this setting, generation frequency serves two opposing objectives: correctness estimation favors frequent outcomes, whereas outcome-level diversity preservation favors less frequent outcomes. We term this tension the \textbf{Frequency Conflict}. To resolve this conflict, we propose MS-TTRL, which obtains frequency-independent correctness estimates through Outcome-Level Self-Verification while reserving generation frequency solely for diversity preservation. Three-State Outcome Cache and the Candidate State support verification reuse across repeated observations and confidence-aware handling of ambiguous outcomes, while Confidence-Gated Inverse Probability Scaling selectively strengthens the learning signals of rare, reliably verified outcomes. Experiments across two benchmarks, four multiple-solution tasks, and three backbone models, each evaluated with five random seeds, show that MS-TTRL improves Recovery Rate by 19.13 percentage points on average over the best-performing label-free baseline and approaches the performance of the supervised IPS-GRPO.

---


### 196. [LapaFM: A Laparoscopic Foundation Model via Multi-Stage Continual Learning](https://arxiv.org/abs/2610.32263)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaobo Zhu, Shiwei Wu, Yu An 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence-based analysis of intraoperative laparoscopic videos has the potential to improve surgical decision-making and precision. However, effective surgical assistance requires models that can generalize across diverse intraoperative tasks. Here we present LapaFM, a foundation model for laparoscopic surgery trained on more than 20,000 minutes of surgical videos using a multi-stage continual learning strategy that mitigates catastrophic forgetting and inter-task interference. LapaFM learns multimodal visual representations and supports multiple tasks, including smoke removal, surgical phase recognition, instrument and polyp segmentation, and lesion identification. The model was evaluated on 13 retrospective and two prospective cohorts collected from different imaging devices. LapaFM consistently outperformed task-specific models and existing foundation models across datasets, and also generalized to gastrointestinal endoscopy tasks, including polyp detection and classification. Notably, it recovered over 90% of smoke-obscured frames and achieved clinician-level or superior performance in lymph node metastasis prediction and prospective polyp classification.

---


### 197. [Beyond Channel Data: Configuration-Enriched Radio Foundation Models](https://arxiv.org/abs/2610.32542)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shrihari Vasudevan, H. G. Ranjani, Raaghul Ranganathan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes incorporating channel configuration (CFG) information into Radio Foundation Model (RFM) pre-training and demonstrates that the resulting CFG-enriched embeddings serve as effective inductive priors for downstream tasks under label scarcity. We compare the proposed embeddings with raw channel tokens and multiple baseline models, under three different data regimes, for multiple downstream tasks --- Line-of-Sight/Non-Line-of-Sight (LoS/NLoS) classification, timing advance (TA) estimation, and beam selection. Evaluation is done in both in-distribution and out-of-distribution configuration settings. Experimental outcomes show that the proposed embeddings consistently outperform and/or are competitive to the baselines, across experiments in both seen and unseen configuration scenarios.

---


### 198. [Reuse, Don't Retrain: Efficient, Modality-Versatile Geospatial Foundation Models through Feature Distillation](https://arxiv.org/abs/2610.32566)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mario Hamon, Pierre Adorni, Minh-Tan Pham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models (GeoFMs) are costly to pretrain, yet model families often repeat this process across backbone scales and sensing modalities. We investigate feature distillation as a more efficient way to reuse existing representations. First, we distill frozen CROMA and TerraMind teachers into smaller Vision Transformers through patch-level feature matching. Across nine PANGAEA tasks, distilled TerraMind Tiny, Small, and Base outperform their scale-matched released counterparts by 2.76, 3.02, and 1.87 mean IoU points, respectively; each also matches or exceeds the next-larger released model. Distilled CROMA-Base gains 2.05 points. TerraMind-Base required only 43 A6000 GPU-hours, approximately 0.5\% of the reported cost of independent pretraining. Second, we introduce TEDI, an unpaired multi-expert approach combining TerraMind for multispectral imagery and DINOv3 for high-resolution RGB. Separate patch embeddings route unpaired inputs into a shared Transformer trunk, removing the need for co-registered data. TEDI-Large achieves the highest single-model mean in our PANGAEA-9 comparison (62.51 mIoU), outperforming both teachers overall while retaining their modality-specific strengths. TEDI-Base reaches 61.75 mIoU with 72\% fewer parameters. These results show that distillation improves the GeoFM accuracy-compute frontier while consolidating complementary experts into a single versatile backbone.

---


### 199. [Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR](https://arxiv.org/abs/2610.32572)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shashi Kumar, Yanis Labrak, Sergio Burdisso 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting ASR to a domain with only untranscribed audio typically relies on pseudo-labeling, a strong teacher transcribes the audio and a student is fine-tuned on it. Because supervised fine-tuning (SFT) treats every pseudo-label token as a target, the student inherits the teacher's errors. We show that using the same pseudo-labels as a reward reference for Group Relative Policy Optimization (GRPO) is more robust to label noise. In the banking domain, GRPO yields 29.3% to 56.2% relative WER improvements over SFT on Whisper-generated labels, and the advantage holds across four Whisper sizes, four teacher families, three domains and four languages. While SFT reproduces almost 100% of teacher errors verbatim, GRPO passes through only 27%. Rollout statistics explain why, erroneous pseudo-label words rarely appear in on-policy rollouts, so group-relative advantages stay aligned with the clean transcript, whereas SFT forces them into the policy's support and collapses the reward variance GRPO relies on.

---


### 200. [When is more search useful? An Empirical Study of Search Utility in Quality-Aware Decoding for Machine Translation](https://arxiv.org/abs/2610.32679)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Javier Garcia Gilabert, Rico Sennrich, André F. T. Martins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quality-Aware Decoding (QAD) improves machine translation through test-time scaling, generating multiple candidate translations and selecting the final output with a quality-aware decoder. Usually the same candidate budget N is spent on every source sentence, assuming that all inputs require the same amount of search. We show that this assumption does not hold and that the quality gain obtained from additional candidates varies across sentences. We study search utility through three quantities: total scaling gain, how much quality a sentence can gain from a much larger candidate pool; marginal scaling gain, the expected gain from generating one additional batch of candidates; and the sampling saturation point, the candidate budget required to realize most of the total scaling gain. We investigate two sources of information for predicting these quantities: signals available before candidate-set expansion, and statistics computed from the candidate pool accumulated during search. We find that sentence-level signals correlate with total scaling gain but are less informative about the sampling saturation point. In contrast, properties of the current candidate pool provide useful signals of marginal scaling gain. Finally, we show that these signals can identify sentences that obtain larger gains when additional search is selectively applied.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
