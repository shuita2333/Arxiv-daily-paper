# 🔐 大模型安全相关研究 | 2026年08月19日

> 本类共 **10** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [LLM Safety Alignment in Low-Resource Languages: A Systematic Literature Review](https://arxiv.org/abs/2608.14626)

**<font color=#1a73e8>作者：</font>** Valdini Douglace Lemofouet, Blessing Ngozi Uzor, Paula Chikaodinaka Anyanwu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved substantial progress in safety alignment, yet their safety guarantees remain significantly weaker in low-resource and multilingual settings than in high-resource languages. In this paper, we conduct a Systematic Literature Review (SLR) of LLM safety alignment in low-resource languages by adopting the PRISMA 2020 methodology. Out of roughly 1,500 papers identified from Semantic Scholar, arXiv, and OpenAlex, 50 relevant studies have been selected and analyzed. Our review is organized around four themes: safety alignment methods, multilingual safety risks, evaluation benchmarks, and cross-lingual transferability. We further propose a taxonomy of safety alignment approaches based on three adaptation mechanisms: data adaptation, objective optimization, and mechanistic alignment. Across literature, translated English benchmarks fail to sufficiently represent culturally rooted harms, and multilingual models are more vulnerable to cross-lingual jailbreaks, code-switching attacks, and safety degradation in underrepresented languages. These failures are driven by several key factors, including uneven multilingual pre-training coverage, insufficient native-language preference data, poor transfer of safety representations, and a lack of culturally aware evaluation frameworks. The review also notes that many low-resource languages, especially African languages, have fewer safety benchmarks available than other multilingual regions. Overall, the results reveal a persistent multilingual safety gap, and suggest that future progress will require culturally grounded benchmarks, participatory data collection, balanced multilingual pre-training, and scalable multilingual alignment methods.

---


### 2. [Inference-Time Mitigation of Adversarial Political Bias in Large Language Models](https://arxiv.org/abs/2608.14629)

**<font color=#1a73e8>作者：</font>** Tejaswi V. Panchagnula, Bruce Coburn, Bryce J. Dietrich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become the mainstay for information retrieval and summarization tasks, ensuring that they are always non-partisan and invulnerable to political bias is a critical step towards safer and more trustworthy Artificial Intelligence (AI). Current model alignment paradigms, such as reinforcement learning from human feedback (RLHF), make LLMs follow overarching safety instructions. However, this instruction tuning can be exploited via adversarial prompt injection and be used to generate unsafe content. In particular, political bias has not been specifically targeted by modern alignment techniques as harmful and biased content. To address this vulnerability of LLMs, we propose mitigation strategies using Chain of Thought (CoT) prompting and Direct Preference Optimization (DPO). Using a public dataset of legislative videos, we generate summaries using LLMs, inject bias via adversarial prompting and evaluate their performance on a four axis scale designed for political summarization. In this paper, we present different methods to shield LLMs against the injection of political bias. Our results demonstrate that the proposed Recursive Self-Correction approach raises model performance from a Political Neutrality Likert scale baseline of 2.14 to 4.56, averaged across all models, demonstrating effective inference-time mitigation of political bias in LLM-generated summaries.

---


### 3. [Workspace Topology as an Attack Vector in Agentic Coding Assistants](https://arxiv.org/abs/2608.14876)

**<font color=#1a73e8>作者：</font>** Alexandre G.R. Day, Pradeep Yadlapalli, Sriram Venkatapathy 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic coding assistants are finding widespread use, not just in new code development but in quickly ingesting and leveraging third-party code. This opens up a risk of malicious code being ingested as these coding tools operate with broad filesystem access inside developer workspaces. In this paper, we extensively study the impact of different dimensions of a novel attack surface we term workspace topology -- defined via directory depth, codebase modularity, in-file injection position and context framing -- on the attack success rate of adversarial prompt injection attempts.
We perform an empirical study of indirect prompt injection (IPI) across a diverse set of open-source repositories spanning 10 languages and 6 engineering domains, evaluating three IPI entry points against open-weight models operating open source code harnesses.
We find that workspace topology measurably affects IPI success. Specifically, changes in codebase modularity can significantly alter the Attack Success Rate (ASR), with highly modular environments demonstrating significantly lower attack success rates. Furthermore, context framing and introduction of security-cues in the workspace can also alter the ASR. Our findings offer practical value for the evaluation and security testing of coding agents across diverse settings, while underscoring the importance of an uncontaminated testing environment to obtain reliable results and conclusions.

---


### 4. [Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish](https://arxiv.org/abs/2608.15392)

**<font color=#1a73e8>作者：</font>** Madhusudhanan G  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought monitoring is a potentially useful safety signal, but its reliability across languages and behavioral settings remains uncertain. In a small case study of eight manually verified synthetic scenarios, one model, one annotator, and one deterministic generation seed, I study API-visible reasoning during indirect prompt injection in Sarvam-105B across English, Tamil, and Tanglish. A four scenario pilot found 5/12 injected attack successes without reasoning and 1/11 with reasoning. A preregistered four-scenario follow-up reversed that direction, finding 2/12 attacks without reasoning and 3/12 with reasoning. With only four scenarios per phase, this design cannot distinguish a real reasoning-mode effect from prompt-specific variation or sampling noise. Across 20 non-empty injected-thinking traces, all 17 benign-correct outputs stated an intent to ignore the injection, while all three attack successes stated an intent to follow it. These descriptive observations provide a reproducible case study of behaviorally informative visible reasoning when it is available; they do not establish that reasoning mode improves safety, that visible reasoning is mechanistically faithful, or that the findings generalize beyond this configuration.

---


### 5. [TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation](https://arxiv.org/abs/2608.15594)

**<font color=#1a73e8>作者：</font>** Md Messal Monem Miah, Adrita Anika, Zhiyuan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks have emerged as a critical safety threat to LLMs, as harmful objectives are decomposed across a sequence of apparently benign turns to bypass guardrails. Existing defenses lack the reasoning capacity to identify evolving manipulation patterns, often trading helpfulness for safety by over-refusing benign requests related to sensitive topics. We introduce Trace, a multi-turn defense with trajectory-aware structured reasoning. Before generating each response, the model identifies manipulation cues from the trajectory, evaluates both the benign and adversarial interpretations of user intent, assigns a jailbreak score, and commits to an action: Allow, Caution, or Decline. We curate 4k multi-turn adversarial conversations from five attack frameworks, pair them with 2.4k benign dialogs, and 600 sensitive-but-benign conversations. We train Llama-3.1-8B-Instruct with SFT and GRPO under a multi-component reward that jointly optimizes helpfulness on benign prompts and robustness against jailbreak attempts. Across seven multi-turn attack benchmarks, Trace attains an average attack success rate (ASR) of 14.5% against 31.4% for the strongest baseline and 74.9% for the undefended target, while significantly raising the attacker effort required per successful jailbreak. Trace also balances usability and safety, achieving a 93.3% average compliance on over-refusal benchmarks.

---


### 6. [PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails](https://arxiv.org/abs/2608.15673)

**<font color=#1a73e8>作者：</font>** Satchit Chatterji, Shihan Wang, Giovanni Sileno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with harmful prompts, or refusals to assist benign ones. To separate grounding and reasoning roles, we propose PL-Guard, a neurosymbolic guardrail architecture. Using a symbolic policy interface consisting of predicates and ProbLog rules, a local LLM grounds prompt-response pairs into predicate probabilities using renormalized True/False token scores, while ProbLog performs explicit probabilistic rule inference over the symbolic policy. On the XSTest benchmark, an offline Qwen-based evaluator finds that PL-Guard with a hand-curated policy reduces unsafe compliance from 22.0% for the base model to 0.5%, and below the 6.0% rate of an LLM-as-a-judge baseline. This comes at the cost of higher over-refusal than the LLM-as-a-judge baseline, 14.4% versus 5.2%. These results suggest that separating neural grounding from probabilistic symbolic reasoning can expose the safety-helpfulness tradeoff while making the guardrail's intermediate reasoning steps explicit and auditable.

---


### 7. [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](https://arxiv.org/abs/2608.16393)

**<font color=#1a73e8>作者：</font>** Zonghao Ying, Xiangfan Wu, Huiyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content channels, text and file carrier modes, 35 payload objectives, one unmodified baseline, and 12 attack methods. The experiment preserves DSH's agent loop, tool registry, model adapter, and session-event path; source tools and sensitive sinks are local fixtures, so attempted actions are recorded without external side effects. We evaluate each trace with a deterministic rule-based judge, \JudgeR{} (RuleJudge), and a semantic LLM-based judge, \JudgeL{} (LLMJudge). The strongest observed attack success rates are 17.0% under \JudgeL{} for fake-completion attack in text mode, 25.5% under \JudgeR{} for hidden Unicode in file mode, and 16.0% under \JudgeR{} for the skills channel in file mode. \JudgeL{} also assigns partial compliance more often than \JudgeR{} (7.3% versus 2.0%). We relate these results to DSH's treatment of tool results, additional contexts, and tool-call policy hooks, then identify controls that should sit between untrusted content and sensitive actions. Our code is available at this https URL.

---


### 8. [JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills](https://arxiv.org/abs/2608.16465)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wen, Jiajia Li, Zhida He 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated red-teaming has produced a growing collection of attack strategies, yet they typically remain scattered across prompts and workflows, making them difficult to systematically integrate, reuse, and improve at scale. We introduce \textsc{JailbreakSkill}, a skill-centric framework for scaling automated red-teaming through reusable and continuously evolving attack capabilities. \textsc{JailbreakSkill} packages existing attack strategies into modular, agent-ready skills that can be directly reused and adaptively selected across tasks and target models. Beyond reuse, it closes the loop between attacking and learning: attack experience is used to diagnose, refine, combine, and discover new skills, which are added back to an ever-growing skill library. This evolution lifts macro-average ASR by 17.5 percentage points on AdvBench and 13.4 points on HarmBench, including a 48.6-point gain against GPT-5.4 on AdvBench, while yielding novel attack strategies such as reframing a direct request as an unfinished document-completion task. Several evolved skills also generalize to unseen prompts and target models without further adaptation. Our code is available at this https URL.

---


### 9. [DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption](https://arxiv.org/abs/2608.16536)

**<font color=#1a73e8>作者：</font>** Chang Liu, Yuni Lai, Mingyue Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Retrieval Augmented Generation (M-RAG) is increasingly vulnerable to adversarial attacks where malicious data are crafted to produce embeddings that align with benign entries in the vector space, deceiving retrieval and inducing harmful outputs. Existing defenses primarily operate at query time, relying on auxiliary detectors, similarity re-ranking, or feature-consistency checks. However, these approaches suffer from non-trivial inference overhead, generalize poorly to unseen attack strategies, and often assume specific attack distributions. To address this, we propose DSPrompt, a Dynamic Soft Prompt defense framework that directly reshapes the retriever's embedding semantics, without modifying the retrieval pipeline. It inserts few learnable soft prompts into each layer of the visual and textual encoders of a frozen retriever, utilizing a shallow-to-deep length schedule that is adaptive to the capacity in the model layers. These prompts are trained under a dynamic min-max scheme: an online multimodal attacker continually crafts hard adversarial documents against the current retriever, while the defender is updated to push such documents out of the top-k while preserving the ranking and diversity of benign evidence. Because the defended encoder can be pre-computed and indexed exactly as in standard dense retrieval, DSPrompt incurs no additional per-query optimization and introduces fewer than 1% additional parameters. Extensive experiments across four benchmarks and three representative poisoning attacks show that DSPrompt substantially reduces the attack success rate and poison retrieval rate while maintaining near-lossless retrieval utility and generation fidelity, consistently outperforming existing defense baselines at a fraction of their computational cost.

---


### 10. [BabelSteering: Multilingual Safety Alignment via English Steering Vectors](https://arxiv.org/abs/2608.16577)

**<font color=#1a73e8>作者：</font>** Emma V. Stein, Dominik Meier, Terry Ruas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are deployed globally in high-stakes settings, yet most safety research and alignment efforts remain concentrated on English. Thus, users interacting with LLMs in other languages may encounter weaker safeguards despite relying on the same systems for similarly sensitive tasks. In this work, we investigate whether safety signals learned from a high-resource language, like English, can improve multilingual safety. We propose BabelSteering, an activation steering method that acts as a lightweight inference- time intervention, using refusal directions derived from English safety supervision to generalize across languages. Our evaluation includes eight languages and jointly measures refusal of harmful requests, over-refusal, and general task utility. The results show that BabelSteering increases the refusal of harmful requests across languages, with only a marginal to no reduction in task utility but with some increase in refusal of pseudo-harmful prompts. For example, for Gemma 7B, we see an average increase in the refusal of harmful prompts across languages of 11 percentage points (pp), with individual languages like Bengali seeing an increase of 17 pp, with no loss of utility on Global MMLU, while pseudo-harmful refusals increase by 13 pp on average. We also introduce a multilingual translation-and-evaluation pipeline to facilitate future work on cross-lingual safety interventions. Overall, our findings suggest that activation steering may provide a practical, low- cost mechanism for extending English-derived safety signals to other languages. Warning: this paper contains examples with unsafe content

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
