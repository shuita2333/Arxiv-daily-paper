# 🧠 大模型相关研究 | 2026年09月18日

> 本类共 **210** 篇论文：已确认 **198** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-210](./part-05.md)

---

### 1. [Enhancing Extubation Failure Prediction with LLM-Derived Features from Respiratory Therapy Clinical Notes](https://arxiv.org/abs/2609.17532)

**<font color=#1a73e8>作者：</font>** Izzy Chaiken, Aditya Khowal, Neha A. Sathe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Invasive mechanical ventilation is a lifesaving therapy, but timely, safe discontinuation is essential to preventing extubation failure (EF) and related risks to health. We present a novel approach to EF prediction that leverages features classified in free-text respiratory therapy notes using a large language model and logistic regression pipeline. Applied to a patient cohort from University of Washington Medicine, our method identifies clinically meaningful EF-related features that improve EF prediction performance when included alongside structured patient data. We further highlight how differences in target populations in prior EF prediction studies, such as heterogenous inclusion criteria and EF definition, can lead to systematic differences in model performance and hinder generalizability between studies.

---


### 2. [Faking Good and Faking Bad in LLMs: Response Distortion Across Dark Triad Personality Traits](https://arxiv.org/abs/2609.17534)

**<font color=#1a73e8>作者：</font>** Victoria Popa, Guglielmo Cola, Caterina Senette 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social desirability and impression management are pervasive sources of response distortion in human personality assessment, yet their effects on Large Language Models (LLMs) remain underexplored. This study investigates whether contemporary LLMs systematically modulate the expression of Dark Triad traits (Machiavellianism, narcissism, and psychopathy) under fake-good and fake-bad conditions. Seven state-of-the-art models were evaluated across two ecologically relevant contexts: employment selection and forensic evaluation, in which socially desirable or undesirable incentives were conveyed through contextual framing. Trait expression was measured using standard psychometric scoring procedures and compared with self-assessment baselines at both aggregate and item levels. Results revealed systematic and condition-consistent response modulation. Most models reduced Dark Triad scores under fake-good conditions and increased them under fake-bad conditions, although the magnitude and consistency of these effects varied across traits and models. Machiavellianism and narcissism showed the strongest and most coherent shifts, whereas psychopathy displayed greater heterogeneity. Context also influenced responses, with employment scenarios generally producing larger effects than forensic scenarios. An additional experiment showed that explicit fake-bad instructions generated substantially stronger distortions than contextual framing alone. The results suggest that personality-related outputs should be interpreted in light of the motivational and situational context in which they are elicited. More broadly, they highlight the value of psychometric paradigms for evaluating susceptibility to response distortion, impression management, and context-dependent behavioral shifts, with important implications for LLM benchmarking, alignment evaluation, and robustness assessment.

---


### 3. [Think Before You Comfort: Reflective Cognitive Alignment for Protocol-Grounded Elderly Stimulation Agents](https://arxiv.org/abs/2609.17536)

**<font color=#1a73e8>作者：</font>** Jiyue Jiang, Ziyi Li, He Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive Stimulation Therapy (CST) offers non-pharmacological support for elders with cognitive impairment, yet scalability remains constrained by reliance on trained facilitators and severe data scarcity, particularly for privacy-sensitive, low-resource languages such as Cantonese. While Large Language Models (LLMs) show promise for automated companionship, they often struggle to balance empathetic engagement with adherence to cognitive stimulation guidelines. We propose a framework addressing these challenges along two complementary axes. First, STaR-CS (Style-Transfer and Role-Conditioned Cognitive Stimulation) synthesizes multi-party dialogues through facilitator style modeling and structured skeleton extraction, mitigating data barriers. Building upon this corpus, the Reflective Cognitive Alignment (RCA) framework models stimulation interactions as a sequential decision process, integrating Protocol-Constrained Chain-of-Cognition (PC-CoC) for structured reasoning and Inference-Time Value Alignment (IVA) for principled response selection based on safety and engagement goals. Evaluations across six backbone LLMs and two independent judges show that RCA consistently improves protocol adherence, safety, and group facilitation over standard prompting baselines. Our code is available at this https URL.

---


### 4. [Relation Before Entity: Deferred Commitment in Language Model Factual Recall](https://arxiv.org/abs/2609.17537)

**<font color=#1a73e8>作者：</font>** Divyansh Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether relation-type information (e.g., capital-of) and entity-specific information (e.g., France to Paris) become causally active at the final-token position at the same depth during recall. Using four complementary causal diagnostics across four decoder-only models and eight prompt families, we find a robust temporal asymmetry: relation information becomes generation-controlling before entity information does. Relation onset precedes entity onset by 10-16 tested layers (31-44% of network depth) at threshold 0.4, with the ordering holding across all 16 model-threshold combinations for thresholds 0.2-0.5. Critically, entity information is not absent early: entity-token patching succeeds at 90-100% in early layers. Instead, entity commitment to generation is deferred: entity information is available at the entity-token position but becomes generation-controlling at the final token only after being routed there.

---


### 5. [From Pixels to Pairs: A Comprehensive Benchmark of LLM-Based Key-Value Extraction in Noisy Document Settings](https://arxiv.org/abs/2609.17538)

**<font color=#1a73e8>作者：</font>** Zahra Anvari, Vassilis Athitsos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for structured information extraction from documents, yet their behavior under realistic OCR noise remains poorly understood. We present a systematic benchmark of open-source instruction-tuned LLMs for key-value pair (KVP) extraction under both clean-text and noisy OCR conditions.
We evaluate representative decoder-only models (Gemma, Mistral, Qwen2.5, LLaMA 3, and DeepSeek) on the FUNSD, CORD, and SROIE benchmarks using both Gold-text annotations and OCR outputs from PaddleOCR, EasyOCR, and Tesseract. A unified evaluation protocol isolates the effects of input quality, model design, and prompting under consistent conditions.
The results show that modern LLMs act as strong semantic extractors when high-quality text is available, in some cases approaching supervised layout-aware systems. Under OCR noise, however, performance degrades substantially and performance gaps between models narrow as input corruption increases.
Across all datasets, extraction performance is governed by two factors: semantic reasoning over text and preservation of textual fidelity under OCR noise. While larger models improve results on clean text, these gains diminish under noisy inputs, where OCR quality becomes the dominant factor. We also identify recurring failure modes, including key-value misalignment, hallucination, and numeric corruption. Our findings highlight the gap between clean-text evaluation and real-world deployment, emphasizing the need to jointly improve OCR quality, structural reasoning, and LLM-based semantic modeling.

---


### 6. [Register Bias in Complexity-Based Large Language Model Routing](https://arxiv.org/abs/2609.17542)

**<font color=#1a73e8>作者：</font>** Simran Koul  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model services increasingly route each query to one of several models of differing capability, using a cheap estimate of query complexity to send easy queries to small models and hard queries to large ones. I show that this routing step is not register neutral: text written in a non-standard English register, African American English or the English of second-language writers, is systematically assigned a lower-capacity tier than a meaning-equivalent standard-English version of the same query. The effect is driven by a specific, common routing signal, input length, because non-standard registers omit function words and thus look shorter and therefore simpler; other complexity signals do not carry it. I demonstrate the disparity on 37,704 authentic learner sentence pairs and on a controlled parallel corpus. I then measure the quality consequence on a device, edge, and cloud model ladder and find that the harm is driven by pervasive model bias, every tier, including a frontier cloud model, answers non-standard-register queries significantly less accurately, while the marginal quality cost of the routing decision itself is not significant on this benchmark. Complexity-based routing thus compounds the exposure of the users that the models already serve worst.

---


### 7. [Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation](https://arxiv.org/abs/2609.17544)

**<font color=#1a73e8>作者：</font>** Jiacheng Xie, Xiaoting Tang, Yang Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being explored for clinical applications, yet their assessment for real-world traditional Chinese medicine (TCM) practice remains limited We constructed a clinical case library comprising 349 de-identified outpatient cases from 62 hospitals and evaluated 16 LLMs and a comparator cohort of 60 practicing TCM physicians using 60 representative cases selected from this library. Model outputs and physician reports were anonymized and scored by five senior TCM experts across nine diagnostic and therapeutic dimensions. Cutting-edge general-purpose LLMs achieved higher expert scores than the physician comparators, particularly for medical advice, treatment principles and selected diagnostic tasks. However, prescription-level analyses revealed discrepancies in herb selection, dosage, and treatment strategy, and qualitative safety review identified hallucinations and undesirable template-driven outputs. These findings highlight the potential of LLMs for TCM decision support while underscoring the need for physician oversight, safety constraints and prospective clinical evaluation.

---


### 8. [Legal LLM Hallucination Should Be Evaluated as Failure of Legal Warrant](https://arxiv.org/abs/2609.17546)

