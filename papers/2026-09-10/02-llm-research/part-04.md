# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 151. [LLMs Mirror Country-Specific Gender Patterns If Asked, but Skew Male When Generating Media in Local Languages](https://arxiv.org/abs/2609.06545)

**<font color=#1a73e8>作者：</font>** Sharif Kazemi, Tanya Popli, Neil K. R. Sehgal 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate media, but whether their content perpetuates gender stereotypes is unknown: standard benchmarks rely on selection-based formats rather than long-form generation, and surveyed baselines for local gender associations are scarce outside the West. We collect gender associations for 22 occupational and domestic roles from 695 respondents across the United States, India, Kenya, and Nigeria, and evaluate eight LLMs under two regimes: direct questioning and media generation. Models track the surveyed associations under direct questioning but skew substantially more male under media generation in major local-language cells, consistent with the male bias documented in human-produced media. Outside the US, the shift is much smaller and non-significant under English prompting, so English-only or country-agnostic evaluation would miss this bias in the languages where these models are most deployed. Instruction prompting reduces the shift directionally, but trades off against alignment with the surveyed associations. Evaluating LLM gender bias for global deployment therefore requires generation-format testing, local-language prompting, and locally-collected human baselines.

---


### 152. [Hidden in Plain Sight: The Overlooked Significance of Canonical Elements for Extreme LLM Sparsity](https://arxiv.org/abs/2609.06557)

**<font color=#1a73e8>作者：</font>** Hyeondo Jang, Kwanhee Lee, Dongyeop Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often considered fragile under aggressive sparsification, and maintaining reliable performance typically requires sticking to moderate sparsity levels. However, recent studies suggest that LLMs are more resilient to high sparsity than previously thought, reframing the problem as a design challenge rather than a fundamental limitation. In this work, we challenge the perceived limits of unstructured post-training LLM pruning by revisiting elementary pruning strategies that have remained relatively underexplored at this scale. Through a progressive sparsification framework with second-order saliency and continued training coordinated with sparsity progression, we show that pretrained LLMs can retain strong performance far beyond commonly studied sparsity regimes. Across LLaMA-2 and Qwen-3 model families, our approach improves perplexity and downstream accuracy up to 99\% sparsity, surpassing both the current state-of-the-art and representative baselines. Precisely, on LLaMA-2-7B, our approach achieves WikiText-2 perplexities of 13.48 and 19.67 at 95\% and 99\% sparsity, respectively, while delivering 3.23$\times$ decoding speedup and 6.21$\times$ memory savings at 95\% sparsity. Taken together, our results show that LLMs can be pushed into extreme sparsity while retaining strong performance, providing a foundation for further improving sparse models in this regime.

---


### 153. [MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games](https://arxiv.org/abs/2609.06563)

**<font color=#1a73e8>作者：</font>** Hwang Yechan, Bae Sangjun, Kim Jeongmo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments. While recent LLM-agent approaches improve gameplay through prompting and preference optimization, they often optimize actions and in-game speech without explicitly grounding them in such beliefs. This frequently leads to strategically inconsistent behavior, especially for compact LLM agents. We introduce Multi-Agent Relational Belief Optimization (MARBO), a belief-grounded preference optimization framework that leverages relational beliefs to guide strategic decisions and in-game speech. MARBO provides preference feedback only when behaviors are supported by reliable relational beliefs and lead to strategically favorable social outcomes, encouraging more consistent learning under uncertainty. Experiments on representative SDGs show that MARBO enables compact LLM agents to consistently outperform existing baselines. The Code is available on this https URL.

---


### 154. [Learning to Use Imagination: Progress-Conditioned Future Utilization for World Action Models](https://arxiv.org/abs/2609.06578)

**<font color=#1a73e8>作者：</font>** Yijie Zhu, Zitong Yu, Wei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) extend Vision-Language-Action (VLA) models by incorporating future visual dynamics into action generation. However, existing WAMs often utilize imagined futures with limited adaptation to evolving execution progress, potentially introducing distracting or unreliable predictive cues. This limitation arises from two empirically identified forms of non-uniformity in future utility: (i) at the inter-progress level, the utility of imagined futures varies across execution stages as control demands change; and (ii) at the intra-progress level, individual future latents exhibit heterogeneous relevance within the same progress state. To address these limitations, we propose ProWAM, a Progress-Conditioned World Action Model that introduces execution progress as an explicit intermediate representation for adaptive imagination utilization. ProWAM comprises two tightly coupled components: (1) To obtain a reliable representation of execution progress, we propose the Self-Supervised Dual-Temporal Progress Encoder (SS-DTPE). SS-DTPE couples short-term action-observation interaction modeling with long-term recurrent progress aggregation to capture recent execution feedback and accumulated task history. (2) Conditioned on the progress representation from SS-DTPE, we propose the Hierarchical Progress-Conditioned Imagination Modulation (HPIM) to adapt imagination utilization to execution progress. HPIM operates at two complementary levels: an inter-progress global modulation mechanism adapts future utilization across execution stages, while an intra-progress relevance mechanism differentiates individual future latents within each progress state. Extensive experiments demonstrate consistent gains over strong VLA and WAM baselines.

---


### 155. [SAGE: A Hierarchical Framework for Evaluating Interpretive Literary Quality in Narratives](https://arxiv.org/abs/2609.06611)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Nianjun Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing the literary quality of narratives requires evaluating interpretive dimensions (cultural representation, emotional depth, and philosophical engagement) that existing NLG metrics cannot measure. We introduce SAGE, a six-layer evaluation framework that separates rule-based assessment of observable textual properties from LLM-based evaluation of interpretive qualities drawn from cultural theory, affect theory, and existentialist philosophy. Each interpretive layer is assessed through multi-round iterative LLM evaluation with independent cross-validation, achieving measurement-grade reliability (98.8% convergence, >94% inter-rater agreement) stable across evaluator models. Validated on 600 evaluations across 100 short stories, our central finding is a systematic capability boundary: emotional-psychological representation approaches human levels, while cultural critique and philosophical depth exhibit approximately double the gap. LLM-generated narratives score below even commercial genre fiction on all three layers. We interpret this as a boundary between pattern-reproducible literary capacities learnable from training corpora and stance-requiring ones demanding cultural positioning and philosophical engagement that pattern matching alone cannot provide.

---


### 156. [Physico-Geospatial Grounded Scene Interpretation for Mobile Robotics](https://arxiv.org/abs/2609.06629)

**<font color=#1a73e8>作者：</font>** Nicolas Schuler, Janik Kurtz, Lea Dewald 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in deep learning allow robotic agents to interact with dynamic and unstructured environments. Of special interest is the integration of physico-geospatial world knowledge into such systems, either by using physics-aware machine learning models, knowledge graphs to model relationships or spatio-temporal and logical reasoning. In the present work, we introduce an approach to augment the output of pre-trained, unmodified VLMs used for scene interpretation by integrating semantic descriptions, OpenStreetMap building data and street information with positional, temporal and metric information obtained from our sensory systems, fusing this information using LLMs. We apply this concept to an outdoor recording within a university campus, achieving an F1-Score of 0.83 in the task of grounding buildings and 0.64 for path surface grounding on our pilot evaluation set. The results demonstrate the conceptual capability of the proposed solution to deliver physico-geospatial grounded natural language descriptions. Code and results are available at this https URL

---


### 157. [Mind the Gap: Exposing LLM Translation Blind Spots Using the AlphaMWE Multilingual Parallel Corpus](https://arxiv.org/abs/2609.06634)

**<font color=#1a73e8>作者：</font>** Lifeng Han, Jiahui Liang, Anna Latusek 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs' performance on machine translation (MT) tasks is often dependent on the data availability in the specific domains and language pairs that they are trained upon. To examine if Multiword Expressions (MWEs) still set a bottleneck for LLMs regarding language understanding and translation, we report the system performances from the WMT2026 Test Suites shared task, for which we used the publicly available multilingual parallel corpus AlphaMWE as the test suites. We received 31 MT systems' outputs covering English to Chinese (zh), Polish (pl), German (de), Arabic (ar) including Modern Standard Arabic (MSA) and two dialectal ones (Egyptian and Tunisian Arabic). We carried out automatic evaluations using BLEU, ChrF, BERT-score to select the Top3 systems per language pair, followed up with human evaluations on the selected systems. Our findings show that: figurative/MWE phenomena remain challenging; automatic metrics sometimes disagree; human evaluation uncovers language-specific errors hidden by aggregate scores.

---


### 158. [SerenAI: State-transition system inspired by text-based world AI models](https://arxiv.org/abs/2609.06647)

