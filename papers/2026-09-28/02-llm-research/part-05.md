# 🧠 大模型相关研究 | 2026年09月28日

> 本类共 **228** 篇论文：已确认 **208** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-228**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-228**

---

### 201. [SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance](https://arxiv.org/abs/2609.30192)

**<font color=#1a73e8>作者：</font>** Xinyue Zeng, Jiawei Zhang, Yujun Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon reasoning remains a central challenge for large language models (LLMs) under sparse-reward regimes. We argue that this brittleness arises from two biases induced by complex reasoning spaces: an exploration bias, where models are drawn toward locally plausible but structurally unstable branches, and a compounding bias, where small local deviations accumulate across depth and suppress rare rewards. We introduce Symbolic Closure Analysis (SCA) as a theoretical lens characterizing how branching structures and sparse rewards induce these biases in long-horizon reasoning with local admissibility, and as a design principle for structural priors in less formal reasoning tasks. Motivated by this analysis, we propose SAGE (Structural Admissibility-Guided Exploration), a unified framework that injects structural guidance to alleviate exploration bias and compounding bias in long-horizon reasoning. SAGE combines two complementary structural guidance: algebraic sparsification, which projects locally admissible candidates onto operator-indexed algebraic subspaces to suppress spurious branching and mitigate exploration bias, and hyperbolic structural guidance, which embeds reasoning states into a negatively curved space to provide dense depth-wise signals and mitigate compounding bias. Across 12 benchmarks and 7 model families, SAGE outperforms competitive baselines. In particular, SAGE achieves up to an 8-fold improvement on the Andrews-Curtis problem, an open real-world long-horizon task. Code is available at: this https URL.

---


### 202. [A Living Benchmark for Information Retrieval from Electronic Health Records](https://arxiv.org/abs/2609.30205)

**<font color=#1a73e8>作者：</font>** Jordan L. Cahoon, Chloe O. Stanwyck, Sulaiman Somani 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from patient records. Their safety and utility depend on rigorous evaluation, yet existing benchmarks are manually curated, costly to update, and rapidly become obsolete with evolving technological advancements. We present a scalable framework that automatically generates question--answer pairs from longitudinal EHR notes. Nineteen clinicians validate the benchmark generator, producing the Benchmark for Retrieving Information in EHRs (BRIE), a continuously maintainable evaluation dataset. Across nine LLMs and five inference strategies, state-of-the-art systems frequently omit clinically important information, particularly for questions requiring synthesis across multiple documents and encounters. Because the generator itself is validated, BRIE supports evaluations that static benchmarks cannot, including the generation of multiple answers that reflect variation in clinician reasoning for robust performance assessment and continuously refreshing benchmark content to guard against leakage. Our results demonstrate that scalable benchmark generation enables rigorous, up-to-date evaluation of clinical LLMs as they are deployed in rapidly evolving healthcare settings.

---


### 203. [The Alignment Illusion in Multimodal Large Language Models](https://arxiv.org/abs/2609.30210)

**<font color=#1a73e8>作者：</font>** Hong-Han Wang, Yuntao Wang, Hu Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interaction. To test this assumption, we apply controlled interventions to the visual stream. Across 13 MLLMs from five families spanning 0.5B to 72B parameters, replacing projector-output visual tokens with Gaussian noise sharply reduces task accuracy, yet four standard scalar measures (CKA, SVCCA, MIR, and the leading principal-angle cosine) fail to consistently separate the corrupted stream from the original. We call this failure the alignment illusion and trace it to the shared language-model pathway: anisotropic MLP down-projections pull visual and text tokens toward common output directions, producing weight-induced alignment. Because this component is essentially one-dimensional, we introduce the principal-angle gap (PA gap), defined as the difference between the top two principal-angle cosines, which separates weight-induced similarity from multi-directional visual structure. Under graded visual corruption, the PA gap tracks task accuracy more consistently than the scalar scores we consider; under a structured but irrelevant image, it further exposes regimes in which internal geometry and task accuracy come apart. Internal visual-text alignment in MLLMs is therefore best read as a geometric diagnostic of the visual stream inside the language model rather than a direct proxy for content-level cross-modal interaction, and is most informative when calibrated by controlled task evidence.

---


### 204. [Minimally Invasive Steering of Language Models](https://arxiv.org/abs/2609.30218)