**<font color=#1a73e8>作者：</font>** Maksym Taranukhin, Vered Shwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this position paper, we argue that legal LLMs' hallucinations should be evaluated as a failure of legal warrant rather than as factual inaccuracy or citation failure. We define claim-authority warrant as the context-sensitive relation between a consequential legal claim and authority that exists, applies to the relevant jurisdiction, is current for the date of analysis, has the legal status represented by the system, and supports the proposition asserted. Warranted legal generation is the broader system behavior that answers, narrows, asks, warns, corrects a false premise, or abstains according to that relation. The falsifiable prediction is that warrant metrics reveal material failures that answer accuracy, citation existence, generic attribution, LegalHalBench-style statute relevance, and CitaLaw-style sentence-citation alignment can miss. We sharpen this claim with a side-by-side comparison item and a small, reproducible pilot over public-rule tests. We then specify benchmark records, claim boundaries, support labels, mixed response-policy scoring, risk weights, annotation reliability reporting, and jurisdiction-specific authority ontologies. The result is a concrete research agenda for evaluating legal AI systems by whether their consequential claims are licensed by law.

---


### 9. [How AI Assistants Respond to Repeated Abuse](https://arxiv.org/abs/2609.17547)

**<font color=#1a73e8>作者：</font>** William Guey, Wei Zhang, Pierrick Bougault 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI assistants are expected to remain useful during difficult interactions, but little is known about how repeated verbal abuse changes their engagement with an otherwise benign task. We contribute a bilingual, multi-turn framework that separates hard disengagement, an unconditional statement of noncontinuation with no stated route to resume, from soft withdrawal, continued availability, observable task-related work, and boundary setting. Each of eight time-specific API configurations contributed 48 escalation conversations and eight smaller constant-frustration comparisons, giving 448 five-turn conversations, 2,240 responses, and 6,720 metadata-blinded model judgments. Primary results use the sustained-abuse endpoint of the 48 escalation conversations per configuration. Hard disengagement ranged from 0/48 in four configurations to 24/48 (50.0%) for Gemini 3.1 Pro, with strong configuration-associated heterogeneity (matched-label Monte Carlo p = 0.00001). GPT-5.6 Sol produced hard-disengagement labels in 15/48 (31.2%) endpoints, whereas Claude Fable 5 produced none and yielded 42/48 (87.5%) soft-withdrawal labels. Aggregate hard-disengagement rates were similar in English and Chinese (30/192 versus 32/192), although configuration-specific directions varied. Availability also differed from task-related work: Claude Opus 4.8 and Claude Fable 5 remained explicitly available in 48/48 endpoints while providing observable task-related work in only 8/48 and 7/48. Human coding was used to evaluate measurement quality. The results show why a single refusal label cannot capture whether an assistant leaves, pauses, preserves a route back, sets a boundary, or still performs substantive work.

---


### 10. [Myovox: Reading Speech from the Muscles of the Face](https://arxiv.org/abs/2609.17548)

**<font color=#1a73e8>作者：</font>** Varshith Madishetty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Myovox, from myo (muscle) and vox (voice), decodes open-vocabulary English text from 31-channel surface electromyography (sEMG) recorded from the muscles of the face during vocalized speech. It takes the single-subject emg2speech General Corpus from a published 51.17% word error rate to 18.53%, in three separable moves, each measured in isolation. First, I recover the open-vocabulary decode settings missing from the public release and reach a faithful 40.63% WER / 39.02% PER baseline whose phone error rate matches the published one to within 0.8 points, so the acoustic model is reproduced faithfully. Second, I replace the causal encoder with a bidirectional Conformer trained by a four-term cross-modal distillation against the parallel audio's WavLM-Large layer-9 features, reaching 26.14% WER / 22.34% PER from the electromyography alone. Third, I ensemble two acoustic models, union their multi-scale n-best lists, and rerank with a QLoRA-fine-tuned 7B language model, reaching 18.53% WER, the best result reported on this corpus, though not the best reported for sEMG-to-text on other corpora (Section 2). I then report the negative result that bounds the whole approach: reranking is exhausted at 18.5% because the binding constraint is the electromyographic acoustic phone error rate (~20.9%), not the language model. The correct words are simply absent from the acoustic posteriors, so no reranker can reach the 9.30% n-best oracle. All test numbers are on the 400-sentence held-out test set under the authors' official 8,500 / 760 / 400 sequential split; every hyperparameter is tuned once on validation and applied once to test.

---


### 11. [Do Social Patterns Hold in Synthetic Data? Analyzing Cyberbullying Dynamics in LLM-Generated and Authentic Dialogues](https://arxiv.org/abs/2609.17549)

**<font color=#1a73e8>作者：</font>** Arefeh Kazemi, Hamza Qadeer, Sinan Asci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyberbullying (CB) is a complex social phenomenon characterized by repeated aggression, power imbalance, and multi-party interaction. Although large language models (LLMs) are increasingly used to generate synthetic CB conversations for data augmentation and benchmarking, it remains unclear whether such data faithfully reproduces the social dynamics of authentic interactions beyond supporting downstream task performance. We present a comprehensive framework for evaluating the social realism of LLM-generated CB conversations. We compare authentic and synthetic dialogues generated by GPT, Grok, and LLaMA across interactional structure (turn-taking, power dynamics, and repair behavior), linguistic and stylistic realism (pronoun usage and humor), affective and behavioral markers (CB types, profanity, and toxicity), and temporal escalation dynamics. We further complement automatic analyses with a human evaluation of cyberbullying presence, scenario relevance, role plausibility, and social realism. Our results show that LLM-generated data consistently preserves high-level interactional structure, including role participation patterns, directional power asymmetry, and broad distributions of behavioral markers. However, all models systematically distort finer-grained social phenomena, including behavioral magnitude, role-specific allocation, categorical distributions, and temporal dynamics. These distortions are strongly model-dependent: GPT suppresses harmful content, Grok amplifies aggressive behaviors, and LLaMA provides the most balanced approximation while smoothing role distinctions. Our findings show that synthetic CB data is useful for modeling global interactional structure but remains an imperfect substitute for authentic conversations when behavioral realism and social dynamics are essential.

---


### 12. [No Usable Linear "Capitulation Direction" in Two Small LLMs: A Validation Protocol for Activation-Steering Claims, and a Cross-Family Behavioral Study of Sycophancy Under Pushback](https://arxiv.org/abs/2609.17550)

**<font color=#1a73e8>作者：</font>** Saad Aamir, Muhammad Awais Bin Adil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models frequently abandon correct answers when users push back. We study this in two small instruction-tuned models from different families, Qwen2.5-1.5B and Llama-3.2-1B, over TriviaQA: the model answers, is challenged with one of four scripted pushback styles, and answers again. Conditioned on an initially correct answer, the models flip to a wrong answer in 41.8% and 43.1% of episodes. Which pressure works is a property of the model, not the pressure: the same within-question paired comparison (bare doubt vs. emotional appeal), specified in advance, is Bonferroni-significant in opposite directions across families (Qwen: bare doubt > emotional, OR 2.5, p=.040; Llama: emotional > bare doubt, OR 4.0, p=.001). Failure mode is also model-dependent: Llama abandons answers without recommitting at six times Qwen's rate (8.2% vs. 1.4%). Identical pushback repairs initially wrong answers only ~13% of the time; pushback is net epistemically destructive. We then ask whether capitulation is linearly decodable from the pre-response residual stream, a prerequisite for steering-vector interventions at that locus. A naive difference-in-means probe appears to succeed (in-sample AUROC 0.81/0.71), but a validation protocol combining question-level cross-validation, shuffled-label nulls, and a known-direction positive control shows the signal is overfitting: the best cross-validated AUROC is 0.582 in Qwen and 0.548 in Llama, both near or below their permutation thresholds and far under a pre-registered usability bar of 0.70, while the identical pipeline recovers a pushback-presence control direction at AUROC 1.000 in both. We further quantify a measurement hazard: substring grading underestimates capitulation by 18-24 percentage points. Code, prompts, transcripts, and analysis are released.

---


### 13. [The Limits of BPE Tokenization in Polish: Segmentation-Flexional Forms, Grammatical Anchoring, and First-Person Stability in Inflectional Language Models](https://arxiv.org/abs/2609.17553)