**<font color=#1a73e8>作者：</font>** Elvin Babayev, Artem Sinitsa, Arash Hajisharifi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although professional workflows leverage large language models widely, the interpretation for auditing unconstrained free-text generation is usually intractable if such generation demands legal, operational or financial workflow. We hereby demonstrate a text based system called SerenAI - inspired by world-models, it is a state transition system that outputs verifiable predictions rather than merely text: Provided with a description of the environment, state, and actions, the generated output contains 4 items: causal deltas that causally effect the given state, a next state that can logically follow from the given state and action, a validity reward, and a termination signal. For the released proto-model, we employ 2 steps of adaptation training, namely parameter efficient fine-tuning followed by verifier based RL over 50,000 exampled cause and effects in 12 environments spanning 10 reasoning domains. Compared to an initial internal evaluation of an 8B open-weight baseline, SerenAI increased JSON validity from 85.0% to 93.2%, schema validity from 55.0% to 84.0%, exact structured-output match from 0.0% to 41.5%, causal-delta exact match from 0.0% to 41.5%, resulting-state exact match from 0.0% to 42.0%, reward exact match from 1.0% to 80.5%, and termination exact match from 38.0% to 81.5%. These support the narrower claim that verifier-compatible adaptation can improve structured transition prediction. They do not yet establish legal-grade reliability. Accordingly, the paper also specifies a validation protocol for evidence-grounded legal workflows, calibration, human oversight, and sovereign on-premise deployment.

---


### 159. [Inducing Emergent Misalignment from Reward Hacks with Iterative DPO](https://arxiv.org/abs/2609.06649)

**<font color=#1a73e8>作者：</font>** Oliver Daniels, Perusha Moodley, Benjamin M. Marlin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward hacking during reinforcement learning from verifiable rewards (RLVR) can induce reward seeking and broad misalignment in language models. Studying this misgeneralization is important for developing better threat models and countermeasures, but is often infeasible due to the cost of RL on large models. As an alternative, we propose studying emergent misalignment from iterative DPO, which preserves important properties of RLVR while reducing costs and enabling training on popular finetuning APIs. In practice, we find that training GPT-4.1 with iterative DPO on a single-turn reward hacking environment induces covert misaligned power-seeking and alignment faking, the first openly available (semi)-online training pipeline to induce these concerning forms of misalignment. We also find that training Qwen2.5-32B-Instruct with the same pipeline induces both misalignment and improved instruction following accuracy, showing that iterative DPO can be used as a testbed for selective generalization. Overall, we think iterative DPO can help democratize and accelerate the study of emergent misalignment from RLVR.

---


### 160. [ECOKV: Geometry-Aware KV Cache Eviction via Complementary Diversity Metrics](https://arxiv.org/abs/2609.06663)

**<font color=#1a73e8>作者：</font>** Chin Ting Hsu, Yu-Syuan Xu, Ling Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although multimodal Large Language Models (MLLMs) excel in diverse tasks, their scalability remains limited by the memory and computational overhead of KV cache storage. Recent KV cache eviction approaches incorporate a cosine similarity-based diversity metric with importance metrics to selectively retain critical key-value pairs. However, cosine similarity involves normalization that discards magnitude information, and it often yields uniformly high similarity values across layers due to the anisotropy property of hidden representations. In our study ECOKV, we rigorously deconstruct the capabilities of existing diversity metrics. Moving beyond simple measurement, we propose a geometry-aware composite metric that jointly leverages Euclidean distance and cosine similarity to capture token diversity from complementary perspectives. Furthermore, we use these two metrics to estimate the redundancy level of each attention head, allowing adaptive weighting between diversity and importance scores during token selection. Finally, we demonstrate that the observation window commonly employed to preserve recent tokens can be substantially reduced, thereby allocating more cache capacity to informative tokens and yielding consistent improvements. Extensive experiments demonstrate that ECOKV achieves state-of-the-art performance under various compression ratios and can be seamlessly integrated with existing KV cache eviction methods. We further analyze the relationship between importance and diversity, and examine redundancy patterns across layers and attention heads.

---


### 161. [Data Efficient Sample Selection for In-Context Learning](https://arxiv.org/abs/2609.06670)

**<font color=#1a73e8>作者：</font>** V Venktesh, Cem levi, Avishek Anand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The In-context learning (ICL) paradigm aids large language models (LLMs) to adapt to new tasks without need for fine-tuning. However, selecting an optimal combination of demonstration examples from a large pool of example subsets is a challenging problem. Existing approaches for selection do not model the complex relationship between ICL samples and downstream LLM performance. They typically perform static task-level selection, choosing subsets once offline, which can fail to generalize to unseen queries. We introduce DearICL (Data Efficient Algorithm for Ranking) ICL samples, a new framework that models demonstration example selection as a subset ranking problem. DearICL employs a non-linear surrogate employing a differentiable sorting objective within a gap-index bandit algorithm. The gap-index based approach enables fine-grained separation of good arms and borderline arms, which is used as an auxiliary objective to train the non-linear surrogate through sufficient sampling of borderline arms, supporting instance-level subset ranking. On exemplar selection benchmarks with open-source LLMs, DearICL achieves 8.08-15.9% accuracy gains over strong linear bandit baselines, with low sample complexity. Code and data: this https URL.

---


### 162. [Detokenization Leaks: Reconstructing Local LLM Outputs From Cache Traces](https://arxiv.org/abs/2609.06674)

**<font color=#1a73e8>作者：</font>** Roy Weiss, Benyamin Konstantinov, Eitam Sheetrit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a new attack that reconstructs the text generated by locally hosted LLMs by observing CPU cache activity during detokenization. Unlike prior attacks that rely on deployment-specific assumptions, such as shared data memory, CPU offloading, or Mixture-of-Experts architectures, our approach targets the detokenizer, a component used in default LLM inference pipelines. To obtain clean signals, we use Flush+Reload on shared tokenizer code to detect when decoding occurs, which lets us perform Prime+Probe at the right moment and isolate token-dependent cache activity. We then apply a clustering-and-language-model pipeline to recover text from noisy cache observations. We evaluate the attack across multiple datasets, hardware platforms, inference frameworks, and model families, and show that it can recover semantically accurate outputs from real-world local LLM deployments, including agentic systems.
This vulnerability is particularly significant because the most widely used tokenizer implementations are susceptible to the attack and are embedded in many popular local LLM products and agent frameworks, including systems such as OpenClaw (which we demonstrate), substantially broadening the practical attack surface.

---


### 163. [A Grapheme-Aware Indic Tokenizer for Tamil: Large-Scale Training and Intrinsic Evaluation](https://arxiv.org/abs/2609.06690)

**<font color=#1a73e8>作者：</font>** Hari Krishnan K V, Sudarsun Santhiappan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization forms the foundation of modern Natural Language Processing (NLP) systems by transforming raw text into discrete units that neural language models can process. The effectiveness of this process directly influences vocabulary efficiency, sequence length, computational cost, and downstream model performance. Although multilingual tokenizers such as Byte Pair Encoding (BPE), WordPiece, and SentencePiece have performed well across numerous languages, they often segment morphologically rich Indic languages inefficiently. Tamil, in particular, poses unique challenges because its grapheme-based writing system can represent a single visible character with multiple Unicode code points. In this work, we present a grapheme-aware Indic tokenizer for Tamil that preserves complete grapheme clusters through a reversible Unicode mapping strategy prior to WordPiece vocabulary learning. By operating on grapheme-level representations instead of individual Unicode code points, the tokenizer produces linguistically meaningful token boundaries while remaining fully compatible with transformer-based language models. The tokenizer is trained on a large-scale Tamil corpus and evaluated using a comprehensive intrinsic evaluation framework that measures compression efficiency, token fragmentation, information density, and vocabulary utilization. Experimental evaluation compares the proposed tokenizer against five widely used multilingual tokenizers: GPT-2, mBERT, mT5, mBART, and NLLB. The proposed tokenizer achieves the strongest performance among the evaluated tokenizers on fragmentation- and sequence-efficiency-oriented intrinsic metrics, while matching the highest observed compression ratio. These results demonstrate the effectiveness of grapheme-aware preprocessing for Tamil tokenization.

---


### 164. [PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents](https://arxiv.org/abs/2609.06702)

**<font color=#1a73e8>作者：</font>** Kun Li, Zexuan Qiu, Tianhua Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sequential memory agents process long documents by reading chunks one after another while maintaining a compact memory state, coupling document traversal to reasoning depth. This coupling introduces sensitivity to evidence placement and ties inference latency linearly to document length. We introduce PARSER, which decouples reading from reasoning. A bank of lightweight subagents each bound to a single chunk read the entire document in parallel, while a lead agent reasons in depth through iterative scatter--gather rounds: at each round it broadcasts a query to all subagents, aggregates the returned evidence, and formulates a deeper follow-up query conditioned on what has been found so far. This decoupled design concentrates all learnable behavior in the lead agent, which is optimized with reinforcement learning, while the subagents remain frozen off-the-shelf models. On multi-hop QA with contexts ranging from 7K to 896K tokens, PARSER with a 4B backbone outperforms the strongest sequential memory baseline by 5.7 points on average and by 12.0 points at 896K tokens. Scaling to a 9B backbone, PARSER surpasses DeepSeek-V4-Pro by 6.3 points. Controlled experiments confirm that PARSER is robust to perturbations in evidence position, order, and distance, conditions that cause large accuracy swings in sequential methods, while reducing inference latency by up to 11x.