**<font color=#1a73e8>作者：</font>** Taha Entesari, Jingyu Zhang, Daniel Khashabi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed through matrix--vector products with the frozen language-model head. We derive an exact decomposition of the sequence-level KL gradient into an analytic Fisher term and a suffix score-function term. For a fixed generation horizon, we show that the suffix term is second order in the steering magnitude and that three Fisher surrogates agree with the full KL gradient to first order. MISVO uses the frozen-reference surrogate to optimize position-specific interventions without updating model parameters. Across preference and code-generation tasks on models with approximately 1B--14B parameters, MISVO achieves the highest mean reward in six of seven model--task settings, with diversity and coherence scores close to those of Best-of-N.

---


### 205. [To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech](https://arxiv.org/abs/2609.30227)

**<font color=#1a73e8>作者：</font>** Debajyoti Mazumder, Mamta, Abhirama Subramanyam Penamakuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benchmark is designed to examine whether factual verification ability transfers from text to speech, and whether retrieval-augmented LALMs can use textual evidence to correctly support or refute spoken claims. Our experiments reveal a consistent text-speech modality gap: LALMs that verify written claims reliably often fail on the same claims when spoken. Moreover, retrieval alone provides limited gains because models frequently conflate retrieved evidence with the spoken claim. In contrast, retrieval combined with explicit reasoning improves claim-evidence comparison, with a thinking-tuned LALM reaching 86.1% accuracy. VeriSpeak highlights that effective speech misinformation detection requires not only speech understanding, but also grounded reasoning over retrieved evidence. The dataset is publicly available via Hugging Face at this https URL.

---


### 206. [OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction](https://arxiv.org/abs/2609.30234)

**<font color=#1a73e8>作者：</font>** Ding-Jiun Huang, Yuanhao Wang, Cheng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated generation of production-ready 3D garment assets from a single image is a central challenge in digital content creation. While recent generative models have significantly advanced 3D geometry reconstruction, synthesizing high-quality textures remains a bottleneck. Existing methods often bake environmental illumination and shadows directly into the texture map, or they fail to maintain global structural coherence, making the resulting assets unusable for physical simulation and relighting. In this work, we introduce OmniFabric, a novel approach that synthesizes globally coherent texture maps directly within the 2D sewing pattern space. Given a single reference image, our pipeline utilizes an estimated 3D mesh and generative priors of powerful Vision-Language Models (VLM) to establish a complete but coarse texture initialization across the unwrapped sewing patterns. We then leverage a specialized diffusion transformer, trained via an automated synthetic data engine and conditioned on 3D positional features, to refine this initialization directly in the canonical UV domain. This effectively removes distortion and baked-in artifacts to extract a clean and normalized texture map that preserves the original garment design. Extensive experiments demonstrate that OmniFabric significantly outperforms state-of-the-art baselines, yielding photorealistic 3D garments with high-quality textures.

---


### 207. [SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data](https://arxiv.org/abs/2609.30238)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Zhibin Wu, Chong Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent research on Multimodal Sentiment Analysis (MSA) has focused on learning from language, visual, and acoustic modalities with incomplete data to infer human sentiment. Most studies typically compensate for missing information by reconstructing modality features or designing complicated fusion mechanisms. However, these methods still suffer from spurious generation and noisy guidance due to the lack of high-level semantic grounding in partially observed multimodal evidence. To address these issues, we propose SemMSA, a latent semantic-aided framework that constructs rich sentiment-relevant semantics with LLMs, fully integrating with all modalities via anchor-free spectral alignment. It mainly consists of Cross-modal Semantic Refinement (CSR) and Cross-modal Spectral Alignment (CSA). Specifically, CSR first adaptively extracts visual and acoustic representations by corresponding adapters to form a unified multimodal prefix with language in the frozen LLM embedding space. It then iteratively produces continuous discriminative semantic states through a token-efficient latent refinement process without decoding explicit text. Next, CSA simultaneously aligns the refined semantics with all modalities by enhancing the dominant spectral component of their kernel Gram matrix. This captures global nonlinear dependencies among all representations without relying on a predefined anchor modality. In addition, an instance-level spectral separation constraint preserves cross-sample discriminability and mitigates representation collapse. Extensive experiments on SIMS, MOSI, and MOSEI benchmarks demonstrate that SemMSA achieves state-of-the-art performance.

---


### 208. [LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266)