**<font color=#1a73e8>作者：</font>** Elzbieta Dawidek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article analyzes BPE tokenization in Polish as a test case for the limits of statistical segmentation in an inflectional language. It asks whether frequency-based tokenization preserves linguistically relevant units, including orthographic form, phonemic and syllabic segmentation, derivational structure, inflectional endings, grammatical form, and the speaking subject. The material includes diagnostic words, a children's text, selected forms from the Preamble to the Constitution of the Republic of Poland, word-family tests, and examples with Polish diacritics and nasal vowels. BPE tokenizers may produce segments that coincide with syllabic or morphologically interpretable divisions, but remain dependent on the frequency of written forms. They do not systematically map orthographic representation onto phonemic structure or context-dependent phonetic realization. The results show that BPE stabilizes frequent surface fragments of grammatical exponents rather than grammatical categories themselves. A form such as ustanawiamy is not merely a sequence ending in -y, but a verbal form anchored in conjugation, person, number, tense, mood, and aspect. The article develops the concept of grammatical form anchoring. In Polish, forms such as poszlam, zrobilam, or bylam can establish the position of the speaking subject without an explicit pronoun. In interaction with AI, this exposes a further problem: a language model does not possess a stable grammatical "I", but reconstructs it contextually and may mirror the user's forms or shift grammatical gender. Roclawski's segmentation-flexional forms are proposed as a diagnostic framework for evaluating tokenization boundaries. More stable modeling of Polish may require sublexical stabilization, anchoring grammatical form in the inflectional system, representing sentence patterns and verbal valency, and maintaining the grammatical "I" in dialogue.

---


### 14. [English Word Sense Disambiguation in 2026: When the Labels Become the Bottleneck](https://arxiv.org/abs/2609.17554)

**<font color=#1a73e8>作者：</font>** Vassili Philippov, Amro Salman, Dmitrii Andreev 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In English all-words word sense disambiguation (WSD), the labels, not the models, have become the bottleneck: frontier LLMs are accurate enough that the errors surviving in the gold standard decide benchmark rankings -- in the test sets we score on and, as we show causally, in the corpus we train on. We release lexEN, a WSD evaluation benchmark built as a conservative, human-adjudicated correction layer over Maru2022's ALL_NEW benchmark (211 labels changed, 56 removed), and SenseBench, an auditable LLM WSD evaluation harness and living leaderboard (57 models, 192 runs). The task is inventory-constrained multiple choice (the model picks from the supplied WordNet senses), so the reported accuracies are a ceiling on what models achieve without that help. On lexEN-v1 the frontier LLMs converge near 95% (best, 95.6%), the top three families are statistically indistinguishable, and accuracy trades off against reasoning effort and cost across a ~2,500x price span. Relabeling SemCor with frontier models and retraining BEM, ESCHER, and ConSeC unchanged lifts them by several F1 points on test sets the relabeling never touched; we release the relabeled corpora and Glite LENS, a 298M bi-encoder trained on the repaired labels -- to our knowledge the strongest reported (83.6 Raganato ALL, 87.4 Maru ALL_NEW) -- serving at ~$0.13 per million items. On hard items, fine-grained WordNet senses are partly ill-posed even for experts (three-reviewer Fleiss kappa=0.537); coarsening raises annotator agreement and model accuracy together across four inventories, placing a top model inside the expert agreement band at coarse granularity (statistically equivalent under three of four) but significantly below it at fine. The binding constraint is now cost.

---


### 15. [Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds](https://arxiv.org/abs/2609.17560)

**<font color=#1a73e8>作者：</font>** Vishnu Bindu Balachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every production model is updated, by retraining, fine-tuning, quantization, or a silent vendor swap, and each update risks being worse than what it replaced. We formalize update promotion as certified paired risk-difference auditing. Our starting point is a support identity: the risk difference between two models lives on the inputs where they disagree, observable without labels. We build DISCERN, a sequential two-tier protocol. A zero-label tier certifies benign updates whose disagreement rate is below tolerance from unlabeled traffic alone. An audited tier labels only sampled disagreements through an anytime-valid confidence sequence, valid at every stopping time and under any label-routing rule, even an adversarial judge. We prove finite-sample validity and matching label-complexity bounds of order rho^2/eps^2 at the rate level, so exploiting free disagreement provably saves a factor 1/rho over any pairing-blind auditor, and the guarantee composes across an unbounded sequence of promotions from one error budget. Across 14,000+ replayed audit streams over 785 update pairs, including LoRA fine-tunes of language models up to 1.4B parameters, miscoverage is 0.0002 (nominal 5%), power 0.986 with zero false alarms, and 56% of benign updates certify with zero labels. Each audit emits a machine-checkable evidence record for post-market monitoring.

---


### 16. [Beyond Static RAG: An Adaptive, Tri-Metric Routing Framework for Efficient Long-Context Inference on Commodity GPUs](https://arxiv.org/abs/2609.17564)

**<font color=#1a73e8>作者：</font>** Saipraveen Vabbilisetty, Ajay Kumar Boddepalli, Deep Narayan Mishra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying retrieval-augmented generation (RAG) on commodity GPUs such as the NVIDIA T4 (16 GB VRAM) exposes a practical failure mode we call the Compression Paradox: neural prompt compression can add key-value (KV) cache contention and preprocessing latency that outweigh generation-time savings, while skipping compression can cause out-of-memory (OOM) failures on long contexts. We identify two distinct failure mechanisms when a vLLM-served LLM and a PyTorch-based compressor are co-deployed under tight memory budgets, and introduce the Tri-Metric Router, a deterministic, training-free policy that selects among Raw, Neural (LLMLingua-2), and Lexical (BM25) pipelines. The router uses three CPU-side signals: spatial complexity ($L$), syntactic density ($\rho_{key}$), and type-token ratio (TTR). Unlike prior semantic-only adaptation, our dispatch signal is hardware-physical, based on VRAM headroom and a latency crossover point. Thresholds are calibrated from profiling on LongBench qasper, yielding an operating crossover near 4,332 words on T4; our contribution is this calibration methodology rather than a hardware-specific constant. On out-of-distribution holdouts, the method achieves 0% OOM failures, 88.5 $\pm$ 4.4% oracle alignment, and 49.3% Combined F1, improving over always-on lexical compression by 5.2 points without additional VRAM or training cost.

---


### 17. [Disentangling Algorithmic Bias from Archival Artifacts: A Controlled Audit of Vision-Language Model Valuation in Metropolitan Museum Archives](https://arxiv.org/abs/2609.17572)

**<font color=#1a73e8>作者：</font>** Manpreet Singh, Rhythm Bhatia, Rahul Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auditing vision-language models (VLMs) for societal bias requires distinguishing direct algorithmic valuation disparities from confounders embedded within archival metadata. In this study, we audit Contrastive Language-Image Pretraining (CLIP) models using historical artwork metadata from the Metropolitan Museum of Art Open Access collection (N = 1,500 total objects; N = 743 attributed works: Male n = 534, Female n = 209; n = 618 anonymous).
We establish a quantitative audit framework evaluating zero-shot CLIP logit differential scores across three semantic prompt pairs (masterpiece, quality, and influence). Unadjusted evaluations demonstrate high score convergence without a statistically significant main gender effect under OpenAI CLIP (mu_F = -0.0067 vs mu_M = -0.0035, p = 0.1829) or OpenCLIP (mu_F = 0.0171 vs mu_M = 0.0237, p = 0.1224). Two One-Sided Tests (TOST) confirm statistical equivalence across Cohen's d >= 0.25 bounds (pTOST < 0.005).
Multivariate OLS regression controlling for artwork medium, creation era, and aspect ratio (R^2 < 0.02) confirms that artist gender has no statistically significant conditional effect (p > 0.20). High residual embedding variance (R^2 < 2%) indicates that global zero-shot valuation metrics operate near an embedding noise floor, showing that broad zero-shot prompt logit differentials are a coarse measurement instrument rather than proving absolute model fairness.
We highlight two key caveats: (i) macro-level score equivalence reflects metric insensitivity to fine-grained visual-semantic features and does not preclude localized micro-level visual biases, and (ii) excluding 41.2% unattributed holdings reflects institutional survival bias. These results demonstrate the necessity of multivariate confound control, equivalence testing, and archival provenance auditing when assessing AI fairness in cultural heritage collections.

---


### 18. [Temperon: Full-Time SAM Quality at a Third Less Wall-Clock](https://arxiv.org/abs/2609.17575)