---


### 165. [Counterfactual Tests for Measuring Chain-of-Thought Faithfulness in Visual Language Models](https://arxiv.org/abs/2609.06704)

**<font color=#1a73e8>作者：</font>** Bayar Menzat, Maximilian Süss, Ruizhi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) may often look plausible, yet it may not faithfully reflect the model's decision-making process. While methods for measuring the faithfulness of CoTs for textual inputs have been increasingly introduced, using these methods for visual inputs is not straightforward. In this work, we adapt the family of counterfactual methods for measuring CoT faithfulness, namely the Counterfactual Test (CT) and Correlational Counterfactual Test (CCT), to visual inputs, and call them vCT and vCCT, respectively. Using vCT and vCCT, we benchmark eight recent open-source Vision Language Models (VLMs) on two datasets. Our analysis shows that CoTs do not reliably track visual evidence that influences model predictions: they may omit the removed object even when its removal causes a large prediction shift, yet mention it when the shift is small. We further find that Predict-then-Explain explanations align more strongly with perturbation-induced probability shifts than pre-answer CoTs, while binary vCT scores are often nearly saturated. We also include a reconstruction control, in which images pass through the same editing pipeline without object removal, and find that the main object-removal intervention induces larger shifts than reconstruction alone. We construct and release Counter-SNLI-VE and Counter-A-OKVQA, two datasets of image pairs that differ by a single object.

---


### 166. [Monte Carlo-Based Ex-Ante Assessment of the Green Benefits of an AI-Driven Smart Agriculture Platform in Hainan](https://arxiv.org/abs/2609.06737)

**<font color=#1a73e8>作者：</font>** Zhaoyang Li, Ruijie Zhang, Zhaoji Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smart agriculture platforms are widely regarded as key carriers for implementing China's pesticide and fertilizer reduction, water-saving and carbon-reduction agendas, yet a unified quantitative framework for assessing their green value is still lacking. Taking an AI-driven decision platform for tropical agriculture as the object (integrating large-language-model question answering, multimodal pest diagnosis, IoT sensing, satellite remote sensing, and a closed-loop field record system), this study builds a cradle-to-farm-gate agricultural carbon accounting model covering pesticide and fertilizer production, field N2O, irrigation electricity and paddy CH4, translates platform interventions into quantifiable transmission parameters, and propagates parameter uncertainty by Monte Carlo simulation over three Hainan scenarios (mango, winter vegetable, rice/nanfan, area-weighted 40%:30%:30%). Under full adoption, median reductions are 23.5% (90% interval 15.0%-33.2%) for pesticide use, 21.0% (13.8%-28.9%) for fertilizer, 16.5% (10.9%-23.5%) for irrigation water, and 21.5% (16.1%-27.2%) for carbon intensity. Attainment probabilities are high for fertilizer reduction >=15% (90.6%) and clear carbon decline (98.1%), but only about 20% for aggregate water saving >=20%, favoring scenario-specific statements. Sobol first-order indices show soil-test recommendation and organic substitution jointly explain about 83% of the variance of aggregate carbon-intensity reduction. Convergence tests show 10,000 iterations stabilize all statistics; conservative/baseline/optimistic scenario bounds are reported. The framework offers a reproducible, calibration-ready methodology for ex-ante green-value assessment and pilot observation design.

---


### 167. [Reason Through the Latent! Making Latent Visual Reasoning Necessary](https://arxiv.org/abs/2609.06746)

**<font color=#1a73e8>作者：</font>** Suhyeong Park, Junha Jung, Jaewoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent visual reasoning aims to perform multimodal reasoning through hidden-state computation rather than explicit textual chains of thought. However, visual information being present in a latent state does not imply that the model actually relies on that state when producing its answer, especially when alternative image-conditioned paths remain available. We introduce \textbf{C}ausal \textbf{V}isual \textbf{R}ecurrent \textbf{R}easoning (CVRR), which preserves pretrained visual competence while making recurrent computation the required image-conditioned path to prediction. CVRR initializes recurrence from the question hidden state after the pretrained vision-language model has incorporated the image, then repeatedly updates this state while re-reading the same fixed visual evidence. Before decoding, visual states and the original multimodal KV cache are removed so that only the final recurrent state carries image-conditioned information to the answer. Across the $V^*$, MMVP, BLINK, and MME-RealWorld-Lite benchmarks, CVRR retains strong performance under this strict interface, while compatible latent reasoners fail to recover comparable visual competence even when retrained under the same constraint. Causal interventions further show that predictions remain sensitive to recurrent content when the question is held fixed, and that persistent visual evidence causally revises the recurrent trajectory. These results distinguish latent informativeness from latent computation that is actually used for prediction.

---


### 168. [A Novel Semantic Manifold Alignment Attack against Embedding-to-Embedding Obfuscation in Privacy-Preserving LLMs](https://arxiv.org/abs/2609.06749)

**<font color=#1a73e8>作者：</font>** Sicong Li, Lingfeng Yao, Xingke Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the widespread applications of large language models (LLMs), privacy-preserving inference has become increasingly essential for sensitive queries. To balance privacy and utility, a series of lightweight obfuscation approaches has recently been proposed, where users locally transform plaintext embeddings into the fixed ciphertext ones. While such Embedding-to-Embedding Obfuscation (E2EO) schemes demonstrate considerable resilience against traditional token frequency and embedding inversion attacks, the core mechanism behind remains to be the large-scale one-to-one substitution, which provides no cryptographic guarantees. In this paper, we propose Proxy Manifold Alignment (PMA), a novel attack against E2EO in privacy-preserving LLMs. Our key observation is that E2EO schemes keep the original semantic structure, so that the obfuscated vector stream can be regarded as an unknown tokenizer-language whose symbols are the vectors themselves. Therefore, the proposed ciphertext to plaintext reconstruction attack can be formulated as a translation task from the unknown tokenizer-language to plaintext. Specifically, by only accessing the obfuscated vector stream, the target tokenizer and a public corpus, the PMA attack first employs Word2Vec to model the co-occurrence patterns within the obfuscated stream and the public corpus independently, and constructs two proxy vector embeddings. Then, the attack aligns the underlying manifolds of these two embeddings based on structural similarity. Finally, it maps the obfuscated vectors back to plaintext. Experimental results demonstrate that PMA consistently achieves higher plaintext recovery than other state-of-the-art attack methods.

---


### 169. [Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758)

**<font color=#1a73e8>作者：</font>** Yinming Huang, Shuyuan Tu, Xi Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generation is evolving from generative models used through a single invocation into agentic control processes that can plan, select tools, inspect intermediate synthesized outputs, revise failures, and reuse prior experience. In most existing systems, the controller is an LLM or VLM, while visual generation models serve as tools or executors. However, existing work lacks a consistent criterion for determining when a generation system becomes agentic. Planning depth, tool use, multi-role collaboration, and reinforcement learning are often treated as evidence of agenticity, even though none of them necessarily determines which generation decisions the controller can make. We organize the field according to what the controller can directly control in the generation process. At L1 Conditioning Control, the controller prepares the input to a predetermined generator but does not control which visual operation is executed. At L2 Execution Control, it selects and invokes actual generation, editing, rendering, or other content-modifying operations. At L3 Outcome-Adaptive Control, it observes an intermediate outcome and uses that observation to change a subsequent operation within the current task. At L4 Experience-Adaptive Control, it retains experience from completed tasks and uses that experience to change decisions on future tasks. L0 Fixed Support separately denotes generators, editors, evaluators, reward models, benchmarks, and fixed pipelines without a deployed controller that makes generation-level decisions. These levels describe a progressively broader decision-making scope rather than model size, system complexity, output quality, tool or role count, or training method. Applying this framework across image, video, editing, 3D, world, slide, and user-interface generation reveals how controller capabilities have evolved and how their mechanisms are distributed across levels.

---


### 170. [DrugReason: Dynamic Multi-View Reasoning over Knowledge Graph and Language Evidence for Drug Repurposing](https://arxiv.org/abs/2609.06779)

