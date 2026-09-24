# 🧠 大模型相关研究 | 2026年09月25日

> 本类共 **172** 篇论文：已确认 **158** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-172](./part-04.md)

---

### 101. [NS-ATTENTION: Newton-Schulz Transformations of Attention Outputs in Vision Transformers](https://arxiv.org/abs/2609.27735)

**<font color=#1a73e8>作者：</font>** Xiaohe Jiang, Guoqiang Zhang, Tianjin Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Newton-Schulz (NS) iteration has recently been used in the Muon optimizer to transform update matrices during the training of large language models. Motivated by its spectral effect, we investigate applying NS directly to Transformer attention representations. We introduce Newton-Schulz Attention (NS-Attn.), a parameter-free transformation applied to the output of each attention head. Each head output is arranged as a feature-by-token matrix and normalized by its Frobenius norm. We then apply a finite NS polynomial step and restore the original norm. The objective is to reduce spectral concentration and increase effective rank before standard head merging and output projection. Across ViT and Swin on CIFAR-10 and CIFAR-100, NS-Attn. improves final-epoch accuracy in all 12 matched-seed comparisons, with mean gains of 0.25--0.83 percentage points. ViT ablations show higher mean accuracy with one iteration than with two. Spectral analysis further shows reduced leading-eigenvalue concentration and increased effective rank. These gains incur additional inference latency.

---


### 102. [Evaluation of pre-trained models for pedagogical assessment of novel AI-assisted educational questions](https://arxiv.org/abs/2609.27749)

**<font color=#1a73e8>作者：</font>** Michael Lawrence Castanares, Princess Ventures, Allan Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The surge in AI-assisted generation of educational materials has outpaced our capacity to validate their pedagogical quality. Automated evaluation using Bloom Classifier models is a promising approach to assess educational materials at scale. These models show high accuracy within-distribution dataset (IID Dataset). However, applying the same models to new out-of-distribution (OOD) datasets such as AI-assisted generated questions could show performance degradation. To identify robust classifiers under dataset shift, we evaluated traditional Machine Learning (ML), transformer, and Large Language models on the Bloom level classification task. We also explored feature-engineering strategies incorporating NLP metrics, appending the learning objectives as part of the input, and text splicing to stabilize OOD performance. Our baseline tests show that TFPOS-IDF ML models perform poorly on OOD (Macro F1-score 0.48) compared to BERT (0.55) and LLMs (0.79). Text splicing improved macro F1-score performance of ML and BERT models (0.59 and 0.62, respectively). Appending the learning objectives with the input increased model performance on specific dataset. Model retraining provided the largest improvement across models and datasets. Overall, these findings highlight the trade-off on the use of pre-trained models with novel AI-assisted educational questions and how strategic feature enhancements help address loss in performance.

---


### 103. [AWM-VLA: AlignedWorld Modeling for Efficient and Explainable Vision-Language-Action Policies](https://arxiv.org/abs/2609.27753)

**<font color=#1a73e8>作者：</font>** An Lanji, Dawei Liu, Jin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models have become a powerful paradigm for generalist robotic manipulation, yet they are often reactive: the policy maps the current observation directly to an action chunk without reasoning about the long-term consequences of its decisions. Prior attempts to endow policies with world models either reconstruct future frames in pixel space---expensive and dominated by task-irrelevant detail---or decouple the world model from the policy, weakening control. We present AWM-VLA, a unified framework that embeds aligned world modeling directly inside a diffusion-transformer policy. Following the Future Latent REpresentation Alignment (FLARE) principle, we add learnable future tokens whose intermediate activations are aligned with vision-language embeddings of future observations, enabling the policy to anticipate long-term consequences while generating actions. We extend this paradigm in two ways. First, we introduce an object-centric decoupled alignment objective that predicts future object-level semantics alongside the global future embedding, improving both interpretability and multi-instruction generalization. Second, we balance the global and object-centric alignment terms against the action flow-matching loss through a principled weighting, yielding a controllable accuracy--interpretability trade-off. On RoboCasa and humanoid tabletop manipulation benchmarks, AWM-VLA outperforms prior VLA and world-model baselines by up to 21% in success rate, improves generalization to novel objects and instructions, and produces object-centric rationales that are preferred by human raters in 83 of cases. Our approach adds only a few learnable tokens to the policy and is compatible with any diffusion or flow-matching policy, making aligned world modeling an inexpensive, broadly applicable component of generalist manipulation.

---


### 104. [Reporting Under Pressure: Separating Factual and Tonal Sycophancy in LLM Statistical Analysis](https://arxiv.org/abs/2609.27756)

**<font color=#1a73e8>作者：</font>** Paras Balani, Subhrakanta Panda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly asked to analyze data and report what the results mean, a task distinct from the belief- or preference-alignment settings studied in most sycophancy research. We test whether editorial framing in the prompt, ranging from a neutral request to an explicit instruction to search exhaustively for reasons to discredit or to support a finding, changes not just the tone but the substance of a model's report. Across a 4 x 4 factorial design crossing four framing conditions with four ground-truth data patterns (a genuine effect, a confound that mimics an effect but fails a robustness check, a well-powered null, and an underpowered null), we collect 480 responses and score each along two independent dimensions: whether its factual claim about the data diverged from the correct interpretation, and whether only its tone diverged while the claim stayed correct. Factual misrepresentation is concentrated in two cells: brutally critical framing applied to a genuine effect, where the model talks itself into unwarranted skepticism (97% of responses), and significance-seeking framing applied to an underpowered null, where the model overstates confidence in a null conclusion the data cannot support (100% of responses). Tone shifts far more broadly than factual content does, with critical framing producing a defensive, hedge-heavy register across every data pattern regardless of what the data show, while significance-seeking framing shifts tone only where the data leave genuine ambiguity. A confound present in the data itself blocks both kinds of shift almost entirely under every framing condition tested. These results indicate that the risk of framing-induced distortion in LLM-assisted data analysis is neither uniform across framings nor uniform across data patterns, and that a model can hold a correct conclusion in place while its tone shifts substantially around it.

---


### 105. [Hard Negatives Reveal What Easy Negatives Hide: Cross-Lingual Harmfulness Representations Degrade with Resource Tier Under Hard Negatives](https://arxiv.org/abs/2609.27758)

**<font color=#1a73e8>作者：</font>** Paras Balani, Subhrakanta Panda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models is trained primarily in English, and recent work reports that the underlying harmfulness representation survives translation: English-trained probes separate harmful from harmless prompts almost as well in low-resource languages as in English. This has been taken as evidence that cross-lingual refusal failures mainly reflect calibration rather than representation quality. We show that this conclusion depends on the choice of negative examples. Across nine languages spanning three resource tiers, we replicate near-perfect transfer (AUROC > 0.98) when harmless prompts come from an unrelated distribution (easy negatives). With XSTest contrast prompts, which are benign but surface-similar to harmful requests (hard negatives), transfer collapses in low-resource languages while remaining largely stable in high-resource languages. On Qwen2.5-7B-Instruct, mean AUROC drop increases from 0.003 in English to 0.017 in high-resource, 0.042 in mid-resource, and 0.276 in low-resource languages. The pattern replicates on Aya Expanse. Back-translation chrF controls and a matched-chrF comparison across three languages reduce the likelihood that translation quality explains the effect. The collapse remains after controlling for chrF (partial r = 0.70, p = 0.03). Tokenizer fertility correlates with the collapse and explains part of the resource-tier effect, but not all of it. The results show that easy-negative transfer can coexist with substantial degradation under hard negatives. Easy-negative evaluation alone therefore cannot establish that the harmfulness representation survives translation.

---


### 106. [Improving LLM-based Autonomous Web Agents with Filtering](https://arxiv.org/abs/2609.27770)

**<font color=#1a73e8>作者：</font>** Zhitong Guo, Jing Yu Koh, Ruiyu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous web agents, powered by Large Language Models (LLMs), have garnered significant attention for automating various web-based tasks with multi-step reasoning and decision-making capabilities. An open research question in the development of these agents lies in the format of the webpage input. Raw HTML source code, with its extensive and often irrelevant details, poses difficulties for LLMs with limited context windows. To address this challenge, we first reproduce baseline models such as GPT-3.5 and LLaMA-2-70B on the WebArena (Zhou et al., 2023) benchmark, identifying common failure modes. We then propose two retrieval strategies to filter out irrelevant context for LLM agents. We develop DeBERTa-based and T5-based models that rank HTML elements by their relevance to the task. We fine-tune them on Mind2Web trajectory data and transfer them to WebArena. Experiments show that our DeBERTa-based model improves the success rate of the LLaMA-2-70B LLM agent on WebArena from 1.97% to 2.96%. Moreover, we develop a zero-shot ColBERT-based retriever that is able to retrieve the ground-truth element with a recall of 0.52 on Mind2Web and 0.47 on WebArena.