**<font color=#1a73e8>作者：</font>** Jeremy Qin, David Schmotz, Derck Prinzhorn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that external attackers can exploit this gap to induce trace deletion. Finally, we show that trace tampering behavior emerges naturally in frontier models, when agents try to improve their rewards. We advise practitioners to ensure trace logging happens through an independent interception mechanism outside of the agent's control, preserving trace integrity even in cases of full host compromise. Overall, our findings identify a concrete failure of trace integrity in agent infrastructure which can be used to conceal misaligned behaviors like scheming or sabotage.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 209. [Privacy Leakage Through AI-mediated Analysis of Smartphone Data](https://arxiv.org/abs/2609.28537)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sarah Radway, Zoe Robert, Matthew Soto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Over the past thirty years, the online advertising industry built a large-scale data collection ecosystem, with the goal of tracking a user's online activity to infer their demographics and interests. Traditionally, the ecosystem relied upon the collation and analysis of highly-structured text data like user IP addresses, GPS coordinates, e-commerce purchase histories, and visited URLs. However, recent ML models can parse not only structured text, but also multimedia files and unstructured text inputs---meaning a user's photos, videos, inboxes, and calendars are now ripe for automated analysis. The privacy risks are particularly acute in the context of smartphone apps. A user's phone already acts as a natural collation point for sensitive user information, but users may not understand that permitting an app to, for example, access a user's photo does not just give the app access to the bytes in the photo: the app also receives access to inferences about the user that are enabled by the photo.
To explore these privacy risks, we built Priva-See, an LLM-based inference system for app-collected user data; Priva-See reflects our best understanding of how real-life adtech companies would leverage machine learning to build user profiles. Through an IRB-approved user study, 465 participants deployed Priva-See on their phones; Priva-See made privacy-invasive inferences despite having access to only a subset of a user's data. We see the experience significantly impacted participant willingness to share permissions data moving forward. Based on the observed privacy violations, we suggest changes to how smartphone OSes should gather user consent for data access, to better inform users about downstream data usage capability.

---


### 210. [TWIST: A Proposed Benchmark for Intervention Quality in Conversational Memory, with a Human-Validated Draft-Alignment](https://arxiv.org/abs/2609.28575)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Subrat Panda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-conversation memory benchmarks increasingly test recall and prompted knowledge updates, and recent work studies evolving user beliefs and memory state. TWIST is a proposed benchmark suite for a complementary, unmeasured property: intervention quality -- whether a deployed memory system, exercised through its own ingest/recall/vet surface, acts correctly at belief change points. Four tracks cover unprompted tension detection, vetting outgoing drafts against the record, answering with current beliefs while preserving supersession history, and governing sensitive recall. The suite extends LoCoMo's corpora and harness, pairing every detect/block metric with a matched do-not-over-detect control: surface-matched hard negatives price false intervention, so no track can be gamed by flagging everything. The benchmark itself is validated first: independent, gold-blind double annotation with adjudication, judge decoy calibration, and a separability audit. On the human-validated Track B v1.0 key (161 items, post-adjudication kappa = 0.85), no tested configuration simultaneously achieves high contradiction recall, high hard-negative specificity, and high attribution: flat-RAG baselines detect 0.76-0.97 of true contradictions but falsely flag 16-43% of surface-matched safe drafts depending on backend, while a deployed coherence-oriented system almost never over-flags (0.98-1.00 specificity) yet catches 42% of true contradictions -- a trade-off no recall-only score can see. A 13-configuration baseline ladder localizes causes: every gold contradiction is detectable from its evidence alone (recall 1.000), calibrated models nearly solve the track given the full transcript -- consistent with substantial retrieval-coverage gaps -- and draft-only floors reveal model-dependent style priors. A system's TWIST profile, beside its recall score, measures whether memory knows when to intervene and when not to.

---


### 211. [Time-Series Foundation Models That Understand Data Revisions](https://arxiv.org/abs/2609.28576)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taimoor Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Historical observations are not always fixed: statistical agencies revise previously published values as new evidence arrives. Forecasting from a contemporary download can therefore expose a model to information unavailable at the date it purportedly made a prediction. We propose VINTAGE-TS, a revision-aware adaptation of a time-series foundation model that distinguishes observation time from information-availability time. Its targets are the next period's first-published value and the value available a fixed number of days after that publication; neither is declared final truth. A joint predictive distribution preserves dependence between these targets and exposes uncertainty about their difference. We specify an ALFRED-based rolling evaluation, a matched Chronos-2 comparison, conventional and revision-aware baselines, and a separate audit of pretraining overlap. The accompanying software implements validity-interval reconstruction, delayed-label filtering, a frozen-backbone adapter interface, and reproducible diagnostics. An executed synthetic demonstration and a 25-configuration sensitivity suite verify the workflow, expose variation across seeds and revision regimes, and illustrate how hindsight contamination changes measured performance. Thirty one automated tests check temporal and integration contracts. Real ALFRED and Chronos-2 experiments have not been executed; no empirical foundation-model advantage is claimed.

---


