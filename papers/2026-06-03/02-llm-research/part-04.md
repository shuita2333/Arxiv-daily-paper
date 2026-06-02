# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 151. [Lost in Delusion: Examining LLM Safety Under User Delusions and Distress](https://arxiv.org/abs/2606.00975)

**<font color=#1a73e8>作者：</font>** Andrew Aquilina, Chetna Nihalani, Vasudha Varadarajan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM chatbots increasingly serve as a first source of support for people in psychological distress, including those whose distress is entangled with delusional beliefs. Prior work on LLM mental-health safety largely evaluates general therapeutic quality or single-turn crisis detection, leaving unclear how models behave when distress is intertwined with delusion over sustained conversations. We address this gap with matched multi-turn simulations, across clinically grounded personas and six LLMs, that pair each delusional conversation with a distress-only control to isolate the effect of delusional framing. This reveals a recognition-intervention gap: models detect distress at comparable rates regardless of framing, yet sharply fail to act on it once distress is embedded in delusion, with safety interventions suppressed by up to 4.5x. The failure tracks accumulated acceptance of the user's premises rather than emotional validation. Worse, the intuitive fix of prompting models to assess user distress backfires under delusional framing; only delusion-aware prompting with explicit response guidance closes the gap, and even this depends on a delusion classifier that is itself unreliable on the most vulnerable models. Safe deployment therefore requires treating delusional framing as a distinct risk signal that overrides conversational accommodation.

---


### 152. [An Open-Source Benchmark and Baseline for Multi-temporal Referring Segmentation](https://arxiv.org/abs/2606.00987)

**<font color=#1a73e8>作者：</font>** Bingyu Li, Da Zhang, Tao Huo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have shown strong visual understanding and language-guided grounding abilities, yet their capacity for multi-temporal visual reasoning remains underexplored. To bridge this gap, we introduce \textbf{Multi-temporal Referring Segmentation (MTRS)}, a new task that aims to segment language-described temporal changes from multi-temporal images. MTRS extends conventional referring segmentation and change detection by jointly requiring temporal correspondence reasoning, language grounding, and pixel-level mask prediction. We propose \textbf{CRAFT-Agent}, an automated data construction pipeline with human auditing, and build \textbf{MTRefSeg-21K}, the first MTRS benchmark, containing 21K high-quality multi-temporal image-text-mask triplets across diverse scenes, viewpoints, and domains. Benchmarking a broad set of VLM- and LVLM-based models reveals that direct inference performs poorly, while task-specific fine-tuning remains limited. To address this, we propose \textbf{MTRefSeg-R1}, a change-aware LVLM framework trained with a two-stage strategy. It first learns general temporal-change perception from 20K vision-only bi-temporal samples, and is then fine-tuned on MTRefSeg-21K for fine-grained language-guided temporal localization. MTRefSeg-R1 explicitly models cross-temporal visual differences, aligns language instructions with temporal variations, and predicts referred change masks. Extensive experiments show that MTRefSeg-R1 achieves strong and often superior performance compared with existing LVLM baselines, demonstrating the challenge and potential of MTRS.

---


### 153. [Large Language Models in Transportation Systems Management and Operations: From Text Reasoning to Multi-modal Decision Support](https://arxiv.org/abs/2606.00991)

**<font color=#1a73e8>作者：</font>** Siyan Li, Zehao Wang, Jiachen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transportation systems management and operations (TSMO) increasingly depends on timely interpretation of heterogeneous data, from various sensor streams, incident reports, traveler feedback, and visual observations. Large language models (LLMs), including emerging multi-modal large language models (MM-LLMs), provide a new mechanism for integrating these structured and unstructured inputs into operator-facing decision support. This survey paper reviews LLM- and MM-LLM-based applications in TSMO across three domains: transportation operations & services (supply), mobility & fleet services (demand), and data, modeling & decision support. Using a PRISMA-guided screening process, we synthesize current studies while distinguishing operationally oriented applications from prototype and emerging concepts. We further identify recurring challenges in data heterogeneity, real-time inference, explainability, multi-modal fusion, and governance. Finally, we outline existing gaps and future directions in localized adaptation, edge deployment, benchmarking, and cross-agency collaboration. Overall, LLM-based systems appear most promising as a decision-support layer, with MM-LLMs offering particular value when heterogeneous text, visual, and sensor inputs must be integrated.

---


### 154. [A Registry-Bound LLM Pipeline for Evidence-Grounded Trait Extraction across Tropical Plants, Aquatic Species, and Exotic Pets](https://arxiv.org/abs/2606.00994)

**<font color=#1a73e8>作者：</font>** Jeff Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe a registry-bound large-language-model extraction pipeline producing evidence-grounded structured trait records at scale, on cultivated tropical plant, aquatic, and pet species. Four mechanisms render LLM-derived rows auditable: a versioned 39-key closed-vocabulary trait registry constraining every admitted value to a typed schema; a per-row verbatim evidence quote tying each value to source text; a per-row confidence label (high or medium; low dropped pre-persist); and multi-version preservation. Applied to 409,880 publishable species from the Tropical Species Encyclopedia, the pipeline executed 706,220 runs and persisted 5,489,881 trait records across 409,820 species (99.985%), 81.57% at high confidence. We report three validation layers in descending evidentiary strength: at full population, 90.12% of 5,427,588 evidence-bearing rows have their quote as a verbatim source substring (93.49% excluding one compliance meta-trait); a quote-supports-value audit on n=100 stratified non-red-zone rows yielded 100/100 (lower bound 96.30%); face-validity on n=50 red-zone rows yielded 50/50 Accept (lower bound 92.86%). Per-record correctness is not claimed; 100% pending human curation. The contribution is the four-mechanism framework.

---


### 155. [Decoding in Order-Agnostic Language Models: Chain-Rule Deviation and Uniform Spreading](https://arxiv.org/abs/2606.00997)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Order-agnostic language models (OALMs), including discrete diffusion language models (dLLMs), are trained to predict masked tokens under arbitrary conditioning sets, allowing sequences to be generated or scored under arbitrary reveal orders at inference time. In LLaDA-2.1, we report three findings. First, the learned conditionals are not exact factorizations of a coherent joint distribution: changing only the reveal order shifts target log-likelihood by up to 0.49 nats/token, so likelihood alone mixes content difficulty with path-dependent artifacts. Second, although confidence-first (CF) decoding is order-agnostic, its reveal orders are close to left-to-right (L2R) on content tokens. Third, we propose a complementary diagnostic based on the shape of the confidence trace. A uniform-spreading theorem shows that, at fixed total likelihood, target recoverability is maximized when per-step confidence is spread uniformly; the resulting deviation motivates $\mathrm{Var}(\log q_t)$ as a diagnostic for comparing decoding paths. Across C4 and four downstream benchmarks, low variance separates structured paths from random ordering, and variance is consistently associated with downstream correctness. These results support reporting mean confidence and confidence variance jointly when comparing OALM decoding paths.

---


### 156. [Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference](https://arxiv.org/abs/2606.01007)

**<font color=#1a73e8>作者：</font>** Zhiyao Xu, Aoxue Liu, Zhanjie Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsely activated Mixture-of-Experts (MoE) models scale capacity via conditional computation, but distributed inference suffers from cross-GPU expert communication and routing-induced load imbalance. Existing placement methods reduce this cost by co-locating frequently co-activated experts; however, they derive a single deployment plan from globally aggregated routing traces, thereby averaging away the heterogeneous, task-specific co-activation patterns that actually drive communication in multi-task serving. We observe that expert co-activation is strongly task-conditioned: pairs tightly coupled in one task family are often uncorrelated in another, so effective deployment should group experts by task-aware co-activation rather than by a task-agnostic average. Based on this insight, we propose \emph{Task-Aware Coactivation Grouping} (TACG), a deployment-time framework that uses family-specific dispatch and co-activation traces to derive per-expert task-family preferences, reweights the co-activation graph so that intra-family locality dominates grouping, and assigns each expert to a primary GPU under exact capacity constraints. To keep the static placement robust under online workload skew, we further introduce \emph{Generic Expert Shared Replication} (GESR), a lightweight companion that identifies generic experts with consistently central co-activation profiles, replicates them across a small set of secondary GPUs, and applies locality- and load-aware selection at serving time. Experiments on three representative open-source MoE models demonstrate that our framework reduces the average communication cost by 31.39\% over the baseline, while preserving an average Jain fairness index of 0.9975. This advantage persists even under severe distribution shifts in the inference data, consistently outperforming strong baselines.