---


### 107. [Ask Which, Not How Good: Sizing Benchmarks Scored by an LLM](https://arxiv.org/abs/2609.27787)

**<font color=#1a73e8>作者：</font>** Atul Anand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks scored by an LLM judge routinely adjudicate differences of a tenth of a point, but the resolution of those benchmarks has never been measured. Existing sample-complexity work covers accuracy benchmarks and leaves the judged case open. Treating the system as the object of measurement, we decompose 373,019 judgments into system, item, judge and interaction components using generalizability theory.
The central result is structural: under a single judge, generalizability asymptotes to sigma2_s/(sigma2_s+sigma2_sj) regardless of item count, because the system-by-judge term carries no n_i. Items saturate; judges do not. The item cost of a target diverges as the target nears that ceiling.
The ceiling is a property of pointwise rubric scoring, not of LLM judging. Run as a pairwise preference in both presentation orders, sigma2_sj falls two orders of magnitude below sigma2_s and the ceiling rises to 0.986 (bootstrap [0.934, 1.000] on 11 systems), so one judge suffices. Pairwise buys a different problem: a system presented first wins 8.6 percentage points more often than the same system presented second, a bias 1.23x the median improvement claimed in the 53 published win-rate comparisons we recovered. Protocol design dominates panel size.
Measured floors are 0.41-1.24 points on a 0-5 scale at native item counts, against a median reported improvement of 0.28 points; on the one benchmark recurring often enough for an exactly matched comparison, all 17 recovered MT-Bench improvements fall below MT-Bench's own floor, and 70% of the win-rate claims fall below the pairwise floor.
An audit of 628 arXiv papers, double-coded by two independent models and validated against blind human coding (kappa=0.73), finds fewer than one paper in four states whether its evaluation was run more than once, and only 46-67% report uncertainty of any kind.

---


### 108. [LabourCrew: A Multi-Agent RAG Framework for Trustworthy Adversarial Deliberation and Statutory Reasoning over Labour Law](https://arxiv.org/abs/2609.27814)

**<font color=#1a73e8>作者：</font>** Fatema Tuj Johora Faria, Mukaffi Bin Moin, Jubayer Al Mahmud 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In statutory question answering, every claim must be traceable to evidence, not merely relevant, since unverifiable labour-rights answers carry serious legal consequences. Current systems fall short: single-pass RAG cannot detect insufficient evidence, while multi-agent legal-debate systems treat grounding as a prompting convention, letting agents cite unretrieved evidence. To address this gap, we introduce LabourCrew, a multi-agent RAG framework built around three grounding mechanisms: StatuteGraph, a graph index that explicitly links chapter, section, proviso, and cross-reference structure rather than fixed-length spans; an Evidence Exchange Protocol that confines advocates and an interpreter to an evidence ledger, making citation to unretrieved text impossible, while a fault-tolerant supervisor board runs advocates in parallel so individual failures degrade rather than crash the system; and a Calibrated Trust Gate that replaces categorical accept/reject decisions with a trust score, thresholded via conformal risk control for a distribution-free bound on the false-accept rate. We evaluate on LabourActQA, a 500-item Bangla question set from the Bangladesh Labour Act, 2006, spanning seven reasoning categories and three difficulty tiers. The framework drives the empirical false-accept rate to 0.081, within the target level ($\alpha = 0.10$), achieves the highest Answer Relevancy among HyDE RAG, Graph-RAG, and Hierarchical RAG (0.862 $>$ 0.839, 0.815, 0.828), and degrades gradually rather than catastrophically as question difficulty increases. These results show that calibrated abstention, not retrieval quality alone, is what makes legal question answering auditable in low-resource statutory domains.

---


### 109. [Groundbench: Multi-Resolution Polygon Grounding Exposes the Geometry Gap in Vision-Language Models](https://arxiv.org/abs/2609.27821)

**<font color=#1a73e8>作者：</font>** Zhonghan Bian, Zhenran Wang, Jinsong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bounding-box scores on RefCOCO-family grounding leave little room to distinguish frontier vision-language systems, yet boxes discard object shape. We introduce GroundingBench, a matched benchmark that re-targets the same 1,500 image-expression-referent triples to exact-N polygons at five vertex budgets. A fixed-denominator harness separately audits filled-region intersection over union (IoU) and legal-polygon completion. The strongest tested configuration reaches 88.2 box IoU and 97.1 accuracy at IoU >= .5 (Acc@.5), versus 57.7 and 69.2 for direct polygons; because these headline scores use different references, we also compare direct polygons with predicted boxes rasterised against the same contour target, obtaining 57.7 versus 57.3 when pooled. Performance is non-monotone in N and collapses at the densest budget, where legality failures compound residual geometric error. Qwen's thinking-setting contrast is the largest tested input-preserving configuration difference; under frozen templates, false spatial cues are more damaging than false colour cues, and target preference can remain high while contour tracing is poor. Alternate masks and a continuous-area scorer preserve the principal ordering. GroundingBench therefore measures an operational output-geometry gap spanning localisation, boundary construction, serialisation, and topology, rather than latent boundary perception alone.

---


### 110. [What Confidence Routing Is Actually Doing: Auditing Routing, Calibration, and Commitment in Multi-Agent Deliberation](https://arxiv.org/abs/2609.27822)

**<font color=#1a73e8>作者：</font>** Jingyan Jiang, Huihuo Zheng, Rajeev Thakur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A common multi-agent design asks agents to report confidence and lets the highest-scoring agent speak next, implicitly using one scalar both to route the conversation and to estimate uncertainty. We audit this confidence-routed broadcast protocol by separating three trace-level questions: whether it selects the right candidate (routing), whether reported confidence behaves like a probability (calibration), and whether the selected agent publicly states the answer that won the turn (commitment). Our primary study covers 4,181 gpt-oss-120b olympiad-math traces; we repeat the audit on a 2-by-2 actor-by-benchmark grid that adds gemma-4-31B-it and a biology multiple-choice benchmark. In the primary cell, confidence discriminates correct from wrong candidates (AUROC 0.72) but is strongly overconfident (79% mean stated confidence versus 52% accuracy). A cross-fitted, tier-stratified isotonic procedure reduces Expected Calibration Error from 0.278 to 0.008 on held-out candidates, but it does not recover missing discrimination: raw AUROC is only 0.537 and 0.440 in the two Gemma cells. Routing is likewise setting-dependent. Fixed routers differ by at most 1.1 percentage points on gpt-oss/math, whereas raw-confidence argmax performs 5.6 and 11.2 points below random-valid selection in the Gemma cells. Commitment is distinct again: in the primary cell, poll and spoken answers diverge in 20.4% of valid pairs, 62.4% of those revisions are fresh generations, and the unconditional correctness shift is -1.7 points; the other three cells instead range from +0.9 to +12.2 points. The transferable lesson is procedural: routing discrimination, probability calibration, and public commitment must be measured separately before raw confidence is used for deployment decisions.

---


### 111. ["AI Is Turning Too Human": How Teenagers Experience and Negotiate AI in Everyday Life](https://arxiv.org/abs/2609.27824)

**<font color=#1a73e8>作者：</font>** Jianfeng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI is rapidly entering adolescents' everyday lives during a critical period of cognitive, social and emotional development. Yet its adoption is outpacing evidence on how adolescents themselves experience, understand and negotiate its expanding role in their lives. We examined AI-related discourse on r/teenagers from January 2023 to July 2026 using validated keyword-based retrieval and a human-in-the-loop, LLM-assisted thematic analysis. AI-related discussion increased substantially over time, and 11,083 analytically coded posts revealed eight interconnected domains of experience. Everyday and social use was most prevalent (36.8 percent), while discourse increasingly shifted toward authenticity, personal control and safety, and future human roles. Across domains, adolescents questioned when AI should support or substitute for human thinking and creativity, how conversational AI changes relationships and perceptions of agency, what can still be considered authentic, who controls personal information and representation, and what opportunities and roles should remain human. These findings position adolescent AI use not simply as technology adoption, but as an emerging negotiation over AI's place and boundaries in everyday life. Supporting this transition will require developmentally appropriate AI literacy, psychological and social support, and AI systems and policies that protect adolescents' agency, privacy, relationships and opportunities for human development.