### 212. [SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models](https://arxiv.org/abs/2609.28582)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xin-Yu Hu, Shuang Liang, Cheng Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent emergence of Time Series Foundation Models (TSFMs) has significantly advanced multi-step forecasting performance, enabling accurate predictions over extended future horizons. However, existing TSFMs often suffer from significantly inherent uncertainty, which typically manifests as derived forecast branches emerging at each time step and spreading to subsequent steps; different forecast branches often exhibit varying forecasting performance, thereby undermining the credibility of TSFM forecasts. In this paper, we propose the Slicing-Graphing-Alignment (SGA) method to quantify the uncertainty of multi-step TSFM forecasts. The proposed SGA first characterizes the topology of all potential forecast branches using a directed acyclic graph, such that the graph complexity bounds the uncertainty of multi-step forecasts, and then precisely measures the graph complexity by integrating both topological information and TSFM-inherent stochasticity. Experimental results conducted on 11 TSFMs and 27 datasets demonstrate that (i) SGA achieves the best performance when ranking predictive errors with uncertainty estimates; (ii) SGA works with a more extensive and more precise sampling coverage than those of existing UQ methods, deriving a quantification mechanism fundamentally different from those of established ones; and (iii) larger model scales of TSFMs correlate with lower uncertainty estimates of multi-step forecasts, suggesting another empirical scaling law for uncertainty quantification of multi-step TSFM forecasts.

---


### 213. [UltraBench 2: Towards Robust Evaluation of Vision Foundation Models on Ultrasound](https://arxiv.org/abs/2609.28610)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashwath Radhachandran, Adam Tupper, Christian Gagné 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarking is an increasingly critical part of research in machine learning and the domains where it is applied, including healthcare. Yet, despite the steady development of new ultrasound foundation models in recent years, the development of well-designed benchmarks to evaluate them has lagged behind. This deficiency has led to fragmented and inconsistent evaluations of competing models, making it difficult to measure progress. To address this issue, we introduce UltraBench 2, a comprehensive benchmark with wide anatomical and task coverage, and a focus on standardization, reproducibility, and ease-of-use. Using this benchmark, we compare existing vision foundation models for ultrasound image analysis. Our analyses demonstrate that ultrasound-specific pretraining still leads on classification, but that state-of-the-art general-purpose models have drawn level on segmentation.

---


### 214. [RLVR landscapes for iterated multiplications can be benign: Insights from spin-glass theory](https://arxiv.org/abs/2609.28625)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Noa Rubin, Zohar Ringel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the importance of reinforcement learning with verifiable rewards (RLVR), the extent to which it can learn new reasoning capabilities remains debated. Here we study the optimization landscape of RLVR on algorithmic tasks, such as iterated group and quasigroup multiplication. To this end, we map entropy-regularized RLVR over myopic tabular policies onto an energy-based (spin-glass) model over deterministic policies. This mapping upper-bounds what RLVR can achieve, and lets us rigorously characterize the landscape in this tabular setting. We show, both theoretically and experimentally, that for a wide class of models and tasks with uncorrelated inputs, this landscape is benign, containing no local minima that could trap RLVR training. Rather, the practical difficulty of these tasks appears to stem, at least in part, from issues such as diffusive barriers and gradient-estimation error in traversing the landscape. These are genuine obstacles that can prevent a solution from being found, but they are distinct from the landscape itself being rugged. We show that these obstacles can often be mitigated through the choice of entropy regulator. Consistent with this theory, we find that a transformer trained from scratch, using only last-token rewards, successfully learns an algorithmic chain of thought for iterated non-Abelian group multiplications.

---


### 215. [WildHSR: Metric Feed-Forward 4D People-Scene Reconstruction from a 3D Foundation Model](https://arxiv.org/abs/2609.29106)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jerrin Bright, John Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D foundation models recover video cameras and geometry in one forward pass, but some of the strongest are up to scale. Joint people-scene reconstruction then requires two missing outputs: metric scale and persistent person identity. We ask whether one up-to-scale foundation representation can support both through lightweight adaptation. Exact metric labels are scarce, but unlabeled in-the-wild video is abundant. We use people in curated web video to initialise the solution: a posed metric body and 2D keypoints give an approximate, closed-form scale pseudo-label. These pseudo-labels pretrain a Scale Readout, which is then fine-tuned together with a lightweight adapter using exact metric supervision from standard real-video training splits. At inference the head predicts metric scale from foundation-model tokens, without the ruler or its teachers. For person identity, we probe the pretrained foundation model alone and find evidence that its intermediate query-key features encode person correspondence across frames. In most evaluated moving-person clips, a mid-layer token prefers that person over the vacated location and other people. A tiny projection reads this correspondence; together with metric pelvis motion and proposal confidence, it drives dustbin-aware Sinkhorn association of per-frame bodies. WildHSR combines both readouts to reconstruct metric cameras, scene and people from monocular video. Each window is predicted feed-forward; analytic association and Sim(3) composition connect windows. On EMDB-2, WildHSR is the first feed-forward method in the published comparison to beat the best optimization-based WA-MPJPE and RTE while leading feed-forward methods on all three world-frame metrics. On RICH, it leads feed-forward people-and-scene methods on WA-MPJPE and W-MPJPE. The complete pipeline runs at 10.1 fps on one GPU.