**<font color=#1a73e8>作者：</font>** Zijie Liu, Hongxuan Li, Zhen Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug repurposing aims to identify new therapeutic uses for existing compounds and, compared with de novo drug discovery, offers a faster and more cost-effective path to clinical translation. However, the space of candidate drug-disease pairs is enormous and their underlying relationships often depend on complex multi-hop biological mechanisms, making it difficult to reliably predict which pairs represent true therapeutic relationships. Existing approaches tackle this from two directions: knowledge graph-based methods organize curated biomedical evidence into structured relational networks for grounded multi-hop reasoning, while LLM-based methods leverage pretrained knowledge to generate flexible mechanistic rationales. Yet neither is sufficient alone - KGs are confined to observed graph structure while LLMs lack factual grounding and risk hallucination. To address this gap, we propose DrugReason, a multi-view reasoning framework that integrates grounded KG reasoning with LLM-generated mechanistic inference for drug repurposing. DrugReason adaptively routes diverse reasoning paths to specialized experts conditioned on the query context, while a cross-expert distillation objective enables knowledge sharing without sacrificing expert specialization. Experiments on PharmaDB, DDInter, and DrugBank show that DrugReason improves average performance over strong single-view reasoning baselines and achieves competitive or superior results compared with graph-based alternatives, while providing interpretable routing-based predictions.

---


### 171. [AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://arxiv.org/abs/2609.06783)

**<font color=#1a73e8>作者：</font>** Ruoxi Shang, Christina-Maria Androna, Orfeas Menis Mastromichalakis 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents operate in workflows where unsafe actions can have real consequences. Existing safety evaluations often reduce behavior to a single score, obscuring risk recognition, pre-action detection, and safe task completion when a safe solution exists. We introduce AURA-Eval, a framework combining controlled augmentation with granular diagnosis of behavior in tool-use trajectories. Its pipeline identifies safety-critical decision points, generates controlled variations, and constructs counterparts differing in whether a request has a safe fulfillment path. Using 157 sourced trajectories, we generate 1,249 evaluation items and evaluate 20 frontier and open-weight models. We developed rubrics to classify risk detection, action strategy, and scenario-specific action safety. Our results show that LLM agents engage in unsafe behavior more often when no safe fulfillment path exists. In these cases, frontier proprietary models more often recognize risk and exhibit safer behavior by proposing alternatives, while evaluated open-weight models more often directly execute unsafe requests. Increasing impact or reducing opportunities for oversight before execution also exposes greater vulnerability across models.

---


### 172. [When Retain Constraints Conflict: Mitigating Forget-Retain Interference in Tabular Data](https://arxiv.org/abs/2609.06786)

**<font color=#1a73e8>作者：</font>** Zijie Liu, Jinhao Duan, Bingqi Shang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of designated training data while preserving model utility, but its behavior on tabular data remains underexplored. This gap is important because tabular prediction is widely used in high-stakes domains and is increasingly adapted to language models through record serialization and schema-aware prompting. We identify a key challenge that distinguishes tabular unlearning from unlearning in free-form text or other modalities: schema-induced forget-retain overlap. In serialized tabular data, records share fixed column-name/value slots, similar attribute ranges, and common output spaces. Consequently, a forget row may have nearby retain rows that rely on the same high-signal attributes, causing retain preservation to oppose the update required for forgetting. Motivated by this failure mode, we propose Conflict-Aware Unlearning (CAU), a schema-aware approach that reduces forget-retain interference by relaxing preservation constraints on retained rows that most conflict with the forget set. Across sample-level and feature-level unlearning on clinical and non-medical tabular tasks, CAU more closely matches a retraining oracle while maintaining predictive utility and retain-region behavior. Our results show that reliable tabular LLM unlearning depends not only on the forgetting objective, but also on how retain constraints are constructed.

---


### 173. [Typed Federated Artifacts for the Agentic Web:Sharing Tool-Routing Knowledge Across Frozen,Heterogeneous LLM Agents](https://arxiv.org/abs/2609.06815)

**<font color=#1a73e8>作者：</font>** Abhijit Chakraborty, Ni Trieu, Vivek Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An open, networked web will allow agents to run frozen models from multiple vendors, keep their history private, and teach each other which tool to call and when. Flat text (prompts, example pools) makes it difficult for the protocol to distinguish between noise statistics, merging rules, and documentation. Weights and adapters cannot transfer that knowledge between platforms. We suggest sharing typed federated artifacts, schema-validated objects with well-defined fields for per-field privacy (described here, but measured), dispute resolution, and cross-model transfer, and instantiating them as SYNAPSE1, a common tool-routing knowledge. After deleting 192 garbage entries and 1,916 training items that duplicate or almost duplicate test queries, a federated compendium routes within 1.1 points of a centralized one at 20 MB of JSON per client each round on StableToolBench (3,180 tools). The same experience merged and shown to the router as typed fields rather than one flat string is worth 8.5 points on clean data and 7.4 under 60% injected contradiction. Crossing merge and rendering shows the halves are inseparable (the typed merge shown flat is the worst arm), while three conflict policies are indistinguishable, so the conflict log that motivated this work is not the On {\tau}-bench retail, each compendium arm improves GPT-4o agents' per-step tool-call accuracy by at least 6.7 points, attributed to format rather than federated experience. Two cautionary findings conclude the paper: on a topic-labeled math proxy and StableToolBench, a TF-IDF classifier over the same labeled experience beats every LLM routing arm (by 48 and 26 points, mostly retrieval recall) because the benchmark's pool holds labeled queries for every supposedly unseen tool and every test query verbatim before our filter. It cannot measure routing to tools without labels, which routing exists for.

---


### 174. [Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823)

**<font color=#1a73e8>作者：</font>** Cristian Sminchisescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The next generation of artificial intelligence systems will likely be natively temporal and multimodal in both inputs and outputs: able to converse, perceive, predict, reason, and synthesize through a shared world representation. Realizing this requires a temporal perceptual substrate integrating sensory streams, language, and structured outputs within a multimodal world model. We seek a generalist open-world perceptual system that represents biological forms, natural physical structures, and artifacts, and their interactions, as a coherent, temporally persistent process. The model should infer geometry, articulation, semantics, interaction structure, and uncertainty from raw multimodal streams; maintain identity through occlusion and viewpoint change; generalize across species, forms, mechanisms, and materials; and abstain or expand its ontology when encountering the unknown. The objective is a structured world state supporting understanding, prediction, counterfactual reasoning, and controllable synthesis. Recent work suggests that some cross-modal and reasoning-like capabilities can emerge from large-scale generative video pretraining, reminiscent of language-model scaling. Yet these capabilities are often accessed through language probes or expressed through photorealistic video, leaving explicit semantic, geometric, or temporal structure largely unexposed. This paper articulates an alternative and complementary paradigm: perception and synthesis as distinct conditionings within a shared Generalist Open-World Temporal Perception Architecture (GOWTPA). Recognition, structured prediction, and simulation arise as different conditionings of the same generative substrate, while reasoning and embodiment-specific policies build upon the resulting world state. This positions generalist temporal perception as a potential foundation layer for broader multimodal intelligence and physical AI.

---


### 175. [NormViz: A Benchmark and Framework for Grounding Multimodal Reasoning in Global Cultures](https://arxiv.org/abs/2609.06831)

**<font color=#1a73e8>作者：</font>** Akhila Yerukola, Fabrice Y Harel-Canada, Simran Khanuja 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are used worldwide, but they struggle to serve the needs of culturally diverse populations. Prior work on cultural understanding evaluates AI systems on text-only settings or on visual artifact recognition (e.g. foods, clothing). The ability to reason about visually observable behaviors through local social norms, which we call visual norm understanding, remains unexamined. We introduce NormViz-Bench, a high quality, human-validated benchmark of 3,268 contrastive image pairs (6,536 images) spanning 16 countries. Each pair varies only in the culturally relevant behavior (e.g., objects, attributes, spatial relations, and actions) that alters how each image is interpreted. Each image is labeled as conforming to, violating, or irrelevant to local social norms, and pair-level evaluation requires both images to be correctly classified, thereby preventing reliance on superficial visual shortcuts. Even the strongest VLMs, Gemini 3.0 Flash and Qwen2.5 VL 7B, succeed on only 26.6% and 21.6% of pairs, struggling most with identifying violating and culturally benign visual behaviors. Towards bridging this, we introduce NormViz-Train, a training dataset of 64k images paired with explanations. Though absolute performance remains low (<30%), finetuning on NormViz-Train improves pair accuracy relatively by up to 125% and 36% Qwen3-VL 4B and 8B respectively, showing a path forward to teach models to connect visual perception to cultural significance. Together, NormViz-Bench and NormViz-Train establish visual norm understanding as a challenging and consequential frontier for multimodal AI.

---


### 176. [WAPP: Safe Learning of Positive Security WAF Policies from Live Traffic](https://arxiv.org/abs/2609.06840)