---


### 112. [Agentic Governance and Adversarial Verification for Policy-Constrained LLM Healthcare Appeal Generation](https://arxiv.org/abs/2609.27844)

**<font color=#1a73e8>作者：</font>** Harshil Lodhiya, Alex McManus, Reese Walker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claim denial management costs U.S. healthcare approximately $260 billion annually in administrative overhead. Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) can produce fluent clinical text, but single-agent architectures fail in high-stakes healthcare: they introduce unsupported clinical details and lose the logical structure of hierarchical payer policy. We propose AGVF (Agentic Governance and Adversarial Verification Framework), a multi-agent architecture for medical-necessity appeal generation under explicit policy and evidence constraints. AGVF models appeal synthesis as a Constrained Markov Decision Process (CMDP) over five agents: policy formalization, evidence retrieval, gap analysis, adversarial critique, and gated synthesis. We prove that refinement over a fixed policy constraint graph monotonically reduces evidence-deficiency and terminates with either a complete satisfying frontier or a localized evidence gap. A deterministic citation- grounding gate prevents assertions without admissible evidence from entering shared state. We provide a reference implementation and validate it on 1,000 synthetic appeal cases parameterized from de-identified public hospital discharge data. The validation confirms zero citation-grounding violations across all AGVF cases and monotone deficiency reduction in every episode; ablating the gate raises violations to 100%, confirming it is load-bearing. The study uses no real patient records and does not measure clinical efficacy. AGVF thus contributes a theory-backed agentic architecture and verified reference implementation for policy-constrained LLM generation in healthcare.

---


### 113. [Same Team Label, Different Evidence: A Full-Text Audit of Claim Denominators in Human-AI Teaming Research](https://arxiv.org/abs/2609.27849)

**<font color=#1a73e8>作者：</font>** Hanjing Shi, Kimberly Wang, Sabrina Doherty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI Teaming (HAT) reviews often group studies by labels such as advisor, teammate, or coordinator. Yet the same label can describe one person taking AI advice, several people coordinating around AI, or a workflow that distributes authority and responsibility. Pooling these studies can therefore change the human unit behind a claim.
We examine how full-text evidence changes the set of studies behind a claim. We audited 86 full texts purposively selected from a 419-record title/abstract map. We find that full-text reading changed core membership for 40 records: 36 of 74 apparent core candidates moved out, while 4 of 12 boundary candidates moved in. Team vocabulary did not reliably identify the social unit: 14 of 27 human-AI dyads and 20 of 23 multi-human peer teams used team or collaboration terms. Only 20 of 86 papers specified who could see AI output. Four blinded language-model runs unanimously labeled 53 screening cases and 59 arrangements, yet 32% and 34% of those consensus decisions differed from the full-text labels.
These results identify claim-denominator drift as a synthesis problem in HAT research. We contribute a full-text audit centered on human arrangements and a claim-pooling checkpoint for deciding when evidence about trust, coordination, performance, efficiency, and accountability can be compared.

---


### 114. [ChronosAttack: Adversarial Tool Scheduling Attacks on LLM Agents](https://arxiv.org/abs/2609.27857)

**<font color=#1a73e8>作者：</font>** Arash Vashagh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often process external tool responses as they arrive, making response timing part of the decision process. We introduce ChronosAttack, a delay-only scheduling attack that changes when authentic tool responses arrive without modifying, adding, removing, or accelerating them. Bounded delays can change the order of the same evidence and alter the final decision. We evaluate ChronosAttack on GPT-5.6 Sol, Gemini 3.6 Flash, DeepSeek V4 Flash, and Claude Sonnet 4.6. GPT-5.6 Sol and Claude show strong targeted shifts in vulnerable settings, Gemini shows large shifts in the opposite direction, and DeepSeek is more stable under the tested schedules. We also find that sequential agent state is not always required and that a single scheduling inversion can cause a large decision change. Synchronization and order-consistency defenses reduce attacker control over observation order. These results show that tool-response timing can itself form an attack surface in asynchronous LLM agents.

---


### 115. [RelCheck: Dual-Evidence Spatial Grounding for VLM Hallucination Correction](https://arxiv.org/abs/2609.27890)

**<font color=#1a73e8>作者：</font>** Siddhi Patil, Navrati Saxena, William B. Andreopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) fre- quently generate text that is inconsistent with the input image. While object- and attribute-level hallucinations have received considerable attention, relational hallucinations (incorrect de- scriptions of spatial or interactive relationships between objects) remain largely unaddressed by existing post-hoc correction methods. We present RelCheck, a training-free post-hoc correction pipeline that augments object-level visual grounding with dual relational evidence: learned scene-graph triples from RelTR and deterministic spatial predicates from bounding-box geometry. These combine with a Woodpecker-style object claim layer to form a three-layer visual knowledge base, which a language model corrector uses to rewrite hallucinated text. Evaluated on LLaVA v1 13B, RelCheck achieves a total MME hallucination score of 630.0 versus 585.0 for a Woodpecker-style baseline, with the largest gain on the position subtask (+31.7 points, accuracy+ improving from 0.367 to 0.600). A four-configuration ablation confirms that both relational layers contribute independently (McNemar p = 0.025). These results show that structured relational evidence meaningfully improves post-hoc hallucination correction on the spatial reasoning subtasks where current MLLMs are most deficient.

---


### 116. [Reliable Fusion of Conflicting Experts](https://arxiv.org/abs/2609.27913)

**<font color=#1a73e8>作者：</font>** Pranuthi Tenali, Sahil Sidheekh, Saurabh Mathur 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of aggregating opinions from multiple black-box experts in noisy, conflict-prone settings where expert reliability varies across inputs. Static aggregation methods, such as majority voting, fail to capture this variability and often yield unreliable outcomes under disagreement. We propose a tractable, probabilistic-circuit-based fusion framework that dynamically combines expert responses using context-specific credibility estimates, enabling principled and reliable reasoning. The framework is agnostic to the underlying experts and does not require access to their internal representations or any retraining. We empirically validate our approach on multiple-choice question answering tasks using multiple LLMs as experts, comparing against individual models and static ensemble baselines. Our method consistently improves predictive performance and produces more reliable decisions under conflict, highlighting the effectiveness of context-aware credibility modeling for robust multi-expert fusion.

---


### 117. [UVU: Improving Multimodal Understanding via Vision-Language Unified Autoregressive Paradigm](https://arxiv.org/abs/2609.27915)

**<font color=#1a73e8>作者：</font>** Zhehan Kan, Xinghua Jiang, Yubo Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable advancements in multimodal large language models (MLLMs), their fine-grained visual understanding is constrained by a primary reliance on sparse textual supervision. Existing efforts to introduce visual supervision typically do so during post-training, when visual representations have already been largely fixed, causing such signals to act mainly as auxiliary constraints rather than as a primary force for shaping perceptual features. In this paper, we aim to fundamentally reshape the model's perceptual backbone by incorporating vision supervision directly into the pre-training stage. We observe that pixel-level image patches and textual tokens naturally coexist in a shared, raw high-dimensional space characterized by an inherent input symmetry. Leveraging this insight, we propose UVU, a novel vision-language unified autoregressive framework that eschews vector quantization. It uniquely employs continuous visual encoding for lossless representation of visual inputs and proposes a large-scale iterative hierarchical clustering algorithm to construct a pixel-level visual codebook, thereby extending the vocabulary for unified supervision and enabling autoregressive generation of pixel-level image tokens alongside textual tokens. UVU effectively synergizes pixel-level visual perception with semantic-level visual understanding, internalizing visual reconstruction capabilities and unlocking the facilitative role of visual supervision in enhancing understanding in the pre-training stage. Extensive experiments across multiple tasks demonstrate that MLLMs are capable of achieving superior multimodal understanding performance under the supervised learning paradigm of UVU.

---


### 118. [Learning When Not to Listen: Selective Anti-Interference Pretraining for Language Models](https://arxiv.org/abs/2609.27925)