---


### 157. [Property Prediction of Stacked Bilayer Materials: A Multimodal Learning Approach](https://arxiv.org/abs/2606.01012)

**<font color=#1a73e8>作者：</font>** An Vuong, Minh-Hao Van, Chen Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI for materials science is a critical topic within AI for science, aiming to accelerate materials discovery and produce accurate property predictions. Bilayer 2D material stacking is essential for exploring new materials with novel functions and inherent phenomena, enabling the creation of new 2D bilayers for diverse real-world applications. Research on bilayer vdWs materials has made significant progress from experimental and computational perspectives. Various bilayer materials have been successfully synthe sized experimentally and the increasing utilization of high-throughput computing technology has con structed several computational two-dimensional materials databases. However, the use of AI to model bilayer stacking and predict new properties remains underexplored, necessitating further research studies. In this work, we propose a novel multimodal learning approach to study the interfaces between dissimilar materials that jointly enable new or multiple functions, and to predict new properties arising from the vertical integration (stacking) of different functional material layers under given configurations. Comprehensive experiments demonstrate the effectiveness and efficiency of our approach compared to baseline methods. Our code is available at this https URL ml.

---


### 158. [PolySpeech-100: A Large-Scale Benchmark for Speech Understanding Across 100+ Languages and Dialects](https://arxiv.org/abs/2606.01016)

**<font color=#1a73e8>作者：</font>** Sicheng Yang, Shulan Ruan, Shiwei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While End-to-End (E2E) Speech-Large Language Models (Speech-LLMs) are rapidly evolving, their evaluation methodologies remain limited to the era of simple transcription. Existing benchmarks suffer from three critical limitations: a pronounced bias towards high-resource languages, a focus on low-level recognition (ASR) rather than semantic reasoning, and a neglect of regional dialects. To bridge this gap, we introduce PolySpeech-100, a massive-scale benchmark designed to assess `native-level' speech comprehension across 110 linguistic variants. We employ a novel hybrid construction pipeline that augments gold-standard human recordings with instruction-driven synthetic speech, allowing us to cover 19 distinct Chinese dialects and over 80 low-resource languages. Extensive evaluation of 22 state-of-the-art models (including Gemini-3, GPT-Audio, and Qwen2.5-Omni) yields pivotal insights. First, we demonstrate that open-source E2E models outperform Cascade (ASR+LLM) systems on heavy dialects, proving that direct audio processing preserves critical paralinguistic cues and prosodic features (e.g., intonation, stress) that are often lost in standard transcription. Second, we reveal a significant performance gap: while commercial models maintain robustness, open-source models suffer catastrophic degradation on low-resource languages. Finally, counter-intuitively, we observe that under standard zero-shot settings, Chain-of-Thought prompting frequently degrades speech understanding performance for most evaluated models, revealing a potential modality alignment gap in current architectures. PolySpeech-100 establishes a rigorous standard for the next generation of inclusive, omni-capable Speech-LLMs. The data, demo, and code are publicly available at this https URL.

---


### 159. [Hybrid Verified Decoding: Learning to Allocate Verification in Speculative Decoding](https://arxiv.org/abs/2606.01019)

**<font color=#1a73e8>作者：</font>** Xin Su, Dawid Majchrowski, Fangyuan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) generation remains expensive because autoregressive decoding calls the model once for each new token. Speculative decoding reduces this cost by drafting multiple tokens and verifying them with the target model in one step, but its speedup depends on how many drafted tokens are accepted. Parameter-free draft sources can propose long continuations at low cost in structured and agentic workloads, yet a cache match that looks promising at one generation step may have low payoff at the next. We propose Hybrid Verified Decoding, which predicts the accepted length of a cache draft before verification and uses this payoff estimate to choose between cache verification and a model-based drafter. Across three LLMs and sixteen datasets, Hybrid Verified Decoding is especially effective on agentic workflows, where it outperforms EAGLE3 in every setting with a 2.73x average speedup. Our analysis shows how prompt structure creates cache opportunities, how high-payoff cache drafts concentrate in a small part of the draft space, and how payoff-guided selection reduces sequential decoding work, pointing to runtime draft selection as a promising direction for speculative decoding.

---


### 160. [ProductWebGen: Benchmarking Multimodal Product Webpage Generation](https://arxiv.org/abs/2606.01022)

**<font color=#1a73e8>作者：</font>** Zhihong Liu, Siqi Kou, Zheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crafting a product display webpage from a source product image, along with layout and visual content instructions, holds significant practical value for domains such as marketing, advertising, and E-commerce. Intuitively, this task demands strict visual consistency across product displays and high-fidelity instruction following to jointly generate renderable HTML code. These requirements on controllability and instruction-following are closely aligned with the core features of advanced multimodal generative models, such as image editing models and unified models. To this end, this paper introduces ProductWebGen to systematically benchmark the product webpage generation capacities of these models. We organize ProductWebGen with 500 test samples covering 13 product categories; each sample consists of a source image, a visual content instruction, and a webpage instruction. The task is to generate a product showcase webpage including multiple consistent images in accordance with the source image and instructions. Given the mixed-modality input-output nature of the task, we design and systematically compare two workflows for evaluation -- one uses large language models and image editing models to separately generate HTML code and images (editing-based), while the other relies on a single UM to generate both, with image generation conditioned on the preceding multimodal context (UM-based). Empirical results show that editing-based approaches achieve leading results in webpage instruction following and content appeal, while UM-based ones may display more advantages in fulfilling visual content instructions. We also construct a supervised fine-tuning dataset, ProductWebGen-1k, with 1,000 groups of real product images and LLM-generated HTML code. We verify its effectiveness on the open-source UM BAGEL. The data and code are available at this https URL.

---


### 161. [Revise, Don't Freeze: Sampler-Matched Training for Self-Correcting Masked Diffusion Language Models](https://arxiv.org/abs/2606.01026)

**<font color=#1a73e8>作者：</font>** Longxuan Yu, Shaorong Zhang, Yu Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) re-predict every position at each denoising step, but standard samplers commit tokens once revealed, leaving this revision capability unused. Existing approaches either add heuristic or learned mechanisms to revise committed tokens, or remask them back to [MASK] before re-predicting; a principled sampler that directly revises visible tokens without auxiliary modules remains underexplored. We introduce D3IM, a parameter-free sampler derived as a corrector-style reverse update that permits direct visible-to-visible revision without additional modules or auxiliary passes. D3IM also reveals a model-side obstacle we term preservation bias: the model tends to reproduce its own wrong committed tokens rather than correct them. We address this with SCOPE (Self-Conditioned On Prediction Errors), a lightweight post-training procedure that simulates D3IM's sampling process. On LLaDA-8B at 64 denoising steps, SCOPE+D3IM improves over the original LLaDA-8B with standard unmasking by +13.0 on GSM8K (68.3%), +4.8 on MATH-500 (23.6%), +15.3 on HumanEval (29.3%), and +10.4 on MBPP (30.8%), with gains that increase as more denoising steps are used on math and HumanEval.

---


### 162. [A Finite-Calibration Regime Map for LLM Judge Panels](https://arxiv.org/abs/2606.01034)

**<font color=#1a73e8>作者：</font>** Bin Zhu, Yanghui Rao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study when LLM judge panels should be calibrated with low-dimensional stackers versus joint output tables under finite human-label budgets. Low-dimensional stackers have small estimation cost but miss interactions, whereas joint-table calibrators can represent interactions but pay for cell counts and unseen patterns. We cast this tradeoff as a finite-calibration regime map and instantiate it as Finite-Calibration Panel Selection, a deployable validation selector over judge path, prefix size, and aggregator family with table and parametric estimation diagnostics. On RewardBench, LLMBar, SummEval, and Arena100K with a seven-judge pool including DeepSeek V4 Flash, scalar/reliability aggregation wins 16 of 20 real dataset--budget cells, indicating that current judge outputs are often additive or redundant. Controlled calibration-growth data show the complementary regime: additive labels remain scalar-favored, whereas a six-way interaction selects a larger joint table and its test MSE drops from 0.224 to 0.061 once unseen mass vanishes. Thus the practical question is not ``how many judges?'' but whether the next judge's information is estimable under the available human labels.

---


### 163. [ExpWeaver: LLM Agents Learn from Experience via Latent RAG](https://arxiv.org/abs/2606.01041)