**<font color=#1a73e8>作者：</font>** Heba Osama, Zeyad Ahmed, Mohamed Amgad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web Application Firewalls (WAFs) mainly rely on signatures to detect known attacks, which can leave gaps against modified or previously unseen payloads. Positive security provides a complementary approach by learning legitimate traffic and blocking inputs that fall outside the learned profile. However, learning directly from live traffic can be unsafe when malicious requests contaminate the training data. This paper presents the Whitelisting Autonomous Policy Producer (WAPP), a framework that combines trust filtering, deterministic rule synthesis, confidence scoring, and validation before enforcement. WAPP is evaluated on three controlled applications using a live Coraza and OWASP Core Rule Set (CRS) stack. Results show that, on the tested DVWA username field, unfiltered learning becomes Degraded at 0.2\% poisoned traffic and Broken at 0.5%, while the evaluated free text field can admit malicious inputs even without poisoning. On the frozen poisoning dataset, the ablation configuration with all seven candidate signals improves the measured poisoning resilience from 53% to 90%, compared with 62% for the Kruegel--Vigna baseline. The deterministic synthesizer provides attack blocking comparable to the tested language model without model inference cost. WAPP blocks confirmed CRS bypasses on constrained fields, while free text inputs remain a precision challenge that requires character level operator control.

---


### 177. [XYBench: Can LLMs Respond Pragmatically to Queries with Misconceptions?](https://arxiv.org/abs/2609.06842)

**<font color=#1a73e8>作者：</font>** Akhila Yerukola, Jena D. Hwang, Mingqian Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When non-expert users ask LLMs for assistance, their queries can often have misconceptions (e.g., "How do I parse XML with regex?"). In such cases, often referred to as the XY-problem, LLMs must identify the misconception ("regex are fragile") and meaningfully direct the user toward a pragmatic solution that will address the root problem implicit in the request ("use an XML parser"). We introduce XYBench, a benchmark of 8,115 such queries, drawn from technical (StackOverflow/StackExchange) and everyday (WikiHow and a manually-curated subset) domains. We design an evaluation paradigm that assesses model responses along three criteria grounded in cooperative response theory: (a) presence and (b) emphasis on pragmatic solutions, and (c) identification of misconceptions. Our experiments show that even the strongest LLMs predominantly answer the literal request (0.75--0.92) and far less often the intended one (0.33--0.71), while substantially lagging behind humans at identifying misconceptions (at most 63% vs. 79--90%). Further, models overwhelmingly prefer pragmatic responses in a multiple choice setting yet consistently fail to generate them. Oracle ablation experiments show that providing explicit user intent at generation time helps; however a large gap remains, suggesting pragmatic redirection is a fundamentally underdeveloped capability in current LLMs.

---


### 178. [Characterizing Contention-Induced Reliability Collapse in KV-Cache Timing Side Channels for Multi-Tenant LLM Serving](https://arxiv.org/abs/2609.06853)

**<font color=#1a73e8>作者：</font>** Rana Abu Bakar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Shared key--value (KV) cache reuse improves large language model (LLM) serving, but it can also create a timing side channel that reveals whether a prefix is already cached. Previous work shows that such attacks are possible, but their reliability under realistic multi-tenant contention is less understood. We study this problem through seven experiments on live shared LLM-serving systems. On a vLLM server running DeepSeek-R1-Distill-Llama-8B on NVIDIA GB10, mean Cohen's d drops from 0.7789 with no synthetic workers to 0.2109 with two workers (t=8.412), while higher worker counts cause no statistically detectable further loss. A 120-run sparse-overlap experiment places the best breakpoint at the boundary of the measured range (tau=0, 95% CI [0.000,0.113]), supporting an ambient-versus-loaded regime change rather than an internal physical threshold. AUROC falls from 0.650 at ambient to 0.531 near 61% overlap and partially recovers to 0.574 at saturation. Concurrency-depth variance is the strongest measured correlate of effect size (r=-0.416) and hit consistency (r=-0.637). An interleaved control preserves the same non-monotonic ordering. The main collapse is also reproduced on a real two-node, two-GPU tensor-parallel vLLM setup, where mean d falls from 3.418 to 0.511 (p<0.01). Two SGLang pilots are statistically inconclusive. Overall, KV-cache timing reliability depends strongly on the load regime and serving stack, and measurements on quiet systems can overestimate operational attack reliability.

---


### 179. [A Queryable Graph-Based Security Analysis Framework for O-RAN](https://arxiv.org/abs/2609.06855)

**<font color=#1a73e8>作者：</font>** Corban Villa, Michele Guerra, Syed Khandker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Open Radio Access Network (O-RAN) replaces vendor-locked RANs with a modular and interoperable architecture that fosters competition and accelerates innovation. With this openness comes increased complexity and a larger attack surface, making security a critical concern. Today, assessing O-RAN security requires manually cross-referencing dozens of specifications, vendor whitepapers, and academic studies, which is error-prone and static. In this paper, we present a graph-based framework that transforms this static corpus into a single, queryable database. Our graph representation contains over 350 nodes and more than 1,250 relationships, distilled from specifications, academic papers, open-source projects, and vulnerability databases. To keep this resource current, we integrate a hybrid data extraction pipeline that couples deterministic parsing of structured specifications with Large Language Model (LLM)-assisted extraction for evolving specifications and unstructured literature. Querying the graph reveals three actionable findings within our curated corpus: critical infrastructure such as the O-DU, SMO, and O-Cloud carries dozens of specification-level threats yet has little or no empirical coverage; memory-safety weaknesses account for 11 of the 21 CWE occurrences associated with the analyzed CVEs; and fuzzing uncovered 18 of the 20 CVEs attributed to research papers. We provide the database, pipeline, and queries as open-source artifacts.

---


### 180. [AutoLexSteer: Automatic Contrast Construction for Lexical Activation Steering](https://arxiv.org/abs/2609.06879)

**<font color=#1a73e8>作者：</font>** Shuhe Wang, Lachlan Cowley, Eduard Hovy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering vectors have rapidly emerged as a popular and effective method for guiding the output of LLMs in very specific ways. But constructing accurate steering vectors is a difficult manual process due to the opacity of embeddings. We introduce Hangman, a novel type of steering vector that operates using word senses, as well as AutoLexSteer, the first fully automated process for building steering vectors. AutoLexSteer employs families of closely-related words extracted from WordNet to specify both the steering source to be avoided and the desired steering target. The steering vectors are quite precise, can be used to steer at the level of words and sets of word senses (meanings), and are able to steer certain LLM behaviors like sycophancy. The dataset and code can be found at this https URL.

---


### 181. [Contextual Observer Grounding: Evaluating Situated Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2609.06880)

**<font color=#1a73e8>作者：</font>** Mimo Shirasaka, Haochen Zhang, Yonatan Bisk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning over language instructions in embodied tasks such as robotics often requires understanding spatial relations from a speaker's situated perspective. Humans infer such perspectives from shared environmental knowledge, activity context, and commonsense. Recent vision-language models (VLMs) appear capable of spatial reasoning, but their ability to infer a speaker's viewpoint from contextual cues and interpret situated spatial relations from that viewpoint remains unclear. We call this capability contextual observer grounding. To study this capability, we construct the Point-of-View Benchmark (POVBench), a dataset of 3D scenes and queries that disentangles Inferred, Stated, and Given forms of observer grounding in natural embodied communication. Given multi-view observations and a natural-language sentence, models must localize unseen or underspecified targets from situated spatial and contextual cues. Across state-of-the-art VLMs, localizing targets from directional language remains challenging, even when observer grounding is made explicit. We find that explicit breakdowns of observer-relative spatial reasoning improve target localization. Our project page is available at this https URL.

---


### 182. [Towards Bridging the Gap Between Offline and Iterative Alignment via Preference Distillation](https://arxiv.org/abs/2609.06893)

**<font color=#1a73e8>作者：</font>** Wenbo Zhang, Wenzhuo Zhou, Hengrui Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct preference optimization DPO is a promising offline approach for aligning large language models (LLMs) due to its simplicity, computational efficiency, and implicit modeling of human preferences. Interestingly, iterative extensions of DPO have achieved stronger performance on academic benchmarks, raising two key questions: (i) Why do iterative methods generally outperform offline ones? (ii) Can their advantages be incorporated into offline alignment? To answer the first question, our controlled experiments reveal that the explicit preference model, additionally introduced in the iterative procedure, is a key factor behind its superiority over offline methods. This insight leads us to answer the second question affirmatively and propose Distilled Preference Probability Policy Optimization (DP3O), an effective and efficient offline alignment algorithm. DP3O first learns an explicit preference model using a helper class of LLMs and then distills its knowledge into policy optimization. Theoretically, we show that explicit preference modeling admits better estimation error control than implicit formulations, and that DP3O achieves a tighter generalization bound than hard-label DPO through variance reduction. Empirically, we evaluate DP3O on a wide range of chat-based and downstream tasks and show that it outperforms state-of-the-art offline methods, achieves performance comparable to iterative DPO, and reduces training time by about $42\%$, demonstrating both its effectiveness and efficiency.

---