**<font color=#1a73e8>作者：</font>** Jinchang Zhu, Haowei He, Yi Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can over-condition on irrelevant preceding text: predictions already supported by local context may still change when distant, unrelated prefix tokens are perturbed. This interference is especially consequential in long, packed, or distractor-heavy contexts, where useful evidence and irrelevant spans coexist. We propose Selective Prefix Anti-Interference Regularization (SPAR), a pretraining objective for selective anti-interference. SPAR runs the original sequence and a corrupt-prefix input in which only the far prefix is changed, then uses a short-context sufficiency gate and a gated KL objective to stabilize locally supported suffix predictions. The gate operationalizes a model-based estimate of whether the far prefix supplies additional information about the target token. Mechanism analyses show that the gate identifies locally sufficient tokens and sharply reduces prefix sensitivity on gate-selected suffix tokens. In continued training on pretrained base models, SPAR improves RULER across Qwen2.5-0.5B, Qwen2.5-3B, Llama-3.2-1B, Llama-3.1-8B, and GPT2-XL under equal counted training compute; pretraining experiments further show gains on both RULER and NoLiMa. These results show that selective anti-interference is an effective objective-level signal for robust context use.

---


### 119. [From Sentiment Classification to Actionable and Responsible Feedback: A Scoping Review and Evidence Map of NLP in Student Evaluation of Teaching, 2015-2026](https://arxiv.org/abs/2609.27939)

**<font color=#1a73e8>作者：</font>** Jeff Eicher, Rafael da Silva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language processing (NLP) applied to open-ended teaching-evaluation comments (Student Evaluation of Teaching, SET) has tracked the field's technical evolution--from lexicons and conventional classifiers to transformers and large language models (LLMs)--but it is not evident that this technical diversification has been accompanied by corresponding gains in educational value and robustness of the evidence. This scoping review (PRISMA-ScR) maps 421 studies (2015-2026, 2026 partial) along a technical axis (RQ1) and four value dimensions (RQ2-RQ5). Dual mutually blinded LLM screening with sampled human adjudication coded seven extraction domains, with targeted codebook-boundary review at synthesis. The joint map's sharpest quantified gap is the actionability discontinuity: demonstrated output or stronger (A2+: 258/421; 61.3%) versus intended-user evaluation or stronger (A3+: 49/421; 11.6%), a 49.7 percentage-point drop. Sentiment analysis remains the modal task (300/421); diagnostic and generative depth is a substantial minority (D4-D5: 28.2% of resolved cases); a formal fairness metric is rare (1.9%). The findings are descriptive and do not support causal claims of progress: technological coexistence and uneven reporting are part of the map, but the A2+ to A3+ cliff is the contribution, not a quality ladder.

---


### 120. [VIVAS: Vitalizing Visual Perception in VLM Pre-training via Vision-language Unified Autoregressive Supervision](https://arxiv.org/abs/2609.27948)

**<font color=#1a73e8>作者：</font>** Zhehan Kan, Yubo Zhu, Xinghua Jiang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) demonstrate strong capabilities, they continue to suffer from a critical limitation: insufficient fine-grained visual perception, which fundamentally limits their multimodal understanding. We attribute this bottleneck to text-dominant optimization biases during pre-training, which encourage the model to overlook fine-grained visual details, thereby limiting the capability of multimodal understanding. We investigate that overcoming this bottleneck requires two key elements: (1) a unified token space paradigm that ensures stable training dynamics, and (2) a modality-aligned dense visual supervision signal enriched with both structural granularity and semantic information to capture critical visual representations. Based on these insights, we propose VIVAS, a framework built upon the unified token space paradigm, which introduces a dense-structural-semantic vision tokenizer, which expands the textual vocabulary into a unified vision-language vocabulary by incorporating a visual vocabulary. During pretraining, VIVAS performs vision-language unified autoregressive supervision over both visual details and linguistic content, thereby enhancing visual perception to improve multimodal understanding. Trained end-to-end on 12.4T tokens, VIVAS achieves state-of-the-art performance across 7 tasks and 39 multimodal benchmarks.

---


### 121. [When Accuracy Gaps Fail to Certify: Auditing Cross-Domain Recalibration of LLM Judges](https://arxiv.org/abs/2609.27954)

**<font color=#1a73e8>作者：</font>** Fariya Afrin, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A scalar recalibration map fitted for an LLM judge on one task can fail when the task distribution changes, but the source-target accuracy gap is often treated as a proxy for that failure. We test what this gap can predict and what it can certify across thirteen judges, two generators, eight domains, and 1,176 predeclared transfers. After accounting for mean score shift, the gap yields a population lower bound on target calibration error, yet identical gaps can induce opposite transfer outcomes. Exact importance weighting recovers target proper loss under covariate shift, so failure of an estimated weighting pipeline does not by itself establish conditional shift. A finite-sample simultaneous lower certificate converts the population bound into a one-sided rejection rule using audit labels disjoint from evaluation outcomes. The leak-free gap correlation is 0.25 (95% CI [-0.09, 0.55]), falls to 0.09 on the second generator, and does not support a generator-invariant association. The certificate retains nominal coverage but has power 0.13 even at m=1024, whereas target-domain temperature scaling with 16 labels reaches harm rate 0.09, compared with 0.34 for source-fitted Platt scaling. Accuracy gaps are therefore weak warning signals for scalar probability transfer, not deployment certificates.

---


### 122. [CS-WCP: Robust Conformal Sets for LLM-Judge Traffic Shifts with Uncertain Group Proportions](https://arxiv.org/abs/2609.27955)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction sets built from an LLM judge can undercover when deployment traffic changes the prevalence of task or policy groups. Weighted conformal prediction is exact under covariate shift when the density ratio is known, but group proportions must usually be estimated from finite unlabeled samples. We introduce confidence-set weighted conformal prediction (CS-WCP), which constructs simultaneous exact intervals for source and target group masses and returns the union of weighted conformal sets over every compatible ratio vector. For a fixed or independently learned finite partition, CS-WCP attains coverage at least 1-alpha-delta_w-tau_A-kappa, where tau_A measures within-cell covariate mismatch and kappa measures conditional shift. A linear endpoint rule computes the robust union in O(G|Y|) time. Across 336 constructed shared-support traffic shifts, CS-WCP reaches 0.973 mean coverage with 13 point failures, compared with 0.954 and 44 failures for source conformal prediction, at mean binary set sizes 1.74 and 1.65. On 336 natural cross-task transfers, coverage rises from 0.882 to 0.962, but mean set size reaches 1.87 and a size-matched group plug-in baseline is competitive. The method therefore supplies an auditable coverage safeguard under uncertain mixture weights; its value is conservative tail protection, not scalar probability calibration or uniformly smaller sets.

---


### 123. [Linear RNN Scaling Laws: When Longer Sequences Beat More Sequences](https://arxiv.org/abs/2609.27964)

**<font color=#1a73e8>作者：</font>** Ziyan Chen, Zhongzhu Zhou, Peilin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical scaling laws for autoregressive language models relate prediction loss to model size, data size, and optimization compute, but their theoretical origin is still poorly understood in sequential pretraining settings. We study this question in a tractable teacher--student model where a stable latent linear RNN generates trajectories and a sketched linear recurrent student is trained by safeguarded full-batch WSD gradient descent on next-token prediction. The sketch dimension $M$ plays the role of model size, while $N$ independent trajectories of length $P$ provide the training tokens. We allow the innovation and initialization covariances to have different power-law exponents $\alpha$ and $\theta$. The induced design spectrum produces explicit approximation, optimization, and statistical scaling laws separated by spectral crossovers. When $\theta\ge\alpha$, the original one-scale rates $M^{1-\beta_\alpha}$, $R^{(1-\beta_\alpha)/\alpha}$, and $(NP)^{-1}\min\{M,R^{1/\alpha}\}$ are recovered. When $\alpha-2r\le\theta<\alpha$, the heavier initialization tail changes the rates beyond $P$-dependent model and optimization crossovers. The proof uses a covariance event only internally and a globally safeguarded step size on its complement. The variance retains the factor $(NP)^{-1}$, while sequence length also suppresses the initialization transient, so $N$ and $P$ cease to be fully interchangeable in the two-scale regime.

---


### 124. [Risk-Controlled KV-Cache Eviction: From Memory Budgets to Risk Targets](https://arxiv.org/abs/2609.27981)

**<font color=#1a73e8>作者：</font>** Beomgu Kang, SoJin Yun, Hojoon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV-cache eviction is typically evaluated through average quality-memory trade-offs, yet a small average loss can hide requests whose utility degrades materially. We reformulate eviction as a deployment risk-control problem: a material degradation occurs when eviction lowers task utility by more than a deployment-specified tolerance relative to full-KV inference on the same request, and deployment risk is the population frequency of such events. Given a reliability contract specifying a target risk level and confidence requirement, we use a compressor-agnostic post-hoc certification procedure to select a retention policy from calibration data with a finite-sample guarantee, falling back to full KV when no compressed policy is certified. Across multiple eviction methods, Llama and Mistral models, and LongBench and RULER-32K, the same contract supports substantially different levels of eviction: on Llama, it certifies SnapKV at 75% retention on LongBench but no tested compressed policy on RULER-32K, triggering full-KV fallback. Policies with empirical degradation rates below the 5% target can still fail finite-sample certification; on Llama LongBench, empirical thresholding selects uncertified policies that retain 5-10 percentage points less cache across fixed-budget methods. The proposed framework converts a deployment-level reliability requirement into a KV-memory operating point.