**<font color=#1a73e8>作者：</font>** Tao Feng, Tianyang Luo, Jingjun Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience learning has achieved promising results in enhancing LLM agent planning and reasoning by integrating past interactions as reusable knowledge. However, existing methods remain confined to explicit text space, retrieving experiences via semantic similarity and concatenating them into the context window, leading to substantial token overhead and a decoupled architecture that separates retrieval from generation. To address these limitations, we propose ExpWeaver, a framework that enables LLM agents to learn from experience via latent retrieval-augmented generation, without requiring a separate RAG module. ExpWeaver encodes experiences using the LLM's own hidden states, retrieves relevant experiences directly in latent space at each decoding step, and integrates them through cross-attention aggregation and gated residual mechanisms. The entire pipeline is optimized end-to-end with reinforcement learning, supporting both generative and ranking tasks. We evaluate ExpWeaver on 13 diverse tasks spanning question answering, reasoning, coding, scientific prediction, and recommendation. Results demonstrate that ExpWeaver achieves state-of-the-art performance on 12 out of 13 tasks, outperforming the strongest baseline by over 6.8%; maintains token efficiency comparable to non-retrieval baselines while text-based retrieval methods require 1.5 to 2 times more tokens; and exhibits superior cross-domain generalization, outperforming the strongest baseline by 16.32% under zero-shot transfer and 15.21% under few-shot transfer. Our code for ExpWeaver is released at this https URL.

---


### 164. [Plausibility Is Not Prediction: Contrastive Evidence for LLM-Based Cellular Perturbation Reasoning](https://arxiv.org/abs/2606.01042)

**<font color=#1a73e8>作者：</font>** Xinyu Yuan, Xixian Liu, Jianan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Perturbation experiments are central to understanding cellular mechanisms, but remain costly and sparse, motivating prediction of gene expression responses for unobserved conditions. A promising recent direction leverages large language models (LLMs) as "virtual cell" simulators-using stepwise, knowledge-grounded mechanistic reasoning to infer differential expression-pointing toward an interpretable, knowledge-driven paradigm that transcends purely data-driven approaches. However, we find that plausibility is not prediction: despite producing biologically plausible explanations, these methods fail to capture perturbation-specific effects: systematically overestimating differential expression, often underperforming a simple gene-frequency baseline in aggregate evaluations, and collapsing to chance-level performance at the per-gene level. This reveals a reliance on intrinsic gene response tendencies rather than true perturbation reasoning. We trace this failure to how evidence is presented: existing methods evaluate perturbation-gene pairs in isolation, without exposing how related perturbations differ in their effects on the same gene. To address this limitation, we introduce CORE (Contrastive Organization of Relational Evidence), which reframes prediction as a comparison task by organizing evidence into positive and negative outcomes from related perturbations. Using a biomedical knowledge graph for evidence retrieval, CORE improves calibration and substantially boosts perturbation-specific prediction in both LLM-based and non-LLM settings: for example, on drug-perturbation data, CORE-Reasoning improves Qwen3.5-9B aggregate metrics by up to 28.6%, while on generic perturbation data, CORE-Voting raises macro-per-gene AUROC from chance to 0.703 in average across four cell lines. This highlights contrastive evidence organization as essential to reliable LLM-based perturbation reasoning

---


### 165. [TravelEval: A Comprehensive Benchmarking Framework for Evaluating LLM-Powered Travel Planning Agents](https://arxiv.org/abs/2606.01046)

**<font color=#1a73e8>作者：</font>** Weiyi Chen, Shuaixiong Wang, Ziyun Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of Large Language Models (LLMs) has significantly improved travel planning applications, yet evaluating such models is limited by existing benchmarks' limitations: 1) overemphasis on constraint compliance, neglecting multi-dimensional qualities like spatio-temporal cost; 2) datasets lacking real-world authenticity and coverage in key areas (e.g., lodging, transport); and 3) isolated daily plan assessments that miss critical details (e.g., the impact of daily accommodation and visit pacing) needed for entire plan's evaluation. To address this gap, we introduce TravelEval, a realistic and comprehensive benchmark. TravelEval features 1) a novel six-dimensional evaluation framework to holistically assess plans across accuracy, compliance, temporality, spatiality, economy, and utility dimensions; 2) a highly realistic data sandbox with precise accommodation pricing and authentic intercity transportation data; and 3) a simulation-based global evaluation method that emulates complete travel plans with API-integrated geographic information and fine-grained queuing time. Evaluating 12 mainstream approaches with TravelEval reveals several valuable insights, such that LLMs struggle with globally-optimized multi-dimensional planning (especially in spatio-temporal reasoning and budget compliance), and agentic reasoning strategies offer no consistent improvement. Concisely, TravelEval facilitates travel plan evaluation via grounded spatio-temporal emulation and comprehensive metrics, providing a robust foundation for advancing LLM-powered travel planning research and applications.

---


### 166. [PMC-InterCPT: Rethinking Biomedical Interleaved Data for Multimodal Continued Pretraining](https://arxiv.org/abs/2606.01049)

**<font color=#1a73e8>作者：</font>** Guanghao Zhu, Zeyu Liu, Zhitian Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale biomedical image-text datasets extracted from scientific literature provide valuable resources for medical multimodal model training. These datasets are commonly organized as image-caption pairs; however, figure captions are often short, context-dependent, and only partially informative without the surrounding article text. At the same time, large-scale automatic extraction introduces structural noise such as missing captions, residual markup, duplicated context, and incoherent multi-paragraph figure descriptions. We revisit data construction for medical multimodal continued pretraining (CPT) and present PMC-InterCPT, a context-grounded biomedical interleaved corpus that incorporates figure-referencing body text in addition to captions. Our pipeline recovers missing captions, cleans caption and context text, reconstructs coherent interleaved image-text samples, and applies LLM-supervised medical relevance and quality classifiers to filter noisy records. We further reveal strong modality imbalance in the resulting corpus and introduce a four-bucket evidence taxonomy for modality-aware resampling. Through CPT followed by supervised fine-tuning (SFT) on Qwen3.5-4B-Base, PMC-InterCPT effectively improves medical and general multimodal performance while using fewer CPT tokens than the raw source pool. The experimental results also illustrate the complementarity between the data quality and modality for medical multimodal CPT.

---


### 167. [3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code](https://arxiv.org/abs/2606.01057)

**<font color=#1a73e8>作者：</font>** Yipeng Gao, Lei Shu, Genzhi Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural 3D modeling through code is emerging as a versatile paradigm, offering deterministic, engine-ready, and precisely editable assets that neural 3D generators inherently lack. Authoring such procedural content, however, demands deep expertise in 3D software APIs, parametric design, and code-level geometric reasoning. In this paper, we propose 3DCodeBench, a systematic benchmark for evaluating vision-language model (VLM) agents for procedural 3D generation in 3D modeling software. Specifically, 3DCodeBench evaluates how effectively 12 advanced VLMs can serve as procedural 3D modelers by translating text and image references into procedural code for 3D modeling software. Recognizing that automated metrics may not fully capture the perceptual quality of 3D shapes, we build 3DCodeArena, a ranking platform based on pairwise human preferences over generated 3D outputs. From extensive evaluations and results, we observe that: (1) Failures mostly arise from API mismatches, while successful renders still suffer from disconnected or floating 3D geometric components. (2) Test-time scaling, such as higher thinking budgets and multi-turn refinement, improves performance overall. Our findings highlight a critical need for high-quality procedural coding data to advance commercial VLMs. Furthermore, effective procedural 3D modeling requires a robust execution environment that provides high-fidelity feedback for iterative refinement. We release 3DCodeBench, including the curated large-scale dataset of multimodal (text/image) prompts, procedural code, 3D object triplets, evaluation protocol, and the public 3DCodeArena platform as a foundational toolkit for exploring VLM-based procedural 3D modelers.

---


### 168. [MENTIS: What Belief Changes Under Alignment? Measuring Multi-Scale Latent Torsion in Language Models](https://arxiv.org/abs/2606.01060)