### 183. [A visual large language foundational model for medical image recognition using clinician-oriented social media](https://arxiv.org/abs/2609.06914)

**<font color=#1a73e8>作者：</font>** Lingxuan Hou, Yuhua Xie, Yue Hu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities across diverse domains, showing considerable potential in medicine. However, their application in medical settings remains limited by the scarcity of visual question answering (VQA) datasets that capture clinical reasoning and explicit image-text alignment. Here, we leverage de-identified medical images and expert commentaries shared on clinician-oriented social media. By combining an advanced LLM with clinician-in-the-loop verification, we established a rigorous pipeline to construct ThoughtMed-1M, a long-form medical VQA dataset containing over one million VQA pairs and designed to capture structured clinical logic and medical image-text alignment. To demonstrate its utility, we developed a FOundational LLM Trained on ThoughtMed-1M (FOLTMed). FOLTMed achieved state-of-the-art performance across 42 medical VQA benchmark datasets, with a macro accuracy of 85.4%, and generated more clinically coherent responses on the ThoughtMed-1M test set. It outperformed state-of-the-art models by 3--5% across factuality and similarity metrics, highlighting a scalable paradigm for advancing research on clinically grounded multimodal LLMs.

---


### 184. [BEFORE THE FLIP: Measuring Hidden Score Shifts In Quantized Vision Language Models Before The Answer Changes for Visual Question Answering](https://arxiv.org/abs/2609.06922)

**<font color=#1a73e8>作者：</font>** Sourajit Saha, Shubhashis Roy Dipta, Shaswati Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantization makes vision language models (VLMs) cheaper to store and run by using fewer bits to represent their weights. While unchanged answers on visual question answering (VQA) after compression are an expected behavior, they can still hide changes in the underlying scores (log probabilities). For example, a model may still answer yes after compression, even as the score gap between yes and no shrinks. We introduce BEFORE THE FLIP to measure these hidden changes. Our method compares the score change caused by compression with the change caused by replacing the image's internal representations, or image tokens, with one fixed average token. We then increase the precision of one weight group at a time to identify where extra bits help, and test whether choosing different groups for each question offers benefits beyond shuffled controls. Among 8,277 LLaVA questions where image token replacement measurably affects the scores, 4-bit compression shifts the yes or no score gap farther toward the replacement output than 8-bit compression. Qwen shows the same pattern, but with a smaller difference. Yet only 265 of 9,000 LLaVA answers change at 4 bits. In a separate study of 1,024 calibration questions, choosing weight groups separately for each question does not outperform both shuffled controls at any tested storage budget. These findings show that compression can alter the scores behind unchanged answers, but do not establish a reliable benefit from adjusting precision for each question.

---


### 185. [CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary Angiography Interpretation](https://arxiv.org/abs/2609.06931)

**<font color=#1a73e8>作者：</font>** Jia-Jen Lee, Shih-Yen Hou, Kee Koon Ng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invasive coronary angiography (CAG) is the gold standard for diagnosing coronary artery disease, but interpretation varies substantially among observers. Existing AI systems can improve consistency but lack auditable decision processes and are limited in comprehensive open-ended assessment, undermining clinician trust and clinical adoption readiness. We developed CARDEA, a unified large vision-language model that serves as the inference core of a CAG pipeline. It was trained solely on public datasets and closed-ended tasks in three stages: visual feature alignment, a self-distilled Chain-of-Box (CoB) cold start, and reinforcement learning with verifiable rewards (RLVR) with a CoB reward encouraging bounding-box use in the reasoning trace. We assessed its two study-level diagnoses, dominance classification and complexity assessment, against a dedicated classifier and two interventional cardiologists. Report generation was excluded from training and evaluated zero-shot across stages on an external cohort using vessel-severity macro-$F_1$. CARDEA trailed the classifier on in-distribution dominance but drew level under domain shift (accuracy, 0.91 [95% confidence interval (CI), 0.86 to 0.95]) and was comparable to the cardiologists on complexity assessment (accuracy, 0.90 [CI, 0.82 to 0.97]). Only RLVR improved zero-shot report generation, raising its vessel-severity macro-$F_1$ (0.686 [CI, 0.664 to 0.707]) above the untuned base model (0.513) and over twice the always-normal floor (0.312). CARDEA runs an end-to-end CAG pipeline from raw multi-view videos through keyframe selection to study-level diagnosis while exposing auditable spatial evidence behind its conclusions. RLVR on verifiable closed-ended tasks surfaced open-ended reporting ability that supervised imitation did not. Clinical use requires prospective validation against expert cardiologists.

---


### 186. [The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists](https://arxiv.org/abs/2609.06934)

**<font color=#1a73e8>作者：</font>** Srikanth Malla, Chiho Choi, Joon Hee Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc safety training (RLHF, DPO) is the dominant way to align large language models, yet jailbreaks (Zou et al., 2023b), fine-tuning attacks (Qi et al., 2024), and activation-space probes (Arditi et al., 2024) keep recovering the behaviors it was meant to remove. We give this fragility one geometric explanation and trace it to when, during pretraining, safety can take hold. We measure the safety update $\Delta = W_{\text{safe}} - W_{\text{base}}$ against the curvature of the model's capabilities (the empirical Fisher of a capability loss). Post-hoc safety consistently lands in a suppression regime: $\Delta$ is nearly orthogonal to the capability directions, and its small in-subspace part concentrates on a few high-curvature ones. The update is thin but sharp, a refusal gate laid over intact capabilities rather than erasure of them. A kernel-immobility lemma explains why such an update can only mask a capability, not remove it, so a little benign fine-tuning restores it: 100 steps of benign fine-tuning collapse refusal on Qwen-2.5-7B and Llama-3-8B Instruct at preserved capability, a signature that replicates across five model families.
Following the account into pretraining, a 267-checkpoint sweep of OLMo-2-1B (OLMo et al., 2025) shows the substrate that safety engages emerging in a sharp transition between roughly 6B and 60B pretraining tokens. We then use the account constructively: models trained from scratch with safety co-training spread continuously across pretraining reach 87 to 98% refusal whose post-attack level holds at 84 to 91% at every scale, an erosion of 2 to 14 pp against 35 to 38 pp for post-hoc installs, at capability matched or better than an LM-only baseline and holding from 410M to 6.9B, whereas a compute-matched windowed schedule installs no lasting refusal. Persistence of the safety signal across pretraining, not its timing, is what buys attack robustness.

---


### 187. [When and Why LLM Causal Priors Help: Closed-Loop Prior Selection for Amortized Causal Inference](https://arxiv.org/abs/2609.06941)

**<font color=#1a73e8>作者：</font>** Haohao Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal effect estimation asks how an outcome would change under an intervention, and medicine, economics, and public policy all treat it as a foundational task. Prior-data fitted networks (PFNs) amortize the task: a model trained on large numbers of programmatically generated synthetic causal tasks reads a new problem's observational data into context and returns an interventional-effect estimate in a single forward pass. The capability of such models is largely determined by the synthetic training prior, which is currently designed by hand, a bottleneck acknowledged by both Do-PFN and CausalPFN. Large language models (LLMs) can now ``draw'' plausible causal graphs for a given domain, suggesting that LLM-distilled graphs could serve as prior material. Whether injecting such graphs helps at all, where any gain comes from, and when injection helps. Practice has so far relied on manual trial and error. We propose a \emph{closed-loop prior selection framework} that casts prior injection as a budget-constrained optimization over a candidate prior pool. Candidates undergo cheap post-training and are scored by a composite metric dominated by real-domain generalization; the winner then receives full training and paired statistical validation. On a 7.34M-parameter Do-PFN, the framework's winner attains a formally significant $2.75\times$ gain on the primary evaluation domain, and its error falls below that of the uninjected official base. Generalization on an adjacent monitoring domain improves significantly, and no monitored capability degrades. Mechanism experiments show that the gain depends on the semantic content of the distilled graph rather than its structural diversity alone does not produce it (directional evidence). With this framework and this regularity in hand, the use of LLM causal priors stops being manual trial and error and becomes an empirically verifiable selection problem.

---


### 188. [Steering Interference Reflects the Model's Defaults, Not the Behavior Directions](https://arxiv.org/abs/2609.06951)