---


### 125. [Riemannian Structure and Optimization for a Class of Low-Parametric Orthogonal Matrices](https://arxiv.org/abs/2609.27982)

**<font color=#1a73e8>作者：</font>** Ali Aliev, Maxim Rakhuba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we are concerned with matrices formed by block-diagonal factors interleaved with fixed permutations -- a flexible family of structured matrices. This class has recently drawn interest in deep learning architectures for its balanced expressivity-efficiency trade-off, yet efficient computational strategies for working with it remain to be found. We approach this problem through Riemannian geometry and examine under what conditions this class admits a smooth manifold structure. For the practically important case of orthogonal two-factor matrices, we derive the essential Riemannian tools and propose efficient algorithms for their implementation. The algorithms leverage automatic differentiation, support parameter sharing within each factor, and avoid explicit dense matrix construction. We test them within the Riemannian optimization framework on the best matrix approximation problem and for parameter-efficient fine-tuning of large language models. Beyond the two-factor setting, we study the geometric and matrix-theoretic properties of factorizations with a larger number of block-diagonal factors.

---


### 126. [PCQC: Privileged Counterfactual Question Credit for Multi-Turn Medical Dialogue](https://arxiv.org/abs/2609.27987)

**<font color=#1a73e8>作者：</font>** Chenxuan Li, Jiayi Wan, Xinrong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made substantial progress on medical question-answering, yet effective medical dialogue also requires learning to ask questions that uncover relevant patient information. To train such dialogue policies, a common pipeline combines supervised fine-tuning with reinforcement learning (RL) based on final diagnostic correctness. However, this outcome-based supervision does not directly distinguish the contributions of individual questions and provides no question-level feedback for unexecuted alternatives. To address this gap, we introduce PCQC (Privileged Counterfactual Question Credit), which uses privileged patient information during training to learn from questions never asked. During training, PCQC makes alternative questions directly comparable at the same dialogue state by using privileged patient facts to construct their answers. A frozen diagnostic scorer evaluates the diagnostic utility of each resulting question-answer pair by how strongly it supports the correct diagnosis. PCQC turns these comparisons into relative question credit that teaches the policy which questions to favor, directly supervising both executed and unexecuted questions alongside outcome-based RL without requiring complete rollouts for the unexecuted alternatives. Extensive experiments across four medical benchmarks demonstrate that PCQC achieves 63.10% mean diagnostic accuracy, outperforming GRPO and ATPO by 4.38 and 4.21 percentage points, respectively. These gains are achieved with 33.1% fewer inquiry turns than GRPO.

---


### 127. [Your Model Is Leaking: Covert Information Transfer through LLM Residual Streams](https://arxiv.org/abs/2609.27996)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Yanna Jiang, Guangsheng Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-sensitive organizations may run large language models (LLMs) in restricted or air-gapped environments while exporting selected diagnostic artifacts. We show that a compromised runtime component can hide sensitive information in intermediate activations that are allowed to leave the restricted environment. An offline observer can recover this information with a simple linear decoder. The attack requires no model retraining or weight modification, no attacker-controlled egress, and no control over the recorder or transfer process. We introduce a residual-stream covert-channel attack that maps messages to codewords and injects them into an intermediate residual stream through a compromised runtime hook. To maintain recoverability, the injection strength is scaled with the local residual norm using the signal-to-residual-norm ratio. Across eleven models from seven architecture families, our evaluation shows 91--100% recovery on nine models with KL divergence 0.001--0.007, while evaluated activation-level detectors remain close to random guessing (AUC <= 0.56). Tested post-hoc defenses do not reliably eliminate the channel. Thus, an activation artifact can be schema-valid while carrying information that is not authorized to cross the boundary.

---


### 128. [Learning from Failures: Heterogeneous Graph Memory for Small Language Model Tool-Using Agents](https://arxiv.org/abs/2609.28003)

**<font color=#1a73e8>作者：</font>** Jiaxing Li, Lei Song, Rui Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small and medium-sized language models offer cost-effective executors for tool-using agents, making them attractive for local and large-scale deployment. However, in long-horizon and stateful environments, they often make structural errors such as missing required observations, performing premature writes, repeating failed calls, and violating action preconditions. These errors can lead to incorrect state updates, policy violations, and costly or irreversible consequences, making reliable tool execution a critical deployment challenge. Existing fine-tuning approaches require substantial data and computation, while flat memory may retrieve failed actions without preserving their causal context or safety conditions. In this paper, we propose FRESH, a Failure-aware Retrieval framework over Experience-Structured Heterogeneous graphs, which transforms historical successes and failures into structured external experience for tool-using agents. By explicitly modeling the dependencies among tasks, actions, errors, repairs, and execution conditions, FRESH helps frozen language models reuse reliable strategies, avoid recurring failures, and make safer decisions in stateful tool interactions. Experiments on $\tau$-Bench and AppWorld with multiple open-source models show that FRESH consistently improves task success and tool-use reliability over no-memory agents and representative memory-based baselines.

---


### 129. [Shared Global KV with Layer-Specific Local History](https://arxiv.org/abs/2609.28006)

**<font color=#1a73e8>作者：</font>** Xinglang Xian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoder-only Transformer language models cache keys and values (KV) to reuse past computation during generation. Sharing KV across layers saves storage but reduces the diversity of representations available across depth. We study what local memory should retain alongside shared global KV, separating historical content from the input source used to form it. At 126M parameters and 2K context, an eight-seed study finds about 1.4% lower held-out test perplexity with local history than with a current-token local branch. Capacity, entry-count and training-compute controls support the value of historical content. In a two-seed comparison, this value persists when adjacent layers share local inputs while retaining independent projections; source sharing also shortens exact cache-construction dependencies. Against GQA and adjacent-layer KV sharing, equal bounded learning-rate searches and new-seed confirmation yield better same-source likelihood with larger caches and higher long-request latency. The ordering against adjacent-layer sharing persists after equal-token adaptation to 8K, with a short-context cost. The eight-seed external-book history effect remains uncertain, and downstream outcomes vary by task. We derive a sufficient suffix schedule that reduces upper-layer construction work while preserving the complete cache in exact arithmetic.

---


### 130. [Evaluating Open-Weight LLMs for Turkish Domain Documents Under Retrieval and Hardware Constraints](https://arxiv.org/abs/2609.28007)

**<font color=#1a73e8>作者：</font>** Imtiaz Ul Hassan, Öykü Akbulut, Onur Kaya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most Turkish-capable large language models (LLMs) are evaluated using general-purpose benchmarks rather than long, structurally complex domain documents. This paper evaluates five open-weight 7B-8B models for Turkish document question answering under a resource-constrained local deployment setting. The primary benchmark contains 100 systematically validated questions derived from a 109-page industrial R&D report, and the evaluation protocol is replicated using a second 112-page public-sector report and an independently constructed 100-question set. All models are evaluated locally on an NVIDIA RTX 3050 laptop GPU with 6 GB VRAM using controlled prompting, decoding, and 4-bit quantisation.
The principal methodological contribution is an evidence-annotated evaluation protocol that separates retrieval failure from downstream model reasoning failure without requiring additional model calls. On the primary benchmark, end-to-end accuracy ranges from 49% to 75%. Seven lexical, dense, and hybrid retrieval configurations are additionally compared using 95% Wilson intervals and exact paired McNemar tests; none significantly outperforms the character TF-IDF baseline on either document. Evidence recall saturates differently across the two reports, showing that retrieval and effective context capacity can be binding constraints for some documents but not others. These results demonstrate that model selection, retrieval behaviour, and hardware limits must be evaluated separately when deploying open-weight LLMs for Turkish domain documents.

---


### 131. [Evaluating Feedback Focus and Pedagogical Adaptivity in LLM-Generated Feedback on Student Writing](https://arxiv.org/abs/2609.28026)