**<font color=#1a73e8>作者：</font>** Stamatis Mastromichalakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharpness-aware minimization (SAM) doubles the cost of every training step, yet its benefit concentrates where training ends. We study where an expensive training mode should be spent and propose Temperon: a plain-SGD explorer for the first 43% of the epoch budget, then one scheduled hand-off that gives the entire final cosine anneal to a SAM-wrapped Muon refiner. On CIFAR-10/100, SVHN and Tiny ImageNet (five seeds, times reported as epochs-to-target times an idle-GPU-calibrated epoch cost), Temperon matches the best full-time-SAM recipe on accuracy everywhere while reaching the hardest common target 35%, 34% and 32% sooner on three of the four, and sits a tier above the published SAM+SGD recipe at level cost. Ablations make the attribution exact: the Muon refiner is worth +0.85pp with everything else fixed; the explorer's shape and its restarts are worth nothing, and we withdraw them as contributions. Re-running the closest rival, late-phase SAM, at matched budget shows the frontier: it is fastest to every mid-level target, but the tier the Muon refiner buys (0.83 on CIFAR-100, 0.97 on CIFAR-10) is reached by no SGD-refined method in any seed, and on Tiny ImageNet, where Muon buys no tier, the rival simply wins -- the measured boundary of the method. The allocation law transfers to GPT-2 pretraining (full-SAM quality at -29% wall-clock) and GLUE fine-tuning (never worse than full-time SAM at a third of its SAM cost). Two constants organize the economics: skipping SAM early buys a fixed credit, and a Muon epoch costs 1.50x a SAM+SGD epoch on all four datasets. Finally, the hand-off cannot be timed from the trajectory: under cosine schedules the accuracy curve is plateau-then-surge, so the information lives in the schedule, making the scheduled switch principled rather than convenient. Code and a pip-installable implementation are released.

---


### 19. [EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents](https://arxiv.org/abs/2609.17632)

**<font color=#1a73e8>作者：</font>** Sehee Kim, Yumin Choi, Minki Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) trading agents can combine market data, news, and executable analysis, but their behavior is often controlled by static hand-written tool-use policies that are fixed before deployment. This limits their ability to adapt how they gather evidence, invoke tools, verify signals, and manage risk under changing market regimes. We introduce EvolveTrade, a self-evolving framework that treats the system prompt of a tool-using trading agent as a text-parameterized policy. After each update interval, a Policy Agent revises this policy using accumulated decision traces and realized portfolio feedback, while keeping the backbone LLM fixed. The updated policy is then used for the next batch of trading decisions, enabling the agent to refine its information-acquisition and portfolio-construction procedure over time. Experiments across multiple market regimes and two LLM backbones show that EvolveTrade often improves Sharpe Ratio and Cumulative Return over fixed-policy LLM baselines, achieving the improved SR and CR in most evaluated settings. Behavioral analyses further show that self-evolved policies increase code-mediated analysis and activate regime-relevant computations; case-level policy-to-return attributions trace how policy-induced allocation changes contribute to realized return differences. These results suggest that adapting the reusable procedure governing tool use is a key direction for building more robust LLM trading agents.

---


### 20. [What You Can't See Is Still What You Learn: A Preregistered Sixty-Society Confirmation That Evidence Masking Drives Compositional Generalization](https://arxiv.org/abs/2609.17637)

**<font color=#1a73e8>作者：</font>** Narcis Marincat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Restricting what a module can read may improve what a system learns to compute. We test this in a preregistered confirmation with sixty four-cell systems sharing a frozen language-model backbone and communicating through learned continuous packets. Five conditions vary evidence masking, ownership markers, and replacement of foreign evidence with neutral filler, across six initialization clusters, each with two data orders, on one fresh task world. With markers available in both regimes, masking improved accuracy on held-out two- and three-operation compositions by median paired differences of 0.846 and 0.859; all twelve pairs cleared the required margins, and the full preregistered behavioral criterion passed. The unmarked replication also passed. No globally visible system passed the marker-following check, so the effect of usable role information remains unresolved. The filler condition yielded seven full generalizers, but its decomposition criteria were inconclusive. Packet interventions in all eighteen audited masked systems followed the predicted intermediate-value changes on eligible cases; these finite, success-conditioned audits do not establish mediation. The results confirm a large advantage of the tested masking regime, while leaving its finer attribution and generality open. Protocols, results, and checkpoints are public.

---


### 21. [Fathom: Per-Query Read Depth for Sparse Decoding over Offloaded KV Caches](https://arxiv.org/abs/2609.17652)

**<font color=#1a73e8>作者：</font>** Vivek Kalyanarangan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When agentic sessions run to a million tokens with many sessions resident at once, the KV cache and the index that ranks it live in host memory, and the scan that ranks all n keys for a top-k step becomes the traffic that bounds decoding. We present Fathom, a key scan in which each query decides how many bits of each key channel to read. The 4-bit K cache is stored channel-major as bit planes, so a prefix of t planes is exactly the channel's t-bit quantizer, and the query spends its bit budget by reverse water-filling over the variance-weighted importance of its channels. At one million tokens on Qwen3-8B a decode step is 1.67x faster in GPU time than with the 136-bit scans of Double Sparsity, Loki and SparQ r=32, and in the same GPU time as SparQ's 68-bit read (r=16) Fathom reads 18% fewer bytes with lower attention error on six of seven model and context settings. On RULER-style tasks every per-token scan matches exact top-k decoding, and on real coding-agent sessions Fathom reaches the step agreement of the most accurate 136-bit scan at 92 bits. The store is the 4-bit K copy a quantized serving stack already holds, and the method is not faster when the index is resident in GPU memory.

---


### 22. [The Missing "I Don't Know": Why Three Reasoning-Reliability Findings Converge on Calibrated Abstention](https://arxiv.org/abs/2609.17686)

**<font color=#1a73e8>作者：</font>** Srijith Ravikumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Three recent results describe what look like unrelated LLM reliability problems. Yin et al. (2026) show reasoning RL collapses tool-reliability representations. Suleymanov et al. (2026) show that under safety-constrained generation, large models rewrite flagged spans while small models truncate. Bastounis et al. (2024) prove any consistent-reasoning system without an implicit "I don't know" function must hallucinate infinitely often on broad problem classes. We argue these findings converge on a single intervention: calibrated abstention is what each independently identifies as the missing capability, even though the unavailability they document, a capability gap, a policy gap, and a recursion-theoretic gap, has a different source in each case. Honesty post-training has narrowed the gap in deployed models, but principled closure of the class Bastounis identifies requires a calibrated abstention function whose training signal at the leaderboard level is absent: dominant benchmarks assign zero reward to decline, so the leaderboard gradient that would select for the function does not exist. We propose four changes to evaluation: triple-scoring, abstention-rate reporting, capability-stratified evaluation, and mandatory calibration metrics. Benchmark reform is necessary, not sufficient, for closing the gap the theorem identifies.

---


### 23. [CapMem: A Benchmark for Caption-Based Episodic Memory in Egocentric Video](https://arxiv.org/abs/2609.17688)

**<font color=#1a73e8>作者：</font>** Dingli Liang, Yiqiao Xie, Yukai Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wearable assistants require episodic memory over egocentric video, yet current vision-language models face bounded frame budgets, growing visual-token costs, and long-context retrieval failures. Under these practical constraints, we study whether textual captions can serve as reusable episodic memory. We define the Episodic Memory Video Caption QA task and introduce CapMem, a human-annotated benchmark with 75 videos totaling 33.7 hours, and 1,000 multiple-choice questions across 16 scenarios. On long videos (>20 min), full-coverage CaptionQA with 30s and 60s caption windows outperforms direct VideoQA for 10/12 and 8/12 models, respectively. On the same video subset, a matched-frame control across six Qwen models retains mean accuracy gains of 3.22 and 2.55 points, respectively. Our caption-guided retrieve-and-verify harness further improves accuracy by up to 5.3 points. These results support the effectiveness of caption memory for episodic reasoning over long egocentric video.

---


### 24. [GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents](https://arxiv.org/abs/2609.17695)

**<font color=#1a73e8>作者：</font>** Sikun Wang, Yixi Zhou, Lei Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) agent can follow more graph paths without acquiring more independent evidence. GraphEcho tests whether agents mistake these repeated encounters for additional corroboration. The benchmark varies path counts and evidential origins while holding evidence content fixed, and evaluates both judgments and active exploration. Controlled synthetic experiments reveal model-dependent judgment shifts, but redundant supporting paths increase the share of repeated walks across all evaluated frozen agents. Provenance-aware post-training (PAPT) reduces revisits and improves synthetic accuracy, yet covers fewer distinct sources. On scientific claims, it continues to reduce repetition while accuracy declines. These findings expose a gap between efficient exploration and effective evidence use: an agent can learn to stop repeating itself while overlooking information it needs. GraphEcho provides a controlled way to evaluate both what graph agents conclude and whether their exploration reaches distinct evidential sources.

---


### 25. [GVD: Governed Versioning and Deduplication for Document Repositories](https://arxiv.org/abs/2609.17696)