**<font color=#1a73e8>作者：</font>** Partha Pratim Saha, Samarth Raina, Mayur Parvatikar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference alignment has substantially improved the observable behavior of large language models, yet it remains unclear what alignment changes internally. Aligned systems still fail under jailbreaks, prompt injection, and retrieval-time corruption, suggesting behavior-level evaluation alone is incomplete. Post-training should leave measurable traces in internal computation. We ask: when an instruction-tuned (IT) model becomes a preference-aligned (PA) model, what geometric structure changes, where do those changes concentrate, and how selectively do they vary across concepts, prompts, and model families?
We introduce MENTIS, a geometry-first framework for measuring alignment-induced internal reorganization in paired checkpoints. MENTIS compares IT and PA models using a primary layerwise covariance-based torsion norm (T1), a secondary spectral torsion diagnostic (T2), and an Energy-Radiance-Activation measure (ERA) for depth localization. Across four 7-8B model pairs on LITMUS, our study reveals that alignment-induced change is selective rather than uniform: normative concepts exhibit larger torsion shifts than factual concepts on average; torsion is negatively correlated with contextual entropy; and peak effects localize to architecture-specific mid-to-late layers. The same pattern appears across word-level, prompt-level, and model-level analyses. These results suggest preference alignment leaves structured, depth-localized geometric signatures in internal computation beyond what behavior-level evaluation alone can reveal.

---


### 169. [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](https://arxiv.org/abs/2606.01062)

**<font color=#1a73e8>作者：</font>** Jiarui Feng, Hanqing Zeng, Karish Grover 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have become a leading approach for decoupling parameter count from computational cost in large language models, yet effectively scaling MoE performance remains a challenge. Prior work shows that fine-grained experts enlarge the space of expert combinations and improve flexibility, but they also impose substantial routing overhead, creating a new scalability bottleneck. In this paper, we explore a complementary axis for scaling -- how expert outputs are aggregated. We theoretically show that replacing the standard weighted-summation aggregation with structural aggregation expands the expert-combination space without altering the experts or router, and enables possible multi-step reasoning within a single MoE layer. To this end, we propose DAG-MoE, a sparse MoE framework that employs a lightweight module to automatically learn the optimal aggregation structure among the selected experts. Extensive experiments under standard language modeling settings show that DAG-MoE consistently improves performance in both pretraining and fine-tuning, surpassing traditional MoE baselines.

---


### 170. [On the Generalization Gap in Self-Evolving Language Model Reasoning](https://arxiv.org/abs/2606.01075)

**<font color=#1a73e8>作者：</font>** Zhenting Qi, Susanna Maria Baby, Stefanie Anna Baby 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that large language models (LLMs) can improve through self-evolution (SE), using supervision signals generated by the model itself. In this work, we ask: under a strict closed-loop setup, where the self-evolution algorithm has access only to an unlabeled prompt set and a base model, how close can internally generated supervision come to oracle-supervised training? We analyze four representative strategies in a unified offline self-evolution framework: single-round verification, multi-turn revision with feedback, iterative training, and curriculum learning. Our primary experiments use Knights and Knaves (KK) logical reasoning tasks, which provide deterministic solutions, controlled difficulty levels, and a clean testbed for easy-to-hard generalization. We first show that self-evolution consistently improves over the base model, but plateaus after excessive training compute is invested, and eventually still leaves a non-trivial gap to oracle supervision. We find that multi-turn critic-revision with large models can reach strong self-evolution performance, with Gemma 12B nearly matching oracle-supervised training. Beyond Knights and Knaves, we also evaluate self-evolution on real-world reasoning benchmarks, where gains are also modest. Overall, our results characterize when closed-loop self-evolution can help and show how internally generated supervision remains insufficient under this minimal formulation.

---


### 171. [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091)

**<font color=#1a73e8>作者：</font>** Wangyi Mei, Zhouhong Gu, Zhenhan Bai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-ended reasoning and long-form generation tasks lack reliable automatic verification signals for reward-based policy optimization. Rubrics offer a promising alternative, but existing approaches treat them as given artifacts -- either hand-crafted or prompt-generated -- and often miss the task-specific, knowledge-intensive dimensions that matter most, distorting the reward signal. Our key observation is that rubric construction is itself a research problem: identifying what makes a response correct or insightful requires discovering and synthesizing external knowledge. We propose Deep Research as Rubric (DR-rubric), a two-stage framework for constructing such rubrics. Stage I elicits domain facts, structural constraints, and failure modes through iterative multi-turn agentic search; Stage II distills this evidence into atomic, independently verifiable constraints for GRPO-based policy optimization. Because the model under training can serve as its own rubric generator, DR-rubric-8B supports bootstrap rubric generation without frontier-model assistance. We evaluate on 6 benchmarks spanning agentic research and expert reasoning. Experiments show that DR-Rubric achieves strong competitive performance with only 1K -- 3K training instances, where GPT-5-generated rubrics particularly benefit breadth coverage on agentic tasks, Gemini-generated rubrics yield the most balanced performance across agentic and expert reasoning tasks, and bootstrap rubrics exhibit a specialization-to-rebalancing evolution achieving the best overall performance at the third iteration. Results demonstrate that reframing rubric construction from static evaluation templates into an evidence-driven research process yields more scalable, fine-grained reward signals for open-ended tasks.

---


### 172. [MiCU: End-to-End Smart Home Command Understanding with Large Language Model](https://arxiv.org/abs/2606.01099)

**<font color=#1a73e8>作者：</font>** Haowei Han, Kexin Hu, Weiwei Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Command understanding systems in smart home ecosystems can automate device control and substantially improve user experience. However, while they perform well on precise utterances (e.g., "turn on the bedroom light"), they struggle with ambiguous or misaligned commands (e.g., "make the bedroom cozy"). Large language models (LLMs) generalize well across various domains and can outperform traditional rule-based systems on such tasks, but their effectiveness is often constrained by scarce domain-specific data, insufficient task-specific adaptation, and high computational costs. In this paper, we propose an automated training data synthesis workflow using user logs and LLMs; then we build MiCU, a domain-specific LLM that excels at command understanding. Specifically, we employ curriculum learning to inject domain knowledge into the base LLM, then we enhance its reasoning ability via cold-start training combined with reinforcement learning (RL) guided by domain-specific thinking rules. Additionally, we introduce a token compression technique that condenses device description into a single special token, substantially reducing inference overhead and enabling \model-fast, an efficient variant optimized for long inputs. Extensive experiments show that MiCU significantly outperforms baselines, with an average accuracy gain of 20.01% across all device categories. We have deployed MiCU in the Xiaomi Home app, receiving approximately 1.7 million page views per day. Production evaluations show that MiCU reduces user correction rate by 1.57% and increases human audited accuracy by 32.05%. Our data and code are available at this https URL

---


### 173. [Soft-NBCE: Entropy-Weighted Chunk Fusion for Long-Context](https://arxiv.org/abs/2606.01101)

**<font color=#1a73e8>作者：</font>** Shihao Ji, Mingyu Li, Zihui Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic complexity of self-attention remains a bottleneck for Large Language Models (LLMs) processing ultra-long contexts. The Naive Bayes Cognitive Engine (NBCE) parallelizes long-context inference by chunking documents and routing to the lowest-entropy chunk at each decoding step. This hard-selection strategy causes semantic fragmentation during cross-chunk reasoning, as abrupt routing changes between adjacent tokens disrupt the model's contextual grounding.
We present Soft-NBCE, a lightweight extension that replaces discrete chunk selection with soft entropy-weighted chunk fusion. A temperature-scaled Softmax over predictive entropies assigns continuous weights to all chunks, enabling log-space aggregation across chunk-conditioned distributions. To partially compensate for the conditional independence assumption introduced by chunking, we propose Consistency Distillation, a LoRA-based self-distillation that constrains the chunked logit distribution toward a full-context teacher via KL-divergence. On LongBench multi-hop benchmarks, Soft-NBCE with Consistency Distillation improves consistently over NBCE-style baselines (MuSiQue F1: 0.310 vs.\ 0.275 for Vanilla NBCE; HotpotQA F1: 0.479 vs.\ 0.427) while maintaining retrieval accuracy (NIAH-32K: 0.909) at O(L^2/n) peak memory.

---


### 174. [Temporal Evidence Routing with Structured Visual Evidence for TimeLogicQA](https://arxiv.org/abs/2606.01106)

**<font color=#1a73e8>作者：</font>** Yuyang Sun, Yongliang Wu, Xingyu Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> TimeLogicQA evaluates whether video question answering systems can reason over temporal relations such as event existence, ordering, persistence, boundary conditions, and overlap. We address this task with a visual evidence routing pipeline that separates perception from symbolic temporal reasoning. The system first parses each question into event targets, answer mode, candidate options, and temporal operators. It then routes videos according to duration and operator difficulty, using ordered full-frame evidence for short clips and event-focused candidate windows for long videos. A multimodal large language model produces structured visual evidence for the relevant events, while programmatic verifiers recover dense action intervals and a deterministic reducer applies operator-specific temporal rules to produce the final answer. Conservative fusion accepts an answer only when the visual evidence, temporal program, and confidence checks agree, reducing noisy answer flips. On the official test evaluation, our final system achieves an AvgAcc of 81.8.