**<font color=#1a73e8>作者：</font>** Norah Almousa, Shayan Peyghambari Oskoui, Raquel Coelho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether state-of-the-art large language models (LLMs) generate feedback that reflects the pedagogical practices of expert teachers in terms of feedback focus and adaptivity. Previous evaluation efforts have examined feedback characteristics, its impact on learning, and its target, yet the focus of feedback and its adaptivity remains largely overlooked. To bridge this gap, we adopt and refine Narciss's taxonomy into seven feedback focus types to annotate teacher and LLM-generated feedback across three university writing courses. We release FeedType, a benchmark containing annotated teacher and LLM feedback from six LLMs under three prompting strategies. We assess the coverage and distribution of feedback focus types, and examine whether LLMs adapt their feedback across draft stages and student performance levels as an expert instructor does. Our findings show that while most LLMs cover most feedback focus types, they fail to reflect teacher feedback distributions and show varying levels of adaptivity, with none matching the teachers' adaptive behavior. We believe FeedType will support future research on pedagogical alignment in LLM feedback generation.

---


### 132. [How Much Were You Told? Measuring External Information in Peer Reviews](https://arxiv.org/abs/2609.28041)

**<font color=#1a73e8>作者：</font>** Matthieu Dubois, Pablo Piantanida, François Yvon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conference policies distinguish using Large Language Models (LLMs) to polish one's own review from delegating the critique, but current Artificial Text Detection (ATD) methods largely measure surface form rather than the origin of its content. We instead measure the external information carried by a review: information not explained by the reviewed paper and a generic reviewing instruction. We propose Self-Conditioning, an unsupervised information-theoretic estimator that compares the likelihood of a review under its production context with its likelihood when that context is augmented with hints extracted from the review itself. On the IntelLabs peer-review benchmark, Self-Conditioning separates fully-delegated from machine-polished reviews with AUC up to $1.0$ while remaining largely insensitive to surface rewriting. Moreover, as generators receive increasing amounts of externally-provided information, their scores move monotonically towards the human regime, unlike standard ATD baselines. High-temperature sampling can evade the estimator, but at the cost of output quality.

---


### 133. [TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval](https://arxiv.org/abs/2609.28048)

**<font color=#1a73e8>作者：</font>** Mourad Hassani, Julien Romero, Amel Bouzeghoub 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern information retrieval (IR) systems rarely represent time, yet many information needs depend on it: in clinical, journalistic, and legal search, when an event occurred can decide whether a document is relevant. Dense retrievers and Retrieval-Augmented Generation (RAG) pipelines match queries to documents well on topic but poorly on time, so they surface content that is on-topic yet temporally wrong. We introduce Temporal Textual Similarity (TTS), a task that measures how well two anchored texts align in time, independent of their topical similarity. We then present TEMPS (Temporal Embedding Model for Precise Search), a modular temporal branch that attaches to a frozen semantic retriever and trains on that signal. It resolves anchored temporal expressions to intervals and moment-matches each one to a Gaussian; the resulting ordering supervises an anchor-date-conditioned encoder, whose score we fuse with the semantic score at inference. Grounding supplies the supervision, so training uses no hand-labeled temporal data. The temporal score itself is the Gaussian-KL inclusion measure from distributional embeddings; what TEMPS adds is the grounding and the moment-matched supervision. On three temporal benchmarks, TEMPS improves MRR for every semantic backbone tested and, on TS- Retriever, lifts R@1 from 19.92 to 25.39 over the prior temporal state of the art.

---


### 134. [Prompt, Probe, Train, or Annotate? Single-camera sports video understanding in amateur settings](https://arxiv.org/abs/2609.28049)

**<font color=#1a73e8>作者：</font>** Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is usually benchmarked on curated, single-actor, or professionally filmed clips, and a strong score there is routinely read as evidence a model is robust enough for deployment. Amateur team sport is a useful, largely untested place to check that assumption: over eight million students played a school sport in the United States in 2024-25 alone, almost none of it filmed by more than a single fixed camera, with several candidate actors crowded into frame and no operator or second angle to fall back on. Using volleyball as a test case, we ask whether strong performance on general video and world-model benchmarks translates into reliable, per-player attribution once footage is this chaotic, turning footage into statistics through a chain of tasks from finding play boundaries to naming who did what. We evaluate four approaches (prompting and agentic reasoning over frontier vision-language models, classical computer vision with small trained specialists, self-supervised video world models, and manual annotation) at every stage, on 66 amateur matches with 46,648 human-labelled contacts, filmed under conditions no published benchmark uses. No single paradigm wins every stage, and static, single-frame computer vision is not competitive at any stage involving motion or identity. A prompted model segments matches well, yet a far smaller trained model beats it at spotting contacts for a fraction of the cost, and the sport's own rules recover rally outcomes the pixels cannot. Identity is where every automated approach struggles: a jersey number is a static fact temporal reasoning cannot recover if never visible, unlike sporting action, a repeated motor pattern a temporal model can exploit, which is why holistic reasoning improves event detection while identity stays unchanged. We close with where each approach earns its cost, and what transfers beyond volleyball to amateur sport.

---


### 135. [Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts](https://arxiv.org/abs/2609.28053)

**<font color=#1a73e8>作者：</font>** Pit Neitemeier, Jiaze Li, Alessio Serra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) training requires global load balance to prevent expert under-utilization and local balance for efficient expert-parallel execution. Existing distributed Quantile Balancing (QB) uses shard-dependent or approximate global quantiles, while token-independent expert biases cannot ensure microbatch-level balance. We introduce Exact Quantile Balancing (EQB), which computes exact global-batch BF16 quantiles with negligible communication, and Load-Error Injection (LEI), which injects local load errors directly into router-score gradients. On 7.5B-parameter MoEs trained for up to 500B tokens, EQB improves global balance and downstream performance over naive QB, while LEI improves local balance and outperforms the GShard loss at comparable quality.

---


### 136. [Can LLMs Catch a Rigged Backtest? A Clean-Control Calibration Benchmark](https://arxiv.org/abs/2609.28090)

**<font color=#1a73e8>作者：</font>** Makar Ulesov, Vladislav Smirnov, Omar Ibrahim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backtest auditing is a calibration problem: high flaw recall is not useful when the model falsely flags matched clean strategies. We build a 96-item paired benchmark in which every flawed backtest has a clean control that holds strategy, dates, code style, labels, and reporting scaffold fixed while changing one methodology detail. A deterministic scorer separates flaw recall, clean-control false positives, evidence localization, and fix relevance. Over 1440 cached audits from four text endpoints, the primary DeepSeek auditor reaches 100.0\% closed and clean-aware code recall, but open prompts over-flag 93.8\% of clean code controls, and clean-aware all-three specificity is 87.5\% even where recall saturates. A clean-aware warning drops DeepSeek code false positives from 20.8\% (95\% CI 11.7--34.3) to 0.0\% (0.0--7.4) at unchanged recall, while the budget anchor still flags 38/48 clean controls under the same prompt. Reporting recall alone would rank three of these four models identically; reporting the clean-control rate separates them by 79 points.

---


### 137. [Scaling Attention Head Analysis via Gradient-Based Attribution in Context-Aware Machine Translation](https://arxiv.org/abs/2609.28117)

**<font color=#1a73e8>作者：</font>** Paweł Mąka, Yusuf Can Semerci, Jan Scholtes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce a gradient-based head attribution strategy where the Token-level Max-Margin loss is backpropagated to the attention maps. This framework enables a large-scale causal analysis of attention heads, making it suitable for LLMs. We evaluate our method on the task of disambiguation in Context-aware Machine Translation, where we analyze 50 phenomena across 4 models and 4 language directions. We empirically show the alignment of our method with the effects of increasing the attention scores of token-to-token relations on three models and two language directions, ensuring the robustness of our method. Our analysis reveals the presence of the "general-purpose" attention heads that improve the model's performance when attending to different relations. We find that the average attention a head assigns to a relation does not necessarily relate to the model's performance, which suggests that the models developed redundancies during training in terms of the head functions.

---


### 138. [RL Starts before RL: On Policy Distillation for Better Reinforcement Learning](https://arxiv.org/abs/2609.28145)