**<font color=#1a73e8>作者：</font>** Mohammadreza Sediqin, Shivali Dalmia, Sumukha Thoppanahalli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document repositories evolve continuously. Guidelines and policies are revised, superseded, and re-uploaded, so the same content recurs in different wording and newer versions refine or contradict earlier ones. These inconsistencies belong to the growing collection rather than to any single document, yet existing work treats versioning, duplicate detection, and contradiction detection as isolated pairwise tasks and stops once a pair is labeled. We present GVD (Governed Versioning and Deduplication), a framework that unifies cross-document version linking with rule-level conflict resolution under an auditable update policy. Incoming documents are assigned to version families through bidirectional rule alignment, and their rules are compared against the family memory to identify duplicates, contradictions, asymmetric refinements, and new knowledge, with Counterfactual Span Probing (CSP) resolving related pairs that inference misclassifies as neutral. Relation-specific policies suppress duplicates and escalate only consequential changes for review, retaining version lineage as an audit trail. The pipeline runs fully locally, with no large language model. On 120 enterprise documents processed as 140 ingestions across 59 version families, GVD reaches an F1 of 0.97 for version-family construction and 0.94 for rule-level consistency, with CSP raising rule consistency from 0.90 to 0.94.

---


### 26. [NeMo Data Designer: An Extensible Framework for Multimodal Synthetic Data Generation](https://arxiv.org/abs/2609.17699)

**<font color=#1a73e8>作者：</font>** Johnny Greco, Nabin Mulepati, Andre Manoel 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present NeMo Data Designer (NDD), an open-source, general-purpose framework for multi-modal synthetic data generation (SDG). Designed to be intuitive to use, NDD provides a declarative configuration format in which human and/or agent users define each dataset column, with column types spanning text, code, structured outputs, images, embeddings, and statistical samplers that are explicitly configured to steer dataset diversity. Additional column types and functionality can be introduced using the framework's flexible plugin system. NDD's configuration is an inspectable artifact, supporting workflow sharing and reproducibility. SDG is an inherently iterative process. NDD therefore builds a preview-and-revision loop into its core workflow, allowing users to generate and inspect a small number of records, refine the specification, and rerun generation at full scale. At runtime, NDD resolves dependencies, schedules calls to user-provided model endpoints, and retries failed requests. We describe NDD's architecture and programming model and present case studies spanning structured, agentic, multimodal, and domain-specialized tasks, including datasets used in Nemotron model development and in production enterprise deployments.

---


### 27. [Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents](https://arxiv.org/abs/2609.17708)

**<font color=#1a73e8>作者：</font>** Caiqi Zhang, Xiaochen Zhu, Chengzu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation is increasingly central to the trustworthy deployment of language models: a calibrated estimate of the probability that an output is correct decides what to ship, what to escalate, and what to retry. Existing confidence estimators, however, share one design premise: they only read the current inference process, either by introspecting on it, scoring its token probabilities, or resampling it. We argue that the current inference is not a sufficient basis for confidence. We propose XConf (eXperiential Confidence): estimating confidence together with the model's accumulated experience. The experience is stored as a record of the model's own graded past episodes, each holding the task, the model's reflection, its stated confidence, the outcome, and a lesson written once the grade arrived. Given a new task, XConf's Recall stage retrieves past episodes on similar tasks met with a similar stated confidence, and reads off their historical success rate; its Reflect stage shows the model this record, has it name its recurring failure mode, and restate a confidence now informed by its own track records. Our estimator is format-general, requiring no logit access or weight updates, and costs only one answer generation. Across nine benchmarks spanning reasoning, coding, multimodal QA, and interactive agents, and four models from three families, XConf beats or matches ten-sample self-consistency in discrimination (AUROC) on 23 of 24 comparisons, with much lower calibration error (ECE), at a tenth of the generation cost. Used for selective prediction, abstaining on the 10% least-confident episodes raises the delivered success rate by up to 8.7 points on agent tasks. We therefore see experiential confidence estimation as a new paradigm for future general-purpose confidence estimation.

---


### 28. ["We Are Tired of Explaining": Communication Practice and AI Roleplay Training for Community Health Workers in Rural India](https://arxiv.org/abs/2609.17710)

**<font color=#1a73e8>作者：</font>** Neil K. R. Sehgal, Sunny Rai, Sai Preethi Matam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Community health workers (CHWs) in the Global South increasingly encounter AI-powered tools, yet the counseling work central to their role remains largely unsupported. We study communication practices among Accredited Social Health Activists (ASHAs) in rural Rajasthan, India, through simulated family-planning calls, semi-structured interviews, and an LLM chatbot roleplay design-probe with 20 participants. In calls, ASHAs often responded to social or material concerns by shifting to health-risk information, denying concerns, promising unspecified help, or listing medical solutions with limited explanation. A smaller set of responses instead engaged concerns, sought permission before involving family members, or left decisions with beneficiaries. We interpret these patterns through Motivational Interviewing, emphasizing restraint from correcting, persuading, or over-solving. Drawing across observed calls, interviews, and probe reactions, we derive design considerations for AI roleplay training: keep AI in a rehearsal role, provide descriptive rather than prescriptive feedback, and evaluate counseling process rather than agreement with prescribed responses.

---


### 29. [SAGE: Governed Artifact Generation from Enterprise Guidelines](https://arxiv.org/abs/2609.17775)

**<font color=#1a73e8>作者：</font>** Mohammadreza Sediqin, Shivali Dalmia, Sumukha Thoppanahalli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise guideline documents mix narrative text, complex tables, and embedded images, and converting them into structured work artifacts still takes two to three days of manual effort each. Current language and vision-language models extract from such documents but offer no governed workflow beyond extraction: no validation, no consistency checking, no traceable artifact generation. We introduce SAGE, a governed multi-stage LLM pipeline organized around a shared versioned rule store with stable identifiers, schema-validated inter-stage contracts, and end-to-end provenance tracking. Extracted rules undergo deterministic structural validation and LLM-based semantic scoring, then a consistency module that removes duplicates, flags contradictions, and surfaces specification gaps; only uncertain or flagged items reach reviewers, while high-confidence outputs are auto-approved. On 120 documents, SAGE cuts turnaround from days to 20-100 minutes, achieving a 96% document-level success rate with 3.2% hallucination, extracting 3,896 rules and producing 812 artifacts ready for human review; without governance, hallucination rises to 15.7%.

---


### 30. [FairCompressAgent: An Agentic Framework for Fairness-Aware Model Compression for FPGA Deployment](https://arxiv.org/abs/2609.17786)

**<font color=#1a73e8>作者：</font>** Yuanbo Guo, Yiyu Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fairness-aware model compression requires selecting methods and configurations that balance accuracy, fairness, and deployment cost. These decisions become more difficult when compression methods are composed or the user's requirements change. In this paper, we propose FairCompressAgent (FCA), an agentic framework that integrates fairness-aware pruning, incremental quantization, and sparse low-rank factorization through a common operator interface. A language-model planner uses model profiles and measured outcomes to select compression configurations, while an execution layer performs compression, fine-tuning, evaluation, and constraint-based selection. FCA also supports requirement updates and reports the remaining violation when a request cannot be satisfied. Experiments on Fitzpatrick-17k with VGG-11 compare four search methods over 40 measured configurations. Under the accuracy-constrained request, FCA selects a compressed model with 59.54% less inference tensor storage, while validation average precision increases from 0.5141 to 0.5233 and equalized opportunity (EOpp) decreases from 0.2251 to 0.2168. It reaches the same final selection as one-shot planning with 7.33 versus 12 candidate evaluations on average, under their respective stopping policies. Repeated fine-tuning, held-out testing, and online requirement updates characterize the stability and interactive use of this compression workflow. The results demonstrate how measured feedback and explicit constraints support the selection and interactive refinement of fairness-aware compression configurations.

---


### 31. [Not All Patches Are Equally Forgettable: Spatially Localized Domain Unlearning in Vision-Language Models](https://arxiv.org/abs/2609.17790)

**<font color=#1a73e8>作者：</font>** Akanksha Singh, Vinod K. Kurmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision-language models (VLMs) exhibit strong cross-domain recognition performance even without additional training. However, this robustness can also preserve undesirable domain-specific behavior, as domain-related and semantic information often remain entangled within the learned representation space, making selective domain unlearning challenging. Existing approaches typically address this problem through latent-space disentanglement and prompt- or feature-level interventions, without directly attributing and attenuating individual patch-token contributions. However, here we suggest that rather than uniformly suppressing the full representation, it may be more effective to exploit the spatial structure of vision transformers to localize and suppress patch regions that contribute disproportionately to forget-domain prediction. Patches that strongly influence forget-domain prediction may not be equally important for semantic recognition, suggesting that forgetting should be guided according to the domain contribution of different visual regions. Specifically, we propose a two-stage patch-selective framework that first estimates patch-level domain sensitivity and then selectively attenuates patches whose contribution to forget-domain prediction is stronger than their semantic utility. We evaluate our framework on Office-Home, Mini DomainNet, and DomainNet. Experimental results demonstrate improved forgetting-retention tradeoffs compared to prior methods while improving retained-domain recognition by up to 3.8\%. Additional evaluations under visually overlapping and unseen-domain settings further demonstrate improved robustness under distribution shift.