**<font color=#1a73e8>作者：</font>** Srikanth Malla, Chiho Choi, Joon Hee Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering promises modular control of language model behavior: a behavior such as politeness corresponds to a direction in a model's activations, and adding that direction while it generates should switch the behavior on and leave everything else alone. It does not. We ask what decides which other behaviors move, and by how much, and find that it is the model rather than the behavior being steered. A steer relaxes the model toward a small set of behaviors it already favors, chiefly refusal, sycophancy, and poeticism, and that set is much the same whatever is steered.
Three results across 24 behaviors and ten instruction-tuned models support this, every effect read off the generated text by a language-model judge rather than off a probe. That readout matters: all 24 behaviors are linearly decodable, but only 20 change what the model writes. First, a direction carrying no behavioral content, matched to a real steer only in the size of the vector it adds, moves the same behaviors in the same order as real steers do, while producing none of the behaviors that need a specific direction. Second, most interference runs one way, so it cannot be an overlap between two directions: steering profanity makes the model toxic, while steering toxicity leaves profanity untouched. Third, with a behavior held out entirely, geometry measured on the others explains almost none of the interference it takes part in. The account holds on all ten models, the pull toward defaults strongest below 10B parameters and weakening in each family's largest. Reading a steer as a perturbation whose endpoint the model fixes implies that disentangling behavior directions cannot by itself make steering modular.

---


### 189. [TurEngMix: A Text Corpus and Benchmark for Turkish-English Code-Mixed Language Identification and Named Entity Recognition](https://arxiv.org/abs/2609.06963)

**<font color=#1a73e8>作者：</font>** Ilayda Dogan, Phuong-Anh Nguyen-Le, Julia Mendelsohn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language processing systems underperform on code-mixed text, particularly for low-resource language pairs. Turkish-English poses a further challenge: it lets English stems combine with Turkish suffixes to form single mixed-language tokens. We introduce TurEngMix, a corpus of 5.5K noisy, naturally occurring social media posts (486,974 tokens) rich in Turkish-English code-mixing. From this corpus, we construct a new Turkish-English benchmark for code-mixed language identification (LID) and named entity recognition (NER), comprising 15K expert-annotated tokens. Evaluating both decoder LLM and fine-tuned encoder baselines, we find that monolingual Turkish and English tokens are labeled reliably, but all models have high error rates on mixed-language tokens for both LID and NER. For morphologically integrated tokens, NER error rates were 5.2x and 6.3x higher for GPT-4o and Qwen, respectively. This highlights how morphological integration remains a challenge. We release the corpus, annotations, and code to support future computational and sociolinguistic research on Turkish-English code-mixing.

---


### 190. [Re-calibrated Contrastive Loss for Transformation-Aware Prompt Conditioning in Vision-Language Models](https://arxiv.org/abs/2609.06967)

**<font color=#1a73e8>作者：</font>** Seungmin Oh, Seunghun Kang, Jongbin Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensuring effective transfer learning for vision-language models without compromising their generalization performance is crucial. However, many existing methods overlook data characteristics and simply reuse the training strategies adopted during pre-training. Specifically, they treat same-class samples as distinct instances and transform images independently of their paired text prompts, which makes model learning more difficult. We address these limitations through transformation-aware prompt conditioning and a re-calibrated contrastive loss. Fixed text descriptors identify the transformations applied to paired images, providing transformation-level consistency without altering class semantics. This design aligns the image and text branches at the transformation level, enabling richer representations while preserving the models' ability to generalize. In addition, our loss function mitigates positive-gradient dilution in soft-target cross-entropy when each anchor has multiple valid positives. During transfer, our approach treats same-class samples as positives rather than distinct instances, enabling the model to learn domain-specific features more effectively. Experiments across distribution shift, transfer learning, and few-shot settings demonstrate consistent improvements over existing approaches. Source code for our method is available at this https URL.

---


### 191. [CantoneseLLM v2: Reasoning in a Low-Resource Language](https://arxiv.org/abs/2609.06970)

**<font color=#1a73e8>作者：</font>** Tsz Chung Cheng, Chung Shing Cheng, Chaak Ming Lau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cantonese is widely spoken but remains low-resource in written data, with no large corpus of native Cantonese reasoning traces available for model training. We develop and release CantoneseLLM v2, comprising models based on Qwen3 8B and 30B-A3B. The models are trained through CPT on 784 million Cantonese and Hong Kong-related tokens, chat-vector merging, SFT, DPO, and RLVR. Evaluation across the training stages shows that chat-vector merging transfers instruction following but preserves the donor model's reasoning language, while SFT with limited Cantonese reasoning data substantially shortens or removes reasoning traces and reduces benchmark performance. DPO restores the reasoning-block format, particularly for the 8B model, but recovers only part of the lost performance. The RLVR training with Cantonese language and Traditional Chinese scripts as multiplicative constraints introduced Cantonese language alignment and restored the lost performance. The 30B-A3B model reaches 73.16 on HKCanto-Eval, within 1.20 points of its merged checkpoint, while retaining the Cantonese reasoning behaviour absent from that checkpoint. We release the model checkpoints, the training environments, and a thirteen-year Traditional Chinese Common Crawl dataset. The models can be accessed at this https URL

---


### 192. [AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories](https://arxiv.org/abs/2609.06972)

**<font color=#1a73e8>作者：</font>** Asif Pinjari, Mithun Paul Saint-Germain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents complete tasks by issuing sequences of tool calls, and every observation they read is a channel through which an indirect prompt injection can enter. A successful injection has a characteristic shape when the trajectory is read in order: a benign prefix gives way to actions that serve the attacker rather than the user. Existing benchmarks measure whether such attacks succeed against live agents, and existing guard models judge a trace as a whole; no public corpus labels, step by step, where an injection enters a trajectory and which steps it corrupts. We present AgentDrift, a benchmark of 12,536 synthetic tool-call trajectories over five agent domains in which every one of the 71,024 steps carries one of four labels: benign, injection point, hijacked, or failed injection. The corpus contains 4,000 benign, 5,536 attacked, 1,500 failed-attack, and 1,500 hard-negative trajectories; attacked trajectories follow three compliance patterns whose label strings obey a stated regular grammar. Failed attacks carry an injection the agent resisted, and hard negatives carry legitimate content that resembles an attack, so a detector must separate attempt from success and deviation from novelty. Trajectories were generated by a single open model under category-specific protocols, enforced by a closed-vocabulary structural validator, screened by an LLM judge, and audited by hand on 1,200 trajectories; we show that the LLM judge was itself fooled by the hard negatives. A surface-feature logistic regression recovers only 55.4% of attacks (F1 0.647), including only 8.2% of partial hijacks and 23.1% of delayed executions, so nearly half of the attacks require modeling the behavioral sequence. We measure template concentration, attack-goal-family collapse, and world-identity leakage in the generated data, and release the corpus with its documentation under CC BY 4.0.

---


### 193. [Train Overcomplete, Deploy Compact: Scaling Recovery Capacity for Structured LLM Pruning](https://arxiv.org/abs/2609.06974)

**<font color=#1a73e8>作者：</font>** Seungmin Oh, Donggeon Lee, Jongbin Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong performance across diverse tasks, but deployment remains costly because of memory, latency, and energy demands. Structured pruning reduces these costs by removing architectural components, yet its recovery stage is often limited by a mismatch between the recovery module's representational capacity and the complexity of the removed knowledge. We call this bottleneck the capacity-knowledge asymmetry and propose OverRep, an Overcomplete Reparameterization framework for structured LLM pruning. Following the principle of "train overcomplete, deploy compact", OverRep temporarily overparameterizes the recovery module during training to absorb complex knowledge distilled from the original model. After recovery, the overcomplete re-parameterization is algebraically merged into a mathematically equivalent compact module, preserving the pruned model's inference-time architecture and computational cost. OverRep further introduces an annealed activation that enables nonlinear training dynamics while converging to a linear regime for exact algebraic merging. Across three backbone families, OverRep improves retained reasoning performance over strong recovery baselines by up to 5.5 and 8.4 points at 25% and 50% pruning, respectively, while keeping memory usage and TFLOPs comparable to existing recovery methods. Our code is available at this https URL.

---


### 194. [HealthLoopQA: A Context-Aware Question Answering Benchmark for Interpreting Wearable Monitoring Data in Diabetes Care](https://arxiv.org/abs/2609.06976)

**<font color=#1a73e8>作者：</font>** Yuchen Niu, Yanan Ma, Srinivasan Nandakumar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As medical wearables become integrated into daily chronic disease care, effectively interpreting longitudinal monitoring data is essential for patients and clinicians to understand health trends, detect safety-critical events, and make informed decisions. While large language models (LLMs) show promise for transforming this streaming physiological data into personalized health insights, evaluating their reasoning capability and analytical rigor in diverse monitoring tasks remains a fundamental challenge. Existing medical wearable question answering (QA) benchmarks primarily assess short-horizon classification or statistical summaries, largely ignoring the long-term patterns, therapeutic and behavioural contexts, and potential system failures inherent in real-world deployments. To address this, we introduce HealthLoopQA, a comprehensive diagnostic benchmark for evaluating LLM reasoning over continuous diabetes monitoring data. Grounded in a novel taxonomy of eleven atomic reasoning abilities, HealthLoopQA comprises 127 tasks and over 1,500 QA instances spanning process mining, anomaly detection, and prediction over 30-day horizons. To systematically evaluate safety awareness, we complement real-world datasets with a fault-injected simulation testbed modeling diverse device malfunctions and cyber-physical attacks to generate physiologically plausible hazard scenarios. Evaluating state-of-the-art LLMs across prompting and agentic frameworks reveals severe limitations in complex temporal pattern mining. Furthermore, we identify a broader phenomenon of In-context Laziness under long-context prompting, highlighting critical open challenges in deploying LLMs for rigorous long-horizon medical reasoning.