**<font color=#1a73e8>作者：</font>** Shuai Dong, Yongfu Zhu, Yuqi Xu 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) improves reasoning, but its performance depends on the policy from which training begins. We study on-policy distillation (OPD) as a preparation stage for RL and ask whether its benefits extend beyond improvements in the distilled model's initial accuracy. Under shared RL settings, students initialized with OPD reach higher final performance than those trained with direct RL or supervised fine-tuning followed by RL. This advantage can emerge even when OPD produces little immediate improvement in accuracy. Pre-RL Pass@k does not fully explain the benefit: similar or even higher values do not necessarily lead to better performance after RL. Behavioral analyses point to alignment with the teacher's distribution beyond top-1 agreement as a possible explanation. Such alignment may favor higher-quality reasoning paths while retaining alternatives that RL can further refine using outcome feedback. We further examine how trajectory sources and divergence objectives affect the value of distillation for subsequent RL. Standard reverse-KL OPD performs better before RL, but forward-KL OPD overtakes it afterward; with teacher-generated distillation trajectories, reverse KL remains ahead at both stages. These findings suggest that the preferred distillation objective depends on both the trajectory source and the training that follows. Our results support evaluating OPD as preparation for RL and selecting distillation choices by the performance achieved after subsequent training.

---


### 139. [Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs](https://arxiv.org/abs/2609.28150)

**<font color=#1a73e8>作者：</font>** Haitong Jiang, Chunlin Liu, Yile Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Closed-loop revision is increasingly used in large language model (LLM) applications, but failures may reflect incomplete feedback or ineffective responses to correct feedback. We introduce a fixed-budget revision protocol with deterministic verifiers that report all remaining violations across exact-length, lexical, and compositional constraints. Fixing feedback correctness and completeness isolates model-side revision behavior. Across 19 open- and closed-source models, controller-level mean final joint success ranges from 17.4% to 99.8%, with substantial cross-model gaps persisting under identical initial drafts. Controlled experiments reveal reproducible model-specific responses to exact feedback. Post-training and scale reshape these responses without consistently bringing them closer to exact correction. Across all constraint families, failed trajectories often repeat earlier outputs, and prior recurrence is associated with lower subsequent recoverability. Matched-state interventions show that removing earlier dialogue while holding the current draft and feedback fixed changes recurrence escape without reliably improving final success; effects depend on the model, task, and trigger-state composition. Exact feedback makes revision errors observable, but does not make the closed loop reliable. Code and reproduction instructions: this https URL.

---


### 140. [PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety](https://arxiv.org/abs/2609.28197)

**<font color=#1a73e8>作者：</font>** Jiapeng Sun, Yujin Zhou, Han Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations, we formalize Decoupled Proactive Safety Monitoring along three dimensions: whether to intervene, when to intervene, and what the risk is. We introduce PASTABench, a benchmark of 1,139 multi-turn trajectories spanning 5 risk categories and 13 subcategories. We further propose the Optimal Intervention Window (OIW), anchored by annotated Earliest-Signal and Trigger turns, to quantify intervention timeliness. Evaluation of 16 LLMs reveals that proactive intervention remains largely unsolved, with the best model achieving only 40.74% optimal-timing interventions. Fine-grained diagnosis further uncovers pervasive lexical overfitting: competitive safety scores of smaller models mask keyword hypersensitivity rather than genuine risk comprehension, as their proactive capability largely collapses once hazard vocabulary is neutralized.

---


### 141. [GUIAuditor: Enabling Post-hoc Child Safety Forensics via Action-Guided GUI Provenance on Mobile Devices](https://arxiv.org/abs/2609.28205)

**<font color=#1a73e8>作者：</font>** Junlin Liu, Yifeng Cai, Shuai Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of smart devices exposes children to online risks like grooming and financial scams that are deeply embedded within legitimate applications. Current approaches rely on automated prevention and detection, a paradigm that is fundamentally limited by its inherent fallibility. Whether rule-based or AI-driven, they inevitably produce false positives and negatives, failing to provide reliable protection. In this paper, we argue for a complementary, human-in-the-loop, post-hoc forensic paradigm. We present GUIAuditor, the first system designed to realize this vision by creating GUI Provenance: a queryable, semantic record of a child's interaction sequence. To generate this, GUIAuditor leverages a Multimodal Large Language Model (MLLM) to translate the temporal sequence of GUI events into a human-understandable narrative. To make this practical on mobile devices, a novel evidence distillation pipeline reduces the data requiring analysis by over 89.2% compared to periodic sampling approaches adopted by industry standards, with negligible impact on accuracy. On a new dataset of 295 interaction clips, GUIAuditor achieves a 95.23% Macro-F1 Score in logging significant events and, crucially, its two-stage forensic query engine successfully retrieves the correct evidence as the top result for over 90.20% of natural language questions. An end-to-end evaluation on three modern smartphones shows that the full pipeline, including on-device MLLM inference, adds 2.1W of power draw and 7.4s of per-event latency, with a peak memory footprint of ${\sim}$3.1GB. These results show that post-hoc GUI forensics can run on modern mobile devices and provide useful context for guardian-led safety review.

---


### 142. [A Unified Framework and Dataset for Oriented Object Visual Grounding in Remote Sensing](https://arxiv.org/abs/2609.28230)

**<font color=#1a73e8>作者：</font>** Zeyu Ding, Yong Zhou, Jiaqi Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding in remote sensing images aims to locate objects described by referring expressions. Most existing methods predict horizontal bounding boxes, which are often inaccurate for objects with arbitrary orientations. To address this limitation, we introduce O$^2$-VG, a family of models for oriented object visual grounding with three complementary designs. Specifically, O$^2$-VG-Trans is a cross-modality transformer for oriented object visual grounding. It establishes a strong discriminative foundation for the model family. Building upon it, O$^2$-VG-Uni predicts universal oriented proposals for possible foreground objects without specific text prompts. It also supports object retrieval through cached proposal embeddings. Using these universal oriented proposals as input prompts, O$^2$-VG-VLM is an autoregressive vision-language model. It generates oriented box token blocks in parallel through multi-token prediction. In addition, we construct DIOR-R-RSVG, a dataset for oriented object visual grounding in remote sensing images. It provides image, expression, and oriented box triplets for training and evaluation. Together, the O$^2$-VG family provides a flexible framework that spans discriminative transformers and generative vision-language models. It achieves superior performance across multiple benchmarks. Code is available at this https URL.

---


### 143. [EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks](https://arxiv.org/abs/2609.28236)

**<font color=#1a73e8>作者：</font>** Lizhou Liang, Xinyu Zhong, Miao Pan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied interaction requires agents to retain and continually update information about the environment as they observe, act, and encounter change. Yet current agents struggle to maintain such memory reliably. Our analysis traces this limitation to four key deficiencies: weak fine-grained visual memory, unreliable dynamic world-state tracking, failing to record world state revealed by interaction outcomes, and limited generalization from prior experience. However, existing benchmarks do not directly assess these memory capabilities during long-horizon embodied interaction. To address this gap, we introduce EmbodiedMemory-Bench (EMem-Bench), comprising 2,554 interactive episodes across four task families. EMem-Bench requires agents to build and update memory from interaction history, then use it to complete a later task by acting in the environment. We further present Embodied-Memorizer (EMem), an external memory system that organizes embodied experience into spatial, event, and scene memories. We also train EMem-8B, an 8B policy that manages and uses these memories. We evaluate a diverse range of open-source and proprietary MLLMs and representative multimodal memory systems. Results show that current models remain weak and uneven across the four challenges. Under matched backbones, EMem achieves the best overall performance among the evaluated memory systems and improves both open-source and proprietary models, while EMem-8B further improves over its backbone. Project page: this https URL

---


### 144. [Beyond Poetry: Can Large Language Models Generate Classical Arabic Maqamat?](https://arxiv.org/abs/2609.28245)

**<font color=#1a73e8>作者：</font>** AbdulRahman A. Morsy, Aya Zirikly  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance in creative text generation, yet their ability to produce culturally grounded and stylistically constrained literary forms remains underexplored. Prior work has focused largely on modern language varieties and poetry, while classical prose traditions such as maqama remain largely unstudied. The maqama is a classical literary genre characterized by rhymed prose (saj), dense rhetorical ornamentation, and episodic narrative structure, making it a challenging testbed for evaluating whether LLMs can move beyond surface fluency toward deeper literary competence. In this paper, we present the first controlled evaluation study of maqama generation with LLMs, comparing five models under zero-shot, few-shot, and rule-based prompting, and evaluating outputs through both human annotation and an LLM-as-a-judge framework across dimensions such as rhetorical richness, saj density, structural coherence, and stylistic authenticity. Our results show that prompting strategy plays a strong role in stylistic quality: few-shot prompting most consistently improves saj density, while its effects on rhetoric and coherence vary by model, with the strongest models (GPT-4o and GPT-5.4-mini) benefiting most from rule-based prompting on these dimensions, though zero-shot prompting yields the highest aggregate scores across all five models. We further observe systematic differences between models in stylistic alignment with Arabic maqama conventions, and corroborate our findings with a second independent LLM judge, paired statistical significance testing, and non-LLM proxy measures of saj.