---


### 32. [AgenTeeth: A Model-Agnostic Framework for Suppressing Hallucination in Frozen Vision-Language Models on Dental X-Rays via Tool Evidence Injection](https://arxiv.org/abs/2609.17800)

**<font color=#1a73e8>作者：</font>** Ahmed Rafid, Fariya Ahmed, Rumman Adib 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) remain largely unreliable on panoramic dental radiographs and can rely on learned anatomical priors rather than evidence in the image. This is particularly problematic for tooth localization and spatial reasoning, and fine-tuned dental VLMs can retain the same spatial biases. We present AgenTeeth, a model-agnostic, tool-augmented framework that grounds frozen VLMs using seven specialized dental vision experts. A question-aware orchestrator selects the relevant tools, whose detections are mapped to FDI tooth numbers or anatomical regions and returned as structured findings together with annotated image overlays. A fresh synthesis call then answers the question using this evidence, without fine-tuning the underlying VLM. On MMOral-OPG-Bench, AgenTeeth improves four backbone VLMs by 12.9-23.0 percentage points over their baselines. Our strongest configuration reaches 65.66% on open-ended VQA, compared with 45.35% for OralGPT-Plus. The advantage also holds at matched scale: a frozen Qwen2.5-VL-7B-Instruct with AgenTeeth reaches 48.11%, exceeding OralGPT-Plus built on the same backbone after supervised fine-tuning and reinforcement learning for tool use. We release the framework, all seven expert models, and a dentist-annotated dataset for alveolar bone-loss detection in panoramic radiographs.

---


### 33. [A Four-Stage Decomposition of Word-Problem Solving and Mechanistic Fragility in LLM Math Reasoning](https://arxiv.org/abs/2609.17804)

**<font color=#1a73e8>作者：</font>** Zhongdi Qu, Carla P. Gomes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models solve grade-school math word problems with high accuracy, yet a single irrelevant clause inserted into the problem can collapse it. We reconcile these observations with a mechanistic account. We show that the model's internal computation decomposes into a four-stage sequential pipeline, Schema Abstraction, Operation Planning, Operand Binding, and Computation, each stage producing a distinct intermediate representation in an identifiable band of layers. Using the same scaffold to diagnose distractor-induced failure, we localize the corruption to a single stage, Operation Planning, implemented by a set of attention heads whose causal role we validate bidirectionally. In short, we provide a mechanistic interpretation of math word problem reasoning in LLMs, and their failure when distracted.

---


### 34. [Evaluating the Impact of Personalization in Conversational Cybersecurity Assistants](https://arxiv.org/abs/2609.17839)

**<font color=#1a73e8>作者：</font>** Lea Duesterwald, Anika Jain, Shreya Kochar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Users increasingly turn to Large Language Models to answer a variety of questions, including cybersecurity questions. We study how personalization strategies can help improve the effectiveness of answers to questions asked to an LLM-based cybersecurity assistant. Beyond accuracy, we focus on the understandability, actionability and, most importantly, motivating power of answers, given how often users fail to follow cybersecurity recommendations. Specifically, we investigate four personalization strategies, ranging from static user profiles to interaction-history-based personalization, using a corpus of 1,045 real-world cybersecurity questions and a 7-day deployment involving 57 participants and 1,066 user questions. Across both a large-scale automated LLM-based evaluation and human evaluation, conversation-based personalization is consistently favored in comparative ratings of perceived helpfulness and likelihood of following security advice. Importantly, the relative trends observed in the LLM-based evaluation align with those obtained from human evaluation, suggesting that LLM-based evaluation can provide a scalable mechanism for comparing personalization strategies before costly user studies. These results indicate that behavior-driven personalization is a promising direction for LLM-powered cybersecurity assistants and highlight the value of combining LLM-based and human evaluation when studying personalized language-model systems.

---


### 35. [Lexara-RF: Reference-Free Metrics for Evaluating Conversational Visual Analytics Agents](https://arxiv.org/abs/2609.17842)

**<font color=#1a73e8>作者：</font>** Srishti Palani, Vidya Setlur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational visual analytics (CVA) agents powered by large language models generate visualizations and natural-language explanations from open-ended queries. Evaluating these multimodal outputs is challenging: curated reference benchmarks are costly to author, cannot comprehensively capture the space of valid responses, and are unavailable in production. Building on the Lexara evaluation framework, we introduce Lexara-RF, a reference-free set of metrics that scores CVA outputs using only the prompt, data, and model response. We reformulate evaluation as verification: 13 metrics operationalize visualization design theory and Gricean cooperative principles as computable consistency, intent-alignment, and design validity checks. On a human-rated corpus of CVA test-cases, Lexara-RF achieves alignment comparable to reference-based formulations, outperforms surface-similarity NLG baselines, and localizes structurally grounded failures with high accuracy.

---


### 36. [SFT or RL for Tool-Calling Agents? A Controlled Study Across Data, Method, and Scale](https://arxiv.org/abs/2609.17848)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Limited controlled evidence exists on how training data, adaptation method, and model scale jointly affect tool-calling performance in language-model agents. We evaluate supervised fine-tuning (SFT) with LoRA, reinforcement learning (RL) via Group Relative Policy Optimization (GRPO), and SFT followed by GRPO across six Qwen3 models from 0.6B to 32B parameters, covering both in-distribution performance and cross-dataset transfer. SFT with LoRA is the strongest in-distribution method throughout the 0.6B-32B range and best in 15 out of 18 experimental settings. On cross-dataset transfer, the methods are closer: GRPO wins 29 out of 54 settings where training and test datasets differ, but its margin over SFT averages under one point, and SFT->GRPO is rarely strongest in either comparison. Dataset mixing gives consistently strong transfer while staying close to specialized in-distribution training, regardless of method. Additional analysis further confirms that LoRA outperforms full-parameter fine-tuning, demonstrating that LoRA better preserves pretrained agentic behavior.

---


### 37. [AfriSyCo: Measuring Assertive Framing, Verification, and Wording Sensitivity Around African-Language Content](https://arxiv.org/abs/2609.17853)

**<font color=#1a73e8>作者：</font>** David Ababio Awuni, Rose-Mary Owusuaa Mensah Gyening, Elvis Gyasi Owusu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AfriSyCo studies answer switching around African-language factual content with two complementary layers: native-language follow-ups and a controlled cross-language factorial whose question, options, and target remain in the African language while the follow-up framing is English. We analyze 1,415 turn-1-correct model-language-item observations derived from 100 source questions across seven open-weight checkpoints and six languages; turn-1-correct denotes observed first-response accuracy, not demonstrated knowledge. Under native prompts, assertive endorsement produces 29.3 percentage points more any-turn false-target selection than mention-plus-verification (M+V), with a 19.0-point immediate T2 contrast. In the precommitted 2 x 2 factorial, averaged over three tested prompt families, assertive framing increases target selection by 30.4 points (95% CI [28.4, 32.3]); verification decreases it by 17.4 points, while the assertive effect rises from 20.5 points without verification to 40.2 with it (interaction +19.7). The effect remains 34.8 points among 611 observations correct after option reordering. Magnitude varies sharply by wording and checkpoint: prompt-family effects span 20.1-42.5 points, a Twi/Qwen3 paraphrase shifts target selection from 70.8% to 4.2%, and checkpoint effects span 9.2-47.0 points. Prompt realization is therefore part of the measurement problem.

---


### 38. [Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels](https://arxiv.org/abs/2609.17857)

**<font color=#1a73e8>作者：</font>** David Ababio Awuni, Luke E. K. Achenie, Benjamin Tei Partey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Who the judge is can affect an LLM-as-judge result, but measuring that effect without confusing it with candidate quality is difficult. We study four open-weight families (Llama 3.1, Qwen 2.5, Gemma 2, and Yi 1.5) in a fully crossed pairwise design with 9,312 judgments. A common per-family statistic is strongly confounded with candidate quality and correlates with Bradley-Terry ability at r = 0.95. We derive a corrected estimator that holds the candidate family fixed and compares judges. All four families then show a positive same-family lift (3.4-8.4 percentage points), with global FPS 0.067 (95% CI [0.053, 0.084], permutation p = 0.0002). The effect remains under panel-based quality controls, an independent human-consensus anchor, and a float16 judging replication. Judge-side likelihood is closely related to the effect: adding likelihood advantage reduces the controlled coefficient by 61%, which we treat as descriptive attenuation rather than causal mediation. Position is a separate failure mode. Across the panel, 55.4% of AB/BA pairs reverse, and reversal above 50% is incompatible with a simple independent content-noise model. Relative to a family-balanced reference, panel composition changes 18.5% of pairwise outcomes. A complete reproducibility archive has been prepared for public release.