---


### 175. [Diagnosing LLM Arbitration Behavior over Pre-evidence Epistemic States in RAG-based Fact-Checking](https://arxiv.org/abs/2606.01120)

**<font color=#1a73e8>作者：</font>** Yuxi Sun, Wenbo Shang, Wei Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In RAG-based fact-checking, LLMs are increasingly used as verifiers to check given claims against retrieved evidence. Their parametric knowledge can induce pre-evidence tendencies that may conflict with the retrieved context, yet existing evaluation frameworks do not characterize such prior-context discrepancy or measure how verifiers arbitrate between parametric and contextual signals. We introduce \textsc{PAVE} (\emph{Prior-Aware Verifier Evaluation}), a diagnostic testbed that stratifies an LLM verifier into four epistemic states based on the correctness and confidence of its pre-evidence prior and evaluates its arbitration behavior on this new benchmark, i.e., whether it persists in correct prior under misleading evidence, and whether it corrects wrong prior when accurate evidence is provided. Experiments across seven LLMs reveal unreliable and highly model-dependent prior-context arbitration, highlighting the importance of verifier selection for real-world RAG-based fact-checking applications. Based on these findings, we propose a lightweight JSD-based test-time arbitration method that improves factual reliability without modifying the underlying model, achieving competitive performance across diverse LLM families.

---


### 176. [From Outliers to Errors: Auditing Pali-to-English LLM Translations with Multi-Reference Adjudication](https://arxiv.org/abs/2606.01136)

**<font color=#1a73e8>作者：</font>** Máté Metzger, Nadnapang Phophichit, Hansa Dhammahaso  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-score translation metrics can conflate legitimate variation with error, a problem especially acute for classical languages where multiple defensible English renderings of the same passage coexist. We audit Pali-to-English output from four flagship large language models (LLMs): GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro, and Grok 4.3, on 1,700 passages from the Pali Canon, using three established human translations by Bhikkhu Sujato, Thanissaro Bhikkhu, and Bhikkhu Bodhi as a local reference envelope rather than a single gold standard. Each candidate's normalized embedding drift from the reference centroid serves as a triage signal, not an error label; the 1,203 candidates above a 1.5 drift threshold are then adjudicated by a blinded three-model LLM judge panel, calibrated against a 300-instance author-adjudicated validation set. Two results stand out. First, drift predicts severity rather than error per se: the major-error rate among adjudicated high-drift candidates rose monotonically from 7.9% in the 1.5-2.0 band to 51.6% above 3.0, while approximately 80% of 1.5-2.0 outliers were judged valid translation variations. Second, model differences were clearest in the high-drift tail: GPT-5.5 had the lowest adjudicated high-drift major-error rate, with confidence intervals overlapping those of Claude Sonnet 4.6 and Gemini 3.1 Pro; Grok 4.3 had both the largest outlier volume and the highest tail major-error rate (27.6% overall, 74.4% above drift 3.0). The dominant major-error categories (e.g. omission or truncation, doctrinal term errors) are precisely the failures most likely to mislead readers of doctrinal text. The contribution is a reusable audit design for classical-to-modern translation: define a local reference envelope from multiple human translators, use embedding drift to prioritize review, and adjudicate the flagged tail rather than treating outlier status as error.

---


### 177. [SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision](https://arxiv.org/abs/2606.01139)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu, Zhaochen Su, Lingyun Xie 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are procedural artifacts that enable LLM agents to execute workflows, verify constraints, and recover from failures. Existing self-evolving methods refine skills using accumulated trajectories. However, they struggle in cold-start settings, where only an initial, imperfect skill is available. Consequently, skill construction defaults to expert authoring or one-shot LLM generation. Expert-authored skills are costly and may not align with how LLM agents actually execute tasks, while one-shot generated skills can be syntactically well formed yet behaviorally weak. To bridge this gap, we propose SkillRevise, an execution-grounded framework designed to iteratively refine these initial skills. SkillRevise diagnoses skill defects from execution evidence, retrieves relevant repair principles from a general memory, and applies execution-anchored edits. By re-executing candidates and measuring empirical utility, it systematically retains the optimal skill version. Evaluated across three benchmarks and five LLMs, SkillRevise substantially outperforms one-shot baselines, improving the base agent's success rate on SkillsBench from 36.05% to 61.63%. Furthermore, the revised skills exhibit strong cross-model transferability, capturing generalized procedural knowledge over model-specific artifacts.

---


### 178. [Reasoning4Sciences: Bridging Reasoning Language Models to All Scientific Branches](https://arxiv.org/abs/2606.01145)

**<font color=#1a73e8>作者：</font>** Teddy Ferdinan, Bartłomiej Koptyra, Mikołaj Langner 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Reasoning Language Models (RLMs) are rapidly emerging as powerful tools for scientific research, their impact is primarily concentrated in "hard science" fields. The slow -- or lack of -- adoption of RLMs in other branches of science is causing a widening gap in research productivity. In this survey, we provide the first comprehensive analysis of RLM adoption across 28 scientific disciplines following the classification used by the European Research Council (ERC), spanning the Social Sciences and Humanities, Physical Sciences and Engineering, and Life Sciences. We examine how RLMs are developed, evaluated, and applied across disciplines. Furthermore, we introduce a maturity-oriented assessment framework based on available domain-specific development and evaluation resources, revealing substantial disparities in RLM maturity that become even more pronounced when only publicly available resources are considered. Finally, we highlight current implementation paradigms that are gaining popularity across disciplines, current challenges, and future directions in enabling RLM adoption across science.

---


### 179. [When Data Is Scarce: Scaling Sparse Language Models with Repeated Training](https://arxiv.org/abs/2606.01155)

**<font color=#1a73e8>作者：</font>** Boqian Wu, Qiao Xiao, Patrik Okanovic 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws for dense LLMs under infinite data are well explored, but how sparsity interacts with limited data is not. In this work, we study sparse training in data-constrained regimes where limited unique tokens require multi-epoch training. Our experiments span models up to 1.92B parameters in the fitting set, sparsity up to 93.75%, unique data budgets up to 2.6B tokens, and total training tokens up to 41.6B over 16 epochs; we further validate extrapolation on held-out dense-equivalent models up to 7.68B parameters. We find that: 1. Sparse scaling in data-limited settings: We introduce a scaling law that models loss as a function of active parameters, unique tokens, data repetition, and sparsity, accurately predicting performance across compute and data budgets. 2. Delayed data saturation: sparse training postpones diminishing returns from repeated data, making multi-epoch training more effective. 3. Resource trade-offs: With fixed data, loss-optimal sparsity is moderate ~ 50%, while compute-optimal sparsity is higher and grows with data scale. Overall, sparsity is not just a tool for efficiency, but a mechanism for improving scaling trade-offs under data scarcity. Our code is available at: this https URL.

---


### 180. [Expected Value Alignment for Generative Reward Modeling in Formal Mathematics Verification](https://arxiv.org/abs/2606.01160)

**<font color=#1a73e8>作者：</font>** Shihao Ji, Haotao Tan, Zihui Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used with formal interactive theorem provers such as Lean 4. Scaling these systems with reinforcement learning or search methods requires process reward models (PRMs) that can evaluate intermediate reasoning steps. Existing reward-model designs expose a practical trade-off. Value-head models provide continuous scores but modify the generative model interface, while generative reward models preserve textual rationales but are poorly matched to continuous floating-point regression because numeric values are split across tokens. We introduce Expected Value Alignment (EVA), a reward-modeling procedure that keeps the surface output discrete while extracting continuous scores from the model's token distribution. The model emits integer scores in a structured JSON format, and EVA computes a continuous score as the expectation over the logits of the corresponding anchor tokens. Training combines the causal language modeling objective with an auxiliary mean squared error loss on these expected values. We instantiate EVA in \textit{Leibniz}, a reward model for Lean 4 formal verification, and evaluate it against zero-shot and reward-modeling baselines. The evaluation demonstrates that continuous logit-based scoring significantly reduces discretization artifacts while retaining the interpretability of generative critiques.

---


### 181. [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)