---


### 216. [Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD](https://arxiv.org/abs/2609.29142)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yibo Zhao, Zixuan Yang, Yunshi Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct On-Policy Distillation (Direct-OPD) transfers reinforcement-learning-induced policy improvements from a small model to a larger student by using the token-level log-ratio between post-RL and pre-RL checkpoints as dense supervision on the student's own rollouts. This transfer rewards the policy shift at every state, yet the log-ratio measures only relative change: it can stay fixed even as the probability mass that both checkpoints assign to the student's candidate tokens vanishes. Through an exact construction, we show that the Direct-OPD reward and its update can remain unchanged while the Jensen-Shannon divergence (JSD) and both KL directions between the checkpoints vanish with this mass, and we note that a small JSD bounds how much the teacher's behavior changed. Motivated by this analysis, we propose Selective Supervision for Direct-OPD (S$^2$D-OPD), which ranks student-sampled states by their teacher-reference JSD and masks Direct-OPD supervision at low-divergence states, retaining only the top 10% of states per response. Across two teacher pairs and four student models ranging from 1.7B to 8B parameters, S$^2$D-OPD improves held-out accuracy over dense Direct-OPD on AIME and HMMT benchmarks in seven of eight settings and matches it in the eighth, without extra forward passes. Our code is available at this https URL.

---


### 217. [ICE: Task-Aligned Clifford Latent Fields for Multimodal Graph Foundation Models](https://arxiv.org/abs/2609.29398)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xunkai Li, Xu Wang, Yinlin Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal attributed graphs connect entities, visual content, language, and observed relations. Learning one foundation across such graphs requires more than compressing each node into a fused Euclidean vector. The representation must preserve entity semantics, construct interaction state from graph neighborhoods, and expose that state to prediction units with different geometry. Our empirical study shows why these requirements are inseparable. Higher-grade channels recover pair relations across the foundation graphs, specialized queries reveal information hidden by a generic readout, and rigid blade isolation removes cross-grade capacity. We therefore introduce ICE (Interaction-aware Clifford Encoder), a multimodal graph foundation model built on a node-indexed Clifford latent field. Topology, text, and images enter explicit Cl(3) addresses. Edge-aware geometric products transform these directions into scalar, bivector, and trivector relations over observed neighborhoods. A protected Grade-1 route preserves entity semantics, while the full grade and depth bank remains available to fresh node and link heads. We establish exact cross-grade reachability, node-permutation equivariance, and a bound on the task residual around the semantic score. Experiments span one shared foundation over eleven graphs, six node-classification datasets, three link-prediction datasets, and matched few-shot tasks. ICE ranks first in all 30 reported supervised and few-shot comparisons. Core removals reduce every task summary, and mechanism controls connect the gains to higher-order transport, retained multidepth structure, semantic protection, and direct field access.

---


### 218. [Towards Trustworthy Biological Alignment in TabPFN-Probed Pathology Foundation Models](https://arxiv.org/abs/2609.29523)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ushashi Bhattacharjee, Alloy Das, Saria Hannan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Histology and transcriptomics provide complementary views of tissue biology, capturing spatial morphology and molecular activity, respectively. Pathology foundation models (PFMs) learn rich morphological representations from H&E images, yet strong downstream performance alone does not establish whether these representations encode biologically meaningful and robust molecular information. We present a **training-free framework for auditing biological alignment in frozen PFMs** using spatially paired histology and transcriptomics from HEST-1k, evaluated on **240 samples spanning three organs**. Multiple frozen PFMs are used to extract H&E representations, while gene expression is aggregated into biologically interpretable pathway-level programs. We use TabPFN as a pretrained probe to quantify the extent to which these molecular programs can be decoded from frozen image representations without task-specific gradient updates. Beyond predictive performance, our audit examines whether pathway decodability generalizes across tissue sections, patient groups, and tissue types; whether representations exhibit section-level or other shortcut dependencies; and whether predictions remain stable under small image perturbations and context resampling. This multi-tissue evaluation distinguishes molecular programs that are consistently encoded from those that are tissue-specific, unstable, or shortcut-sensitive. Our framework therefore provides a systematic approach for assessing not only **what biological information pathology foundation models encode, but also how reliably that information persists under clinically relevant sources of variation**.