---


### 145. [Complementary Roles of Activation and Parametric Memory in Few-Shot Learning](https://arxiv.org/abs/2609.28250)

**<font color=#1a73e8>作者：</font>** Miaohe Niu, Runsong Zhao, Xinyu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At test time, large language models (LLMs) can encode historical information in activation memory (i.e., KV caches) and parametric memory (i.e., updated parameters). While activation memory is generally considered effective for factual recall and parametric memory for learning new tasks, their interplay remains unclear. In this work, we systematically investigate the role of memory in few-shot learning through controlled experiments. We find that activation memory is superior for recalling facts, whereas parametric memory does not consistently outperform activation memory in task learning. Moreover, our experiments show that the composite task, Conditional Arithmetic, requires the synergy of both memory types. Through neuron-level analysis, we find that the model activates distinct sets of neurons when accessing the same historical information through activation versus parametric memory. When both memory types are combined, the model recruits neurons from both sets, which is crucial for solving Conditional Arithmetic. These findings suggest that neither memory mechanism alone is sufficient for this composite task, highlighting the importance of their collaboration.

---


### 146. [Resource-Adaptive Stochastic Gradient Descent for Online Linear Programming without Re-solving](https://arxiv.org/abs/2609.28263)

**<font color=#1a73e8>作者：</font>** Jiameng Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growth of large language model (LLM) inference and search services increases the scale of online linear programming problems, motivating computationally efficient algorithms. We develop resource-adaptive stochastic gradient descent (RASGD) for stochastic online linear programming. The algorithm uses one request and current inventory to update resource prices, requiring O(m) operations for m resources and memory per arrival and no LP or sample-average optimization. The central idea is to express the current-resource pricing logic of re-solving through a first-order SGD update: each arrival refreshes the remaining-inventory allowance in the dual objective, while the stepsize decreases for early learning and increases later to match the speed of inventory adjustment. Under standard non-degeneracy conditions, our algorithm is feasible on every sample path and achieves O(\log T) expected regret against the realized fractional hindsight optimum, which matches the lower bound, even for policies that know the distribution and have unrestricted computation. The analysis converts curvature around the fixed reference price into inventory stability without tracking optimal prices at changing resource levels. Numerical experiments show that RASGD achieves regret competitive with per-arrival LP re-solving and improves upon the tested first-order baselines, while retaining the computational efficiency of first-order methods. These results establish RASGD as a computationally efficient approach to achieving high allocation quality in large-scale OLP.

---


### 147. [Towards Efficient Reasoning: Learning Causal Shortcuts for Diffusion Language Models](https://arxiv.org/abs/2609.28272)

**<font color=#1a73e8>作者：</font>** Dian Jin, Kairong Han, Baohong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have attracted significant attention for their strong reasoning ability. However, under a bidirectional attention mechanism, DLMs operate over an exponentially large exploration space compared to autoregressive models (ARMs), making it challenging to focus on reasoning-guiding tokens under random masking. We define causal shortcuts as token chains that cover the full sequence and provide explicit guidance towards correct reasoning trajectories. We analyze the effects of causal shortcuts on the reasoning accuracy and convergence speed of DLMs, and find that they largely improve answer convergence efficiency and generation accuracy. Motivated by this, we propose a Causal Shortcut Learning (CSL) Framework for DLMs. Specifically, we introduce a step-by-step token extraction procedure to extract causal shortcuts from data, and apply parallel prioritized masking on these tokens during training to enable efficient and accurate convergence to correct answers via causal shortcuts. Extensive experiments across multiple reasoning benchmarks and two base models demonstrate that CSL consistently outperforms existing SFT-variant baselines, achieving an average improvement of $1.92\%$ over SFT-only models, and up to $4.20\%$ on MATH-500. The code is available at the \href{this https URL}{this https URL

---


### 148. [Computation Over Geometry: Meaning Identity Is Computed, Not Shipped in the Embeddings](https://arxiv.org/abs/2609.28290)

**<font color=#1a73e8>作者：</font>** Jiaqi Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meaning identity (whether two sentences say the same thing after wording changes) is treated in retrieval and RAG as a geometric fact about independently encoded sentence vectors. We show that, for frozen off-the-shelf encoders and language models, it is not: identity is computed when both sentences share one forward pass, and is not a property of the embedding geometry those systems ship. On overlap-matched PAWS-X, purpose-built encoders (BGE, E5, GTE, MiniLM, E5-Mistral-7B) reach English confirm AUC only 0.55-0.65 (dense peak 0.70). Independently encoded last-token states of Llama 3, Mistral, and Qwen do no better; late fusion of the two vectors stays near chance. The same probe on a joint forward pass reaches 0.90-0.96 from 1.5B to 32B, collapses under partner shuffle, is mid-depth, saturates near 0.94 by 3B, and appears more weakly in GPT-2 XL (0.76). The gap holds beyond Llama-style models on other causal LMs, bidirectional encoders (DeBERTa, RoBERTa), and encoder-decoders (Flan-T5, T5, BART). Fixed or linear readers over frozen independent encodings never unlock identity; nonlinear pair readers recover part of it only on the full 49k-pair PAWS train split (0.68-0.87). Off-the-shelf rerankers split: BGE-reranker-large reaches 0.94, while MS-MARCO and Jina stay at 0.55-0.64. Independently trained families compute the same relation and a 1.5B joint reader can distill it from unlabelled teacher scores, while no linear function of the teachers own independent vectors can. Bi-encoders can be fine-tuned to fit PAWS (0.87-0.93), but transfer and STS-B suffer. Cosine compares wording neighbourhoods; identity is a cheap computed operator, not a property of either sentence vector.

---


### 149. [Learning the Cost of Reliable Inference](https://arxiv.org/abs/2609.28322)

**<font color=#1a73e8>作者：</font>** Dimitrios Rontogiannis, Ander Artola Velasco, Manuel Gomez Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarking and routing platforms increasingly act as intermediaries connecting large language model providers with end-users. However, providers on these platforms typically use a fixed price per token, preventing users from achieving the most competitive price for their tasks. % workloads. In this work, we design a procurement platform where token prices for each task are driven by provider competition, enabling users to secure competitive pricing for guaranteed quality levels. To this end, the platform sequentially routes queries via a reverse second-price auction that incentivizes model providers to truthfully bid their best estimate of the average cost to serve a user's query. As it routes queries, the platform learns the quality offered by each provider and progressively routes queries to the most cost-competitive provider among those meeting a desired quality threshold. To validate our design, we conduct experiments with multiple LLMs from the \texttt{Llama} and \texttt{Qwen} families on popular mathematical reasoning and question-answering benchmarks. The results show that the pricing margin of the most cost-competitive provider on our platform varies significantly---from $10\%$ to $71\%$---depending on the task and quality threshold. This suggests a substantial inefficiency in the current fixed-price market, and it demonstrates that our platform may enable users to capture maximum savings whenever competitive market conditions permit.

---


### 150. [An Open Pipeline and Dashboard for Systemic-Risk Evidence under the EU AI Act's Code of Practice](https://arxiv.org/abs/2609.28335)

**<font color=#1a73e8>作者：</font>** Jacob T. Emmerson, Phuong-Anh Nguyen-Le, Ronan Romano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claims about AI safety reach audiences well beyond the AI community, yet many rely on opaque evidence or static assessments, when supporting evidence is accessible at all. We present the Systemic Risk Index, an open evaluation pipeline and dashboard built to make empirical evidence more transparent and traceable to the public. Our work organizes 19 public benchmarks into four systemic-risk categories defined by the EU GPAI Code of Practice---CBRN, cyber offense, harmful manipulation, and loss of control---and evaluates models using harm-preserving perturbations and simulated deployment contexts. The interactive dashboard lets users alternate between average and worst-case aggregation, vary how model capability affects the aggregate score, and trace each risk rating to its benchmark evidence. Across 18 models, scores fall by 14 to 37 points under worst-case aggregation, highlighting information that can be hidden by an average assessment of model risk. LLM judges show agreement with human graders comparable to human--human agreement ($\kappa = 0.78\text{--}0.82$), and a blind audit finds that $83\%$ of sampled transformations preserve the original harm. In a survey ($N = 21$), most participants report that scores are easy to understand and that the dashboard encouraged them to view model evaluations under different settings

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