**<font color=#1a73e8>作者：</font>** Jiuming Liu, Chaojun Ni, Mengmeng Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI, autonomous driving, etc. Through explicitly incorporating user actions into world state transition, recent literature empowers world modeling with interactivity in an action-conditioned video or 3D generation paradigm, further enhancing controllability over world evolutions and facilitating users to freely traverse, manipulate, navigate, and personalize the state evolution. In this paper, we aim to systematically review recent research trends, technical developments, evaluation benchmarks, and also propose future potential directions in interactive world modeling. Specifically, we first summarize recent efforts and trends in terms of application scenarios, world state evolution, and scene modality. Afterwards, we delve into three crucial technical challenges, including action-conditioned controllability, long-horizon interactions and memory, and action-following responsiveness for real-time interactivity. Furthermore, we also thoroughly compare existing benchmarks and metrics in four specific application fields: open-world exploration, game engine, autonomous driving, and robotics. Finally, we discuss several promising future directions in achieving next-generation interactive world modeling. The corresponding repository is publicly available at: this https URL.

---


### 182. [Thinking Economically: A Hierarchical Framework for Adaptive-Complexity Reasoning in LLMs](https://arxiv.org/abs/2606.01168)

**<font color=#1a73e8>作者：</font>** Yubo Gao, Haotian Wu, Hong Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) has significantly enhanced LLM reasoning, yet often incurs substantial computational overhead due to "overthinking": generating excessively long rationales without commensurate accuracy gains. Existing efficiency methods typically apply uniform compression, which overlooks a critical observation that reasoning complexity is heterogeneous at two distinct granularity: across different problems and within individual reasoning steps. This motivates our principle of Thinking Economically: intelligently allocating computational resources based on intrinsic task and step demands rather than pursuing uniform brevity. We propose Hierarchical Adaptive Budgeter (HAB), a training framework that operationalizes this principle through coarse-to-fine budgeting. At the inter-step level, HAB predicts the optimal reasoning depth for each problem. At the intra-step level, HAB learns step-specific token budgeting signals from PPL-derived step comparisons and an adaptive Pareto optimization objective that captures the local quality-efficiency trade-off, while a Fisher Information-based pruner further provides fine-grained training-time guidance, thereby encouraging the generator to internalize more economical reasoning patterns. Experiments on GSM8K and MATH500 show that HAB not only surpasses standard CoT in accuracy but also reduces token usage, achieving a stronger performance-efficiency trade-off than the compared baselines.

---


### 183. [CA-BED: Conversation-Aware Bayesian Experimental Design](https://arxiv.org/abs/2606.01182)

**<font color=#1a73e8>作者：</font>** Daniel Arnould, Rashad Aziz, Zixuan Kang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel at static reasoning tasks, yet their performance often degrades in interactive scenarios where information must be actively acquired through questioning. A key challenge lies in selecting questions that reduce uncertainty while incorporating responses that may be ambiguous or only partially informative. To address this, we propose Conversation-Aware Bayesian Experimental Design (CA-BED), an inference-time probabilistic dialog planning framework that integrates Bayesian Experimental Design with LLM-based likelihood estimation to optimize question selection over multiple conversational turns. CA-BED maintains a belief distribution over hypotheses, anticipates possible answers, and propagates expected information gain through a simulated conversation tree. Across two structured entity-deduction benchmarks, CA-BED yields an average 21.8% improvement in success rates over direct prompting, with comparable gains relative to alternative information-seeking methods. It achieves these gains with an average increase of only 1.8 conversational turns compared to direct prompting.

---


### 184. [pcbGPT: Automatic PCB Schematic Synthesis from Natural Language Requirements](https://arxiv.org/abs/2606.01188)

**<font color=#1a73e8>作者：</font>** Tobias King, Steven Kehrberg, Michael Beigl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Translating natural-language hardware requirements into correct printed circuit board (PCB) schematics remains difficult in embedded, IoT, and wearable development. Designers must choose compatible components, interpret datasheets, add support circuitry, and expose correct interfaces before layout and prototyping can begin, while many such circuits cannot be validated through straightforward simulation. We present pcbGPT, a grounded system for generating editable KiCad schematics from natural-language specifications. pcbGPT represents circuits in a Python DSL and combines tool-augmented synthesis with component-library search, datasheet-grounded design knowledge, execution-based checking, structural and semantic validation, and an interactive web workflow that supports iterative refinement and synchronization with KiCad projects. We evaluate the system on 20 embedded schematic-generation tasks with reference implementations, required components, and interface constraints that enable automatic comparison. The best model reaches overall pass@1 of 0.90 and pass@5 of 1.00; pass@1 is 1.00 on basic and easy tasks, 0.91 on medium tasks, and 0.72 on hard tasks. These results, together with failure analysis, show that pcbGPT can already generate useful, reviewable first-draft schematics for early prototyping, but is not yet reliable enough to replace expert review.

---


### 185. [Can LLM Agents Sustain Long-Horizon Organizational Dynamics?](https://arxiv.org/abs/2606.01199)

**<font color=#1a73e8>作者：</font>** Xuancheng Zhu, Yang Yue, Shuaibing Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language agents are increasingly used for social simulation, yet it remains unclear whether they can sustain coherent behavior in structured organizations, where goals must propagate through hierarchy, tasks depend on prior execution, and artifacts accumulate over long horizons. We formulate long-horizon organizational simulation as a memory-centered coordination problem and introduce TaskWeave, a hierarchical agentic framework that maintains planning states through a Formulate-Partition-Diagnose-Align cycle and grounds execution through dependency-aware trace memory. We evaluate TaskWeave in a year-long IT company simulation and compare it with other multi-agent frameworks on organizational coherence, execution grounding, and downstream enterprise NLP utility. Experiments show that TaskWeave supports coherent and long-horizon organizational dynamics while producing grounded artifacts and adapting to external environments. These findings suggest that structured simulation memory is a key mechanism for building reliable LLM-based organizational simulators.

---


### 186. [The Shape of Wisdom: Decision Trajectories in Language Models](https://arxiv.org/abs/2606.01202)

**<font color=#1a73e8>作者：</font>** Shailesh Rana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models do not simply choose an answer at the output layer. In a 9,000-trajectory MMLU study across Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and Mistral-7B-Instruct-v0.3, the score of the answer moves across depth in structured ways. We describe each trajectory with three quantities: the current answer margin, the next-layer change in that margin, and the distance from a decision flip. The main empirical picture is that correctness and stability are different: the largest group is unstable-correct, not stable-correct. A traced subset then asks what moves the margin. In stable-correct cases, the average attention scalar points in the correct direction, while the average MLP scalar does not; span deletion shows that removing answer-supporting text hurts the margin and removing distractor-like text helps it. The result is not a full circuit explanation. It is a reproducible way to see which answers are settled, which remain fragile, and which measured sources move them.

---


### 187. [Implicit Geographic Inference in LLM Medical Triage: Language-Driven Disparities in Emergency Recommendations](https://arxiv.org/abs/2606.01204)

**<font color=#1a73e8>作者：</font>** Qi Han Wong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether large language models produce different medical triage recommendations for identical symptoms based solely on the language of the patient prompt. Using Gemini 3.5 Flash, we evaluate a neurological symptom profile (persistent headache, blurred vision, nausea) across six languages (English, Spanish, Chinese, Hindi, Japanese, Arabic) with 30 runs per condition (n=450 total API calls). We find that the model recommends emergency room visits at rates ranging from 0% (Japanese, Hindi) to 30% (English, Arabic), despite assigning nearly identical severity scores (7.7-8.0/10) across all languages. Adding a single sentence specifying the patient's US location increases ER recommendations by up to 76.7 percentage points for non-English prompts, while the reverse anchor (English prompt with a Tokyo location) reduces the ER rate from 30% to 6.7%. A back-translation control (Japanese to English) produces ER rates comparable to the English baseline, confirming that the disparity is not caused by translation quality but by implicit geographic inference from the input language. We release the complete dataset, experiment code, and results.

---


### 188. [Feature Alignment Determines Fusion Strategy: A Comparative Study of Cross-Attention and Concatenation in Multimodal Learning](https://arxiv.org/abs/2606.01207)