---


### 219. [Safe Skill Retirement for Physical Agents](https://arxiv.org/abs/2609.29543)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhonghao Zhan, Xiao Ma, Hamed Haddadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills bundle procedural guidance with execution conditions governing authority, user consent, and live environment state. When model capabilities advance, maintainers prune instructions that appear redundant on authorized benchmark tasks. However, authorized maintenance tests can leave dormant safety conditions untested. This mismatch creates an unmeasured support gap over physical and privacy-sensitive effects. We introduce matched authority counterfactuals that hold the requested action, tool parameters, and intended effect fixed while systematically varying a single governing predicate. We formalize this evaluation via a two-gate retirement certificate requiring a candidate reduction to preserve authorized utility within a declared margin while producing zero unauthorized protected effects. In controlled experiments spanning four frontier and local model configurations across twelve skill bundles (2,592 evaluation cells), task-certified reductions remove over 94% of skill clauses and preserve authorized completion, yet produce unauthorized protected effects in every bundle. Boundary enforcement eliminates protected effects on the declared audit but fails the utility gate for one configuration. One bounded combined protocol passes both gates across all four configurations, with zero utility headroom. An end-to-end check on one read-only Home Assistant camera chain verifies proposal, decision, and effect measurements on a real device. These results demonstrate that while task benchmarks can justify retiring procedural guidance, retirement decisions require explicitly auditing the authority contracts governing physical actions.

---


### 220. [ModularSQL: A Runtime Guardrail for the Multiplicity Blind Spot in Text-to-SQL](https://arxiv.org/abs/2609.29573)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianxin Zhou, Ruixi Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems are increasingly deployed on production databases, where queries that pass benchmark evaluation can still produce results that distort downstream workflows. Standard set-based execution accuracy (Set-EX) collapses duplicate rows and can therefore miss multiplicity errors, including missing DISTINCT, inflated aggregates, and Cartesian-style join explosions.
We call this the Multiplicity Blind Spot (MBS) and introduce Multiset-EX, a multiplicity-preserving evaluation criterion that exposes such failures. Across released DeepEye-SQL artifacts from three backbones (Qwen2.5-Coder-32B, Qwen3-Coder-30B-A3B, and Gemma-3-27B) on executable BIRD-Dev N=1532, we find a consistent 5.81--6.79 pp gap between Set-EX and Multiset-EX. The gap is not specific to DeepEye-SQL: it persists on released DAIL-SQL+GPT-4 (5.22 pp) and BIRD GPT-3.5-turbo (3.39 pp) predictions.
We further introduce ModularSQL, a lightweight post-selection runtime guardrail that probes executed results for multiplicity anomalies and applies deterministic patches or low-cost LLM rescue only to flagged queries. Integrated with DeepEye-SQL using Qwen3-Coder, ModularSQL preserves Set-EX at 72.06% while improving Multiset-EX from 65.86% to 67.75% (+1.89 pp). It flags 77 high-risk anomalies, while adding only $0.0076 in total LLM cost and 120 ms amortized latency per query. Cross-pipeline evaluation shows that the candidate-free detector and deterministic patches also transfer to independently released prediction sets. Overall, these results show that benchmark accuracy does not necessarily imply execution-safe SQL, and that lightweight, multiplicity-aware runtime guardrails can narrow this gap with modest computational overhead.

---


### 221. [AgentKernel: The Trust-Native Agentic Operating System](https://arxiv.org/abs/2609.29647)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenhua Zou, Sheng Guo, Qiuyang Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI agents routinely cross trust boundaries: they ingest untrusted content, combine it with privileged instructions, persist intermediate beliefs in long-term memory, and invoke privileged tools. This creates an attack surface in which malicious payloads can enter through model inputs and cause harmful tool actions. Yet current governance stacks remain application-level middleware that share a process trust boundary with the agents they monitor. We argue that agents need an operating-system substrate providing mandatory, non-bypassable services for identity, input mediation, memory governance, and execution control.
We introduce AgentKernel, a trust-native agent operating system built around the premise that security must be a first-class design constraint. AgentKernel wraps the agent lifecycle in a mandatory enforcement boundary organized into four pillars: Identity, Perception, Cognition, and Execution. Each pillar adapts classical OS security principles to failures at the semantic plane, including delegation abuse, prompt injection, memory poisoning, and tool misuse.
AgentKernel treats structural security as a capability multiplier. Kernel-managed identity supports trustworthy cross-organization collaboration; graduated perception replaces brittle single-point filters; information-flow-controlled memory improves retrieval fidelity while limiting poisoning; and semantic-to-kernel enforcement permits broader tool privileges behind a non-bypassable boundary. We position AgentKernel as the missing OS layer beneath orchestration frameworks, agent runtimes, governance platforms, and execution sandboxes, and use systematic comparison and security analysis to show how a single integrated architecture can enforce security across the full agent lifecycle.