---


### 39. [The Inference Engineering Pareto Atlas: Which Optimizations Dominate the Cost, Quality, and Latency Frontier?](https://arxiv.org/abs/2609.17863)

**<font color=#1a73e8>作者：</font>** Srikanta Datta Tumkur, Jay Iyer, Mehar Simhadri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM inference optimizations report speedups on different models, GPUs, prompts, and quality metrics, making them hard to compare or combine. We build a cost, quality, and latency Pareto atlas to identify the best configurations for different deployment constraints. Since exhaustive testing is impractical, we measure 54 configurations of Qwen2.5-7B-Instruct running on vLLM 0.12 across L4, A100, and H100 GPUs and use these anchors to calibrate a simulator. It reproduces measurements at anchored batch sizes, with cross campaign drift below 1.5 percent. A separate quality evaluation tests FP16, AWQ 4bit, FP8 weights, and FP8 KV cache on 200 GSM8K questions with five examples per prompt. Sparse attention is evaluated only in simulation. On the calibrated grid, 18 of 36 configurations reach the Pareto frontier. Combined methods reach it more often than individual methods, with 9 of 15 combinations versus 9 of 21 single methods. Quality testing changes the winners. AWQ 4bit reduces per token latency to 0.34 times baseline on L4 but loses 5.9 percent of strict GSM8K accuracy, narrowly missing the 95 percent quality floor within sampling uncertainty. Flexible answer extraction matches FP16 accuracy, suggesting the loss comes from formatting rather than arithmetic. FP8 weights retain 99.4 percent of baseline accuracy at 0.61 to 0.65 times baseline latency across all three GPUs and appear in three of four regime winners. A naive FP8 KV cache maintains normal throughput but answers none of the 200 questions correctly, showing why speed alone is insufficient. Under two prompt designs, n gram speculative decoding measures at 0.90 to 0.98 times baseline and adds no benefit on this stack. The best choice depends on the constraint and GPU: H100 wins for tight latency, while A100 wins for throughput and low cost at 0.106 dollars per million tokens.

---


### 40. [Do Frontier Models Seek Safety Evidence Before Acting?](https://arxiv.org/abs/2609.17865)

**<font color=#1a73e8>作者：</font>** Omer Tafveez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier models are often evaluated on how they respond to safety information once it is already in context. We study an earlier decision point: whether models choose to acquire safety-relevant evidence before acting. We introduce SAFE, a controlled benchmark in which models make deployment decisions with optional evidence that varies in retrieval cost, probability, severity, and presentation. Across GPT-5.5, o3, Claude Opus 4.8, and Claude Sonnet 4.6, we find distinct evidence-acquisition policies: Opus inspects nearly by default, o3 is the most skip-heavy and threshold-sensitive, and GPT-5.5 and Sonnet occupy intermediate regimes. Inspection increases strongly with severity and decreases with retrieval cost, whereas probability has much weaker behavioral influence: increasing the stated likelihood of a problem from 10% to 70% changes inspection by at most 21 percentage points. Despite these differences, Stage 1 rationales are dominated by expected-value reasoning across models. A cost-obligation decomposition further shows that avoidance is driven primarily by retrieval friction and explicit threats to the deployment payoff rather than by the remediation duties created by knowing. Counterfactual interventions reveal a further mismatch between behavior and explanation: evidence framing can strongly change decisions near the inspection boundary while going largely unmentioned, whereas probability is frequently cited despite having little causal influence. These results suggest that deployment-time safety depends not only on how models respond to known risks, but also on whether they acquire the evidence needed to know that acting is safe.

---


### 41. [Lumen: Parameter-Efficient Alignment of Pretrained Vision and Language Encoders for Zero-Shot Computational Pathology](https://arxiv.org/abs/2609.17868)

**<font color=#1a73e8>作者：</font>** Kiarash Tajbakhsh, Abdelrahman Faqieh, Michael Jopiti 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language models are commonly built by pretraining or fine-tuning large encoders on paired image-caption data. We asked whether a pathology vision-language model can instead be assembled by parameter-efficient alignment of frozen unimodal foundation models, leaving their pretrained representations untouched. Here we present Lumen, which aligns frozen Virchow2 and BioMedBERT backbones using rank-4 adapters and projection heads, training only 0.40% of the total parameters on the public QUILT-1M corpus. Across nine public zero-shot patch benchmarks, Lumen achieved the highest mean chance-corrected balanced accuracy, 0.546 versus 0.461 for the strongest baseline (paired difference 0.086, 95% CI 0.042-0.136). On lymph-node metastasis detection, Lumen reached an AUROC of 0.964 (95% CI 0.956-0.971) on 4,214 held-out internal slides and 0.955 (95% CI 0.942-0.966) on 2,368 slides across nine external cohorts and six organs. At the internally calibrated threshold, it outperformed all vision-language baselines, with a balanced accuracy of 0.909 (95% CI 0.896-0.923) internally and 0.915 (95% CI 0.902-0.929) externally. Lumen performed competitively across the evaluations, with the exception of cross-modal retrieval, where it ranked third behind CONCH and PathGen-L/14. Fully fine-tuning both encoders gave Lumen no consistent benefit over low-rank adaptation, although it improved retrieval. Aligning frozen unimodal foundation models therefore yields strong and transferable performance at patch and slide level while training only a small fraction of the parameters.

---


### 42. [Can VLMs Reliably Assess Sidewalk Accessibility Attributes from Pedestrian-Level Imagery?](https://arxiv.org/abs/2609.17882)

**<font color=#1a73e8>作者：</font>** Seung Jae Lieu, Diego Morra, Chiara Cadoni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An important component of urban accessibility, particularly for wheelchair users and people with reduced mobility, is sidewalk compliance with measurable requirements. We test whether effective width, longitudinal slope, cross slope, and pavement condition can be assessed reliably from pedestrian-level imagery using vision-language models (VLMs). We present the first application of sampling-based conformal prediction (CP) for VLM-based accessibility assessment. We evaluate four VLMs on 514 sidewalk images from Seoul, South Korea, with field-measured ground truth. Conformal calibration attains the nominal 90% coverage for all models and attributes, but the calibrated regions differ in informativeness. Effective width yields the most informative estimates, with a mean interval half-width of about 1.0 m for the best model. Since every model overestimates width, asymmetric calibration shortens the intervals by up to 33% at unchanged coverage. Longitudinal slope is marginally informative, cross-slope intervals are too wide to resolve regulatory thresholds, and pavement-condition sets degenerate to all five grades (A-E) for three of the four models. Uncalibrated intervals from raw sampling dispersion cover only 17-47% of field-measured values at a nominal 90% level. Among the images with the most self-consistent responses, these intervals miss the field-measured value in up to 96% of cases. Response self-consistency is therefore not evidence of accuracy, and sampling dispersion cannot be interpreted as uncertainty until it has been calibrated against field-measured ground truth. No quantitative attribute reaches the precision required for general compliance assessment, but CP identifies from calibration data alone which attributes can support screening of segments far from the thresholds. We release the annotated pedestrian-level images and their corresponding field-measured attribute values.

---


### 43. [Does AI Assistance Leave a Temporal Fingerprint? Detecting Overreliance in AI-Assisted Writing and Programming](https://arxiv.org/abs/2609.17883)

**<font color=#1a73e8>作者：</font>** Eduardo Davalos, Yike Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of generative AI has made final artifacts unreliable evidence of student learning, and AI detectors that examine only the finished product are inaccurate and ethically contentious. Process data offers an alternative, but prior work covers only English essay writing. We ask whether AI assistance carries a temporal signature, whether it generalizes from writing to programming, and whether it distinguishes ordinary collaboration from wholesale delegation. We analyze three public corpora: CoAuthor (1,447 keystroke-level co-writing sessions), RealHumanEval (editor telemetry from 243 programmer records), and a pre-LLM CS1 corpus (5.1 million keystrokes) as a human-only baseline, comparing minimal-AI work, collaborative AI use, and simulated wholesale delegation. Three findings emerge. First, the signature generalizes: AI contributions arrive in bursts far outside the author's own baseline in both mediums (paired d_z = 1.13 and 3.54). Second, engagement diverges by medium: 93% of AI-inserted characters survived to writers' final documents, while only 14% of accepted code suggestions survived intact. Third, classifiers using only observable temporal features separate simulated delegation from authentic work nearly perfectly (F1 $\geq$ 0.997; at most 0.5% of real work misclassified), while ordinary collaboration remains hard to distinguish from unassisted work. Temporal evidence flags wholesale delegation rather than assistance, positioning process visibility as a candidate evidentiary basis for academic integrity, pending validation in authentic coursework.

---


### 44. [ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software](https://arxiv.org/abs/2609.17885)