**<font color=#1a73e8>作者：</font>** Zhiqiang Zhou, Xuezhen Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The choice between cross-attention and concatenation for multimodal fusion remains governed by practitioner intuition rather than principled understanding. In this paper, we demonstrate that feature alignment quality, not data scale alone, is the primary determinant of which fusion strategy excels. Through controlled experiments on Flickr8k using two feature extraction backbones (ResNet18 and CLIP ViT-B/32), we show that concatenation outperforms cross-attention by 4.1-5.1 percentage points across all tested scales (2048-16384 samples) when features are pre-aligned by a vision-language pretraining objective. We provide a theoretical explanation grounded in sample complexity analysis: concatenation requires O(d_v + d_t) samples to learn its fusion projection, while cross-attention requires O(d_v * d_t) samples to learn bilinear attention weights, over 256 times as many for 512-dimensional CLIP features. When features are already aligned, the approximation error gap between the two methods vanishes, and concatenation's sample efficiency dominates at all practical dataset sizes. An alignment degradation study confirms a monotonic trend: as feature alignment degrades, concatenation's advantage grows from 1.3% to 2.8%. These findings provide a principled decision framework for fusion method selection in multimodal systems, with direct implications for the design of Multimodal Large Language Models.

---


### 189. [DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation](https://arxiv.org/abs/2606.01212)

**<font color=#1a73e8>作者：</font>** Yuyang Gong, Miaokun Chen, Jiawei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems are widely deployed and increasingly influential, but their reliance on external corpora exposes new security risks from poisoned retrieval content. Existing RAG attacks are largely focusing on individual queries or narrow topic-local query sets, which limits their practical reach and offers limited camouflage in real-world settings. In this paper, we introduce discourse-level opinion manipulation, a new threat model in which coordinated influence across a semantic query network induces opinion shifts over a holistic, multi-topic query space. We formalize this threat in a black-box setting and propose DiscourseFlip, an agentic, graph-guided attack that dynamically allocates a limited poisoning budget to maximize discourse-level opinion deviation. Extensive experiments demonstrate that DiscourseFlip consistently induces targeted opinion shifts across the contextualized query network and significantly outperforms existing baselines in terms of coverage and effectiveness. User studies further confirm that DiscourseFlip is effective while remaining well camouflaged from user detection. Moreover, systematic analyses show that existing mitigation strategies are ineffective against discourse-level manipulation, underscoring the urgent need for more robust and adaptive defenses to address discourse-level vulnerabilities.

---


### 190. [Distilling Neuro-Symbolic Programs into 3D Multi-modal LLMs](https://arxiv.org/abs/2606.01215)

**<font color=#1a73e8>作者：</font>** Wentao Mo, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current 3D spatial reasoning methods face a fundamental trade-off: neuro-symbolic 3D (NS3D) concept learners achieve interpretable reasoning through compositional programs but are constrained to closed-set concept vocabularies and simple programs; end-to-end 3D multi-modal LLMs (3D MLLMs) could handle complex natural language and open-vocabulary concepts but suffer from black-box reasoning without explicit spatial verification. We introduce APEIRIA, a neuro-symbolic 3D MLLM to bridge two paradigms by distilling symbolic reasoning patterns into MLLMs with natural language chain-of-thought. Our three-stage curriculum progressively builds reasoning capabilities: a) 3D perception alignment grounds object visual-geometric features to the LLM, b) CoT-SFT teaches query decomposition and stepwise verification from symbolic program traces, and c) CoT-RL extends reasoning patterns to open-set concepts and deeply nested instructions. By transferring reasoning patterns rather than concept-specific knowledge, APEIRIA preserves key NS3D virtues: transparent reasoning and modular interchangeability of planning and perception components. Evaluations on grounding, question answering, and captioning show that APEIRIA surpasses prior NS3D methods and matches state-of-the-art 3D MLLMs on 3D spatial reasoning datasets, unifying symbolic methods' systematic reasoning with MLLMs' flexibility. Code is available at this https URL.

---


### 191. [Fine-Tuning Diffusion Models for Molecular Generation via Reinforcement Learning and Fast Sampling](https://arxiv.org/abs/2606.01220)

**<font color=#1a73e8>作者：</font>** Guang Lin, Shikui Tu, Lei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating molecules that simultaneously satisfy drug-like properties and conform to the 3D structure of a target protein is a core challenge in structure-based drug design (SBDD). Existing generative approaches, however, often rely on costly post-hoc processing during Sampling or require carefully curated datasets during training, yet still achieve modest gains. These limitations are especially pronounced in multi-objective settings, where balancing conflicting criteria remains a core challenge. To address these challenges, We propose FTDiff, a reinforcement learning fine-tuning framework tailored for diffusion-based molecular generation under structural constraints. To ensure stable and sample-efficient optimization, FTDiff adopts a group relative policy optimization (GRPO) style strategy. Furthermore, FTDiff builds upon a time-free pretrained diffusion model and incorporates a fast sampling mechanism that reduces the number of denoising steps, significantly accelerating both training and inference while maintaining generation quality. By optimizing a fixed threshold-aware reward, FTDiff effectively guides the model to produce valid, diverse, and high- quality molecules that balance multiple drug design objectives. Extensive experiments on benchmark datasets demonstrate that FTDiff consistently outperforms prior methods, without requiring expensive post-hoc optimization or intricate data engineering.

---


### 192. [Advanced Mathematics Learning Behavior Prediction and Academic Early Warning Model Based on Multimodal Data Analysis](https://arxiv.org/abs/2606.01224)

**<font color=#1a73e8>作者：</font>** Liu Qiong, Li Zhengbo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early detection of at-risk students and timely academic intervention pose major challenges in advanced mathematics education, where complex conceptual hierarchies and nonlinear learning trajectories often hold back students' academic performance. This study adopts multimodal data analytics to build a dynamic framework for learning behavior prediction and academic early warning. It constructs a hierarchical knowledge graph ontology, realizes adaptive edge weighting according to problem difficulty and student performance, and combines heterogeneous graph attention with temporal sequence modeling to capture students' evolving knowledge states. Empirical tests on semester-long multimodal datasets prove that this method can accurately identify high-risk students and effectively track error propagation. Targeted interventions greatly improve students' knowledge mastery and reduce academic risks. The results verify that integrating knowledge graph analytics with multimodal temporal modeling can deliver more efficient and personalized learning support for advanced mathematics education.

---


### 193. [HomeFlow: A Data Flywheel for Smart Home Agent Training with Verifiable Simulation](https://arxiv.org/abs/2606.01230)

**<font color=#1a73e8>作者：</font>** Yi Gu, Huacan Wang, Shuo Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are moving beyond text-only interaction toward physical-world control, with smart homes as a representative domain. Real domestic interaction requires understanding ambiguous intents, operating in dynamic environments, and performing multi-turn reasoning. However, existing methods struggle to generate high-quality training data for smart home agents. We propose HomeFlow, a verifiable data flywheel for this domain. HomeFlow uses HomeEnv as a unified simulation environment and HomeMaker to procedurally generate diverse home settings. Subsequently, Blueprint compiles open-ended user intents into executable state-based success conditions, while MCTS-Flow synthesizes diverse, verifiable multi-turn trajectories through environment-guided tree search. We then optimize the agents via supervised fine-tuning and step-wise RLVE, which facilitates iterative improvement through authentic physical feedback. We further construct SmartHome-Bench to evaluate the agent across various smart home tasks. On this benchmark, HomeFlow-RL-4B and HomeFlow-RL-8B achieve task success rates of 84.60% and 87.03%. It is worth noting that HomeFlow-RL-8B even surpasses the leading GPT-5.5 by 1.23 percentage points.

---


### 194. [Brain-Atlas-Guided Generative Counterfactual Attention for Explainable Cognitive Decline Diagnosis Using Multimodal Connectomes](https://arxiv.org/abs/2606.01237)

**<font color=#1a73e8>作者：</font>** Xiongri Shen, Jiaqi Wang, Zhenxi Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mild cognitive impairment (MCI) and subjective cognitive decline (SCD) are closely associated with the early Alzheimer's disease continuum, where accurate and explainable diagnosis is important for early risk assessment and intervention. Existing connectome-based deep learning models can improve classification performance but often provide limited insight into disease-related functional and structural connectivity changes. This paper proposes an atlas-knowledge-guided Generative Counterfactual Attention-guided Network (GCAN) for explainable cognitive decline diagnosis using multimodal brain connectomes. GCAN formulates diagnosis as a source-to-target counterfactual generation problem, where target-label connectomes are generated from source-label inputs and their differences are used to construct counterfactual attention maps. To preserve connectome topology, an Atlas-aware Bidirectional Transformer (AABT) performs network-level token encoding and decoding under brain-atlas constraints. The framework is further extended from functional connectivity (FC) to joint functional and structural connectivity (SC) modeling, enabling counterfactual analysis of complementary functional reorganization and structural topology changes. Experiments on hospital-collected and ADNI datasets show that GCAN achieves competitive performance across HC vs. SCD, HC vs. MCI, and SCD vs. MCI classification tasks. Visualization, circular connectome analysis, CAM-based comparison, ablation studies, and confidence interval analysis further support the interpretability and reliability of the proposed framework. Modality-specific FC and SC pre-trained classifiers are used to provide target-state priors for counterfactual generation while being separated from the downstream diagnostic classifier to prevent data leakage.