---


### 222. [Stochastic Semantic Evidence Graphs: Uncertainty Propagation and Governance for Agentic AI](https://arxiv.org/abs/2609.29703)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matthew Francis Dixon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-agent evaluations usually inspect a final answer, yet error may enter through evidence, retrieval, prompting, generation or decision mapping. We introduce a stochastic semantic evidence graph (SSEG), a hierarchical stochastic DAG whose language node expands into an autoregressive token subgraph and whose observable output may be a law over complete phrases. Semantic reduction and calibration are optional. We define graph-relative local defects and downstream edge influences, derive a pathwise bound on terminal error and use its nodewise terms to diagnose governance triggers. For source provenance, the graph preserves uncertain claim--passage relations and propagates sharp Fréchet bounds rather than assuming independence across sources. Across three open-weight architectures, information-equivalent changes materially alter complete-phrase laws. A controlled experiment yields no certificate violations in 5,000 cases; crossed-RAG and live Brave-retrieval experiments separate retrieval, presentation, source and interaction effects. SSEG therefore turns workflow provenance into a quantitative account of where uncertainty entered, how it propagated and whether an output is qualified for use.

---


### 223. [FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates](https://arxiv.org/abs/2609.29812)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wanqi Yang, Shiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers have attracted substantial attention as a parameter-efficient approach to increasing computational depth through repeated application of shared Transformer blocks. However, their practical advantages over conventional Transformers remain under debate: each additional loop incurs another Transformer pass and requires caching another set of KV states, causing inference FLOPs and KV-cache memory to grow continuously with loop depth. This overhead becomes particularly severe at large loop counts and long context, preventing the parameter efficiency of Looped Transformers from translating into practical inference efficiency. In this paper, we find that much of the additional computation and storage introduced by looping is redundant. As recurrence proceeds, state changes become increasingly concentrated on a small subset of tokens; attention-output differences are dominated by a sparse and stable subset of key columns; and KV residuals between adjacent loops become progressively more amenable to low-bit quantization. Building on these observations, we introduce FlashLoop, a training-free inference framework that reduces cross-loop redundancy through token-sparse updates, sparse attention, and KV-residual quantization. Across several Looped Transformers models, \textsc{FlashLoop} delivers lossless accuracy while achieving up to 1.64$\times$ end-to-end speedup and up to 6$\times$ KV-cache memory reduction, substantially improving the practicality of scaling Looped Transformers to greater computational depths and longer context.

---


### 224. [ENDOPROMPT: Victim-Side Pseudo-References for Utility Degradation](https://arxiv.org/abs/2609.29948)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qingyu Wu, Zeyu Feng, Yongda Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt injection can degrade benign task performance without eliciting harmful content. Yet many attack objectives depend on task labels or predefined target responses. We present ENDOPROMPT, a white-box method that learns utility-degrading prefixes from unlabeled instructions. Its generator takes the request text as input. Clean victim continuations serve as pseudo-references: local search identifies prefixes that reduce continuation likelihood, and preference fitting on comparisons within the same instruction, followed by reward refinement, distills this signal into a generator. At deployment, the generator produces one prefix per request without further victim-side search. Across four instruction-tuned models and the complete splits of seven benign benchmarks, ENDOPROMPT yields a mean utility change of -26.8 percentage points; 27 of 28 cells are negative. Failure analysis reveals output expansion and prefix reuse; the controls do not establish a degradation advantage from request matching. Victim-derived supervision can reveal utility weaknesses without benchmark feedback or prescribed failure responses. The code will be released upon acceptance.

---