**<font color=#1a73e8>作者：</font>** Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents that operate through screenshots and simulated actions are advancing rapidly, yet their evaluation remains anchored to general desktop and web tasks. Enterprise Resource Planning (ERP) systems run the finance, procurement, inventory, and customer operations of organizations worldwide, and pose distinct challenges for computer-use agents: dense interfaces, coordinated multi-step interactions, and errors that alter persistent business records rather than surfacing on screen. Existing enterprise benchmarks rely on proprietary platforms or on simulated approximations of such software. We introduce ERPBench, a benchmark that evaluates screenshot-only agents on a live and reproducible ERP system and scores each task against ground-truth values in its database. Beyond the benchmark, we present a production-grade harness that gates agent actions behind human approval for safe deployment, which ERPBench runs autonomously. Evaluating six closed and open-source agents, we demonstrate that strong general GUI performance does not transfer to enterprise reliability. Even when an agent reaches the right form and saves it, the stored record is often wrong: some agents save in up to 85% of runs but write the correct value in as few as 3%. We further characterize failure modes specific to enterprise workflows.

---


### 45. [Long-Context Demonstration Selection Using State Space Models](https://arxiv.org/abs/2609.17888)

**<font color=#1a73e8>作者：</font>** Ziniu Zhang, Zhenshuo Zhang, Ruoxuan Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of demonstration selection, which involves selecting a subset of examples for prepending to a query to a language model. This problem is closely related to in-context learning and language model inference. Since the inference cost of a transformer model scales quadratically with sequence length, the selection problem becomes especially challenging in a long-context scenario. In this paper, we tackle this problem by building on state space models (SSMs), which require only linear inference time given the input. Our approach involves two algorithms. The first learns a small set of SSMs through distillation of a (trained) transformer model. We partition all the layers into consecutive groups. Then for each group, we estimate a separate state space model to replicate the input-output behavior within the adjacent layers. Second, we map the distilled model outputs to a small set of tokens, and apply these embeddings for demonstration selection in downstream applications. We perform extensive experiments in both synthetic and real-world datasets to validate our approach. We demonstrate that the distilled SSMs only incur an approximation error of less than $0.7\%$ relative to the true output. In downstream evaluation, we show that on several text classification and reasoning tasks, our approach reduces FLOPs by $14.2\times$ and improves accuracy by $6.48\%$ relative to baseline demonstration selection methods.

---


### 46. [OBC-Prune: Outcome-Based Calibration for Large Reasoning Model Pruning](https://arxiv.org/abs/2609.17890)

**<font color=#1a73e8>作者：</font>** Ha Lan Nguyen, Huy Hoang Tran, Trac-Duy Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) generate long chain-of-thought traces before answering, creating significant inference overhead. Pruning can reduce this cost, but its effectiveness depends on the calibration data used to estimate parameter importance. Recent work calibrates on the model's own rollouts instead of generic dataset, but treats all reasoning tokens uniformly, regardless of whether they contribute to successful reasoning. As a result, pruning protects weights by statistical salience rather than by their contribution to correct reasoning, so weights behind erroneous computation survive as readily as those behind correct computation. These erroneous patterns then get carried into the pruned model, degrading reasoning quality, producing both lower accuracy and longer reasoning traces. We propose Outcome-Based Calibration for Large Reasoning Model Pruning (OBC-Prune) to close this gap. OBC first constructs difficulty-matched pairs of correct and incorrect rollouts from problems the model answers inconsistently. It then estimates the causal importance of each reasoning sentence through intervention-based analysis, quantifying how removing its influence affects subsequent predictions. These causal importance scores are converted into per-token weights that rescale the calibration activations used by one-shot pruning methods (SparseGPT, Wanda, ALPS), without modifying the underlying pruning algorithms. Experiments on DeepSeek-R1-Distill-Qwen 1.5B, 7B, and 14B models at 40\% and 50\% sparsity demonstrate consistent improvements over state-of-the-art calibration baselines across most model sizes and sparsity levels on MATH500, LiveCodeBench, and AIME 2025. These results indicate that preserving causally important reasoning circuits is a substantially more effective pruning objective than uniformly preserving observed activations.

---


### 47. [Collaborative Memory for Multi-Agent VLM Systems](https://arxiv.org/abs/2609.17921)

**<font color=#1a73e8>作者：</font>** Huixin Zhang, Shao-Jun Xia, Di Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) agents combine specialized perception, tools, and reasoning to address complex visual tasks. In multi-agent settings, different agents inspect different image regions, video frames, or visual representations, so collaboration extends beyond distributed reasoning to distributed perception. This makes shared visual context a central problem in VLM agent collaboration. In this paper, we frame memory hierarchy, cross-agent sharing, and consistency mechanisms around the need to reconcile interpretations and update dependent reasoning. Effective collaboration requires agents to build on contributions from other agents, recover missing visual context, and reconcile differing interpretations as new evidence emerges. Shared visual memory preserves not only images or textual summaries but also the dependencies among observations, agent interpretations, and subsequent reasoning. Together, these design considerations shape how information flows and evolves across VLM agents. The proposed framework provides a foundation for building reliable and resource-efficient agent teams.

---


### 48. [AI Mediators Regulate Emotion and Create Value in Disputes](https://arxiv.org/abs/2609.17933)

**<font color=#1a73e8>作者：</font>** James Hale, Jonathan Gratch  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In conflict and disputes, especially, emotion acts as a salient force in influencing outcomes. Prior work shows negative affect can obstruct collaborative behaviors, which typically lead to ``win-win'' outcomes. Thus, some suggest mediators may help regulate emotion and achieve joint gains. With the proliferation of AI, we posit LLMs may perform well at this task, with the added benefit of better accessibility compared with a human mediator. To examine the effectiveness of AI versus novice human mediators, we conduct a between-subjects experiment, where participants engage in a dispute mediated by a human, AI, or no mediator. We first analyze how well the mediators regulate emotions within a dispute -- finding AI mediators perform significantly better than humans at reducing negative emotion. We next examine whether AI mediators facilitate disputants better realizing joint gains in disputes with high integrative potential (IP) -- we find a marginally significant interaction between IP and condition (AI versus human), indicating LLMs may outperform humans at aiding disputants realize joint gains. Lastly, we perform an analysis of the messages the mediators sent, finding the AI sent significantly more messages suggesting trade-offs compared to the humans.

---


### 49. [Beyond the Previous Layer: Residual Predictive Structure in Sparse MoE Routing](https://arxiv.org/abs/2609.17940)

**<font color=#1a73e8>作者：</font>** Hao Li, Yasuyuki Tahara, Yuichi Sei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts models route each token through a sequence of expert selections. We ask whether the immediately preceding selection adequately summarizes this trajectory for predicting the next router. Using frozen OLMoE and JetMoE models, we measure the held-out predictive gain from earlier expert selections while retaining the most recent selection as a common baseline. In OLMoE, extending the history from one to eleven layers raises router-logit $R^2$ from 0.59879 to 0.66544. A preregistered JetMoE replication yields four-layer gains of 0.14275 and 0.20528 at two target depths, with paired bootstrap intervals above zero. These gains survive nonlinear decoding: adding history to a small multilayer perceptron improves $R^2$ by 0.17137 and 0.21861, whereas nonlinear decoding of the recent state alone adds 0.00139 and 0.00936 over a linear probe. Parameter-matched controls preserve the advantage, and cross-fitted history residuals predict target residuals with $R^2$ of 0.20549 and 0.23556. These findings identify residual predictive structure in expert-selection trajectories beyond adjacent-layer persistence.

---


### 50. [ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference](https://arxiv.org/abs/2609.17943)

**<font color=#1a73e8>作者：</font>** Amir Ziashahabi, Hossein Entezari Zarch, Lei Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by attention, whose repeated KV-cache reads make decoding memory-bound. Self-speculative decoding alleviates this by drafting tokens with sparse attention and verifying them with full attention, but existing batched methods remain synchronized: all requests in a batch share a single draft-verify schedule, even though the optimal draft length varies widely across requests and changes dynamically within each request. We propose ASPIRE, a non-synchronized batched self-speculative decoding framework built on three components. First, a unified mixed forward allows drafting and verifying requests to coexist in the same batched forward pass, removing the need for global draft-verify phases. Second, a lightweight online speculation scheduler uses per-request acceptance-rate estimates and a batch-aware cost model to let each request independently choose when to verify. Third, an intra-draft refresh layer performs full attention at a single designated layer during drafting, updating the sparse context at every draft step to reduce staleness during drafting. Across three models and five reasoning and long-context benchmarks, ASPIRE achieves $1.70$-$4.58\times$ speedup in decoding throughput over autoregressive baselines and improves average speedup by approximately $27\%$ over the strongest prior self-speculative baselines.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-210](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