---


### 195. [Efficient RAG with Intent-Aware Retrieval and Semantics-Preserving Chunking](https://arxiv.org/abs/2606.01240)

**<font color=#1a73e8>作者：</font>** Fachrina Dewi Puspitasari, Chaoning Zhang, Jiaquan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The demand for powerful instruction following and reasoning capability of large language models (LLMs) has promoted rapid development of retrieval-augmented generation (RAG). The RAG system assists LLM generation by retrieving chunks of query-fit supplementary knowledge from an external database. Conventional RAG systems, however, suffer from information insufficiency due to two factors, which are intent-agnostic retrieval and information fragmentation. Our work proposes a RAG framework, termed InSemRAG, that addresses these challenges via an iterative retrieve-and-check mechanism with two supporting modules, an intention-aware retriever (IAR) and semantics-preserving chunking (SPC). IAR implements a dynamic hybrid retrieval method that adaptively weights the retrieval channels based on the query intent, while SPC performs detection and reparation to the damaged evidence chunks to preserve the semantic integrity. To alleviate the computational latency brought by our iterative mechanism, we leverage small language models (SLMs). Extensive experiments across several benchmark datasets consistently demonstrate the competitiveness of our method against recent state-of-the-art RAG mechanisms. Particularly, our method achieves significant gains on multi-hop and evidence-sensitive tasks, with a 2.65-point improvement in F1 on HotPotQA and a 1.5-point increase in accuracy on FEVER. Our method also achieves competitive performance to Multi-Hop RAG with 4.32$\times$ lower latency with the utilization of SLM.

---


### 196. [Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration?](https://arxiv.org/abs/2606.01247)

**<font color=#1a73e8>作者：</font>** Liyang Li, Muzhi Zhu, Zhiyue Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can reproduce the viewpoint specified by a target image through active head and body motion, yet spatial intelligence in foundation models has largely been studied as passive understanding of pre-collected observations. We introduce Target Viewpoint Reproduction (TVR) -- an active task where an agent adjusts its viewpoint in a 3D environment until its observation matches a given target image -- and TVRBench, an indoor-simulation benchmark spanning scene scale and target-view visual richness. TVR is far from solved: on the evaluation split, the strongest open-source and closed-source models reach only 7.8% and 12.0% success. Fine-grained analysis identifies two consistent bottlenecks: off-the-shelf models struggle with multi-turn visual history, and performance drops sharply when viewpoint reproduction requires body translation rather than in-place rotation, exposing a gap in mapping spatial discrepancies to embodied movement. To study reducing this gap, we build a unified TVR post-training framework covering expert-trajectory SFT, rationale-supervised CoT-SFT, offline Single-turn GRPO, and on-policy Multi-turn GRPO from live simulator rollouts. Visual-action SFT supplies the main gain, raising a 9B open-source model to 50.8% success; Multi-turn GRPO provides targeted multi-room refinement and reaches 51.4% overall, while CoT supervision and Single-turn GRPO degrade closed-loop performance. These results establish TVRBench as a testbed for measuring and training foundation models that actively perceive and act in 3D environments. Our code, data, and models are available at this https URL.

---


### 197. [Trust Region On-Policy Distillation](https://arxiv.org/abs/2606.01249)

**<font color=#1a73e8>作者：</font>** Xingrun Xing, Haoqing Wang, Boyan Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) is a fundamental technique for efficient post-training of large language models (LLMs), with broad applications in agent learning, multi-task enhancement, and model compression. However, OPD training becomes unstable when the teacher and student distributions differ substantially, as teacher supervision on student-generated tokens may yield unreliable policy gradients and even cause optimization failure. This work addresses reliable on-policy token-level supervision through credit assignment strategies, and proposes Trust Region On-Policy Distillation, TrOPD. It features the following characteristics: 1) Trust-Region On-Policy Learning: TrOPD performs OPD only in regions where the teacher provides reliable supervision, mitigating the optimization difficulty of the K1 reverse-KL estimator under distribution mismatch. 2) Outlier Estimation: For outlier regions, we explore gradient clipping, masking, and forward-KL estimation to reduce the adverse effects of unreliable supervision. 3) Off-Policy Guidance: The student continues generation from teacher prefixes and uses forward KL to imitate off-policy guidance, encouraging on-policy exploration toward reliable regions. Experiments show that TrOPD consistently outperforms SoTA OPD baselines, including OPD, EOPD, and REOPOLD, across mathematical reasoning, code generation, and general-domain benchmarks.

---


### 198. [Understanding LLM Behavior in Multi-Target Cross-Lingual Summarization](https://arxiv.org/abs/2606.01252)

**<font color=#1a73e8>作者：</font>** Sangwon Ryu, Yihong Liu, Mingyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-target cross-lingual text summarization (MTXLS), which summarizes a source document into multiple target languages, is increasingly important as users consume content in diverse languages, but remains underexplored. To address this gap, we introduce multi-target cross-lingual element-aware (MEA), a new MTXLS benchmark covering 24 target languages. We benchmark end-to-end and pipeline approaches across various LLMs and show that MTXLS performance still substantially lags behind English monolingual summarization. To better understand MTXLS in LLMs, we propose a layer-wise analysis framework for investigating how LLMs internally perform MTXLS. Our analyses suggest that translation and summarization behaviors emerge jointly within later layers rather than as distinctly decomposed stages. Most task-relevant processing occurs within these layers, and errors also tend to arise at similar depths. Motivated by these findings, we introduce an inference-time activation steering method that leverages hidden representations from English summarization to guide MTXLS generation. Experiments show that our method consistently improves MTXLS quality across target languages.

---


### 199. [Agentic Clustering: Controllable Text Taxonomies via Multi-Agent Refinement](https://arxiv.org/abs/2606.01255)

**<font color=#1a73e8>作者：</font>** Simon Löwe, Emily Silcock  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent text-clustering methods use large language models to propose a cluster taxonomy from a corpus and then assign each text to it. These pipelines are fundamentally programmatic: the sequence of LLM calls and the rules for stopping, merging, and splitting clusters are fixed in code in advance, so they generalise poorly across corpora of different structure and cannot easily incorporate user-supplied constraints such as a target cluster count or a clustering intent. We propose an agentic alternative in which an orchestrator LLM inspects the state of the discovery process at each step and dispatches one of a small set of specialised agents - proposer, synthesizer, auditor, investigator, and critic - adapting the pipeline to the corpus rather than executing a fixed one. On seven public text-clustering benchmarks the method achieves state-of-the-art performance, beating the strongest prior LLM baseline by up to 32% in ARI.

---


### 200. [IndoBias: A Dual Track Culturally Grounded Benchmark for LLMs Bias Evaluation in Indonesian Languages](https://arxiv.org/abs/2606.01260)

**<font color=#1a73e8>作者：</font>** Ikhlasul Akmal Hanif, Muhammad Falensi Azmi, Filbert Aurelian Tjiaranata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite being home to more than 1300 ethnic groups and 700 indigenous languages, bias in Large Language Models has not been fully studied in Indonesia, thus leaving a critical gap in evaluating representational fairness and localized stereotypes within its uniquely vast, multilingual, and diverse sociocultural landscape. To address this, we introduce IndoBias as a culturally-grounded bias benchmark to assess LLMs bias in Indonesian and three local languages: Javanese, Sundanese, and Makasar. IndoBias features dual perspective evaluation tracks: depth-oriented (with contrastive-pairs) and breadth-oriented (with generation-based), where the latter is grounded in social science frameworks (SPI, O*NET, and WGI). Our results show that existing LLMs -- particularly decoder models -- exhibit strong bias towards prototypical sentences in Indonesian, while local languages suffer higher bias under Ideology and Religion category. We also find that LLMs responses exhibit a non-uniform Stereotype Polarity when prompted with various local entities. Finally, we discover that, in Indonesian, Common Crawl texts introduce more bias during pretraining, compared to human-reviewed article texts (e.g., Wikipedia, News), whereas introducing local languages to pretraining generally increases bias. This work highlights the importance of studying bias in culture-specific context. Warning: This paper contains example data that may be offensive, harmful, or biased.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