### 225. [Guardrails or Roadblocks? Effects of Pedagogical Style and Context Awareness in AI Teaching Assistants for Programming](https://arxiv.org/abs/2609.29995)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Madeleine Eastwood, Harshith Narne, Joseph Hilby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI teaching assistants (AI TAs) backed by large language models (LLMs) and pedagogical guardrails are increasingly being integrated into programming courses, providing students with scalable access to hints, conceptual explanations, and code-level feedback. However, guardrails may also create friction. If students feel that the support provided is overly restrictive or poorly contextualized to their current progress, they may bypass approved tools for general-purpose LLMs. To investigate how AI TA design affects students' learning experiences, we conducted a randomized controlled trial with 132 students in an introductory programming course. Students completed three tasks related to code-writing and debugging and were randomly assigned to one of four AI TAs varied across two dimensions: pedagogical guidance style (Socratic vs. Direct instruction) and context awareness (no context vs. full context of the problem and student solution). We examined students' perceptions, interaction behaviors, and evidence of post-task comprehension. Students rated the Socratic AI TA with full context least favorably, reporting significantly lower perceived support for task completion. Descriptively, this condition also showed the highest observed interaction stress, the highest rate of external LLM use, and the lowest proportion of post-task explanations demonstrating full comprehension, though these differences were not statistically significant. These findings suggest that guardrailed AI TAs are not automatically better for learning. Instead, their effectiveness depends on how pedagogical guidance and contextual awareness are balanced in ways that students experience as useful, supportive, and worth continuing to use.

---


### 226. [Self-Play Pretraining with Zero Data](https://arxiv.org/abs/2609.30063)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aditya Cowsik, Kfir Dolev, Michael Y. Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in language modeling have been driven by scaling pretraining on ever more data. Yet, the training data is still largely curated on the model's behalf. A more general approach to pretraining would let the model learn to generate the data most useful for its own improvement. This would provide an effectively unbounded source of training data, limited by compute rather than human knowledge. We introduce Self-Play Pretraining with Zero Data, an initial proof-of-concept towards realizing this vision. Our procedure casts synthetic data generation as a search over the space of all computable structure, taking inspiration from Solomonoff induction. Starting from random initialization, two models learn in tandem: a generator proposes programs interpreted by a universal Turing machine, generating byte sequences, while a learner autoregressively predicts these byte sequences. The learner is trained with standard cross-entropy, while the generator is trained with reinforcement learning to produce sequences at the frontier of the learner's capabilities, yielding an adaptive curriculum. A universal Turing machine gives us a search space over all computable data-generating processes, imposing little domain-specific structure, and self-play searches over this space for useful training data. We test whether zero-shot performance on natural data improves predictably with self-play compute; this is a clean test of transfer since neither generator nor learner is trained on natural data. Across several natural datasets, zero-shot loss exhibits predictable scaling in compute. The models also exhibit in-context learning, and discover recognizable mathematical sequences during training.

---


### 227. [Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure](https://arxiv.org/abs/2609.30217)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary tasks. We introduce EvasionBench, a benchmark of 50 diverse task-policy pairs in which completing the task requires an operation prohibited by a runtime monitor. Agents know that their tool calls are monitored and are prompted to continue working when they pause. Across our evaluations, best-of-3 evasion attempt rates reach up to 98% and success rates up to 88%, with substantial variance across models. Claude Fable 5.1 succeeds less often, but frequently makes creative attempts to circumvent the monitor. Evasion generally increases with test-time compute, with higher evasion rates at greater reasoning effort and token use. Traces show that agents encode prohibited commands, decompose operations across tool calls, and retry until relevant context leaves the monitor's history. We also find that GPT-6 Astra's low evasion rate comes with overrefusal, as it frequently abandons otherwise solvable tasks under a denial-of-service prompt injection. Our findings show that ordinary task pressure can lead to adaptive attempts to evade runtime monitors without an explicit adversarial objective. Effective oversight must therefore remain robust against repeated attempts, as the persistence that helps agents solve difficult tasks can also drive them to circumvent their guardrails.

---


### 228. [WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yubo Zhu, Yawen Shao, Ziyun Dai 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions, the textual prompt largely directs the production, planning how actions, camera trajectories, lighting, and sound unfold across multi-shot sequences. In this paper, we present WanPE, a 397B-parameter prompt enhancement model trained on 1.05M real-world videos to master director-level cinematic planning. WanPE formulates shot-level cinematic plans via video-grounded reverse construction and employs Semantic-Consistency GRPO (SC-GRPO) to faithfully preserve user requirements across shots and over time. To benchmark this capability, we curate WanPEval, a human-annotated testbed covering durations from 5 to 30 seconds across varying intent granularities, supported by approximately 11K blind pairwise assessments. When powering Wan3.0's video generator, WanPE-397B boosts human preference over raw user prompts by 10.66-18.84 points at 5-15 seconds and by a dramatic 50.86 points in the 30-second arena. Ablation studies show that reverse construction demonstrates clear superiority over forward rewriting, while SC-GRPO robustly preserves semantic fidelity across model scales. Ultimately, WanPE leads all evaluated commercial offerings at 5-15 seconds and remains competitive with Seedance 2.5 at 30 seconds.

---


> [!TIP]
> 当前位于：**201-228**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-228**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