---


### 195. [AnomalyCraft-700K: Component-Level Controllable and Verifiable Synthetic Anomalies for Fine-Grained Video Anomaly Understanding](https://arxiv.org/abs/2609.06978)

**<font color=#1a73e8>作者：</font>** Yuzhou Long, Haodong Zhang, Yunpeng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in video anomaly understanding (VAU) has long been limited by inherent deficiencies of real-world anomaly videos, which are hard to collect and offer little control over their content. Synthetic anomaly approaches partially alleviate data scarcity, yet their generation remains largely controlled at the category or prompt level. They also lack component-level verification of video-text consistency and provide insufficient hard normal samples near the normal-anomaly boundary. To address this, we present AnomalyCraft-700K, a component-controllable synthetic anomaly dataset for fine-grained VAU, containing over 40K videos and over 700K task-level textual annotations. From fine-grained semantic components and a progressive three-stage pipeline, we craft anomaly events that are richly detailed, semantically controlled, and temporally structured, and additionally construct per-category hard normal samples to prompt the model to discriminate based on anomaly semantics rather than surface visual cues. Moreover, using the components as verification units, AnomalyCraft-700K further performs component-wise correction of video-text discrepancies introduced during generation, providing reliable annotations with verified cross-modal alignment for six tasks that progress from anomaly detection, through anomaly retrieval and captioning, to fine-grained anomaly reasoning. Evaluations of widely used methods under both traditional and MLLM-based protocols demonstrate that AnomalyCraft-700K serves as an effective source of supervision, from anomaly detection to fine-grained anomaly understanding.

---


### 196. [Continual Learning Mechanisms Compose for Long-Horizon Memorization](https://arxiv.org/abs/2609.06986)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Alvin Zhang, Daniel Khashabi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models may need to internalize information that arrives over time and retain it through many subsequent updates. To study this challenge, we introduce long-horizon memorization, a setting in which a model learns 100 query-answer tasks through continual supervised fine-tuning without retaining earlier training examples or receiving task identifiers at inference. Sequential updates cause catastrophic forgetting, and no single continual learning mechanism we evaluate maintains strong retention at this horizon. We hypothesize that mechanisms addressing complementary sources of forgetting will be more effective when composed. We organize these compositions along two design dimensions. Data, function, and weight anchors specify what prior information each update should preserve, while low-rank allocation rules determine where successive updates are retained. To test this hypothesis systematically, we construct three distinct 100-task memorization datasets. We introduce task-level successive halving to search the combinatorial design space and use a factorial experiment to measure individual and interaction effects. Our best method combines all three anchors with merged LoRA, ranks among the top 3 methods in all datasets, and raises average final retention from 1.2% under naive sequential fine-tuning to 34.9%, a 28-fold improvement. The data anchor and merged LoRA provide the largest average gains and interact super-additively on all three datasets. Together, these results show that composing complementary mechanisms substantially improves long-horizon memorization beyond what any individual mechanism achieves.

---


### 197. [CGSM: Concept-Guided Segmentation Model for Precise Pulmonary Lesion Delineation](https://arxiv.org/abs/2609.07004)

**<font color=#1a73e8>作者：</font>** Changheng Lin, Wenjie Zhang, Yushan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of pulmonary lesions is essential for effective clinical diagnosis and treatment strategies. Existing segmentation approaches often lack task-specific semantic guidance, as text-based annotations typically offer coarse localization of lesions, leading to inadequate delineation of lesion boundaries and poor performance on small-scale lesions. To address this, we propose CGSM, a Concept-Guided Segmentation Model that integrates LLM-generated and clinically reviewed concepts into the segmentation process. Specifically, we design a Concept-Visual Alignment Module (CVAM) to activate relevant tokens within the concepts that align with visual features, enhancing the interaction between textual and visual information. In addition, we introduce a Concept Modulated Decoder (CM-Decoder), which uses concepts from CVAM as modulation signals to facilitate the adaptive fusion of image and text features, improving the segmentation accuracy. Extensive experiments on two public datasets show that CGSM achieves state-of-the-art performance, with results of 91.59% Dice and 84.49% mIoU on the QaTa-COV19 dataset, demonstrating its effectiveness in pulmonary lesion segmentation.

---


### 198. [GIFT: Goal-Injected Fine-Tuning for Efficient Manipulation Policy Adaptation](https://arxiv.org/abs/2609.07006)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Fang, Shuo Feng, Yuxuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compared with relying solely on initial observations and language instructions, predicting goal images with generative models as high-level visual guidance can significantly enhance the robustness of Vision-Language-Action (VLA) models. However, most existing foundation models have not systematically incorporated goal image conditioning due to the high computational training cost. To this end, we propose Goal-Injected Fine-Tuning (GIFT), a lightweight and efficient fine-tuning framework that seamlessly integrates generated goal images into multiple representative pretrained VLA models. Our approach introduces goal image features into observations via a zero-initialized convolution which progressively grows parameters from zero and prevents harmful noise from disrupting the pretrained policy during fine-tuning. As training proceeds, goal information is gradually incorporated, enabling efficient goal understanding without disrupting model stability. We further introduce a refined image editing method to generate semantically and visually consistent goal images from initial observations and task instructions. Experiments show that goal-aware VLA models achieve substantial performance gains across tasks: with only a single epoch of fine-tuning, GIFT outperforms the base model by 6.0% and 13.4% on two SIMPLER settings, and by 4.7% on LIBERO, demonstrating both efficiency and effectiveness.

---


### 199. [RedKnot-MLA: Multi-Head Offline-Online Reuse for DeepSeek-V4 Long-Context Serving](https://arxiv.org/abs/2609.07008)

**<font color=#1a73e8>作者：</font>** Yang Liu, Zhaokai Luo, Huayi Jin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-head latent attention (MLA) exposes many logical query heads through one packed latent KV stream. This representation is memory efficient, but it removes the physical per-head cache boundary assumed by conventional head-wise reuse. We present our system, a DeepSeek-V4 realization of RedKnot's head-aware reuse principle. Each immutable document is processed offline at canonical position zero; certified Local-head contributions are retained as MLA-Off. At serving time, query-side RoPE relocation restores the document's request position, a small Global-head set and protected Local token rows are recomputed as MLA-Online, and the two paths are merged before a single shared output projection. The packed MLA latent is never split. DeepSeek-V4-Flash uses 37 reusable layers and a 56/8 Local/Global partition, giving a 75.29% analytic logical head-row ceiling; the Pro-0813 profile uses 55 layers and 112/16 heads, giving 78.89%. Frozen Flash operating points show hot-artifact TTFT speedups of 2.02-3.84x. At 256K, the archived three-dataset study reports an aggregate F1 change of +3.24 percentage points, an EM change of +4.16 points, and a 78.7-79.5% analytic major-operator arithmetic saving, while one dataset decreases by 2.81 F1 points. A separate author-reported 256K hot-artifact QPS measurement is approximately 2.0x; because its raw concurrency trace is not included in this bundle, we mark it as preliminary rather than archived evidence. We describe the factorization, position repair, token-row closure, sparse-MoE support, TP8 integration, and the measurement boundaries needed to interpret these results.

---


### 200. [LoGAN: Multilingual Font Localization with Generative Agents](https://arxiv.org/abs/2609.07029)

**<font color=#1a73e8>作者：</font>** Zhuoning Yuan, Ta-Ying Cheng, Benjamin Klein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing a font into new languages is a highly intricate task requiring precise design adaptation of glyphs, color/texture, and spacing/kerning, from source to target languages. Most existing methods focus on single glyph generation with limited capability in handling multilingual font rendering. In this work, we propose LoGAN, a VLM-based agentic framework for few-shot multilingual font localization, which takes in a small number of individual glyphs from a font or letters from a logo and uses them to generate complete character sets in other languages. LoGAN breaks down this task into multiple components: a glyph-level diffusion model, a style finetuning module, a spacing and kerning transfer algorithm, and a texture expansion model, with a VLM agent coordinator. LoGAN achieves broad language coverage for font localization with various styles, including Chinese/Korean/Japanese (CJK). We evaluate our approach on both font and real-world logo datasets spanning more than 27 languages and compare it against both specialized font generation and state-of-the-art image editing models with strong text rendering capabilities (e.g., FLUX, Nano-Banana). Our approach yields higher glyph fidelity while maintaining better style, texture, and kerning consistency according to both quantitative and qualitative evaluations.

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
